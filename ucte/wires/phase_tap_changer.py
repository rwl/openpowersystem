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

""" A specialization of a voltage tap changer that has detailed modeling for phase shifting capabilities.   A phase shifting tap changer is also in general a voltage magnitude transformer.    The symmetrical and asymmetrical transformer tap changer models are defined here. 
"""

# <<< imports
# @generated
from ucte.wires.tap_changer import TapChanger


from ucte.domain import Reactance
from ucte.domain import AngleDegrees
from ucte.wires import PhaseTapChangerKind
from ucte.domain import Voltage

from google.appengine.ext import db
# >>> imports

class PhaseTapChanger(TapChanger):
    """ A specialization of a voltage tap changer that has detailed modeling for phase shifting capabilities.   A phase shifting tap changer is also in general a voltage magnitude transformer.    The symmetrical and asymmetrical transformer tap changer models are defined here. 
    """
    # <<< phase_tap_changer.attributes
    # @generated
    # The reactance at the minimum tap step. 
    x_step_min = Reactance

    # The reactance at the maximum tap step. 
    x_step_max = Reactance

    # Phase shift per step position. A positive value indicates a positive phase shift from the winding where the tap is located to the other winding (for a two-winding transformer). The actual phase shift increment might be more accureatly computed from the symmetrical or asymmetrical models or a tap step table lookup if those are available. 
    step_phase_shift_increment = AngleDegrees

    # The phase angle between the in-phase winding and the out-of -phase winding used for creating phase shift.   It is only possible to have a symmemtrical transformer if this angle is 90 degrees. This is required if PST is Asymmetrical 
    winding_connection_angle = AngleDegrees

    # The type of phase shifter construction. 
    phase_tap_changer_type = PhaseTapChangerKind

    # The voltage step increment on the out of phase winding.    This voltage step on the out of phase winding of the phase shifter.  Similar to TapChanger.voltageStepIncrement, but it is applied only to the out of phase winding. This is required if PST is Asymmetrical. 
    voltage_step_increment_out_of_phase = Voltage

    # >>> phase_tap_changer.attributes

    # <<< phase_tap_changer.references
    # @generated
    # The transformer winding to which the phase tap changer belongs. 
    transformer_winding = db.ReferenceProperty(db.Model, collection_name="_phase_tap_changer_set")

    # >>> phase_tap_changer.references

    # <<< phase_tap_changer.operations
    # @generated
    # >>> phase_tap_changer.operations

# EOF -------------------------------------------------------------------------
