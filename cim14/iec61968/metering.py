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

from cim14.iec61968.work import Work
from cim14 import Element
from cim14.iec61970.core import IdentifiedObject
from cim14.iec61968.common import ActivityRecord
from cim14.iec61968.common import Location
from cim14.iec61968.assets import AssetFunction
from cim14.iec61970.meas import MeasurementValue
from cim14.iec61968.assets import AssetContainer

from cim14.iec61970.domain import CurrentFlow
from cim14.iec61970.domain import Voltage
from cim14.iec61970.domain import ActivePower
from cim14.iec61970.domain import RealEnergy
from cim14.iec61970.domain import FloatQuantity
from cim14.iec61970.domain import UnitSymbol
from cim14.iec61970.domain import UnitMultiplier
from cim14.iec61970.domain import Seconds
from cim14.iec61970.domain import AbsoluteDate
from cim14.iec61970.domain import Minutes

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

ReadingKind = db.StringProperty(choices=("other", "volume", "phase_angle", "demand", "voltage", "voltage_angle", "energy", "power_factor", "pressure", "current_angle", "time", "current", "power", "date"))

PhaseConfigurationKind = db.StringProperty(choices=("two_phase_two_wire", "other", "two_phase_three_wire", "three_phase_four_wire", "three_phase_two_wire", "one_phase_three_wire", "three_phase_three_wire", "one_phase_two_wire"))

ns_prefix = "cim.IEC61968.Metering"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#IEC61968.Metering"

class MeterServiceWork(Work):
    """ Work involving meters.
    """

#    old_meter_asset = db.ReferenceProperty()
#    meter_asset = db.ReferenceProperty()

class IntervalBlock(Element):
    """ Time sequence of Readings of the same ReadingType. Contained IntervalReadings may need conversion through the application of an offset and a scalar defined in associated Pending.
    """

#    meter_reading = db.ReferenceProperty()
#    pending = db.ReferenceProperty()
#    reading_type = db.ReferenceProperty()
#    interval_readings = db.ListProperty(db.Key)

#    @property
#    def interval_blocks(self):
#        return IntervalReading.gql("WHERE interval_readings = :1", self.key())

class ReadingQuality(Element):
    """ Quality of a specific reading value or interval reading value. Note that more than one Quality may be applicable to a given Reading. Typically not unsed unless problems or unusual conditions occur (i.e., quality for each Reading is assumed to be 'Good' unless stated otherwise in associated ReadingQuality).
    """

    # Quality, to be specified if different than 'Good'.
    quality = db.StringProperty()
#    interval_reading = db.ReferenceProperty()
#    reading = db.ReferenceProperty()

class EndDeviceGroup(IdentifiedObject):
    """ Abstraction for management of group communications within a two-way AMR system or the data for a group of related meters. Commands can be issued to all of the meters that belong to a meter group using a defined group address and the underlying AMR communication infrastructure.
    """

    # Address of this end device group.
    group_address = db.IntegerProperty()
#    end_device_assets = db.ListProperty(db.Key)

#    @property
#    def end_device_groups(self):
#        return EndDeviceAsset.gql("WHERE end_device_assets = :1", self.key())
    # The 'end_device_controls' property has been implicitly created by
    # the end_device_group' property of EndDeviceControl.
    pass
#    demand_response_program = db.ReferenceProperty()

class Register(IdentifiedObject):
    """ Display for quantity that is metered on an end device such as a meter.
    """

    # Number of digits (dials on a mechanical meter) to the left of the decimal place; default is 5.
    left_digit_count = db.IntegerProperty()
    # Number of digits (dials on a mechanical meter) to the right of the decimal place.
    right_digit_count = db.IntegerProperty()
#    device_function = db.ReferenceProperty()
#    reading_type = db.ReferenceProperty()

