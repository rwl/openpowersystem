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

from ucte.core import ConductingEquipment
from ucte.core import IdentifiedObject
from ucte.core import Curve
from ucte.core import Equipment
from ucte.core import EquipmentContainer

from ucte.domain import PerCent
from ucte.domain import Voltage
from ucte.domain import Reactance
from ucte.domain import Susceptance
from ucte.domain import ApparentPower
from ucte.domain import Resistance
from ucte.domain import Conductance
from ucte.domain import AngleDegrees
from ucte.domain import LongLength
from ucte.domain import ReactivePower

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

#------------------------------------------------------------------------------
#  Properties:
#------------------------------------------------------------------------------

WindingType = db.StringProperty(choices=("tertiary", "primary", "secondary"))

WindingConnection = db.StringProperty(choices=("z", "y", "d"))

RegulatingControlModeKind = db.StringProperty(choices=("reactive_power", "voltage", "active_power", "current_flow", "fixed", "admittance"))

SynchronousMachineType = db.StringProperty(choices=("condenser", "generator_or_condenser", "generator"))

SynchronousMachineOperatingMode = db.StringProperty(choices=("condenser", "generator"))

PhaseTapChangerKind = db.StringProperty(choices=("asymmetrical", "symmetrical"))

#------------------------------------------------------------------------------
#  Constants:
#------------------------------------------------------------------------------

NS_PREFIX = "cim"
NS_URI = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_Wires"

#------------------------------------------------------------------------------
#  "BusbarSection" class:
#------------------------------------------------------------------------------

class BusbarSection(ConductingEquipment):
    """ A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation.  Voltage measurements are typically obtained from VoltageTransformers that are connected to busbar sections. A bus bar section may have many physical terminals but for analysis is modelled with exactly one logical terminal.Terminals of Switches can also be used for regulation.A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation.  Voltage measurements are typically obtained from VoltageTransformers that are connected to busbar sections. A bus bar section may have many physical terminals but for analysis is modelled with exactly one logical terminal.Terminals of Switches can also be used for regulation.
    """

    
    # A VoltageControlZone is controlled by a designated BusbarSection.A VoltageControlZone is controlled by a designated BusbarSection.
    voltage_control_zone = db.ReferenceProperty()

    # <<< busbar_section
    # @generated
    # >>> busbar_section


#------------------------------------------------------------------------------
#  "TapChanger" class:
#------------------------------------------------------------------------------

class TapChanger(IdentifiedObject):
    """ Mechanism for changing transformer winding tap positions.Mechanism for changing transformer winding tap positions.
    """

    
    # Tap step increment, in per cent of nominal voltage, per step position. This could be supplanted by more detailed model information in either the PhaseTapChanger if modeled or in detailed per tap step table information.This is required for RatioTapChanger. It is Optional for most phase shifters since these are not used to regulate voltagesTap step increment, in per cent of nominal voltage, per step position. This could be supplanted by more detailed model information in either the PhaseTapChanger if modeled or in detailed per tap step table information.This is required for RatioTapChanger. It is Optional for most phase shifters since these are not used to regulate voltages
    step_voltage_increment = PerCent

    # Voltage at which the winding operates at the neutral tap setting.Voltage at which the winding operates at the neutral tap setting.
    neutral_u = Voltage

    # Lowest possible tap step position, retard from neutralLowest possible tap step position, retard from neutral
    low_step = db.IntegerProperty()

    # The neutral tap step position for this winding.This attribute is used to define the neutral step for a tap changer or a phase tap changer.  The neutralStep value cannot be higher than the highStep value or lower than the lowStep value. The neutral tap step position for this winding.This attribute is used to define the neutral step for a tap changer or a phase tap changer.  The neutralStep value cannot be higher than the highStep value or lower than the lowStep value. 
    neutral_step = db.IntegerProperty()

    # Highest possible tap step position, advance from neutralHighest possible tap step position, advance from neutral
    high_step = db.IntegerProperty()

    # The tap step state associated with the tap changer.The tap step state associated with the tap changer.
    sv_tap_step = db.ReferenceProperty()

    # 
    regulating_control = db.ReferenceProperty(collection_name="tap_changer")

    # <<< tap_changer
    # @generated
    # >>> tap_changer


