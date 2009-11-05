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

""" A rotating machine which may be used as a generator or motor. 
"""

# <<< imports
# @generated
from dynamics.element import Element


from dynamics.domain import ApparentPower
from dynamics.domain import Seconds
from dynamics.domain import Resistance
from dynamics.domain import Reactance

from google.appengine.ext import db
# >>> imports

class RotatingMachine(Element):
    """ A rotating machine which may be used as a generator or motor. 
    """
    # <<< rotating_machine.attributes
    # @generated
    # Nameplate apparent power rating for the unit 
    rated_s = ApparentPower

    # Saturation factor at rated term. voltage (&gt;= 0.) 
    s1 = db.FloatProperty()

    # Saturation factor at 120% of rated term.voltage (&gt;=S1) 
    s12 = db.FloatProperty()

    # Inertia constant of generator or motor and mechanical load (&gt;0). <b>H</b> is the stored energy in the rotating mass. For a generator, this includes the <b>generator plus all other elements (turbine, exciter) on the same shaft</b> and has units of MW-sec. For a motor, it includes the motor plus its mechanical load. Conventional units are per unit on the generator MVA base, usually expressed as MW-sec./MVA or just sec. 
    h = Seconds

    # Damping torque coefficient. <b>D</b> represents a linearized approximation of damping torque effects. This value is often zero when the sources of damping torques (generator damper windings, load damping effects, etc.) are modeled in detail 
    d = db.FloatProperty()

    # Stator (armature) resistance (&gt;= 0.) - Equivalent resistance when used for GenEquiv model 
    rs = Resistance

    # Stator leakage reactance (&gt; 0.) 
    xls = Reactance

    # >>> rotating_machine.attributes

    # <<< rotating_machine.references
    # @generated
    # >>> rotating_machine.references

    # <<< rotating_machine.operations
    # @generated
    # >>> rotating_machine.operations

# EOF -------------------------------------------------------------------------
