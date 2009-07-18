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

from cim14.iec61970.core import ConductingEquipment
from cim14.iec61970.core import PowerSystemResource
from cim14.iec61970.core import EquipmentContainer
from cim14.iec61970.core import Curve
from cim14.iec61970.core import RegularIntervalSchedule
from cim14.iec61970.core import Equipment
from cim14.iec61970.core import IdentifiedObject

from cim14.iec61970.domain import Resistance
from cim14.iec61970.domain import ApparentPower
from cim14.iec61970.domain import Voltage
from cim14.iec61970.domain import Reactance
from cim14.iec61970.domain import Conductance
from cim14.iec61970.domain import Susceptance
from cim14.iec61970.domain import ActivePower
from cim14.iec61970.domain import Frequency
from cim14.iec61970.domain import CurrentFlow
from cim14.iec61970.domain import Seconds
from cim14.iec61970.domain import ReactivePower
from cim14.iec61970.domain import PU
from cim14.iec61970.domain import PerCent
from cim14.iec61970.domain import Damping
from cim14.iec61970.domain import VoltagePerReactivePower
from cim14.iec61970.domain import Inductance
from cim14.iec61970.domain import Pressure
from cim14.iec61970.domain import Temperature
from cim14.iec61970.domain import Admittance
from cim14.iec61970.domain import KWActivePower
from cim14.iec61970.domain import Impedance
from cim14.iec61970.domain import AngleDegrees
from cim14.iec61970.domain import AngleRadians
from cim14.iec61970.core import PhaseCode

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

OperatingMode = db.StringProperty()

CompositeSwitchType = db.StringProperty()

CoolantType = db.StringProperty(choices=("water", "air", "hydrogen_gas"))

TapChangerKind = db.StringProperty(choices=("phase_control", "fixed", "voltage_control", "voltage_and_phase_control"))

SynchronousMachineOperatingMode = db.StringProperty(choices=("generator", "condenser"))

RegulatingControlModeKind = db.StringProperty(choices=("admittance", "fixed", "active_power", "current_flow", "voltage", "reactive_power"))

PhaseTapChangerKind = db.StringProperty(choices=("unknown", "asymmetrical", "symmetrical"))

SVCControlMode = db.StringProperty(choices=("off", "reactive_power", "voltage"))

WindingType = db.StringProperty(choices=("primary", "secondary", "quaternary", "tertiary"))

WindingConnection = db.StringProperty(choices=("zn", "y", "d", "z", "yn"))

TransformerControlMode = db.StringProperty(choices=("local", "off", "volt", "active", "reactive"))

SynchronousMachineType = db.StringProperty(choices=("generator", "condenser", "generator_or_condenser"))

ns_prefix = "cim.IEC61970.Wires"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#IEC61970.Wires"

class TransformerWinding(ConductingEquipment):
    """ A winding is associated with each defined terminal of a transformer (or phase shifter).
    """

    # Set if the winding is grounded.
    grounded = db.BooleanProperty()
    # Zero sequence series resistance of the winding.
    r0 = Resistance
    # The apparent power that the winding can carry  under emergency conditions.
    emergency_s = ApparentPower
    # Basic insulation level voltage rating
    insulation_u = Voltage
    # Ground reactance path through connected grounding transformer.
    xground = Reactance
    # Positive sequence series reactance of the winding.
    x = Reactance
    # Zero sequence magnetizing branch conductance.
    g0 = Conductance
    # Zero sequence magnetizing branch susceptance.
    b0 = Susceptance
    # The type of connection of the winding.
    connection_type = WindingConnection
    # Zero sequence series reactance of the winding.
    x0 = Reactance
    # Ground resistance path through connected grounding transformer.
    rground = Resistance
    # Apparent power that the winding can carry for a short period of time.
    short_term_s = ApparentPower
    # Magnetizing branch conductance (G mag).
    g = Conductance
    # The normal apparent power rating for the winding
    rated_s = ApparentPower
    # Magnetizing branch susceptance (B mag).
    b = Susceptance
    # The type of winding.
    winding_type = WindingType
    # Positive sequence series resistance of the winding.
    r = Resistance
    # The rated voltage (phase-to-phase) of the winding, usually the same as the neutral voltage.
    rated_u = Voltage
    # The 'from_winding_insulations' property has been implicitly created by
    # the from_transformer_winding' property of WindingInsulation.
    pass
    # The 'to_winding_test' property has been implicitly created by
    # the to_transformer_winding' property of WindingTest.
    pass