#------------------------------------------------------------------------------
#  "TransformerWinding" class:
#------------------------------------------------------------------------------

class TransformerWinding(ConductingEquipment):
    """ A winding is associated with each defined terminal of a transformer (or phase shifter).The association between the TransformerWinding class and MemberOf_EquipmentContainer is not used in this Profile since the association to Power Transformer is already there.  The only time this association should be used is if the association refers to a different substation than what is used in the PowerTransformer association.A winding is associated with each defined terminal of a transformer (or phase shifter).The association between the TransformerWinding class and MemberOf_EquipmentContainer is not used in this Profile since the association to Power Transformer is already there.  The only time this association should be used is if the association refers to a different substation than what is used in the PowerTransformer association.
    """

    
    # Positive sequence series reactance of the winding.Positive sequence series reactance of the winding.
    x = Reactance

    # Magnetizing branch susceptance (B mag).Magnetizing branch susceptance (B mag).
    b = Susceptance

    # The type of connection of the winding.The type of connection of the winding.
    connection_type = WindingConnection

    # The normal apparent power rating for the windingThe normal apparent power rating for the winding
    rated_s = ApparentPower

    # Zero sequence series reactance of the winding.This is for Short Circuit only.Zero sequence series reactance of the winding.This is for Short Circuit only.
    x0 = Reactance

    # Positive sequence series resistance of the winding.Positive sequence series resistance of the winding.
    r = Resistance

    # Zero sequence series resistance of the winding.This is for Short Circuit only.Zero sequence series resistance of the winding.This is for Short Circuit only.
    r0 = Resistance

    # Zero sequence magnetizing branch susceptance.This is for Short Circuit only.Zero sequence magnetizing branch susceptance.This is for Short Circuit only.
    b0 = Susceptance

    # The rated voltage (phase-to-phase) of the winding, usually the same as the neutral voltage.The rated voltage (phase-to-phase) of the winding, usually the same as the neutral voltage.
    rated_u = Voltage

    # Zero sequence magnetizing branch conductance.This is for Short Circuit only.Zero sequence magnetizing branch conductance.This is for Short Circuit only.
    g0 = Conductance

    # Magnetizing branch conductance (G mag).Magnetizing branch conductance (G mag).
    g = Conductance

    # Ground reactance path through connected grounding transformer.This is for Short Circuit only.Ground reactance path through connected grounding transformer.This is for Short Circuit only.
    xground = Reactance

    # The type of winding.The type of winding.
    winding_type = WindingType

    # Ground resistance path through connected grounding transformer.This is for Short Circuit only.Ground resistance path through connected grounding transformer.This is for Short Circuit only.
    rground = Resistance

    # A transformer has windingsA transformer has windings
    member_of_power_transformer = db.ReferenceProperty(collection_name="contains_transformer_windings")

    # The ratio tap changer associated with the transformer winding.The ratio tap changer associated with the transformer winding.
    ratio_tap_changer = db.ReferenceProperty()

    # The phase tap changer associated with the transformer winding.The phase tap changer associated with the transformer winding.
    phase_tap_changer = db.ReferenceProperty()

    # <<< transformer_winding
    # @generated
    # >>> transformer_winding


#------------------------------------------------------------------------------
#  "RegulatingControl" class:
#------------------------------------------------------------------------------

