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

class ExcDC1A(ExcitationSystem):
    """ IEEE (1992/2005) DC1A Model  This model is used to represent field-controlled dc commutator exciters with continuously acting voltage regulators (especially the direct-acting rheostatic, rotating amplifier, and magnetic amplifier types). Because this model has been widely implemented by the industry, it is sometimes used to represent other types of systems when detailed data for them are not available or when a simplified model is required. 
    """
    # <<< exc_dc1_a.attributes
    # @generated
    # If not 0, apply lower limit of 0. to exciter output 
    exclim = db.FloatProperty()

    # Minimum controller output (&lt; 0.) 
    vrmin = db.FloatProperty()

    # Lead time constant 
    tc = Seconds

    # Time constant (&gt; 0.) 
    ta = Seconds

    # Lag time constant (&gt;= 0.) 
    tb = Seconds

    # Gain (&gt; 0.) 
    ka = db.FloatProperty()

    # Exciter field resistance line slope 
    ke = db.FloatProperty()

    # Saturation factor at e2  (&gt;= 0.) 
    se2 = db.FloatProperty()

    # Exciter time constant (&gt; 0.) 
    te = Seconds

    # Saturation factor at e1  (&gt;= 0.) 
    se1 = db.FloatProperty()

    # Rate feedback time constant, sec. (&gt; 0.) 
    tf = Seconds

    # Rate feedback gain (&gt;= 0.) 
    kf = db.FloatProperty()

    # UEL input: if &lt; 2, HV gate; if = 2, add to error signal 
    uelin = db.FloatProperty()

    # Filter time constant (&gt;= 0.) 
    tr = Seconds

    # Field voltage value 1    (&gt; 0.) 
    e1 = db.FloatProperty()

    # Maximum controller output 
    vrmax = db.FloatProperty()

    # Field voltage value 2.   (&gt; 0.) 
    e2 = db.FloatProperty()

    # >>> exc_dc1_a.attributes

    # <<< exc_dc1_a.references
    # @generated
    # >>> exc_dc1_a.references

    # <<< exc_dc1_a.operations
    # @generated
    # >>> exc_dc1_a.operations

# EOF -------------------------------------------------------------------------
