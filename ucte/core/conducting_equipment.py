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

""" The parts of the power system that are designed to carry current or that are conductively connected therewith. ConductingEquipment is contained within an EquipmentContainer that may be a Substation, or a VoltageLevel or a Bay within a Substation. 
"""

# <<< imports
# @generated
from ucte.core.equipment import Equipment

from ucte.core.base_voltage import BaseVoltage


from google.appengine.ext import db
# >>> imports

class ConductingEquipment(Equipment):
    """ The parts of the power system that are designed to carry current or that are conductively connected therewith. ConductingEquipment is contained within an EquipmentContainer that may be a Substation, or a VoltageLevel or a Bay within a Substation. 
    """
    # <<< conducting_equipment.attributes
    # @generated
    # >>> conducting_equipment.attributes

    # <<< conducting_equipment.references
    # @generated
    # Use association to ConductingEquipment only when there is no VoltageLevel container used. The profile requires a BaseVoltage associaton on ConductingEquipment subtypes of classes ACLineSegment and TransformerWinding. The association is not used for any other subtypes. 
    base_voltage = db.ReferenceProperty(BaseVoltage,
        collection_name="conducting_equipment")

    # Virtual property. ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes  
    pass # terminals

    # >>> conducting_equipment.references

    # <<< conducting_equipment.operations
    # @generated
    # >>> conducting_equipment.operations

# EOF -------------------------------------------------------------------------
