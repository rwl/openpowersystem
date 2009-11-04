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

""" Collection of BaseVoltages which is used to verify that the BusbarSection.BaseVoltage and other voltage attributes in the CIM are given a value existing in the collection. The profile requires a BaseVoltage associaton on ConductingEquipment subtypes of classes ACLineSegment and TransformerWinding. The association is not used for any other subtypes. The base voltage of the TopologicalNode should match the BaseVoltage of the containing VoltageLevel if such a containing VoltageLevel is specified. 
"""

# <<< imports
# @generated
from ucte.core.identified_object import IdentifiedObject


from ucte.domain import Voltage

from google.appengine.ext import db
# >>> imports

class BaseVoltage(IdentifiedObject):
    """ Collection of BaseVoltages which is used to verify that the BusbarSection.BaseVoltage and other voltage attributes in the CIM are given a value existing in the collection. The profile requires a BaseVoltage associaton on ConductingEquipment subtypes of classes ACLineSegment and TransformerWinding. The association is not used for any other subtypes. The base voltage of the TopologicalNode should match the BaseVoltage of the containing VoltageLevel if such a containing VoltageLevel is specified. 
    """
    # <<< base_voltage.attributes
    # @generated
    # The PowerSystemResource's base voltage. 
    nominal_voltage = Voltage

    # If true, this is a direct current base voltage and items assigned to this base voltage are also associated with a direct current capabilities.   False indicates alternating current. 
    is_dc = db.BooleanProperty(default=False)

    # >>> base_voltage.attributes

    # <<< base_voltage.references
    # @generated
    # Virtual property. Use association to ConductingEquipment only when there is no VoltageLevel container used.  
    pass # conducting_equipment

    # Virtual property. The VoltageLevels having this BaseVoltage.  
    pass # voltage_level

    # Virtual property. The topological nodes at the base voltage.  
    pass # topological_node

    # >>> base_voltage.references

    # <<< base_voltage.operations
    # @generated
    # >>> base_voltage.operations

# EOF -------------------------------------------------------------------------
