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

""" State variable for power flow. Only Terminal instances of EnergyConsumer and SynchronousMachine will have SvPowerFlow instances assigned.   The number of SvPowerFlow instances in the model should match the number EnergyConsumer plus SynchronousMachine objects in the model regardless of the Terminal.connected values.    Any SvPowerFlow with a Terminal.connected value of false must have zero flow explicitly specified on an SvPowerFlow instance. The other types of terminals are not included in exchanges since their values can be readily computed from local voltages and attributes without a global powerflow solution. 
"""

# <<< imports
# @generated
from ucte.state_variables.state_variable import StateVariable


from ucte.domain import ActivePower
from ucte.domain import ReactivePower

from google.appengine.ext import db
# >>> imports

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
    terminal = db.ReferenceProperty(db.Model,
        collection_name="_sv_power_flow_set") # sv_power_flow

    # >>> sv_power_flow.references

    # <<< sv_power_flow.operations
    # @generated
    # >>> sv_power_flow.operations

# EOF -------------------------------------------------------------------------
