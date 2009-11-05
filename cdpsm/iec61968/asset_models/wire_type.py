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

""" Wire conductor (per IEEE specs). A specific type of wire or combination of wires, not insulated from each other, suitable for carrying electrical current. 
"""

# <<< imports
# @generated
from cdpsm.iec61970.core.identified_object import IdentifiedObject


from cdpsm.iec61970.domain import Resistance
from cdpsm.iec61970.domain import Length
from cdpsm.iec61968.asset_models import ConductorMaterialKind
from cdpsm.iec61970.domain import CurrentFlow

from google.appengine.ext import db
# >>> imports

class WireType(IdentifiedObject):
    """ Wire conductor (per IEEE specs). A specific type of wire or combination of wires, not insulated from each other, suitable for carrying electrical current. 
    """
    # <<< wire_type.attributes
    # @generated
    # AC resistance per unit length of the conductor at 75 degrees C. 
    r_ac75 = Resistance

    # (if there is a different core material) Radius of the central core. 
    core_radius = Length

    # (if used) Number of strands in the steel core. 
    core_strand_count = db.IntegerProperty()

    # AC resistance per unit length of the conductor at 25 degrees C. 
    r_ac25 = Resistance

    # Outside radius of the wire. 
    radius = Length

    # Geometric Mean Radius. If we replace the conductor by a thin walled tube of radius GMR, then its reactance is identical to the reactance of the actual conductor. 
    gmr = Length

    # DC resistance per unit length of the conductor at 20 degrees C. 
    r_dc20 = Resistance

    # AC resistance per unit length of the conductor at 50 degrees C. 
    r_ac50 = Resistance

    # Wire material. 
    material = ConductorMaterialKind

    # Describes the wire guage or cross section (e.g., 4/0, #2, 336.5). 
    size_description = db.StringProperty()

    # Number of strands in the wire. 
    strand_count = db.IntegerProperty()

    # Current carrying capacity of the wire under stated thermal conditions. 
    rated_current = CurrentFlow

    # >>> wire_type.attributes

    # <<< wire_type.references
    # @generated
    # Virtual property. All concentric neutral cables using this wire type. 
    pass # concentric_neutral_cable_infos

    # Virtual property. All wire arrangements using this wire type. 
    pass # wire_arrangements

    # >>> wire_type.references

    # <<< wire_type.operations
    # @generated
    # >>> wire_type.operations

# EOF -------------------------------------------------------------------------
