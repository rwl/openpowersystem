# Copyright (C) 2009 Richard W. Lincoln
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation; version 2 dated June, 1991.
#
# This software is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANDABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA

from cim14.iec61968.common import Document
from cim14.iec61970.core import IdentifiedObject
from cim14.iec61968.assets import AssetContainer
from cim14.iec61968.informative.inf_common import Role
from cim14.iec61968.assets import Asset
from cim14.iec61968.assets import ElectricalInfo
from cim14.iec61970.core import Curve
from cim14.iec61968.common import ActivityRecord
from cim14 import Element

from cim14.iec61970.domain import ApparentPower
from cim14.iec61970.domain import Length
from cim14.iec61970.domain import ActivePower
from cim14.iec61970.domain import CurrentFlow
from cim14.iec61970.domain import AbsoluteDate
from cim14.iec61970.domain import AngleDegrees
from cim14.iec61970.domain import Voltage
from cim14.iec61970.core import PhaseCode
from cim14.iec61970.domain import ReactivePower
from cim14.iec61970.domain import PU
from cim14.iec61970.domain import Hours
from cim14.iec61970.domain import Reactance
from cim14.iec61970.domain import Volume
from cim14.iec61970.domain import PerCent
from cim14.iec61970.domain import Resistance
from cim14.iec61970.domain import Impedance
from cim14.iec61970.domain import Capacitance
from cim14.iec61970.domain import Temperature
from cim14.iec61970.wires import WindingConnection
from cim14.iec61970.domain import IntegerQuantity
from cim14.iec61970.domain import Money

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

PoleTreatmentKind = db.StringProperty(choices=("green_stain", "gray_stain", "other", "natural", "butt", "full", "unknown", "penta"))

PolePreservativeKind = db.StringProperty(choices=("penta", "other", "creosote", "chemonite", "cellon", "unknown", "naphthena"))

JointConfigurationKind = db.StringProperty(choices=("wires3to1", "wires1to1", "other", "wires2to1"))

VehicleUsageKind = db.StringProperty(choices=("crew", "other", "user", "contractor"))

TransformerFunctionKind = db.StringProperty(choices=("autotransformer", "other", "secondary_transformer", "voltage_regulator", "power_transformer"))

JointFillKind = db.StringProperty(choices=("no_void", "no_fill_prefab", "other", "petrolatum", "insoluseal", "oil", "air_no_filling", "epoxy", "asphaltic", "bluefill254"))

ProcedureKind = db.StringProperty(choices=("test", "diagnosis", "inspection", "other", "maintenance"))

PoleBaseKind = db.StringProperty(choices=("dirt", "cement", "other", "asphalt", "unknown"))

ShuntImpedanceLocalControlKind = db.StringProperty(choices=("none", "voltage", "power_factor", "time", "reactive_power", "temperature", "current"))

CoolingKind = db.StringProperty(choices=("self_cooling", "forced_oil_and_air", "forced_air", "other"))

SubstationFunctionKind = db.StringProperty(choices=("distribution", "transmission", "sub_transmission", "industrial", "other", "generation"))

BushingInsulationPfTestKind = db.StringProperty(choices=("c1", "c2"))

TowerConstructionKind = db.StringProperty(choices=("tension", "suspension"))

FactsDeviceKind = db.StringProperty(choices=("tsbr", "tssc", "svc", "statcom", "tcvl", "tcpar", "tcsc", "upfc"))

ShuntImpedanceControlKind = db.StringProperty(choices=("remote_with_local_override", "local_only", "fixed", "remote_only"))

StreetlightLampKind = db.StringProperty(choices=("high_pressure_sodium", "other", "mercury_vapor", "metal_halide"))

FacilityKind = db.StringProperty(choices=("storage", "plant", "building", "switching", "generation"))

AnchorKind = db.StringProperty(choices=("unknown", "multi_helix", "other", "rod", "concrete", "helix", "screw"))

CompositeSwitchKind = db.StringProperty(choices=("other", "throw_over", "ug_multi_switch", "esco_throw_over", "gral", "ral", "regulator_bypass"))

StructureMaterialKind = db.StringProperty(choices=("other", "steel", "concrete", "wood"))

FailureIsolationMethodKind = db.StringProperty(choices=("manually_isolated", "other", "breaker_operation", "fuse", "burned_in_the_clear"))

TransformerConstructionKind = db.StringProperty(choices=("padmount_dead_front", "padmounted", "valut", "one_phase", "network", "underground", "subway", "overhead", "three_phase", "padmount_live_front", "padmount_loop_through", "padmount_feed_through", "dry_type", "aerial", "vault_three_phase", "unknown"))

RegulationBranchKind = db.StringProperty(choices=("breaker", "recloser", "sectionner", "line", "transformer", "switch", "other", "fuse"))

MediumKind = db.StringProperty(choices=("gas", "solid", "liquid"))

ns_prefix = "cim.IEC61968.Informative.InfAssets"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#IEC61968.Informative.InfAssets"

class ProcedureDataSet(Document):
    """ A data set recorded each time a procedure is executed. Observed results are captured in associated measurement values and/or values for properties relevant to the type of procedure performed.
    """

#    measurement_values = db.ListProperty(db.Key)

#    @property
#    def procedure_data_sets(self):
#        return MeasurementValue.gql("WHERE measurement_values = :1", self.key())
#    transformer_observations = db.ListProperty(db.Key)

#    @property
#    def procedure_data_sets(self):
#        return TransformerObservation.gql("WHERE transformer_observations = :1", self.key())
#    procedure = db.ReferenceProperty()
#    properties = db.ListProperty(db.Key)

#    @property
#    def procedure_data_sets(self):
#        return UserAttribute.gql("WHERE properties = :1", self.key())