#    ratio_tap_changer = db.ReferenceProperty()
#    power_transformer = db.ReferenceProperty()
    # The 'from_winding_test' property has been implicitly created by
    # the from_transformer_winding' property of WindingTest.
    pass
#    phase_tap_changer = db.ReferenceProperty()
    # The 'to_winding_insulations' property has been implicitly created by
    # the to_transformer_winding' property of WindingInsulation.
    pass

class RegulatingControl(PowerSystemResource):
    """ Specifies a set of equipment that works together to control a power system quantity such as voltage or flow.
    """

    # This is the case input target range.   This performs the same function as the value2 attribute on the regulation schedule in the case that schedules are not used.   The units of those appropriate for the mode.
    target_range = db.FloatProperty()
    # The regulation is performed in a discrete mode.
    discrete = db.BooleanProperty()
    # The target value specified for case input.   This value can be used for the target value wihout the use of schedules. The value has the units appropriate to the mode attribute.
    target_value = db.FloatProperty()
    # The regulating control mode presently available.  This specifications allows for determining the kind of regualation without need for obtaining the units from a schedule.
    mode = RegulatingControlModeKind
    # The 'tap_changer' property has been implicitly created by
    # the regulating_control' property of TapChanger.
    pass
    # The 'regulating_cond_eq' property has been implicitly created by
    # the regulating_control' property of RegulatingCondEq.
    pass
#    regulation_schedule = db.ReferenceProperty()
#    terminal = db.ReferenceProperty()

class RegulatingCondEq(ConductingEquipment):
    """ RegulatingCondEq is a type of ConductingEquipment that can regulate Measurements and have a RegulationSchedule.
    """

#    regulating_control = db.ReferenceProperty()
    # The 'controls' property has been implicitly created by
    # the regulating_cond_eq' property of Control.
    pass

class RectifierInverter(ConductingEquipment):
    """ Bi-directional AC-DC conversion equipment that can be used to control DC current, DC voltage, DC power flow, or firing angle.
    """

    # The minimum active power on the DC side at which the converter should operate.
    min_p = ActivePower
    # Operating mode for the converter.
    operating_mode = OperatingMode
    # Compounding resistance.
    compound_resistance = Resistance
    # Rectifier/inverter primary base voltage
    rated_u = Voltage
    # Commutating reactance at AC bus frequency.
    commutating_reactance = Reactance
    # Number of bridges
    bridges = db.IntegerProperty()
    # The maximum voltage on the DC side at which the converter should operate.
    max_u = Voltage
    # Frequency on the AC side.
    frequency = Frequency
    # The maximum active power on the DC side at which the fconverter should operate.
    max_p = ActivePower
    # Minimum compounded DC voltage
    min_compound_voltage = Voltage
    # The minimum voltage on the DC side at which the converter should operate.
    min_u = Voltage
    # Commutating resistance.
    commutating_resistance = Resistance

class Switch(ConductingEquipment):
    """ A generic device designed to close, or open, or both, one or more electric circuits.
    """

    # The switch on count since the switch was last reset or initialized.
    switch_on_count = db.IntegerProperty()
    # The attribute is used in cases when no Measurement for the status value is present. If the Switch has a status measurment the Discrete.normalValue is expected to match with the Switch.normalOpen.
    normal_open = db.BooleanProperty()
    # Branch is retained in a bus branch model.
    retained = db.BooleanProperty()
    # The date and time when the switch was last switched on.
    switch_on_date = db.DateProperty()
#    connect_disconnect_functions = db.ListProperty(db.Key)