class RegulatingControl(IdentifiedObject):
    """ Specifies a set of equipment that works together to control a power system quantity such as voltage or flow.Regulating control scheme in which this equipment participates.Specifies a set of equipment that works together to control a power system quantity such as voltage or flow.Regulating control scheme in which this equipment participates.
    """

    
    # The regulating control mode presently available.  This specifications allows for determining the kind of regualation without need for obtaining the units from a schedule.The regulating control mode presently available.  This specifications allows for determining the kind of regualation without need for obtaining the units from a schedule.
    mode = RegulatingControlModeKind

    # The regulation is performed in a discrete mode.The regulation is performed in a discrete mode.
    discrete = db.BooleanProperty()

    # The target value specified for case input.   This value can be used for the target value wihout the use of schedules. The value has the units appropriate to the mode attribute.The target value specified for case input.   This value can be used for the target value wihout the use of schedules. The value has the units appropriate to the mode attribute.
    target_value = db.FloatProperty()

    # This is the case input target range.   This performs the same function as the value2 attribute on the regulation schedule in the case that schedules are not used.   The units of those appropriate for the mode.This is the case input target range.   This performs the same function as the value2 attribute on the regulation schedule in the case that schedules are not used.   The units of those appropriate for the mode.
    target_range = db.FloatProperty()

    # The terminal associated with this regulating control.The terminal associated with this regulating control.
    terminal = db.ReferenceProperty(collection_name="regulating_control")

    # Virtual property. copy from reg cond eqcopy from reg cond eq
    pass #regulating_cond_eq

    # Virtual property. copy from reg conduting eqcopy from reg conduting eq
    pass #tap_changer

    # <<< regulating_control
    # @generated
    # >>> regulating_control


#------------------------------------------------------------------------------
#  "ReactiveCapabilityCurve" class:
#------------------------------------------------------------------------------

class ReactiveCapabilityCurve(Curve):
    """ Reactive power rating envelope versus the synchronous machine's active power, in both the generating and motoring modes. For each active power value there is a corresponding high and low reactive power limit  value. Typically there will be a separate curve for each coolant condition, such as hydrogen pressure.  The Y1 axis values represent reactive minimum and the Y2 axis values represent reactive maximum.By convention in this profile, the CurveData points have y1multiplier of M, y2Multiplier of M, y1Units of W and y2Units of W,  xUnits of W and xMultiplier of M.Reactive power rating envelope versus the synchronous machine's active power, in both the generating and motoring modes. For each active power value there is a corresponding high and low reactive power limit  value. Typically there will be a separate curve for each coolant condition, such as hydrogen pressure.  The Y1 axis values represent reactive minimum and the Y2 axis values represent reactive maximum.By convention in this profile, the CurveData points have y1multiplier of M, y2Multiplier of M, y1Units of W and y2Units of W,  xUnits of W and xMultiplier of M.
    """

    
    # Virtual property. Synchronous machines using this curve as default.Synchronous machines using this curve as default.
    pass #initially_used_by_synchronous_machine

    # <<< reactive_capability_curve
    # @generated
    # >>> reactive_capability_curve


#------------------------------------------------------------------------------
#  "MutualCoupling" class:
#------------------------------------------------------------------------------