class PowerRating(IdentifiedObject):
    """ There are often stages of power which are associated with stages of cooling. For instance, a transformer may be rated 121kV on the primary, 15kV on the secondary and 4kV on the tertiary winding. These are voltage ratings and the power ratings are generally the same for all three windings and independent of the voltage ratings, there are instances where the tertiary may have a lower power rating. For example, for three stages, the power rating may be 15/20/25 MVA and the cooling is OA/FA/FOA. The 15 MVA rating goes with the OA cooling (Oil and Air cooling). This is called the self cooled rating as there are no external cooling enhancements. The 20 MVA rating goes with the FA cooling (Forced Air cooling), this means that when the fans are running and thus enhancing the cooling characteristics, the transformer can operate at a power level of 20 MVA. The 25 MVA rating goes with the FOA cooling (Forced Oil and Air cooling), this means that when the fans and pumps are running and thus enhancing the cooling characteristics even more than before, the transformer can operate at a power level of 25 MVA. This 15/20/25 MVA does not state how the power is split between the various windings. It may be 25 MVA input on the primary, 25 MVA output on the secondary and 0 MVA output on the tertiary. It may also operate at 25 MVA input on the primary, 17 MVA output on the secondary and 8 MVA output on the tertiary.
    """

    # Kind of cooling system.
    cooling_kind = CoolingKind
    # Stage of cooling and associated power rating.
    stage = db.IntegerProperty()
    # The power rating associated with type of cooling specified for this stage.
    power_rating = ApparentPower
#    transformer_assets = db.ListProperty(db.Key)

#    @property
#    def power_ratings(self):
#        return TransformerAsset.gql("WHERE transformer_assets = :1", self.key())

class Facility(AssetContainer):
    """ A facility may contain buildings, storage facilities, switching facilities, power generation, manufacturing facilities, maintenance facilities, etc.
    """

    # Kind of this facility.
    kind = db.StringProperty()

class Specification(Document):
    """ Specification can be used for various purposes relative to an asset, a logical device (PowerSystemResource), location, etc. Examples include documents supplied by manufacturers such as asset installation instructions, asset maintenance instructions, etc.
    """

    # The 'asset_properites' property has been implicitly created by
    # the property_specification' property of UserAttribute.
    pass
    # The 'mediums' property has been implicitly created by
    # the specification' property of Medium.
    pass
#    qualification_requirements = db.ListProperty(db.Key)

#    @property
#    def specifications(self):
#        return QualificationRequirement.gql("WHERE qualification_requirements = :1", self.key())
    # The 'asset_property_curves' property has been implicitly created by
    # the specification' property of AssetPropertyCurve.
    pass
#    dimensions_infos = db.ListProperty(db.Key)

#    @property
#    def specifications(self):
#        return DimensionsInfo.gql("WHERE dimensions_infos = :1", self.key())
    # The 'ratings' property has been implicitly created by
    # the rating_specification' property of UserAttribute.
    pass
    # The 'reliability_infos' property has been implicitly created by
    # the specification' property of ReliabilityInfo.
    pass

class SubstationAsset(AssetContainer):
    """ A grouping of assets such as conductors, transformers, switchgear, etc. When located on the ground surface, it is usually surrounded by some kind of fence with a locked gate. It may also be located inside buildings, in underground vaults, and on structures. Use 'category' for utility-specific categorisation (such as Air Cooled, Gas Insultated, etc.).
    """

    # Function of this substation asset.
    function = SubstationFunctionKind
#    substation = db.ReferenceProperty()

class DocAssetRole(Role):
    """ Roles played between Documents and Assets.
    """

#    asset = db.ReferenceProperty()
#    document = db.ReferenceProperty()

class Procedure(Document):
    """ A documented procedure for various types of Work or Work Tasks. One or more procedures guide a compatible unit, a standard way of performing a unit of work. The type of procedure is defined in Procedure.type. For example, when type=Inspection, this procedure coupled with Schedule and other information provides the key items of an inspection plan. Another type of Procedure is a Diagnosis. Note that each specific values and settings to be used in a procedure is intended to be described in an instance of ProcedureValue. A maintenance ticket, a type of Work, is generated whenever maintenance is determined to be needed as a result of an inspection or diagnosis.
    """

    # The textual description of the procedure, which references instances of ProcedureValue as appropriate.
    instruction = db.StringProperty()
    # Kind of this procedure.
    kind = ProcedureKind
    # Code for this kind of procedure.
    corporate_code = db.StringProperty()
    # Sequence number in a sequence of procedures being performed.
    sequence_number = db.StringProperty()
#    compatible_units = db.ListProperty(db.Key)

#    @property
#    def procedures(self):
#        return CompatibleUnit.gql("WHERE compatible_units = :1", self.key())
#    limits = db.ListProperty(db.Key)

#    @property
#    def procedures(self):
#        return Limit.gql("WHERE limits = :1", self.key())
    # The 'procedure_data_sets' property has been implicitly created by
    # the procedure' property of ProcedureDataSet.
    pass
    # The 'procedure_values' property has been implicitly created by
    # the procedure' property of UserAttribute.
    pass

class Cabinet(AssetContainer):
    """ Enclosure that offers protection to the equipment it contains and/or safety to people/animals outside it.
    """

#    cabinet_model = db.ReferenceProperty()

class DimensionsInfo(IdentifiedObject):
    """ As applicable, the basic linear, area, or volume dimensions of an asset, asset type (AssetModel) or other type of object (such as land area). Units and multipliers are specified per dimension.
    """

    # A description of the orientation of the object relative to the dimensions. As an example, a vault may have north-south orientation for the sizeLength measurement and sizeDepth may be the height of the vault.
    orientation = db.StringProperty()
    # Length measurement.
    size_length = Length
    # Depth measurement.
    size_depth = Length
    # Width measurement.
    size_width = Length
    # Diameter measurement.
    size_diameter = Length
    # The 'assets' property has been implicitly created by
    # the dimensions_info' property of Asset.
    pass
    # The 'locations' property has been implicitly created by
    # the dimensions_info' property of Location.
    pass
#    specifications = db.ListProperty(db.Key)

#    @property
#    def dimensions_infos(self):
#        return Specification.gql("WHERE specifications = :1", self.key())

class TapChangerAsset(Asset):
    """ Physical asset performing TapChanger function.
    """

#    tap_changer_model = db.ReferenceProperty()

