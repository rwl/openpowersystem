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

""" An extension to the Core and Topology package that models information on the electrical characteristics of Transmission and Distribution networks. This package is used by network applications such as State Estimation, Load Flow and Optimal Power Flow.An extension to the Core and Topology package that models information on the electrical characteristics of Transmission and Distribution networks. This package is used by network applications such as State Estimation, Load Flow and Optimal Power Flow.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from cpsm.core import Equipment
from cpsm.core import ConductingEquipment
from cpsm.core import PowerSystemResource
from cpsm.core import RegularIntervalSchedule
from cpsm.core import Curve
from cpsm.core import EquipmentContainer

from cpsm.domain import ReactivePower
from cpsm.domain import Voltage
from cpsm.domain import CurrentFlow
from cpsm.domain import PerCent
from cpsm.domain import ActivePower
from cpsm.domain import ApparentPower
from cpsm.domain import Reactance
from cpsm.domain import Resistance
from cpsm.domain import Susceptance
from cpsm.domain import AngleDegrees
from cpsm.domain import VoltagePerReactivePower

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

#------------------------------------------------------------------------------
#  Properties:
#------------------------------------------------------------------------------

SynchronousMachineOperatingMode = db.StringProperty(choices=("generator", "condenser"))

TapChangerKind = db.StringProperty(choices=("voltage_and_phase_control", "phase_control", "fixed", "voltage_control"))

SVCControlMode = db.StringProperty(choices=("voltage", "off", "reactive_power"))

WindingType = db.StringProperty(choices=("primary", "tertiary", "secondary", "quaternary"))

SynchronousMachineType = db.StringProperty(choices=("generator", "generator_or_condenser", "condenser"))

TransformerControlMode = db.StringProperty(choices=("local", "active", "volt", "off", "reactive"))

#------------------------------------------------------------------------------
#  Constants:
#------------------------------------------------------------------------------

NS_PREFIX = "cim"
NS_URI = "http://iec.ch/TC57/2008/CIM-schema-cim13#Package_Wires"

#------------------------------------------------------------------------------
#  "PowerTransformer" class:
#------------------------------------------------------------------------------

class PowerTransformer(Equipment):
    """ An electrical device consisting of  two or more coupled windings, with or without a magnetic core, for introducing mutual coupling between electric circuits. Transformers can be used to control voltage and phase shift (active power flow).An electrical device consisting of  two or more coupled windings, with or without a magnetic core, for introducing mutual coupling between electric circuits. Transformers can be used to control voltage and phase shift (active power flow).
    """

    
    # Virtual property. A transformer has windingsA transformer has windings
    pass #contains_transformer_windings

    # <<< power_transformer
    # @generated
    # >>> power_transformer


#------------------------------------------------------------------------------
#  "BusbarSection" class:
#------------------------------------------------------------------------------

class BusbarSection(ConductingEquipment):
    """ A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation.  Voltage measurements are typically obtained from VoltageTransformers that are connected to busbar sections. A bus bar section may have many physical terminals but for analysis is modelled with exactly one logical terminal.A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation.  Voltage measurements are typically obtained from VoltageTransformers that are connected to busbar sections. A bus bar section may have many physical terminals but for analysis is modelled with exactly one logical terminal.
    """

    pass
    # <<< busbar_section
    # @generated
    # >>> busbar_section


#------------------------------------------------------------------------------
#  "RegulatingCondEq" class:
#------------------------------------------------------------------------------

class RegulatingCondEq(ConductingEquipment):
    """ RegulatingCondEq is a type of ConductingEquipment that can regulate Measurements and have a RegulationSchedule.RegulatingCondEq is a type of ConductingEquipment that can regulate Measurements and have a RegulationSchedule.
    """

    
    # copy from ...copy from ...
    regulating_control = db.ReferenceProperty(collection_name="regulating_cond_eq")

    # <<< regulating_cond_eq
    # @generated
    # >>> regulating_cond_eq


#------------------------------------------------------------------------------
#  "EnergyConsumer" class:
#------------------------------------------------------------------------------

class EnergyConsumer(ConductingEquipment):
    """ Generic user of energy - a  point of consumption on the power system modelGeneric user of energy - a  point of consumption on the power system model
    """

    
    # Fixed reactive power as per cent of load group fixed reactive power.Fixed reactive power as per cent of load group fixed reactive power.
    qfixed_pct = PerCent

    # Active power of the load that is a fixed quantity.Active power of the load that is a fixed quantity.
    pfixed = ActivePower

    # Reactive power of the load that is a fixed quantity.Reactive power of the load that is a fixed quantity.
    qfixed = ReactivePower

    # Fixed active power as per cent of load group fixed active powerFixed active power as per cent of load group fixed active power
    pfixed_pct = PerCent

    # The load response characteristic of this load.The load response characteristic of this load.
    load_response = db.ReferenceProperty(collection_name="energy_consumer")

    # <<< energy_consumer
    # @generated
    # >>> energy_consumer


#------------------------------------------------------------------------------
#  "TransformerWinding" class:
#------------------------------------------------------------------------------

class TransformerWinding(ConductingEquipment):
    """ A winding is associated with each defined terminal of a transformer (or phase shifter).A winding is associated with each defined terminal of a transformer (or phase shifter).
    """

    
    # The type of winding.The type of winding.
    winding_type = WindingType

    # The normal apparent power rating for the windingThe normal apparent power rating for the winding
    rated_s = ApparentPower

    # Positive sequence series reactance of the winding.Positive sequence series reactance of the winding.
    x = Reactance

    # The rated voltage (phase-to-phase) of the winding, usually the same as the neutral voltage.The rated voltage (phase-to-phase) of the winding, usually the same as the neutral voltage.
    rated_u = Voltage

    # Positive sequence series resistance of the winding.Positive sequence series resistance of the winding.
    r = Resistance

    # Magnetizing branch susceptance (B mag).Magnetizing branch susceptance (B mag).
    b = Susceptance

    # Virtual property. A transformer winding may have tap changers, separately for voltage and phase angle.  If a TransformerWinding does not have an associated TapChanger, the winding is assumed to be fixed tap.A transformer winding may have tap changers, separately for voltage and phase angle.  If a TransformerWinding does not have an associated TapChanger, the winding is assumed to be fixed tap.
    pass #tap_changers

    # A transformer has windingsA transformer has windings
    member_of_power_transformer = db.ReferenceProperty(collection_name="contains_transformer_windings")

    # <<< transformer_winding
    # @generated
    # >>> transformer_winding


#------------------------------------------------------------------------------
#  "RegulatingControl" class:
#------------------------------------------------------------------------------

class RegulatingControl(PowerSystemResource):
    """ Specifies a set of equipment that works together to control a power system quantity such as voltage or flow.Specifies a set of equipment that works together to control a power system quantity such as voltage or flow.
    """

    
    # The terminal associated with this regulating control.The terminal associated with this regulating control.
    terminal = db.ReferenceProperty(collection_name="regulating_control")

    # Schedule for this Regulating regulating control.Schedule for this Regulating regulating control.
    regulation_schedule = db.ReferenceProperty(collection_name="regulating_control")

    # Virtual property. copy from reg conduting eqcopy from reg conduting eq
    pass #tap_changer

    # Virtual property. copy from reg cond eqcopy from reg cond eq
    pass #regulating_cond_eq

    # <<< regulating_control
    # @generated
    # >>> regulating_control


#------------------------------------------------------------------------------
#  "RegulationSchedule" class:
#------------------------------------------------------------------------------

class RegulationSchedule(RegularIntervalSchedule):
    """ A pre-established pattern over time for a controlled variable, e.g., busbar voltage.A pre-established pattern over time for a controlled variable, e.g., busbar voltage.
    """

    
    # Virtual property. Regulating controls that have this Schedule.Regulating controls that have this Schedule.
    pass #regulating_control

    # <<< regulation_schedule
    # @generated
    # >>> regulation_schedule


#------------------------------------------------------------------------------
#  "Switch" class:
#------------------------------------------------------------------------------

class Switch(ConductingEquipment):
    """ A generic device designed to close, or open, or both, one or more electric circuits.A generic device designed to close, or open, or both, one or more electric circuits.
    """

    
    # The attribute is used in cases when no Measurement for the status value is present. If the Switch has a status measurment the Discrete.normalValue is expected to match with the Switch.normalOpen.The attribute is used in cases when no Measurement for the status value is present. If the Switch has a status measurment the Discrete.normalValue is expected to match with the Switch.normalOpen.
    normal_open = db.BooleanProperty()

    # <<< switch
    # @generated
    # >>> switch


#------------------------------------------------------------------------------
#  "Conductor" class:
#------------------------------------------------------------------------------

class Conductor(ConductingEquipment):
    """ Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system.Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system.
    """

    
    # Positive sequence series resistance of the entire line section.Positive sequence series resistance of the entire line section.
    r = Resistance

    # Positive sequence series reactance of the entire line section.Positive sequence series reactance of the entire line section.
    x = Reactance

    # Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.
    bch = Susceptance

    # <<< conductor
    # @generated
    # >>> conductor


#------------------------------------------------------------------------------
#  "ReactiveCapabilityCurve" class:
#------------------------------------------------------------------------------

class ReactiveCapabilityCurve(Curve):
    """ Reactive power rating envelope versus the synchronous machine's active power, in both the generating and motoring modes. For each active power value there is a corresponding high and low reactive power limit  value. Typically there will be a separate curve for each coolant condition, such as hydrogen pressure.  The Y1 axis values represent reactive minimum and the Y2 axis values represent reactive maximum.Reactive power rating envelope versus the synchronous machine's active power, in both the generating and motoring modes. For each active power value there is a corresponding high and low reactive power limit  value. Typically there will be a separate curve for each coolant condition, such as hydrogen pressure.  The Y1 axis values represent reactive minimum and the Y2 axis values represent reactive maximum.
    """

    
    # Virtual property. Synchronous machines using this curve as default.Synchronous machines using this curve as default.
    pass #initially_used_by_synchronous_machine

    # <<< reactive_capability_curve
    # @generated
    # >>> reactive_capability_curve


#------------------------------------------------------------------------------
#  "TapChanger" class:
#------------------------------------------------------------------------------

class TapChanger(PowerSystemResource):
    """ Mechanism for changing transformer winding tap positions.Mechanism for changing transformer winding tap positions.
    """

    
    # The tap step position used in 'normal' network operation for this winding. For a 'Fixed' tap changer indicates the current physical tap setting.The tap step position used in 'normal' network operation for this winding. For a 'Fixed' tap changer indicates the current physical tap setting.
    normal_step = db.IntegerProperty()

    # Highest possible tap step position, advance from neutralHighest possible tap step position, advance from neutral
    high_step = db.IntegerProperty()

    # Phase shift per step position. A positive value indicates a positive phase shift from the winding where the tap is located to the other winding (for a two-winding transformer).Phase shift per step position. A positive value indicates a positive phase shift from the winding where the tap is located to the other winding (for a two-winding transformer).
    step_phase_shift_increment = AngleDegrees

    # The neutral tap step position for this winding.The neutral tap step position for this winding.
    neutral_step = db.IntegerProperty()

    # Lowest possible tap step position, retard from neutralLowest possible tap step position, retard from neutral
    low_step = db.IntegerProperty()

    # For an LTC, the tap changer control mode.For an LTC, the tap changer control mode.
    tcul_control_mode = TransformerControlMode

    # Tap step increment, in per cent of nominal voltage, per step position.Tap step increment, in per cent of nominal voltage, per step position.
    step_voltage_increment = PerCent

    # The type of tap changer. Indicates the ability of the transformer to perform various regulation tasks. The tap changer must be also be associated wtih a RegulationControl object before any regulation is possible.The type of tap changer. Indicates the ability of the transformer to perform various regulation tasks. The tap changer must be also be associated wtih a RegulationControl object before any regulation is possible.
    type = TapChangerKind

    # Voltage at which the winding operates at the neutral tap setting.Voltage at which the winding operates at the neutral tap setting.
    neutral_u = Voltage

    # 
    regulating_control = db.ReferenceProperty(collection_name="tap_changer")

    # A transformer winding may have tap changers, separately for voltage and phase angleA transformer winding may have tap changers, separately for voltage and phase angle
    transformer_winding = db.ReferenceProperty(collection_name="tap_changers")

    # <<< tap_changer
    # @generated
    # >>> tap_changer


#------------------------------------------------------------------------------
#  "Line" class:
#------------------------------------------------------------------------------

class Line(EquipmentContainer):
    """ A component part of a system extending between adjacent substations or from a substation to an adjacent interconnection point.A component part of a system extending between adjacent substations or from a substation to an adjacent interconnection point.
    """

    
    # A Line can be contained by a SubGeographical Region.A Line can be contained by a SubGeographical Region.
    region = db.ReferenceProperty(collection_name="lines")

    # <<< line
    # @generated
    # >>> line


#------------------------------------------------------------------------------
#  "SeriesCompensator" class:
#------------------------------------------------------------------------------

class SeriesCompensator(ConductingEquipment):
    """ A Series Compensator is a series capacitor or reactor or an AC transmission line without charging susceptance.A Series Compensator is a series capacitor or reactor or an AC transmission line without charging susceptance.
    """

    
    # Positive sequence resistance.Positive sequence resistance.
    r = Resistance

    # Positive sequence reactance.Positive sequence reactance.
    x = Reactance

    # <<< series_compensator
    # @generated
    # >>> series_compensator


#------------------------------------------------------------------------------
#  "Disconnector" class:
#------------------------------------------------------------------------------

class Disconnector(Switch):
    """ A manually operated or motor operated mechanical switching device used for changing the connections in a circuit, or for isolating a circuit or equipment from a source of power. It is required to open or close circuits when negligible current is broken or made.A manually operated or motor operated mechanical switching device used for changing the connections in a circuit, or for isolating a circuit or equipment from a source of power. It is required to open or close circuits when negligible current is broken or made.
    """

    pass
    # <<< disconnector
    # @generated
    # >>> disconnector


#------------------------------------------------------------------------------
#  "SynchronousMachine" class:
#------------------------------------------------------------------------------

class SynchronousMachine(RegulatingCondEq):
    """ An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.
    """

    
    # Current mode of operation.Current mode of operation.
    operating_mode = SynchronousMachineOperatingMode

    # Minimum reactive power limit for the unit.Minimum reactive power limit for the unit.
    min_q = ReactivePower

    # Modes that this synchronous machine can operate in.Modes that this synchronous machine can operate in.
    type = SynchronousMachineType

    # Maximum reactive power limit. This is the maximum (nameplate) limit for the unit.Maximum reactive power limit. This is the maximum (nameplate) limit for the unit.
    max_q = ReactivePower

    # The default ReactiveCapabilityCurve for use by a SynchronousMachineThe default ReactiveCapabilityCurve for use by a SynchronousMachine
    initial_reactive_capability_curve = db.ReferenceProperty(collection_name="initially_used_by_synchronous_machine")

    # A synchronous machine may operate as a generator and as such becomes a member of a generating unitA synchronous machine may operate as a generator and as such becomes a member of a generating unit
    member_of_generating_unit = db.ReferenceProperty(collection_name="contains_synchronous_machines")

    # <<< synchronous_machine
    # @generated
    # >>> synchronous_machine


#------------------------------------------------------------------------------
#  "ShuntCompensator" class:
#------------------------------------------------------------------------------

class ShuntCompensator(RegulatingCondEq):
    """ A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  Negative values for mVArPerSection and nominalMVAr indicate that the compensator is a reactor.A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  Negative values for mVArPerSection and nominalMVAr indicate that the compensator is a reactor.
    """

    
    # For a capacitor bank, the maximum number of sections that may be switched in.For a capacitor bank, the maximum number of sections that may be switched in.
    maximum_sections = db.IntegerProperty()

    # For a capacitor bank, the normal number of sections switched in. This number should correspond to the nominal reactive power (nomQ).For a capacitor bank, the normal number of sections switched in. This number should correspond to the nominal reactive power (nomQ).
    normal_sections = db.IntegerProperty()

    # The nominal voltage at which the nominal reactive power was measured. This should normally be within 10% of the voltage at which the capacitor is connected to the network.The nominal voltage at which the nominal reactive power was measured. This should normally be within 10% of the voltage at which the capacitor is connected to the network.
    nom_u = Voltage

    # For a capacitor bank, the size in reactive power of each switchable section at the nominal voltage.For a capacitor bank, the size in reactive power of each switchable section at the nominal voltage.
    reactive_per_section = ReactivePower

    # <<< shunt_compensator
    # @generated
    # >>> shunt_compensator


#------------------------------------------------------------------------------
#  "LoadBreakSwitch" class:
#------------------------------------------------------------------------------

class LoadBreakSwitch(Switch):
    """ A mechanical switching device capable of making, carrying, and breaking currents under normal operating conditions.A mechanical switching device capable of making, carrying, and breaking currents under normal operating conditions.
    """

    
    # Current carrying capacity of a wire or cable under stated thermal conditions.Current carrying capacity of a wire or cable under stated thermal conditions.
    rated_current = CurrentFlow

    # <<< load_break_switch
    # @generated
    # >>> load_break_switch


#------------------------------------------------------------------------------
#  "ACLineSegment" class:
#------------------------------------------------------------------------------

class ACLineSegment(Conductor):
    """ A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system.A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system.
    """

    pass
    # <<< acline_segment
    # @generated
    # >>> acline_segment


#------------------------------------------------------------------------------
#  "StaticVarCompensator" class:
#------------------------------------------------------------------------------

class StaticVarCompensator(RegulatingCondEq):
    """ A facility for providing variable and controllable shunt reactive power. The SVC typically consists of a stepdown transformer, filter, thyristor-controlled reactor, and thyristor-switched capacitor arms.  The SVC may operate in fixed MVar output mode or in voltage control mode.  When in voltage control mode, the output of the SVC will be proportional to the deviation of voltage at the controlled bus from the voltage setpoint.  The SVC characteristic slope defines the proportion.  If the voltage at the controlled bus is equal to the voltage setpoint, the SVC MVar output is zero.A facility for providing variable and controllable shunt reactive power. The SVC typically consists of a stepdown transformer, filter, thyristor-controlled reactor, and thyristor-switched capacitor arms.  The SVC may operate in fixed MVar output mode or in voltage control mode.  When in voltage control mode, the output of the SVC will be proportional to the deviation of voltage at the controlled bus from the voltage setpoint.  The SVC characteristic slope defines the proportion.  If the voltage at the controlled bus is equal to the voltage setpoint, the SVC MVar output is zero.
    """

    
    # The reactive power output of the SVC is proportional to the difference between the voltage at the regulated bus and the voltage setpoint.  When the regulated bus voltage is equal to the voltage setpoint, the reactive power output is zero.The reactive power output of the SVC is proportional to the difference between the voltage at the regulated bus and the voltage setpoint.  When the regulated bus voltage is equal to the voltage setpoint, the reactive power output is zero.
    voltage_set_point = Voltage

    # SVC control mode.SVC control mode.
    s_vccontrol_mode = SVCControlMode

    # Maximum available capacitive reactive powerMaximum available capacitive reactive power
    capacitive_rating = Reactance

    # The characteristics slope of an SVC defines how the reactive power output changes in proportion to the difference between the regulated bus voltage and the voltage setpoint.The characteristics slope of an SVC defines how the reactive power output changes in proportion to the difference between the regulated bus voltage and the voltage setpoint.
    slope = VoltagePerReactivePower

    # Maximum available inductive reactive powerMaximum available inductive reactive power
    inductive_rating = Reactance

    # <<< static_var_compensator
    # @generated
    # >>> static_var_compensator


#------------------------------------------------------------------------------
#  "Breaker" class:
#------------------------------------------------------------------------------

class Breaker(Switch):
    """ A mechanical switching device capable of making, carrying, and breaking currents under normal circuit conditions and also making, carrying for a specified time, and breaking currents under specified abnormal circuit conditions e.g.  those of short circuit.A mechanical switching device capable of making, carrying, and breaking currents under normal circuit conditions and also making, carrying for a specified time, and breaking currents under specified abnormal circuit conditions e.g.  those of short circuit.
    """

    
    # Fault interrupting current rating.Fault interrupting current rating.
    rated_current = CurrentFlow

    # <<< breaker
    # @generated
    # >>> breaker




# EOF -------------------------------------------------------------------------
