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

class ExcAC1A(ExcitationSystem):
    """ IEEE (1992/2005) AC1A Model The model represents the field-controlled alternator-rectifier excitation systems designated Type AC1A. These excitation systems consist of an alternator main exciter with non-controlled rectifiers. 
    """
    # <<< exc_ac1_a.attributes
    # @generated
    # Saturation factor at e1  (&gt;= 0.) 
    se1 = db.FloatProperty()

    # Saturation factor at e2   (&gt;= 0.) 
    se2 = db.FloatProperty()

    # Field voltage value 2.   (&gt; 0.) 
    e2 = db.FloatProperty()

    # Field voltage value 1    (&gt; 0.) 
    e1 = db.FloatProperty()

    # Filter time constant (&gt;= 0.) 
    tr = Seconds

    # Minimum AVR output (&lt; 0.) 
    vamin = db.FloatProperty()

    # Maximum AVR output (&gt; 0.) 
    vamax = db.FloatProperty()

    # Maximum exciter control signal (&gt; 0.) 
    vrmax = db.FloatProperty()

    # TGR lag time constant (&gt;= 0.) 
    tb = Seconds

    # Exciter internal reactance  (&gt;= 0.) 
    kd = db.FloatProperty()

    # TGR lead time constant 
    tc = Seconds

    # Rectifier regulation factor (&gt;= 0.) 
    kc = db.FloatProperty()

    # Rate feedback gain (&gt;= 0.) 
    kf = db.FloatProperty()

    # AVR time constant (&gt; 0.) 
    ta = Seconds

    # Minimum exciter control signal  (&lt; 0.) 
    vrmin = db.FloatProperty()

    # Exciter field resistance constant 
    ke = db.FloatProperty()

    # Exciter time constant (&gt; 0.) 
    te = Seconds

    # Rate feedback time constant (&gt; 0.) 
    tf = Seconds

    # AVR gain (&gt; 0.) 
    ka = db.FloatProperty()

    # >>> exc_ac1_a.attributes

    # <<< exc_ac1_a.references
    # @generated
    # >>> exc_ac1_a.references

    # <<< exc_ac1_a.operations
    # @generated
    # >>> exc_ac1_a.operations

# EOF -------------------------------------------------------------------------
