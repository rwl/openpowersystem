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

""" An attribute from the associated PowerSystemResource is used.   This is like reflection into the UML model as one must name the paramter the same as the CIM name of the desired attribute. Such parameters are not important for completely standard models as the relation to the CIM attributes is fixed.  This object is required for user defined models that use attributes already existing on the PowerSystemResource or its derived classes.   Using this class avoids creating new paramter instances (with values) when we already have the values as class attributes of the associated PowerSystemResource.   Standard block models might optinally use objects of this class to convey information about the internals of the standard block. 
"""

# <<< imports
# @generated
from dynamics.dynamics.meta_block_parameter import MetaBlockParameter



from google.appengine.ext import db
# >>> imports

class AttributeBlockParameter(MetaBlockParameter):
    """ An attribute from the associated PowerSystemResource is used.   This is like reflection into the UML model as one must name the paramter the same as the CIM name of the desired attribute. Such parameters are not important for completely standard models as the relation to the CIM attributes is fixed.  This object is required for user defined models that use attributes already existing on the PowerSystemResource or its derived classes.   Using this class avoids creating new paramter instances (with values) when we already have the values as class attributes of the associated PowerSystemResource.   Standard block models might optinally use objects of this class to convey information about the internals of the standard block. 
    """
    # <<< attribute_block_parameter.attributes
    # @generated
    # The name of the attribute in the information model. This could be any attribute of the derived class of the power system resource for which the block is intended to be used.  For example, if the one were using the xxx attribute from Generator class, one would specifiy this attribute as 'xxx'.  This would also limit the block to only those classes which have an 'xxx' attribute.  This attribute could be replaced by using the inherited IdentifiedObject.name value for the purpose described above. 
    attribute_name = db.StringProperty()

    # >>> attribute_block_parameter.attributes

    # <<< attribute_block_parameter.references
    # @generated
    # >>> attribute_block_parameter.references

    # <<< attribute_block_parameter.operations
    # @generated
    # >>> attribute_block_parameter.operations

# EOF -------------------------------------------------------------------------
