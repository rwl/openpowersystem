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

from cim14.iec61970.domain import PU
from cim14.iec61970.domain import Seconds
from cim14.iec61970.domain import RotationSpeed
from cim14.iec61970.domain import ActivePower
from cim14.iec61970.domain import Temperature

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

TurbineType = db.StringProperty(choices=("kaplan", "pelton", "francis"))

BoilerControlMode = db.StringProperty(choices=("following", "coordinated"))

ns_prefix = "cim.IEC61970.Generation.GenerationDynamics"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#IEC61970.Generation.GenerationDynamics"

class SteamSupply(PowerSystemResource):
    """ Steam supply for steam turbine
    """

    # Rating of steam supply
    steam_supply_rating = db.FloatProperty()
#    steam_turbines = db.ListProperty(db.Key)

#    @property
#    def steam_supplys(self):
#        return SteamTurbine.gql("WHERE steam_turbines = :1", self.key())

class PrimeMover(PowerSystemResource):
    """ The machine used to develop mechanical energy used to drive a generator.
    """

    # Rating of prime mover
    prime_mover_rating = db.FloatProperty()
#    synchronous_machines = db.ListProperty(db.Key)

#    @property
#    def prime_movers(self):
#        return SynchronousMachine.gql("WHERE synchronous_machines = :1", self.key())

class CTTempActivePowerCurve(Curve):
    """ Relationship between the combustion turbine's power output rating in gross active power (X-axis) and the ambient air temperature (Y-axis)
    """

#    combustion_turbine = db.ReferenceProperty()

class BWRSteamSupply(SteamSupply):
    """ Boiling water reactor used as a steam supply to a steam turbine
    """

    # Pressure Limit
    pressure_limit = PU
    # Pressure Setpoint Gain Adjuster
    pressure_setpoint_ga = db.FloatProperty()
    # In-Core Thermal Time Constant
    in_core_thermal_tc = Seconds
    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rf_aux6 = PU
    # Pressure Setpoint Time Constant
    pressure_setpoint_tc1 = Seconds
    # High Power Limit
    high_power_limit = PU
    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rf_aux4 = PU
    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rf_aux2 = PU
    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rf_aux8 = PU
    # Initial Lower Limit
    lower_limit = PU
    # Integral Gain
    integral_gain = db.FloatProperty()
    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rf_aux5 = PU
    # Rod Pattern
    rod_pattern = PU
    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rf_aux1 = PU
    # Pressure Setpoint Time Constant
    pressure_setpoint_tc2 = Seconds
    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rf_aux7 = PU
    # Low Power Limit
    low_power_limit = PU
    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rf_aux3 = PU
    # Constant Associated With Rod Pattern
    rod_pattern_constant = db.FloatProperty()
    # Proportional Gain
    proportional_gain = db.FloatProperty()
    # Initial Upper Limit
    upper_limit = PU

class HydroTurbine(PrimeMover):
    """ A water driven prime mover. Typical turbine types are: Francis, Kaplan, and Pelton.
    """

    # Transient Regulation
    transient_regulation = PU
    # Water Starting Time
    water_starting_time = Seconds
    # Gate Rate Limit
    gate_rate_limit = db.FloatProperty()
    # Transient Droop Time Constant
    transient_droop_time = Seconds
    # Rated speed in number of revolutions.
    speed_rating = RotationSpeed
    # Maximum efficiency active power at maximum head conditions
    max_head_max_p = ActivePower
    # Type of turbine.
    turbine_type = TurbineType
    # Gate Upper Limit
    gate_upper_limit = PU
    # Speed Regulation
    speed_regulation = PU
    # Maximum efficiency active power at minimum head conditions
    min_head_max_p = ActivePower
    # Rated turbine active power
    turbine_rating = ActivePower