#    @property
#    def switches(self):
#        return ConnectDisconnectFunction.gql("WHERE connect_disconnect_functions = :1", self.key())
#    composite_switch = db.ReferenceProperty()
#    load_mgmt_functions = db.ListProperty(db.Key)

#    @property
#    def switches(self):
#        return LoadMgmtFunction.gql("WHERE load_mgmt_functions = :1", self.key())
#    switching_operations = db.ListProperty(db.Key)

#    @property
#    def switches(self):
#        return SwitchingOperation.gql("WHERE switching_operations = :1", self.key())

class Line(EquipmentContainer):
    """ A component part of a system extending between adjacent substations or from a substation to an adjacent interconnection point.
    """

#    transmission_right_of_way = db.ReferenceProperty()
#    region = db.ReferenceProperty()
#    flowgates = db.ListProperty(db.Key)

#    @property
#    def lines(self):
#        return Flowgate.gql("WHERE flowgates = :1", self.key())

class ReactiveCapabilityCurve(Curve):
    """ Reactive power rating envelope versus the synchronous machine's active power, in both the generating and motoring modes. For each active power value there is a corresponding high and low reactive power limit  value. Typically there will be a separate curve for each coolant condition, such as hydrogen pressure.  The Y1 axis values represent reactive minimum and the Y2 axis values represent reactive maximum.
    """

    # The hydrogen coolant pressure
    hydrogen_pressure = Pressure
    # The machine's coolant temperature (e.g., ambient air or stator circulating water).
    coolant_temperature = Temperature
#    synchronous_machines = db.ListProperty(db.Key)

#    @property
#    def reactive_capability_curves(self):
#        return SynchronousMachine.gql("WHERE synchronous_machines = :1", self.key())
    # The 'initially_used_by_synchronous_machines' property has been implicitly created by
    # the initial_reactive_capability_curve' property of SynchronousMachine.
    pass

class SeriesCompensator(ConductingEquipment):
    """ A Series Compensator is a series capacitor or reactor or an AC transmission line without charging susceptance.  It is a two terminal device.
    """

    # Positive sequence resistance.
    r = Resistance
    # Positive sequence reactance.
    x = Reactance

class EnergyConsumer(ConductingEquipment):
    """ Generic user of energy - a  point of consumption on the power system model
    """

    # Number of individual customers represented by this Demand
    customer_count = db.IntegerProperty()
    # Active power of the load that is a fixed quantity.
    pfixed = ActivePower
    # Fixed reactive power as per cent of load group fixed reactive power.
    qfixed_pct = PerCent
    # Fixed active power as per cent of load group fixed active power
    pfixed_pct = PerCent
    # Reactive power of the load that is a fixed quantity.
    qfixed = ReactivePower
    # The 'service_delivery_points' property has been implicitly created by
    # the energy_consumer' property of ServiceDeliveryPoint.
    pass
    # The 'phase_loads' property has been implicitly created by
    # the energy_consumer' property of PhaseLoad.
    pass
#    power_cut_zone = db.ReferenceProperty()
#    load_response = db.ReferenceProperty()

class RegulationSchedule(RegularIntervalSchedule):
    """ A pre-established pattern over time for a controlled variable, e.g., busbar voltage.
    """

    # Line drop resistance.
    line_drop_r = Resistance
    # Flag to indicate that line drop compensation is to be applied
    line_drop_compensation = db.BooleanProperty()
    # Line drop reactance.
    line_drop_x = Reactance
    # The 'regulating_control' property has been implicitly created by
    # the regulation_schedule' property of RegulatingControl.
    pass
    # The 'voltage_control_zones' property has been implicitly created by
    # the regulation_schedule' property of VoltageControlZone.
    pass

class Connector(ConductingEquipment):
    """ A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation and are modelled with a single logical terminal.
    """

    pass

class Resistor(ConductingEquipment):
    """ Resistor, typically used in filter configurations or as earthing resistor for transformers.  Used for electrical model of distribution networks.
    """

#    resistor_type_asset = db.ReferenceProperty()
#    resistor_asset = db.ReferenceProperty()

