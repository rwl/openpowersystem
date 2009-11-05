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

class ExcST2A(ExcitationSystem):
    """ IEEE (1992/2005) ST2A Model  Some static systems utilize both current and voltage sources (generator terminal quantities) to comprise the power source. These compound-source rectifier excitation systems are designated Type ST2A. The regulator controls the exciter output through controlled saturation of the power transformer components. 
    """
    # <<< exc_st2_a.attributes
    # @generated
    # Minimum controller output (&lt; 0.) 
    vrmin = db.FloatProperty()

    # Time constant 
    tc = Seconds

    # Time constant (&gt;=0.) 
    tb = Seconds

    # Time constant (&gt; 0.) 
    ta = Seconds

    # Gain (&gt; 0.) 
    ka = db.FloatProperty()

    # Time constant feedback 
    ke = db.FloatProperty()

    # UEL input: if = 1, HV gate; if = 2, add to error signal 
    uelin = db.FloatProperty()

    # Rectifier loading factor (&gt;= 0.) 
    kc = db.FloatProperty()

    # Transformer saturation control time constant (&gt; 0.) 
    te = Seconds

    # Current source gain (&gt;= 0.) 
    ki = db.FloatProperty()

    # Rate feedback gain (&gt;= 0.) 
    kf = db.FloatProperty()

    # Rate feedback time constant (&gt;= 0.) 
    tf = Seconds

    # Maximum controller output (&gt; 0.) 
    vrmax = db.FloatProperty()

    # Maximum field voltage (&gt;=0.) 
    efdmax = db.FloatProperty()

    # Filter time constant (&gt;= 0.) 
    tr = Seconds

    # Potential source gain (&gt;= 0.) 
    kp = db.FloatProperty()

    # >>> exc_st2_a.attributes

    # <<< exc_st2_a.references
    # @generated
    # >>> exc_st2_a.references

    # <<< exc_st2_a.operations
    # @generated
    # >>> exc_st2_a.operations

# EOF -------------------------------------------------------------------------
