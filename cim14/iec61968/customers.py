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

from cim14.iec61968.common import Organisation
from cim14.iec61968.common import Location
from cim14.iec61968.common import Agreement
from cim14.iec61968.common import Document
from cim14.iec61970.core import IdentifiedObject

from cim14.iec61970.domain import AbsoluteDate

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

RevenueKind = db.StringProperty(choices=("residential", "industrial", "non_residential", "irrigation", "commercial", "street_light", "other"))

ServiceKind = db.StringProperty(choices=("refuse", "electricty", "other", "water", "tv_licence", "sewerage", "time", "internet", "gas", "rates", "heat"))

CustomerKind = db.StringProperty(choices=("energy_service_scheduler", "wind_machine", "residential_and_commercial", "internal_use", "residential_streetlight_others", "energy_service_supplier", "commercial_industrial", "other", "pumping_load", "residential_and_streetlight", "residential", "residential_farm_service"))

ns_prefix = "cim.IEC61968.Customers"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#IEC61968.Customers"

class Customer(Organisation):
    """ Organisation receiving services from ServiceSupplier.
    """

    # True if this is an important customer. Importance is for matters different than those in 'specialNeed' attribute.
    vip = db.BooleanProperty()
    # (if applicable) Public Utility Commission identification number.
    puc_number = db.StringProperty()
    # Kind of customer.
    kind = CustomerKind
    # True if customer organisation has special service needs such as life support, hospitals, etc.
    special_need = db.StringProperty()
    # Status of this customer.
    status = db.ReferenceProperty()
    # The 'customer_agreements' property has been implicitly created by
    # the customer' property of CustomerAgreement.
    pass
#    works = db.ListProperty(db.Key)

#    @property
#    def customers(self):
#        return Work.gql("WHERE works = :1", self.key())
#    planned_outage = db.ReferenceProperty()
    # The 'erp_persons' property has been implicitly created by
    # the customer_data' property of ErpPerson.
    pass
#    outage_notifications = db.ListProperty(db.Key)

#    @property
#    def customer_datas(self):
#        return OutageNotification.gql("WHERE outage_notifications = :1", self.key())
    # The 'trouble_tickets' property has been implicitly created by
    # the customer_data' property of TroubleTicket.
    pass
    # The 'end_device_assets' property has been implicitly created by
    # the customer' property of EndDeviceAsset.
    pass

class ServiceLocation(Location):
    """ A customer ServiceLocation has one or more ServiceDeliveryPoint(s), which in turn relate to Meters. The location may be a point or a polygon, depending on the specific circumstances. For distribution, the ServiceLocation is typically the location of the utility customer's premise. Because a customer's premise may have one or more meters, the ServiceDeliveryPoint is used to define the actual conducting equipment that the EndDeviceAsset attaches to at the utility customer's ServiceLocation. For transmission, it is the point(s) of interconnection on the transmission provider's transmission system where capacity and/or energy transmitted by the transmission provider is made available to the receiving party.
    """

    # Problems previously encountered when visiting or performing work on this site. Examples include: bad dog, viloent customer, verbally abusive occupant, obstructions, safety hazards, etc.
    site_access_problem = db.StringProperty()
    # Method for the service person to access the appropriate service locations. For example, a description of where to obtain a key if the facility is unmanned and secured.
    access_method = db.StringProperty()
    # True if inspection is needed of facilities at this service location. This could be requested by a customer, due to suspected tampering, environmental concerns (e.g., a fire in the vicinity), or to correct incompatible data.
    needs_inspection = db.BooleanProperty()
    # The 'service_delivery_points' property has been implicitly created by
    # the service_location' property of ServiceDeliveryPoint.
    pass
#    customer_agreements = db.ListProperty(db.Key)

#    @property
#    def service_locations(self):
#        return CustomerAgreement.gql("WHERE customer_agreements = :1", self.key())
    # The 'end_device_assets' property has been implicitly created by
    # the service_location' property of EndDeviceAsset.
    pass

class CustomerAgreement(Agreement):
    """ Agreement between the Customer and the ServiceSupplier to pay for service at a specific ServiceLocation. It records certain billing information about the type of service provided at the ServiceLocation and is used during charge creation to determine the type of service.
    """

    # The 'service_delivery_points' property has been implicitly created by
    # the customer_agreement' property of ServiceDeliveryPoint.
    pass
#    customer = db.ReferenceProperty()
#    service_supplier = db.ReferenceProperty()
#    customer_account = db.ReferenceProperty()
#    standard_industry_code = db.ReferenceProperty()
    # The 'end_device_controls' property has been implicitly created by
    # the customer_agreement' property of EndDeviceControl.
    pass
#    service_category = db.ReferenceProperty()
#    equipments = db.ListProperty(db.Key)

#    @property
#    def customer_agreements(self):
#        return Equipment.gql("WHERE equipments = :1", self.key())
    # The 'auxiliary_agreements' property has been implicitly created by
    # the customer_agreement' property of AuxiliaryAgreement.
    pass
#    service_locations = db.ListProperty(db.Key)

