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

from cim14.iec61970.core import IdentifiedObject
from cim14 import Element

from cim14.iec61970.domain import Money
from cim14.iec61970.domain import PerCent
from cim14.iec61970.domain import Conductance
from cim14.iec61970.domain import Reactance
from cim14.iec61970.domain import Resistance
from cim14.iec61970.domain import Voltage
from cim14.iec61970.domain import Susceptance
from cim14.iec61970.domain import ApparentPower
from cim14.iec61970.domain import CurrentFlow
from cim14.iec61970.domain import Frequency

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

SealKind = db.StringProperty(choices=("steel", "other", "lock", "lead"))

SealConditionKind = db.StringProperty(choices=("locked", "other", "broken", "missing", "open"))

ns_prefix = "cim.IEC61968.Assets"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#IEC61968.Assets"

class Seal(IdentifiedObject):
    """ Physically controls access to AssetContainers.
    """

    # Kind of seal.
    kind = SealKind
    # Date and time this seal has been applied.
    applied_date_time = db.DateProperty()
    # (reserved word) Seal number.
    seal_number = db.StringProperty()
    # Condition of seal.
    condition = SealConditionKind
#    asset_container = db.ReferenceProperty()

class AcceptanceTest(Element):
    """ Acceptance test for assets.
    """

    # Type of test or group of tests that was conducted on 'dateTime'.
    type = db.StringProperty()
    # Date and time the asset was last tested using the 'type' of test and yiedling the currnet status in 'success' attribute.
    date_time = db.DateProperty()
    # True if asset has passed acceptance test and may be placed in or is in service. It is set to false if asset is removed from service and is required to be tested again before being placed back in service, possibly in a new location. Since asset may go through multiple tests during its life cycle, the date of each acceptance test may be recorded in Asset.ActivityRecord.status.dateTime.
    success = db.BooleanProperty()

class Asset(IdentifiedObject):
    """ Tangible resource of the utility, including power system equipment, cabinets, buildings, etc. For electrical network equipment, the role of the asset is defined through PowerSystemResource and its subclasses, defined mainly in the Wires model (refer to IEC61970-301 and model package IEC61970::Wires). Asset description places emphasis on the physical characteristics of the equipment fulfilling that role.
    """

    # Purchase price of asset.
    purchase_price = Money
    # The way this particular asset is being used in this installation. For example, the application of a bushing when attached to a specific transformer winding would be one of the following: H1, H2, H3, H0, X1, X2, X3, X0, Y1, Y2, Y3, Y0.
    application = db.StringProperty()
    # Whenever an asset is reconditioned, percentage of expected life for the asset when it was new; zero for new devices.
    initial_loss_of_life = PerCent
    # Condition of asset in inventory or at time of installation. Examples include new, rebuilt, overhaul required, other. Refer to inspection data for information on the most current condition of the asset.
    initial_condition = db.StringProperty()
    # Code for this type of asset.
    corporate_code = db.StringProperty()
    # (if applicable) Date current installation was completed, which may not be the same as the in-service date. Asset may have been installed at other locations previously. Ignored if asset is (1) not currently installed (e.g., stored in a depot) or (2) not intended to be installed (e.g., vehicle, tool).
    installation_date = db.DateProperty()
    # Date this asset was manufactured.
    manufactured_date = db.DateProperty()
    # Extension mechanism to accommodate utility-specific categorisation of Asset and its subtypes, according to their corporate standards, practices, and existing IT systems (e.g., for management of assets, maintenance, work, outage, customers, etc.).
    category = db.StringProperty()
    # Uniquely Tracked Commodity (UTC) number.
    utc_number = db.StringProperty()
    # True if asset is considered critical for some reason (for example, a pole with critical attachments).
    critical = db.BooleanProperty()
    # Lot number for this asset. Even for the same model and version number, many assets are manufactured in lots.
    lot_number = db.StringProperty()
    # Serial number of this asset.
    serial_number = db.StringProperty()
    # Information on acceptance test.
    acceptance_test = db.ReferenceProperty()
    # Status of this asset.
    status = db.ReferenceProperty()
    # The 'to_asset_roles' property has been implicitly created by
    # the from_asset' property of AssetAssetRole.
    pass
#    erp_rec_delivery_items = db.ListProperty(db.Key)

#    @property
#    def assets(self):
#        return ErpRecDelvLineItem.gql("WHERE erp_rec_delivery_items = :1", self.key())
    # The 'asset_functions' property has been implicitly created by
    # the asset' property of AssetFunction.
    pass
    # The 'electronic_addresses' property has been implicitly created by
    # the asset' property of ElectronicAddress.
    pass
#    dimensions_info = db.ReferenceProperty()
#    erp_item_master = db.ReferenceProperty()
#    properties = db.ListProperty(db.Key)

#    @property
#    def property_assets(self):
#        return UserAttribute.gql("WHERE properties = :1", self.key())
#    erp_inventory = db.ReferenceProperty()
#    scheduled_events = db.ListProperty(db.Key)

#    @property
#    def assets(self):
#        return ScheduledEvent.gql("WHERE scheduled_events = :1", self.key())
    # The 'change_items' property has been implicitly created by
    # the asset' property of ChangeItem.
    pass
#    ratings = db.ListProperty(db.Key)

#    @property
#    def rating_assets(self):
#        return UserAttribute.gql("WHERE ratings = :1", self.key())
#    asset_container = db.ReferenceProperty()
#    work_task = db.ReferenceProperty()
    # The 'document_roles' property has been implicitly created by
    # the asset' property of DocAssetRole.
    pass
    # The 'from_asset_roles' property has been implicitly created by
    # the to_asset' property of AssetAssetRole.
    pass
