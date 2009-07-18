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
from cim14.iec61968.asset_models import AssetModel
from cim14.iec61970.core import IdentifiedObject

from cim14.iec61970.domain import Weight
from cim14.iec61970.domain import Voltage
from cim14.iec61968.informative.inf_assets import StreetlightLampKind
from cim14.iec61970.domain import ActivePower
from cim14.iec61970.domain import Money
from cim14.iec61970.domain import Length
from cim14.iec61970.domain import Temperature

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

TapChangerSwitchingKind = db.StringProperty(choices=("resistive", "other", "reactive", "vacuum"))

LinearConductorUsageKind = db.StringProperty(choices=("transmission", "other", "distribution"))

OilPreservationKind = db.StringProperty(choices=("nitrogen_blanket", "conservator", "free_breathing", "other"))

WindingInsulationKind = db.StringProperty(choices=("thermally_upgraded_paper", "other", "nomex", "paper"))

ConductorMaterialKind = db.StringProperty(choices=("copper", "other", "aluminum"))

CableShieldKind = db.StringProperty(choices=("superclean", "free_form", "conventional", "supersmooth", "other"))

BushingInsulationKind = db.StringProperty(choices=("compound", "other", "solid_porcelain", "paperoil"))

LinearAssetInsulationKind = db.StringProperty(choices=("unbelted_pilc", "varnished_cambric_cloth", "tree_resistant_high_molecular_weight_polyethylene", "butyl", "low_capacitance_rubber", "high_molecular_weight_polyethylene", "other", "tree_retardant_crosslinked_polyethylene", "crosslinked_polyethylene", "silicon_rubber", "oil_paper", "ethylene_propylene_rubber", "varnished_dacron_glass", "rubber", "ozone_resistant_rubber", "belted_pilc", "asbestos_and_varnished_cambric"))

CableConstructionKind = db.StringProperty(choices=("segmental", "compressed", "other", "sector", "stranded", "solid", "compacted"))

CableOuterJacketKind = db.StringProperty(choices=("other", "linear_low_density_polyethylene", "insulating", "semiconducting", "polyethylene", "pvc", "none"))

TransformerCoreKind = db.StringProperty(choices=("shell", "core"))

ns_prefix = "cim.IEC61968.Informative.InfAssetModels"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#IEC61968.Informative.InfAssetModels"

class AssetModelCatalogueItem(Document):
    """ Provides pricing and other relevant information about a specific manufacturer's product (i.e., AssetModel), and its price from a given supplier. A single AssetModel may be availble from multiple suppliers. Note that manufacturer and supplier are both types of organisation, which the association is inherited from Document.
    """

    # Unit cost for an asset model from a specific supplier, either for a unit cost or cost per unit length. Cost is for material or asset only and does not include labor to install/construct or configure it.
    unit_cost = Money
    # The 'erp_poline_items' property has been implicitly created by
    # the asset_model_catalogue_item' property of ErpPOLineItem.
    pass
#    asset_model = db.ReferenceProperty()
#    asset_model_catalogue = db.ReferenceProperty()
    # The 'erp_quote_line_items' property has been implicitly created by
    # the asset_model_catalogue_item' property of ErpQuoteLineItem.
    pass

class CompositeSwitchAssetModel(AssetModel):
    """ Documentation for a type of a composite switch asset of a particular product model made by a manufacturer.
    """

#    composite_switch_type_asset = db.ReferenceProperty()
    # The 'composite_switch_assets' property has been implicitly created by
    # the composite_switch_asset_model' property of CompositeSwitchAsset.
    pass
#    composite_switch_info = db.ReferenceProperty()

class WorkEquipmentAssetModel(AssetModel):
    """ Documentation for a type of an equipment used for work of a particular product model made by a manufacturer.
    """

    # The 'work_equipment_assets' property has been implicitly created by
    # the work_equipment_asset_model' property of WorkEquipmentAsset.
    pass
#    work_equipment_type_asset = db.ReferenceProperty()

class AssetFunctionAssetModel(AssetModel):
    """ Documentation for a type of an asset function of a particular product model made by a manufacturer.(Organisation). Asset Functions are typically component parts of Assets or Asset Containers.
    """

    # The 'asset_functions' property has been implicitly created by
    # the asset_function_asset_model' property of AssetFunction.
    pass