class ServiceDeliveryPoint(IdentifiedObject):
    """ Logical point on the network where the ownership of the service changes hands. It is one of potentially many service points within a ServiceLocation, delivering service in accordance with a CustomerAgreement. Used at the place where a meter may be installed.
    """

    # Remarks about this service delivery point, for example the reason for it being rated with a non-nominal priority.
    service_delivery_remark = db.StringProperty()
    # Current that this service delivery point is configured to deliver.
    rated_current = CurrentFlow
    # Power that this service delivery point is configured to deliver.
    rated_power = ActivePower
    # Nominal service voltage.
    nominal_service_voltage = db.IntegerProperty()
    # Budget bill code.
    budget_bill = db.StringProperty()
    # Estimated load.
    estimated_load = CurrentFlow
    # Load management code.
    load_mgmt = db.StringProperty()
    # Phase configuration kind.
    phase_config = PhaseConfigurationKind
    # True if as a result of an inspection or otherwise, there is a reason to suspect that a previous billing may have been performed with erroneous data. Value should be reset once this potential discrepancy has been resolved.
    check_billing = db.BooleanProperty()
    # Billing cycle.
    billing_cycle = db.StringProperty()
    # True if grounded.
    grounded = db.BooleanProperty()
    # Cumulative totalizing register of consumed service at this service delivery point over its lifetime.
    consumption_real_energy = RealEnergy
    # Priority of service for this service delivery point. Note that service delivery points at the same service location can have different priorities.
    service_priority = db.StringProperty()
    # (optional for medium voltage connections) Reference to the low side terminal of a CT or PT that obtain readings from a medium or high voltage point.
    ctpt_reference = db.IntegerProperty()
    # The 'meter_readings' property has been implicitly created by
    # the service_delivery_point' property of MeterReading.
    pass
#    sdplocations = db.ListProperty(db.Key)

#    @property
#    def service_delivery_points(self):
#        return SDPLocation.gql("WHERE sdplocations = :1", self.key())
#    service_category = db.ReferenceProperty()
#    service_location = db.ReferenceProperty()
#    service_supplier = db.ReferenceProperty()
#    pricing_structures = db.ListProperty(db.Key)

#    @property
#    def service_delivery_points(self):
#        return PricingStructure.gql("WHERE pricing_structures = :1", self.key())
    # The 'end_device_assets' property has been implicitly created by
    # the service_delivery_point' property of EndDeviceAsset.
    pass
#    power_quality_pricings = db.ListProperty(db.Key)

#    @property
#    def service_delivery_points(self):
#        return PowerQualityPricing.gql("WHERE power_quality_pricings = :1", self.key())
#    customer_agreement = db.ReferenceProperty()
#    energy_consumer = db.ReferenceProperty()

class MeterReading(IdentifiedObject):
    """ Set of values obtained from the meter.
    """

    # Date and time interval of the data items contained within this meter reading.
    values_interval = db.ReferenceProperty()
#    service_delivery_point = db.ReferenceProperty()
#    customer_agreement = db.ReferenceProperty()
#    readings = db.ListProperty(db.Key)

#    @property
#    def meter_readings(self):
#        return Reading.gql("WHERE readings = :1", self.key())
    # The 'interval_blocks' property has been implicitly created by
    # the meter_reading' property of IntervalBlock.
    pass
    # The 'end_device_events' property has been implicitly created by
    # the meter_reading' property of EndDeviceEvent.
    pass
#    meter_asset = db.ReferenceProperty()

class EndDeviceControl(IdentifiedObject):
    """ Instructs an EndDeviceAsset (or EndDeviceGroup) to perform a specified action.
    """

    # Type of control.
    type = db.StringProperty()
    # Level of a demand response program request, where 0=emergency. Note: Attribute is not defined on DemandResponseProgram as it is not its inherent property (it serves to conrol it).
    dr_program_level = db.IntegerProperty()
    # Whether a demand response program request is mandatory. Note: Attribute is not defined on DemandResponseProgram as it is not its inherent property (it serves to conrol it).
    dr_program_mandatory = db.BooleanProperty()
    # (if applicable) Price signal used as parameter for this end device control.
    price_signal = FloatQuantity
    # (if control has scheduled duration) Date and time interval the control has been scheduled to execute within.
    scheduled_interval = db.ReferenceProperty()
#    demand_response_program = db.ReferenceProperty()
#    customer_agreement = db.ReferenceProperty()
#    end_device_asset = db.ReferenceProperty()
#    end_device_group = db.ReferenceProperty()

class ReadingType(IdentifiedObject):
    """ Type of data conveyed by a specific Reading.
    """

    # Logical positioning of this measurement data.
    channel_number = db.IntegerProperty()
    # Unit for the reading value.
    unit = UnitSymbol
    # True for systems that must operate in 'reverse' chronological order.
    reverse_chronology = db.BooleanProperty()
    # Demand configuration such as block, rolling, logarithmic and sizes such as 15 minutes, 30 minutes, 5 minutes subinterval.
    dynamic_configuration = db.StringProperty()
    # Multiplier for 'unit'.
    multiplier = UnitMultiplier
    # (if incremental reading value) Length of increment interval.
    interval_length = Seconds
    # Numeric type to be expected for the associated IntervalBlock.value (e.g. unsignedInteger).
    default_value_data_type = db.StringProperty()
    # Kind of reading.
    kind = ReadingKind
    # Characteristics of a data value conveyed by a specific Reading, which allow an application to understand how a specific Reading is to be interpreted.
    default_quality = db.StringProperty()
    # The 'interval_blocks' property has been implicitly created by
    # the reading_type' property of IntervalBlock.
    pass
