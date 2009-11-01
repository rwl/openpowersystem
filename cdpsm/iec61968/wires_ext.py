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

""" Contains only diagrams to be discussed with WG13, for consolidating T&amp;D models.Contains only diagrams to be discussed with WG13, for consolidating T&amp;D models.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from cdpsm.iec61970.core import ConductingEquipment
from cdpsm.iec61970.wires import ACLineSegment
from cdpsm.iec61970.core import IdentifiedObject
from cdpsm.iec61970.wires import RatioTapChanger
from cdpsm.iec61970.core import Equipment
from cdpsm import Element

from cdpsm.iec61970.domain import Resistance
from cdpsm.iec61970.domain import Reactance
from cdpsm.iec61970.domain import Conductance
from cdpsm.iec61970.domain import Susceptance
from cdpsm.iec61970.core import PhaseCode
from cdpsm.iec61970.domain import Voltage

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

#------------------------------------------------------------------------------
#  Properties:
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  Constants:
#------------------------------------------------------------------------------

NS_PREFIX = "cim"
NS_URI = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_WiresExt"

#------------------------------------------------------------------------------
#  "DistributionTransformerWinding" class:
#------------------------------------------------------------------------------

class DistributionTransformerWinding(ConductingEquipment):
    """ Conducting connection point of a distribution / unbalanced transformer winding instance. This class differs from Wires::TransformerWinding as follows: - the eight Pi model attributes are moved into separate class, that can be optionally referred to from several winding instances. - the three grounding attributes can differ per winding instance, even for windings that use the same TransformerInfo, so they are kept on DistributionTransformerWinding. 'sequenceNumber' attribute replaces 'windingType' attribute.  All the other attributes come from the WindingInfo (and its relationships). TransformerInfo is associated to the DistributionTransformer as referenceable data, so it can be defined once and referred to from instances, instead of being specified with each instance.Conducting connection point of a distribution / unbalanced transformer winding instance. This class differs from Wires::TransformerWinding as follows: - the eight Pi model attributes are moved into separate class, that can be optionally referred to from several winding instances. - the three grounding attributes can differ per winding instance, even for windings that use the same TransformerInfo, so they are kept on DistributionTransformerWinding. 'sequenceNumber' attribute replaces 'windingType' attribute.  All the other attributes come from the WindingInfo (and its relationships). TransformerInfo is associated to the DistributionTransformer as referenceable data, so it can be defined once and referred to from instances, instead of being specified with each instance.
    """

    
    # (for Yn and Zn connections) Resistance part of neutral impedance where 'grounded' is true.(for Yn and Zn connections) Resistance part of neutral impedance where 'grounded' is true.
    rground = Resistance

    # (for Yn and Zn connections) Reactive part of neutral impedance where 'grounded' is true.(for Yn and Zn connections) Reactive part of neutral impedance where 'grounded' is true.
    xground = Reactance

    # (for Yn and Zn connections) True if the neutral is solidly grounded.(for Yn and Zn connections) True if the neutral is solidly grounded.
    grounded = db.BooleanProperty()

    # Data for this winding.Data for this winding.
    winding_info = db.ReferenceProperty(collection_name="windings")

    # Transformer this winding belongs to.Transformer this winding belongs to.
    transformer = db.ReferenceProperty(collection_name="windings")

    # Ratio tap changer associated with this winding.Ratio tap changer associated with this winding.
    ratio_tap_changer = db.ReferenceProperty()

    # (accurate for 2- or 3-winding transformers only) Pi-model impedances of this winding.(accurate for 2- or 3-winding transformers only) Pi-model impedances of this winding.
    pi_impedance = db.ReferenceProperty(collection_name="windings")

    # <<< distribution_transformer_winding
    # @generated
    # >>> distribution_transformer_winding


#------------------------------------------------------------------------------
#  "DistributionLineSegment" class:
#------------------------------------------------------------------------------

class DistributionLineSegment(ACLineSegment):
    """ Extends ACLineSegment with references to a library of standard types from which electrical parameters can be calculated, as follows: - calculate electrical parameters from asset data, using associated ConductorInfo, with values then multiplied by Conductor.length to produce a matrix model. - calculate unbalanced electrical parameters from associated PerLengthPhaseImpedance, then multiplied by Conductor.length to produce a matrix model. - calculate transposed electrical parameters from associated PerLengthSequenceImpedance, then multiplied by Conductor.length to produce a sequence model. For symmetrical, transposed 3ph lines, it is sufficient to use inherited ACLineSegment attributes, which describe sequence impedances and admittances for the entire length of the segment.  Known issue: Attributes expressing impedances and admittances in PerLengthSequenceImpedance and PhaseImpedanceData use Resistance, etc., which describe pre-calculated, full length of segment, while we should have a longitudinal unit, per length. Taking 'r' as example, its 'unit'=Ohm, but the value is effectively in Ohm/m, so the value needs to be multiplied by Conductor.length. This is against the whole idea of unit data types and is semantically wrong, but base CIM does not have the required data types at this moment. Until the revision of unit modelling in CIM, applications need to deduce and locally handle appending '/m' for units and ensure they multiply the values by Conductor.length.At least one of the Associations must exist.Extends ACLineSegment with references to a library of standard types from which electrical parameters can be calculated, as follows: - calculate electrical parameters from asset data, using associated ConductorInfo, with values then multiplied by Conductor.length to produce a matrix model. - calculate unbalanced electrical parameters from associated PerLengthPhaseImpedance, then multiplied by Conductor.length to produce a matrix model. - calculate transposed electrical parameters from associated PerLengthSequenceImpedance, then multiplied by Conductor.length to produce a sequence model. For symmetrical, transposed 3ph lines, it is sufficient to use inherited ACLineSegment attributes, which describe sequence impedances and admittances for the entire length of the segment.  Known issue: Attributes expressing impedances and admittances in PerLengthSequenceImpedance and PhaseImpedanceData use Resistance, etc., which describe pre-calculated, full length of segment, while we should have a longitudinal unit, per length. Taking 'r' as example, its 'unit'=Ohm, but the value is effectively in Ohm/m, so the value needs to be multiplied by Conductor.length. This is against the whole idea of unit data types and is semantically wrong, but base CIM does not have the required data types at this moment. Until the revision of unit modelling in CIM, applications need to deduce and locally handle appending '/m' for units and ensure they multiply the values by Conductor.length.At least one of the Associations must exist.
    """

    
    # Conductor data of this conductor segment.Conductor data of this conductor segment.
    conductor_info = db.ReferenceProperty(collection_name="conductor_segments")

    # Sequence impedance of this conductor segment; used for balanced model.Sequence impedance of this conductor segment; used for balanced model.
    sequence_impedance = db.ReferenceProperty(collection_name="conductor_segments")

    # Phase impedance of this conductor segment; used for unbalanced model.Phase impedance of this conductor segment; used for unbalanced model.
    phase_impedance = db.ReferenceProperty(collection_name="conductor_segments")

    # <<< distribution_line_segment
    # @generated
    # >>> distribution_line_segment


#------------------------------------------------------------------------------
#  "WindingPiImpedance" class:
#------------------------------------------------------------------------------

class WindingPiImpedance(IdentifiedObject):
    """ Transformer Pi-model impedance that accurately reflects impedance for transformers with 2 or 3 windings. For transformers with 4 or more windings, you must use TransformerInfo.Transformer Pi-model impedance that accurately reflects impedance for transformers with 2 or 3 windings. For transformers with 4 or more windings, you must use TransformerInfo.
    """

    
    # Positive sequence series reactance of the winding.  For a two winding transformer, the full reactance of the transformer should be entered on the primary (high voltage) winding.Positive sequence series reactance of the winding.  For a two winding transformer, the full reactance of the transformer should be entered on the primary (high voltage) winding.
    x = Reactance

    # Magnetizing branch conductance (G mag).Magnetizing branch conductance (G mag).
    g = Conductance

    # Zero sequence series resistance of the winding.Zero sequence series resistance of the winding.
    r0 = Resistance

    # DC resistance of the winding.DC resistance of the winding.
    r = Resistance

    # Magnetizing branch susceptance (B mag).  The value can be positive or negative.Magnetizing branch susceptance (B mag).  The value can be positive or negative.
    b = Susceptance

    # Zero sequence magnetizing branch conductance.Zero sequence magnetizing branch conductance.
    g0 = Conductance

    # Zero sequence series reactance of the winding.Zero sequence series reactance of the winding.
    x0 = Reactance

    # Zero sequence magnetizing branch susceptance.Zero sequence magnetizing branch susceptance.
    b0 = Susceptance

    # Virtual property. All windings having this Pi impedance.All windings having this Pi impedance.
    pass #windings

    # <<< winding_pi_impedance
    # @generated
    # >>> winding_pi_impedance


#------------------------------------------------------------------------------
#  "DistributionTapChanger" class:
#------------------------------------------------------------------------------

class DistributionTapChanger(RatioTapChanger):
    """ Additional ratio tap changer parameters common to distribution line regulators. 'tculControlMode' would always be 'volt'. If 'monitoredPhase' is not specified, then if the controlled DistributionTransformerWinding is single-phase, the PT primary is assumed to be connected across that winding, which is the normal case. If the controlled winding is three-phase, then the 'monitoredPhase' is assumed to be 'AN', unless otherwise specified. Whenever 'ctRatio' and 'ptRatio' are specified, it's customary to specify the R and X in 'volts' referred to the PT secondary circuit, otherwise R and X are in feeder primary ohms. If 'ptRatio' is not specified, then 'targetVoltage', 'limitVoltage', and 'bandVoltage' are on the feeder primary base, phase-neutral or phase-phase depending on the 'monitoredPhase'. Otherwise, these attributes are all on the PT secondary base.Additional ratio tap changer parameters common to distribution line regulators. 'tculControlMode' would always be 'volt'. If 'monitoredPhase' is not specified, then if the controlled DistributionTransformerWinding is single-phase, the PT primary is assumed to be connected across that winding, which is the normal case. If the controlled winding is three-phase, then the 'monitoredPhase' is assumed to be 'AN', unless otherwise specified. Whenever 'ctRatio' and 'ptRatio' are specified, it's customary to specify the R and X in 'volts' referred to the PT secondary circuit, otherwise R and X are in feeder primary ohms. If 'ptRatio' is not specified, then 'targetVoltage', 'limitVoltage', and 'bandVoltage' are on the feeder primary base, phase-neutral or phase-phase depending on the 'monitoredPhase'. Otherwise, these attributes are all on the PT secondary base.
    """

    
    # Line drop compensator resistance setting for normal (forward) power flow.Line drop compensator resistance setting for normal (forward) power flow.
    line_drop_r = Resistance

    # Phase voltage controlling this regulator, measured at regulator location.Phase voltage controlling this regulator, measured at regulator location.
    monitored_phase = PhaseCode

    # If true, the line drop compensation is to be applied.If true, the line drop compensation is to be applied.
    line_drop_compensation = db.BooleanProperty()

    # Built-in voltage transducer ratio.Built-in voltage transducer ratio.
    pt_ratio = db.FloatProperty()

    # Built-in current transducer ratio.Built-in current transducer ratio.
    ct_ratio = db.FloatProperty()

    # Line drop compensator resistance setting for reverse power flow.Line drop compensator resistance setting for reverse power flow.
    reverse_line_drop_r = Resistance

    # Maximum allowed regulated voltage on the PT secondary base, regardless of line drop compensation. Sometimes referred to as first-house protection.Maximum allowed regulated voltage on the PT secondary base, regardless of line drop compensation. Sometimes referred to as first-house protection.
    limit_voltage = Voltage

    # Line drop compensator reactance setting for reverse power flow.Line drop compensator reactance setting for reverse power flow.
    reverse_line_drop_x = Reactance

    # Voltage range (max - min) on the PT secondary base, centered on 'targetVoltage'.Voltage range (max - min) on the PT secondary base, centered on 'targetVoltage'.
    band_voltage = Voltage

    # Target voltage on the PT secondary base.Target voltage on the PT secondary base.
    target_voltage = Voltage

    # Line drop compensator reactance setting for normal (forward) power flow.Line drop compensator reactance setting for normal (forward) power flow.
    line_drop_x = Reactance

    # <<< distribution_tap_changer
    # @generated
    # >>> distribution_tap_changer


#------------------------------------------------------------------------------
#  "PerLengthSequenceImpedance" class:
#------------------------------------------------------------------------------

class PerLengthSequenceImpedance(IdentifiedObject):
    """ Sequence impedance and admittance parameters per unit length, for transposed lines of 1, 2, or 3 phases. For 1-phase lines, define x=x0=xself. For 2-phase lines, define x=xs-xm and x0=xs+xm.Sequence impedance and admittance parameters per unit length, for transposed lines of 1, 2, or 3 phases. For 1-phase lines, define x=x0=xself. For 2-phase lines, define x=xs-xm and x0=xs+xm.
    """

    
    # Positive sequence series reactance, per unit of length.Positive sequence series reactance, per unit of length.
    x = Reactance

    # Positive sequence shunt (charging) conductance, per unit of length.Positive sequence shunt (charging) conductance, per unit of length.
    gch = Conductance

    # Zero sequence series resistance, per unit of length.Zero sequence series resistance, per unit of length.
    r0 = Resistance

    # Zero sequence series reactance, per unit of length.Zero sequence series reactance, per unit of length.
    x0 = Reactance

    # Zero sequence shunt (charging) conductance, per unit of length.Zero sequence shunt (charging) conductance, per unit of length.
    g0ch = Conductance

    # Zero sequence shunt (charging) susceptance, per unit of length.Zero sequence shunt (charging) susceptance, per unit of length.
    b0ch = Susceptance

    # Positive sequence series resistance, per unit of length.Positive sequence series resistance, per unit of length.
    r = Resistance

    # Positive sequence shunt (charging) susceptance, per unit of length.Positive sequence shunt (charging) susceptance, per unit of length.
    bch = Susceptance

    # Virtual property. All conductor segments described by this sequence impedance.All conductor segments described by this sequence impedance.
    pass #conductor_segments

    # <<< per_length_sequence_impedance
    # @generated
    # >>> per_length_sequence_impedance


#------------------------------------------------------------------------------
#  "TransformerBank" class:
#------------------------------------------------------------------------------

class TransformerBank(Equipment):
    """ An assembly of transformers that are connected together. For three-phase transformers, there would be one transformer per bank. For banks of single-phase transformers, there will be more than one transformer per bank, and they need not be identical.An assembly of transformers that are connected together. For three-phase transformers, there would be one transformer per bank. For banks of single-phase transformers, there will be more than one transformer per bank, and they need not be identical.
    """

    
    # Vector group of the bank for protective relaying, e.g., Dyn1. For unbalanced transformers, this may not be simply determined from the constituent winding connections.Vector group of the bank for protective relaying, e.g., Dyn1. For unbalanced transformers, this may not be simply determined from the constituent winding connections.
    vector_group = db.StringProperty()

    # Virtual property. All transformers that belong to this bank.All transformers that belong to this bank.
    pass #transformers

    # <<< transformer_bank
    # @generated
    # >>> transformer_bank


#------------------------------------------------------------------------------
#  "PerLengthPhaseImpedance" class:
#------------------------------------------------------------------------------

class PerLengthPhaseImpedance(IdentifiedObject):
    """ Impedance and admittance parameters per unit length for n-wire unbalanced lines, in matrix form.Impedance and admittance parameters per unit length for n-wire unbalanced lines, in matrix form.
    """

    
    # Number of phase, neutral, and other wires retained. Constrains the number of matrix elements and the phase codes that can be used with this matrix.Number of phase, neutral, and other wires retained. Constrains the number of matrix elements and the phase codes that can be used with this matrix.
    conductor_count = db.IntegerProperty()

    # Virtual property. All data that belong to this conductor phase impedance.All data that belong to this conductor phase impedance.
    pass #phase_impedance_data

    # Virtual property. All conductor segments described by this phase impedance.All conductor segments described by this phase impedance.
    pass #conductor_segments

    # <<< per_length_phase_impedance
    # @generated
    # >>> per_length_phase_impedance


#------------------------------------------------------------------------------
#  "DistributionTransformer" class:
#------------------------------------------------------------------------------

class DistributionTransformer(Equipment):
    """ An assembly of two or more coupled windings that transform electrical power between voltage levels. Supports both balanced and unbalanced winding connections. This class differs from Wires::PowerTransformer as follows: - it is part of a TransformerBank - it draws parameters exclusively from TransformerInfo and its associated classes.An assembly of two or more coupled windings that transform electrical power between voltage levels. Supports both balanced and unbalanced winding connections. This class differs from Wires::PowerTransformer as follows: - it is part of a TransformerBank - it draws parameters exclusively from TransformerInfo and its associated classes.
    """

    
    # Transformer data.Transformer data.
    transformer_info = db.ReferenceProperty(collection_name="transformers")

    # Virtual property. All windings of this transformer.All windings of this transformer.
    pass #windings

    # Bank this transformer belongs to.Bank this transformer belongs to.
    transformer_bank = db.ReferenceProperty(collection_name="transformers")

    # <<< distribution_transformer
    # @generated
    # >>> distribution_transformer


#------------------------------------------------------------------------------
#  "PhaseImpedanceData" class:
#------------------------------------------------------------------------------

class PhaseImpedanceData(Element):
    """ Triplet of resistance, reactance, and susceptance matrix element values.Triplet of resistance, reactance, and susceptance matrix element values.
    """

    
    # Reactance matrix element value, per length of unit.Reactance matrix element value, per length of unit.
    x = Reactance

    # Column-wise element index, assuming a symmetrical matrix. Ranges from 1 to N + N*(N-1)/2.Column-wise element index, assuming a symmetrical matrix. Ranges from 1 to N + N*(N-1)/2.
    sequence_number = db.IntegerProperty()

    # Susceptance matrix element value, per length of unit.Susceptance matrix element value, per length of unit.
    b = Susceptance

    # Resistance matrix element value, per length of unit.Resistance matrix element value, per length of unit.
    r = Resistance

    # Conductor phase impedance to which this data belongs.Conductor phase impedance to which this data belongs.
    phase_impedance = db.ReferenceProperty(collection_name="phase_impedance_data")

    # <<< phase_impedance_data
    # @generated
    # >>> phase_impedance_data




# EOF -------------------------------------------------------------------------
