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

class ExcAC5A(ExcitationSystem):
    """ IEEE (1992/2005) AC5A Model  The model designated as Type AC5A, is a simplified model for brushless excitation systems. The regulator is supplied from a source, such as a permanent magnet generator, which is not affected by system disturbances. Unlike other ac models, this model uses loaded rather than open circuit exciter saturation data in the same way as it is used for the dc models. Because the model has been widely implemented by the industry, it is sometimes used to represent other types of systems when either detailed data for them are not available or simplified models are required. 
    """
    # <<< exc_ac5_a.attributes
    # @generated
    # Time constant (&gt; 0.) 
    ta = Seconds

    # Maximum controller output (&gt; 0.) 
    vrmax = db.FloatProperty()

    # Gain  (&gt; 0.) 
    ka = db.FloatProperty()

    # Minimum controller output (&lt;  0.) 
    vrmin = db.FloatProperty()

    # Filter time constant (&gt;= 0.) 
    tr = Seconds

    # Rate feedback lag time constant (&gt; 0.) 
    tf1 = Seconds

    # Exciter field resistance line slope 
    ke = db.FloatProperty()

    # Rate feedback lag time constant (&gt;= 0.) 
    tf2 = Seconds

    # Exciter time constant, sec. (&gt; 0.) 
    te = Seconds

    # Rate feedback gain (&gt;= 0.) 
    kf = db.FloatProperty()

    # Field voltage value 1      (&gt; 0.) 
    e1 = db.FloatProperty()

    # Rate feedback lead time constant 
    tf3 = Seconds

    # Field voltage value 2.  (&gt; 0.) 
    e2 = db.FloatProperty()

    # Saturation factor at e1  (&gt;= 0.) 
    se1 = db.FloatProperty()

    # Saturation factor at e2 (&gt;= 0.) 
    se2 = db.FloatProperty()

    # >>> exc_ac5_a.attributes

    # <<< exc_ac5_a.references
    # @generated
    # >>> exc_ac5_a.references

    # <<< exc_ac5_a.operations
    # @generated
    # >>> exc_ac5_a.operations

# EOF -------------------------------------------------------------------------