#    asset_function_type_asset = db.ReferenceProperty()

class CabinetModel(AssetModel):
    """ Documentation for a type of Cabinet of a particular product model made by a manufacturer.
    """

    # The 'cabinets' property has been implicitly created by
    # the cabinet_model' property of Cabinet.
    pass
#    cabinet_type_asset = db.ReferenceProperty()

class PoleModel(AssetModel):
    """ A type of pole supplied by a given manufacturer.
    """

    # Pole species. Aluminum, Aluminum Davit, Concrete, Fiberglass, Galvanized Davit, Galvanized, Steel Davit Primed, Steel Davit, Steel Standard Primed, Steel, Truncated, Wood-Treated, Wood-Hard, Wood-Salt Treated, Wood-Soft, Wood, Other, Unknown.
    species_type = db.StringProperty()
    # Pole class: 1, 2, 3, 4, 5, 6, 7, H1, H2, Other, Unknown.
    classification = db.StringProperty()
    # The 'poles' property has been implicitly created by
    # the pole_model' property of Pole.
    pass
#    pole_type_asset = db.ReferenceProperty()

class TowerAssetModel(AssetModel):
    """ A type of tower supplied by a given manufacturer or constructed from a common design.
    """

    # The 'towers' property has been implicitly created by
    # the tower_asset_model' property of Tower.
    pass
#    tower_type_asset = db.ReferenceProperty()

class ElectricalAssetModel(AssetModel):
    """ Documentation for a type of ElectricalAsset of a particular product model made by a manufacturer.
    """

    # The 'electrical_info_roles' property has been implicitly created by
    # the electrical_asset_model' property of ElecAMElecPropRole.
    pass

class VehicleAssetModel(AssetModel):
    """ Documentation for a type of a vehicle of a particular product model made by a manufacturer.
    """

#    vehicle_type_asset = db.ReferenceProperty()
    # The 'vehicles' property has been implicitly created by
    # the vehicle_asset_model' property of Vehicle.
    pass

class AssetModelCatalogue(IdentifiedObject):
    """ Catalogue of available types of products and materials that are used to build or install, maintain or operate an Asset. Each catalogue item is for a specific product (AssetModel) available from a specific supplier.
    """

    status = db.ReferenceProperty()
    # The 'asset_model_catalogue_items' property has been implicitly created by
    # the asset_model_catalogue' property of AssetModelCatalogueItem.
    pass

class ToolAssetModel(AssetModel):
    """ Documentation for a type of a tool of a particular product model made by a manufacturer.
    """

#    tool_type_asset = db.ReferenceProperty()
    # The 'tools' property has been implicitly created by
    # the tool_asset_model' property of Tool.
    pass

class TransformerAssetModel(ElectricalAssetModel):
    """ Documentation for a type of a transformer of a particular product model made by a manufacturer.
    """

    # Core kind of this transformer product.
    core_kind = TransformerCoreKind
    # Type of insultation used for transformer windings: Paper, Thermally Upgraded Paper, Nomex, other
    winding_insulation_kind = WindingInsulationKind
    # True if this is an autotransformer, false otherwise.
    auto_transformer = db.BooleanProperty()
    # Weight of core and coils in transformer.
    core_coils_weight = Weight
    # Weight of solid insultation in transformer.
    solid_insulation_weight = Weight
    # Basic Insulation Level of Neutral
    neutral_bil = Voltage
    # Kind of oil preservation system.
    oil_preservation_kind = OilPreservationKind
#    transformer_info = db.ReferenceProperty()
#    transformer_type_asset = db.ReferenceProperty()
    # The 'transformer_assets' property has been implicitly created by
    # the transformer_asset_model' property of TransformerAsset.
    pass

class GeneratorAssetModel(ElectricalAssetModel):
    """ Documentation for a type of generation equipment of a particular product model made by a manufacturer.
    """

#    generator_type_asset = db.ReferenceProperty()
    # The 'generator_assets' property has been implicitly created by
    # the generator_asset_model' property of GeneratorAsset.
    pass

