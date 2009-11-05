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


# <<< imports
# @generated
from dynamics.dynamics.loads.aggregate_load import AggregateLoad


from dynamics.domain import Resistance
from dynamics.domain import Reactance
from dynamics.domain import Seconds
from dynamics.domain import Voltage

from google.appengine.ext import db
# >>> imports

class LoadMotor(AggregateLoad):
    """ Aggregate induction motor load. This model  is used to represent a fraction of an ordinary load as 'induction motor load'.  It allows load that is treated as ordinary constant power in power flow analysis to be represented by an induction motor in dynamic simulation.  Either a 'one-cage' or 'two-cage' model of the induction machine can be modeled.  Magnetic saturation is not modeled.  This model is intended for representation of aggregations of many motors dispersed through a load represented at a high voltage bus but where there is no information on the characteristics of individual motors. 
    """
    # <<< load_motor.attributes
    # @generated
    # Loading factor &ndash; ratio of initial P to motor MVA base 
    lfac = db.FloatProperty()

    # Stator resistance 
    ra = Resistance

    # Damping factor 
    d = db.FloatProperty()

    # Synchronous reactance 
    ls = Reactance

    # Sub-transient rotor time constant 
    tppo = Seconds

    # Circuit breaker operating time (default = 999) 
    tbkr = Seconds

    # Sub-transient reactance 
    lpp = Reactance

    # Transient rotor time constant 
    tpo = Seconds

    # Transient reactance 
    lp = Reactance

    # Inertia constant 
    h = Seconds

    # Voltage threshold for tripping (default = 0) 
    vt = Voltage

    # Fraction of constant-power load to be represented                               by this motor model (between 1.0 and 0.0) 
    pfrac = db.FloatProperty()

    # Voltage trip pickup time (default = 999) 
    tv = Seconds

    # >>> load_motor.attributes

    # <<< load_motor.references
    # @generated
    # >>> load_motor.references

    # <<< load_motor.operations
    # @generated
    # >>> load_motor.operations

# EOF -------------------------------------------------------------------------
