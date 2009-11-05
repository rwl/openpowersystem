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

""" Identification, spacing and configuration of the wires of a Conductor, with reference to their type. 
"""

# <<< imports
# @generated
from cdpsm.iec61970.core.identified_object import IdentifiedObject

from cdpsm.iec61968.asset_models.conductor_info import ConductorInfo
from cdpsm.iec61968.asset_models.wire_type import WireType

from cdpsm.iec61970.domain import Length

from google.appengine.ext import db
# >>> imports

class WireArrangement(IdentifiedObject):
    """ Identification, spacing and configuration of the wires of a Conductor, with reference to their type. 
    """
    # <<< wire_arrangement.attributes
    # @generated
    # Signed horizontal distance from the first wire to a common reference point. 
    mounting_point_x = Length

    # Height above ground of the first wire. 
    mounting_point_y = Length

    # Position number on the structure corresponding to this wire. For example, use 1..3 for phases and 4 for the neutral on a 3-phase structure. The individual phase assignments matter; for example, ABC will produce a different set of unbalanced line parameters, by phase, than BAC. 
    position = db.IntegerProperty()

    # >>> wire_arrangement.attributes

    # <<< wire_arrangement.references
    # @generated
    # Conductor data this wire arrangement belongs to. 
    conductor_info = db.ReferenceProperty(ConductorInfo,
        collection_name="wire_arrangements")

    # Wire type used for this wire arrangement. 
    wire_type = db.ReferenceProperty(WireType,
        collection_name="wire_arrangements")

    # >>> wire_arrangement.references

    # <<< wire_arrangement.operations
    # @generated
    # >>> wire_arrangement.operations

# EOF -------------------------------------------------------------------------
