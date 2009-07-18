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
from cim14.iec61968.common import ActivityRecord

from cim14.iec61970.domain import ActivePower
from cim14.iec61970.domain import Seconds
from cim14.iec61970.domain import Minutes

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

LoadStateKind = db.StringProperty(choices=("limited_load", "full_load", "no_load"))

LoadMgmtKind = db.StringProperty(choices=("manual_control", "time_based", "remote_control", "tariff_based"))

ns_prefix = "cim.IEC61968.Informative.InfLoadControl"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#IEC61968.Informative.InfLoadControl"

class LoadMgmtFunction(DeviceFunction):
    """ A collective function at an end device that manages the customer load.
    """

    # The basis of Load Management scheduling used here: Time Based, Tariff Based, Remote Control and Manual Control.
    scheduling_basis = LoadMgmtKind
    # True if the currently active schedule is being remotely over-ridden to either shed load or to limit load.
    remote_over_ride = db.BooleanProperty()
    # True if the currently active schedule is being manually over-ridden to either shed load or to limit load.
    manual_over_ride = db.BooleanProperty()
    # The present state of the load being either shed (noLoad), limited (limitedLoad) or fully connected (fullLoad). This refers only to the portion of the customer load that is under control of the LoadMgmtFunction.
    load_status = LoadStateKind
    # After a command had been received to activate the mannualOverRide state or remoteOverRideState, the normal (halted) schedule will resume after this specified time duration had elapsed.
    over_ride_time_out = Minutes
    # True if LoadMgmtFunction operates under automatic control, otherwise it operates under manual control.
    is_auto_op = db.BooleanProperty()
#    switches = db.ListProperty(db.Key)

#    @property
#    def load_mgmt_functions(self):
#        return Switch.gql("WHERE switches = :1", self.key())
    # The 'load_mgmt_records' property has been implicitly created by
    # the load_mgmt_function' property of LoadMgmtRecord.
    pass

class LoadMgmtRecord(ActivityRecord):
    """ A log of actual measured load reductions as a result of load shed operations.
    """

    # The measured reduction of the total load power as a result of the load shed activation. Thus it is the difference in power before and after the load shed operation.
    load_reduction = ActivePower
#    load_mgmt_function = db.ReferenceProperty()

class LoadShedFunction(LoadMgmtFunction):
    """ A kind of LoadMgmtFunction that sheds a part of the customer load.
    """

    # The value of the load that is connected to the shedding switch. Typically this is a noted nominal value rather than a measured value.
    switched_load = ActivePower

class LoadLimitFunction(LoadMgmtFunction):
    """ A kind of LoadMgmtFunction that limits the customer load to a given value.
    """

    # The power level, to which the customer load is being limited when this function activates. When the maximum load is exceeded the switch will typically open to shed the complete customer load.
    maximum_load = ActivePower
    # From the point when the load recovers from an overload condition and crosses the maximumLoad threshold going down, there may be a finite time delay before the switch actually reconnects the load. Typically this is to give overload conditions sufficient time to clear, thus preventing unnecessary load switching activity.
    reconnect_time_delay = Seconds
    # True if the switch will reconnect automatically, otherwise it will reconnect under manual control.
    is_auto_recon_op = db.BooleanProperty()
    # From the point when the maximumLoad threshold is crossed there may be a finite delay before the switch actually disconnects the load. Typically this is to buffer against transient load fluctuations.
    disconnect_time_delay = Seconds


