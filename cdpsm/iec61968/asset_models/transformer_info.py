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

""" Set of transformer data, from an equipment library. 
"""

# <<< imports
# @generated
from cdpsm.iec61970.core.identified_object import IdentifiedObject



from google.appengine.ext import db
# >>> imports

class TransformerInfo(IdentifiedObject):
    """ Set of transformer data, from an equipment library. 
    """
    # <<< transformer_info.attributes
    # @generated
    # >>> transformer_info.attributes

    # <<< transformer_info.references
    # @generated
    # Virtual property. All transformers that can be described with this transformer data. 
    pass # transformers

    # Virtual property. Data for all the windings described by this transformer data. 
    pass # winding_infos

    # >>> transformer_info.references

    # <<< transformer_info.operations
    # @generated
    # >>> transformer_info.operations

# EOF -------------------------------------------------------------------------