class Structure(AssetContainer):
    """ Construction holding assets such as conductors, transformers, switchgear, etc.
    """

    # True if weeds are to be removed around asset.
    remove_weed = db.BooleanProperty()
    # Material this structure is made of.
    material_kind = StructureMaterialKind
    # Date weed were last removed.
    weed_removed_date = AbsoluteDate
    # Name of fumigant.
    fumigant_name = db.StringProperty()
    # Date fumigant was last applied.
    fumigant_applied_date = AbsoluteDate
    # Visible height of structure above ground level for overhead construction (e.g., Pole or Tower) or below ground level for an underground vault, manhole, etc. Refer to associated DimensionPropertiesInfo for other types of dimensions.
    height = Length
    # The 'structure_supports' property has been implicitly created by
    # the secured_structure' property of StructureSupport.
    pass

class StructureSupport(Asset):
    """ Support for Structures.
    """

    # Length of anchor lead or guy.
    length = Length
    # Number of rods used for an anchor.
    rod_count = db.IntegerProperty()
    # Length of rod used for an anchor.
    rod_length = Length
    # Size of anchor or guy.
    size = db.StringProperty()
    # Direction of supporting anchor or guy.
    direction = AngleDegrees
#    secured_structure = db.ReferenceProperty()

class SwitchInfo(ElectricalInfo):
    """ Properties of a switch.
    """

    # True if device is capable of being operated by remote control.
    remote = db.BooleanProperty()
    # The lowest value of current that the switch can make, carry and break in uninterrupted duty at the rated voltage under specified operating conditions without suffering significant deterioration of its performance.
    minimum_current = CurrentFlow
    # The maximum rms voltage that may be applied across an open contact without breaking down the dielectric properties of the switch in the open position.
    dielectric_strength = Voltage
    # Breaking capacity, or short circuit rating, is the maximum rated current which the device can safely interrupt at the rated voltage.
    interrupting_rating = CurrentFlow
    # True if switch has load breaking capabiity. Unless specified false, this is always assumed to be true for breakers and reclosers.
    load_break = db.BooleanProperty()
    # Number of poles (i.e. of current carrying conductors that are switched).
    pole_count = db.IntegerProperty()
    # True if multi-phase switch controls all phases concurrently.
    gang = db.BooleanProperty()
    # The highest value of current the switch can carry in the closed position at the rated voltage under specified operating conditions without suffering significant deterioration of its performance.
    withstand_current = CurrentFlow
    # The highest value of current the switch can make at the rated voltage under specified operating conditions without suffering significant deterioration of its performance.
    making_capacity = CurrentFlow
#    switch_type_asset = db.ReferenceProperty()
#    switch_asset_model = db.ReferenceProperty()
    # The 'switch_assets' property has been implicitly created by
    # the switch_info' property of SwitchAsset.
    pass

class ElectricalAsset(Asset):
    """ An asset that has (or can have) a role in the electrical network.
    """

    # True if the asset is physically connected to electrical network (as opposed to being in a warehouse, being refurbished, etc.). Note that this attribute is not intended to imply energization status and/or whether the asset is actually being used.
    is_connected = db.BooleanProperty()
    # If 'isConnected' is true, then this is the as-built phase(s) that the asset is associatied with.
    phase_code = PhaseCode
#    conducting_equipment = db.ReferenceProperty()
#    electrical_infos = db.ListProperty(db.Key)

#    @property
#    def electrical_assets(self):
#        return ElectricalInfo.gql("WHERE electrical_infos = :1", self.key())

class ShuntImpedanceInfo(ElectricalInfo):
    """ Properties of a shunt impedance.
    """

    # Lower control setting.
    local_on_level = db.StringProperty()
    # True if the locally controlled capacitor has voltage override capability.
    local_override = db.BooleanProperty()
    # The size of the individual units that make up the bank.
    cell_size = ReactivePower
    # Kind of local controller.
    local_control_kind = ShuntImpedanceLocalControlKind
    # For locally controlled shunt impedances which have a voltage override feature, the high voltage override value. If the voltage is above this value, the shunt impedance will be turned off regardless of the other local controller settings.
    high_voltage_override = PU
    # For VAR, amp, or power factor locally controlled shunt impedances, the index of the regulation branch.
    reg_branch = db.StringProperty()
    # Kind of control (if any).
    control_kind = ShuntImpedanceControlKind
    # True if open is normal status for a fixed capacitor bank, otherwise normal status is closed.
    normal_open = db.BooleanProperty()
    # Upper control setting.
    local_off_level = db.StringProperty()
    # (For VAR, amp, or power factor locally controlled shunt impedances) Kind of regulation branch.
    reg_branch_kind = RegulationBranchKind
    # For locally controlled shunt impedances which have a voltage override feature, the low voltage override value. If the voltage is below this value, the shunt impedance will be turned on regardless of the other local controller settings.
    low_voltage_override = PU
    # IdmsShuntImpedanceData.maxNumSwitchOps
    max_switch_operation_count = db.IntegerProperty()
    # For VAR, amp, or power factor locally controlled shunt impedances, the end of the branch that is regulated. The field has the following values: from side, to side, and tertiary (only if the branch is a transformer).
    reg_branch_end = db.IntegerProperty()
    # Time interval between consecutive switching operations.
    switch_operation_cycle = Hours
    # For VAR, amp, or power factor locally controlled shunt impedances, the flow direction: in, out.
    branch_direct = db.IntegerProperty()
    # Phases that are measured for controlling the device.
    sensing_phase_code = PhaseCode
    # True if regulated voltages are measured line to line, otherwise they are measured line to ground.
    v_reg_line_line = db.BooleanProperty()
#    shunt_compensator_type_asset = db.ReferenceProperty()
#    shunt_compensator_asset_model = db.ReferenceProperty()
    # The 'shunt_compensator_assets' property has been implicitly created by
    # the shunt_impedance_info' property of ShuntCompensatorAsset.
    pass

class WindingInsulation(IdentifiedObject):
    """ Winding insulation condition as a result of a test.
    """

    # As of statusDate, the leakage reactance measured at the 'from' winding with the 'to' winding short-circuited and all other windings open-circuited.
    leakage_reactance = Reactance
    # For testType, status of Winding Insulation Resistance as of statusDate. Typical values are: Acceptable, Questionable, Failed.
    insulation_resistance = db.StringProperty()
    # Status of Winding Insulation Power Factor as of statusDate: Acceptable, Minor Deterioration or Moisture Absorption, Major Deterioration or Moisture Absorption, Failed.
    insulation_pfstatus = db.StringProperty()
    status = db.ReferenceProperty()
