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
""" The OperationalLimits package models a specification of limits associated with equipment and other operational entities.The OperationalLimits package models a specification of limits associated with equipment and other operational entities.
"""

from ucte.core import IdentifiedObject

from ucte.domain import CurrentFlow
from ucte.domain import Voltage
from ucte.domain import Seconds

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

OperationalLimitDirectionKind = db.StringProperty(choices=("high", "absolute_value", "low"))

ns_prefix = "cim"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_OperationalLimits"

class OperationalLimit(IdentifiedObject):
    """ A value associated with a specific kind of limit.A value associated with a specific kind of limit.
    """

#    operational_limit_set = db.ReferenceProperty()
#    operational_limit_type = db.ReferenceProperty()

class OperationalLimitSet(IdentifiedObject):
    """ A set of limits associated with equipmnet.  Sets of limits might apply to a specific temperature, or season for example. A set of limits may contain may different severiteis of limit levels that would apply to the same equipment.   The set may contain limits of different types such as apparent power and current limits or high and low voltage limits  that are logically applied together as a set.A set of limits associated with equipmnet.  Sets of limits might apply to a specific temperature, or season for example. A set of limits may contain may different severiteis of limit levels that would apply to the same equipment.   The set may contain limits of different types such as apparent power and current limits or high and low voltage limits  that are logically applied together as a set.
    """

#    terminal = db.ReferenceProperty()
    # The 'operational_limit_value' property has been implicitly created by
    # the operational_limit_set' property of OperationalLimit.
    pass

class OperationalLimitType(IdentifiedObject):
    """ A type of limit.  The meaning of a specific limit is described in this class.A type of limit.  The meaning of a specific limit is described in this class.
    """

    # The direction of the limit.The direction of the limit.
    direction = OperationalLimitDirectionKind
    # The nominal acceptable duration of the limit.  Limits are commonly expressed in terms of the a time limit for which the limit is normally acceptable.   The actual acceptable duration of a specific limit may depend on other local factors such as temperature or wind speed.The nominal acceptable duration of the limit.  Limits are commonly expressed in terms of the a time limit for which the limit is normally acceptable.   The actual acceptable duration of a specific limit may depend on other local factors such as temperature or wind speed.
    acceptable_duration = Seconds
    # The 'operational_limit' property has been implicitly created by
    # the operational_limit_type' property of OperationalLimit.
    pass

class CurrentLimit(OperationalLimit):
    """ Operational limit on current.Operational limit on current.
    """

    # Limit on current flow.Limit on current flow.
    value = CurrentFlow

class VoltageLimit(OperationalLimit):
    """ Operational limit applied to voltage.Operational limit applied to voltage.
    """

    # Limit on voltage. High or low limit depends on the OperatoinalLimit.limitKindLimit on voltage. High or low limit depends on the OperatoinalLimit.limitKind
    value = Voltage


