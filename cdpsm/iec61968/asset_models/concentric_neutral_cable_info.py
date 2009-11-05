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

""" Concentric neutral cable data. 
"""

# <<< imports
# @generated
from cdpsm.iec61968.asset_models.cable_info import CableInfo

from cdpsm.iec61968.asset_models.wire_type import WireType

from cdpsm.iec61970.domain import Length

from google.appengine.ext import db
# >>> imports

class ConcentricNeutralCableInfo(CableInfo):
    """ Concentric neutral cable data. 
    """
    # <<< concentric_neutral_cable_info.attributes
    # @generated
    # Number of concentric neutral strands. 
    neutral_strand_count = db.IntegerProperty()

    # Diameter over the concentric neutral strands. 
    diameter_over_neutral = Length

    # >>> concentric_neutral_cable_info.attributes

    # <<< concentric_neutral_cable_info.references
    # @generated
    # Wire type used for this concentric neutral cable. 
    wire_type = db.ReferenceProperty(WireType,
        collection_name="concentric_neutral_cable_infos")

    # >>> concentric_neutral_cable_info.references

    # <<< concentric_neutral_cable_info.operations
    # @generated
    # >>> concentric_neutral_cable_info.operations

# EOF -------------------------------------------------------------------------
