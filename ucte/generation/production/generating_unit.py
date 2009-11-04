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

""" A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set. One GeneratingUnit or its subtype is to be modeled for each SynchronousMachine.     In case the type of generating unit (such as hydro, coal, nuclear, ...) is not well known the GeneratingUnit class may be used as a concrete class in the exchange.  If the type is well known, then an appropriate subtype of GeneratingUnit such as HydroGeneratingUnit should be used in the exchange file. Each SynchronousMachine is a member of one and only one GeneratingUnit plus each GeneratingUnit should have one and only one SynchronousMachine.   This is required to properly proportion generation limits specified on GeneratingUnit to the appropriate injection points specified by SynchronousMachine and its Terminal connection. 
"""

# <<< imports
# @generated
from ucte.core.equipment import Equipment


from ucte.domain import ActivePower
from ucte.domain import Money
from ucte.domain import PerCent

from google.appengine.ext import db
# >>> imports

class GeneratingUnit(Equipment):
    """ A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set. One GeneratingUnit or its subtype is to be modeled for each SynchronousMachine.     In case the type of generating unit (such as hydro, coal, nuclear, ...) is not well known the GeneratingUnit class may be used as a concrete class in the exchange.  If the type is well known, then an appropriate subtype of GeneratingUnit such as HydroGeneratingUnit should be used in the exchange file. Each SynchronousMachine is a member of one and only one GeneratingUnit plus each GeneratingUnit should have one and only one SynchronousMachine.   This is required to properly proportion generation limits specified on GeneratingUnit to the appropriate injection points specified by SynchronousMachine and its Terminal connection. 
    """
    # <<< generating_unit.attributes
    # @generated
    # This is the maximum operating active power limit the dispatcher can enter for this unit 
    max_operating_p = ActivePower

    # The initial startup cost incurred for each start of the GeneratingUnit. This is for Short Circuit only. 
    startup_cost = Money

    # The nominal power of the generating unit.  Used to give precise meaning to percentage based attributes such as the govenor speed change droop (govenorSCD attribute). 
    nominal_p = ActivePower

    # Governor Speed Changer Droop.   This is the change in generator power output divided by the change in frequency normalized by the nominal power of the generator and the nominal frequency and expressed in percent and negated. A positive value of speed change droop provides additional generator output upon a drop in frequency. This is for Short Circuit Only. 
    governor_scd = PerCent

    # Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value regardless of the current operating point. 
    maximum_allowable_spinning_reserve = ActivePower

    # The variable cost component of production per unit of ActivePower. This is for Short Circuit only. 
    variable_cost = Money

    # This is the minimum operating active power limit the dispatcher can enter for this unit. 
    min_operating_p = ActivePower

    # Generating unit economic participation factor For UCTE only one Generating per control area should be non-zero.  The attribute is optional on a GeneratingUnit and the value can be assumed to be zero if missing.   This minimizes the data that must be exchanged.   By convention the non-zero value is specified as one.  
    normal_pf = db.FloatProperty()

    # >>> generating_unit.attributes

    # <<< generating_unit.references
    # @generated
    # Virtual property. A synchronous machine may operate as a generator and as such becomes a member of a generating unit  
    pass # contains_synchronous_machines

    # Virtual property. ControlArea specifications for this generating unit.  
    pass # control_area_generating_unit

    # >>> generating_unit.references

    # <<< generating_unit.operations
    # @generated
    # >>> generating_unit.operations

# EOF -------------------------------------------------------------------------