#    from_transformer_winding = db.ReferenceProperty()
#    ground = db.ReferenceProperty()
#    transformer_observation = db.ReferenceProperty()
#    to_transformer_winding = db.ReferenceProperty()

class PotentialTransformerInfo(ElectricalInfo):
    """ Used to define either the required additional electrical properties of a type of a Potential Transformer (PT), or a PT Model.
    """

    # Ratio for the secondary winding tap changer.
    secondary_ratio = db.ReferenceProperty()
    # Ratio for the primary winding tap changer.
    primary_ratio = db.ReferenceProperty()
    # Ratio for the tertiary winding tap changer.
    tertiary_ratio = db.ReferenceProperty()
    # The 'potential_transformer_assets' property has been implicitly created by
    # the potential_transformer_info' property of PotentialTransformerAsset.
    pass
#    potential_transformer_type_asset = db.ReferenceProperty()
    # The 'potential_transformer_asset_models' property has been implicitly created by
    # the potential_transformer_info' property of PotentialTransformerAssetModel.
    pass

class SVCInfo(ElectricalInfo):
    """ Properties for an SVC, allowing the capacitive and inductive ratings for each phase to be specified individually if required.
    """

    # Maximum inductive reactive power
    inductive_rating = Reactance
    # Maximum capacitive reactive power
    capacitive_rating = Reactance
#    svcasset_model = db.ReferenceProperty()
#    svcasset = db.ReferenceProperty()
#    svctype_assets = db.ListProperty(db.Key)

#    @property
#    def svc_infos(self):
#        return SVCTypeAsset.gql("WHERE svctype_assets = :1", self.key())

class CompositeSwitchAsset(Asset):
    """ Physical asset that performs a given CompositeSwitch's role.
    """

    # Kind of composite switch.
    kind = CompositeSwitchKind
#    composite_switch_info = db.ReferenceProperty()
#    composite_switch_asset_model = db.ReferenceProperty()

class Medium(IdentifiedObject):
    """ A substance that either (1) provides the means of transmission of a force or effect, such as hydraulic fluid, or (2) is used for a surrounding or enveloping substance, such as oil in a transformer or circuit breaker.
    """

    # The volume of the medium specified for this application. Note that the actual volume is a type of measurement associated witht the asset.
    volume_spec = Volume
    # Kind of this medium.
    kind = MediumKind
#    assets = db.ListProperty(db.Key)

#    @property
#    def mediums(self):
#        return Asset.gql("WHERE assets = :1", self.key())
#    specification = db.ReferenceProperty()

class AssetAssetRole(Role):
    """ Roles played between Assets and other Assets.
    """

#    from_asset = db.ReferenceProperty()
#    to_asset = db.ReferenceProperty()

class WireArrangement(IdentifiedObject):
    """ Identification, spacing and configuration of the wires of a ConductorType, with reference to their type.
    """

    # Mounting point where wire One is mounted.
    mounting_point_y = db.IntegerProperty()
    # Mounting point where wire One is mounted.
    mounting_point_x = db.IntegerProperty()
#    wire_type = db.ReferenceProperty()
#    conductor_type = db.ReferenceProperty()

class ReliabilityInfo(IdentifiedObject):
    """ Information regarding the experienced and expected reliability of a specific asset, type of asset, or asset model.
    """

    # Momentary failure rate (temporary failures/kft-year).
    mom_failure_rate = PerCent
    # Mean time to repair (MTTR - hours).
    m_ttr = Hours
#    specification = db.ReferenceProperty()
#    assets = db.ListProperty(db.Key)

#    @property
#    def reliability_infos(self):
#        return Asset.gql("WHERE assets = :1", self.key())

class TransformerInfo(ElectricalInfo):
    """ Additional electrical properties of a type of transformer, of a transformer model, or the actual ones of a particular transformer asset.
    """

    # Secondary winding line drop compensation resistance.
    line_drp_rs = Resistance
    # Secondary winding line drop compensation reactance.
    line_drp_xs = Reactance
    # True if secondary winding tap changer has reverse regulation capability.
    rev_reg_s = db.BooleanProperty()
    # Impedance Secondary to Tertiary.
    impedance_xy = Impedance
    # True if transformer is grounded.
    grounded = db.BooleanProperty()
    # Ground resistance path through connected grounding transformer.
    r_ground = Resistance
    # Primary winding line drop compensation resistance.
    line_drp_rp = Resistance
    # Magnetization power factor.
    mag_pf = db.FloatProperty()
    # Primary winding line drop compensation reactance.
    line_drp_xp = Reactance
    # Apparent power that the winding can carry under emergency conditions.
    emergency_apparent_power = ApparentPower
    # Impedance Primary to Tertiary.
    impedance_hy = Impedance
    # Ground reactance path through connected grounding transformer.
    x_ground = Reactance
    # True if primary winding tap changer has reverse regulation capability.
    rev_reg_p = db.BooleanProperty()
    # Tertiary winding line drop compensation resistance.
    line_drp_rt = Resistance
    # Tertiary winding line drop compensation reactance.
    line_drp_xt = Reactance
    # True if tertiary winding tap changer has reverse regulation capability.
    rev_reg_t = db.BooleanProperty()
    # Impedance Primary to Secondary.
    impedance_hx = Impedance
    # Details on winding, allowing to specify winding code such as DYn11, DYn1 or DY11.
    winding_code = db.ReferenceProperty()
    # The 'transformer_type_assets' property has been implicitly created by
    # the transformer_info' property of TransformerTypeAsset.
    pass
    # The 'transformer_assets' property has been implicitly created by
    # the transformer_info' property of TransformerAsset.
    pass
    # The 'transformer_asset_models' property has been implicitly created by
    # the transformer_info' property of TransformerAssetModel.
    pass

class ComEquipmentAsset(AssetContainer):
    """ Communicaiton equipment, other than media, such as gateways, routers, controllers, etc.
    """

    # The 'device_functions' property has been implicitly created by
    # the com_equipment_asset' property of DeviceFunction.
    pass

