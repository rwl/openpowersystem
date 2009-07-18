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

from cim14.iec61968.informative.inf_common import Role
from cim14.iec61970.core import IdentifiedObject
from cim14.iec61968.common import Document

from cim14.iec61970.domain import Length
from cim14.iec61970.domain import ActivePower
from cim14.iec61970.domain import Reactance
from cim14.iec61970.domain import Resistance
from cim14.iec61970.domain import ReactivePower
from cim14.iec61970.domain import ApparentPower
from cim14.iec61970.domain import PerCent
from cim14.iec61970.domain import AngleDegrees
from cim14.iec61970.domain import Seconds
from cim14.iec61970.domain import CurrentFlow
from cim14.iec61970.domain import Voltage
from cim14.iec61970.domain import StringQuantity
from cim14.iec61970.domain import Money
from cim14.iec61970.core import PhaseCode

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

FaultIndicatorResetKind = db.StringProperty(choices=("remote", "automatic", "other", "manual"))

ns_prefix = "cim.IEC61968.Informative.InfTypeAsset"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#IEC61968.Informative.InfTypeAsset"

class ElecAMElecPropRole(Role):
    """ ElectricalAssetModel - ElectrialProperties Role. Used to define what the properties refers to in the AssetModel. e.g. for a Transformer, it will have an association to an instance of ElectricalProperties for each Winding, with the roleType defining whether it is the primary, secondary, tertiary, quartiary winding.
    """

#    electrical_asset_model = db.ReferenceProperty()
#    electrical_info = db.ReferenceProperty()

class Connection(IdentifiedObject):
    """ A structure can have multiple connection points for electrical connections (e.g. line) each with multiple mounting points, one for each phase. e.g. a Tower may have three Connections, two with three mounting points, one for each phase and a third with a single mounting point for the neutral line. A pole, on the other hand, may have a single Connection with one, two or three mounting points depending on whether it is carrying 1,2 or 3 phases.
    """

#    structure_type_assets = db.ListProperty(db.Key)

#    @property
#    def mount_connections(self):
#        return StructureTypeAsset.gql("WHERE structure_type_assets = :1", self.key())
#    mounting_points = db.ListProperty(db.Key)

#    @property
#    def connections(self):
#        return MountingPoint.gql("WHERE mounting_points = :1", self.key())

class ElecTAElecPropRole(Role):
    """ ElectricalTypeAsset - ElectrialProperties Role. Used to define what the properties refers to in the TypeAsset. e.g. for a Transformer, it will have an association to an instance of ElectricalProperties for each Winding, with the roleType defining whether it is the primary, secondary, tertiary, quartiary winding.
    """

#    electrical_type_asset = db.ReferenceProperty()
#    electrical_info = db.ReferenceProperty()

class TypeAsset(Document):
    """ Whereas an AssetModel is a particular model and version of a vendor's product, a TypeAsset is documentation for a generic asset or material item that may be used for design purposes. Any number of AssetModels may be used to perform this generic function. The primary role of the TypeAsset is typically defined by the PowereSystemResource it is associated with.
    """

    # True if item is a stock item (default).
    stock_item = db.BooleanProperty()
    # The value, unit of measure, and multiplier for the quantity.
    quantity = StringQuantity
    # Estimated unit cost (or cost per unit length) of the this type of asset. It does not include labor to install/construct or configure it.
    estimated_unit_cost = Money
    # The 'erp_req_line_items' property has been implicitly created by
    # the type_asset' property of ErpReqLineItem.
    pass
    # The 'asset_models' property has been implicitly created by
    # the type_asset' property of AssetModel.
    pass
    # The 'erp_bom_item_datas' property has been implicitly created by
    # the type_asset' property of ErpBomItemData.
    pass
#    type_asset_catalogue = db.ReferenceProperty()
    # The 'erp_inventory_issues' property has been implicitly created by
    # the type_asset' property of ErpIssueInventory.
    pass
#    cuwork_equipment_asset = db.ReferenceProperty()
#    cuasset = db.ReferenceProperty()

