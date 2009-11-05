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
from dynamics.domain import Frequency
from dynamics.domain import ActivePower

from google.appengine.ext import db
# >>> imports

class GovHydro2(TurbineGovernor):
    # <<< gov_hydro2.attributes
    # @generated
    # Turbine denominator multiplier 
    bturb = db.FloatProperty()

    # Temporary droop 
    rtemp = db.FloatProperty()

    # Water inertia time constant 
    tw = Seconds

    # Permanent droop 
    rperm = db.FloatProperty()

    # Nonlinear gain point 1, p.u. gv 
    gv1 = db.FloatProperty()

    # Nonlinear gain point 2, p.u. gv 
    gv2 = db.FloatProperty()

    # Dashpot time constant 
    tr = Seconds

    # Turbine numerator multiplier 
    aturb = db.FloatProperty()

    # Pilot servo valve time constant 
    tp = Seconds

    # Maximum gate opening velocity 
    uo = db.FloatProperty()

    # Nonlinear gain point 6, p.u. gv 
    gv6 = db.FloatProperty()

    # Nonlinear gain point 5, p.u. gv 
    gv5 = db.FloatProperty()

    # Nonlinear gain point 5, p.u. power 
    pgv5 = db.FloatProperty()

    # Nonlinear gain point 4, p.u. gv 
    gv4 = db.FloatProperty()

    # Nonlinear gain point 6, p.u. power 
    pgv6 = db.FloatProperty()

    # Nonlinear gain point 3, p.u. gv 
    gv3 = db.FloatProperty()

    # Nonlinear gain point 2, p.u. power 
    pgv2 = db.FloatProperty()

    # Nonlinear gain point 1, p.u. power 
    pgv1 = db.FloatProperty()

    # Intentional deadband width 
    db1 = Frequency

    # Nonlinear gain point 4, p.u. power 
    pgv4 = db.FloatProperty()

    # Turbine gain 
    kturb = db.FloatProperty()

    # Unintentional deadband 
    db2 = ActivePower

    # Gate servo time constant 
    tg = Seconds

    # Maximum gate opening 
    pmax = db.FloatProperty()

    # Nonlinear gain point 3, p.u. power 
    pgv3 = db.FloatProperty()

    # Base for power values (&gt; 0.) 
    mwbase = ActivePower

    # Maximum gate closing velocity (&lt;0.) 
    uc = db.FloatProperty()

    # Minimum gate opening 
    pmin = db.FloatProperty()

    # Intentional db hysteresis 
    eps = Frequency

    # >>> gov_hydro2.attributes

    # <<< gov_hydro2.references
    # @generated
    # >>> gov_hydro2.references

    # <<< gov_hydro2.operations
    # @generated
    # >>> gov_hydro2.operations

# EOF -------------------------------------------------------------------------
