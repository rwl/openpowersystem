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

from cim14.iec61970.core import PowerSystemResource
from cim14.iec61970.core import Curve
from cim14.iec61970.core import Equipment
from cim14.iec61970.core import IdentifiedObject
from cim14.iec61970.core import RegularIntervalSchedule

from cim14.iec61970.domain import Length
from cim14.iec61970.domain import WaterLevel
from cim14.iec61970.domain import Volume
from cim14.iec61970.domain import Seconds
from cim14.iec61970.domain import Money
from cim14.iec61970.domain import ActivePower
from cim14.iec61970.domain import ActivePowerChangeRate
from cim14.iec61970.domain import PerCent
from cim14.iec61970.domain import PU
from cim14.iec61970.domain import RealEnergy
from cim14.iec61970.domain import Hours
from cim14.iec61970.domain import CostRate
from cim14.iec61970.domain import CostPerEnergyUnit

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

HeatRate = db.FloatProperty(0)

CostPerHeatUnit = db.FloatProperty(0)

Classification = db.IntegerProperty(0)

Emission = db.FloatProperty(0)

SurgeTankCode = db.StringProperty()

GeneratorOperatingMode = db.StringProperty(choices=("mrn", "manual", "reg", "lfc", "edc", "fixed", "agc", "off"))

HydroPlantType = db.StringProperty(choices=("major_storage", "run_of_river", "minor_storage", "pumped_storage"))

GeneratorControlSource = db.StringProperty(choices=("unavailable", "off_agc", "on_agc", "plant_control"))

GeneratorControlMode = db.StringProperty(choices=("pulse", "setpoint"))

EmissionType = db.StringProperty(choices=("nitrogen_oxide", "chlorine", "hydrogen_sulfide", "sulfur_dioxide", "carbon_disulfide", "carbon_dioxide"))

EmissionValueSource = db.StringProperty(choices=("calculated", "measured"))

FuelType = db.StringProperty(choices=("coal", "oil", "gas"))

PenstockType = db.StringProperty()

SpillwayGateType = db.StringProperty()

HydroEnergyConversionKind = db.StringProperty(choices=("generator", "pump_and_generator"))

ns_prefix = "cim.IEC61970.Generation.Production"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#IEC61970.Generation.Production"

class Reservoir(PowerSystemResource):
    """ A water storage facility within a hydro system, including: ponds, lakes, lagoons, and rivers. The storage is usually behind some type of dam.
    """

    # The length of the spillway crest
    spillway_crest_length = Length
    # River outlet works for riparian right releases or other purposes
    river_outlet_works = db.StringProperty()
    # Normal minimum operating level below which the penstocks will draw air
    normal_min_operate_level = WaterLevel
    # Total capacity of reservoir
    gross_capacity = Volume
    # Spillway crest level above which water will spill
    spillway_crest_level = WaterLevel
    # The reservoir's energy storage rating in energy for given head conditions
    energy_storage_rating = db.FloatProperty()
    # Full supply level, above which water will spill. This can be the spillway crest level or the top of closed gates.
    full_supply_level = WaterLevel
    # Type of spillway gate, including parameters
    spill_way_gate_type = SpillwayGateType
    # The flow capacity of the spillway in cubic meters per second
    spillway_capacity = db.FloatProperty()
    # Storage volume between the full supply level and the normal minimum operating level
    active_storage_capacity = Volume
    # The spillway water travel delay to the next downstream reservoir
    spill_travel_delay = Seconds
    # The 'upstream_from_hydro_power_plants' property has been implicitly created by
    # the gen_source_pump_discharge_reservoir' property of HydroPowerPlant.
    pass
    # The 'spills_into_reservoirs' property has been implicitly created by
    # the spills_from_reservoir' property of Reservoir.
    pass
#    target_level_schedule = db.ReferenceProperty()
#    spills_from_reservoir = db.ReferenceProperty()
    # The 'level_vs_volume_curves' property has been implicitly created by
    # the reservoir' property of LevelVsVolumeCurve.
    pass
    # The 'inflow_forecasts' property has been implicitly created by
    # the reservoir' property of InflowForecast.
    pass
    # The 'hydro_power_plants' property has been implicitly created by
    # the reservoir' property of HydroPowerPlant.
    pass

