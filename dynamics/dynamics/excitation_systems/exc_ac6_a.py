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

class ExcAC6A(ExcitationSystem):
    """ IEEE (1992/2005) AC6A Model  The model is used to represent field-controlled alternator-rectifier excitation systems with system-supplied electronic voltage regulators. The maximum output of the regulator, <i>V</i><i><sub>R</sub></i>, is a function of terminal voltage, <i>V</i><i><sub>T</sub></i>. The field current limiter included in the original model AC6A remains in the 2005 update. 
    """
    # <<< exc_ac6_a.attributes
    # @generated
    # Maximum controller element output (&gt; 0.) 
    vamax = db.FloatProperty()

    # Exciter field current limit reference (&gt; 0.) 
    vfelim = db.FloatProperty()

    # Filter time constant 
    tr = Seconds

    # Field voltage value 2.    (&gt; 0.) 
    e2 = db.FloatProperty()

    # Field voltage value 1     (&gt; 0.) 
    e1 = db.FloatProperty()

    # Minimum controller element output (&lt; 0.) 
    vamin = db.FloatProperty()

    # Maximum field current limiter signal (&gt; 0.) 
    vhmax = db.FloatProperty()

    # Maximum exciter control signal (&gt; 0.) 
    vrmax = db.FloatProperty()

    # Saturation factor at e1 (&gt;= 0.) 
    se1 = db.FloatProperty()

    # Saturation factor at e2  (&gt;= 0.) 
    se2 = db.FloatProperty()

    # Minimum exciter control signal (&lt; 0.) 
    vrmin = db.FloatProperty()

    # Exciter time constant (&gt; 0.) 
    te = Seconds

    # Exciter field current limiter gain (&gt;= 0.) 
    kh = db.FloatProperty()

    # Time constant (&gt;= 0.) 
    tb = Seconds

    # Lead time constant 
    tc = Seconds

    # Time constant (&gt;= 0.) 
    ta = Seconds

    # Gain (&gt; 0.) 
    ka = db.FloatProperty()

    # Rectifier regulation factor (&gt;= 0.) 
    kc = db.FloatProperty()

    # Field current limiter time constant (&gt;= 0.) 
    tj = Seconds

    # Lag time constant (&gt;= 0.) 
    tk = Seconds

    # Exciter field resistance constant 
    ke = db.FloatProperty()

    # Field current limiter time constant (&gt; 0.) 
    th = Seconds

    # Exciter internal reactance (&gt;= 0.) 
    kd = db.FloatProperty()

    # >>> exc_ac6_a.attributes

    # <<< exc_ac6_a.references
    # @generated
    # >>> exc_ac6_a.references

    # <<< exc_ac6_a.operations
    # @generated
    # >>> exc_ac6_a.operations

# EOF -------------------------------------------------------------------------
