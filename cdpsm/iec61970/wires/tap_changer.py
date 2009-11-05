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

""" Mechanism for changing transformer winding tap positions. 
"""

# <<< imports
# @generated
from cdpsm.iec61970.core.power_system_resource import PowerSystemResource


from cdpsm.iec61970.domain import PerCent
from cdpsm.iec61970.domain import Seconds
from cdpsm.iec61970.domain import Voltage

from google.appengine.ext import db
# >>> imports

class TapChanger(PowerSystemResource):
    """ Mechanism for changing transformer winding tap positions. 
    """
    # <<< tap_changer.attributes
    # @generated
    # Tap step increment, in per cent of nominal voltage, per step position.  For a symmetrical PhaseTapChanger, the stepVoltageIncrement is used in the formula for calculation of the phase angle.  For a symmetrical PhaseTapChanger, the voltage magnitude does not change with tap step. 
    step_voltage_increment = PerCent

    # For an LTC, the delay for subsequent tap changer operation (second and later step changes) 
    subsequent_delay = Seconds

    # The neutral tap step position for this winding. 
    neutral_step = db.IntegerProperty()

    # The tap step position used in 'normal' network operation for this winding. For a 'Fixed' tap changer indicates the current physical tap setting. 
    normal_step = db.IntegerProperty()

    # Specifies whether or not a TapChanger has load tap changing capabilities. 
    ltc_flag = db.BooleanProperty()

    # Voltage at which the winding operates at the neutral tap setting. 
    neutral_u = Voltage

    # Lowest possible tap step position, retard from neutral 
    low_step = db.IntegerProperty()

    # For an LTC, the delay for initial tap changer operation (first step change) 
    initial_delay = Seconds

    # Specifies the default regulation status of the TapChanger.  True is regulating.  False is not regulating. 
    regulation_status = db.BooleanProperty()

    # Highest possible tap step position, advance from neutral 
    high_step = db.IntegerProperty()

    # >>> tap_changer.attributes

    # <<< tap_changer.references
    # @generated
    # The tap step state associated with the tap changer. 
    sv_tap_step = db.ReferenceProperty(db.Model,
        collection_name="_tap_changer_set") # tap_changer

    # >>> tap_changer.references

    # <<< tap_changer.operations
    # @generated
    # >>> tap_changer.operations

# EOF -------------------------------------------------------------------------
