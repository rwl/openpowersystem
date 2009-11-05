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

class ExcDC3A(ExcitationSystem):
    """ IEEE (1992/2005) DC3A Model  The Type DC3A model is used to represent older systems, in particular those dc commutator exciters with non-continuously acting regulators that were commonly used before the development of the continuously acting varieties. These systems respond at basically two different rates, depending upon the magnitude of voltage error. For small errors, adjustment is made periodically with a signal to a motor-operated rheostat. Larger errors cause resistors to be quickly shorted or inserted and a strong forcing signal applied to the exciter. Continuous motion of the motor-operated rheostat occurs for these larger error signals, even though it is bypassed by contactor action. 
    """
    # <<< exc_dc3_a.attributes
    # @generated
    # Maximum control element output (&gt; 0.) 
    vrmax = db.FloatProperty()

    # Exciter field resistance line slope 
    ke = db.FloatProperty()

    # Exciter field time constant (&gt; 0.) 
    te = Seconds

    # If not 0, apply lower limit of 0. to exciter output 
    exclim = db.FloatProperty()

    # Saturation factor at e1 (&gt;= 0.) 
    se1 = db.FloatProperty()

    # Saturation factor at e2  (&gt;= 0.) 
    se2 = db.FloatProperty()

    # Rheostat full range travel time (&gt; 0.) 
    trh = Seconds

    # Voltage error threshold min/max control action (&gt; 0.) 
    kv = db.FloatProperty()

    # Field voltage value 1    (&gt; 0.) 
    e1 = db.FloatProperty()

    # Field voltage value 2.     (&gt; 0.) 
    e2 = db.FloatProperty()

    # Minimum control element output (&lt;= 0.) 
    vrmin = db.FloatProperty()

    # Filter  time constant (&gt;= 0.) 
    tr = Seconds

    # >>> exc_dc3_a.attributes

    # <<< exc_dc3_a.references
    # @generated
    # >>> exc_dc3_a.references

    # <<< exc_dc3_a.operations
    # @generated
    # >>> exc_dc3_a.operations

# EOF -------------------------------------------------------------------------