class CompositeSwitch(Equipment):
    """ A model of a set of individual Switches normally enclosed within the same cabinet and possibly with interlocks that restrict the combination of switch positions. These are typically found in medium voltage distribution networks.  A CompositeSwitch could represent a Ring-Main-Unit (RMU), or pad-mounted switchgear, with primitive internal devices such as an internal bus-bar plus 3 or 4 internal switches each of which may individually be open or closed. A CompositeSwitch and a set of contained Switches can also be used to represent a multi-position switch e.g. a switch that can connect a circuit to Ground, Open or Busbar.
    """

    # An alphanumeric code that can be used as a reference to extar information such as the description of the interlocking scheme if any
    composite_switch_type = CompositeSwitchType
    # The 'switches' property has been implicitly created by
    # the composite_switch' property of Switch.
    pass

class WindingTest(IdentifiedObject):
    """ Physical winding test data for the winding/tap pairs of a transformer (or phase shifter). This test data can be used to derive other attributes of specific transformer or phase shifter models.
    """

    # The voltage measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited.
    voltage = Voltage
    # The exciting current on open-circuit test, expressed as a percentage of rated current, at nominal voltage
    exciting_current = PerCent
    # The no load loss kW 'to' winding open-circuited) from the test report.
    no_load_loss = KWActivePower
    # The leakage impedance measured at the 'from' winding  with the 'to' winding short-circuited and all other windings open-circuited.  Leakage impedance is expressed in units based on the apparent power and voltage ratings of the 'from' winding.
    leakage_impedance = Impedance
    # The load loss kW ('to' winding short-circuited) from the test report.
    load_loss = KWActivePower
    # The tap step number for the 'to' winding of the test pair.
    to_tap_step = db.IntegerProperty()
    # The phase shift measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited.
    phase_shift = AngleDegrees
    # The tap step number for the 'from' winding of the test pair.
    from_tap_step = db.IntegerProperty()
#    from_transformer_winding = db.ReferenceProperty()
#    to_transformer_winding = db.ReferenceProperty()
#    transformer_observations = db.ListProperty(db.Key)

#    @property
#    def winding_tests(self):
#        return TransformerObservation.gql("WHERE transformer_observations = :1", self.key())

class TapChanger(PowerSystemResource):
    """ Mechanism for changing transformer winding tap positions.
    """

    # The tap step position used in 'normal' network operation for this winding. For a 'Fixed' tap changer indicates the current physical tap setting.
    normal_step = db.IntegerProperty()
    # Lowest possible tap step position, retard from neutral
    low_step = db.IntegerProperty()
    # Tap step increment, in per cent of nominal voltage, per step position.
    step_voltage_increment = PerCent
    # Highest possible tap step position, advance from neutral
    high_step = db.IntegerProperty()
    # For an LTC, the delay for initial tap changer operation (first step change)
    initial_delay = Seconds
    # The type of tap changer. Indicates the ability of the transformer to perform various regulation tasks. The tap changer must be also be associated wtih a RegulationControl object before any regulation is possible.
    type = TapChangerKind
    # For an LTC, the tap changer control mode.
    tcul_control_mode = TransformerControlMode
    # For an LTC, the delay for subsequent tap changer operation (second and later step changes)
    subsequent_delay = Seconds
    # The neutral tap step position for this winding.
    neutral_step = db.IntegerProperty()
    # Voltage at which the winding operates at the neutral tap setting.
    neutral_u = Voltage
#    sv_tap_step = db.ReferenceProperty()
#    regulating_control = db.ReferenceProperty()

class HeatExchanger(Equipment):
    """ Equipment for the cooling of electrical equipment and the extraction of heat
    """

#    power_transformer = db.ReferenceProperty()

class MutualCoupling(IdentifiedObject):
    """ This class represents the zero sequence line mutual coupling.
    """

    # Zero sequence mutual coupling shunt (charging) susceptance, uniformly distributed, of the entire line section.
    b0ch = Susceptance
    # Zero sequence mutual coupling shunt (charging) conductance, uniformly distributed, of the entire line section.
    g0ch = Conductance
    # Zero sequence branch-to-branch mutual impedance coupling, resistance
    r0 = Resistance
    # Zero sequence branch-to-branch mutual impedance coupling, reactance
    x0 = Resistance
