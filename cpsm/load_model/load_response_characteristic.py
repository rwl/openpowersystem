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
from cpsm.core.identified_object import IdentifiedObject



from google.appengine.ext import db
# >>> imports

class LoadResponseCharacteristic(IdentifiedObject):
    """ Models the characteristic response of the load demand due to to changes in system conditions such as voltage and frequency. This is not related to demand response. 
    """
    # <<< load_response_characteristic.attributes
    # @generated
    # Exponent of per unit frequency effecting active power 
    p_frequency_exponent = db.FloatProperty()

    # Exponent of per unit voltage effecting reactive power.   This model used only when 'useExponentModel' is true. 
    q_voltage_exponent = db.FloatProperty()

    # Exponent of per unit frequency effecting reactive power 
    q_frequency_exponent = db.FloatProperty()

    # Exponent of per unit voltage effecting real power.   This model used only when 'useExponentModel' is true. 
    p_voltage_exponent = db.FloatProperty()

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
