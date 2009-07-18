# Copyright (C) 2009 Richard W. Lincoln
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation; version 2 dated June, 1991.
#
# This software is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANDABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA

from cim14.iec61968.metering import DeviceFunction
from cim14 import Element

from cim14.iec61970.domain import Seconds
from cim14.iec61970.domain import ActivePower
from cim14.iec61970.domain import Voltage
from cim14.iec61970.domain import RealEnergy

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

ns_prefix = "cim.IEC61968.LoadControl"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#IEC61968.LoadControl"

class ConnectDisconnectFunction(DeviceFunction):
    """ A function that will disconnect or reconnect the customer's load under defined conditions.
    """

    # Running cumulative count of (connect or disconnect) events, for the lifetime of this function or until the value is cleared.
    event_count = db.IntegerProperty()
    # True if this function is in the connected state.
    is_connected = db.BooleanProperty()
    # If set true and if reconnection can be operated locally, then the operation happens automatically. Otherwise, it is manually.
    is_local_auto_recon_op = db.BooleanProperty()
    # (if disconnection can be operated locally) If set true, the operation happens automatically, otherwise it happens manually.
    is_local_auto_discon_op = db.BooleanProperty()
    # If set true and if reconnection can be operated remotely, then the operation happens automatically. If false and if reconnection can be operated remotely, then the operation happens manually.
    is_remote_auto_recon_op = db.BooleanProperty()
    # If set true and if disconnection can be operated remotely, then the operation happens automatically. If set false and if disconnection can be operated remotely, then the operation happens manually.
    is_remote_auto_discon_op = db.BooleanProperty()
    # If set true, the switch may disconnect the service at the end of a specified time delay after the disconnect signal had been given. If set false, the switch may disconnect the service immediately after the disconnect signal had been given. This is typically the case for over current circuit-breakers which are classified as either instantaneous or slow acting.
    is_delayed_discon = db.BooleanProperty()
    # Information on remote connect disconnect switch.
    rcd_info = db.ReferenceProperty()
#    switches = db.ListProperty(db.Key)

#    @property
#    def connect_disconnect_functions(self):
#        return Switch.gql("WHERE switches = :1", self.key())

class RemoteConnectDisconnectInfo(Element):
    """ Details of remote connect disconnect function.
    """

    # Setting of the timeout elapsed time.
    armed_timeout = Seconds
    # True if the RCD switch must be armed before a disconnect action can be initiated.
    is_arm_disconnect = db.BooleanProperty()
    # True if pushbutton must be used for connect.
    use_pushbutton = db.BooleanProperty()
    # True if load limit must be checked to issue an immediate disconnect (after a connect) if load is over the limit.
    needs_power_limit_check = db.BooleanProperty()
    # Load limit above which the connect should either not take place or should cause an immediate disconnect.
    power_limit = ActivePower
    # True if the energy usage is limited and the customer will be disconnected if they go over the limit.
    is_energy_limiting = db.BooleanProperty()
    # True if voltage limit must be checked to prevent connect if voltage is over the limit.
    needs_voltage_limit_check = db.BooleanProperty()
    # Voltage limit on customer side of RCD switch above which the connect should not be made.
    customer_voltage_limit = Voltage
    # True if the RCD switch must be armed before a connect action can be initiated.
    is_arm_connect = db.BooleanProperty()
    # Limit of energy before disconnect.
    energy_limit = RealEnergy
    # Start date and time to accumulate energy for energy usage limiting.
    energy_usage_start_date_time = db.DateProperty()
    # Warning energy limit, used to trigger event code that energy usage is nearing limit.
    energy_usage_warning = RealEnergy