class MountingPoint(IdentifiedObject):
    """ Point on a structure that a connection may have a conductor connected to. Defined with an x and y coordinate plus a phase. A connection may have multiple mounting points, one for each phase.
    """

    x_coord = db.IntegerProperty()
    phase_code = PhaseCode
    y_coord = db.IntegerProperty()
#    connections = db.ListProperty(db.Key)

#    @property
#    def mounting_points(self):
#        return Connection.gql("WHERE connections = :1", self.key())
    # The 'overhead_conductors' property has been implicitly created by
    # the mounting_point' property of OverheadConductorAsset.
    pass

class TypeAssetCatalogue(IdentifiedObject):
    """ Catalogue of generic types of assets (TypeAsset) that may be used for design purposes. It is not associated with a particular manufacturer.
    """

    status = db.ReferenceProperty()
    # The 'type_assets' property has been implicitly created by
    # the type_asset_catalogue' property of TypeAsset.
    pass

class ToolTypeAsset(TypeAsset):
    """ Documentation for a generic tool that may be used for various purposes such as work planning.
    """

    # The 'tool_asset_models' property has been implicitly created by
    # the tool_type_asset' property of ToolAssetModel.
    pass

class AssetFunctionTypeAsset(TypeAsset):
    """ Documentation for a generic Asset Function that may be used for various purposes such as work planning.
    """

    # The 'asset_function_asset_models' property has been implicitly created by
    # the asset_function_type_asset' property of AssetFunctionAssetModel.
    pass

class SubstationTypeAsset(TypeAsset):
    """ Documentation for a type of substation that may be used for design purposes.
    """

    pass

class WorkEquipmentTypeAsset(TypeAsset):
    """ Documentation for generic equipment that may be used for various purposes such as work planning.
    """

    # The 'work_equipment_asset_models' property has been implicitly created by
    # the work_equipment_type_asset' property of WorkEquipmentAssetModel.
    pass

class ComEquipmentTypeAsset(TypeAsset):
    """ Documentation for a piece of Communication Equipment (e.g., gateway, router, network hub, etc.) that may be used for design purposes.
    """

    pass

class VehicleTypeAsset(TypeAsset):
    """ Documentation for a generic vehicle that may be used for various purposes such as work planning.
    """

    # The 'vehicle_asset_models' property has been implicitly created by
    # the vehicle_type_asset' property of VehicleAssetModel.
    pass

class EndDeviceTypeAsset(TypeAsset):
    """ Documentation for generic End Device that may be used for various purposes such as work planning.
    """

    # The 'end_device_models' property has been implicitly created by
    # the end_device_type_asset' property of EndDeviceModel.
    pass

class ElectricalTypeAsset(TypeAsset):
    """ Generic TypeAsset for all types of component in the network that have electrical characteristics.
    """

    # The 'electrical_info_roles' property has been implicitly created by
    # the electrical_type_asset' property of ElecTAElecPropRole.
    pass

class ProtectionEquipmentTypeAsset(ElectricalTypeAsset):
    """ Documentation for generic protection equiment that may be used for design purposes.
    """

    # Default ground trip setting for this type of relay, if applicable.
    default_ground_trip = CurrentFlow
    # Default phase trip setting for this type of relay, if applicable.
    default_phase_trip = CurrentFlow
    # The 'protection_equipment_asset_models' property has been implicitly created by
    # the protection_equipment_type_asset' property of ProtectionEquipmentAssetModel.
    pass

class BreakerTypeAsset(ElectricalTypeAsset):
    """ Documentation for a generic breaker asset that may be used for design purposes.
    """

#    breaker_info = db.ReferenceProperty()
    # The 'breaker_asset_models' property has been implicitly created by
    # the breaker_type_asset' property of BreakerAssetModel.
    pass

class TransformerTypeAsset(ElectricalTypeAsset):
    """ Documentation for generic transformers that may be used for various purposes such as work planning. The operating voltages can be found via the ElectricalProperties class. e.g. a two winding transformer will have two instances of ElectricalProperties and the primary/secondaryWinding can be found from the ratedKV attributes of each and the ElecTAElecPropRole used to define which is the primaryWinding and which is the secondaryWinding.
    """

    # Maximum loss of power in the transformer core.
    core_loss = ApparentPower
    # Number of windings.
    winding_count = db.IntegerProperty()
    # The 'transformer_asset_models' property has been implicitly created by
    # the transformer_type_asset' property of TransformerAssetModel.
    pass
