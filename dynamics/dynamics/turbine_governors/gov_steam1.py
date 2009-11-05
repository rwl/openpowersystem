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


from dynamics.domain import Frequency
from dynamics.domain import ActivePower
from dynamics.domain import Seconds

from google.appengine.ext import db
# >>> imports

class GovSteam1(TurbineGovernor):
    """ IEEE steam turbine/governor model  (with optional deadband and nonlinear valve gain added) 
    """
    # <<< gov_steam1.attributes
    # @generated
    # Intentional db hysteresis 
    eps = Frequency

    # Maximum valve closing velocity, p.u./sec (&lt; 0.) 
    uc = db.FloatProperty()

    # Base for power values (&gt; 0.) 
    mwbase = ActivePower

    # Minimum valve opening (&gt;= 0.) 
    pmin = db.FloatProperty()

    # Fraction of HP shaft power after second boiler pass 
    k3 = db.FloatProperty()

    # Governor gain (reciprocal of droop) (&gt; 0.) 
    k = db.FloatProperty()

    # Fraction of LP shaft power after first boiler pass 
    k2 = db.FloatProperty()

    # Fraction of HP shaft power after first boiler pass 
    k1 = db.FloatProperty()

    # Nonlinear gain power value point 1 
    pgv1 = db.FloatProperty()

    # Fraction of HP shaft power after fourth boiler pass 
    k7 = db.FloatProperty()

    # Fraction of LP shaft power after third boiler pass 
    k6 = db.FloatProperty()

    # Maximum valve opening (&gt; Pmin) 
    pmax = db.FloatProperty()

    # Fraction of HP shaft power after third boiler pass 
    k5 = db.FloatProperty()

    # Fraction of LP shaft power after second boiler pass 
    k4 = db.FloatProperty()

    # Nonlinear gain valve position point 6 
    gv6 = db.FloatProperty()

    # Time constant of third boiler pass 
    t6 = Seconds

    # Nonlinear gain power value point 6 
    pgv6 = db.FloatProperty()

    # Time constant of fourth boiler pas 
    t7 = Seconds

    # Nonlinear gain valve position point 5 
    gv5 = db.FloatProperty()

    # Fraction of LP shaft power after fourth boiler pass 
    k8 = db.FloatProperty()

    # Nonlinear gain valve position point 1 
    gv1 = db.FloatProperty()

    # Governor lag time constant 
    t1 = Seconds

    # Governor lead time constant 
    t2 = Seconds

    # Nonlinear gain power value point 3 
    pgv3 = db.FloatProperty()

    # Intentional deadband width 
    db1 = Frequency

    # Valve positioner time constant (&gt; 0.) 
    t3 = Seconds

    # Maximum valve opening velocity (&gt; 0.) 
    uo = db.FloatProperty()

    # Nonlinear gain power value point 2 
    pgv2 = db.FloatProperty()

    # Nonlinear gain valve position point 4 
    gv4 = db.FloatProperty()

    # Nonlinear gain power value point 5 
    pgv5 = db.FloatProperty()

    # Inlet piping/steam bowl time constant 
    t4 = Seconds

    # Nonlinear gain valve position point 2 
    gv2 = db.FloatProperty()

    # Nonlinear gain valve position point 3 
    gv3 = db.FloatProperty()

    # Time constant of second boiler pass 
    t5 = Seconds

    # Nonlinear gain power value point 4 
    pgv4 = db.FloatProperty()

    # Unintentional deadband 
    db2 = ActivePower

    # >>> gov_steam1.attributes

    # <<< gov_steam1.references
    # @generated
    # >>> gov_steam1.references

    # <<< gov_steam1.operations
    # @generated
    # >>> gov_steam1.operations

# EOF -------------------------------------------------------------------------