class StreetlightAssetModel(ElectricalAssetModel):
    """ Documentation for a type of a streelight of a particular product model made by a manufacturer.
    """

    # Lamp kind supplied from manufacturer (vs. one that has been replaced in the field).
    lamp_kind = StreetlightLampKind
    # Power rating of light as supplied by the manufacturer.
    light_rating = ActivePower
#    streetlight_type_assets = db.ListProperty(db.Key)

#    @property
#    def streetlight_asset_models(self):
#        return StreetlightTypeAsset.gql("WHERE streetlight_type_assets = :1", self.key())
    # The 'streetlights' property has been implicitly created by
    # the streetlight_asset_model' property of Streetlight.
    pass

class ProtectionEquipmentAssetModel(ElectricalAssetModel):
    """ Documentation for a type of protection equipment asset of a particular product model made by a manufacturer.
    """

    # The 'protection_equipment_assets' property has been implicitly created by
    # the protection_equipment_asset_model' property of ProtectionEquipmentAsset.
    pass
#    protection_equipment_type_asset = db.ReferenceProperty()

class FaultIndicatorAssetModel(ElectricalAssetModel):
    """ Documentation for a type of an FaultIndicator asset of a particular product model made by a manufacturer.
    """

#    fault_indicator_type_asset = db.ReferenceProperty()
    # The 'fault_indicator_assets' property has been implicitly created by
    # the fault_indicator_asset_model' property of FaultIndicatorAsset.
    pass

class LinearConductorAssetModel(ElectricalAssetModel):
    """ A type of linear conductor made by a particular manufacturer (Organisation). Its ElectricalProperties are defined as being per unit length (which is defined by the unitLength attribute)
    """

    # True if conductor is insultated.
    insulated = db.BooleanProperty()
    # Usage of this linear conductor product.
    usage = LinearConductorUsageKind
    # Kind of insulation material.
    insulation_kind = LinearAssetInsulationKind
    # Radius of the conductor
    radius = db.IntegerProperty()
    # Geometric Mean Radius. If the conductor were replaced by a thin walled tube of radius gMR then its reactance would be identical to that of the actual conductor
    g_mr = Length
    # Commonly referred to size for this type of conductor.
    size = db.StringProperty()
#    linear_conductor_type_asset = db.ReferenceProperty()
    # The 'linear_conductor_assets' property has been implicitly created by
    # the linear_conductor_asset_model' property of LinearConductorAsset.
    pass

class SwitchAssetModel(ElectricalAssetModel):
    """ Documentation for a type of a switch asset of a particular product model made by a manufacturer.
    """

#    switch_info = db.ReferenceProperty()
#    switch_type_asset = db.ReferenceProperty()
    # The 'switch_assets' property has been implicitly created by
    # the switch_asset_model' property of SwitchAsset.
    pass

class PotentialTransformerAssetModel(ElectricalAssetModel):
    """ A particular model supplied by a manufacturer of a Potential Transformer (PT), wich is used to measure electrical qualities of the circuit that is being protected and/or monitored.
    """

#    potential_transformer_type_asset = db.ReferenceProperty()
    # The 'potential_transformer_assets' property has been implicitly created by
    # the potential_transformer_asset_model' property of PotentialTransformerAsset.
    pass
#    potential_transformer_info = db.ReferenceProperty()

class ResistorAssetModel(ElectricalAssetModel):
    """ Documentation for a type of a resistor asset of a particular product model made by a manufacturer.
    """

    # The 'resistor_assets' property has been implicitly created by
    # the resistor_asset_model' property of ResistorAsset.
    pass
#    resistor_type_asset = db.ReferenceProperty()