#    transformer_info = db.ReferenceProperty()

class BushingTypeAsset(ElectricalTypeAsset):
    """ Documentation for a generic bushing that may be used for various purposes such as work planning.
    """

    # The 'bushing_models' property has been implicitly created by
    # the bushing_type_asset' property of BushingModel.
    pass

class StructureTypeAsset(TypeAsset):
    """ A Type of Structural Asset with properties common to a large number of asset models.
    """

    # Maximum rated voltage of the equipment that can be mounted on/contained within the structure.
    rated_voltage = Voltage
#    mount_connections = db.ListProperty(db.Key)

#    @property
#    def structure_type_assets(self):
#        return Connection.gql("WHERE mount_connections = :1", self.key())

class CompositeSwitchTypeAsset(TypeAsset):
    """ Documentation for a generic composite switch asset that may be used for design purposes. A composite wwitch is an amalgamation of multiple Switches.
    """

    # The 'composite_switch_asset_models' property has been implicitly created by
    # the composite_switch_type_asset' property of CompositeSwitchAssetModel.
    pass
    # The 'switch_types_assets' property has been implicitly created by
    # the composite_switch_type_asset' property of SwitchTypeAsset.
    pass
#    composite_switch_info = db.ReferenceProperty()

class DuctTypeAsset(StructureTypeAsset):
    """ A Duct contains underground cables and is contained within a duct bank. The xCoord and yCoord attributes define its positioning within the DuctBank.
    """

    # Y position of the duct within the duct bank.
    y_coord = db.IntegerProperty()
    # X position of the duct within the duct bank.
    x_coord = db.IntegerProperty()
    # The 'cable_assets' property has been implicitly created by
    # the duct_bank_type_asset' property of CableAsset.
    pass
#    duct_bank_type_asset = db.ReferenceProperty()

class CabinetTypeAsset(StructureTypeAsset):
    """ Documentation for a generic cabinet that may be used for various purposes such as work planning.
    """

    # The 'cabinet_models' property has been implicitly created by
    # the cabinet_type_asset' property of CabinetModel.
    pass

class SurgeProtectorTypeAsset(ElectricalTypeAsset):
    """ Documentation for a generic surge arrestor that may be used for design purposes.
    """

    maximum_energy_absorption = db.FloatProperty()
    maximum_continous_operating_voltage = Voltage
    maximum_current_rating = CurrentFlow
    nominal_design_voltage = Voltage
    # The 'surge_protectors' property has been implicitly created by
    # the surge_protector_type_asset' property of SurgeProtector.
    pass
    # The 'surge_protector_asset_models' property has been implicitly created by
    # the surge_protector_type_asset' property of SurgeProtectorAssetModel.
    pass

class CurrentTransformerTypeAsset(ElectricalTypeAsset):
    """ Documentation for a generic Current Transformer (CT) that may be used for various purposes such as work planning.
    """

    ct_class = db.StringProperty()
    # Maximum primary current where the CT still displays linear characteristicts.
    knee_point_current = CurrentFlow
    # CT accuracy classification
    accuracy_class = db.StringProperty()
    # Power burden of the CT core
    core_burden = ActivePower
    # Maximum voltage across the secondary terminals where the CT still displays linear characteristicts.
    knee_point_voltage = Voltage
    # Number of cores.
    core_count = db.IntegerProperty()
    # eg. metering, protection, etc
    usage = db.StringProperty()
    accuracy_limit = CurrentFlow
    # Maximum ratio between the primary and secondary current.
    max_ratio = db.ReferenceProperty()
    # Nominal ratio between the primary and secondary current; i.e. 100:5
    nominal_ratio = db.ReferenceProperty()
