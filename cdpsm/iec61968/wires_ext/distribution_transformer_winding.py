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

""" Conducting connection point of a distribution / unbalanced transformer winding instance. This class differs from Wires::TransformerWinding as follows: - the eight Pi model attributes are moved into separate class, that can be optionally referred to from several winding instances. - the three grounding attributes can differ per winding instance, even for windings that use the same TransformerInfo, so they are kept on DistributionTransformerWinding. 'sequenceNumber' attribute replaces 'windingType' attribute.  All the other attributes come from the WindingInfo (and its relationships). TransformerInfo is associated to the DistributionTransformer as referenceable data, so it can be defined once and referred to from instances, instead of being specified with each instance. 
"""

# <<< imports
# @generated
from cdpsm.iec61970.core.conducting_equipment import ConductingEquipment

from cdpsm.iec61968.asset_models.winding_info import WindingInfo
from cdpsm.iec61968.wires_ext.distribution_transformer import DistributionTransformer
from cdpsm.iec61968.wires_ext.winding_pi_impedance import WindingPiImpedance

from cdpsm.iec61970.domain import Resistance
from cdpsm.iec61970.domain import Reactance

from google.appengine.ext import db
# >>> imports

class DistributionTransformerWinding(ConductingEquipment):
    """ Conducting connection point of a distribution / unbalanced transformer winding instance. This class differs from Wires::TransformerWinding as follows: - the eight Pi model attributes are moved into separate class, that can be optionally referred to from several winding instances. - the three grounding attributes can differ per winding instance, even for windings that use the same TransformerInfo, so they are kept on DistributionTransformerWinding. 'sequenceNumber' attribute replaces 'windingType' attribute.  All the other attributes come from the WindingInfo (and its relationships). TransformerInfo is associated to the DistributionTransformer as referenceable data, so it can be defined once and referred to from instances, instead of being specified with each instance. 
    """
    # <<< distribution_transformer_winding.attributes
    # @generated
    # (for Yn and Zn connections) Resistance part of neutral impedance where 'grounded' is true. 
    rground = Resistance

    # (for Yn and Zn connections) Reactive part of neutral impedance where 'grounded' is true. 
    xground = Reactance

    # (for Yn and Zn connections) True if the neutral is solidly grounded. 
    grounded = db.BooleanProperty()

    # >>> distribution_transformer_winding.attributes

    # <<< distribution_transformer_winding.references
    # @generated
    # Data for this winding. 
    winding_info = db.ReferenceProperty(WindingInfo,
        collection_name="windings")

    # Transformer this winding belongs to. 
    transformer = db.ReferenceProperty(DistributionTransformer,
        collection_name="windings")

    # Ratio tap changer associated with this winding. 
    ratio_tap_changer = db.ReferenceProperty(db.Model,
        collection_name="_distribution_transformer_winding_set") # winding

    # (accurate for 2- or 3-winding transformers only) Pi-model impedances of this winding. 
    pi_impedance = db.ReferenceProperty(WindingPiImpedance,
        collection_name="windings")

    # >>> distribution_transformer_winding.references

    # <<< distribution_transformer_winding.operations
    # @generated
    # >>> distribution_transformer_winding.operations

# EOF -------------------------------------------------------------------------
