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

from cim14 import Element
from cim14.iec61970.core import IdentifiedObject

from cim14.iec61970.domain import Seconds
from cim14.iec61970.domain import ActivePower
from cim14.iec61970.domain import ReactivePower
from cim14.iec61970.domain import ApparentPower
from cim14.iec61970.domain import Voltage
from cim14.iec61970.domain import CurrentFlow

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

OperationalLimitDirectionKind = db.StringProperty(choices=("absolute_value", "high", "low"))

ns_prefix = "cim.IEC61970.OperationalLimits"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#IEC61970.OperationalLimits"

class OperationalLimitType(Element):
    """ A type of limit.  The meaning of a specific limit is described in this class.
    """

    # The direction of the limit.
    direction = OperationalLimitDirectionKind
    # The nominal acceptable duration of the limit.  Limits are commonly expressed in terms of the a time limit for which the limit is normally acceptable.   The actual acceptable duration of a specific limit may depend on other local factors such as temperature or wind speed.
    acceptable_duration = Seconds
    # The 'operational_limit' property has been implicitly created by
    # the operational_limit_type' property of OperationalLimit.
    pass

class BranchGroup(IdentifiedObject):
    """ A group of branch terminals whose directed flow summation is to be monitored. Abranch group need not form a cutset of the network.
    """

    # Monitor the reactive power flow.
    monitor_reactive_power = db.BooleanProperty()
    # Monitor the active power flow.
    monitor_active_power = db.BooleanProperty()
    # The maximum active power flow.
    maximum_active_power = ActivePower
    # The minimum reactive power flow.
    minimum_reactive_power = ReactivePower
    # The maximum reactive power flow.
    maximum_reactive_power = ReactivePower
    # The minimum active power flow.
    minimum_active_power = ActivePower
    # The 'branch_group_terminal' property has been implicitly created by
    # the branch_group' property of BranchGroupTerminal.
    pass

class BranchGroupTerminal(Element):
    """ A specific directed terminal flow for a branch group.
    """

    # The flow into the terminal is summed if set true.   The flow out of the terminanl is summed if set false.
    positive_flow_in = db.BooleanProperty()
#    terminal = db.ReferenceProperty()
#    branch_group = db.ReferenceProperty()

class OperationalLimit(IdentifiedObject):
    """ A value associated with a specific kind of limit.
    """

    # Used to specify high/low and limit levels.
    type = db.StringProperty()
#    operational_limit_type = db.ReferenceProperty()
#    operational_limit_set = db.ReferenceProperty()

class OperationalLimitSet(IdentifiedObject):
    """ A set of limits associated with equipmnet.  Sets of limits might apply to a specific temperature, or season for example. A set of limits may contain may different severities of limit levels that would apply to the same equipment.   The set may contain limits of different types such as apparent power and current limits or high and low voltage limits  that are logically applied together as a set.
    """

#    equipment = db.ReferenceProperty()
#    terminal = db.ReferenceProperty()
    # The 'operational_limit_value' property has been implicitly created by
    # the operational_limit_set' property of OperationalLimit.
    pass

class ApparentPowerLimit(OperationalLimit):
    """ Apparent power limit.
    """

    # The apparent power limit.
    value = ApparentPower

class VoltageLimit(OperationalLimit):
    """ Operational limit applied to voltage.
    """

    # Limit on voltage. High or low limit depends on the OperatoinalLimit.limitKind
    value = Voltage

class CurrentLimit(OperationalLimit):
    """ Operational limit on current.
    """

    # Limit on current flow.
    value = CurrentFlow

class ActivePowerLimit(OperationalLimit):
    """ Limit on active power flow.
    """

    # Value of active power limit.
    value = ActivePower


