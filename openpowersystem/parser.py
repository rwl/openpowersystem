#------------------------------------------------------------------------------
# Copyright (C) 2009 Richard W. Lincoln
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation; version 2 dated June, 1991.
#
# This software is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANDABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#------------------------------------------------------------------------------

""" Defines sinks for use with rdfxml.py by Sean Palmer.
"""

import os
import re
import sys
import gzip
import bz2
import zipfile
import logging

from google.appengine.ext import db

import rdfxml

from ucte_pkg_map import ucte_pkg_map
#from cpsm_pkg_map import cpsm_pkg_map
#from cdpsm_pkg_map import cdpsm_pkg_map

pkg_map = {"ucte": ucte_pkg_map}#, "cpsm": cpsm_pkg_map, "cdpsm": cdpsm_pkg_map}

from ucte import ns_uri as ns_ucte
#from cpsm import ns_uri as ns_cpsm
#from cdpsm import ns_uri as ns_cdpsm

ns_map = {"ucte": ns_ucte}#, "cpsm": ns_cpsm, "cdpsm": ns_cdpsm}

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG,
    format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

#------------------------------------------------------------------------------
#  "AttributeSink" class:
#------------------------------------------------------------------------------

class AttributeSink(object):
    """ Uses triples from the RDF parser to populate a dictionary that maps
        rdf:IDs to objects.  The objects are instantiated and their attributes
        are set, but any references are not.  This is done with a second pass
        using a CIMReferenceSink that is passed this sink.
    """

    def __init__(self, pkg):
        self.uri_object_map = {}
        self.pkg_map = pkg_map[pkg]
        self.ns_cim = rdfxml.Namespace(ns_map[pkg])

        # Convertor from camel case to lowercase underscore separated.
        self.under = _CamelToLowercaseUnderscore()


    def triple(self, sub, pred, obj):
        """ Handles triples from the RDF parser.
        """
        ns_sub,  frag_sub  = splitURI(sub)
        ns_pred, frag_pred = splitURI(pred)
        ns_obj,  frag_obj  = splitURI(obj)

        # Instantiate an object if the predicate is an RDF type and the object
        # is in the CIM namespace.
        if (ns_pred == rdfxml.rdf) and \
            (frag_pred == "type") and \
            (ns_obj == self.ns_cim):

            cls_name = frag_obj
            uri      = frag_sub

            if self.pkg_map.has_key(cls_name):
                # It is fairly cheap to import an already imported module.
                module_name = self.pkg_map[cls_name]

                logger.debug("Class [%s] located [%s]." %
                    (cls_name, module_name))

                exec "import %s" % module_name
                element = eval("%s.%s(uri=uri)" % (module_name, cls_name))

                if hasattr(element, "m_rid"):
                    element.m_rid = uri
            else:
                logger.error("Module for '%s' not located." % cls_name)

            # Map the element according to its URI.
            self.uri_object_map[uri] = element

            element.put()

        # If the predicate is in the CIM namespace the triple is specifying
        # an attribute or a reference.
        elif ns_pred == self.ns_cim:
            # The URI of the object with the attribute being set.
            uri = frag_sub
            # Strip the double quotes that rdfxml.py adds to literals.
            value = ns_obj.strip('"')

            # Split the class name and the attribute name.
            class_name, camel_attr_name = frag_pred.rsplit(".", 1)
            attr_name = self.under(camel_attr_name)
#            logger.debug("Attempting to set '%s' for '%s' to '%s'." %
#                (attr_name, class_name, value))

            # Retrieve the object from the URI map.
            if self.uri_object_map.has_key(uri):
                element = self.uri_object_map[uri]
            else:
                logger.error("Element [%s] not found." % uri)
                return

            if not hasattr(element, attr_name):
                logger.error("Element [%s] has no attribute: %s" %
                    (element.__class__.__name__, attr_name))
                return

            prop = element.properties()[attr_name]

            logger.debug("Model property: %s" % prop.__class__.__name__)

            logger.debug("ReferenceProperty: %s" %
                         isinstance(prop, db.ReferenceProperty))
#            logger.debug("StringProperty: %s" %
#                         isinstance(prop, db.StringProperty))
#            logger.debug("FloatProperty: %s" %
#                         isinstance(prop, db.FloatProperty))
#            logger.debug("BooleanProperty: %s" %
#                         isinstance(prop, db.BooleanProperty))

            # Leave references until the second pass.
            # FIXME: Use isinstance(prop, db.ReferenceProperty)
            if prop.__class__.__name__ != "ReferenceProperty":
                default = prop.default_value()

                if default is not None:
#                    logger.debug("Default value of '%s'." % default)
                    # Coerce the value according to the type of the default.
                    default_type = type(default)
                    value = default_type(value)
                else:
                    logger.error("No default value [%s]." % attr_name)
                    return
            else:
                return

            # TODO: Handle enumerations where the 'object' in the triple is the
            # URL for the data type and the value must be split of the end of
            # the fragment.
            # value = frag_obj.rsplit(".", 1)[1]

#            logger.debug("Setting '%s' attribute '%s' to: %s %s" %
#                (element.__class__.__name__, attr_name, str(value),
#                 type(value)))

            setattr(element, attr_name, value)

#------------------------------------------------------------------------------
#  "ReferenceSink" class:
#------------------------------------------------------------------------------

class ReferenceSink(object):
    """ Handles setting the references for a CIM.
    """

    def __init__(self, attr_sink):
        assert isinstance(attr_sink, AttributeSink)

        # The sink used in the first pass.
        self.attr_sink = attr_sink

