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
from ucte.element import Element



from google.appengine.ext import db
# >>> imports

class IdentifiedObject(Element):
    """ This is a root class to provide common naming attributes for all classes needing naming attributes 
    """
    # <<< identified_object.attributes
    # @generated
    # The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. 
    description = db.StringProperty(default='')

    # The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy. This attribute is required on all instances in this Profile that inherit from IdentifiedObject except for the following Classes: 1) BaseVoltage; 2) Terminal; 3) TransformerWinding; 4) RatioTapChanger; 5) PhaseTapChanger; 6) OperationalLImitSet; 7) CurrentLimit; and, 8) VoltageLimit. 
    name = db.StringProperty(default='')

    # The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy. In the UCTE profile the aliasName is used to hold the EIC code.    The code length is 16 characters.    Not all CIM classes have an EIC code so the attribute is optional.    
    alias_name = db.StringProperty(default='')

    # >>> identified_object.attributes

    # <<< identified_object.references
    # @generated
    # >>> identified_object.references

    # <<< identified_object.operations
    # @generated
    # >>> identified_object.operations

# EOF -------------------------------------------------------------------------
