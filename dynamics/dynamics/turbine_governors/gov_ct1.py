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

class GovCT1(TurbineGovernor):
    """ General model for any prime mover with a PID governor, used primarily for combustion turbine and combined cycle units. 
    """
    # <<< gov_ct1.attributes
    # @generated
    # Maximum rate of load limit decrease 
    rdown = db.FloatProperty()

    # Maximum valve position limit 
    vmax = db.FloatProperty()

    # No load fuel flow 
    wfnl = db.FloatProperty()

    # Governor derivative controller time constant 
    tdgov = Seconds

    # Acceleration limiter setpoint 
    aset = db.FloatProperty()

    # Permanent droop 
    r = db.FloatProperty()

    # Switch for fuel source characteristic = 0 for fuel flow independent of speed = 1 fuel flow proportional to speed 
    wfspd = db.BooleanProperty()

    # Governor proportional gain 
    kpgov = db.FloatProperty()

    # Minimum value for speed error signal 
    minerr = db.FloatProperty()

    # Temperature detection lead time constant 
    tsa = Seconds

    # Actuator time constant 
    tact = Seconds

    # Temperature detection lag time constant 
    tsb = Seconds

    # Load limiter reference value 
    ldref = db.FloatProperty()

    # Power controller (reset) gain 
    kimw = db.FloatProperty()

    # Maximum value for speed error signal 
    maxerr = db.FloatProperty()

    # Minimum valve position limit 
    vmin = db.FloatProperty()

    # Base for power values (&gt; 0.) 
    mwbase = ActivePower

    # Minimum valve closing rate 
    rclose = db.FloatProperty()

    # Electrical power transducer time constant, sec. (&gt;0.) 
    tpelec = Seconds

    # Maximum rate of load limit increase 
    rup = db.FloatProperty()

    # Turbine lag time constant, sec.  (&gt;0.) 
    tb = Seconds

    # Acceleration limiter gain 
    ka = db.FloatProperty()

    # Acceleration limiter time constant (&gt;0.) 
    ta = Seconds

    # Governor derivative gain 
    kdgov = db.FloatProperty()

    # Turbine gain  (&gt;0.) 
    kturb = db.FloatProperty()

    # Speed governor dead band 
    db = db.FloatProperty()

    # Transport time delay for diesel engine 
    teng = Seconds

    # Turbine lead time constant, sec. 
    tc = Seconds

    # Maximum valve opening rate 
    ropen = db.FloatProperty()

    # Speed sensitivity coefficient 
    dm = db.FloatProperty()

    # Load limiter integral gain for PI controller 
    kiload = db.FloatProperty()

    # Power controller setpoint 
    pmwset = ActivePower

    # Feedback signal for droop  = 1 electrical power = 0 none (isochronous governor) = -1 fuel valve stroke ( true stroke) = -2 governor output ( requested stroke) 
    rselect = db.BooleanProperty()

    # Governor integral gain 
    kigov = db.FloatProperty()

    # Load limiter proportional gain for PI controller 
    kpload = db.FloatProperty()

    # Load Limiter time constant (&gt;0.) 
    tfload = Seconds

    # >>> gov_ct1.attributes

    # <<< gov_ct1.references
    # @generated
    # >>> gov_ct1.references

    # <<< gov_ct1.operations
    # @generated
    # >>> gov_ct1.operations

# EOF -------------------------------------------------------------------------
