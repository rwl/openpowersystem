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

class ExcAC3A(ExcitationSystem):
    """ IEEE (1992/2005) AC3A Model  The model represents the field-controlled alternator-rectifier excitation systems designated Type AC3A. These excitation systems include an alternator main exciter with non-controlled rectifiers. The exciter employs self-excitation, and the voltage regulator power is derived from the exciter output voltage. Therefore, this system has an additional nonlinearity, simulated by the use of a multiplier whose inputs are the voltage regulator command signal, <i>VA</i>, and the exciter output voltage, <i>EFD</i>, times <i>KR</i>. This model is applicable to excitation systems employing static voltage regulators. 
    """
    # <<< exc_ac3_a.attributes
    # @generated
    # AVR time constant (&gt; 0.) 
    ta = Seconds

    # AVR gain (&gt; 0.) 
    ka = db.FloatProperty()

    # Exciter internal reactance (&gt;= 0.) 
    kd = db.FloatProperty()

    # Saturation factor at e1   (&gt;= 0.) 
    se1 = db.FloatProperty()

    # Rectifier regulation factor (&gt;= 0.) 
    kc = db.FloatProperty()

    # Saturation factor at e2   (&gt;= 0.) 
    se2 = db.FloatProperty()

    # Exciter time constant (&gt; 0.) 
    te = Seconds

    # Rate feedback time constant (&gt; 0.) 
    tf = Seconds

    # TGR lag time constant (&gt;= 0.) 
    tb = Seconds

    # TGR lead time constant 
    tc = Seconds

    # Maximum AVR output (&gt; 0.) 
    vamax = db.FloatProperty()

    # Low level rate feedback gain (&gt;= 0.) 
    kf = db.FloatProperty()

    # Minimum field voltage limit (&lt;= 0.) 
    vemin = db.FloatProperty()

    # Exciter field resistance constant 
    ke = db.FloatProperty()

    # Exciter field current limit parameter (&gt;= 0.) 
    vfemax = db.FloatProperty()

    # Filter time constant (&gt;= 0.) 
    tr = Seconds

    # Field voltage value 2.     (&gt; 0.) 
    e2 = db.FloatProperty()

    # Field voltage value 1     (&gt; 0.) 
    e1 = db.FloatProperty()

    # High level rate feedback gain (&gt;= 0.) 
    kn = db.FloatProperty()

    # Minimum AVR output (&lt; 0.) 
    vamin = db.FloatProperty()

    # Field self-excitation feedback gain (&gt; 0.) 
    kr = db.FloatProperty()

    # Rate feedback gain break level (&gt; 0.) 
    efdn = db.FloatProperty()

    # >>> exc_ac3_a.attributes

    # <<< exc_ac3_a.references
    # @generated
    # >>> exc_ac3_a.references

    # <<< exc_ac3_a.operations
    # @generated
    # >>> exc_ac3_a.operations

# EOF -------------------------------------------------------------------------