#    pending = db.ReferenceProperty()
    # The 'readings' property has been implicitly created by
    # the reading_type' property of Reading.
    pass
#    register = db.ReferenceProperty()

class EndDeviceEvent(ActivityRecord):
    """ Event detected by a DeviceFunction associated with EndDeviceAsset.
    """

    # (if user initiated) ID of user who initiated this end device event.
    user_id = db.StringProperty()
#    device_function = db.ReferenceProperty()
#    meter_reading = db.ReferenceProperty()

class SDPLocation(Location):
    """ Location of an individual service delivery point. For residential or most businesses, it is typically the location of a meter on the customer's premises. For transmission, it is the point(s) of interconnection on the transmission provider's transmission system where capacity and/or energy transmitted by the transmission provider is made available to the receiving party. The point(s) of delivery is specified in the Service Agreement.
    """

    # Method for the service person to access this service delivery point location. For example, a description of where to obtain a key if the facility is unmanned and secured.
    access_method = db.StringProperty()
    # Problems previously encountered when visiting or performing work at this service delivery point location. Examples include: bad dog, violent customer, verbally abusive occupant, obstructions, safety hazards, etc.
    site_access_problem = db.StringProperty()
    # Date when certificate of occupancy was provided for this location, 0 if valid certificate of occupancy does not exist for (inherited) 'Location.corporateCode'.
    occupancy_date = AbsoluteDate
    # Remarks about this location.
    remark = db.StringProperty()
#    service_delivery_points = db.ListProperty(db.Key)

#    @property
#    def sdplocations(self):
#        return ServiceDeliveryPoint.gql("WHERE service_delivery_points = :1", self.key())

class Pending(Element):
    """ When present, a scalar conversion that is associatied with IntervalBlock and which needs to be applied to every contained IntervalReading value. This conversion results in a new associated ReadingType, reflecting the true dimensions of interval reading values after the conversion.
    """

    # (if applicable) Offset to be added as well as multiplication using scalars.
    offset = db.IntegerProperty()
    # (if scalar is floating number) When multiplied with 'IntervalReading.value', it causes a unit of measure conversion to occur, resulting in the 'ReadingType.unit'.
    scalar_float = db.FloatProperty()
    # (if scalar is integer or rational number)  When the scalar is a simple integer, and this attribute is presented alone and multiplied with 'IntervalReading.value', it causes a unit of measure conversion to occur, resulting in the 'ReadingType.unit'. It is never used in conjuction with 'scalarFloat', only with 'scalarDenominator'.
    scalar_numerator = db.IntegerProperty()
    # Whether scalars should be applied before adding the 'offset'.
    multiply_before_add = db.BooleanProperty()
    # (if scalar is rational number) When 'IntervalReading.value' is multiplied by this attribute and divided by 'scalarDenominator, it causes a unit of measure conversion to occur, resulting in the 'ReadingType.unit'.
    scalar_denominator = db.IntegerProperty()
#    reading_type = db.ReferenceProperty()
    # The 'interval_blocks' property has been implicitly created by
    # the pending' property of IntervalBlock.
    pass

class DeviceFunction(AssetFunction):
    """ Function performed by a device such as a meter, communication equipment, controllers, etc.
    """

    # True if the device function is disabled (deactivated). Default is false (i.e., function is enabled).
    disabled = db.BooleanProperty()
#    end_device_asset = db.ReferenceProperty()
#    com_equipment_asset = db.ReferenceProperty()
    # The 'registers' property has been implicitly created by
    # the device_function' property of Register.
    pass
    # The 'end_device_events' property has been implicitly created by
    # the device_function' property of EndDeviceEvent.
    pass

class Reading(MeasurementValue):
    """ Specific value measured by a meter or other asset. Each Reading is associated with a specific ReadingType.
    """

    # Value of this reading.
    value = db.FloatProperty()
#    reading_type = db.ReferenceProperty()
#    meter_readings = db.ListProperty(db.Key)

#    @property
#    def readings(self):
#        return MeterReading.gql("WHERE meter_readings = :1", self.key())
    # The 'reading_qualities' property has been implicitly created by
    # the reading' property of ReadingQuality.
    pass
