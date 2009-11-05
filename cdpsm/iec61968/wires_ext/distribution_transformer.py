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

""" An assembly of two or more coupled windings that transform electrical power between voltage levels. Supports both balanced and unbalanced winding connections. This class differs from Wires::PowerTransformer as follows: - it is part of a TransformerBank - it draws parameters exclusively from TransformerInfo and its associated classes. 
"""

# <<< imports
# @generated
from cdpsm.iec61970.core.equipment import Equipment

from cdpsm.iec61968.asset_models.transformer_info import TransformerInfo
from cdpsm.iec61968.wires_ext.transformer_bank import TransformerBank


from google.appengine.ext import db
# >>> imports

class DistributionTransformer(Equipment):
    """ An assembly of two or more coupled windings that transform electrical power between voltage levels. Supports both balanced and unbalanced winding connections. This class differs from Wires::PowerTransformer as follows: - it is part of a TransformerBank - it draws parameters exclusively from TransformerInfo and its associated classes. 
    """
    # <<< distribution_transformer.attributes
    # @generated
    # >>> distribution_transformer.attributes

    # <<< distribution_transformer.references
    # @generated
    # Transformer data. 
    transformer_info = db.ReferenceProperty(TransformerInfo,
        collection_name="transformers")

    # Virtual property. All windings of this transformer. 
    pass # windings

    # Bank this transformer belongs to. 
    transformer_bank = db.ReferenceProperty(TransformerBank,
        collection_name="transformers")

    # >>> distribution_transformer.references

    # <<< distribution_transformer.operations
    # @generated
    # >>> distribution_transformer.operations

# EOF -------------------------------------------------------------------------