class GrossToNetActivePowerCurve(Curve):
    """ Relationship between the generating unit's gross active power output on the X-axis (measured at the terminals of the machine(s)) and the generating unit's net active power output on the Y-axis (based on utility-defined measurements at the power station). Station service loads, when modeled, should be treated as non-conforming bus loads. There may be more than one curve, depending on the auxiliary equipment that is in service.
    """

#    generating_unit = db.ReferenceProperty()

class ShutdownCurve(Curve):
    """ Relationship between the rate in gross active power/minute (Y-axis) at which a unit should be shutdown and its present gross MW output (X-axis)
    """

    # Fixed shutdown cost
    shutdown_cost = Money
    # The date and time of the most recent generating unit shutdown
    shutdown_date = db.DateProperty()
#    thermal_generating_unit = db.ReferenceProperty()

class HydroPump(PowerSystemResource):
    """ A synchronous motor-driven pump, typically associated with a pumped storage plant
    """

    # The pumping power under minimum head conditions, usually at full gate.
    pump_power_at_min_head = ActivePower
    # The pumping discharge (m3/sec) under minimum head conditions, usually at full gate
    pump_disch_at_min_head = db.FloatProperty()
    # The pumping discharge (m3/sec) under maximum head conditions, usually at full gate
    pump_disch_at_max_head = db.FloatProperty()
    # The pumping power under maximum head conditions, usually at full gate
    pump_power_at_max_head = ActivePower
#    hydro_pump_op_schedule = db.ReferenceProperty()
#    synchronous_machine = db.ReferenceProperty()
#    hydro_power_plant = db.ReferenceProperty()

class EmissionCurve(Curve):
    """ Relationship between the unit's emission rate in units of mass per hour (Y-axis) and output active power (X-axis) for a given type of emission. This curve applies when only one type of fuel is being burned.
    """

    # Flag is set to true when output is expressed in net active power
    is_net_gross_p = db.BooleanProperty()
    # The type of emission, which also gives the production rate measurement unit. The y1AxisUnits of the curve contains the unit of measure (e.g. kg) and the emissionType is the type of emission (e.g. sulfer dioxide).
    emission_type = EmissionType
    # The emission content per quantity of fuel burned
    emission_content = Emission
#    thermal_generating_unit = db.ReferenceProperty()

class AirCompressor(PowerSystemResource):
    """ Combustion turbine air compressor which is an integral part of a compressed air energy storage (CAES) plant
    """

    # Rating of the CAES air compressor
    air_compressor_rating = db.FloatProperty()
#    combustion_turbine = db.ReferenceProperty()
#    caesplant = db.ReferenceProperty()

class EmissionAccount(Curve):
    """ Accounts for tracking emissions usage and credits for thermal generating units. A unit may have zero or more emission accounts, and will typically have one for tracking usage and one for tracking credits.
    """

    # The type of emission, for example sulfur dioxide (SO2). The y1AxisUnits of the curve contains the unit of measure (e.g. kg) and the emissionType is the type of emission (e.g. sulfer dioxide).
    emission_type = EmissionType
    # The source of the emission value.
    emission_value_source = EmissionValueSource
#    thermal_generating_unit = db.ReferenceProperty()

class LevelVsVolumeCurve(Curve):
    """ Relationship between reservoir volume and reservoir level. The  volume is at the y-axis and the reservoir level at the x-axis.
    """

#    reservoir = db.ReferenceProperty()

