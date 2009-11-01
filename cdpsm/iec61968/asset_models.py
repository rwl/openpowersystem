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

""" This package is an extension of Assets package and contains the core information classes that support asset management and different network and work planning applications with specialized documentation classes describing assets of a particular product model made by a manufacturer. There are typically many instances of an asset associated with a single asset model. It also contains 'lightweight' *Info classes, which hold model attributes that can be referenced by not only Assets but also by ConductingEquipments.This package is an extension of Assets package and contains the core information classes that support asset management and different network and work planning applications with specialized documentation classes describing assets of a particular product model made by a manufacturer. There are typically many instances of an asset associated with a single asset model. It also contains 'lightweight' *Info classes, which hold model attributes that can be referenced by not only Assets but also by ConductingEquipments.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from cdpsm.iec61970.core import IdentifiedObject

from cdpsm.iec61970.domain import Voltage
from cdpsm.iec61970.domain import AngleDegrees
from cdpsm.iec61970.domain import Length
from cdpsm.iec61970.domain import Temperature
from cdpsm.iec61970.domain import KWActivePower
from cdpsm.iec61970.domain import PerCent
from cdpsm.iec61970.domain import Resistance
from cdpsm.iec61970.domain import CurrentFlow
from cdpsm.iec61970.domain import ApparentPower
from cdpsm.iec61970.wires import WindingConnection
from cdpsm.iec61970.domain import Impedance

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

#------------------------------------------------------------------------------
#  Properties:
#------------------------------------------------------------------------------

CableOuterJacketKind = db.StringProperty(choices=("insulating", "other", "semiconducting", "polyethylene", "none", "linear_low_density_polyethylene", "pvc"))

CableShieldMaterialKind = db.StringProperty(choices=("other", "lead", "steel", "aluminum", "copper"))

ConductorInsulationKind = db.StringProperty(choices=("crosslinked_polyethylene", "butyl", "tree_retardant_crosslinked_polyethylene", "asbestos_and_varnished_cambric", "high_pressure_fluid_filled", "ethylene_propylene_rubber", "ozone_resistant_rubber", "oil_paper", "varnished_dacron_glass", "high_molecular_weight_polyethylene", "other", "varnished_cambric_cloth", "tree_resistant_high_molecular_weight_polyethylene", "unbelted_pilc", "belted_pilc", "rubber", "low_capacitance_rubber", "silicon_rubber"))

ConductorMaterialKind = db.StringProperty(choices=("steel", "other", "aluminum", "copper", "acsr"))

ConductorUsageKind = db.StringProperty(choices=("secondary", "other", "distribution", "transmission"))

CableConstructionKind = db.StringProperty(choices=("solid", "stranded", "other", "segmental", "compacted", "sector", "compressed"))

#------------------------------------------------------------------------------
#  Constants:
#------------------------------------------------------------------------------

NS_PREFIX = "cim"
NS_URI = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_AssetModels"

#------------------------------------------------------------------------------
#  "TransformerInfo" class:
#------------------------------------------------------------------------------

class TransformerInfo(IdentifiedObject):
    """ Set of transformer data, from an equipment library.Set of transformer data, from an equipment library.
    """

    
    # Virtual property. All transformers that can be described with this transformer data.All transformers that can be described with this transformer data.
    pass #transformers

    # Virtual property. Data for all the windings described by this transformer data.Data for all the windings described by this transformer data.
    pass #winding_infos

    # <<< transformer_info
    # @generated
    # >>> transformer_info


#------------------------------------------------------------------------------
#  "ToWindingSpec" class:
#------------------------------------------------------------------------------

class ToWindingSpec(IdentifiedObject):
    """ For short-circuit tests, specifies the winding and tap for all short-circuited windings.  For open-circuit tests, specifies the winding, tap, induced voltage, and induced angle for any non-excited windings that were measured during the test. This won't apply if only the exciting current and no-load losses were measured.For short-circuit tests, specifies the winding and tap for all short-circuited windings.  For open-circuit tests, specifies the winding, tap, induced voltage, and induced angle for any non-excited windings that were measured during the test. This won't apply if only the exciting current and no-load losses were measured.
    """

    
    # Tap step number for the 'to' winding of the test pair.Tap step number for the 'to' winding of the test pair.
    to_tap_step = db.IntegerProperty()

    # (if open-circuit test) Voltage measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited.(if open-circuit test) Voltage measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited.
    voltage = Voltage

    # (if open-circuit test) Phase shift measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited.(if open-circuit test) Phase shift measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited.
    phase_shift = AngleDegrees

    open_circuit_tests = db.ListProperty(db.Key)

    short_circuit_tests = db.ListProperty(db.Key)

    # Winding short-circuited in a short-circuit test, or measured for induced voltage and angle in an open-circuit test.Winding short-circuited in a short-circuit test, or measured for induced voltage and angle in an open-circuit test.
    to_winding = db.ReferenceProperty(collection_name="to_winding_specs")

    # <<< to_winding_spec
    # @generated
    # >>> to_winding_spec


#------------------------------------------------------------------------------
#  "WireArrangement" class:
#------------------------------------------------------------------------------

class WireArrangement(IdentifiedObject):
    """ Identification, spacing and configuration of the wires of a Conductor, with reference to their type.Identification, spacing and configuration of the wires of a Conductor, with reference to their type.
    """

    
    # Signed horizontal distance from the first wire to a common reference point.Signed horizontal distance from the first wire to a common reference point.
    mounting_point_x = Length

    # Height above ground of the first wire.Height above ground of the first wire.
    mounting_point_y = Length

    # Position number on the structure corresponding to this wire. For example, use 1..3 for phases and 4 for the neutral on a 3-phase structure. The individual phase assignments matter; for example, ABC will produce a different set of unbalanced line parameters, by phase, than BAC.Position number on the structure corresponding to this wire. For example, use 1..3 for phases and 4 for the neutral on a 3-phase structure. The individual phase assignments matter; for example, ABC will produce a different set of unbalanced line parameters, by phase, than BAC.
    position = db.IntegerProperty()

    # Conductor data this wire arrangement belongs to.Conductor data this wire arrangement belongs to.
    conductor_info = db.ReferenceProperty(collection_name="wire_arrangements")

    # Wire type used for this wire arrangement.Wire type used for this wire arrangement.
    wire_type = db.ReferenceProperty(collection_name="wire_arrangements")

    # <<< wire_arrangement
    # @generated
    # >>> wire_arrangement


#------------------------------------------------------------------------------
#  "ConductorInfo" class:
#------------------------------------------------------------------------------

class ConductorInfo(IdentifiedObject):
    """ Conductor data.Conductor data.
    """

    
    # Number of phases (including neutral) to be retained. Any wires beyond this number should be reduced into the earth return.Number of phases (including neutral) to be retained. Any wires beyond this number should be reduced into the earth return.
    phase_count = db.IntegerProperty()

    # (if insulated conductor) Material used for insulation.(if insulated conductor) Material used for insulation.
    insulation_material = ConductorInsulationKind

    # (if insulated conductor) Thickness of the insulation.(if insulated conductor) Thickness of the insulation.
    insulation_thickness = Length

    # True if conductor is insulated.True if conductor is insulated.
    insulated = db.BooleanProperty()

    # Usage of this conductor.Usage of this conductor.
    usage = ConductorUsageKind

    # Virtual property. All wire arrangements (single wires) that make this conductor.All wire arrangements (single wires) that make this conductor.
    pass #wire_arrangements

    # Virtual property. All conductor segments described by this conductor data.All conductor segments described by this conductor data.
    pass #conductor_segments

    # <<< conductor_info
    # @generated
    # >>> conductor_info


#------------------------------------------------------------------------------
#  "DistributionWindingTest" class:
#------------------------------------------------------------------------------

class DistributionWindingTest(IdentifiedObject):
    """ Test results for one or more transformer windings. These may include short-circuit or open-circuit (excitation) tests. Short-circuit test results include load losses and leakage impedances. Open-circuit test results may include no-load losses, exciting current, phase shifts, and induced voltage. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence.Test results for one or more transformer windings. These may include short-circuit or open-circuit (excitation) tests. Short-circuit test results include load losses and leakage impedances. Open-circuit test results may include no-load losses, exciting current, phase shifts, and induced voltage. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence.
    """

    
    # Tap step number for the 'from' winding of the test pair.Tap step number for the 'from' winding of the test pair.
    from_tap_step = db.IntegerProperty()

    # Winding that voltage or current is applied to during the test.Winding that voltage or current is applied to during the test.
    from_winding = db.ReferenceProperty(collection_name="winding_tests")

    # <<< distribution_winding_test
    # @generated
    # >>> distribution_winding_test


#------------------------------------------------------------------------------
#  "WireType" class:
#------------------------------------------------------------------------------

class WireType(IdentifiedObject):
    """ Wire conductor (per IEEE specs). A specific type of wire or combination of wires, not insulated from each other, suitable for carrying electrical current.Wire conductor (per IEEE specs). A specific type of wire or combination of wires, not insulated from each other, suitable for carrying electrical current.
    """

    
    # AC resistance per unit length of the conductor at 75 degrees C.AC resistance per unit length of the conductor at 75 degrees C.
    r_ac75 = Resistance

    # (if there is a different core material) Radius of the central core.(if there is a different core material) Radius of the central core.
    core_radius = Length

    # (if used) Number of strands in the steel core.(if used) Number of strands in the steel core.
    core_strand_count = db.IntegerProperty()

    # AC resistance per unit length of the conductor at 25 degrees C.AC resistance per unit length of the conductor at 25 degrees C.
    r_ac25 = Resistance

    # Outside radius of the wire.Outside radius of the wire.
    radius = Length

    # Geometric Mean Radius. If we replace the conductor by a thin walled tube of radius GMR, then its reactance is identical to the reactance of the actual conductor.Geometric Mean Radius. If we replace the conductor by a thin walled tube of radius GMR, then its reactance is identical to the reactance of the actual conductor.
    gmr = Length

    # DC resistance per unit length of the conductor at 20 degrees C.DC resistance per unit length of the conductor at 20 degrees C.
    r_dc20 = Resistance

    # AC resistance per unit length of the conductor at 50 degrees C.AC resistance per unit length of the conductor at 50 degrees C.
    r_ac50 = Resistance

    # Wire material.Wire material.
    material = ConductorMaterialKind

    # Describes the wire guage or cross section (e.g., 4/0, #2, 336.5).Describes the wire guage or cross section (e.g., 4/0, #2, 336.5).
    size_description = db.StringProperty()

    # Number of strands in the wire.Number of strands in the wire.
    strand_count = db.IntegerProperty()

    # Current carrying capacity of the wire under stated thermal conditions.Current carrying capacity of the wire under stated thermal conditions.
    rated_current = CurrentFlow

    # Virtual property. All concentric neutral cables using this wire type.All concentric neutral cables using this wire type.
    pass #concentric_neutral_cable_infos

    # Virtual property. All wire arrangements using this wire type.All wire arrangements using this wire type.
    pass #wire_arrangements

    # <<< wire_type
    # @generated
    # >>> wire_type


#------------------------------------------------------------------------------
#  "WindingInfo" class:
#------------------------------------------------------------------------------

class WindingInfo(IdentifiedObject):
    """ Winding data.Winding data.
    """

    
    # Sequence number for this winding, corresponding to the winding's order in the TransformerBank.vectorGroup attribute. Highest voltage winding should be '1'.Sequence number for this winding, corresponding to the winding's order in the TransformerBank.vectorGroup attribute. Highest voltage winding should be '1'.
    sequence_number = db.IntegerProperty()

    # Normal apparent power rating of this winding.Normal apparent power rating of this winding.
    rated_s = ApparentPower

    # Rated voltage of this winding: phase-phase for three-phase windings, and either phase-phase or phase-neutral for single-phase windings.Rated voltage of this winding: phase-phase for three-phase windings, and either phase-phase or phase-neutral for single-phase windings.
    rated_u = Voltage

    # Kind of connection of this winding.Kind of connection of this winding.
    connection_kind = WindingConnection

    # Apparent power that the winding can carry under emergency conditions.Apparent power that the winding can carry under emergency conditions.
    emergency_s = ApparentPower

    # DC resistance of this winding.DC resistance of this winding.
    r = Resistance

    # Winding phase angle where 360 degrees are represented with clock hours, so the valid values are {0, ..., 11}. For example, to express winding code 'Dyn11', set attributes as follows: 'connectionKind' = Yn and 'phaseAngle' = 11.Winding phase angle where 360 degrees are represented with clock hours, so the valid values are {0, ..., 11}. For example, to express winding code 'Dyn11', set attributes as follows: 'connectionKind' = Yn and 'phaseAngle' = 11.
    phase_angle = db.IntegerProperty()

    # Basic insulation level voltage rating.Basic insulation level voltage rating.
    insulation_u = Voltage

    # Apparent power that this winding can carry for a short period of time.Apparent power that this winding can carry for a short period of time.
    short_term_s = ApparentPower

    # Virtual property. All winding tests during which voltage or current was applied to this winding.All winding tests during which voltage or current was applied to this winding.
    pass #winding_tests

    # Virtual property. Tap steps and induced voltage/angle measurements for tests in which this winding was not excited.Tap steps and induced voltage/angle measurements for tests in which this winding was not excited.
    pass #to_winding_specs

    # Transformer data that this winding description is part of.Transformer data that this winding description is part of.
    transformer_info = db.ReferenceProperty(collection_name="winding_infos")

    # Virtual property. All windings described by this winding data.All windings described by this winding data.
    pass #windings

    # <<< winding_info
    # @generated
    # >>> winding_info


#------------------------------------------------------------------------------
#  "CableInfo" class:
#------------------------------------------------------------------------------

class CableInfo(ConductorInfo):
    """ Cable data.Cable data.
    """

    
    # Maximum nominal design operating temperature.Maximum nominal design operating temperature.
    nominal_temperature = Temperature

    # Diameter over the outer screen; should be the shield's inside diameter..Diameter over the outer screen; should be the shield's inside diameter..
    diameter_over_screen = Length

    # True if sheath / shield is used as a neutral (i.e., bonded).True if sheath / shield is used as a neutral (i.e., bonded).
    sheath_as_neutral = db.BooleanProperty()

    # Diameter over the outermost jacketing layer.Diameter over the outermost jacketing layer.
    diameter_over_jacket = Length

    # Diameter over the core, including any semi-con screen; should be the insulating layer's inside diameter.Diameter over the core, including any semi-con screen; should be the insulating layer's inside diameter.
    diameter_over_core = Length

    # Kind of construction of this cable.Kind of construction of this cable.
    construction_kind = CableConstructionKind

    # Kind of outer jacket of this cable.Kind of outer jacket of this cable.
    outer_jacket_kind = CableOuterJacketKind

    # True if wire strands are extruded in a way to fill the voids in the cable.True if wire strands are extruded in a way to fill the voids in the cable.
    is_strand_fill = db.BooleanProperty()

    # Material of the shield.Material of the shield.
    shield_material = CableShieldMaterialKind

    # Diameter over the insulating layer, excluding outer screen.Diameter over the insulating layer, excluding outer screen.
    diameter_over_insulation = Length

    # <<< cable_info
    # @generated
    # >>> cable_info


#------------------------------------------------------------------------------
#  "OpenCircuitTest" class:
#------------------------------------------------------------------------------

class OpenCircuitTest(DistributionWindingTest):
    """ Open-circuit test results may include no-load losses, exciting current, phase shifts, and induced voltage. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence. For induced voltage and phase shifts, use the associated ToWindingSpec class.Open-circuit test results may include no-load losses, exciting current, phase shifts, and induced voltage. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence. For induced voltage and phase shifts, use the associated ToWindingSpec class.
    """

    
    # Losses measured from a zero-sequence open-circuit (excitation) test.Losses measured from a zero-sequence open-circuit (excitation) test.
    no_load_loss_zero = KWActivePower

    # Losses measured from a positive-sequence or single-phase open-circuit (excitation) test.Losses measured from a positive-sequence or single-phase open-circuit (excitation) test.
    no_load_loss = KWActivePower

    # Exciting current measured from a positive-sequence or single-phase open-circuit (excitation) test.Exciting current measured from a positive-sequence or single-phase open-circuit (excitation) test.
    exciting_current = PerCent

    # Exciting current measured from a zero-sequence open-circuit (excitation) test.Exciting current measured from a zero-sequence open-circuit (excitation) test.
    exciting_current_zero = PerCent

    measured_winding_specs = db.ListProperty(db.Key)

    # <<< open_circuit_test
    # @generated
    # >>> open_circuit_test


#------------------------------------------------------------------------------
#  "ConcentricNeutralCableInfo" class:
#------------------------------------------------------------------------------

class ConcentricNeutralCableInfo(CableInfo):
    """ Concentric neutral cable data.Concentric neutral cable data.
    """

    
    # Number of concentric neutral strands.Number of concentric neutral strands.
    neutral_strand_count = db.IntegerProperty()

    # Diameter over the concentric neutral strands.Diameter over the concentric neutral strands.
    diameter_over_neutral = Length

    # Wire type used for this concentric neutral cable.Wire type used for this concentric neutral cable.
    wire_type = db.ReferenceProperty(collection_name="concentric_neutral_cable_infos")

    # <<< concentric_neutral_cable_info
    # @generated
    # >>> concentric_neutral_cable_info


#------------------------------------------------------------------------------
#  "OverheadConductorInfo" class:
#------------------------------------------------------------------------------

class OverheadConductorInfo(ConductorInfo):
    """ Overhead conductor data.Overhead conductor data.
    """

    
    # (if applicable) Insulation thickness of the neutral conductor.(if applicable) Insulation thickness of the neutral conductor.
    neutral_insulation_thickness = Length

    # Number of conductor strands in the symmetrical bundle (1-12).Number of conductor strands in the symmetrical bundle (1-12).
    phase_conductor_count = db.IntegerProperty()

    # Distance between conductor strands in a symmetrical bundle.Distance between conductor strands in a symmetrical bundle.
    phase_conductor_spacing = Length

    # <<< overhead_conductor_info
    # @generated
    # >>> overhead_conductor_info


#------------------------------------------------------------------------------
#  "TapeShieldCableInfo" class:
#------------------------------------------------------------------------------

class TapeShieldCableInfo(CableInfo):
    """ Tape shield cable data.Tape shield cable data.
    """

    
    # Thickness of the tape shield, before wrapping.Thickness of the tape shield, before wrapping.
    tape_thickness = Length

    # Percentage of the tape shield width that overlaps in each wrap, typically 10% to 25%.Percentage of the tape shield width that overlaps in each wrap, typically 10% to 25%.
    tape_lap = PerCent

    # <<< tape_shield_cable_info
    # @generated
    # >>> tape_shield_cable_info


#------------------------------------------------------------------------------
#  "ShortCircuitTest" class:
#------------------------------------------------------------------------------

class ShortCircuitTest(DistributionWindingTest):
    """ Short-circuit test results include load losses and leakage impedances. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence. There must be at least one short-circuited ('to') winding.Short-circuit test results include load losses and leakage impedances. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence. There must be at least one short-circuited ('to') winding.
    """

    
    # Load losses from a zero-sequence short-circuit test.Load losses from a zero-sequence short-circuit test.
    load_loss_zero = KWActivePower

    # Leakage impedance measured from a zero-sequence short-circuit test.Leakage impedance measured from a zero-sequence short-circuit test.
    leakage_impedance_zero = Impedance

    # Leakage impedance measured from a positive-sequence or single-phase short-circuit test.Leakage impedance measured from a positive-sequence or single-phase short-circuit test.
    leakage_impedance = Impedance

    # Load losses from a positive-sequence or single-phase short-circuit test.Load losses from a positive-sequence or single-phase short-circuit test.
    load_loss = KWActivePower

    shorted_winding_specs = db.ListProperty(db.Key)

    # <<< short_circuit_test
    # @generated
    # >>> short_circuit_test




# EOF -------------------------------------------------------------------------