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
from dynamics.dynamics.power_system_stabilizers.power_system_stabilizer import PowerSystemStabilizer


from dynamics.domain import Seconds

from google.appengine.ext import db
# >>> imports

class PssIEEE2B(PowerSystemStabilizer):
    """ IEEE (2005) PSS2B Model  This stabilizer model is designed to represent a variety of dual-input stabilizers, which normally use combinations of power and speed or frequency to derive the stabilizing signal. 
    """
    # <<< pss_ieee2_b.attributes
    # @generated
    # Lead/lag time constant 
    t10 = Seconds

    # Numerator constant 
    a = db.FloatProperty()

    # Stabilizer gain 
    ks1 = db.FloatProperty()

    # Gain on signal #2 input before ramp-tracking filter 
    ks3 = db.FloatProperty()

    # Lead/lag time constant 
    t11 = Seconds

    # Gain on signal #2 
    ks2 = db.FloatProperty()

    # Stabilizer output min limit 
    vstmin = db.FloatProperty()

    # Input signal #1 max limit 
    vsi1max = db.FloatProperty()

    # Input signal #2 max limit 
    vsi2max = db.FloatProperty()

    # Lag time constant 
    tb = Seconds

    # Lead/lag time constant 
    t2 = Seconds

    # Lead constant 
    ta = Seconds

    # Lead/lag time constant 
    t1 = Seconds

    # Lead/lag time constant 
    t4 = Seconds

    # Order of ramp tracking filter 
    n = db.BooleanProperty()

    # Lead/lag time constant 
    t3 = Seconds

    # Denominator order of ramp tracking filter 
    m = db.BooleanProperty()

    # Time constant on signal #1 
    t6 = Seconds

    # Lead of ramp tracking filter 
    t8 = Seconds

    # Input signal #1 min limit 
    vsi1min = db.FloatProperty()

    # Time constant on signal #2 
    t7 = Seconds

    # Lag of ramp tracking filter 
    t9 = Seconds

    # Gain on signal #2 input after ramp-tracking filter 
    ks4 = db.FloatProperty()

    # Second washout on signal #1 
    tw2 = Seconds

    # First washout on signal #1 
    tw1 = Seconds

    # Second washout on signal #2 
    tw4 = Seconds

    # Input signal #2 min limit 
    vsi2min = db.FloatProperty()

    # First washout on signal #2 
    tw3 = Seconds

    # Stabilizer output max limit 
    vstmax = db.FloatProperty()

    # >>> pss_ieee2_b.attributes

    # <<< pss_ieee2_b.references
    # @generated
    # >>> pss_ieee2_b.references

    # <<< pss_ieee2_b.operations
    # @generated
    # >>> pss_ieee2_b.operations

# EOF -------------------------------------------------------------------------
