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

class ExcST4B(ExcitationSystem):
    """ IEEE (2005) ST4B Model  This model is a variation of the Type ST3A model, with a proportional plus integral (PI) regulator block replacing the lag-lead regulator characteristic that was in the ST3A model. Both potential- and compoundsource rectifier excitation systems are modeled. The PI regulator blocks have nonwindup limits that are represented. The voltage regulator of this model is typically implemented digitally. 
    """
    # <<< exc_st4_b.attributes
    # @generated
    # Potential source gain (&gt; 0.) 
    kp = db.FloatProperty()

    # P-bar leakage reactance (&gt;= 0.) 
    xl = db.FloatProperty()

    # Maximum excitation voltage (&gt; 0.) 
    vbmax = db.FloatProperty()

    # Current source gain (&gt;= 0.) 
    ki = db.FloatProperty()

    # AVR Integral gain 
    kir = db.FloatProperty()

    # Minimum AVR output (&lt; 0.) 
    vrmin = db.FloatProperty()

    # Minimum inner loop regulator output 
    vmmin = db.FloatProperty()

    # Integral gain of inner loop regulator 
    kim = db.FloatProperty()

    # AVR time constant (&gt;= 0.) 
    ta = Seconds

    # Inner loop feedback gain (&gt;= 0.) 
    kg = db.FloatProperty()

    # Voltage transducer time constant (&gt;= 0.) 
    tr = Seconds

    # Exciter regulation factor (&gt;= 0.) 
    kc = db.FloatProperty()

    # Maximum AVR output (&gt; 0.) 
    vrmax = db.FloatProperty()

    # Phase angle of potential source 
    angp = db.FloatProperty()

    # AVR proportional gain 
    kpr = db.FloatProperty()

    # Maximum inner loop feedback gain (&gt;= 0.) 
    vgmax = db.FloatProperty()

    # Prop. gain of inner loop regulator 
    kpm = db.FloatProperty()

    # Maximum inner loop regulator output 
    vmmax = db.FloatProperty()

    # >>> exc_st4_b.attributes

    # <<< exc_st4_b.references
    # @generated
    # >>> exc_st4_b.references

    # <<< exc_st4_b.operations
    # @generated
    # >>> exc_st4_b.operations

# EOF -------------------------------------------------------------------------