class MutualCoupling(IdentifiedObject):
    """ This class represents the zero sequence line mutual coupling.This class is Optional and only used for Short Circuit.This class represents the zero sequence line mutual coupling.This class is Optional and only used for Short Circuit.
    """

    
    # Distance from the second line's specified terminal to end of coupled regionMust be greater than the value of distance21 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number.Distance from the second line's specified terminal to end of coupled regionMust be greater than the value of distance21 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number.
    distance22 = LongLength

    # Zero sequence mutual coupling shunt (charging) conductance, uniformly distributed, of the entire line section.Zero sequence mutual coupling shunt (charging) conductance, uniformly distributed, of the entire line section.
    g0ch = Conductance

    # Distance from the second line's specified terminal to start of coupled regionCannot be equal to distance22 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number.Distance from the second line's specified terminal to start of coupled regionCannot be equal to distance22 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number.
    distance21 = LongLength

    # Zero sequence branch-to-branch mutual impedance coupling, resistanceZero sequence branch-to-branch mutual impedance coupling, resistance
    r0 = Resistance

    # Zero sequence mutual coupling shunt (charging) susceptance, uniformly distributed, of the entire line section.Zero sequence mutual coupling shunt (charging) susceptance, uniformly distributed, of the entire line section.
    b0ch = Susceptance

    # Zero sequence branch-to-branch mutual impedance coupling, reactanceZero sequence branch-to-branch mutual impedance coupling, reactance
    x0 = Resistance

    # Distance from the first line's specified terminal to start of coupled regionCannot be equal to distance12 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number.Distance from the first line's specified terminal to start of coupled regionCannot be equal to distance12 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number.
    distance11 = LongLength

    # Distance from the first line's from specified terminal to end of coupled regionMust be greater than the value of distance11 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number.Distance from the first line's from specified terminal to end of coupled regionMust be greater than the value of distance11 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number.
    distance12 = LongLength

    # The starting terminal for the calculation of distances along the first branch of the mutual coupling.  Normally MutualCoupling would only be used for terminals of AC line segments.  The first and second terminals of a mutual coupling should point to different AC line segments.The starting terminal for the calculation of distances along the first branch of the mutual coupling.  Normally MutualCoupling would only be used for terminals of AC line segments.  The first and second terminals of a mutual coupling should point to different AC line segments.
    first_terminal = db.ReferenceProperty(collection_name="has_first_mutual_coupling")

    # The starting terminal for the calculation of distances along the second branch of the mutual coupling.The starting terminal for the calculation of distances along the second branch of the mutual coupling.
    second_terminal = db.ReferenceProperty(collection_name="has_second_mutual_coupling")

    # <<< mutual_coupling
    # @generated
    # >>> mutual_coupling


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
#  "EnergyConsumer" class:
#------------------------------------------------------------------------------

class EnergyConsumer(ConductingEquipment):
    """ Generic user of energy - a  point of consumption on the power system modelGeneric user of energy - a  point of consumption on the power system model
    """

    
    # The load response characteristic of this load.The load response characteristic of this load.
    load_response = db.ReferenceProperty(collection_name="energy_consumer")

    # <<< energy_consumer
    # @generated
    # >>> energy_consumer


#------------------------------------------------------------------------------
#  "Switch" class:
#------------------------------------------------------------------------------

class Switch(ConductingEquipment):
    """ A generic device designed to close, or open, or both, one or more electric circuits.A generic device designed to close, or open, or both, one or more electric circuits.
    """

    pass
    # <<< switch
    # @generated
    # >>> switch


#------------------------------------------------------------------------------
#  "RegulatingCondEq" class:
#------------------------------------------------------------------------------

class RegulatingCondEq(ConductingEquipment):
    """ RegulatingCondEq is a type of ConductingEquipment that can regulate Measurements and have a RegulationSchedule.RegulatingCondEq is a type of ConductingEquipment that can regulate Measurements and have a RegulationSchedule.
    """

    
    # copy from ...Regulating control scheme in which this equipment participates.copy from ...Regulating control scheme in which this equipment participates.
    regulating_control = db.ReferenceProperty(collection_name="regulating_cond_eq")

    # <<< regulating_cond_eq
    # @generated
    # >>> regulating_cond_eq


#------------------------------------------------------------------------------
#  "VoltageControlZone" class:
#------------------------------------------------------------------------------

class VoltageControlZone(IdentifiedObject):
    """ An area of the power system network which is defined for secondary voltage control purposes. A voltage control zone consists of a collection of substations with a designated bus bar section whose voltage will be controlled.An area of the power system network which is defined for secondary voltage control purposes. A voltage control zone consists of a collection of substations with a designated bus bar section whose voltage will be controlled.
    """

    
    # A VoltageControlZone is controlled by a designated BusbarSection.A VoltageControlZone is controlled by a designated BusbarSection.
    busbar_section = db.ReferenceProperty()

    # <<< voltage_control_zone
    # @generated
    # >>> voltage_control_zone