#    end_device_asset = db.ReferenceProperty()

class EndDeviceAsset(AssetContainer):
    """ AssetContainer that performs one or more end device functions. One type of EndDeviceAsset is a MeterAsset which can perform metering, load management, connect/disconnect, accounting functions, etc. Some EndDeviceAssets, such as ones monitoring and controlling air conditioner, refrigerator, pool pumps may be connected to a MeterAsset. All EndDeviceAssets may have communication capability defined by the associated ComFunction(s). An EndDeviceAsset may be owned by a consumer, a service provider, utility or otherwise. There may be a related end device function that identifies a sensor or control point within a metering applicaiton or communications systems (e.g., water, gas, electricity). Some devices may use an optical port that conforms to the ANSI C12.18 standard for communications.
    """

    # True if this end device asset is capable of supporting the means to report historical power interruption data.
    outage_report = db.BooleanProperty()
    # True if this end device asset is capable of supporting load control functions through either the meter or the AMR option. To determine whether this functionality is installed and enabled, check the 'DeviceFunction.disabled' attribute of the respective function contained by this end device asset.
    load_control = db.BooleanProperty()
    # True if this EndDeviceAsset is capable of supporting detection and monitoring of reverse flow.
    reverse_flow_handling = db.BooleanProperty()
    # True if this end device asset is capable of supporting the presention of metered values to a user or another system (always true for a meter, but might not be true for a load control unit.)
    metrology = db.BooleanProperty()
    # Time zone offset relative to GMT for the location of this end device.
    time_zone_offset = Minutes
    # Automated meter reading (AMR) system responsible for communications to this end device.
    amr_system = db.StringProperty()
    # True if this end device asset is capable of supporting the autonomous application of daylight savings time (DST).
    dst_enabled = db.BooleanProperty()
    # True if this end device asset is capable of supporting on-request reads for this end device.
    read_request = db.BooleanProperty()
    # True if this end device asset is capable of supporting demand response functions. To determine whether this functionality is installed and enabled, check the 'DeviceFunction.disabled' attribute of the respective function contained by this end device asset.
    demand_response = db.BooleanProperty()
    # True if this end device asset is capable of supporting remote whole-house disconnect capability. To determine whether this functionality is installed and enabled, check the 'DeviceFunction.disabled' attribute of the ConnectDisconnectFunction contained by this end device asset.
    disconnect = db.BooleanProperty()
    # True if this end device asset is capable of supporting one or more relays. The relays may be programmable in the meter and tied to TOU, time pulse, load control or other functions. To determine whether this functionality is installed and enabled, check the 'DeviceFunction.disabled' attribute of the respective function contained by this end device asset.
    relay_capable = db.BooleanProperty()
#    electrical_infos = db.ListProperty(db.Key)

#    @property
#    def end_device_assets(self):
#        return ElectricalInfo.gql("WHERE electrical_infos = :1", self.key())
#    customer = db.ReferenceProperty()
    # The 'device_functions' property has been implicitly created by
    # the end_device_asset' property of DeviceFunction.
    pass
#    end_device_groups = db.ListProperty(db.Key)

#    @property
#    def end_device_assets(self):
#        return EndDeviceGroup.gql("WHERE end_device_groups = :1", self.key())
#    end_device_model = db.ReferenceProperty()
    # The 'end_device_controls' property has been implicitly created by
    # the end_device_asset' property of EndDeviceControl.
    pass
    # The 'readings' property has been implicitly created by
    # the end_device_asset' property of Reading.
    pass
#    service_location = db.ReferenceProperty()
#    service_delivery_point = db.ReferenceProperty()

class IntervalReading(MeasurementValue):
    """ Data captured at regular intervals of time. Interval data could be captured as incremental data, absolute data, or relative data. The source for the data is usually a tariff quantity or an engineering quantity. Data is typically captured in time-tagged, uniform, fixed-length intervals of 5, 10, 15, 30, or 60 minutes. Note: Interval Data is sometimes also called 'Interval Data Readings' (IDR).
    """

    # Value of this interval reading.
    value = db.FloatProperty()
    # The 'reading_qualities' property has been implicitly created by
    # the interval_reading' property of ReadingQuality.
    pass
#    interval_blocks = db.ListProperty(db.Key)

#    @property
#    def interval_readings(self):
#        return IntervalBlock.gql("WHERE interval_blocks = :1", self.key())