#        self.pkg_map = self.attr_sink.pkg_map
        self.ns_cim = self.attr_sink.ns_cim
        # Map of URIs to model elements from the first pass.
        self.uri_map = self.attr_sink.uri_object_map

        # Convertor from camel case to lowercase underscore separated.
        self.under = _CamelToLowercaseUnderscore()


    def triple(self, sub, pred, obj):
        """ Handles triples from the RDF parser.
        """
        ns_pred, frag_pred = splitURI(pred)
        ns_obj,  obj_uri   = splitURI(obj)

        # If the predicate is in the CIM namespace, the triple is specifying
        # an attribute or a reference.
        if ns_pred == self.ns_cim:
            ns_sub, uri_subject = splitURI(sub)

            # Try to get the object with the reference being set.
            if self.uri_map.has_key(uri_subject):
                sub_obj = self.uri_map[uri_subject]
            else:
                logger.error("Referencing object [%s] not found." %
                    uri_subject)
                return

            # Split the predicate fragment into class name and attribute name.
            class_name, camel_ref_name = frag_pred.rsplit(".", 1)
            ref_name = self.under(camel_ref_name)
            # Assert that the object from the dictionary has the same type as
            # that specified in the predicate.
#            assert sub_obj.__class__.__name__ == class_name

#            logger.debug("Trying to set the '%s' reference of '%s' to: '%s'" %
#                (ref_name, class_name, ref_name))

            # Get the attribute object so the type can be determined.
#            trait = sub_obj.trait( ref_name )
            if not hasattr(object, ref_name):
                logger.error("Object [%s] has no reference: %s" %
                    (sub_obj.__class__.__name__, ref_name))
                return

            # Try to get the object being referenced.
            if uri_map.has_key(obj_uri):
                ref_obj = self.attr_sink.uri_object_map[obj_uri]
            else:
                logger.error("Referenced object [%s] not found." % obj_uri)
                return


            logger.debug("Setting the '%s' reference of '%s' to: %s" %
                (ref_name, sub_obj, ref_obj))

            setattr(sub_obj, ref_name, ref_obj)

            # One to many and many to many references (List(Instance)).
#            elif trait.is_trait_type( List ) and \
#                trait.inner_traits[0].is_trait_type( Instance ):
#
#                logger.warning("Skipping multiplicity-many reference.")

#------------------------------------------------------------------------------
#  "Parser" class:
#------------------------------------------------------------------------------

class Parser(object):
    """ Reads CIM RDF/XML data files and returns a dictionary that maps
        unique resource identifiers to CIM object instances.
    """

    def __init__(self, profile, pwd=None):
        """ Initialises a new CIMReader instance.
        """
        # CIM profile to which the data conforms.
        self.profile = profile
        # Password used for encrypted zip files.
        self.pwd = pwd


    def parse(self, filename):
        """ Parses an RDF/XML file and returns a model containing CIM elements.
        """
        # Split the extension from the pathname
        root, extension = os.path.splitext(filename)

        if isinstance(filename, file):
            s = filename.read()
        elif extension in [".xml"]:
            fd = None
            try:
                fd = open(filename, "rb")
                s = fd.read()
            except:
                logger.error("Error reading XML data file.")
            finally:
                if fd is not None:
                    fd.close()
        else:
            s = filename

        # Instantiate CIM objects and set their attributes.
        attr_sink = AttributeSink(self.profile)
#        logger.debug("Parsing objects and attributes in: %s" % filename)
        rdfxml.parseRDF(s, base=filename, sink=attr_sink)

        # Second pass to set references.
        ref_sink = ReferenceSink(attr_sink)
#        logger.debug("Starting second pass to set references.")
#        rdfxml.parseRDF(s, base=filename, sink=ref_sink)

        # Return a map of unique resource identifiers to CIM objects.
        return attr_sink.uri_object_map

#------------------------------------------------------------------------------
#  "splitURI" function:
#------------------------------------------------------------------------------

def splitURI(uri):
    """ Splits the fragment from an URI and returns a tuple.

        For example:
            <http://www.w3.org/1999/02/22-rdf-syntax-ns#type>
        returns:
            ('http://www.w3.org/1999/02/22-rdf-syntax-ns#', 'type')

            http://www.github.com/rwl/pylon
        returns:
            (http://www.github.com/rwl/pylon, "")
    """
    if (uri[0] == "<") and (uri[-1] == ">"):
        uri = uri[1:-1]

    head, sep, tail = uri.rpartition("#")
    if head and sep:
#        logger.debug("Partitioned URI: '%s', '%s'." % (head + sep, tail))
        return (head + sep, tail)
    else:
#        logger.debug("URI [%s] has no end fragment." % uri)
        return (tail, "")

#------------------------------------------------------------------------------
#  "_CamelToLowercaseUnderscore" callable:
#------------------------------------------------------------------------------

class _CamelToLowercaseUnderscore(object):
    """ Simple functor class to convert names from CamelCase to
        lowercase underscore separated names.
    """
    def __call__(self, name):
        s = ""
        for i, c in enumerate(name):
            if i > 0:
                next = "a"
                if i < len(name) - 1:
                    next = name[i + 1]
                prev = name[i - 1]

                if c.isupper() and (prev != "_") and (not prev.isupper()):
                    s += "_"
            s += c.lower()

        return s

# EOF -------------------------------------------------------------------------