#------------------------------------------------------------------------------
#  "Line" class:
#------------------------------------------------------------------------------

class Line(EquipmentContainer):
    """ A component part of a system extending between adjacent substations or from a substation to an adjacent interconnection point.A component part of a system extending between adjacent substations or from a substation to an adjacent interconnection point.
    """

    pass
    # <<< line
    # @generated
    # >>> line


#------------------------------------------------------------------------------
#  "Conductor" class:
#------------------------------------------------------------------------------

class Conductor(ConductingEquipment):
    """ Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system.Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system.
    """

    
    # Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.This is for Short Circuit only.Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.This is for Short Circuit only.
    b0ch = Susceptance

    # Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.
    bch = Susceptance

    # Zero sequence series resistance of the entire line section.This is for Short Circuit only.Zero sequence series resistance of the entire line section.This is for Short Circuit only.
    r0 = Resistance

    # Zero sequence series reactance of the entire line section.This is for Short Circuit only.Zero sequence series reactance of the entire line section.This is for Short Circuit only.
    x0 = Reactance

    # Positive sequence shunt (charging) conductance, uniformly distributed, of the entire line section.This is for Short Circuit only.Positive sequence shunt (charging) conductance, uniformly distributed, of the entire line section.This is for Short Circuit only.
    gch = Conductance

    # Positive sequence series reactance of the entire line section.Positive sequence series reactance of the entire line section.
    x = Reactance

    # Segment length for calculating line section capabilitiesRequired only for ACLineSegement objects involved in MutualCoupling.Segment length for calculating line section capabilitiesRequired only for ACLineSegement objects involved in MutualCoupling.
    length = LongLength

    # Positive sequence series resistance of the entire line section.Positive sequence series resistance of the entire line section.
    r = Resistance

    # Zero sequence shunt (charging) conductance, uniformly distributed, of the entire line section.This is for Short Circuit only.Zero sequence shunt (charging) conductance, uniformly distributed, of the entire line section.This is for Short Circuit only.
    g0ch = Conductance

    # <<< conductor
    # @generated
    # >>> conductor


#------------------------------------------------------------------------------
#  "ACLineSegment" class:
#------------------------------------------------------------------------------

class ACLineSegment(Conductor):
    """ A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system.Series compensators can be modeled as ACLineSegement.  The attribute Conductor.length is required only when used in conjunction with a Mutual Coupling.A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system.Series compensators can be modeled as ACLineSegement.  The attribute Conductor.length is required only when used in conjunction with a Mutual Coupling.
    """

    pass
    # <<< acline_segment
    # @generated
    # >>> acline_segment


#------------------------------------------------------------------------------
#  "PhaseTapChanger" class:
#------------------------------------------------------------------------------