class MeterAssetModel(ElectricalAssetModel):
    """ Documentation for a type of a meter asset of a particular product model made by a manufacturer.
    """

    # Meter form number.
    form = db.StringProperty()
    # True when the meter or the installed AMR option is capable of capturing kWh interval data.
    load_profile_meter = db.BooleanProperty()
    # True when the meter is capable of metering real energy in kWh.
    kwh_meter = db.BooleanProperty()
    # True when the meter is capable of metering reactive energy in kVArh.
    reactive_meter = db.BooleanProperty()
    # Number of wires.
    wire_count = db.IntegerProperty()
    # True when the meter or installed AMR option is capable of capturing demand data.
    demand_meter = db.BooleanProperty()
    # Maximum number of registers this meter model can support. The actual number in use is based on the number of Registers associated with a given MeterAsset.
    max_register_count = db.IntegerProperty()
    # True when the meter or meter+AMR module are capable of offering TOU data.
    time_of_use_meter = db.BooleanProperty()
    # True when the meter is capable of metering apparent energy in kVAh.
    k_vah_meter = db.BooleanProperty()
    # Meter kh (watthour) constant. This constant is the number of watthours that must be applied to the meter to cause one disk revolution for an electromechanical meter or the number of watthours represented by one increment pulse for an electronic meter.
    k_h = db.FloatProperty()
    # True when the meter is capable of metering reactive energy in kQh.
    q_meter = db.BooleanProperty()
    # True when the meter or the installed AMR option is capable of capturing interval data for a user selectable measurement (kWh, Volts, or some other billing or engineering quantity).
    interval_data_meter = db.BooleanProperty()
    # Meter register ratio.
    register_ratio = db.FloatProperty()
#    meter_type_asset = db.ReferenceProperty()
    # The 'meter_assets' property has been implicitly created by
    # the meter_asset_model' property of MeterAsset.
    pass

class SurgeProtectorAssetModel(ElectricalAssetModel):
    """ Documentation for a type of an SurgeProtector asset of a particular product model made by a manufacturer.
    """

    # The 'surge_protector_assets' property has been implicitly created by
    # the surge_protector_asset_model' property of SurgeProtectorAsset.
    pass
#    surge_protector_type_asset = db.ReferenceProperty()

class OverheadConductorAssetModel(LinearConductorAssetModel):
    """ A type of linear conductor model made by a particular manufacturer (Organisation). Its ElectricalProperties are defined as being per unit length (which is defined by the unitLength attribute)
    """

#    overhead_conductor_type_asset = db.ReferenceProperty()

class ShuntCompensatorAssetModel(ElectricalAssetModel):
    """ For application as shunt capacitor or reactor or switchable bank of shunt capacitors or reactors, this is documentation for a type of a capacitor or reactor of a particular product model made by a manufacturer (Organisation). There are typically many instances of an asset associated with a single asset model.
    """

    # The 'shunt_compensator_assets' property has been implicitly created by
    # the shunt_compensator_asset_model' property of ShuntCompensatorAsset.
    pass
#    shunt_compensator_type_asset = db.ReferenceProperty()
#    shunt_impedance_info = db.ReferenceProperty()

class CableAssetModel(LinearConductorAssetModel):
    """ Documentation for a type of a Cable of a particular product model made by a manufacturer.
    """

    # Insulating compound name.
    insulating_compound = db.StringProperty()
    # Sheath material: Lead, Copper, Steel, Aluminum, None.
    sheath_material = db.StringProperty()
    # Kind of conductor shield of this cable product.
    shield_kind = CableShieldKind
    # Center to neutral conductor spacing for a concentric neutral cable (blank for a transmission model).
    center_to_neutral = Length
    # Thickness of the insulation.
    insulation_thickness = Length
    # Neutral conductor design: Concentric Neutral, Copper Tape, Aluminum Tape, Lead insulation, Other.
    neutral_cond_design = db.StringProperty()
    # Kind of outer jacket of this cable.
    outer_jacket_kind = CableOuterJacketKind
    # Diameter of a concentric neutral strand for a concentric neutral cable.
    diameter_to_neutral = Length
    # Kind of construction of this cable product.
    construction_kind = CableConstructionKind
    # Maximum nominal design operating temperature.
    nominal_temp = Temperature
    # Kind of conductor material of this cable product.
    conductor_material_kind = ConductorMaterialKind
    # True if wire strands are extruded in a way to fill the voids in the cable.
    strand_fill_flag = db.BooleanProperty()
    # Number of conductors physically contained in the cable.
    conductor_count = db.IntegerProperty()
    # True if sheath is used as a neutral.
    sheath_neutral = db.BooleanProperty()
#    cable_type_asset = db.ReferenceProperty()