class FossilSteamSupply(SteamSupply):
    """ Fossil fueled boiler (e.g., coal, oil, gas)
    """

    # Pressure Control Proportional Gain ratio
    pressure_ctrl_pg = db.FloatProperty()
    # Pressure Control Integral Gain ratio
    pressure_ctrl_ig = db.FloatProperty()
    # Off nominal frequency effect on auxiliary real power. Per unit active power variation versus per unit frequency variation.
    aux_power_versus_frequency = PU
    # Throttle Pressure Setpoint
    throttle_pressure_sp = PU
    # Off nominal voltage effect on auxiliary real power. Per unit active power variation versus per unit voltage variation.
    aux_power_versus_voltage = PU
    # Superheater Pipe Pressure Drop Constant
    super_heater_pipe_pd = db.FloatProperty()
    # Pressure Control Derivative Gain ratio
    pressure_ctrl_dg = db.FloatProperty()
    # Secondary Superheater Capacity
    super_heater2_capacity = db.FloatProperty()
    # Active power Error Bias ratio
    control_error_bias_p = db.FloatProperty()
    # Proportional Constant
    control_pc = db.FloatProperty()
    # Mechanical Power Sensor Lag
    mech_power_sensor_lag = Seconds
    # The control mode of the boiler
    boiler_control_mode = BoilerControlMode
    # Time Constant
    control_tc = db.FloatProperty()
    # Feedwater Time Constant rato
    feed_water_tc = Seconds
    # Feedwater Proportional Gain ratio
    feed_water_pg = db.FloatProperty()
    # Fuel Supply Time Constant
    fuel_supply_tc = Seconds
    # Active power Minimum Error Rate Limit
    min_error_rate_p = db.FloatProperty()
    # Integral Constant
    control_ic = db.FloatProperty()
    # Fuel Demand Limit
    fuel_demand_limit = PU
    # Pressure Feedback Indicator
    pressure_feedback = db.IntegerProperty()
    # Pressure Error Bias ratio
    control_peb = db.FloatProperty()
    # Fuel Delay
    fuel_supply_delay = Seconds
    # Feedwater Integral Gain ratio
    feed_water_ig = db.FloatProperty()
    # Drum/Primary Superheater Capacity
    super_heater1_capacity = db.FloatProperty()
    # Pressure Error Deadband
    control_ped = PU
    # Active power Maximum Error Rate Limit
    max_error_rate_p = db.FloatProperty()

class PWRSteamSupply(SteamSupply):
    """ Pressurized water reactor used as a steam supply to a steam turbine
    """

    # Cold Leg Feedback Lead Time Constant
    cold_leg_fblead_tc1 = PU
    # Throttle Pressure Setpoint
    throttle_pressure_sp = PU
    # Cold Leg Feedback Gain 1
    cold_leg_fg1 = PU
    # Cold Leg Feedback Lag Time Constant
    cold_leg_fblag_tc = PU
    # Core Heat Transfer Lag Time Constant
    core_htlag_tc1 = PU
    # Hot Leg Lag Time Constant
    hot_leg_lag_tc = PU
    # Core Neutronics And Heat Transfer
    core_neutronics_ht = PU
    # Steam Pressure Feedback Gain
    steam_pressure_fg = PU
    # Throttle Pressure Factor
    throttle_pressure_factor = PU
    # Hot Leg To Cold Leg Gain
    hot_leg_to_cold_leg_gain = PU
    # Steam Pressure Drop Lag Time Constant
    steam_pressure_drop_lag_tc = PU
    # Pressure Control Gain
    pressure_cg = PU
    # Cold Leg Feedback Lead Time Constant
    cold_leg_fblead_tc2 = PU
    # Feedback Factor
    feedback_factor = PU
    # Steam Flow Feedback Gain
    steam_flow_fg = PU
    # Cold Leg Lag Time Constant
    cold_leg_lag_tc = PU
    # Hot Leg Steam Gain
    hot_leg_steam_gain = PU
    # Core Neutronics Effective Time Constant
    core_neutronics_eff_tc = PU
    # Cold Leg Feedback Gain 2
    cold_leg_fg2 = PU
    # Core Heat Transfer Lag Time Constant
    core_htlag_tc2 = PU