class ConductorType(IdentifiedObject):
    """ Wire or cable conductor (per IEEE specs). A specific type of wire or combination of wires not insulated from one another, suitable for carrying electric current. It may be bare or insulated.
    """

    # Reactance of the sheath for cable conductors.
    sheath_reactance = Reactance
    # Resistance of the sheath for cable conductors.
    sheath_resistance = Resistance
    # The 'wire_arrangements' property has been implicitly created by
    # the conductor_type' property of WireArrangement.
    pass
    # The 'linear_conductor_assets' property has been implicitly created by
    # the conductor_type' property of LinearConductorAsset.
    pass
    # The 'conductors' property has been implicitly created by
    # the conductor_type' property of Conductor.
    pass
#    linear_conductro_type_asset = db.ReferenceProperty()

class WireType(IdentifiedObject):
    """ Wire conductor (per IEEE specs). A specific type of wire or combination of wires, not insulated from each other, suitable for carrying electrical current.
    """

    # Geometric Mean Radius. If we replace the conductor by a thin walled tube of radius GMR, then its reactance is identical to the reactance of the actual conductor.
    g_mr = Length
    # The resistance per unit length of the conductor
    resistance = Resistance
    # Current carrying capacity of a wire or cable under stated thermal conditions
    rated_current = CurrentFlow
    # Distance between conductor strands in a (symmetrical) bundle.
    phase_conductor_spacing = Length
    # The radius of the conductor
    radius = Length
    # Number of conductor strands in the (symmetrical) bundle (1-12)
    phase_conductor_count = db.IntegerProperty()
    # The 'wire_arrangements' property has been implicitly created by
    # the wire_type' property of WireArrangement.
    pass

class BushingInsulationPF(IdentifiedObject):
    """ Bushing insulation power factor condition as a result of a test. Typical status values are: Acceptable, Minor Deterioration or Moisture Absorption, Major Deterioration or Moisture Absorption, Failed.
    """

    # Kind of test for this bushing.
    test_kind = BushingInsulationPfTestKind
    status = db.ReferenceProperty()
#    transformer_observation = db.ReferenceProperty()
#    bushing_asset = db.ReferenceProperty()

class CurrentTransformerInfo(ElectricalInfo):
    """ Used to define either the required additional electrical properties of a type of Current Transformer (CT) or a CT Model.
    """

    # Full load secondary (FLS) rating for tertiary winding.
    tertiary_fls_rating = CurrentFlow
    # Full load secondary (FLS) rating for secondary winding.
    secondary_fls_rating = CurrentFlow
    # Full load secondary (FLS) rating for primary winding.
    primary_fls_rating = CurrentFlow
    # Ratio for the secondary winding tap changer.
    secondary_ratio = db.ReferenceProperty()
    # Ratio for the tertiary winding tap changer.
    tertiary_ratio = db.ReferenceProperty()
    # Ratio for the primary winding tap changer.
    primary_ratio = db.ReferenceProperty()
    # The 'current_transformer_assert_models' property has been implicitly created by
    # the current_transformer_info' property of CurrentTransformerAssetModel.
    pass
#    current_transformer_type_asset = db.ReferenceProperty()
    # The 'current_transformer_assets' property has been implicitly created by
    # the current_transformer_info' property of CurrentTransformerAsset.
    pass

class OrgAssetRole(Role):
    """ The roles played between an Organisations and an Asset.
    """

    # If the role type is 'owner,' this indicate the percentage of ownership.
    percent_ownership = db.FloatProperty()
#    erp_organisation = db.ReferenceProperty()
#    asset = db.ReferenceProperty()

class Vehicle(Asset):
    """ A vehicle is a type of utility asset.
    """

    # Odometer reading of this vehicle as of the 'odometerReadingDateTime'. Refer to associated ActivityRecords for earlier readings.
    odometer_reading = Length
    # Date and time the last odometer reading was recorded.
    odometer_read_date_time = db.DateProperty()
    # The general categorization type of vehicle as categorized by the utility's asset management standards and practices. Note: (1) Vehicle model is defined by VehicleAssetModel, and (2) Specific people and organizations and their roles relative to this vehicle may be determined by the inherited Asset-ErpPerson and Asset-Organization associations.
    usage_kind = VehicleUsageKind
#    vehicle_asset_model = db.ReferenceProperty()
#    crew = db.ReferenceProperty()

class AssetPropertyCurve(Curve):
    """ An Asset Property that is described through curves rather than as a data point. The relationship is to be defined between an independent variable (X-axis) and one or two dependent variables (Y1-axis and Y2-axis).
    """

#    assets = db.ListProperty(db.Key)

#    @property
#    def asset_property_curves(self):
#        return Asset.gql("WHERE assets = :1", self.key())
#    specification = db.ReferenceProperty()

class Tool(Asset):
    """ Utility asset typically used by utility resources like crews and persons. As is the case for other assets, tools must be maintained.
    """

    # Date the tool was last caibrated, if applicable.
    last_calibration_date = AbsoluteDate
#    crew = db.ReferenceProperty()
#    tool_asset_model = db.ReferenceProperty()

class FailureEvent(ActivityRecord):
    """ An event where an asset has failed to perform its functions within specified parameters.
    """

    # The method used for locating the faulted part of the asset. For example, cable options include: Cap Discharge-Thumping, Bridge Method, Visual Inspection, Other.
    fault_locating_method = db.StringProperty()
    # How the asset failure was isolated from the system.
    failure_isolation_method = FailureIsolationMethodKind
    # Code for asset failure.
    corporate_code = db.StringProperty()
    # Failure location on an object.
    location = db.StringProperty()

