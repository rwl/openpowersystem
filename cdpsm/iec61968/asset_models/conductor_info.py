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

""" Conductor data. 
"""

# <<< imports
# @generated
from cdpsm.iec61970.core.identified_object import IdentifiedObject


from cdpsm.iec61968.asset_models import ConductorInsulationKind
from cdpsm.iec61970.domain import Length
from cdpsm.iec61968.asset_models import ConductorUsageKind

from google.appengine.ext import db
# >>> imports

class ConductorInfo(IdentifiedObject):
    """ Conductor data. 
    """
    # <<< conductor_info.attributes
    # @generated
    # Number of phases (including neutral) to be retained. Any wires beyond this number should be reduced into the earth return. 
    phase_count = db.IntegerProperty()

    # (if insulated conductor) Material used for insulation. 
    insulation_material = ConductorInsulationKind

    # (if insulated conductor) Thickness of the insulation. 
    insulation_thickness = Length

    # True if conductor is insulated. 
    insulated = db.BooleanProperty()

    # Usage of this conductor. 
    usage = ConductorUsageKind

    # >>> conductor_info.attributes

    # <<< conductor_info.references
    # @generated
    # Virtual property. All wire arrangements (single wires) that make this conductor. 
    pass # wire_arrangements

    # Virtual property. All conductor segments described by this conductor data. 
    pass # conductor_segments

    # >>> conductor_info.references

    # <<< conductor_info.operations
    # @generated
    # >>> conductor_info.operations

# EOF -------------------------------------------------------------------------
