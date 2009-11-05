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

class ExcAC7B(ExcitationSystem):
    """ IEEE (2005) AC7B Model  These excitation systems consist of an ac alternator with either stationary or rotating rectifiers to produce the dc field requirements. Upgrades to earlier ac excitation systems, which replace only the controls but retain the ac alternator and diode rectifier bridge, have resulted in this new model. Some of the features of this excitation system include a high bandwidth inner loop regulating generator field voltage or exciter current (<i>KF</i>2, <i>KF</i>1), a fast exciter current limit, <i>VFEMAX</i>, to protect the field of the ac alternator, and the PID generator voltage regulator (AVR). An alternative rate feedback loop (<i>KF</i>, <i>TF</i>) is provided for stabilization if the AVR does not include a derivative term. If a PSS control is supplied, the Type PSS2B or PSS3B models are appropriate. 
    """
    # <<< exc_ac7_b.attributes
    # @generated
    # Exciter internal reactance (&gt;= 0.) 
    kd = db.FloatProperty()

    # Rectifier regulation factor (&gt;= 0.) 
    kc = db.FloatProperty()

    # Minimum regulator output (&lt; 0.) 
    vrmin = db.FloatProperty()

    # Regulator derivative gain (&gt;= 0.) 
    kdr = db.FloatProperty()

    # Maximum regulator output (&gt; 0.) 
    vrmax = db.FloatProperty()

    # Regulator proportional gain (&gt; 0. if kir = 0.) 
    kpr = db.FloatProperty()

    # Minimum exciter ouput voltage (&lt;= 0.) 
    vemin = db.FloatProperty()

    # Exciter field voltage lower limit parameter 
    kl = db.FloatProperty()

    # Field voltage feedback gain (&gt;= 0.) 
    kf1 = db.FloatProperty()

    # Amplifier integral gain (&gt;= 0.) 
    kia = db.FloatProperty()

    # Rate feedback gain (&gt;= 0.) 
    kf3 = db.FloatProperty()

    # Saturation factor at e1  (&gt;= 0.) 
    se1 = db.FloatProperty()

    # Exciter field current limit parameter 
    vfemax = db.FloatProperty()

    # Exciter field current feedback gain (&gt;= 0.) 
    kf2 = db.FloatProperty()

    # Exciter time constant, sec. (&gt; 0.) 
    te = Seconds

    # Rate feedback time constant (&gt; 0.) 
    tf = Seconds

    # Exciter field resistance constant 
    ke = db.FloatProperty()

    # Amplifier proportional gain (&gt; 0. if kia = 0.) 
    kpa = db.FloatProperty()

    # Field voltage value 2.    (&gt; 0.) 
    e2 = db.FloatProperty()

    # Saturation factor at e2   (&gt;= 0.) 
    se2 = db.FloatProperty()

    # Exciter field voltage source gain (&gt; 0.) 
    kp = db.FloatProperty()

    # Field voltage value 1   (&gt; 0.) 
    e1 = db.FloatProperty()

    # Regulator integral gain (&gt;= 0.) 
    kir = db.FloatProperty()

    # Filter time constant (&gt;= 0.) 
    tr = Seconds

    # Derivative gain washout time constant (&gt;= 0.) 
    tdr = Seconds

    # Minimum amplifier output (&lt; 0.) 
    vamin = db.FloatProperty()

    # Maximum amplifier output (&gt; 0.) 
    vamax = db.FloatProperty()

    # >>> exc_ac7_b.attributes

    # <<< exc_ac7_b.references
    # @generated
    # >>> exc_ac7_b.references

    # <<< exc_ac7_b.operations
    # @generated
    # >>> exc_ac7_b.operations

# EOF -------------------------------------------------------------------------