class DemandResponseProgram(IdentifiedObject):
    """ Demand response program.
    """

    # Type of demand response program; examples are CPP (critical-peak pricing), RTP (real-time pricing), DLC (direct load control), DBP (demand bidding program), BIP (base interruptible program). Note that possible types change a lot and it would be impossible to enumerate them all.
    type = db.StringProperty()
    # Interval within which the program is valid.
    validity_interval = db.ReferenceProperty()
    # The 'end_device_groups' property has been implicitly created by
    # the demand_response_program' property of EndDeviceGroup.
    pass
    # The 'end_device_controls' property has been implicitly created by
    # the demand_response_program' property of EndDeviceControl.
    pass
    # The 'customer_agreements' property has been implicitly created by
    # the demand_response_program' property of CustomerAgreement.
    pass

class ElectricMeteringFunction(DeviceFunction):
    """ Functionality performed by an electric meter.
    """

    # Current transformer ratio used to convert associated quantities to real measurements.
    transformer_ctratio = db.FloatProperty()
    # Customer billing value = meter multiplier * transformer ratios * reading value. The multiplier identifies the scaling value to apply to the reported value after delivery of the tagged item.
    billing_multiplier = db.FloatProperty()
    # True if transformer ratios have been already applied to the associated quantities.
    transformer_ratios_applied = db.BooleanProperty()
    # An additional multiplier that may be used for normalization of the demand value to an hourly value. For example, if the demand interval were set to 15 minutes, the demand multiplier would be 4. If the meter design is such that the demand value reported and displayed is compensated for by the meter itself and no additional scaling is required outside of the meter, the value of the demand multiplier should be '1'.
    demand_multiplier = db.FloatProperty()
    # Meter kWh multiplier, used as a multiplier for a meter register reading to determine the actual amount of usage for which to bill a customer.
    k_wh_multiplier = db.IntegerProperty()
    # Voltage transformer ratio used to convert associated quantities to real measurements.
    transformer_vtratio = db.FloatProperty()
    # True if the billingMultiplier ratio has already been applied to the associated quantities.
    billing_multiplier_applied = db.BooleanProperty()
    # The current class of the meter. Typical current classes in North America are 10, 20, 100, 200, or 320 A.
    current_rating = CurrentFlow
    # The service voltage at which the meter is designed to operate. Typical voltage ratings in North America are 120, 240, 277 or 480V.
    voltage_rating = Voltage
    # Meter kW (pulse) multiplier, used as a multiplier for a meter register reading to determine the actual amount of usage for which to bill a customer.
    k_wmultiplier = db.IntegerProperty()
    # True if the demandMultiplier ratio has already been applied to the associated quantities.
    demand_multiplier_applied = db.BooleanProperty()
#    metering_function_configuration = db.ReferenceProperty()

class MeterAsset(EndDeviceAsset):
    """ Physical asset that performs the metering role of the ServiceDeliveryPoint. Used for measuring consumption and detection of events.
    """

    # Meter kh (watthour) constant. It is the number of watthours that must be applied to the meter to cause one disk revolution for an electromechanical meter or the number of watthours represented by one increment pulse for an electronic meter.
    k_h = db.FloatProperty()
    # Meter form designation per ANSI C12.10 or other applicable standard. An alphanumeric designation denoting the circuit arrangement for which the meter is applicable and its specific terminal arrangement.
    form_number = db.StringProperty()
    # Display multiplier used to produce a displayed value from a register value.
    k_r = db.FloatProperty()
    # The 'meter_service_works' property has been implicitly created by
    # the meter_asset' property of MeterServiceWork.
    pass
#    meter_asset_model = db.ReferenceProperty()
    # The 'meter_readings' property has been implicitly created by
    # the meter_asset' property of MeterReading.
    pass
    # The 'vending_transactions' property has been implicitly created by
    # the meter_asset' property of Transaction.
    pass
    # The 'meter_replacement_works' property has been implicitly created by
    # the old_meter_asset' property of MeterServiceWork.
    pass

class ComFunction(DeviceFunction):
    """ Communication function of communication equipment or a device such as a meter.
    """

    # Communication ID number (e.g. port number, serial number, data collector ID, etc.) of the parent device associated to this AMR module. Note: If someone swaps out a meter, they may inadvertently disrupt the AMR system. Some technologies route readings from nearby meters through a common collection point on an electricity meter. Removal of such a meter disrupts AMR for numerous nearby meters.
    amr_router = db.StringProperty()
    # True when the AMR module can both send and receive messages. Default is false (i.e., module can only send).
    two_way = db.BooleanProperty()
    # Communication ID number (e.g. serial number, IP address, telephone number, etc.) of the AMR module which serves this meter.
    amr_address = db.StringProperty()


