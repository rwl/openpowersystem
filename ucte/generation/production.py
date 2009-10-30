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
""" The production package is responsible for classes which describe various kinds of generators. These classes also provide production costing information which is used to economically allocate demand among committed units and calculate reserve quantities.The production package is responsible for classes which describe various kinds of generators. These classes also provide production costing information which is used to economically allocate demand among committed units and calculate reserve quantities.
"""

from ucte.core import Equipment
from ucte.core import IdentifiedObject

from ucte.domain import ActivePower
from ucte.domain import Money
from ucte.domain import PerCent

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

FuelType = db.StringProperty(choices=("oil", "coal", "lignite", "gas"))

ns_prefix = "cim"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_Production"

class GeneratingUnit(Equipment):
    """ A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.One GeneratingUnit or its subtype is to be modeled for each SynchronousMachine.     In case the type of generating unit (such as hydro, coal, nuclear, ...) is not well known the GeneratingUnit class may be used as a concrete class in the exchange.  If the type is well known, then an appropriate subtype of GeneratingUnit such as HydroGeneratingUnit should be used in the exchange file. Each SynchronousMachine is a member of one and only one GeneratingUnit plus each GeneratingUnit should have one and only one SynchronousMachine.   This is required to properly proportion generation limits specified on GeneratingUnit to the appropriate injection points specified by SynchronousMachine and its Terminal connection.A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.One GeneratingUnit or its subtype is to be modeled for each SynchronousMachine.     In case the type of generating unit (such as hydro, coal, nuclear, ...) is not well known the GeneratingUnit class may be used as a concrete class in the exchange.  If the type is well known, then an appropriate subtype of GeneratingUnit such as HydroGeneratingUnit should be used in the exchange file. Each SynchronousMachine is a member of one and only one GeneratingUnit plus each GeneratingUnit should have one and only one SynchronousMachine.   This is required to properly proportion generation limits specified on GeneratingUnit to the appropriate injection points specified by SynchronousMachine and its Terminal connection.
    """

    # This is the maximum operating active power limit the dispatcher can enter for this unitThis is the maximum operating active power limit the dispatcher can enter for this unit
    max_operating_p = ActivePower
    # The initial startup cost incurred for each start of the GeneratingUnit.This is for Short Circuit only.The initial startup cost incurred for each start of the GeneratingUnit.This is for Short Circuit only.
    startup_cost = Money
    # The nominal power of the generating unit.  Used to give precise meaning to percentage based attributes such as the govenor speed change droop (govenorSCD attribute).The nominal power of the generating unit.  Used to give precise meaning to percentage based attributes such as the govenor speed change droop (govenorSCD attribute).
    nominal_p = ActivePower
    # Governor Speed Changer Droop.   This is the change in generator power output divided by the change in frequency normalized by the nominal power of the generator and the nominal frequency and expressed in percent and negated. A positive value of speed change droop provides additional generator output upon a drop in frequency.This is for Short Circuit Only.Governor Speed Changer Droop.   This is the change in generator power output divided by the change in frequency normalized by the nominal power of the generator and the nominal frequency and expressed in percent and negated. A positive value of speed change droop provides additional generator output upon a drop in frequency.This is for Short Circuit Only.
    governor_scd = PerCent
    # Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value regardless of the current operating point.Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value regardless of the current operating point.
    maximum_allowable_spinning_reserve = ActivePower
    # The variable cost component of production per unit of ActivePower.This is for Short Circuit only.The variable cost component of production per unit of ActivePower.This is for Short Circuit only.
    variable_cost = Money
    # This is the minimum operating active power limit the dispatcher can enter for this unit.This is the minimum operating active power limit the dispatcher can enter for this unit.
    min_operating_p = ActivePower
    # Generating unit economic participation factorFor UCTE only one Generating per control area should be non-zero.  The attribute is optional on a GeneratingUnit and the value can be assumed to be zero if missing.   This minimizes the data that must be exchanged.   By convention the non-zero value is specified as one. Generating unit economic participation factorFor UCTE only one Generating per control area should be non-zero.  The attribute is optional on a GeneratingUnit and the value can be assumed to be zero if missing.   This minimizes the data that must be exchanged.   By convention the non-zero value is specified as one. 
    normal_pf = db.FloatProperty()
    # The 'contains_synchronous_machines' property has been implicitly created by
    # the member_of_generating_unit' property of SynchronousMachine.
    pass
    # The 'control_area_generating_unit' property has been implicitly created by
    # the generating_unit' property of ControlAreaGeneratingUnit.
    pass

class FossilFuel(IdentifiedObject):
    """ The fossil fuel consumed by the non-nuclear thermal generating units, e.g., coal, oil, gasThe UCTE profile allows only one type of fuel per ThermalGeneratingUnit. The UCTE profile allows only one type of fuel per ThermalGeneratingUnit.The fossil fuel consumed by the non-nuclear thermal generating units, e.g., coal, oil, gasThe UCTE profile allows only one type of fuel per ThermalGeneratingUnit. The UCTE profile allows only one type of fuel per ThermalGeneratingUnit.
    """

    # The type of fossil fuel, such as coal, oil, or gas.The type of fossil fuel, such as coal, oil, or gas.
    fossil_fuel_type = FuelType
#    thermal_generating_unit = db.ReferenceProperty()

class HydroPump(IdentifiedObject):
    """ A synchronous motor-driven pump, typically associated with a pumped storage plantA HydroPump is included in the profile to indicate the associated SynchronousMachine can run in pump mode.A synchronous motor-driven pump, typically associated with a pumped storage plantA HydroPump is included in the profile to indicate the associated SynchronousMachine can run in pump mode.
    """

#    driven_by_synchronous_machine = db.ReferenceProperty()

class WindGeneratingUnit(GeneratingUnit):
    """ A wind driven generating unit.A wind driven generating unit.
    """

    pass

class NuclearGeneratingUnit(GeneratingUnit):
    """ A nuclear generating unit.A nuclear generating unit.
    """

    pass

class HydroGeneratingUnit(GeneratingUnit):
    """ A generating unit whose prime mover is a hydraulic turbine (e.g., Francis, Pelton, Kaplan)A generating unit whose prime mover is a hydraulic turbine (e.g., Francis, Pelton, Kaplan)
    """

    pass

class ThermalGeneratingUnit(GeneratingUnit):
    """ A generating unit whose prime mover could be a steam turbine, combustion turbine, or diesel engine.A generating unit whose prime mover could be a steam turbine, combustion turbine, or diesel engine.
    """

#    fossil_fuels = db.ReferenceProperty()