class TransformerObservation(IdentifiedObject):
    """ Common information captured during transformer inspections and/or diagrnotics. Note that some properties may be measured through other means and therefore have measurement values in addition to the observed values recorded here.
    """

    # Frequency Response Analysis. Typical values are: acceptable, slight movement, significant movement, failed, near failure. A graphic of the response diagram, which is a type of document, may be associated with this analysis through the recursive document relationship of the ProcedureDataSet.
    freq_resp = db.StringProperty()
    # Top oil temperature.
    top_oil_temp = Temperature
    # Bushing temperature.
    bushing_temp = Temperature
    # Hotspot oil temperature.
    hot_spot_temp = Temperature
    # Oil Quality Analysis-Dielectric Strength.
    oil_dielectric_strength = Voltage
    # Dissolved Gas Analysis. Typical values are: Acceptable, Overheating, Corona, Sparking, Arcing.
    dga = db.StringProperty()
    # Pump vibration, with typical values being: nominal, high.
    pump_vibration = db.StringProperty()
    # Overall measure of furfural in oil and mechanical strength of paper. DP, the degree of polymerization, is the strength of the paper. Furfural is a measure of furfural compounds, often expressed in parts per million.
    furfural_dp = db.StringProperty()
    # Water Content expressed in parts per million.
    water_content = db.StringProperty()
    # Oil Quality Analysis-Neutralization Number - Number - Mg KOH.
    oil_neutralization_number = db.StringProperty()
    # The level of oil in the transformer.
    oil_level = db.StringProperty()
    # Oil Quality Analysis-Color.
    oil_color = db.StringProperty()
    # Oil Quality Analysis- inter facial tension (IFT) - number-Dynes/CM.
    oil_ift = db.StringProperty()
    status = db.ReferenceProperty()
#    procedure_data_sets = db.ListProperty(db.Key)

#    @property
#    def transformer_observations(self):
#        return ProcedureDataSet.gql("WHERE procedure_data_sets = :1", self.key())
    # The 'winding_insulation_pfs' property has been implicitly created by
    # the transformer_observation' property of WindingInsulation.
    pass
    # The 'bushing_insultation_pfs' property has been implicitly created by
    # the transformer_observation' property of BushingInsulationPF.
    pass
#    transformer_asset = db.ReferenceProperty()
#    winding_tests = db.ListProperty(db.Key)

#    @property
#    def transformer_observations(self):
#        return WindingTest.gql("WHERE winding_tests = :1", self.key())

class CompositeSwitchInfo(IdentifiedObject):
    """ Properties of a composite switch.
    """

    # Supported number of phases, typically 0, 1 or 3.
    phase_count = db.IntegerProperty()
    # True if multi-phase switch controls all phases concurrently.
    gang = db.BooleanProperty()
    # True if device is capable of being operated by remote control.
    remote = db.BooleanProperty()
    # Rated voltage.
    rated_voltage = Voltage
    # Breaking capacity, or short circuit rating, is the maximum rated current which the device can safely interrupt at the rated voltage.
    interrupting_rating = CurrentFlow
    # Phases carried, if applicable.
    phase_code = PhaseCode
    # Number of switch states represented by the composite switch.
    switch_state_count = db.IntegerProperty()
    # Initial operating mode, with the following values: Automatic, Manual.
    init_op_mode = db.StringProperty()
#    composite_switch_type_asset = db.ReferenceProperty()
#    composite_switch_asset_model = db.ReferenceProperty()
    # The 'composite_switch_assets' property has been implicitly created by
    # the composite_switch_info' property of CompositeSwitchAsset.
    pass

class AssetPsrRole(Role):
    """ Roles played between Assets and Power System Resources.
    """

#    asset = db.ReferenceProperty()
#    power_system_resource = db.ReferenceProperty()

class PSRStatus(IdentifiedObject):
    """ The current status of the PowerSystemResource. History of the status is tracked through instances of ActivityRecord.
    """

    status = db.ReferenceProperty()
#    power_system_resource = db.ReferenceProperty()

class WorkEquipmentAsset(Asset):
    """ Various equipment used to perform units of work by crews, office staff, etc.
    """

#    crew = db.ReferenceProperty()
#    work_equipment_asset_model = db.ReferenceProperty()
    # The 'usages' property has been implicitly created by
    # the work_equipment_asset' property of Usage.
    pass

class DuctBank(Asset):
    """ A duct bank may contain many ducts. Each duct contains individual lines that are expressed as linear assets (thereby describing each line's physical asset characteristics), which are each associated with ACLineSegments and other classes describing their electrical characteristics.
    """

    # Number of ducts in duct bank.
    duct_count = db.IntegerProperty()
    # Number of circuits in duct bank. Refer to associations between a duct (LinearAsset) and an ACLineSegment to understand which circuits are in which ducts.
    circuit_count = db.IntegerProperty()
#    duct_band_type_asset = db.ReferenceProperty()
#    cable_assets = db.ListProperty(db.Key)

#    @property
#    def duct_banks(self):
#        return CableAsset.gql("WHERE cable_assets = :1", self.key())

class WindingInfo(Element):
    """ Details on winding. For example, to express winding code 'DYn11', set attributes as follows: 'windingConnectionKind' = Yn and 'phaseAngle' = 11.
    """

    # Kind of winding connection.
    winding_connection_kind = WindingConnection
    # Winding phase angle where 360 degrees are represented with clock hours, so the valid values are {0, ..., 11}.
    phase_angle = db.IntegerProperty()

class FinancialInfo(IdentifiedObject):
    """ Various current financial properties associated with a particular asset. Historical properties may be determined by ActivityRecords associated with the asset.
    """

    # The quantity of the asset if per unit length, for example conductor.
    quantity = IntegerQuantity
    # Date asset's financial value was put in plant for regulatory accounting purposes (e.g., for rate base calculations). This is sometime referred to as the 'in-service date.'
    plant_transfer_date = db.DateProperty()
    # Date warranty on asset expires.
    warranty_date = db.DateProperty()
    # Purchase order identifier.
    purchase_order_number = db.StringProperty()
    # Description of the cost.
    cost_description = db.StringProperty()
    # The actual purchase cost of this particular asset.
    actual_purchase_cost = Money
    # Value of asset as of 'valueDate'.
    financial_value = Money
    # The category of cost to which this Material Item belongs.
    cost_type = db.StringProperty()
    # The account to which this actual material item is charged.
    account = db.StringProperty()
    # The date and time at which the financial value was last established.
    value_date = db.DateProperty()
    # Date asset was purchased.
    purchase_date = db.DateProperty()
