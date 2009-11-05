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

""" An asynchronous (induction) machine with no external connection to the rotor windings, e.g squirel-cage induction machine. 
"""

# <<< imports
# @generated
from dynamics.dynamics.rotating_machine import RotatingMachine


from dynamics.domain import Resistance
from dynamics.domain import Reactance
from dynamics.domain import Seconds

from google.appengine.ext import db
# >>> imports

class AsynchronousMachine(RotatingMachine):
    """ An asynchronous (induction) machine with no external connection to the rotor windings, e.g squirel-cage induction machine. 
    """
    # <<< asynchronous_machine.attributes
    # @generated
    # Damper 1 winding resistance 
    rr1 = Resistance

    # Transient reactance (unsaturated) (&gt; =Xpp) 
    xp = Reactance

    # Transient rotor time constant (&gt; Tppo) 
    tpo = Seconds

    # Magnetizing reactance 
    xm = Reactance

    # Synchronous reactance (&gt;= Xp) 
    xs = Reactance

    # Damper 2 winding resistance 
    rr2 = Resistance

    # Damper 1 winding leakage reactance 
    xlr1 = Reactance

    # Damper 2 winding leakage reactance 
    xlr2 = Reactance

    # Sub-transient rotor time constant (&gt; 0.) 
    tppo = Seconds

    # Sub-transient reactance (unsaturated) (&gt; Xl) 
    xpp = Reactance

    # >>> asynchronous_machine.attributes

    # <<< asynchronous_machine.references
    # @generated
    # >>> asynchronous_machine.references

    # <<< asynchronous_machine.operations
    # @generated
    # >>> asynchronous_machine.operations

# EOF -------------------------------------------------------------------------
