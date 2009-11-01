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

""" State variables for analysis solutions such as powerflow.State variables for analysis solutions such as powerflow.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from ucte import Element

from ucte.domain import AngleRadians
from ucte.domain import Voltage
from ucte.domain import ActivePower
from ucte.domain import ReactivePower

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

#------------------------------------------------------------------------------
#  Properties:
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  Constants:
#------------------------------------------------------------------------------

NS_PREFIX = "cim"
NS_URI = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_StateVariables"

#------------------------------------------------------------------------------
#  "StateVariable" class:
#------------------------------------------------------------------------------

class StateVariable(Element):
    """ An abstract class for state variables.An abstract class for state variables.
    """

    pass
    # <<< state_variable
    # @generated
    # >>> state_variable


#------------------------------------------------------------------------------
#  "SvVoltage" class:
#------------------------------------------------------------------------------

class SvVoltage(StateVariable):
    """ State variable for voltage.State variable for voltage.
    """

    
    # The voltage angle in radians of the topological node.The voltage angle in radians of the topological node.
    angle = AngleRadians

    # The voltage magnitude of the topological node.The voltage magnitude of the topological node.
    v = Voltage

    # The topological node associated with the voltage state.The topological node associated with the voltage state.
    topological_node = db.ReferenceProperty()

    # <<< sv_voltage
    # @generated
    # >>> sv_voltage


#------------------------------------------------------------------------------
#  "SvShuntCompensatorSections" class:
#------------------------------------------------------------------------------

class SvShuntCompensatorSections(StateVariable):
    """ State variable for the number of sections in service for a shunt compensator.A SvShuntCompensator is always associated with any instance of ShuntCompensator.   The sections or continuousSections values are specified depending upon the value of the associated RegulatingControl.discrete attribute.  If no RegulatingControl is associated, then the ShuntCompensator is treated as discrete.    In discrete mode, the 'sections' attribute must be present.   In the not 'discrete' mode (continuous mode) the 'continuousSections' attribute must be present.     In the case the Terminal.connected value is 'false' the specificed number of sections is not meaningful to the powerflow solution and powerflow implementations should interpret this as zero injection.   Note that an SvShuntCompensatorSections should be supplied even for ShuntCompensators whose Terminal.connected status is 'false' to keep total number of ShuntCompensator and SvShuntCompensatorSection objects in the model the same.State variable for the number of sections in service for a shunt compensator.A SvShuntCompensator is always associated with any instance of ShuntCompensator.   The sections or continuousSections values are specified depending upon the value of the associated RegulatingControl.discrete attribute.  If no RegulatingControl is associated, then the ShuntCompensator is treated as discrete.    In discrete mode, the 'sections' attribute must be present.   In the not 'discrete' mode (continuous mode) the 'continuousSections' attribute must be present.     In the case the Terminal.connected value is 'false' the specificed number of sections is not meaningful to the powerflow solution and powerflow implementations should interpret this as zero injection.   Note that an SvShuntCompensatorSections should be supplied even for ShuntCompensators whose Terminal.connected status is 'false' to keep total number of ShuntCompensator and SvShuntCompensatorSection objects in the model the same.
    """

    
    # The number of sections in service as a continous variable.The number of sections in service as a continous variable.
    continuous_sections = db.FloatProperty()

    # The shunt compensator for which the state applies.The shunt compensator for which the state applies.
    shunt_compensator = db.ReferenceProperty()

    # <<< sv_shunt_compensator_sections
    # @generated
    # >>> sv_shunt_compensator_sections


#------------------------------------------------------------------------------
#  "SvTapStep" class:
#------------------------------------------------------------------------------

class SvTapStep(StateVariable):
    """ State variable for transformer tap step.     Normally a profile specifies only one of the attributes 'position'or 'continuousPosition'.SvTapStep is only meant to be used for taps that change under load.State variable for transformer tap step.     Normally a profile specifies only one of the attributes 'position'or 'continuousPosition'.SvTapStep is only meant to be used for taps that change under load.
    """

    
    # The floating point tap position.The floating point tap position.
    continuous_position = db.FloatProperty()

    # The tap changer associated with the tap step state.The tap changer associated with the tap step state.
    tap_changer = db.ReferenceProperty()

    # <<< sv_tap_step
    # @generated
    # >>> sv_tap_step


#------------------------------------------------------------------------------
#  "SvPowerFlow" class:
#------------------------------------------------------------------------------

class SvPowerFlow(StateVariable):
    """ State variable for power flow.Only Terminal instances of EnergyConsumer and SynchronousMachine will have SvPowerFlow instances assigned.   The number of SvPowerFlow instances in the model should match the number EnergyConsumer plus SynchronousMachine objects in the model regardless of the Terminal.connected values.    Any SvPowerFlow with a Terminal.connected value of false must have zero flow explicitly specified on an SvPowerFlow instance. The other types of terminals are not included in exchanges since their values can be readily computed from local voltages and attributes without a global powerflow solution.State variable for power flow.Only Terminal instances of EnergyConsumer and SynchronousMachine will have SvPowerFlow instances assigned.   The number of SvPowerFlow instances in the model should match the number EnergyConsumer plus SynchronousMachine objects in the model regardless of the Terminal.connected values.    Any SvPowerFlow with a Terminal.connected value of false must have zero flow explicitly specified on an SvPowerFlow instance. The other types of terminals are not included in exchanges since their values can be readily computed from local voltages and attributes without a global powerflow solution.
    """

    
    # The active power flow into the terminal.If the associated Terminal.connected status is 'false', the flow specified in the SvPowerFlow.p should be zero.   The power flow is into the Terminal of the ConductingEquipment.The active power flow into the terminal.If the associated Terminal.connected status is 'false', the flow specified in the SvPowerFlow.p should be zero.   The power flow is into the Terminal of the ConductingEquipment.
    p = ActivePower

    # The reactive power flow into the terminal.If the associated Terminal.connected status is 'false', the flow specified in the SvPowerFlow.q should be zero.   The power flow is into the Terminal of the ConductingEquipment.The reactive power flow into the terminal.If the associated Terminal.connected status is 'false', the flow specified in the SvPowerFlow.q should be zero.   The power flow is into the Terminal of the ConductingEquipment.
    q = ReactivePower

    # The terminal associated with the power flow state.The SvPowerFlow is only associated with the Terminal objects of shunt injection classes EnergyConsumer and  SynchronousMachine.  Branch flows are not exchanged since they can be readily computed from the voltages, impedances, and for transformers additionally the tap parameters including the SvTapStep.  Similarly, Switch flows are not included because they can typically be uniquely computed, except in the case of meshed networks of Switch objects.  Terminals of the ShuntCompensator class are not associated because the injection value can be computed from the solved voltage, number of sections, Termianl.connected state, and the impedance per section attributes on the ShuntCompensator. The terminal associated with the power flow state.The SvPowerFlow is only associated with the Terminal objects of shunt injection classes EnergyConsumer and  SynchronousMachine.  Branch flows are not exchanged since they can be readily computed from the voltages, impedances, and for transformers additionally the tap parameters including the SvTapStep.  Similarly, Switch flows are not included because they can typically be uniquely computed, except in the case of meshed networks of Switch objects.  Terminals of the ShuntCompensator class are not associated because the injection value can be computed from the solved voltage, number of sections, Termianl.connected state, and the impedance per section attributes on the ShuntCompensator. 
    terminal = db.ReferenceProperty()

    # <<< sv_power_flow
    # @generated
    # >>> sv_power_flow




# EOF -------------------------------------------------------------------------
