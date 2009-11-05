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

class ExcAC4A(ExcitationSystem):
    """ IEEE (1992/2005) AC4A Model  The Type AC4A alternator-supplied controlled-rectifier excitation system is quite different from the other type ac systems. This high initial response excitation system utilizes a full thyristor bridge in the exciter output circuit. The voltage regulator controls the firing of the thyristor bridges. The exciter alternator uses an independent voltage regulator to control its output voltage to a constant value. These effects are not modeled; however, transient loading effects on the exciter alternator are included. 
    """
    # <<< exc_ac4_a.attributes
    # @generated
    # Lag time constant (&gt;= 0.) 
    tb = Seconds

    # Time constant (&gt; 0.) 
    ta = Seconds

    # Lead time constant 
    tc = Seconds

    # Minimum controller output (&lt; 0.) 
    vrmin = db.FloatProperty()

    # Maximum error signal ( &gt; 0.) 
    vimax = db.FloatProperty()

    # Maximum controller output (&gt; 0.) 
    vrmax = db.FloatProperty()

    # Filter time constant (&gt;= 0.) 
    tr = Seconds

    # Excitation system regulation (&gt;= 0.) 
    kc = db.FloatProperty()

    # Minimum error signal (&lt; 0.) 
    vimin = db.FloatProperty()

    # Gain (&gt; 0.) 
    ka = db.FloatProperty()

    # >>> exc_ac4_a.attributes

    # <<< exc_ac4_a.references
    # @generated
    # >>> exc_ac4_a.references

    # <<< exc_ac4_a.operations
    # @generated
    # >>> exc_ac4_a.operations

# EOF -------------------------------------------------------------------------