class PhaseTapChanger(TapChanger):
    """ A specialization of a voltage tap changer that has detailed modeling for phase shifting capabilities.   A phase shifting tap changer is also in general a voltage magnitude transformer.    The symmetrical and asymmetrical transformer tap changer models are defined here.A specialization of a voltage tap changer that has detailed modeling for phase shifting capabilities.   A phase shifting tap changer is also in general a voltage magnitude transformer.    The symmetrical and asymmetrical transformer tap changer models are defined here.
    """

    
    # The reactance at the minimum tap step.The reactance at the minimum tap step.
    x_step_min = Reactance

    # The reactance at the maximum tap step.The reactance at the maximum tap step.
    x_step_max = Reactance

    # Phase shift per step position. A positive value indicates a positive phase shift from the winding where the tap is located to the other winding (for a two-winding transformer). The actual phase shift increment might be more accureatly computed from the symmetrical or asymmetrical models or a tap step table lookup if those are available.Phase shift per step position. A positive value indicates a positive phase shift from the winding where the tap is located to the other winding (for a two-winding transformer). The actual phase shift increment might be more accureatly computed from the symmetrical or asymmetrical models or a tap step table lookup if those are available.
    step_phase_shift_increment = AngleDegrees

    # The phase angle between the in-phase winding and the out-of -phase winding used for creating phase shift.   It is only possible to have a symmemtrical transformer if this angle is 90 degrees.This is required if PST is AsymmetricalThe phase angle between the in-phase winding and the out-of -phase winding used for creating phase shift.   It is only possible to have a symmemtrical transformer if this angle is 90 degrees.This is required if PST is Asymmetrical
    winding_connection_angle = AngleDegrees

    # The type of phase shifter construction.The type of phase shifter construction.
    phase_tap_changer_type = PhaseTapChangerKind

    # The voltage step increment on the out of phase winding.    This voltage step on the out of phase winding of the phase shifter.  Similar to TapChanger.voltageStepIncrement, but it is applied only to the out of phase winding.This is required if PST is Asymmetrical.The voltage step increment on the out of phase winding.    This voltage step on the out of phase winding of the phase shifter.  Similar to TapChanger.voltageStepIncrement, but it is applied only to the out of phase winding.This is required if PST is Asymmetrical.
    voltage_step_increment_out_of_phase = Voltage

    # The transformer winding to which the phase tap changer belongs.The transformer winding to which the phase tap changer belongs.
    transformer_winding = db.ReferenceProperty()

    # <<< phase_tap_changer
    # @generated
    # >>> phase_tap_changer


#------------------------------------------------------------------------------
#  "SynchronousMachine" class:
#------------------------------------------------------------------------------

class SynchronousMachine(RegulatingCondEq):
    """ An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.In this profile: - If a SynchronousMachine is not associated with a ReactiveCapabilityCurve, then the minQ and maxQ attributes will be used.    - If a ReactiveCapabilityCurve is supplied, then the minQ and maxQ attributes are not required.  - For UCTE, there is no synchronous condenser mode; therefore, the SynchronousMachine must be associated with one and only one  GeneratingUnit.  In this case, the type and operatingMode attributes must both be set to ?condenser?. An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.In this profile: - If a SynchronousMachine is not associated with a ReactiveCapabilityCurve, then the minQ and maxQ attributes will be used.    - If a ReactiveCapabilityCurve is supplied, then the minQ and maxQ attributes are not required.  - For UCTE, there is no synchronous condenser mode; therefore, the SynchronousMachine must be associated with one and only one  GeneratingUnit.  In this case, the type and operatingMode attributes must both be set to ?condenser?. 
    """

    
    # Zero sequence reactance of the synchronous machine.This is for Short Circuit only.Zero sequence reactance of the synchronous machine.This is for Short Circuit only.
    x0 = Reactance

    # Current mode of operation.Current mode of operation.
    operating_mode = SynchronousMachineOperatingMode

    # Zero sequence resistance of the synchronous machine.This is for Short Circuit only.Zero sequence resistance of the synchronous machine.This is for Short Circuit only.
    r0 = Resistance

    # Percent of the coordinated reactive control that comes from this machine.Percent of the coordinated reactive control that comes from this machine.
    q_percent = PerCent

    # Negative sequence reactance.This is for Short Circuit only.Negative sequence reactance.This is for Short Circuit only.
    x2 = Reactance

    # Modes that this synchronous machine can operate in.Modes that this synchronous machine can operate in.
    type = SynchronousMachineType

    # Negative sequence resistance.This is for Short Circuit only.Negative sequence resistance.This is for Short Circuit only.
    r2 = Resistance

    # Positive sequence resistance of the synchronous machine.Positive sequence resistance of the synchronous machine.
    r = Resistance

    # Maximum reactive power limit. This is the maximum (nameplate) limit for the unit.Maximum reactive power limit. This is the maximum (nameplate) limit for the unit.
    max_q = ReactivePower

    # Positive sequence reactance of the synchronous machine.Positive sequence reactance of the synchronous machine.
    x = Reactance

    # Nameplate apparent power rating for the unitNameplate apparent power rating for the unit
    rated_s = ApparentPower

    # Minimum reactive power limit for the unit.Minimum reactive power limit for the unit.
    min_q = ReactivePower

    # The default ReactiveCapabilityCurve for use by a SynchronousMachineThe default ReactiveCapabilityCurve for use by a SynchronousMachine
    initial_reactive_capability_curve = db.ReferenceProperty(collection_name="initially_used_by_synchronous_machine")

    # The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.
    drives_hydro_pump = db.ReferenceProperty()

    # A synchronous machine may operate as a generator and as such becomes a member of a generating unitEach SynchronousMachine is a member of one and only one GeneratingUnit plus each GeneratingUnit should have one and only one SynchronousMachine.   This is required to properly proportion generation limits specified on GeneratingUnit to the appropriate injection points specified by SynchronousMachine and its Terminal connection.A synchronous machine may operate as a generator and as such becomes a member of a generating unitEach SynchronousMachine is a member of one and only one GeneratingUnit plus each GeneratingUnit should have one and only one SynchronousMachine.   This is required to properly proportion generation limits specified on GeneratingUnit to the appropriate injection points specified by SynchronousMachine and its Terminal connection.
    member_of_generating_unit = db.ReferenceProperty(collection_name="contains_synchronous_machines")

    # <<< synchronous_machine
    # @generated
    # >>> synchronous_machine


