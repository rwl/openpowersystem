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

class ExcAC8B(ExcitationSystem):
    """ IEEE (2005) AC8B Model  The AVR in this model consists of PID control, with separate constants for the proportional (<i>KPR</i>), integral (<i>KIR</i>), and derivative (<i>KDR</i>) gains. The representation of the brushless exciter (<i>TE</i>, <i>KE</i>, <i>SE</i>, <i>KC</i>, <i>KD</i>) is similar to the model Type AC2A. The Type AC8B model can be used to represent static voltage regulators applied to brushless excitation systems. Digitally based voltage regulators feeding dc rotating main exciters can be represented with the AC Type AC8B model with the parameters <i>KC </i>and <i>KD </i>set to 0. For thyristor power stages fed from the generator terminals, the limits <i>VRMAX </i>and <i>VRMIN </i>should be a function of terminal voltage: <i>VT </i>x <i>VRMAX </i>and <i>VT </i>x <i>VRMIN</i>. 
    """
    # <<< exc_ac8_b.attributes
    # @generated
    # Voltage Regulator Derivative Gain (&gt;= 0.) 
    kdr = db.FloatProperty()

    # Voltage transducer time constant (&gt;= 0.) 
    tr = Seconds

    # Field voltage value 1     (&gt; 0.) 
    e1 = db.FloatProperty()

    # Field voltage value 2.    (&gt; 0.) 
    e2 = db.FloatProperty()

    # Voltage Regulator Integral Gain (&gt;= 0.) 
    kir = db.FloatProperty()

    # Rectifier regulation factor (&gt;= 0.) 
    kc = db.FloatProperty()

    # Maximum controller output (&gt; 0.) 
    vrmax = db.FloatProperty()

    # Amplifier gain (&gt; 0.) 
    ka = db.FloatProperty()

    # Saturation factor at e2  (&gt;= 0.) 
    se2 = db.FloatProperty()

    # Voltage Regulator Derivative Time Constant (&gt; 0. if kdr &gt; 0.) 
    tdr = Seconds

    # Voltage Regulator Proportional Gain (&gt; 0. if kir = 0.) 
    kpr = db.FloatProperty()

    # Minimum exciter ouput voltage (&lt;= 0.) 
    vemin = db.FloatProperty()

    # Exciter regulation factor (&gt;= 0.) 
    kd = db.FloatProperty()

    # Exciter field time constant (&gt; 0.) 
    te = Seconds

    # Saturation factor at e1 (&gt;= 0.) 
    se1 = db.FloatProperty()

    # Exciter field proportional constant 
    ke = db.FloatProperty()

    # Exciter field current limit parameter 
    vfemax = db.FloatProperty()

    # Amplifier time constant  (&gt;= 0.) 
    ta = Seconds

    # Minimum controller output (&lt;= 0.) 
    vrmin = db.FloatProperty()

    # if not 0, multiply vrmax and vrmin by terminal voltage 
    vtmult = db.FloatProperty()

    # >>> exc_ac8_b.attributes

    # <<< exc_ac8_b.references
    # @generated
    # >>> exc_ac8_b.references

    # <<< exc_ac8_b.operations
    # @generated
    # >>> exc_ac8_b.operations

# EOF -------------------------------------------------------------------------