#    first_terminal = db.ReferenceProperty()
#    second_terminal = db.ReferenceProperty()

class EnergySource(ConductingEquipment):
    """ A generic equivalent for an energy supplier on a transmission or distribution voltage level.
    """

    # Phase angle of a-phase open circuit.
    voltage_angle = AngleRadians
    # Phase-to-phase open circuit voltage magnitude.
    voltage_magnitude = Voltage
    # Zero sequence Thevenin resistance.
    r0 = Resistance
    # Negative sequence Thevenin reactance.
    xn = Reactance
    # Positive sequence Thevenin reactance.
    x = Reactance
    # Phase-to-phase nominal voltage.
    nominal_voltage = Voltage
    # Negative sequence Thevenin resistance.
    rn = Resistance
    # Zero sequence Thevenin reactance.
    x0 = Reactance
    # High voltage source load
    active_power = ActivePower
    # Positive sequence Thevenin resistance.
    r = Resistance

class VoltageControlZone(PowerSystemResource):
    """ An area of the power system network which is defined for secondary voltage control purposes. A voltage control zone consists of a collection of substations with a designated bus bar section whose voltage will be controlled.
    """

#    regulation_schedule = db.ReferenceProperty()
#    busbar_section = db.ReferenceProperty()

class Conductor(ConductingEquipment):
    """ Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system.
    """

    # Zero sequence shunt (charging) conductance, uniformly distributed, of the entire line section.
    g0ch = Conductance
    # Positive sequence shunt (charging) conductance, uniformly distributed, of the entire line section.
    gch = Conductance
    # Positive sequence series reactance of the entire line section.
    x = Reactance
    # Zero sequence series reactance of the entire line section.
    x0 = Reactance
    # Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.
    bch = Susceptance
    # Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.
    b0ch = Susceptance
    # Zero sequence series resistance of the entire line section.
    r0 = Resistance
    # Positive sequence series resistance of the entire line section.
    r = Resistance
#    linear_conductor_type_assets = db.ListProperty(db.Key)

#    @property
#    def conductors(self):
#        return LinearConductorTypeAsset.gql("WHERE linear_conductor_type_assets = :1", self.key())
#    conductor_type = db.ReferenceProperty()
#    linear_conductor_assets = db.ListProperty(db.Key)

#    @property
#    def conductors(self):
#        return LinearConductorAsset.gql("WHERE linear_conductor_assets = :1", self.key())

class Plant(EquipmentContainer):
    """ A Plant is a collection of equipment for purposes of generation.
    """

    pass

class Ground(ConductingEquipment):
    """ A common point for connecting grounded conducting equipment such as shunt capacitors. The power system model can have more than one ground.
    """

    # The 'winding_insulations' property has been implicitly created by
    # the ground' property of WindingInsulation.
    pass

class PowerTransformer(Equipment):
    """ An electrical device consisting of  two or more coupled windings, with or without a magnetic core, for introducing mutual coupling between electric circuits. Transformers can be used to control voltage and phase shift (active power flow).
    """

    # Core shunt magnetizing susceptance in the saturation region.
    bmag_sat = PerCent
    # Core magnetizing saturation curve knee flux level.
    mag_sat_flux = PerCent
    # Describes the phases carried by a power transformer.
    phases = PhaseCode
    # The reference voltage at which the magnetizing saturation measurements were made
    mag_base_u = Voltage
    # The 'transformer_windings' property has been implicitly created by
    # the power_transformer' property of TransformerWinding.
    pass
#    heat_exchanger = db.ReferenceProperty()
#    flowgates = db.ListProperty(db.Key)

#    @property
#    def power_transormers(self):
#        return Flowgate.gql("WHERE flowgates = :1", self.key())

class Disconnector(Switch):
    """ A manually operated or motor operated mechanical switching device used for changing the connections in a circuit, or for isolating a circuit or equipment from a source of power. It is required to open or close circuits when negligible current is broken or made.
    """

    pass

