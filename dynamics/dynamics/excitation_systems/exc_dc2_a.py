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

class ExcDC2A(ExcitationSystem):
    """ IEEE (1992/2005) DC2A Model  The model is used to represent field-controlled dc commutator exciters with continuously acting voltage regulators having supplies obtained from the generator or auxiliary bus. It differs from the Type DC1A model only in the voltage regulator output limits, which are now proportional to terminal voltage <i>V</i><i><sub>T</sub></i>. It is representative of solid-state replacements for various forms of older mechanical and rotating amplifier regulating equipment connected to dc commutator exciters. 
    """
    # <<< exc_dc2_a.attributes
    # @generated
    # Exciter time constant (&gt; 0.) 
    te = Seconds

    # Rate feedback time constant, sec. (&gt; 0.) 
    tf = Seconds

    # Gain (&gt; 0.) 
    ka = db.FloatProperty()

    # Lead time constant 
    tc = Seconds

    # Minimum controller output (&lt; 0.) 
    vrmin = db.FloatProperty()

    # Time constant (&gt; 0.) 
    ta = Seconds

    # Lag time constant (&gt;= 0.) 
    tb = Seconds

    # Maximum controller output 
    vrmax = db.FloatProperty()

    # Rate feedback gain (&gt;= 0.) 
    kf = db.FloatProperty()

    # Exciter field resistance line slope 
    ke = db.FloatProperty()

    # UEL input: if &lt; 2, HV gate; if = 2, add to error signal 
    uelin = db.FloatProperty()

    # Saturation factor at e1  (&gt;= 0.) 
    se1 = db.FloatProperty()

    # Filter time constant (&gt;= 0.) 
    tr = Seconds

    # Saturation factor at e2  (&gt;= 0.) 
    se2 = db.FloatProperty()

    # If not 0, apply lower limit of 0. to exciter output 
    exclim = db.FloatProperty()

    # Field voltage value 2.    (&gt; 0.) 
    e2 = db.FloatProperty()

    # Field voltage value 1     (&gt; 0.) 
    e1 = db.FloatProperty()

    # >>> exc_dc2_a.attributes

    # <<< exc_dc2_a.references
    # @generated
    # >>> exc_dc2_a.references

    # <<< exc_dc2_a.operations
    # @generated
    # >>> exc_dc2_a.operations

# EOF -------------------------------------------------------------------------