#    current_transformer_info = db.ReferenceProperty()
    # The 'current_transformers' property has been implicitly created by
    # the current_transformer_type_asset' property of CurrentTransformer.
    pass
    # The 'current_transformer_asset_models' property has been implicitly created by
    # the current_transformer_type_asset' property of CurrentTransformerAssetModel.
    pass

class TowerTypeAsset(StructureTypeAsset):
    """ Documentation for a generic tower that may be used for various purposes such as work planning. A transmission tower carrying two 3-phase circuits will have 2 instances of Connection, each of which will have 3 MountingPoint instances, one for each phase all with coordinates relative to a common origin on the tower. (It may also have a 3rd Connection with a single MountingPoint for the Neutral line).
    """

    # The 'tower_asset_models' property has been implicitly created by
    # the tower_type_asset' property of TowerAssetModel.
    pass

class RecloserTypeAsset(ElectricalTypeAsset):
    """ Documentation for a generic recloser asset that may be used for design purposes.
    """

    # The 'recloser_asset_models' property has been implicitly created by
    # the recloser_type_asset' property of RecloserAssetModel.
    pass
#    recloser_info = db.ReferenceProperty()

class PotentialTransformerTypeAsset(ElectricalTypeAsset):
    """ Documentation for a generic Potential Transformer (PT) that may be used for various purposes such as work planning.
    """

    accuracy_class = db.StringProperty()
    pt_class = db.StringProperty()
    nominal_ratio = db.ReferenceProperty()
    # The 'potential_transformers' property has been implicitly created by
    # the potential_transformer_type_asset' property of PotentialTransformer.
    pass
    # The 'potential_transformer_asset_models' property has been implicitly created by
    # the potential_transformer_type_asset' property of PotentialTransformerAssetModel.
    pass
#    potential_transformer_info = db.ReferenceProperty()

class DuctBankTypeAsset(StructureTypeAsset):
    """ A DuctBank contains multiple Ducts. The DuctBank itself should have no connections, since these are defined by the individual ducts within it. However, it will have a ConstructionType and the material it is constructed from.
    """

    # The 'duct_banks' property has been implicitly created by
    # the duct_band_type_asset' property of DuctBank.
    pass
    # The 'duct_type_assets' property has been implicitly created by
    # the duct_bank_type_asset' property of DuctTypeAsset.
    pass

class FaultIndicatorTypeAsset(ElectricalTypeAsset):
    """ Documentation for a generic fault indicator that may be used for design purposes.
    """

    # Kind of reset mechanisim of this fault indicator.
    reset_kind = FaultIndicatorResetKind
    # The 'fault_indicators' property has been implicitly created by
    # the fault_indicator_type_asset' property of FaultIndicator.
    pass
    # The 'fault_indicator_asset_models' property has been implicitly created by
    # the fault_indicator_type_asset' property of FaultIndicatorAssetModel.
    pass

class SwitchTypeAsset(ElectricalTypeAsset):
    """ Documentation for a generic switch asset that may be used for design purposes.
    """

    # The 'switch_asset_models' property has been implicitly created by
    # the switch_type_asset' property of SwitchAssetModel.
    pass
#    composite_switch_type_asset = db.ReferenceProperty()
#    switch_info = db.ReferenceProperty()

class SeriesCompensatorTypeAsset(ElectricalTypeAsset):
    """ Documentation for a generic series compensator that may be used for design purposes.
    """

    # The 'shunt_compensator_asset_models' property has been implicitly created by
    # the shunt_compensator_type_asset' property of SeriesCompensatorAssetModel.
    pass

