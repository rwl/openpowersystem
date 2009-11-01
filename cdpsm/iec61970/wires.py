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

from cdpsm.iec61970.core import ConductingEquipment
from cdpsm.iec61970.core import PowerSystemResource
from cdpsm.iec61970.core import EquipmentContainer

from cdpsm.iec61970.domain import CurrentFlow
from cdpsm.iec61970.domain import PerCent
from cdpsm.iec61970.domain import Seconds
from cdpsm.iec61970.domain import Voltage
from cdpsm.iec61970.domain import Resistance
from cdpsm.iec61970.domain import Reactance
from cdpsm.iec61970.domain import Susceptance
from cdpsm.iec61970.domain import AngleRadians
from cdpsm.iec61970.domain import ReactivePower
from cdpsm.iec61970.domain import ActivePower
from cdpsm.iec61970.domain import Length

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

#------------------------------------------------------------------------------
#  Properties:
#------------------------------------------------------------------------------

TransformerControlMode = db.StringProperty(choices=("reactive", "volt"))

WindingConnection = db.StringProperty(choices=("i", "z", "yn", "y", "a", "d", "zn"))

SynchronousMachineType = db.StringProperty(choices=("condenser", "generator_or_condenser", "generator"))

SynchronousMachineOperatingMode = db.StringProperty(choices=("condenser", "generator"))

#------------------------------------------------------------------------------
#  Constants:
#------------------------------------------------------------------------------

NS_PREFIX = "cim"
NS_URI = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_Wires"

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
#  "TapChanger" class:
#------------------------------------------------------------------------------

class TapChanger(PowerSystemResource):
    """ Mechanism for changing transformer winding tap positions.Mechanism for changing transformer winding tap positions.
    """

    
    # Tap step increment, in per cent of nominal voltage, per step position.  For a symmetrical PhaseTapChanger, the stepVoltageIncrement is used in the formula for calculation of the phase angle.  For a symmetrical PhaseTapChanger, the voltage magnitude does not change with tap step.Tap step increment, in per cent of nominal voltage, per step position.  For a symmetrical PhaseTapChanger, the stepVoltageIncrement is used in the formula for calculation of the phase angle.  For a symmetrical PhaseTapChanger, the voltage magnitude does not change with tap step.
    step_voltage_increment = PerCent

    # For an LTC, the delay for subsequent tap changer operation (second and later step changes)For an LTC, the delay for subsequent tap changer operation (second and later step changes)
    subsequent_delay = Seconds

    # The neutral tap step position for this winding.The neutral tap step position for this winding.
    neutral_step = db.IntegerProperty()

    # The tap step position used in 'normal' network operation for this winding. For a 'Fixed' tap changer indicates the current physical tap setting.The tap step position used in 'normal' network operation for this winding. For a 'Fixed' tap changer indicates the current physical tap setting.
    normal_step = db.IntegerProperty()

    # Specifies whether or not a TapChanger has load tap changing capabilities.Specifies whether or not a TapChanger has load tap changing capabilities.
    ltc_flag = db.BooleanProperty()

    # Voltage at which the winding operates at the neutral tap setting.Voltage at which the winding operates at the neutral tap setting.
    neutral_u = Voltage

    # Lowest possible tap step position, retard from neutralLowest possible tap step position, retard from neutral
    low_step = db.IntegerProperty()

    # For an LTC, the delay for initial tap changer operation (first step change)For an LTC, the delay for initial tap changer operation (first step change)
    initial_delay = Seconds

    # Specifies the default regulation status of the TapChanger.  True is regulating.  False is not regulating.Specifies the default regulation status of the TapChanger.  True is regulating.  False is not regulating.
    regulation_status = db.BooleanProperty()

    # Highest possible tap step position, advance from neutralHighest possible tap step position, advance from neutral
    high_step = db.IntegerProperty()

    # The tap step state associated with the tap changer.The tap step state associated with the tap changer.
    sv_tap_step = db.ReferenceProperty()

    # <<< tap_changer
    # @generated
    # >>> tap_changer


#------------------------------------------------------------------------------
#  "Junction" class:
#------------------------------------------------------------------------------

