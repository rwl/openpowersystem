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

""" The production package is responsible for classes which describe various kinds of generators. These classes also provide production costing information which is used to economically allocate demand among committed units and calculate reserve quantities. 
"""

# <<< imports
# @generated
from ucte.core import Equipment
from ucte.core import IdentifiedObject

from ucte.domain import ActivePower
from ucte.domain import Money
from ucte.domain import PerCent

from google.appengine.ext import db
# >>> imports

# <<< properties
# @generated

FuelType = db.StringProperty(choices=("oil", "coal", "lignite", "gas"))
# >>> properties

# <<< constants
# @generated
NS_PREFIX = "cim"
NS_URI = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_Production"
# >>> constants

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

class FossilFuel(IdentifiedObject):
    """ The fossil fuel consumed by the non-nuclear thermal generating units, e.g., coal, oil, gas The UCTE profile allows only one type of fuel per ThermalGeneratingUnit. The UCTE profile allows only one type of fuel per ThermalGeneratingUnit. 
    """
    # <<< fossil_fuel.attributes
    # @generated
    # The type of fossil fuel, such as coal, oil, or gas. 
    fossil_fuel_type = FuelType

    # >>> fossil_fuel.attributes

    # <<< fossil_fuel.references
    # @generated
    # A thermal generating unit may have one or more fossil fuels  
    thermal_generating_unit = db.ReferenceProperty(collection_name="_fossil_fuel_set")

    # >>> fossil_fuel.references

    # <<< fossil_fuel.operations
    # @generated
    # >>> fossil_fuel.operations

class HydroPump(IdentifiedObject):
    """ A synchronous motor-driven pump, typically associated with a pumped storage plant A HydroPump is included in the profile to indicate the associated SynchronousMachine can run in pump mode. 
    """
    # <<< hydro_pump.attributes
    # @generated
    # >>> hydro_pump.attributes

    # <<< hydro_pump.references
    # @generated
    # The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating. 
    driven_by_synchronous_machine = db.ReferenceProperty(collection_name="_hydro_pump_set")

    # >>> hydro_pump.references

    # <<< hydro_pump.operations
    # @generated
    # >>> hydro_pump.operations

class WindGeneratingUnit(GeneratingUnit):
    """ A wind driven generating unit. 
    """
    # <<< wind_generating_unit.attributes
    # @generated
    # >>> wind_generating_unit.attributes

    # <<< wind_generating_unit.references
    # @generated
    # >>> wind_generating_unit.references

    # <<< wind_generating_unit.operations
    # @generated
    # >>> wind_generating_unit.operations

class NuclearGeneratingUnit(GeneratingUnit):
    """ A nuclear generating unit. 
    """
    # <<< nuclear_generating_unit.attributes
    # @generated
    # >>> nuclear_generating_unit.attributes

    # <<< nuclear_generating_unit.references
    # @generated
    # >>> nuclear_generating_unit.references

    # <<< nuclear_generating_unit.operations
    # @generated
    # >>> nuclear_generating_unit.operations

class HydroGeneratingUnit(GeneratingUnit):
    """ A generating unit whose prime mover is a hydraulic turbine (e.g., Francis, Pelton, Kaplan) 
    """
    # <<< hydro_generating_unit.attributes
    # @generated
    # >>> hydro_generating_unit.attributes

    # <<< hydro_generating_unit.references
    # @generated
    # >>> hydro_generating_unit.references

    # <<< hydro_generating_unit.operations
    # @generated
    # >>> hydro_generating_unit.operations

class ThermalGeneratingUnit(GeneratingUnit):
    """ A generating unit whose prime mover could be a steam turbine, combustion turbine, or diesel engine. 
    """
    # <<< thermal_generating_unit.attributes
    # @generated
    # >>> thermal_generating_unit.attributes

    # <<< thermal_generating_unit.references
    # @generated
    # A thermal generating unit may have one or more fossil fuels The UCTE profile allows only one type of fuel per ThermalGeneratingUnit. 
    fossil_fuels = db.ReferenceProperty(collection_name="_thermal_generating_unit_set")

    # >>> thermal_generating_unit.references

    # <<< thermal_generating_unit.operations
    # @generated
    # >>> thermal_generating_unit.operations



# EOF -------------------------------------------------------------------------
