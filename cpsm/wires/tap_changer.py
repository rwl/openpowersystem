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

""" Mechanism for changing transformer winding tap positions. 
"""

# <<< imports
# @generated
from cpsm.core.power_system_resource import PowerSystemResource

from cpsm.wires.regulating_control import RegulatingControl
from cpsm.wires.transformer_winding import TransformerWinding

from cpsm.domain import AngleDegrees
from cpsm.wires import TransformerControlMode
from cpsm.domain import PerCent
from cpsm.wires import TapChangerKind
from cpsm.domain import Voltage

from google.appengine.ext import db
# >>> imports

class TapChanger(PowerSystemResource):
    """ Mechanism for changing transformer winding tap positions. 
    """
    # <<< tap_changer.attributes
    # @generated
    # The tap step position used in 'normal' network operation for this winding. For a 'Fixed' tap changer indicates the current physical tap setting. 
    normal_step = db.IntegerProperty()

    # Highest possible tap step position, advance from neutral 
    high_step = db.IntegerProperty()

    # Phase shift per step position. A positive value indicates a positive phase shift from the winding where the tap is located to the other winding (for a two-winding transformer). 
    step_phase_shift_increment = AngleDegrees

    # The neutral tap step position for this winding. 
    neutral_step = db.IntegerProperty()

    # Lowest possible tap step position, retard from neutral 
    low_step = db.IntegerProperty()

    # For an LTC, the tap changer control mode. 
    tcul_control_mode = TransformerControlMode

    # Tap step increment, in per cent of nominal voltage, per step position. 
    step_voltage_increment = PerCent

    # The type of tap changer. Indicates the ability of the transformer to perform various regulation tasks. The tap changer must be also be associated wtih a RegulationControl object before any regulation is possible. 
    type = TapChangerKind

    # Voltage at which the winding operates at the neutral tap setting. 
    neutral_u = Voltage

    # >>> tap_changer.attributes

    # <<< tap_changer.references
    # @generated
    # 
    regulating_control = db.ReferenceProperty(RegulatingControl,
        collection_name="tap_changer")

    # A transformer winding may have tap changers, separately for voltage and phase angle 
    transformer_winding = db.ReferenceProperty(TransformerWinding,
        collection_name="tap_changers")

    # >>> tap_changer.references

    # <<< tap_changer.operations
    # @generated
    # >>> tap_changer.operations

# EOF -------------------------------------------------------------------------