class GeneratingUnit(Equipment):
    """ A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.
    """

    # The source of controls for a generating unit.
    gen_control_source = GeneratorControlSource
    # Time it takes to get the unit on-line, from the time that the prime mover mechanical power is applied
    startup_time = Seconds
    # This is the minimum operating active power limit the dispatcher can enter for this unit.
    min_operating_p = ActivePower
    # High limit for secondary (AGC) control
    high_control_limit = ActivePower
    # Minimum time interval between unit shutdown and startup
    minimum_off_time = Seconds
    energy_min_p = HeatRate
    # For dispatchable units, this value represents the economic active power basepoint, for units that are not dispatchable, this value represents the fixed generation value. The value must be between the operating low and high limits.
    base_p = ActivePower
    # Low economic active power limit that must be greater than or equal to the minimum operating active power limit
    min_economic_p = ActivePower
    spin_reserve_ramp = ActivePowerChangeRate
    # Pulse high limit which is the largest control pulse that the unit can respond to
    control_pulse_high = Seconds
    # Low limit for secondary (AGC) control
    low_control_limit = ActivePower
    # Governor Speed Changer Droop.   This is the change in generator power output divided by the change in frequency normalized by the nominal power of the generator and the nominal frequency and expressed in percent and negated. A positive value of speed change droop provides additional generator output upon a drop in frequency.
    governor_scd = PerCent
    # The unit control mode.
    gen_control_mode = GeneratorControlMode
    # Unit control error deadband. When a unit's desired active power change is less than this deadband, then no control pulses will be sent to the unit.
    control_deadband = ActivePower
    step_change = ActivePower
    # The net rated maximum capacity determined by subtracting the auxiliary power used to operate the internal plant machinery from the rated gross maximum capacity
    rated_net_max_p = ActivePower
    # Generating unit economic participation factor
    short_pf = db.FloatProperty()
    # Operating mode for secondary control.
    gen_operating_mode = GeneratorOperatingMode
    # Governor Motor Position Limit
    governor_mpl = PU
    # Default Initial active power  which is used to store a powerflow result for the initial active power for this unit in this network configuration
    initial_p = ActivePower
    disp_reserve_flag = db.BooleanProperty()
    # Unit response rate which specifies the active power change for a control pulse of one second in the most responsive loading level of the unit.
    control_response_rate = ActivePowerChangeRate
    # The planned unused capacity which can be used to support automatic control overruns.
    auto_cntrl_margin_p = ActivePower
    # The efficiency of the unit in converting mechanical energy, from the prime mover, into electrical energy.
    efficiency = PU
    # The gross rated minimum generation level which the unit can safely operate at while delivering power to the transmission grid
    rated_gross_min_p = ActivePower
    # Detail level of the generator model data
    model_detail = Classification
    lower_ramp_rate = ActivePowerChangeRate
    # Maximum high economic active power limit, that should not exceed the maximum operating active power limit
    max_economic_p = ActivePower
    # Pulse low limit which is the smallest control pulse that the unit can respond to
    control_pulse_low = Seconds
    # Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value regardless of the current operating point.
    maximum_allowable_spinning_reserve = ActivePower
    # The unit's gross rated maximum capacity (Book Value).
    rated_gross_max_p = ActivePower
    # Generating unit economic participation factor
    normal_pf = db.FloatProperty()
    # The variable cost component of production per unit of ActivePower.
    variable_cost = Money
    # The initial startup cost incurred for each start of the GeneratingUnit.
    startup_cost = Money
    # Generating unit economic participation factor
    long_pf = db.FloatProperty()
    # The planned unused capacity (spinning reserve) which can be used to support emergency load
    alloc_spin_res_p = ActivePower
    # Generating unit economic participation factor
    tie_line_pf = db.FloatProperty()
    fast_start_flag = db.BooleanProperty()
    # The nominal power of the generating unit.  Used to give precise meaning to percentage based attributes such as the govenor speed change droop (govenorSCD attribute).
    nominal_p = ActivePower
    # This is the maximum operating active power limit the dispatcher can enter for this unit
    max_operating_p = ActivePower
    fuel_priority = db.IntegerProperty()
    raise_ramp_rate = ActivePowerChangeRate
    # Defined as: 1 / ( 1 - Incremental Transmission Loss); with the Incremental Transmission Loss expressed as a plus or minus value. The typical range of penalty factors is (0.9 to 1.1).
    penalty_factor = db.FloatProperty()
