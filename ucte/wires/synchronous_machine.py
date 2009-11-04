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

""" An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump. In this profile: - If a SynchronousMachine is not associated with a ReactiveCapabilityCurve, then the minQ and maxQ attributes will be used.    - If a ReactiveCapabilityCurve is supplied, then the minQ and maxQ attributes are not required.  - For UCTE, there is no synchronous condenser mode; therefore, the SynchronousMachine must be associated with one and only one  GeneratingUnit.  In this case, the type and operatingMode attributes must both be set to ?condenser?.  
"""

# <<< imports
# @generated
from ucte.wires.regulating_cond_eq import RegulatingCondEq

from ucte.wires.reactive_capability_curve import ReactiveCapabilityCurve
from ucte.generation.production.generating_unit import GeneratingUnit

from ucte.domain import Reactance
from ucte.wires import SynchronousMachineOperatingMode
from ucte.domain import Resistance
from ucte.domain import PerCent
from ucte.wires import SynchronousMachineType
from ucte.domain import ReactivePower
from ucte.domain import ApparentPower

from google.appengine.ext import db
# >>> imports

class SynchronousMachine(RegulatingCondEq):
    """ An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump. In this profile: - If a SynchronousMachine is not associated with a ReactiveCapabilityCurve, then the minQ and maxQ attributes will be used.    - If a ReactiveCapabilityCurve is supplied, then the minQ and maxQ attributes are not required.  - For UCTE, there is no synchronous condenser mode; therefore, the SynchronousMachine must be associated with one and only one  GeneratingUnit.  In this case, the type and operatingMode attributes must both be set to ?condenser?.  
    """
    # <<< synchronous_machine.attributes
    # @generated
    # Zero sequence reactance of the synchronous machine. This is for Short Circuit only. 
    x0 = Reactance

    # Current mode of operation. 
    operating_mode = SynchronousMachineOperatingMode

    # Zero sequence resistance of the synchronous machine. This is for Short Circuit only. 
    r0 = Resistance

    # Percent of the coordinated reactive control that comes from this machine. 
    q_percent = PerCent

    # Negative sequence reactance. This is for Short Circuit only. 
    x2 = Reactance

    # Modes that this synchronous machine can operate in. 
    type = SynchronousMachineType

    # Negative sequence resistance. This is for Short Circuit only. 
    r2 = Resistance

    # Positive sequence resistance of the synchronous machine. 
    r = Resistance

    # Maximum reactive power limit. This is the maximum (nameplate) limit for the unit. 
    max_q = ReactivePower

    # Positive sequence reactance of the synchronous machine. 
    x = Reactance

    # Nameplate apparent power rating for the unit 
    rated_s = ApparentPower

    # Minimum reactive power limit for the unit. 
    min_q = ReactivePower

    # >>> synchronous_machine.attributes

    # <<< synchronous_machine.references
    # @generated
    # The default ReactiveCapabilityCurve for use by a SynchronousMachine 
    initial_reactive_capability_curve = db.ReferenceProperty(ReactiveCapabilityCurve,
        collection_name="initially_used_by_synchronous_machine")

    # The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.  
    drives_hydro_pump = db.ReferenceProperty(db.Model,
        collection_name="_synchronous_machine_set") # driven_by_synchronous_machine

    # A synchronous machine may operate as a generator and as such becomes a member of a generating unit Each SynchronousMachine is a member of one and only one GeneratingUnit plus each GeneratingUnit should have one and only one SynchronousMachine.   This is required to properly proportion generation limits specified on GeneratingUnit to the appropriate injection points specified by SynchronousMachine and its Terminal connection. 
    member_of_generating_unit = db.ReferenceProperty(GeneratingUnit,
        collection_name="contains_synchronous_machines")

    # >>> synchronous_machine.references

    # <<< synchronous_machine.operations
    # @generated
    # >>> synchronous_machine.operations

# EOF -------------------------------------------------------------------------
