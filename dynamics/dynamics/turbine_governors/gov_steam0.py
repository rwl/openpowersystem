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
from dynamics.dynamics.turbine_governors.turbine_governor import TurbineGovernor


from dynamics.domain import Seconds
from dynamics.domain import ActivePower

from google.appengine.ext import db
# >>> imports

class GovSteam0(TurbineGovernor):
    """ A simplified steam turbine-governor model. 
    """
    # <<< gov_steam0.attributes
    # @generated
    # Numerator time constant of T2/T3 block 
    t2 = Seconds

    # Reheater time constant 
    t3 = Seconds

    # Steam bowl time constant 
    t1 = Seconds

    # Maximum valve position, p.u. of mwcap 
    vmax = db.FloatProperty()

    # Turbine damping coefficient 
    dt = db.FloatProperty()

    # Permanent droop 
    r = db.FloatProperty()

    # Minimum valve position, p.u. of mwcap 
    vmin = db.FloatProperty()

    # Base for power values  (&gt; 0.) 
    mwbase = ActivePower

    # >>> gov_steam0.attributes

    # <<< gov_steam0.references
    # @generated
    # >>> gov_steam0.references

    # <<< gov_steam0.operations
    # @generated
    # >>> gov_steam0.operations

# EOF -------------------------------------------------------------------------
