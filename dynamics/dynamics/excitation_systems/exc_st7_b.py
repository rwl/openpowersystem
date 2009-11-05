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

class ExcST7B(ExcitationSystem):
    """ IEEE (2005) ST7B Model  The model ST7B is representative of static potential-source excitation systems. In this system, the AVR consists of a PI voltage regulator. A phase lead-lag filter in series allows introduction of a derivative function, typically used with brushless excitation systems. In that case, the regulator is of the PID type. In addition, the terminal voltage channel includes a phase lead-lag filter. The AVR includes the appropriate inputs on its reference for overexcitation limiter (OEL1), underexcitation limiter (UEL), stator current limiter (SCL), and current compensator (DROOP). All these limitations, when they work at voltage reference level, keep the PSS (VS signal from Type PSS1A, PSS2A, or PSS2B) in operation. However, the UEL limitation can also be transferred to the high value (HV) gate acting on the output signal. In addition, the output signal passes through a low value (LV) gate for a ceiling overexcitation limiter (OEL2). 
    """
    # <<< exc_st7_b.attributes
    # @generated
    # Input lead-lag numerator time constant (&gt;= 0.) 
    tg = Seconds

    # Regulator proportional gain (&gt; 0.) 
    kpa = db.FloatProperty()

    # Minimum voltage reference signal (&gt; 0.) 
    vmin = db.FloatProperty()

    # Maximum field voltage output (&gt; 0.) 
    vrmax = db.FloatProperty()

    # Low-value gate feedback gain (&gt;= 0.) 
    kl = db.FloatProperty()

    # Filter time constant 
    tr = Seconds

    # High-value gate feedback gain (&gt;= 0.) 
    kh = db.FloatProperty()

    # Rectifier firing time constant (&gt;= 0.) (not in IEEE model) 
    ts = Seconds

    # Minimum field voltage output (&lt; 0.) 
    vrmin = db.FloatProperty()

    # OEL input selector: 1 ? add to Vref, 2 ? input LV gate,  2 ? output LV gate, 0 ? no OEL input 
    oelin = db.FloatProperty()

    # UEL input selector: 1 ? add to Vref, 2 ? input HV gate,  3 ? output HV gate, 0 ? no UEL input 
    uelin = db.FloatProperty()

    # Feedback time constant (&gt;= 0.) 
    tia = Seconds

    # Lead-lag denominator time constant (&gt;= 0.) 
    tb = Seconds

    # Lead-lag numerator time constant (&gt;= 0.) 
    tc = Seconds

    # Input lead-lag denominator time constant (&gt;= 0.) 
    tf = Seconds

    # Feedback gain (&gt;= 0.) 
    kia = db.FloatProperty()

    # Maximum voltage reference signal (&gt; 0.) 
    vmax = db.FloatProperty()

    # >>> exc_st7_b.attributes

    # <<< exc_st7_b.references
    # @generated
    # >>> exc_st7_b.references

    # <<< exc_st7_b.operations
    # @generated
    # >>> exc_st7_b.operations

# EOF -------------------------------------------------------------------------
