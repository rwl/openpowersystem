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

""" The parts of a power system that are physical devices, electronic or mechanical 
"""

# <<< imports
# @generated
from ucte.core.identified_object import IdentifiedObject

from ucte.core.equipment_container import EquipmentContainer


from google.appengine.ext import db
# >>> imports

class Equipment(IdentifiedObject):
    """ The parts of a power system that are physical devices, electronic or mechanical 
    """
    # <<< equipment.attributes
    # @generated
    # Indicates if the equipment is real equipment (false) or an equivalent. If this is missing, it is assumed to be False.  It is required for Equipment connected to the X-Node. All classes derived from Equipment are to include this attribute except for the TransformerWinding class.     For transformers the PowerTransformer class will be used to specify the real or equivalent status and the contained TransformerWinding class instances need not and should not specify this attribute. 
    equivalent = db.BooleanProperty(default=False)

    # >>> equipment.attributes

    # <<< equipment.references
    # @generated
    # The association is used in the naming hierarchy. For a TransformerWinding and ACLineSegment, the association Equipment.MemberOf_EquipmentContainer is not used.  The TransformerWinding instance is instead contained within a PowerTransformer unless the association refers to a different substation than what is used in the PowerTransformer association.  
    member_of_equipment_container = db.ReferenceProperty(EquipmentContainer,
        collection_name="contains_equipments")

    # >>> equipment.references

    # <<< equipment.operations
    # @generated
    # >>> equipment.operations

# EOF -------------------------------------------------------------------------