class GeneratorTypeAsset(ElectricalTypeAsset):
    """ Documentation for generic generation equipment that may be used for various purposes such as work planning. It defines both the Real and Reactive power properties (modelled at the PSR level as a GeneratingUnit + SynchronousMachine)
    """

    # Maximum real power limit.
    max_p = ActivePower
    # Minimum real power generated.
    min_p = ActivePower
    # Quadrature-axis subtransient reactance
    x_quad_subtrans = Reactance
    # Quadrature-axis synchronous reactance
    x_quad_sync = Reactance
    # Direct-axis Transient reactance
    x_direct_trans = Reactance
    # Direct-axis Transient resistance
    r_direct_trans = Resistance
    # Quadrature-axis transient reactance.
    x_quad_trans = Reactance
    # Direct-axis subtransient resistance
    r_direct_subtrans = Resistance
    # Quadrature-axis synchronous resistance
    r_quad_sync = Resistance
    # Direct-axis synchronous resistance
    r_direct_sync = Resistance
    # Quadrature-axis Transient resistance
    r_quad_trans = Resistance
    # Maximum reactive power limit.
    max_q = ReactivePower
    # Minimum reactive power generated.
    min_q = ReactivePower
    # Direct-axis subtransient reactance
    x_direct_subtrans = Reactance
    # Direct-axis synchronous reactance
    x_direct_sync = Reactance
    # Quadrature-axis subtransient resistance
    r_quad_subtrans = Resistance
    # The 'generator_asset_models' property has been implicitly created by
    # the generator_type_asset' property of GeneratorAssetModel.
    pass

class PoleTypeAsset(StructureTypeAsset):
    """ Documentation for a generic pole that may be used for various purposes such as work planning. A pole typically has a single Connection with 1,2 or 3 mounting points.
    """

    # Diameter of the pole.
    diameter = Length
    # Length of the pole (inclusive of any section of the pole that may be underground post-installation).
    length = Length
    # The 'pole_models' property has been implicitly created by
    # the pole_type_asset' property of PoleModel.
    pass

class FACTSDeviceTypeAsset(ElectricalTypeAsset):
    """ Documentation for generic Flexible alternating current transmission systems (FACTS) devices that may be used for various purposes such as work planning.
    """

    # The 'factsdevice_asset_models' property has been implicitly created by
    # the factsdevice_type_asset' property of FACTSDeviceAssetModel.
    pass

class SVCTypeAsset(FACTSDeviceTypeAsset):
    """ Documentation for a generic Static Var Compensator (SVC) that may be used for various purposes such as work planning.
    """

    # The 'svcasset_models' property has been implicitly created by
    # the svctype_asset' property of SVCAssetModel.
    pass
#    svc_infos = db.ListProperty(db.Key)

#    @property
#    def svctype_assets(self):
#        return SVCInfo.gql("WHERE svc_infos = :1", self.key())

class StreetlightTypeAsset(ElectricalTypeAsset):
    """ Documentation for a generic streetlight that may be used for various purposes such as work planning. Use 'category' for utility specific categorisation, such as luminar, grid light, lantern, open bottom, flood, etc.
    """

    # Nominal (as designed) power rating of light.
    light_rating = ActivePower
#    streetlight_asset_models = db.ListProperty(db.Key)

#    @property
#    def streetlight_type_assets(self):
#        return StreetlightAssetModel.gql("WHERE streetlight_asset_models = :1", self.key())

class BusbarTypeAsset(ElectricalTypeAsset):
    """ Documentation for a generic busbar that may be used for design purposes. It is typically associated with PoserSystemResource BusbarSection.
    """

    # The 'busbar_type_assets' property has been implicitly created by
    # the busbar_asset_model' property of BusbarAssetModel.
    pass

class LinearConductorTypeAsset(ElectricalTypeAsset):
    """ Documentation for a generic linear conductor that may be used for various purposes such as work planning. ElectricalProperties are defined as being per unit length (which is defined by 'unitLength').
    """

    # Radius of the conductor
    radius = db.IntegerProperty()
    # True if conductor is insultated.
    insulated = db.BooleanProperty()
    # Commonly referred to size for this type of conductor.
    size = db.StringProperty()
    # Geometric mean radius (GMR): If the conductor were replaced by a thin walled tube of radius with this value, then its reactance would be identical to that of the actual conductor.
    gmr = Length
    # Length of each unit of the LinearConductor which has characteristics defined by the associated ElectricalProperties.
    unit_length = db.IntegerProperty()
#    conductor_type = db.ReferenceProperty()
    # The 'linear_conductor_asset_models' property has been implicitly created by
    # the linear_conductor_type_asset' property of LinearConductorAssetModel.
    pass