class GroundDisconnector(Switch):
    """ A manually operated or motor operated mechanical switching device used for isolating a circuit or equipment from Ground.
    """

    pass

class Jumper(Switch):
    """ A short section of conductor with negligible impedance which can be manually removed and replaced if the circuit is de-energized. Note that zero-impedance branches can be modelled by an ACLineSegment with a zero impedance ConductorType
    """

    pass

class BusbarSection(Connector):
    """ A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation.  Voltage measurements are typically obtained from VoltageTransformers that are connected to busbar sections. A bus bar section may have many physical terminals but for analysis is modelled with exactly one logical terminal.
    """

#    voltage_control_zone = db.ReferenceProperty()

class SynchronousMachine(RegulatingCondEq):
    """ An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.
    """

    # Modes that this synchronous machine can operate in.
    type = SynchronousMachineType
    # Maximum voltage limit for the unit.
    max_u = Voltage
    # Minimum voltage  limit for the unit.
    min_u = Voltage
    # Direct-axis subtransient reactance, also known as X'd.
    x_direct_subtrans = Reactance
    # Method of cooling the machine.
    coolant_type = CoolantType
    # Active power consumed when in condenser mode operation.
    condenser_p = ActivePower
    # Quadrature-axis synchronous reactance (Xq) , the ratio of the component of reactive armature voltage, due to the quadrature-axis component of armature current, to this component of current, under steady state conditions and at rated frequency.
    x_quad_sync = Reactance
    # Zero sequence resistance of the synchronous machine.
    r0 = Resistance
    # Time delay required when switching from Automatic Voltage Regulation (AVR) to Manual for a leading MVAr violation.
    a_vrto_manual_lead = Seconds
    # Zero sequence reactance of the synchronous machine.
    x0 = Reactance
    # Priority of unit for reference bus selection. 0 = don t care (default) 1 = highest priority. 2 is less than 1 and so on.
    reference_priority = db.IntegerProperty()
    # Positive sequence resistance of the synchronous machine.
    r = Resistance
    # Quadrature-axis transient reactance, also known as X'q.
    x_quad_trans = Reactance
    # Negative sequence resistance.
    r2 = Resistance
    # Default base reactive power value. This value represents the initial reactive power that can be used by any application function.
    base_q = ReactivePower
    # The energy stored in the rotor when operating at rated speed. This value is used in the accelerating power reference frame for  operator training simulator solutions.
    inertia = PU
    # Negative sequence reactance.
    x2 = Reactance
    # Time delay required when switching from Automatic Voltage Regulation (AVR) to Manual for a lagging MVAr violation.
    a_vrto_manual_lag = Seconds
    # Direct-axis transient reactance, also known as X'd.
    x_direct_trans = Reactance
    # Percent of the coordinated reactive control that comes from this machine.
    q_percent = PerCent
    # Temperature or pressure of coolant medium
    coolant_condition = db.FloatProperty()
    # Time delay required when switching from Manual to Automatic Voltage Regulation. This value is used in the accelerating power reference frame for powerflow solutions
    manual_to_avr = Seconds
    # Current mode of operation.
    operating_mode = SynchronousMachineOperatingMode
    # Direct-axis synchronous reactance. The quotient of a sustained value of that AC component of armature voltage that is produced by the total direct-axis flux due to direct-axis armature current and the value of the AC component of this current, the machine running at rated speed. (Xd)
    x_direct_sync = Reactance
    # Maximum reactive power limit. This is the maximum (nameplate) limit for the unit.
    max_q = ReactivePower
    # Damping torque coefficient, a proportionality constant that, when multiplied by the angular velocity of the rotor poles with respect to the magnetic field (frequency), results in the damping torque.
    damping = Damping
    # Nameplate apparent power rating for the unit
    rated_s = ApparentPower
    # Minimum reactive power limit for the unit.
    min_q = ReactivePower
    # Quadrature-axis subtransient reactance, also known as X'q.
    x_quad_subtrans = Reactance
    # Positive sequence reactance of the synchronous machine.
    x = Reactance