#    registered_generator = db.ReferenceProperty()
    # The 'control_area_generating_unit' property has been implicitly created by
    # the generating_unit' property of ControlAreaGeneratingUnit.
    pass
#    sub_control_area = db.ReferenceProperty()
#    gen_unit_op_schedule = db.ReferenceProperty()
#    operated_by_generation_provider = db.ReferenceProperty()
    # The 'synchronous_machines' property has been implicitly created by
    # the generating_unit' property of SynchronousMachine.
    pass
    # The 'gross_to_net_active_power_curves' property has been implicitly created by
    # the generating_unit' property of GrossToNetActivePowerCurve.
    pass
    # The 'gen_unit_op_cost_curves' property has been implicitly created by
    # the generating_unit' property of GenUnitOpCostCurve.
    pass

class FuelAllocationSchedule(Curve):
    """ The amount of fuel of a given type which is allocated for consumption over a specified period of time
    """

    # The minimum amount fuel that is allocated for consumption for the scheduled time period, e.g., based on a 'take-or-pay' contract
    min_fuel_allocation = db.FloatProperty()
    # The start time and date of the fuel allocation schedule
    fuel_allocation_start_date = db.DateProperty()
    # The maximum amount fuel that is allocated for consumption for the scheduled time period
    max_fuel_allocation = db.FloatProperty()
    # The type of fuel, which also indicates the corresponding measurement unit
    fuel_type = FuelType
    # The end time and date of the fuel allocation schedule
    fuel_allocation_end_date = db.DateProperty()
#    fossil_fuel = db.ReferenceProperty()
#    thermal_generating_unit = db.ReferenceProperty()

class CAESPlant(PowerSystemResource):
    """ Compressed air energy storage plant
    """

    # The rated energy storage capacity.
    energy_storage_capacity = RealEnergy
    # The CAES plant's gross rated generating capacity
    rated_capacity_p = ActivePower
#    thermal_generating_unit = db.ReferenceProperty()
#    air_compressor = db.ReferenceProperty()

class TargetLevelSchedule(Curve):
    """ Reservoir water level targets from advanced studies or 'rule curves'. Typically in one hour increments for up to 10 days
    """

    # Low target level limit, below which the reservoir operation will be penalized
    low_level_limit = WaterLevel
    # High target level limit, above which the reservoir operation will be penalized
    high_level_limit = WaterLevel
#    reservoir = db.ReferenceProperty()

class HeatRateCurve(Curve):
    """ Relationship between unit heat rate per active power (Y-axis) and  unit output (X-axis). The heat input is from all fuels.
    """

    # Flag is set to true when output is expressed in net active power
    is_net_gross_p = db.BooleanProperty()
#    thermal_generating_unit = db.ReferenceProperty()

class GenUnitOpCostCurve(Curve):
    """ Relationship between unit operating cost (Y-axis) and unit output active power (X-axis). The operating cost curve for thermal units is derived from heat input and fuel costs. The operating cost curve for hydro units is derived from water flow rates and equivalent water costs.
    """

    # Flag is set to true when output is expressed in net active power
    is_net_gross_p = db.BooleanProperty()
#    generating_unit = db.ReferenceProperty()

class StartupModel(IdentifiedObject):
    """ Unit start up characteristics depending on how long the unit has been off line
    """

    # Startup priority within control area where lower numbers indicate higher priorities.  More than one unit in an area may be assigned the same priority.
    startup_priority = db.IntegerProperty()
    # Total miscellaneous start up costs
    startup_cost = Money
    # The amount of heat input per time uint required for hot standby operation
    hot_standby_heat = HeatRate
    # The unit's auxiliary active power consumption to maintain standby mode
    stby_aux_p = ActivePower
    # The opportunity cost associated with the return in monetary unit. This represents the restart's 'share' of the unit depreciation and risk of an event which would damage the unit.
    risk_factor_cost = Money
    # The date and time of the most recent generating unit startup
    startup_date = db.DateProperty()
    # The minimum number of hours the unit must be down before restart
    minimum_down_time = Hours
    # Fixed Maintenance Cost
    fixed_maint_cost = CostRate
    # Incremental Maintenance Cost
    incremental_maint_cost = CostPerEnergyUnit
    # The minimum number of hours the unit must be operating before being allowed to shut down
    minimum_run_time = Hours