class Junction(ConductingEquipment):
    """ A point where one or more conducting equipments are connected with zero resistance.A point where one or more conducting equipments are connected with zero resistance.
    """

    pass
    # <<< junction
    # @generated
    # >>> junction


#------------------------------------------------------------------------------
#  "EnergySource" class:
#------------------------------------------------------------------------------

class EnergySource(ConductingEquipment):
    """ A generic equivalent for an energy supplier on a transmission or distribution voltage level.A generic equivalent for an energy supplier on a transmission or distribution voltage level.
    """

    
    # Positive sequence Thevenin reactance.Positive sequence Thevenin reactance.
    x = Reactance

    # Phase-to-phase open circuit voltage magnitude.Phase-to-phase open circuit voltage magnitude.
    voltage_magnitude = Voltage

    # Phase angle of a-phase open circuit.Phase angle of a-phase open circuit.
    voltage_angle = AngleRadians

    # Phase-to-phase nominal voltage.Phase-to-phase nominal voltage.
    nominal_voltage = Voltage

    # <<< energy_source
    # @generated
    # >>> energy_source


#------------------------------------------------------------------------------
#  "SynchronousMachine" class:
#------------------------------------------------------------------------------

class SynchronousMachine(ConductingEquipment):
    """ An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.
    """

    
    # Default base reactive power value. This value represents the initial reactive power that can be used by any application function.Default base reactive power value. This value represents the initial reactive power that can be used by any application function.
    base_q = ReactivePower

    # Current mode of operation.Current mode of operation.
    operating_mode = SynchronousMachineOperatingMode

    # Modes that this synchronous machine can operate in.Modes that this synchronous machine can operate in.
    type = SynchronousMachineType

    # Maximum reactive power limit. This is the maximum (nameplate) limit for the unit.Maximum reactive power limit. This is the maximum (nameplate) limit for the unit.
    max_q = ReactivePower

    # Minimum reactive power limit for the unit.Minimum reactive power limit for the unit.
    min_q = ReactivePower

    # A synchronous machine may operate as a generator and as such becomes a member of a generating unitA synchronous machine may operate as a generator and as such becomes a member of a generating unit
    generating_unit = db.ReferenceProperty(collection_name="synchronous_machines")

    # <<< synchronous_machine
    # @generated
    # >>> synchronous_machine


#------------------------------------------------------------------------------
#  "EnergyConsumer" class:
#------------------------------------------------------------------------------

class EnergyConsumer(ConductingEquipment):
    """ Generic user of energy - a  point of consumption on the power system modelGeneric user of energy - a  point of consumption on the power system model
    """

    
    # Active power of the load that is a fixed quantity.Active power of the load that is a fixed quantity.
    pfixed = ActivePower

    # Fixed active power as per cent of load group fixed active powerFixed active power as per cent of load group fixed active power
    pfixed_pct = PerCent

    # Fixed reactive power as per cent of load group fixed reactive power.Fixed reactive power as per cent of load group fixed reactive power.
    qfixed_pct = PerCent

    # Reactive power of the load that is a fixed quantity.Reactive power of the load that is a fixed quantity.
    qfixed = ReactivePower

    # Number of individual customers represented by this DemandNumber of individual customers represented by this Demand
    customer_count = db.IntegerProperty()

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

    
    # The attribute is used in cases when no Measurement for the status value is present. If the Switch has a status measurment the Discrete.normalValue is expected to match with the Switch.normalOpen.The attribute is used in cases when no Measurement for the status value is present. If the Switch has a status measurment the Discrete.normalValue is expected to match with the Switch.normalOpen.
    normal_open = db.BooleanProperty()

    # <<< switch
    # @generated
    # >>> switch


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
#  "ShuntCompensator" class:
#------------------------------------------------------------------------------

