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
""" The specificatoin of limits associated with equipment and other operational entities.
"""

from cpsm.core import IdentifiedObject

from cpsm.domain import ActivePower
from cpsm.domain import ApparentPower
from cpsm.domain import Voltage
from cpsm.domain import CurrentFlow

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

ns_prefix = "cim"
ns_uri = "http://iec.ch/TC57/2008/CIM-schema-cim13#Package_OperationalLimits"

class OperationalLimit(IdentifiedObject):
    """ A value associated with a specific kind of limit.
    """

    # Used to specify high/low and limit levels.
    type = db.StringProperty()
#    operational_limit_set = db.ReferenceProperty()

class OperationalLimitSet(IdentifiedObject):
    """ A set of limits associated with equipmnet.
    """

#    equipment = db.ReferenceProperty()
#    operational_limit_value = db.ReferenceProperty()

class ActivePowerLimit(OperationalLimit):
    """ Limit on active power flow.
    """

    # Value of active power limit.
    value = ActivePower

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
    """ OIoeratuibak kimit on current.
    """

    # Limit on current flow.
    value = CurrentFlow


