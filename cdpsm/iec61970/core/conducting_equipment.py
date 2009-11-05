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
from cdpsm.iec61970.core.equipment import Equipment

from cdpsm.iec61970.core.base_voltage import BaseVoltage

from cdpsm.iec61970.core import PhaseCode

from google.appengine.ext import db
# >>> imports

class ConductingEquipment(Equipment):
    """ The parts of the power system that are designed to carry current or that are conductively connected therewith. ConductingEquipment is contained within an EquipmentContainer that may be a Substation, or a VoltageLevel or a Bay within a Substation. 
    """
    # <<< conducting_equipment.attributes
    # @generated
    # Describes the phases carried by a conducting equipment. 
    phases = PhaseCode

    # >>> conducting_equipment.attributes

    # <<< conducting_equipment.references
    # @generated
    # Virtual property. ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes 
    pass # terminals

    # Use association to ConductingEquipment only when there is no VoltageLevel container used. 
    base_voltage = db.ReferenceProperty(BaseVoltage,
        collection_name="conducting_equipment")

    # >>> conducting_equipment.references

    # <<< conducting_equipment.operations
    # @generated
    # >>> conducting_equipment.operations

# EOF -------------------------------------------------------------------------
