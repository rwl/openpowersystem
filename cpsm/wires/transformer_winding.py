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

""" A winding is associated with each defined terminal of a transformer (or phase shifter). 
"""

# <<< imports
# @generated
from cpsm.core.conducting_equipment import ConductingEquipment

from cpsm.wires.power_transformer import PowerTransformer

from cpsm.wires import WindingType
from cpsm.domain import ApparentPower
from cpsm.domain import Reactance
from cpsm.domain import Voltage
from cpsm.domain import Resistance
from cpsm.domain import Susceptance

from google.appengine.ext import db
# >>> imports

class TransformerWinding(ConductingEquipment):
    """ A winding is associated with each defined terminal of a transformer (or phase shifter). 
    """
    # <<< transformer_winding.attributes
    # @generated
    # The type of winding. 
    winding_type = WindingType

    # The normal apparent power rating for the winding 
    rated_s = ApparentPower

    # Positive sequence series reactance of the winding. 
    x = Reactance

    # The rated voltage (phase-to-phase) of the winding, usually the same as the neutral voltage. 
    rated_u = Voltage

    # Positive sequence series resistance of the winding. 
    r = Resistance

    # Magnetizing branch susceptance (B mag). 
    b = Susceptance

    # >>> transformer_winding.attributes

    # <<< transformer_winding.references
    # @generated
    # Virtual property. A transformer winding may have tap changers, separately for voltage and phase angle.  If a TransformerWinding does not have an associated TapChanger, the winding is assumed to be fixed tap.  
    pass # tap_changers

    # A transformer has windings 
    member_of_power_transformer = db.ReferenceProperty(PowerTransformer,
        collection_name="contains_transformer_windings")

    # >>> transformer_winding.references

    # <<< transformer_winding.operations
    # @generated
    # >>> transformer_winding.operations

# EOF -------------------------------------------------------------------------