#    initial_reactive_capability_curve = db.ReferenceProperty()
#    hydro_pump = db.ReferenceProperty()
#    reactive_capability_curves = db.ListProperty(db.Key)

#    @property
#    def synchronous_machines(self):
#        return ReactiveCapabilityCurve.gql("WHERE reactive_capability_curves = :1", self.key())
#    generating_unit = db.ReferenceProperty()
#    prime_movers = db.ListProperty(db.Key)

#    @property
#    def synchronous_machines(self):
#        return PrimeMover.gql("WHERE prime_movers = :1", self.key())

class StaticVarCompensator(RegulatingCondEq):
    """ A facility for providing variable and controllable shunt reactive power. The SVC typically consists of a stepdown transformer, filter, thyristor-controlled reactor, and thyristor-switched capacitor arms.  The SVC may operate in fixed MVar output mode or in voltage control mode.  When in voltage control mode, the output of the SVC will be proportional to the deviation of voltage at the controlled bus from the voltage setpoint.  The SVC characteristic slope defines the proportion.  If the voltage at the controlled bus is equal to the voltage setpoint, the SVC MVar output is zero.
    """

    # Maximum available capacitive reactive power
    capacitive_rating = Reactance
    # The reactive power output of the SVC is proportional to the difference between the voltage at the regulated bus and the voltage setpoint.  When the regulated bus voltage is equal to the voltage setpoint, the reactive power output is zero.
    voltage_set_point = Voltage
    # SVC control mode.
    s_vccontrol_mode = SVCControlMode
    # The characteristics slope of an SVC defines how the reactive power output changes in proportion to the difference between the regulated bus voltage and the voltage setpoint.
    slope = VoltagePerReactivePower
    # Maximum available inductive reactive power
    inductive_rating = Reactance

class RatioTapChanger(TapChanger):
    """ A tap changer that changes the voltage ratio impacting the voltage magnitude but not direclty the phase angle across the transformer..
    """

#    transformer_winding = db.ReferenceProperty()

class DCLineSegment(Conductor):
    """ A wire or combination of wires not insulated from one another, with consistent electrical characteristics, used to carry direct current between points in the DC region of the power system.
    """

    # Resistance of the DC line segment.
    dc_segment_resistance = Resistance
    # Inductance of the DC line segment.
    dc_segment_inductance = Inductance

class FrequencyConverter(RegulatingCondEq):
    """ A device to convert from one frequency to another (e.g., frequency F1 to F2) comprises a pair of FrequencyConverter instances. One converts from F1 to DC, the other converts the DC to F2.
    """

    # The maximum active power on the DC side at which the frequence converter should operate.
    max_p = ActivePower
    # Frequency on the AC side.
    frequency = Frequency
    # The minimum active power on the DC side at which the frequence converter should operate.
    min_p = ActivePower
    # Operating mode for the frequency converter
    operating_mode = OperatingMode
    # The minimum voltage on the DC side at which the frequency converter should operate.
    min_u = Voltage
    # The maximum voltage on the DC side at which the frequency converter should operate.
    max_u = Voltage

class ACLineSegment(Conductor):
    """ A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system.
    """

    pass

