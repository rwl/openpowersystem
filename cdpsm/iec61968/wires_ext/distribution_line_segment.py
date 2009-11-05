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

""" Extends ACLineSegment with references to a library of standard types from which electrical parameters can be calculated, as follows: - calculate electrical parameters from asset data, using associated ConductorInfo, with values then multiplied by Conductor.length to produce a matrix model. - calculate unbalanced electrical parameters from associated PerLengthPhaseImpedance, then multiplied by Conductor.length to produce a matrix model. - calculate transposed electrical parameters from associated PerLengthSequenceImpedance, then multiplied by Conductor.length to produce a sequence model. For symmetrical, transposed 3ph lines, it is sufficient to use inherited ACLineSegment attributes, which describe sequence impedances and admittances for the entire length of the segment.  Known issue: Attributes expressing impedances and admittances in PerLengthSequenceImpedance and PhaseImpedanceData use Resistance, etc., which describe pre-calculated, full length of segment, while we should have a longitudinal unit, per length. Taking 'r' as example, its 'unit'=Ohm, but the value is effectively in Ohm/m, so the value needs to be multiplied by Conductor.length. This is against the whole idea of unit data types and is semantically wrong, but base CIM does not have the required data types at this moment. Until the revision of unit modelling in CIM, applications need to deduce and locally handle appending '/m' for units and ensure they multiply the values by Conductor.length. At least one of the Associations must exist. 
"""

# <<< imports
# @generated
from cdpsm.iec61970.wires.acline_segment import ACLineSegment

from cdpsm.iec61968.asset_models.conductor_info import ConductorInfo
from cdpsm.iec61968.wires_ext.per_length_sequence_impedance import PerLengthSequenceImpedance
from cdpsm.iec61968.wires_ext.per_length_phase_impedance import PerLengthPhaseImpedance


from google.appengine.ext import db
# >>> imports

class DistributionLineSegment(ACLineSegment):
    """ Extends ACLineSegment with references to a library of standard types from which electrical parameters can be calculated, as follows: - calculate electrical parameters from asset data, using associated ConductorInfo, with values then multiplied by Conductor.length to produce a matrix model. - calculate unbalanced electrical parameters from associated PerLengthPhaseImpedance, then multiplied by Conductor.length to produce a matrix model. - calculate transposed electrical parameters from associated PerLengthSequenceImpedance, then multiplied by Conductor.length to produce a sequence model. For symmetrical, transposed 3ph lines, it is sufficient to use inherited ACLineSegment attributes, which describe sequence impedances and admittances for the entire length of the segment.  Known issue: Attributes expressing impedances and admittances in PerLengthSequenceImpedance and PhaseImpedanceData use Resistance, etc., which describe pre-calculated, full length of segment, while we should have a longitudinal unit, per length. Taking 'r' as example, its 'unit'=Ohm, but the value is effectively in Ohm/m, so the value needs to be multiplied by Conductor.length. This is against the whole idea of unit data types and is semantically wrong, but base CIM does not have the required data types at this moment. Until the revision of unit modelling in CIM, applications need to deduce and locally handle appending '/m' for units and ensure they multiply the values by Conductor.length. At least one of the Associations must exist. 
    """
    # <<< distribution_line_segment.attributes
    # @generated
    # >>> distribution_line_segment.attributes

    # <<< distribution_line_segment.references
    # @generated
    # Conductor data of this conductor segment. 
    conductor_info = db.ReferenceProperty(ConductorInfo,
        collection_name="conductor_segments")

    # Sequence impedance of this conductor segment; used for balanced model. 
    sequence_impedance = db.ReferenceProperty(PerLengthSequenceImpedance,
        collection_name="conductor_segments")

    # Phase impedance of this conductor segment; used for unbalanced model. 
    phase_impedance = db.ReferenceProperty(PerLengthPhaseImpedance,
        collection_name="conductor_segments")

    # >>> distribution_line_segment.references

    # <<< distribution_line_segment.operations
    # @generated
    # >>> distribution_line_segment.operations

# EOF -------------------------------------------------------------------------