#    start_ign_fuel_curve = db.ReferenceProperty()
#    start_main_fuel_curve = db.ReferenceProperty()
#    thermal_generating_unit = db.ReferenceProperty()
#    start_ramp_curve = db.ReferenceProperty()

class FossilFuel(IdentifiedObject):
    """ The fossil fuel consumed by the non-nuclear thermal generating units, e.g., coal, oil, gas
    """

    # The fuel's fraction of pollution credit per unit of heat content
    fuel_sulfur = PU
    # Handling and processing cost associated with this fuel
    fuel_handling_cost = CostPerHeatUnit
    # The efficiency factor for the fuel (per unit) in terms of the effective energy absorbed
    fuel_eff_factor = PU
    # The cost in terms of heat value for the given type of fuel
    fuel_cost = CostPerHeatUnit
    # Relative amount of the given type of fuel, when multiple fuels are being consumed.
    fuel_mixture = PerCent
    # The type of fossil fuel, such as coal, oil, or gas.
    fossil_fuel_type = FuelType
    # The active power output level of the unit at which the given type of fuel is switched off. This fuel (e.g., oil) is sometimes used to stabilize the base fuel (e.g., coal) at low active power output levels.
    low_breakpoint_p = ActivePower
    # The amount of heat per weight (or volume) of the given type of fuel
    fuel_heat_content = db.FloatProperty()
    # The active power output level of the unit at which the given type of fuel is switched on. This fuel (e.g., oil) is sometimes used to supplement the base fuel (e.g., coal) at high active power output levels.
    high_breakpoint_p = ActivePower
    # The cost of fuel used for economic dispatching which includes: fuel cost, transportation cost,  and incremental maintenance cost
    fuel_dispatch_cost = CostPerHeatUnit
    # The 'fuel_allocation_schedules' property has been implicitly created by
    # the fossil_fuel' property of FuelAllocationSchedule.
    pass
#    thermal_generating_unit = db.ReferenceProperty()

class StartMainFuelCurve(Curve):
    """ The quantity of main fuel (Y-axis) used to restart and repay the auxiliary power consumed versus the number of hours (X-axis) the unit was off line
    """

    # Type of main fuel
    main_fuel_type = FuelType
#    startup_model = db.ReferenceProperty()

class CogenerationPlant(PowerSystemResource):
    """ A set of thermal generating units for the production of electrical energy and process steam (usually from the output of the steam turbines). The steam sendout is typically used for industrial purposes or for municipal heating and cooling.
    """

    # The low pressure steam sendout
    cogen_lpsendout_rating = db.FloatProperty()
    # The high pressure steam rating
    cogen_hpsteam_rating = db.FloatProperty()
    # The rated output active power of the cogeneration plant
    rated_p = ActivePower
    # The high pressure steam sendout
    cogen_hpsendout_rating = db.FloatProperty()
    # The low pressure steam rating
    cogen_lpsteam_rating = db.FloatProperty()
#    steam_sendout_schedule = db.ReferenceProperty()
    # The 'thermal_generating_units' property has been implicitly created by
    # the cogeneration_plant' property of ThermalGeneratingUnit.
    pass

class HydroGeneratingEfficiencyCurve(Curve):
    """ Relationship between unit efficiency in percent and unit output active power for a given net head in meters. The relationship between efficiency, discharge, head, and power output is expressed as follows:   E =KP/HQ Where:  (E=percentage)  (P=active power)  (H=height)  (Q=volume/time unit)  (K=constant) For example, a curve instance for a given net head could relate efficiency (Y-axis) versus active power output (X-axis) or versus discharge on the X-axis.
    """

#    hydro_generating_unit = db.ReferenceProperty()

