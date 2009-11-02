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

""" The OperationalLimits package models a specification of limits associated with equipment and other operational entities. 
"""

# <<< imports
# @generated
from ucte.core import IdentifiedObject

from ucte.domain import CurrentFlow
from ucte.domain import Voltage
from ucte.domain import Seconds

from google.appengine.ext import db
# >>> imports

# <<< properties
# @generated

OperationalLimitDirectionKind = db.StringProperty(choices=("high", "absolute_value", "low"))
# >>> properties

# <<< constants
# @generated
NS_PREFIX = "cim"
NS_URI = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_OperationalLimits"
# >>> constants

class OperationalLimit(IdentifiedObject):
    """ A value associated with a specific kind of limit. 
    """
    # <<< operational_limit.attributes
    # @generated
    # >>> operational_limit.attributes

    # <<< operational_limit.references
    # @generated
    # The limit set to which the limit values belong. 
    operational_limit_set = db.ReferenceProperty(db.Model, collection_name="operational_limit_value")

    # The limit type associated with this limit. 
    operational_limit_type = db.ReferenceProperty(db.Model, collection_name="operational_limit")

    # >>> operational_limit.references

    # <<< operational_limit.operations
    # @generated
    # >>> operational_limit.operations

class OperationalLimitSet(IdentifiedObject):
    """ A set of limits associated with equipmnet.  Sets of limits might apply to a specific temperature, or season for example. A set of limits may contain may different severiteis of limit levels that would apply to the same equipment.   The set may contain limits of different types such as apparent power and current limits or high and low voltage limits  that are logically applied together as a set. 
    """
    # <<< operational_limit_set.attributes
    # @generated
    # >>> operational_limit_set.attributes

    # <<< operational_limit_set.references
    # @generated
    # The terminal specifically associated to this operational limit set.  If no terminal is associated, all terminals of the equipment are implied. For UCTE profile, the terminal associated with the limit is always required, and thus there is no need to exchange the associated Equipment which can always be derived from the terminal. 
    terminal = db.ReferenceProperty(db.Model, collection_name="operational_limit_set")

    # Virtual property. Values of equipment limits.  
    pass # operational_limit_value

    # >>> operational_limit_set.references

    # <<< operational_limit_set.operations
    # @generated
    # >>> operational_limit_set.operations

class OperationalLimitType(IdentifiedObject):
    """ A type of limit.  The meaning of a specific limit is described in this class. 
    """
    # <<< operational_limit_type.attributes
    # @generated
    # The direction of the limit. 
    direction = OperationalLimitDirectionKind

    # The nominal acceptable duration of the limit.  Limits are commonly expressed in terms of the a time limit for which the limit is normally acceptable.   The actual acceptable duration of a specific limit may depend on other local factors such as temperature or wind speed. 
    acceptable_duration = Seconds

    # >>> operational_limit_type.attributes

    # <<< operational_limit_type.references
    # @generated
    # Virtual property. The operational limits associated with this type of limit.  
    pass # operational_limit

    # >>> operational_limit_type.references

    # <<< operational_limit_type.operations
    # @generated
    # >>> operational_limit_type.operations

class CurrentLimit(OperationalLimit):
    """ Operational limit on current. 
    """
    # <<< current_limit.attributes
    # @generated
    # Limit on current flow. 
    value = CurrentFlow

    # >>> current_limit.attributes

    # <<< current_limit.references
    # @generated
    # >>> current_limit.references

    # <<< current_limit.operations
    # @generated
    # >>> current_limit.operations

class VoltageLimit(OperationalLimit):
    """ Operational limit applied to voltage. 
    """
    # <<< voltage_limit.attributes
    # @generated
    # Limit on voltage. High or low limit depends on the OperatoinalLimit.limitKind 
    value = Voltage

    # >>> voltage_limit.attributes

    # <<< voltage_limit.references
    # @generated
    # >>> voltage_limit.references

    # <<< voltage_limit.operations
    # @generated
    # >>> voltage_limit.operations



# EOF -------------------------------------------------------------------------
