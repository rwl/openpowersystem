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

""" A winding is associated with each defined terminal of a transformer (or phase shifter). The association between the TransformerWinding class and MemberOf_EquipmentContainer is not used in this Profile since the association to Power Transformer is already there.  The only time this association should be used is if the association refers to a different substation than what is used in the PowerTransformer association. 
"""

# <<< imports
# @generated
from ucte.core.conducting_equipment import ConductingEquipment

from ucte.wires.power_transformer import PowerTransformer

from ucte.domain import Reactance
from ucte.domain import Susceptance
from ucte.wires import WindingConnection
from ucte.domain import ApparentPower
from ucte.domain import Resistance
from ucte.domain import Voltage
from ucte.domain import Conductance
from ucte.wires import WindingType

from google.appengine.ext import db
# >>> imports

class TransformerWinding(ConductingEquipment):
    """ A winding is associated with each defined terminal of a transformer (or phase shifter). The association between the TransformerWinding class and MemberOf_EquipmentContainer is not used in this Profile since the association to Power Transformer is already there.  The only time this association should be used is if the association refers to a different substation than what is used in the PowerTransformer association. 
    """
    # <<< transformer_winding.attributes
    # @generated
    # Positive sequence series reactance of the winding. 
    x = Reactance

    # Magnetizing branch susceptance (B mag). 
    b = Susceptance

    # The type of connection of the winding. 
    connection_type = WindingConnection

    # The normal apparent power rating for the winding 
    rated_s = ApparentPower

    # Zero sequence series reactance of the winding. This is for Short Circuit only. 
    x0 = Reactance

    # Positive sequence series resistance of the winding. 
    r = Resistance

    # Zero sequence series resistance of the winding. This is for Short Circuit only. 
    r0 = Resistance

    # Zero sequence magnetizing branch susceptance. This is for Short Circuit only. 
    b0 = Susceptance

    # The rated voltage (phase-to-phase) of the winding, usually the same as the neutral voltage. 
    rated_u = Voltage

    # Zero sequence magnetizing branch conductance. This is for Short Circuit only. 
    g0 = Conductance

    # Magnetizing branch conductance (G mag). 
    g = Conductance

    # Ground reactance path through connected grounding transformer. This is for Short Circuit only. 
    xground = Reactance

    # The type of winding. 
    winding_type = WindingType

    # Ground resistance path through connected grounding transformer. This is for Short Circuit only. 
    rground = Resistance

    # >>> transformer_winding.attributes

    # <<< transformer_winding.references
    # A transformer has windings
    member_of_power_transformer = db.ReferenceProperty(PowerTransformer, collection_name="contains_transformer_windings")

    # The ratio tap changer associated with the transformer winding.
    ratio_tap_changer = db.ReferenceProperty(db.Model, collection_name="_transformer_winding_set")

    # The phase tap changer associated with the transformer winding.
    phase_tap_changer = db.ReferenceProperty(db.Model, collection_name="_transformer_windings")

    # >>> transformer_winding.references

    # <<< transformer_winding.operations
    # @generated
    # >>> transformer_winding.operations

# EOF -------------------------------------------------------------------------
