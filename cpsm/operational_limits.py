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

""" The specificatoin of limits associated with equipment and other operational entities.The specificatoin of limits associated with equipment and other operational entities.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from cpsm.core import IdentifiedObject

from cpsm.domain import ActivePower
from cpsm.domain import ApparentPower
from cpsm.domain import Voltage
from cpsm.domain import CurrentFlow

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

#------------------------------------------------------------------------------
#  Properties:
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  Constants:
#------------------------------------------------------------------------------

NS_PREFIX = "cim"
NS_URI = "http://iec.ch/TC57/2008/CIM-schema-cim13#Package_OperationalLimits"

#------------------------------------------------------------------------------
#  "OperationalLimit" class:
#------------------------------------------------------------------------------

class OperationalLimit(IdentifiedObject):
    """ A value associated with a specific kind of limit.A value associated with a specific kind of limit.
    """

    
    # Used to specify high/low and limit levels.Used to specify high/low and limit levels.
    type = db.StringProperty()

    # The limit set to which the limit values belong.The limit set to which the limit values belong.
    operational_limit_set = db.ReferenceProperty(collection_name="operational_limit_value")

    # <<< operational_limit
    # @generated
    # >>> operational_limit


#------------------------------------------------------------------------------
#  "OperationalLimitSet" class:
#------------------------------------------------------------------------------

class OperationalLimitSet(IdentifiedObject):
    """ A set of limits associated with equipmnet.A set of limits associated with equipmnet.
    """

    
    # The equpment to which the limit set applies.The equpment to which the limit set applies.
    equipment = db.ReferenceProperty(collection_name="operational_limit_set")

    # Virtual property. Values of equipment limits.Values of equipment limits.
    pass #operational_limit_value

    # <<< operational_limit_set
    # @generated
    # >>> operational_limit_set


#------------------------------------------------------------------------------
#  "ActivePowerLimit" class:
#------------------------------------------------------------------------------

class ActivePowerLimit(OperationalLimit):
    """ Limit on active power flow.Limit on active power flow.
    """

    
    # Value of active power limit.Value of active power limit.
    value = ActivePower

    # <<< active_power_limit
    # @generated
    # >>> active_power_limit


#------------------------------------------------------------------------------
#  "ApparentPowerLimit" class:
#------------------------------------------------------------------------------

class ApparentPowerLimit(OperationalLimit):
    """ Apparent power limit.Apparent power limit.
    """

    
    # The apparent power limit.The apparent power limit.
    value = ApparentPower

    # <<< apparent_power_limit
    # @generated
    # >>> apparent_power_limit


#------------------------------------------------------------------------------
#  "VoltageLimit" class:
#------------------------------------------------------------------------------

class VoltageLimit(OperationalLimit):
    """ Operational limit applied to voltage.Operational limit applied to voltage.
    """

    
    # Limit on voltage. High or low limit depends on the OperatoinalLimit.limitKindLimit on voltage. High or low limit depends on the OperatoinalLimit.limitKind
    value = Voltage

    # <<< voltage_limit
    # @generated
    # >>> voltage_limit


#------------------------------------------------------------------------------
#  "CurrentLimit" class:
#------------------------------------------------------------------------------

class CurrentLimit(OperationalLimit):
    """ OIoeratuibak kimit on current.OIoeratuibak kimit on current.
    """

    
    # Limit on current flow.Limit on current flow.
    value = CurrentFlow

    # <<< current_limit
    # @generated
    # >>> current_limit




# EOF -------------------------------------------------------------------------
