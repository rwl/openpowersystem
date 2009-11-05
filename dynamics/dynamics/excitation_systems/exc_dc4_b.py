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

class ExcDC4B(ExcitationSystem):
    """ IEEE (2005) DC4B Model  These excitation systems utilize a field-controlled dc commutator exciter with a continuously acting voltage regulator having supplies obtained from the generator or auxiliary bus. The replacement of the controls only as an upgrade (retaining the dc commutator exciter) has resulted in a new model. This excitation system typically includes a proportional, integral, and differential (PID) generator voltage regulator (AVR). An alternative rate feedback loop (<i>kf</i>, <i>tf</i>) for stabilization is also shown in the model if the AVR does not include a derivative term. If a PSS control is supplied, the appropriate model is the Type PSS2B model. 
    """
    # <<< exc_dc4_b.attributes
    # @generated
    # Minimum controller output (&lt;= 0.) 
    vrmin = db.FloatProperty()

    # UEL input: if &lt; 2, HV gate; if = 2, add to error signal 
    uelin = db.FloatProperty()

    # Integral gain (&gt;= 0.) 
    ki = db.FloatProperty()

    # Proportional gain (&gt;= 0.) 
    kp = db.FloatProperty()

    # Field voltage value 2.   (&gt; 0.) 
    e2 = db.FloatProperty()

    # OEL input: if &lt; 2, LV gate; if = 2, subtract from error signal 
    oelin = db.FloatProperty()

    # Maximum controller output 
    vrmax = db.FloatProperty()

    # Rate feedback gain (&gt;= 0.) 
    kf = db.FloatProperty()

    # Exciter time constant (&gt; 0.) 
    te = Seconds

    # Exciter field resistance line slope 
    ke = db.FloatProperty()

    # Exciter minimum output  (&lt;= 0.) 
    vemin = db.FloatProperty()

    # Rate feedback time constant (&gt;= 0.) 
    tf = Seconds

    # Derivative gain (&gt;= 0.) 
    kd = db.FloatProperty()

    # Saturation factor at e2 (&gt;= 0.) 
    se2 = db.FloatProperty()

    # Time constant (&gt; 0.) 
    ta = Seconds

    # Filter time constant (&gt;= 0.) 
    tr = Seconds

    # Gain (&gt; 0.) 
    ka = db.FloatProperty()

    # Saturation factor at e1   (&gt;= 0.) 
    se1 = db.FloatProperty()

    # Derivative time constant (&gt; 0. If kd &gt; 0.) 
    td = Seconds

    # Field voltage value 1     (&gt; 0.) 
    e1 = db.FloatProperty()

    # >>> exc_dc4_b.attributes

    # <<< exc_dc4_b.references
    # @generated
    # >>> exc_dc4_b.references

    # <<< exc_dc4_b.operations
    # @generated
    # >>> exc_dc4_b.operations

# EOF -------------------------------------------------------------------------