#    asset = db.ReferenceProperty()

class Anchor(StructureSupport):
    """ A type of support for structures, used to hold poles secure.
    """

    # Kind of this anchor.
    kind = AnchorKind

class PotentialTransformerAsset(ElectricalAsset):
    """ Physical asset performing Potential Transformer (PT) function.
    """

#    potential_transformer_info = db.ReferenceProperty()
#    potential_transformer = db.ReferenceProperty()
#    potential_transformer_asset_model = db.ReferenceProperty()

class RecloserAsset(ElectricalAsset):
    """ Physical recloser performing a reclosing function, which is modeled through Breaker.
    """

#    recloser_asset_model = db.ReferenceProperty()
#    recloser_info = db.ReferenceProperty()

class CurrentTransformerAsset(ElectricalAsset):
    """ Physical asset performing Current Transformer (CT) function.
    """

    # Type of CT as categorized by the utility's asset management standards and practices.
    type_ct = db.StringProperty()
#    current_transformer = db.ReferenceProperty()
#    current_transformer_info = db.ReferenceProperty()
#    current_transformer_asset_model = db.ReferenceProperty()

class Streetlight(ElectricalAsset):
    """ Streetlight asset.
    """

    # Length of arm of this specific asset. Note that a new light may be placed on an existing arm.
    arm_length = Length
    # Lamp kind currently installed.
    lamp_kind = StreetlightLampKind
    # Actual power rating of light.
    light_rating = ActivePower
#    attached_to_pole = db.ReferenceProperty()
#    streetlight_asset_model = db.ReferenceProperty()

class LinearConductorAsset(ElectricalAsset):
    """ Physical asset used to perform the conductor's role.
    """

    # True when orientation is horizontal (e.g., transmission and distribution lines), false if vertical (e.g. a riser for underground to overhead service).
    is_horizontal = db.BooleanProperty()
    # True if linear asset has an insulator around the core material.
    insulated = db.BooleanProperty()
    # Description of the method used for grounding the linear conductor. For a cable, the grounding/bonding shield may be multi-point, single-point, cross cable, or other.
    grounding_method = db.StringProperty()
#    circuit_section = db.ReferenceProperty()
#    conductor_type = db.ReferenceProperty()
#    linear_conductor_type_asset = db.ReferenceProperty()
#    conductors = db.ListProperty(db.Key)

#    @property
#    def linear_conductor_assets(self):
#        return Conductor.gql("WHERE conductors = :1", self.key())
#    linear_conductor_asset_model = db.ReferenceProperty()

class ProtectionEquipmentAsset(ElectricalAsset):
    """ Physical asset performing ProtectionEquipment function.
    """

    # Actual phase trip for this type of relay, if applicable.
    phase_trip = CurrentFlow
    # Actual ground trip for this type of relay, if applicable.
    ground_trip = CurrentFlow
#    protection_equipment_asset_model = db.ReferenceProperty()

class Pole(Structure):
    """ A long, slender piece of wood, metal, etc. usually rounded that stands vertically from the ground and is used for mounting various types of overhead equipment. Dimensions of Pole are specified in associated DimensionsInfo.
    """

    # Kind of base for this pole.
    base_kind = PoleBaseKind
    # Kind of treatment for this pole.
    treatment_kind = PoleTreatmentKind
    # True if a block of material has been attached to base of pole in ground for stability. This technique is used primarily when anchors can not be used.
    breast_block = db.BooleanProperty()
    # Joint pole agreement reference number.
    jpa_reference = db.StringProperty()
    # Date pole was last treated with preservative.
    treated_date = db.DateProperty()
    # Kind of preservative for this pole.
    preservative_kind = PolePreservativeKind
    # The framing structure mounted on the pole.
    construction = db.StringProperty()
    # The 'support_streetlights' property has been implicitly created by
    # the attached_to_pole' property of Streetlight.
    pass
#    pole_model = db.ReferenceProperty()

class CableAsset(LinearConductorAsset):
    """ Insultated physical cable for performing the Conductor role used in undergrond and other applications..
    """

#    duct_bank_type_asset = db.ReferenceProperty()
#    duct_banks = db.ListProperty(db.Key)

#    @property
#    def cable_assets(self):
#        return DuctBank.gql("WHERE duct_banks = :1", self.key())

class FACTSDeviceAsset(ElectricalAsset):
    """ Physical asset used to perform the FACTSDevice's role.
    """

    # Kind of FACTS device.
    kind = FactsDeviceKind
#    factsdevice_asset_model = db.ReferenceProperty()

class TestDataSet(ProcedureDataSet):
    """ Test results, usually obtained by a lab or other independent organisation.
    """

    # Conclusion drawn from test results.
    conclusion = db.StringProperty()
    # The date the specimen was received by the lab.
    spec_to_lab_date = db.DateProperty()
    # Identifier of specimen used in inspection or test.
    specimen_id = db.StringProperty()
    # The date the conclusion form the test was issued by the lab.
    conclusion_date = db.DateProperty()

class FaultIndicatorAsset(ElectricalAsset):
    """ Physical asset performing FaultIndicator function.
    """

#    fault_indicator_asset_model = db.ReferenceProperty()
#    fault_indicator = db.ReferenceProperty()

class TransformerAsset(ElectricalAsset):
    """ A specific physical (vs. logical) transformer.
    """

    # 24-hour overload rating.
    day_over_load_rating = ApparentPower
    # Nominal voltage rating for alternate configuration for secondary winding.
    alt_secondary_nom_voltage = Voltage
    # Function of this transformer.
    function = TransformerFunctionKind
    # True if windings can be re-configured to result in a different input or output voltage.
    reconfig_winding = db.BooleanProperty()
    # Nominal voltage rating for alternate configuration for primary winding.
    alt_primary_nom_voltage = Voltage
    # Kind of construction for this transformer.
    construction_kind = TransformerConstructionKind
    # 1-hour overload rating.
    hour_over_load_rating = ApparentPower
    # Date and time this asset was last reconditioned or had a major overhaul.
    reconditioned_date_time = db.DateProperty()
    # The 'transformer_observations' property has been implicitly created by
    # the transformer_asset' property of TransformerObservation.
    pass
