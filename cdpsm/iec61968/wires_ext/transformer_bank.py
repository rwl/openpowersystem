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

""" An assembly of transformers that are connected together. For three-phase transformers, there would be one transformer per bank. For banks of single-phase transformers, there will be more than one transformer per bank, and they need not be identical. 
"""

# <<< imports
# @generated
from cdpsm.iec61970.core.equipment import Equipment



from google.appengine.ext import db
# >>> imports

class TransformerBank(Equipment):
    """ An assembly of transformers that are connected together. For three-phase transformers, there would be one transformer per bank. For banks of single-phase transformers, there will be more than one transformer per bank, and they need not be identical. 
    """
    # <<< transformer_bank.attributes
    # @generated
    # Vector group of the bank for protective relaying, e.g., Dyn1. For unbalanced transformers, this may not be simply determined from the constituent winding connections. 
    vector_group = db.StringProperty()

    # >>> transformer_bank.attributes

    # <<< transformer_bank.references
    # @generated
    # Virtual property. All transformers that belong to this bank. 
    pass # transformers

    # >>> transformer_bank.references

    # <<< transformer_bank.operations
    # @generated
    # >>> transformer_bank.operations

# EOF -------------------------------------------------------------------------