#    @property
#    def customer_agreements(self):
#        return ServiceLocation.gql("WHERE service_locations = :1", self.key())
#    pricing_structures = db.ListProperty(db.Key)

#    @property
#    def customer_agreements(self):
#        return PricingStructure.gql("WHERE pricing_structures = :1", self.key())
#    demand_response_program = db.ReferenceProperty()
    # The 'meter_readings' property has been implicitly created by
    # the customer_agreement' property of MeterReading.
    pass

class CustomerAccount(Document):
    """ Assignment of a group of products and services purchased by the Customer through a CustomerAgreement, used as a mechanism for customer billing and payment. It contains common information from the various types of CustomerAgreements to create billings (invoices) for a Customer and receive payment.
    """

    # Budget bill code.
    budget_bill = db.StringProperty()
    # Cycle day on which this customer account will normally be billed, used to determine when to produce the CustomerBillingInfo for this customer account.
    billing_cycle = db.StringProperty()
    # The 'customer_billing_infos' property has been implicitly created by
    # the customer_account' property of CustomerBillingInfo.
    pass
    # The 'payment_transactions' property has been implicitly created by
    # the customer_account' property of Transaction.
    pass
    # The 'erp_invoicees' property has been implicitly created by
    # the customer_account' property of ErpInvoice.
    pass
    # The 'work_billing_infos' property has been implicitly created by
    # the customer_account' property of WorkBillingInfo.
    pass
    # The 'customer_agreements' property has been implicitly created by
    # the customer_account' property of CustomerAgreement.
    pass

class Tariff(Document):
    """ Document, approved by the responsible regulatory agency, listing the terms and conditions, including a schedule of prices, under which utility services will be provided. It has a unique number within the state or province. For Rate Schedules it is frequently allocated by the affiliated Public Utilities Commission.
    """

    # Date tarrif was activated.
    start_date = AbsoluteDate
    # (if tariff became inactive) Date tarrif was terminated.
    end_date = AbsoluteDate
#    pricing_structures = db.ListProperty(db.Key)

#    @property
#    def tariffs(self):
#        return PricingStructure.gql("WHERE pricing_structures = :1", self.key())
#    tariff_profiles = db.ListProperty(db.Key)

#    @property
#    def tariffs(self):
#        return TariffProfile.gql("WHERE tariff_profiles = :1", self.key())

class ServiceCategory(IdentifiedObject):
    """ Category of service provided to the customer.
    """

    # Kind of service.
    kind = ServiceKind
    # The 'pricing_structures' property has been implicitly created by
    # the service_category' property of PricingStructure.
    pass
    # The 'customer_agreements' property has been implicitly created by
    # the service_category' property of CustomerAgreement.
    pass
    # The 'service_delivery_points' property has been implicitly created by
    # the service_category' property of ServiceDeliveryPoint.
    pass
    # The 'spaccounting_functions' property has been implicitly created by
    # the service_kind' property of SDPAccountingFunction.
    pass

class PricingStructure(Document):
    """ Grouping of pricing components and prices used in the creation of customer charges and the eligibility criteria under which these terms may be offered to a customer. The reasons for grouping include state, customer classification, site characteristics, classification (i.e. fee price structure, deposit price structure, electric service price structure, etc.) and accounting requirements.
    """

    # Absolute minimum valid non-demand usage quantity used in validating a customer's billed non-demand usage.
    daily_floor_usage = db.IntegerProperty()
    # Absolute maximum valid non-demand usage quantity used in validating a customer's billed non-demand usage.
    daily_ceiling_usage = db.IntegerProperty()
    # True if this pricing structure is not taxable.
    tax_exemption = db.BooleanProperty()
    # Unique user-allocated key for this pricing structure, used by company representatives to identify the correct price structure for allocating to a customer. For rate schedules it is often prefixed by a state code.
    code = db.StringProperty()
    # Used in place of actual computed estimated average when history of usage is not available, and typically manually entered by customer accounting.
    daily_estimated_usage = db.IntegerProperty()
    # (Accounting) Kind of revenue, often used to determine the grace period allowed, before collection actions are taken on a customer (grace periods vary between revenue classes).
    revenue_kind = RevenueKind
#    subscribe_power_curve = db.ReferenceProperty()
#    service_delivery_points = db.ListProperty(db.Key)

#    @property
#    def pricing_structures(self):
#        return ServiceDeliveryPoint.gql("WHERE service_delivery_points = :1", self.key())
#    customer_agreements = db.ListProperty(db.Key)

#    @property
#    def pricing_structures(self):
#        return CustomerAgreement.gql("WHERE customer_agreements = :1", self.key())
    # The 'transactions' property has been implicitly created by
    # the pricing_structure' property of Transaction.
    pass
#    tariffs = db.ListProperty(db.Key)

#    @property
#    def pricing_structures(self):
#        return Tariff.gql("WHERE tariffs = :1", self.key())
    # The 'power_quality_pricings' property has been implicitly created by
    # the pricing_structure' property of PowerQualityPricing.
    pass
#    service_category = db.ReferenceProperty()