class GenUnitOpSchedule(RegularIntervalSchedule):
    """ The generating unit's Operator-approved current operating schedule (or plan), typically produced with the aid of unit commitment type analyses. The X-axis represents absolute time. The Y1-axis represents the status (0=off-line and unavailable: 1=available: 2=must run: 3=must run at fixed power value: etc.). The Y2-axis represents the must run fixed power value where required.
    """

#    generating_unit = db.ReferenceProperty()

class PenstockLossCurve(Curve):
    """ Relationship between penstock head loss (in meters) and  total discharge through the penstock (in cubic meters per second). One or more turbines may be connected to the same penstock.
    """

#    hydro_generating_unit = db.ReferenceProperty()

class HeatInputCurve(Curve):
    """ Relationship between unit heat input in energy per time for main fuel (Y1-axis) and supplemental fuel (Y2-axis) versus unit output in active power (X-axis). The quantity of main fuel used to sustain generation at this output level is prorated for throttling between definition points. The quantity of supplemental fuel used at this output level is fixed and not prorated.
    """

    # Power output - auxiliary power multiplier adjustment factor.
    aux_power_mult = PU
    # Heat input - offset adjustment factor.
    heat_input_offset = HeatRate
    # Flag is set to true when output is expressed in net active power
    is_net_gross_p = db.BooleanProperty()
    # Heat input - efficiency multiplier adjustment factor.
    heat_input_eff = PU
    # Power output - auxiliary power offset adjustment factor
    aux_power_offset = ActivePower
#    thermal_generating_unit = db.ReferenceProperty()

class StartIgnFuelCurve(Curve):
    """ The quantity of ignition fuel (Y-axis) used to restart and repay the auxiliary power consumed versus the number of hours (X-axis) the unit was off line
    """

    # Type of ignition fuel
    ignition_fuel_type = FuelType
#    startup_model = db.ReferenceProperty()

class TailbayLossCurve(Curve):
    """ Relationship between tailbay head loss hight (y-axis) and the total discharge into the power station's tailbay volume per time unit (x-axis) . There could be more than one curve depending on the level of the tailbay reservoir or river level
    """

#    hydro_generating_unit = db.ReferenceProperty()

class StartRampCurve(Curve):
    """ Rate in gross active power/minute (Y-axis) at which a unit can be loaded versus the number of hours (X-axis) the unit was off line
    """

    # The startup ramp rate in gross for a unit that is on hot standby
    hot_standby_ramp = ActivePowerChangeRate
#    startup_model = db.ReferenceProperty()

class IncrementalHeatRateCurve(Curve):
    """ Relationship between unit incremental heat rate in (delta energy/time) per (delta active power) and unit output in active power. The IHR curve represents the slope of the HeatInputCurve. Note that the 'incremental heat rate' and the 'heat rate' have the same engineering units.
    """

    # Flag is set to true when output is expressed in net active power
    is_net_gross_p = db.BooleanProperty()
#    thermal_generating_unit = db.ReferenceProperty()

class CombinedCyclePlant(PowerSystemResource):
    """ A set of combustion turbines and steam turbines where the exhaust heat from the combustion turbines is recovered to make steam for the steam turbines, resulting in greater overall plant efficiency
    """

    # The combined cycle plant's active power output rating
    comb_cycle_plant_rating = ActivePower
    # The 'thermal_generating_units' property has been implicitly created by
    # the combined_cycle_plant' property of ThermalGeneratingUnit.
    pass

class InflowForecast(RegularIntervalSchedule):
    """ Natural water inflow to a reservoir, usually forecasted from predicted rain and snowmelt. Typically in one hour increments for up to 10 days. The forecast is given in average cubic meters per second over the time increment.
    """

#    reservoir = db.ReferenceProperty()

class SteamSendoutSchedule(RegularIntervalSchedule):
    """ The cogeneration plant's steam sendout schedule in volume per time unit.
    """

#    cogeneration_plant = db.ReferenceProperty()

