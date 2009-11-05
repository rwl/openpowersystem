#------------------------------------------------------------------------------
# Copyright (C) 2009 Richard Lincoln
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the Free
# Software Foundation; version 2 dated June, 1991.
#
# This software is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANDABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#------------------------------------------------------------------------------

""" This is a root class to provide common naming attributes for all classes needing naming attributes 
"""

# <<< imports
# @generated
from cdpsm.element import Element



from google.appengine.ext import db
# >>> imports

class IdentifiedObject(Element):
    """ This is a root class to provide common naming attributes for all classes needing naming attributes 
    """
    # <<< identified_object.attributes
    # @generated
    # A Model Authority issues mRIDs. Given that each Model Authority has a unique id and this id is part of the mRID, then the mRID is globally unique. This attribute is only used when generating XSD Profiles.  For RDF Profiles, the RDF ID is used. 
    m_rid = db.StringProperty()

    # The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. 
    description = db.StringProperty()

    # The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy. 
    name = db.StringProperty()

    # The localName is a human readable name of the object. It is only used with objects organized in a naming hierarchy. The simplest naming hierarchy has just one parent (the root) giving a flat naming hierarchy. However, the naming hierarchy usually has several levels, e.g. Substation, VoltageLevel, Equipment etc. Children of the same parent have names that are unique among them. If the uniqueness requirement cannot be met IdentifiedObject.localName shall not be used, use IdentifiedObject.name  instead. 
    local_name = db.StringProperty()

    # The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy. 
    alias_name = db.StringProperty()

    # >>> identified_object.attributes

    # <<< identified_object.references
    # @generated
    # >>> identified_object.references

    # <<< identified_object.operations
    # @generated
    # >>> identified_object.operations

# EOF -------------------------------------------------------------------------
