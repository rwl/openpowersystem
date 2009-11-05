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

class ExcAC2A(ExcitationSystem):
    """ IEEE (1992/2005) AC2A Model The model designated as Type AC2A, represents a high initial response fieldcontrolled alternator-rectifier excitation system. The alternator main exciter is used with non-controlled rectifiers. The Type AC2A model is similar to that of Type AC1A except for the inclusion of exciter time constant compensation and exciter field current limiting elements. 
    """
    # <<< exc_ac2_a.attributes
    # @generated
    # TGR lag time constant (&gt;= 0.) 
    tb = Seconds

    # Field voltage value 1     (&gt; 0.) 
    e1 = db.FloatProperty()

    # AVR time constant (&gt; 0.) 
    ta = Seconds

    # Minimum exciter control signal (&lt; 0.) 
    vrmin = db.FloatProperty()

    # Field voltage value 2.    (&gt; 0.) 
    e2 = db.FloatProperty()

    # Exciter field current limit parameter (&gt;= 0.) 
    vfemax = db.FloatProperty()

    # Maximum exciter control signal (&gt; 0.) 
    vrmax = db.FloatProperty()

    # AVR gain (&gt; 0.) 
    ka = db.FloatProperty()

    # Saturation factor at e1  (&gt;= 0.) 
    se1 = db.FloatProperty()

    # Saturation factor at e2   (&gt;= 0.) 
    se2 = db.FloatProperty()

    # Rate feedback gain (&gt;= 0.) 
    kf = db.FloatProperty()

    # Exciter field current feedback gain (&gt;= 0.) 
    kh = db.FloatProperty()

    # Rectifier regulation factor (&gt;= 0.) 
    kc = db.FloatProperty()

    # Minimum AVR output (&lt; 0.) 
    vamin = db.FloatProperty()

    # Exciter field current controller gain (&gt; 0.) 
    kb = db.FloatProperty()

    # Exciter field resistance constant 
    ke = db.FloatProperty()

    # Filter time constant (&gt;= 0.) 
    tr = Seconds

    # Exciter internal reactance (&gt;= 0.) 
    kd = db.FloatProperty()

    # Exciter time constant (&gt; 0.) 
    te = Seconds

    # TGR lead time constant 
    tc = Seconds

    # Maximum AVR output (&gt; 0.) 
    vamax = db.FloatProperty()

    # Rate feedback time constant (&gt; 0.) 
    tf = Seconds

    # >>> exc_ac2_a.attributes

    # <<< exc_ac2_a.references
    # @generated
    # >>> exc_ac2_a.references

    # <<< exc_ac2_a.operations
    # @generated
    # >>> exc_ac2_a.operations

# EOF -------------------------------------------------------------------------