class HydroPowerPlant(PowerSystemResource):
    """ A hydro power station which can generate or pump. When generating, the generator turbines receive there water from an upper reservoir. When pumping, the pumps receive their water from a lower reservoir.
    """

    # The hydro plant's generating rating active power for rated head conditions
    gen_rated_p = ActivePower
    # The plant's rated gross head
    plant_rated_head = Length
    # Water travel delay from tailbay to next downstream hydro power station
    discharge_travel_delay = Seconds
    # The level at which the surge tank spills
    surge_tank_crest_level = WaterLevel
    # Type and configuration of hydro plant penstock(s)
    penstock_type = PenstockType
    # The type of hydro power plant.
    hydro_plant_type = HydroPlantType
    # Total plant discharge capacity in cubic meters per second
    plant_discharge_capacity = db.FloatProperty()
    # The hydro plant's pumping rating active power for rated head conditions
    pump_rated_p = ActivePower
    # A code describing the type (or absence) of surge tank that is associated with the hydro power plant
    surge_tank_code = SurgeTankCode
#    reservoir = db.ReferenceProperty()
    # The 'hydro_pumps' property has been implicitly created by
    # the hydro_power_plant' property of HydroPump.
    pass
#    gen_source_pump_discharge_reservoir = db.ReferenceProperty()
    # The 'hydro_generating_units' property has been implicitly created by
    # the hydro_power_plant' property of HydroGeneratingUnit.
    pass

class HydroPumpOpSchedule(RegularIntervalSchedule):
    """ The hydro pump's Operator-approved current operating schedule (or plan), typically produced with the aid of unit commitment type analyses.The unit's operating schedule status is typically given as: (0=unavailable)  (1=avilable to startup or shutdown)  (2=must pump)
    """

#    hydro_pump = db.ReferenceProperty()

class ThermalGeneratingUnit(GeneratingUnit):
    """ A generating unit whose prime mover could be a steam turbine, combustion turbine, or diesel engine.
    """

    # Operating and maintenance cost for the thermal unit
    o_mcost = CostPerHeatUnit
#    heat_input_curve = db.ReferenceProperty()
    # The 'emission_curves' property has been implicitly created by
    # the thermal_generating_unit' property of EmissionCurve.
    pass
#    incremental_heat_rate_curve = db.ReferenceProperty()
    # The 'fuel_allocation_schedules' property has been implicitly created by
    # the thermal_generating_unit' property of FuelAllocationSchedule.
    pass
#    cogeneration_plant = db.ReferenceProperty()
#    startup_model = db.ReferenceProperty()
    # The 'fossil_fuels' property has been implicitly created by
    # the thermal_generating_unit' property of FossilFuel.
    pass
#    combined_cycle_plant = db.ReferenceProperty()
#    caesplant = db.ReferenceProperty()
#    heat_rate_curve = db.ReferenceProperty()
    # The 'emmission_accounts' property has been implicitly created by
    # the thermal_generating_unit' property of EmissionAccount.
    pass
#    shutdown_curve = db.ReferenceProperty()

class HydroGeneratingUnit(GeneratingUnit):
    """ A generating unit whose prime mover is a hydraulic turbine (e.g., Francis, Pelton, Kaplan)
    """

    # The equivalent cost of water that drives the hydro turbine, expressed as cost per volume.
    hydro_unit_water_cost = db.FloatProperty()
    # Energy conversion capability for generating.
    energy_conversion_capability = HydroEnergyConversionKind
#    penstock_loss_curve = db.ReferenceProperty()
    # The 'tailbay_loss_curve' property has been implicitly created by
    # the hydro_generating_unit' property of TailbayLossCurve.
    pass
#    hydro_power_plant = db.ReferenceProperty()
    # The 'hydro_generating_efficiency_curves' property has been implicitly created by
    # the hydro_generating_unit' property of HydroGeneratingEfficiencyCurve.
    pass

class WindGeneratingUnit(GeneratingUnit):
    """ A wind driven generating unit.
    """

    pass

class NuclearGeneratingUnit(GeneratingUnit):
    """ A nuclear generating unit.
    """

    pass


