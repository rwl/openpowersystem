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
from dynamics.dynamics.excitation_systems.excitation_system import ExcitationSystem


from dynamics.domain import Seconds

from google.appengine.ext import db
# >>> imports

class ExcST6B(ExcitationSystem):
    """ IEEE (2005) ST6B Model  The AVR consists of a PI voltage regulator with an inner loop field voltage regulator and pre-control. The field voltage regulator implements a proportional control. The pre-control and the delay in the feedback circuit increase the dynamic response. 
    """
    # <<< exc_st6_b.attributes
    # @generated
    # PI minimum output (&lt; 0.) 
    vamin = db.FloatProperty()

    # Minimum regulator output (&lt; 0.) 
    vrmin = db.FloatProperty()

    # Main gain 
    km = db.FloatProperty()

    # Rectifier firing time constant (not in IEEE model) (&gt;= 0.) 
    ts = Seconds

    # Feedback gain (&gt;= 0.) 
    kg = db.FloatProperty()

    # Filter time constant (&gt;= 0.) 
    tr = Seconds

    # Field current limiter conversion factor (&gt; 0.) 
    kcl = db.FloatProperty()

    # Field current limiter gain (&gt; 0.) 
    klr = db.FloatProperty()

    # Maximum regulator output (&gt; 0.) 
    vrmax = db.FloatProperty()

    # Field current limiter setpoint (&gt; 0.) 
    ilr = db.FloatProperty()

    # Regulator proportional gain (&gt; 0.) 
    kpa = db.FloatProperty()

    # Feedback time constant (&gt;= 0.) 
    tg = Seconds

    # PI maximum output. (&gt; 0.) 
    vamax = db.FloatProperty()

    # OEL input selector: 1 ? before UEL, 2 ? after UEL, 0 ? no OEL input 
    oelin = db.FloatProperty()

    # Feedforward gain 
    kff = db.FloatProperty()

    # If non-zero, multiply regulator output by terminal voltage 
    vmult = db.FloatProperty()

    # Regulator integral gain (&gt; 0.) 
    kia = db.FloatProperty()

    # >>> exc_st6_b.attributes

    # <<< exc_st6_b.references
    # @generated
    # >>> exc_st6_b.references

    # <<< exc_st6_b.operations
    # @generated
    # >>> exc_st6_b.operations

# EOF -------------------------------------------------------------------------