#------------------------------------------------------------------------------
#  "RatioTapChanger" class:
#------------------------------------------------------------------------------

class RatioTapChanger(TapChanger):
    """ A tap changer that changes the voltage ratio impacting the voltage magnitude but not direclty the phase angle across the transformer..A tap changer that changes the voltage ratio impacting the voltage magnitude but not direclty the phase angle across the transformer..
    """

    
    # The transformer winding to which the ratio tap changer belongs.The transformer winding to which the ratio tap changer belongs.
    transformer_winding = db.ReferenceProperty()

    # <<< ratio_tap_changer
    # @generated
    # >>> ratio_tap_changer


#------------------------------------------------------------------------------
#  "ShuntCompensator" class:
#------------------------------------------------------------------------------

class ShuntCompensator(RegulatingCondEq):
    """ A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  Negative values for mVArPerSection and nominalMVAr indicate that the compensator is a reactor.mVArPerSection and nominalMVAr is now bPerSection.A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  Negative values for mVArPerSection and nominalMVAr indicate that the compensator is a reactor.mVArPerSection and nominalMVAr is now bPerSection.
    """

    
    # Zero sequence shunt (charging) susceptance per sectionThis is for Short Circuit only.Zero sequence shunt (charging) susceptance per sectionThis is for Short Circuit only.
    b0_per_section = Susceptance

    # For a capacitor bank, the maximum number of sections that may be switched in.For a capacitor bank, the maximum number of sections that may be switched in.
    maximum_sections = db.IntegerProperty()

    # Zero sequence shunt (charging) conductance per sectionThis is for Short Circuit only.Zero sequence shunt (charging) conductance per sectionThis is for Short Circuit only.
    g0_per_section = Conductance

    # Positive sequence shunt (charging) susceptance per sectionPositive sequence shunt (charging) susceptance per section
    b_per_section = Susceptance

    # Positive sequence shunt (charging) conductance per sectionPositive sequence shunt (charging) conductance per section
    g_per_section = Conductance

    # The state for the number of shunt compensator sections in service.The state for the number of shunt compensator sections in service.
    sv_shunt_compensator_sections = db.ReferenceProperty()

    # <<< shunt_compensator
    # @generated
    # >>> shunt_compensator




# EOF -------------------------------------------------------------------------