class CombustionTurbine(PrimeMover):
    """ A prime mover that is typically fueled by gas or light oil
    """

    # The time constant for the turbine.
    time_constant = Seconds
    # Reference temperature at which the output of the turbine was defined.
    reference_temp = Temperature
    # Off-nominal voltage effect on turbine auxiliaries. Per unit reduction in auxiliary active power consumption versus per unit reduction in auxiliary bus voltage (from a specified voltage level).
    aux_power_versus_voltage = PU
    # Per unit change in power per (versus) unit change in ambient temperature
    power_variation_by_temp = PU
    # Off-nominal frequency effect on turbine capability. Per unit reduction in unit active power capability versus per unit reduction in frequency (from rated frequency).
    capability_versus_frequency = PU
    # Default ambient temperature to be used in modeling applications
    ambient_temp = Temperature
    # Flag that is set to true if the combustion turbine is associated with a heat recovery boiler
    heat_recovery_flag = db.BooleanProperty()
    # Off-nominal frequency effect on turbine auxiliaries. Per unit reduction in auxiliary active power consumption versus per unit reduction in frequency (from rated frequency).
    aux_power_versus_frequency = PU
#    air_compressor = db.ReferenceProperty()
#    heat_recovery_boiler = db.ReferenceProperty()
#    cttemp_active_power_curve = db.ReferenceProperty()

class Supercritical(FossilSteamSupply):
    """ Once-through supercritical boiler
    """

    pass

class SteamTurbine(PrimeMover):
    """ Steam turbine
    """

    # Steam Chest Time Constant
    steam_chest_tc = Seconds
    # Fraction Of Power From Shaft 2 Second Low Pressure Turbine output
    shaft2_power_lp2 = db.FloatProperty()
    # Crossover Time Constant
    crossover_tc = Seconds
    # Fraction Of Power From Shaft 1 First Low Pressure Turbine output
    shaft1_power_lp1 = db.FloatProperty()
    # First Reheater Time Constant
    reheater1_tc = Seconds
    # Fraction Of Power From Shaft 1 High Pressure Turbine output
    shaft1_power_hp = db.FloatProperty()
    # Fraction Of Power From Shaft 2 High Pressure Turbine output
    shaft2_power_hp = db.FloatProperty()
    # Fraction Of Power From Shaft 2 First Low Pressure Turbine output
    shaft2_power_lp1 = db.FloatProperty()
    # Fraction Of Power From Shaft 1 Intermediate Pressure Turbine output
    shaft1_power_ip = db.FloatProperty()
    # Fraction Of Power From Shaft 1 Second Low Pressure Turbine output
    shaft1_power_lp2 = db.FloatProperty()
    # Second Reheater Time Constant
    reheater2_tc = Seconds
    # Fraction Of Power From Shaft 2 Intermediate Pressure Turbine output
    shaft2_power_ip = db.FloatProperty()
#    steam_supplys = db.ListProperty(db.Key)

#    @property
#    def steam_turbines(self):
#        return SteamSupply.gql("WHERE steam_supplys = :1", self.key())

class Subcritical(FossilSteamSupply):
    """ Once-through subcritical boiler
    """

    pass

class DrumBoiler(FossilSteamSupply):
    """ Drum boiler
    """

    # Rating of drum boiler in steam units
    drum_boiler_rating = db.FloatProperty()

class HeatRecoveryBoiler(FossilSteamSupply):
    """ The heat recovery system associated with combustion turbines in order to produce steam for combined cycle plants
    """

    # The steam supply rating in kilopounds per hour, if dual pressure boiler
    steam_supply_rating2 = db.FloatProperty()
    # The 'combustion_turbines' property has been implicitly created by
    # the heat_recovery_boiler' property of CombustionTurbine.
    pass


