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

""" State variables for analysis solutions such as powerflow. 
"""

# <<< imports
# @generated
from ucte import Element

from ucte.domain import AngleRadians
from ucte.domain import Voltage
from ucte.domain import ActivePower
from ucte.domain import ReactivePower

from google.appengine.ext import db
# >>> imports

# <<< properties
# @generated
# >>> properties

# <<< constants
# @generated
NS_PREFIX = "cim"
NS_URI = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_StateVariables"
# >>> constants

class StateVariable(Element):
    """ An abstract class for state variables. 
    """
    # <<< state_variable.attributes
    # @generated
    # >>> state_variable.attributes

    # <<< state_variable.references
    # @generated
    # >>> state_variable.references

    # <<< state_variable.operations
    # @generated
    # >>> state_variable.operations

class SvVoltage(StateVariable):
    """ State variable for voltage. 
    """
    # <<< sv_voltage.attributes
    # @generated
    # The voltage angle in radians of the topological node. 
    angle = AngleRadians

    # The voltage magnitude of the topological node. 
    v = Voltage

    # >>> sv_voltage.attributes

    # <<< sv_voltage.references
    # @generated
    # The topological node associated with the voltage state. 
    topological_node = db.ReferenceProperty(collection_name="_sv_voltage_set")

    # >>> sv_voltage.references

    # <<< sv_voltage.operations
    # @generated
    # >>> sv_voltage.operations

class SvShuntCompensatorSections(StateVariable):
    """ State variable for the number of sections in service for a shunt compensator. A SvShuntCompensator is always associated with any instance of ShuntCompensator.   The sections or continuousSections values are specified depending upon the value of the associated RegulatingControl.discrete attribute.  If no RegulatingControl is associated, then the ShuntCompensator is treated as discrete.    In discrete mode, the 'sections' attribute must be present.   In the not 'discrete' mode (continuous mode) the 'continuousSections' attribute must be present.     In the case the Terminal.connected value is 'false' the specificed number of sections is not meaningful to the powerflow solution and powerflow implementations should interpret this as zero injection.   Note that an SvShuntCompensatorSections should be supplied even for ShuntCompensators whose Terminal.connected status is 'false' to keep total number of ShuntCompensator and SvShuntCompensatorSection objects in the model the same. 
    """
    # <<< sv_shunt_compensator_sections.attributes
    # @generated
    # The number of sections in service as a continous variable. 
    continuous_sections = db.FloatProperty()

    # >>> sv_shunt_compensator_sections.attributes

    # <<< sv_shunt_compensator_sections.references
    # @generated
    # The shunt compensator for which the state applies. 
    shunt_compensator = db.ReferenceProperty(collection_name="_sv_shunt_compensator_sections_set")

    # >>> sv_shunt_compensator_sections.references

    # <<< sv_shunt_compensator_sections.operations
    # @generated
    # >>> sv_shunt_compensator_sections.operations

class SvTapStep(StateVariable):
    """ State variable for transformer tap step.     Normally a profile specifies only one of the attributes 'position'or 'continuousPosition'. SvTapStep is only meant to be used for taps that change under load. 
    """
    # <<< sv_tap_step.attributes
    # @generated
    # The floating point tap position. 
    continuous_position = db.FloatProperty()

    # >>> sv_tap_step.attributes

    # <<< sv_tap_step.references
    # @generated
    # The tap changer associated with the tap step state. 
    tap_changer = db.ReferenceProperty(collection_name="_sv_tap_step_set")

    # >>> sv_tap_step.references

    # <<< sv_tap_step.operations
    # @generated
    # >>> sv_tap_step.operations

class SvPowerFlow(StateVariable):
    """ State variable for power flow. Only Terminal instances of EnergyConsumer and SynchronousMachine will have SvPowerFlow instances assigned.   The number of SvPowerFlow instances in the model should match the number EnergyConsumer plus SynchronousMachine objects in the model regardless of the Terminal.connected values.    Any SvPowerFlow with a Terminal.connected value of false must have zero flow explicitly specified on an SvPowerFlow instance. The other types of terminals are not included in exchanges since their values can be readily computed from local voltages and attributes without a global powerflow solution. 
    """
    # <<< sv_power_flow.attributes
    # @generated
    # The active power flow into the terminal. If the associated Terminal.connected status is 'false', the flow specified in the SvPowerFlow.p should be zero.   The power flow is into the Terminal of the ConductingEquipment. 
    p = ActivePower

    # The reactive power flow into the terminal. If the associated Terminal.connected status is 'false', the flow specified in the SvPowerFlow.q should be zero.   The power flow is into the Terminal of the ConductingEquipment. 
    q = ReactivePower

    # >>> sv_power_flow.attributes

    # <<< sv_power_flow.references
    # @generated
    # The terminal associated with the power flow state. The SvPowerFlow is only associated with the Terminal objects of shunt injection classes EnergyConsumer and  SynchronousMachine.  Branch flows are not exchanged since they can be readily computed from the voltages, impedances, and for transformers additionally the tap parameters including the SvTapStep.  Similarly, Switch flows are not included because they can typically be uniquely computed, except in the case of meshed networks of Switch objects.  Terminals of the ShuntCompensator class are not associated because the injection value can be computed from the solved voltage, number of sections, Termianl.connected state, and the impedance per section attributes on the ShuntCompensator.  
    terminal = db.ReferenceProperty(collection_name="_sv_power_flow_set")

    # >>> sv_power_flow.references

    # <<< sv_power_flow.operations
    # @generated
    # >>> sv_power_flow.operations



# EOF -------------------------------------------------------------------------