class ShuntCompensator(ConductingEquipment):
    """ A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  A negative value for reactivePerSection indicates that the compensator is a reactor. ShuntCompensator is a single terminal device.  Ground is implied.A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  A negative value for reactivePerSection indicates that the compensator is a reactor. ShuntCompensator is a single terminal device.  Ground is implied.
    """

    
    # Nominal reactive power output of the capacitor bank at the nominal voltage. This number should be positive.Nominal reactive power output of the capacitor bank at the nominal voltage. This number should be positive.
    nom_q = ReactivePower

    # The nominal voltage at which the nominal reactive power was measured. This should normally be within 10% of the voltage at which the capacitor is connected to the network.The nominal voltage at which the nominal reactive power was measured. This should normally be within 10% of the voltage at which the capacitor is connected to the network.
    nom_u = Voltage

    # For a capacitor bank, the normal number of sections switched in. This number should correspond to the nominal reactive power (nomQ).For a capacitor bank, the normal number of sections switched in. This number should correspond to the nominal reactive power (nomQ).
    normal_sections = db.IntegerProperty()

    # For a capacitor bank, the maximum number of sections that may be switched in.For a capacitor bank, the maximum number of sections that may be switched in.
    maximum_sections = db.IntegerProperty()

    # For a capacitor bank, the size in reactive power of each switchable section at the nominal voltage.For a capacitor bank, the size in reactive power of each switchable section at the nominal voltage.
    reactive_per_section = ReactivePower

    # <<< shunt_compensator
    # @generated
    # >>> shunt_compensator


#------------------------------------------------------------------------------
#  "Conductor" class:
#------------------------------------------------------------------------------

class Conductor(ConductingEquipment):
    """ Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system.Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system.
    """

    
    # Segment length for calculating line section capabilitiesSegment length for calculating line section capabilities
    length = Length

    # <<< conductor
    # @generated
    # >>> conductor


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
#  "Fuse" class:
#------------------------------------------------------------------------------

class Fuse(Switch):
    """ An overcurrent protective device with a circuit opening fusible part that is heated and severed by the passage of overcurrent through it. A fuse is considered a switching device because it breaks current.An overcurrent protective device with a circuit opening fusible part that is heated and severed by the passage of overcurrent through it. A fuse is considered a switching device because it breaks current.
    """

    
    # Fault interrupting current rating.Fault interrupting current rating.
    rating_current = CurrentFlow

    # <<< fuse
    # @generated
    # >>> fuse


#------------------------------------------------------------------------------
#  "ACLineSegment" class:
#------------------------------------------------------------------------------

class ACLineSegment(Conductor):
    """ A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system.If the instance is an ACLineSegment, the resistance and reactance is mandatory.  However, if the line segment is for a DistributionLineSegment, these are not mandatory.A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system.If the instance is an ACLineSegment, the resistance and reactance is mandatory.  However, if the line segment is for a DistributionLineSegment, these are not mandatory.
    """

    
    # Positive sequence series resistance of the entire line section.Positive sequence series resistance of the entire line section.
    r = Resistance

    # Zero sequence series reactance of the entire line section.Zero sequence series reactance of the entire line section.
    x0 = Reactance

    # Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.  This value represents the full charging over the full length of the line.Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.  This value represents the full charging over the full length of the line.
    bch = Susceptance

    # Positive sequence series reactance of the entire line section.Positive sequence series reactance of the entire line section.
    x = Reactance

    # Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.
    b0ch = Susceptance

    # Zero sequence series resistance of the entire line section.Zero sequence series resistance of the entire line section.
    r0 = Resistance

    # <<< acline_segment
    # @generated
    # >>> acline_segment


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
#  "RatioTapChanger" class:
#------------------------------------------------------------------------------

class RatioTapChanger(TapChanger):
    """ A tap changer that changes the voltage ratio impacting the voltage magnitude but not direclty the phase angle across the transformer..A tap changer that changes the voltage ratio impacting the voltage magnitude but not direclty the phase angle across the transformer..
    """

    
    # Specifies the regulation control mode (voltage or reactive) of the RatioTapChanger.Specifies the regulation control mode (voltage or reactive) of the RatioTapChanger.
    tcul_control_mode = TransformerControlMode

    # Winding to which this ratio tap changer belongs.Winding to which this ratio tap changer belongs.
    winding = db.ReferenceProperty()

    # <<< ratio_tap_changer
    # @generated
    # >>> ratio_tap_changer


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
