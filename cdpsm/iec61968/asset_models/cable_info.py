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

""" Cable data. 
"""

# <<< imports
# @generated
from cdpsm.iec61968.asset_models.conductor_info import ConductorInfo


from cdpsm.iec61970.domain import Temperature
from cdpsm.iec61970.domain import Length
from cdpsm.iec61968.asset_models import CableConstructionKind
from cdpsm.iec61968.asset_models import CableOuterJacketKind
from cdpsm.iec61968.asset_models import CableShieldMaterialKind

from google.appengine.ext import db
# >>> imports

class CableInfo(ConductorInfo):
    """ Cable data. 
    """
    # <<< cable_info.attributes
    # @generated
    # Maximum nominal design operating temperature. 
    nominal_temperature = Temperature

    # Diameter over the outer screen; should be the shield's inside diameter.. 
    diameter_over_screen = Length

    # True if sheath / shield is used as a neutral (i.e., bonded). 
    sheath_as_neutral = db.BooleanProperty()

    # Diameter over the outermost jacketing layer. 
    diameter_over_jacket = Length

    # Diameter over the core, including any semi-con screen; should be the insulating layer's inside diameter. 
    diameter_over_core = Length

    # Kind of construction of this cable. 
    construction_kind = CableConstructionKind

    # Kind of outer jacket of this cable. 
    outer_jacket_kind = CableOuterJacketKind

    # True if wire strands are extruded in a way to fill the voids in the cable. 
    is_strand_fill = db.BooleanProperty()

    # Material of the shield. 
    shield_material = CableShieldMaterialKind

    # Diameter over the insulating layer, excluding outer screen. 
    diameter_over_insulation = Length

    # >>> cable_info.attributes

    # <<< cable_info.references
    # @generated
    # >>> cable_info.references

    # <<< cable_info.operations
    # @generated
    # >>> cable_info.operations

# EOF -------------------------------------------------------------------------