#    conductors = db.ListProperty(db.Key)

#    @property
#    def linear_conductor_type_assets(self):
#        return Conductor.gql("WHERE conductors = :1", self.key())
    # The 'linear_conductor_assets' property has been implicitly created by
    # the linear_conductor_type_asset' property of LinearConductorAsset.
    pass

class MeterTypeAsset(ElectricalTypeAsset):
    """ Documentation for a generic meter that may be used for design purposes. Rather than being associated with CustomerMeter, it is associated with EnergyConsumer as it may be used for many applications, such as tie line metering, in addition to customer metering.
    """

    # The 'meter_asset_models' property has been implicitly created by
    # the meter_type_asset' property of MeterAssetModel.
    pass

class ShuntCompensatorTypeAsset(ElectricalTypeAsset):
    """ Documentation for a generic shunt compensator that may be used for design purposes.
    """

    # Maximum allowed Apparent Power loss
    max_power_loss = ApparentPower
#    shunt_impedance_info = db.ReferenceProperty()
    # The 'shunt_compensator_asset_models' property has been implicitly created by
    # the shunt_compensator_type_asset' property of ShuntCompensatorAssetModel.
    pass

class ComFunctionTypeAsset(ElectricalTypeAsset):
    """ Documentation for a generic communication function that may be used for various purposes such as work planning.
    """

    # The 'com_function_asset_models' property has been implicitly created by
    # the com_function_type_asset' property of ComFunctionAssetModel.
    pass

class TapChangerTypeAsset(ElectricalTypeAsset):
    """ Documentation for generic tap changers that may be used for various purposes such as work planning.
    """

    # Tap step increment, in per cent of nominal voltage, per step position.
    step_voltage_increment = PerCent
    # Phase shift, in degrees, per step position
    step_phase_increment = AngleDegrees
    # Highest possible tap step position, advance from neutral
    high_step = db.IntegerProperty()
    # The neutral tap step position for this type of winding.
    neutral_step = db.IntegerProperty()
    # Maximum allowed delay for isubsequent tap changer operations
    subsequent_delay = Seconds
    # Maximum allowed delay for initial tap changer operation (first step change)
    initial_delay = Seconds
    # Lowest possible tap step position, retard from neutral
    low_step = db.IntegerProperty()
    # The 'tap_changer_models' property has been implicitly created by
    # the tap_changer_type_asset' property of TapChangerModel.
    pass

class ResistorTypeAsset(ElectricalTypeAsset):
    """ Documentation for a generic resistor that may be used for design purposes.
    """

    # The 'resistor_asset_models' property has been implicitly created by
    # the resistor_type_asset' property of ResistorAssetModel.
    pass
    # The 'resistors' property has been implicitly created by
    # the resistor_type_asset' property of Resistor.
    pass

class OverheadConductorTypeAsset(LinearConductorTypeAsset):
    """ Documentation for a generic Overhead Conductor that may be used for various purposes such as work planning. It is a specialisation of LinearConductor that includes attributes specific to overhead lines.
    """

    # Spacing between the individual conductor strands for a single overhead conductor phase.
    conductor_spacing = Length
    # Number of conductor strands for a particular overhead conductor phase. Separate phases and their spacings are modelled by the MountingPoint positions for the structure the Overhead Conductor is supported by (e.g. pole, tower)
    conductor_count = db.IntegerProperty()
    # The 'overhead_conductor_models' property has been implicitly created by
    # the overhead_conductor_type_asset' property of OverheadConductorAssetModel.
    pass

class CableTypeAsset(LinearConductorTypeAsset):
    """ Documentation for a generic cable that may be used for various purposes such as work planning. It is a specialisation of LinearConductor that includes attributes specific to underground cables.
    """

    # Outside diameter over the shield (inches) for a non concentric neutral cable.
    outside_diameter = Length
    # Phase conductor spacing for a three conductor cable if a distribution model is given.
    conductor_spacing = Length
    # Thickness of the shielding
    shield_thickness = Length
    # The 'cable_asset_models' property has been implicitly created by
    # the cable_type_asset' property of CableAssetModel.
    pass


