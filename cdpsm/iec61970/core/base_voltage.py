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

""" Collection of BaseVoltages which is used to verify that the BusbarSection.BaseVoltage and other voltage attributes in the CIM are given a value existing in the collection. 
"""

# <<< imports
# @generated
from cdpsm.iec61970.core.identified_object import IdentifiedObject


from cdpsm.iec61970.domain import Voltage

from google.appengine.ext import db
# >>> imports

class BaseVoltage(IdentifiedObject):
    """ Collection of BaseVoltages which is used to verify that the BusbarSection.BaseVoltage and other voltage attributes in the CIM are given a value existing in the collection. 
    """
    # <<< base_voltage.attributes
    # @generated
    # The PowerSystemResource's base voltage. 
    nominal_voltage = Voltage

    # >>> base_voltage.attributes

    # <<< base_voltage.references
    # @generated
    # Virtual property. Use association to ConductingEquipment only when there is no VoltageLevel container used.  
    pass # conducting_equipment

    # Virtual property. The VoltageLevels having this BaseVoltage.  
    pass # voltage_level

    # >>> base_voltage.references

    # <<< base_voltage.operations
    # @generated
    # >>> base_voltage.operations

# EOF -------------------------------------------------------------------------