#    financial_info = db.ReferenceProperty()
#    asset_property_curves = db.ListProperty(db.Key)

#    @property
#    def assets(self):
#        return AssetPropertyCurve.gql("WHERE asset_property_curves = :1", self.key())
    # The 'erp_organisation_roles' property has been implicitly created by
    # the asset' property of OrgAssetRole.
    pass
    # The 'measurements' property has been implicitly created by
    # the asset' property of Measurement.
    pass
#    hazards = db.ListProperty(db.Key)

#    @property
#    def assets(self):
#        return Hazard.gql("WHERE hazards = :1", self.key())
#    mediums = db.ListProperty(db.Key)

#    @property
#    def assets(self):
#        return Medium.gql("WHERE mediums = :1", self.key())
#    reliability_infos = db.ListProperty(db.Key)

#    @property
#    def assets(self):
#        return ReliabilityInfo.gql("WHERE reliability_infos = :1", self.key())
    # The 'location_roles' property has been implicitly created by
    # the asset' property of AssetLocRole.
    pass
    # The 'power_system_resource_roles' property has been implicitly created by
    # the asset' property of AssetPsrRole.
    pass
#    activity_records = db.ListProperty(db.Key)

#    @property
#    def assets(self):
#        return ActivityRecord.gql("WHERE activity_records = :1", self.key())

class ElectricalInfo(IdentifiedObject):
    """ Electrical properties of an asset or of an asset model (product by a manufacturer). Can also be used to define electrical properties for each phase individually. Not every attribute will be required for each type of asset or asset model. For example, a transformer may only have requirments for 'ratedVoltage', 'ratedApparentPower' and 'phaseCount' attributes, while a LinearConductor will have 'r', 'x', 'b' and 'g' requirements per unit length on top of a 'ratedCurrent' and 'ratedVoltage'.
    """

    # Zero sequence conductance.
    g0 = Conductance
    # Positive sequence series reactance.
    x = Reactance
    # Zero sequence series resistance.
    r0 = Resistance
    # For an installed asset, this is the total number of electrical wires that are physically connected to it. For an AssetModel, this is the total number of wires that can potentially be connected to this asset type. This is particularly useful to understand overall electrical configurations for distribution secondary where the number of wires can not be derived from phase information alone. For example, 120v 2 Wires; 240v 2 Wires; 480v 1Ph 2 Wires; 120/240v 1Ph; 120/208v 3Ph Y; 120/208v 1Ph Y; 120/240v 3Ph D; 240/480v 1Ph 3 Wires; 480v 3Ph D; 240/480v 3Ph D; 277/480v 3Ph Y.
    wire_count = db.IntegerProperty()
    # Zero sequence series reactance.
    x0 = Reactance
    # Rated voltage.
    rated_voltage = Voltage
    # Positive sequence conductance.
    g = Conductance
    # Zero sequence susceptance.
    b0 = Susceptance
    # Positive sequence susceptance.
    b = Susceptance
    # Rated apparent power.
    rated_apparent_power = ApparentPower
    # Positive sequence series resistance.
    r = Resistance
    # Number of potential phases the asset supports, typically 0, 1 or 3. The actual phases connected are determined from 'ConductingEquipment.phases' attribute in the ConductingEquipment subclass associated with the asset or from 'ElectricalAsset.phaseCode' attribute.
    phase_count = db.IntegerProperty()
    # Basic Insulation Level (BIL) for switchgear, insulators, etc. A reference insulation level expressed as the impulse crest voltage of a nominal wave, typically 1.2 X 50 microsecond. This is a measure of the ability of the insulation to withstand very high voltage surges.
    bil = Voltage
    # Rated current.
    rated_current = CurrentFlow
    # Frequency at which stated device ratings apply, typically 50Hz or 60Hz.
    frequency = Frequency
#    end_device_assets = db.ListProperty(db.Key)

#    @property
#    def electrical_infos(self):
#        return EndDeviceAsset.gql("WHERE end_device_assets = :1", self.key())
#    electrical_assets = db.ListProperty(db.Key)

#    @property
#    def electrical_infos(self):
#        return ElectricalAsset.gql("WHERE electrical_assets = :1", self.key())
    # The 'electrical_asset_model_roles' property has been implicitly created by
    # the electrical_info' property of ElecAMElecPropRole.
    pass
    # The 'electrical_type_asset_roles' property has been implicitly created by
    # the electrical_info' property of ElecTAElecPropRole.
    pass

class AssetContainer(Asset):
    """ Asset that is aggregation of other assets such as conductors, transformers, switchgear, land, fences, buildings, equipment, vehicles, etc.
    """

    # The 'seals' property has been implicitly created by
    # the asset_container' property of Seal.
    pass
#    land_properties = db.ListProperty(db.Key)

#    @property
#    def asset_containers(self):
#        return LandProperty.gql("WHERE land_properties = :1", self.key())
    # The 'assets' property has been implicitly created by
    # the asset_container' property of Asset.
    pass

class AssetFunction(Asset):
    """ Function performed by an asset. Often, function is a module (or a board that plugs into a backplane) that can be replaced or updated without impacting the rest of the asset. Therefore functions are treated as assets because they have life-cycles that are independent of the asset containing the function.
    """

    # Configuration specified for this function.
    config_id = db.StringProperty()
    # Hardware version.
    hardware_id = db.StringProperty()
    # Name of program.
    program_id = db.StringProperty()
    # Firmware version.
    firmware_id = db.StringProperty()
    # Password needed to access this function.
    password = db.StringProperty()
#    asset = db.ReferenceProperty()
#    asset_function_asset_model = db.ReferenceProperty()

class ComMediaAsset(Asset):
    """ Communication media such as fiber optic cable, power-line, telephone, etc.
    """

    pass


