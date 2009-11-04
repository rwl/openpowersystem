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

""" Models the characteristic response of the load demand due to to changes in system conditions such as voltage and frequency. This is not related to demand response. 
"""

# <<< imports
# @generated
from ucte.core.identified_object import IdentifiedObject



from google.appengine.ext import db
# >>> imports

class LoadResponseCharacteristic(IdentifiedObject):
    """ Models the characteristic response of the load demand due to to changes in system conditions such as voltage and frequency. This is not related to demand response. 
    """
    # <<< load_response_characteristic.attributes
    # @generated
    # Exponent of per unit voltage effecting real power.   This model used only when 'useExponentModel' is true. 
    p_voltage_exponent = db.FloatProperty()

    # Portion of reactive power load modeled as constant current. Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP. 
    q_constant_current = db.FloatProperty()

    # Portion of active power load modeled as constant current. Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP. 
    p_constant_current = db.FloatProperty()

    # Indicates the exponential voltage dependency model (pVoltateExponent and qVoltageExponent) is to be used.   If false, the coeficient model (consisting of pConstantImpedance, pConstantCurrent, pConstantPower, qConstantImpedance, qConstantCurrent, and qConstantPower) is to be used. 
    exponent_model = db.BooleanProperty()

    # Portion of active power load modeled as constant power. Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP. 
    p_constant_power = db.FloatProperty()

    # Exponent of per unit voltage effecting reactive power.   This model used only when 'useExponentModel' is true. 
    q_voltage_exponent = db.FloatProperty()

    # Portion of reactive power load modeled as constant power. Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP. 
    q_constant_power = db.FloatProperty()

    # Portion of reactive power load modeled as constant impedance.  Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP. 
    q_constant_impedance = db.FloatProperty()

    # Portion of active power load modeled as constant impedance.  Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP. 
    p_constant_impedance = db.FloatProperty()

    # >>> load_response_characteristic.attributes

    # <<< load_response_characteristic.references
    # @generated
    # Virtual property. The set of loads that have the response characteristics.  
    pass # energy_consumer

    # >>> load_response_characteristic.references

    # <<< load_response_characteristic.operations
    # @generated
    # >>> load_response_characteristic.operations

# EOF -------------------------------------------------------------------------