class RecloserAssetModel(ElectricalAssetModel):
    """ Documentation for a type of a recloser asset of a particular product model made by a manufacturer.
    """

    # The 'recloser_assets' property has been implicitly created by
    # the recloser_asset_model' property of RecloserAsset.
    pass
#    recloser_type_asset = db.ReferenceProperty()
#    recloser_info = db.ReferenceProperty()

class ComFunctionAssetModel(ElectricalAssetModel):
    """ Documentation for a type of communication function of a particular product model made by a manufacturer.
    """

#    com_function_type_asset = db.ReferenceProperty()

class BusbarAssetModel(ElectricalAssetModel):
    """ Documentation for a type of a busbar asset of a particular product model made by a manufacturer.
    """

    # The 'busbar_assets' property has been implicitly created by
    # the busbar_asset_model' property of BusbarAsset.
    pass
#    busbar_asset_model = db.ReferenceProperty()

class TapChangerModel(ElectricalAssetModel):
    """ Documentation for a type of a tap changer of a particular product model made by a manufacturer.
    """

    # Number of taps.
    tap_count = db.IntegerProperty()
    # Switching kind of tap changer.
    switching_kind = TapChangerSwitchingKind
    # The 'tap_changer_assets' property has been implicitly created by
    # the tap_changer_model' property of TapChangerAsset.
    pass
#    tap_changer_type_asset = db.ReferenceProperty()

class BushingModel(ElectricalAssetModel):
    """ Documentation for a type of a bushing of a particular product model made by a manufacturer.
    """

    # Kind of insulation used in this bushing model.
    insulation_kind = BushingInsulationKind
#    bushing_asset = db.ReferenceProperty()
#    bushing_type_asset = db.ReferenceProperty()

class BreakerAssetModel(ElectricalAssetModel):
    """ Documentation for a type of a breaker asset of a particular product model made by a manufacturer.
    """

#    breaker_type_asset = db.ReferenceProperty()
#    breaker_info = db.ReferenceProperty()
    # The 'breaker_assets' property has been implicitly created by
    # the breaker_asset_model' property of BreakerAsset.
    pass

class CurrentTransformerAssetModel(ElectricalAssetModel):
    """ A particular model supplied by a manufacturer of a Current Transformer (CT), wich is used to measure electrical qualities of the circuit that is being protected and/or monitored.
    """

#    current_transformer_info = db.ReferenceProperty()
#    current_transformer_type_asset = db.ReferenceProperty()
    # The 'current_transformer_assets' property has been implicitly created by
    # the current_transformer_asset_model' property of CurrentTransformerAsset.
    pass

class FACTSDeviceAssetModel(ElectricalAssetModel):
    """ A particular model of FACTS device provided from a manufacturer. A FACTS devices are used for the dynamic control of voltage, impedance and phase angle of high voltage AC transmission lines. FACTS device types include: - SVC = Static Var Compensator - STATCOM = Static Synchronous Compensator - TCPAR = Thyristor Controlled Phase-Angle Regulator - TCSC = Thyristor Controlled Series Capacitor - TCVL = Thyristor Controlled Voltage Limiter - TSBR = Thyristor Switched Braking Resistor - TSSC = Thyristor Switched Series Capacitor - UPFC = Unified Power Flow Controller
    """

    # The 'factsdevice_assets' property has been implicitly created by
    # the factsdevice_asset_model' property of FACTSDeviceAsset.
    pass
#    factsdevice_type_asset = db.ReferenceProperty()

class SeriesCompensatorAssetModel(ElectricalAssetModel):
    """ For application as a series capacitor or reactor, this is documentation for a type of a capacitor or reactor of a particular product model made by a manufacturer.
    """

#    series_compensator_asset = db.ReferenceProperty()
#    shunt_compensator_type_asset = db.ReferenceProperty()

class SVCAssetModel(FACTSDeviceAssetModel):
    """ Documentation for a type of a Static Var Compensator of a particular product model made by a manufacturer.
    """

#    svctype_asset = db.ReferenceProperty()
    # The 'svcassets' property has been implicitly created by
    # the svcasset_model' property of SVCAsset.
    pass
#    svc_info = db.ReferenceProperty()


