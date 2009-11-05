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

class GovHydro1(TurbineGovernor):
    """ Hydro turbine-governor model. 
    """
    # <<< gov_hydro1.attributes
    # @generated
    # Permanent droop (R) (&gt;0) 
    rperm = db.FloatProperty()

    # Gate servo time constant (&gt;0) 
    tg = Seconds

    # Filter time constant (&gt;0) 
    tf = Seconds

    # Base for power values  (&gt; 0.) 
    mwbase = ActivePower

    # Turbine gain (&gt;0) 
    at = db.FloatProperty()

    # No-load flow at nominal head (&gt;=0) 
    qnl = db.FloatProperty()

    # Water inertia time constant (&gt;0) 
    tw = Seconds

    # Turbine damping factor (&gt;=0) 
    dturb = db.FloatProperty()

    # Temporary droop (r) (&gt;R) 
    rtemp = db.FloatProperty()

    # Washout time constant (&gt;0) 
    tr = Seconds

    # >>> gov_hydro1.attributes

    # <<< gov_hydro1.references
    # @generated
    # >>> gov_hydro1.references

    # <<< gov_hydro1.operations
    # @generated
    # >>> gov_hydro1.operations

# EOF -------------------------------------------------------------------------