#    transformer_asset_model = db.ReferenceProperty()
#    power_ratings = db.ListProperty(db.Key)

#    @property
#    def transformer_assets(self):
#        return PowerRating.gql("WHERE power_ratings = :1", self.key())
#    transformer_info = db.ReferenceProperty()

class OverheadConductorAsset(LinearConductorAsset):
    """ Physical conductor performing the Conductor role that is used in overhead applications.
    """

#    mounting_point = db.ReferenceProperty()

class BusbarAsset(ElectricalAsset):
    """ Physical asset used to perform the BusbarSection's role.
    """

#    busbar_asset_model = db.ReferenceProperty()

class SeriesCompensatorAsset(ElectricalAsset):
    """ For a a series capacitor or reactor, this is the physical asset performing the SeriesCompensator role (PSR).
    """

#    series_compensator_asset_model = db.ReferenceProperty()

class SurgeProtectorAsset(ElectricalAsset):
    """ Physical asset performing SurgeProtector function.
    """

#    surge_protector = db.ReferenceProperty()
#    surge_protector_asset_model = db.ReferenceProperty()

class UndergroundStructure(Structure):
    """ Abstract class for underground structures. Typical structure types are: BURD, Enclosure, Hand Hole, Manhole, Pad/Slab, Subsurface Enclosure, Trench, Tunnel, Vault, Pull/Splice Box.
    """

    # Date vault was sealed.
    sealing_date = AbsoluteDate
    # Date sealing warranty expires.
    sealing_warranty_expires = AbsoluteDate
    # Primary material of underground structure.
    material = db.StringProperty()
    # True if vault is ventilating.
    ventilation = db.BooleanProperty()

class GeneratorAsset(ElectricalAsset):
    """ Physical asset performing the Generator role.
    """

#    generator_asset_model = db.ReferenceProperty()

class BreakerInfo(SwitchInfo):
    """ Properties of breakers.
    """

    # Phase trip rating.
    phase_trip = CurrentFlow
    # The 'breaker_asset_models' property has been implicitly created by
    # the breaker_info' property of BreakerAssetModel.
    pass
    # The 'breaker_assets' property has been implicitly created by
    # the breaker_info' property of BreakerAsset.
    pass
#    breaker_type_asset = db.ReferenceProperty()

class RecloserInfo(SwitchInfo):
    """ Properties of reclosers.
    """

    # True if normal status of ground trip is enabled.
    ground_trip_normal_enabled = db.BooleanProperty()
    # Phase trip rating.
    phase_trip_rating = CurrentFlow
    # True if device has ground trip capability.
    ground_trip_capable = db.BooleanProperty()
    # Ground trip rating.
    ground_trip_rating = CurrentFlow
    # Total number of phase reclose operations.
    reclose_lockout_count = db.IntegerProperty()
    # The 'recloser_assets' property has been implicitly created by
    # the recloser_info' property of RecloserAsset.
    pass
    # The 'recloser_asset_models' property has been implicitly created by
    # the recloser_info' property of RecloserAssetModel.
    pass
#    recloser_type_asset = db.ReferenceProperty()

class Tower(Structure):
    """ Large structure used to carry transmission lines, subtransmission lines, and/or other equipment/lines (e.g., communication). Dimensions of the Tower are specified in associated DimensionsInfo class.
    """

    # Construction structure on the tower.
    construction_kind = TowerConstructionKind
#    tower_asset_model = db.ReferenceProperty()

class JointAsset(ElectricalAsset):
    """ Physical asset connecting two or more cable assets. It includes the portion of cable under wipes, welds, or other seals.
    """

    # Configuration of joint.
    configuration_kind = JointConfigurationKind
    # Material used to fill the joint.
    fill_kind = JointFillKind
    # The type of insulation around the joint, classified according to the utility's asset management standards and practices.
    insulation = db.StringProperty()

class SwitchAsset(ElectricalAsset):
    """ Physical asset performing Switch function.
    """

#    switch_info = db.ReferenceProperty()
#    switch_asset_model = db.ReferenceProperty()

class BushingAsset(ElectricalAsset):
    """ Physical bushing that insulates and protects from abrasion a conductor that passes through it. It is associated with a specific Terminal, which is in turn associated with a ConductingEquipment.
    """

    # Factory Measured Insulation Power Factor measured between the Power Factor tap and the bushing conductor.
    c1_power_factor = db.FloatProperty()
    # Factory Measured Capacitance measured between the Power Factor tap and the bushing conductor.
    c1_capacitance = Capacitance
    # Factory Measured Capacitance measured between the Power Factor tap and ground.
    c2_capacitance = Capacitance
    # Factory Measured Insulation Power Factor measured between the Power Factor tap and ground.
    c2_power_factor = db.FloatProperty()
    # The 'bushing_insulation_pfs' property has been implicitly created by
    # the bushing_asset' property of BushingInsulationPF.
    pass
#    terminal = db.ReferenceProperty()
#    bushing_model = db.ReferenceProperty()

class BreakerAsset(ElectricalAsset):
    """ Physical asset performing Breaker role.
    """

#    breaker_asset_model = db.ReferenceProperty()
#    breaker_info = db.ReferenceProperty()

class ShuntCompensatorAsset(ElectricalAsset):
    """ For a shunt capacitor or reactor or switchable bank of shunt capacitors or reactors, this is the physical asset performing the ShuntCompensator role (PSR).
    """

#    shunt_compensator_asset_model = db.ReferenceProperty()
#    shunt_impedance_info = db.ReferenceProperty()

class SVCAsset(FACTSDeviceAsset):
    """ Physical asset performing StaticVarCompensator function.
    """

#    svc_info = db.ReferenceProperty()
#    svcasset_model = db.ReferenceProperty()

class ResistorAsset(ElectricalAsset):
    """ Physical asset performing Resistor function.
    """

#    resistor = db.ReferenceProperty()
#    resistor_asset_model = db.ReferenceProperty()

class Guy(StructureSupport):
    """ A type of support for structures.
    """

    pass

class Manhole(UndergroundStructure):
    """ Provides access at key locations to underground cables, equipment, etc. housed inside a protective vault.
    """

    pass


