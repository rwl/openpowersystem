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

""" Winding data. 
"""

# <<< imports
# @generated
from cdpsm.iec61970.core.identified_object import IdentifiedObject

from cdpsm.iec61968.asset_models.transformer_info import TransformerInfo

from cdpsm.iec61970.domain import ApparentPower
from cdpsm.iec61970.domain import Voltage
from cdpsm.iec61970.wires import WindingConnection
from cdpsm.iec61970.domain import Resistance

from google.appengine.ext import db
# >>> imports

class WindingInfo(IdentifiedObject):
    """ Winding data. 
    """
    # <<< winding_info.attributes
    # @generated
    # Sequence number for this winding, corresponding to the winding's order in the TransformerBank.vectorGroup attribute. Highest voltage winding should be '1'. 
    sequence_number = db.IntegerProperty()

    # Normal apparent power rating of this winding. 
    rated_s = ApparentPower

    # Rated voltage of this winding: phase-phase for three-phase windings, and either phase-phase or phase-neutral for single-phase windings. 
    rated_u = Voltage

    # Kind of connection of this winding. 
    connection_kind = WindingConnection

    # Apparent power that the winding can carry under emergency conditions. 
    emergency_s = ApparentPower

    # DC resistance of this winding. 
    r = Resistance

    # Winding phase angle where 360 degrees are represented with clock hours, so the valid values are {0, ..., 11}. For example, to express winding code 'Dyn11', set attributes as follows: 'connectionKind' = Yn and 'phaseAngle' = 11. 
    phase_angle = db.IntegerProperty()

    # Basic insulation level voltage rating. 
    insulation_u = Voltage

    # Apparent power that this winding can carry for a short period of time. 
    short_term_s = ApparentPower

    # >>> winding_info.attributes

    # <<< winding_info.references
    # @generated
    # Virtual property. All winding tests during which voltage or current was applied to this winding. 
    pass # winding_tests

    # Virtual property. Tap steps and induced voltage/angle measurements for tests in which this winding was not excited. 
    pass # to_winding_specs

    # Transformer data that this winding description is part of. 
    transformer_info = db.ReferenceProperty(TransformerInfo,
        collection_name="winding_infos")

    # Virtual property. All windings described by this winding data. 
    pass # windings

    # >>> winding_info.references

    # <<< winding_info.operations
    # @generated
    # >>> winding_info.operations

# EOF -------------------------------------------------------------------------
