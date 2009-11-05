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

class ExcST3A(ExcitationSystem):
    """ IEEE (1992/2005) ST3A Model  Some static systems utilize a field voltage control loop to linearize the exciter control characteristic. This also makes the output independent of supply source variations until supply limitations are reached. These systems utilize a variety of controlled-rectifier designs: full thyristor complements or hybrid bridges in either series or shunt configurations. The power source may consist of only a potential source, either fed from the machine terminals or from internal windings. Some designs may have compound power sources utilizing both machine potential and current. These power sources are represented as phasor combinations of machine terminal current and voltage and are accommodated by suitable parameters in the model Type ST3A. 
    """
    # <<< exc_st3_a.attributes
    # @generated
    # Minimum AVR output (&lt; 0.) 
    vrmin = db.FloatProperty()

    # Exciter regulation factor (&gt;= 0.) 
    kc = db.FloatProperty()

    # AVR gain (&gt; 0.) 
    ka = db.FloatProperty()

    # Maximum excitation voltage (&gt; 0.) 
    vbmax = db.FloatProperty()

    # Minimum error (&lt; 0.) 
    vimin = db.FloatProperty()

    # P-bar reactance (&gt;= 0.) 
    xl = db.FloatProperty()

    # Maximum inner loop feedback voltage (&gt;= 0.) 
    vgmax = db.FloatProperty()

    # Phase angle of potential source 
    angp = db.FloatProperty()

    # Minimum inner loop output (&lt;= 0.) 
    vmmin = db.FloatProperty()

    # Maximum AVR output (&gt; 0.) 
    vrmax = db.FloatProperty()

    # Potential source gain (&gt; 0.) 
    kp = db.FloatProperty()

    # Inner loop forward gain (&gt; 0.) 
    km = db.FloatProperty()

    # Maximum error (&gt; 0.) 
    vimax = db.FloatProperty()

    # Voltage transducer time constant (&gt;= 0.) 
    tr = Seconds

    # Maximum inner loop output (&gt; 0.) 
    vmmax = db.FloatProperty()

    # Current source gain (&gt;= 0.) 
    ki = db.FloatProperty()

    # Inner loop time constant (&gt; 0.) 
    tm = Seconds

    # AVR time constant (&gt;= 0.) 
    ta = Seconds

    # AVR lag time constant (&gt;= 0.) 
    tb = Seconds

    # Inner loop feedback gain (&gt;= 0.) 
    kg = db.FloatProperty()

    # AVR lead time constant 
    tc = Seconds

    # >>> exc_st3_a.attributes

    # <<< exc_st3_a.references
    # @generated
    # >>> exc_st3_a.references

    # <<< exc_st3_a.operations
    # @generated
    # >>> exc_st3_a.operations

# EOF -------------------------------------------------------------------------