class ShuntCompensator(RegulatingCondEq):
    """ A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  A negative value for reactivePerSection indicates that the compensator is a reactor. ShuntCompensator is a single terminal device.  Ground is implied.
    """

    # Nominal reactive power output of the capacitor bank at the nominal voltage. This number should be positive.
    nom_q = ReactivePower
    # The maximum voltage at which the capacitor bank should operate.
    max_u = Voltage
    # Time delay required for the device to be connected or disconnected by automatic voltage regulation (AVR).
    a_vrdelay = Seconds
    # The nominal voltage at which the nominal reactive power was measured. This should normally be within 10% of the voltage at which the capacitor is connected to the network.
    nom_u = Voltage
    # Voltage sensitivity required for the device to regulate the bus voltage, in voltage/reactive power.
    voltage_sensitivity = VoltagePerReactivePower
    # For a capacitor bank, the size in reactive power of each switchable section at the nominal voltage.
    reactive_per_section = ReactivePower
    # For a capacitor bank, the maximum number of sections that may be switched in.
    maximum_sections = db.IntegerProperty()
    # The date and time when the capacitor bank was last switched on.
    switch_on_date = db.DateProperty()
    # For a capacitor bank, the normal number of sections switched in. This number should correspond to the nominal reactive power (nomQ).
    normal_sections = db.IntegerProperty()
    # Zero sequence shunt (charging) susceptance per section
    b0_per_section = Susceptance
    # The minimum voltage at which the capacitor bank should operate.
    min_u = Voltage
    # Zero sequence shunt (charging) conductance per section
    g0_per_section = Conductance
    # For a capacitor bank, the admittance of each switchable section. Calculated using the reactive power per section and corrected for network voltage.
    y_per_section = Admittance
    # The switch on count since the capacitor count was last reset or initialized.
    switch_on_count = db.IntegerProperty()
#    sv_shunt_compensator_sections = db.ReferenceProperty()

class ProtectedSwitch(Switch):
    """ A ProtectedSwitch is a switching device that can be operated by ProtectionEquipment.
    """

    # The 'reclose_sequences' property has been implicitly created by
    # the protected_switch' property of RecloseSequence.
    pass
#    protection_equipments = db.ListProperty(db.Key)

#    @property
#    def protected_switches(self):
#        return ProtectionEquipment.gql("WHERE protection_equipments = :1", self.key())

class Fuse(Switch):
    """ An overcurrent protective device with a circuit opening fusible part that is heated and severed by the passage of overcurrent through it. A fuse is considered a switching device because it breaks current.
    """

    # Fault interrupting current rating.
    amp_rating = CurrentFlow

class PhaseTapChanger(TapChanger):
    """ A specialization of a voltage tap changer that has detailed modeling for phase shifting capabilities.   A phase shifting tap changer is also in general a voltage magnitude transformer.    The symmetrical and asymmetrical transformer tap changer models are defined here.
    """

    # Similar to TapChanger.nominalVoltage, but this is the nominal voltage in the out of phase winding at the nominal tap step. A typical case may have zero voltage at the nominal step, indicating no phase shift at the nominal voltage.
    nominal_voltage_out_of_phase = Voltage
    # The reactance at the maximum tap step.
    x_step_max = Reactance
    # The type of phase shifter construction.
    phase_tap_changer_type = PhaseTapChangerKind
    # The reactance at the minimum tap step.
    x_step_min = Reactance
    # The phase angle between the in-phase winding and the out-of -phase winding used for creating phase shift.   It is only possible to have a symmemtrical transformer if this angle is 90 degrees.
    winding_connection_angle = AngleDegrees
    # The voltage step increment on the out of phase winding.    This voltage step on the out of phase winding of the phase shifter.  Similar to TapChanger.voltageStepIncrement, but it is applied only to the out of phase winding.
    voltage_step_increment_out_of_phase = Voltage
    # Phase shift per step position. A positive value indicates a positive phase shift from the winding where the tap is located to the other winding (for a two-winding transformer). The actual phase shift increment might be more accureatly computed from the symmetrical or asymmetrical models or a tap step table lookup if those are available.
    step_phase_shift_increment = AngleDegrees
#    transformer_winding = db.ReferenceProperty()

class Breaker(ProtectedSwitch):
    """ A mechanical switching device capable of making, carrying, and breaking currents under normal circuit conditions and also making, carrying for a specified time, and breaking currents under specified abnormal circuit conditions e.g.  those of short circuit.
    """

    # The transition time from open to close.
    in_transit_time = Seconds
    # Fault interrupting current rating.
    rated_current = CurrentFlow

class Junction(Connector):
    """ A point where one or more conducting equipments are connected with zero resistance.
    """

    pass

class LoadBreakSwitch(ProtectedSwitch):
    """ A mechanical switching device capable of making, carrying, and breaking currents under normal operating conditions.
    """

    # Current carrying capacity of a wire or cable under stated thermal conditions.
    rated_current = CurrentFlow


