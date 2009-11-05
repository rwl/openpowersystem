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

""" A facility for providing variable and controllable shunt reactive power. The SVC typically consists of a stepdown transformer, filter, thyristor-controlled reactor, and thyristor-switched capacitor arms.  The SVC may operate in fixed MVar output mode or in voltage control mode.  When in voltage control mode, the output of the SVC will be proportional to the deviation of voltage at the controlled bus from the voltage setpoint.  The SVC characteristic slope defines the proportion.  If the voltage at the controlled bus is equal to the voltage setpoint, the SVC MVar output is zero. 
"""

# <<< imports
# @generated
from cpsm.wires.regulating_cond_eq import RegulatingCondEq


from cpsm.domain import Voltage
from cpsm.wires import SVCControlMode
from cpsm.domain import Reactance
from cpsm.domain import VoltagePerReactivePower

from google.appengine.ext import db
# >>> imports

class StaticVarCompensator(RegulatingCondEq):
    """ A facility for providing variable and controllable shunt reactive power. The SVC typically consists of a stepdown transformer, filter, thyristor-controlled reactor, and thyristor-switched capacitor arms.  The SVC may operate in fixed MVar output mode or in voltage control mode.  When in voltage control mode, the output of the SVC will be proportional to the deviation of voltage at the controlled bus from the voltage setpoint.  The SVC characteristic slope defines the proportion.  If the voltage at the controlled bus is equal to the voltage setpoint, the SVC MVar output is zero. 
    """
    # <<< static_var_compensator.attributes
    # @generated
    # The reactive power output of the SVC is proportional to the difference between the voltage at the regulated bus and the voltage setpoint.  When the regulated bus voltage is equal to the voltage setpoint, the reactive power output is zero. 
    voltage_set_point = Voltage

    # SVC control mode. 
    s_vccontrol_mode = SVCControlMode

    # Maximum available capacitive reactive power 
    capacitive_rating = Reactance

    # The characteristics slope of an SVC defines how the reactive power output changes in proportion to the difference between the regulated bus voltage and the voltage setpoint. 
    slope = VoltagePerReactivePower

    # Maximum available inductive reactive power 
    inductive_rating = Reactance

    # >>> static_var_compensator.attributes

    # <<< static_var_compensator.references
    # @generated
    # >>> static_var_compensator.references

    # <<< static_var_compensator.operations
    # @generated
    # >>> static_var_compensator.operations

# EOF -------------------------------------------------------------------------
