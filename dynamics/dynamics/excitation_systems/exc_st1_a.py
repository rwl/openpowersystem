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

class ExcST1A(ExcitationSystem):
    """ IEEE (1992/2005) ST1A Model  The computer model of the Type ST1A potential-source controlled-rectifier excitation system represents systems in which excitation power is supplied through a transformer from the generator terminals (or the unit's auxiliary bus) and is regulated by a controlled rectifier. The maximum exciter voltage available from such systems is directly related to the generator terminal voltage. 
    """
    # <<< exc_st1_a.attributes
    # @generated
    # Excitation voltage lower limit (&lt; 0.) 
    vrmin = db.FloatProperty()

    # Excitation system regulation factor (&gt;= 0.) 
    kc = db.FloatProperty()

    # Minimum error (&lt; 0.) 
    vimin = db.FloatProperty()

    # = 2 ? UEL input added to error signal = 1 ? UEL input HV gate with error signal = -1 ? UEL input HV gate with volt. reg. output = 0 ? ignore UEL signal 
    uelin = db.FloatProperty()

    # Rate feedback time constant (&gt;= 0.) 
    tf = Seconds

    # Rate feedback gain (&gt;= 0.) 
    kf = db.FloatProperty()

    # Lead time constant 
    tc1 = Seconds

    # = 0 ? PSS input (Vs) added to error signal not 0 ? PSS input (Vs) added to voltage regulator output 
    pssin = db.FloatProperty()

    # Lead time constant 
    tc = Seconds

    # Lag time constant (&gt;= 0.) 
    tb = Seconds

    # Gain (&gt; 0.) 
    ka = db.FloatProperty()

    # Time constant (&gt;= 0.) 
    ta = Seconds

    # Voltage transducer time constant (&gt;= 0.) 
    tr = Seconds

    # Maximum field current 
    ilr = db.FloatProperty()

    # Minimum control element output (&lt; 0.) 
    vamin = db.FloatProperty()

    # Gain on field current limit 
    klr = db.FloatProperty()

    # Lag time constant (&gt;= 0.) 
    tb1 = Seconds

    # Maximum control element output (&gt; 0.) 
    vamax = db.FloatProperty()

    # Excitation voltage upper limit (&gt; 0.) 
    vrmax = db.FloatProperty()

    # Maximum error (&gt; 0.) 
    vimax = db.FloatProperty()

    # >>> exc_st1_a.attributes

    # <<< exc_st1_a.references
    # @generated
    # >>> exc_st1_a.references

    # <<< exc_st1_a.operations
    # @generated
    # >>> exc_st1_a.operations

# EOF -------------------------------------------------------------------------
