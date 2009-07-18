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
from cim14.iec61968.common import Agreement
from cim14.iec61968.common import Document
from cim14.iec61970.core import Curve

from cim14.iec61970.domain import PerCent
from cim14.iec61970.domain import Money
from cim14.iec61970.domain import AbsoluteDate
from cim14.iec61970.domain import Voltage

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

CustomerBillingKind = db.StringProperty(choices=("separate_ess_udc", "consolidated_udc", "consolidated_ess", "other"))

ns_prefix = "cim.IEC61968.Informative.InfCustomers"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#IEC61968.Informative.InfCustomers"

class PhaseLoad(IdentifiedObject):
    """ Model's load with the unified characteristics. It can be one phase of a multi-phase load and also can be a three-phase load with unified characteristics. The aggregate relationship between DistributionLoad and PhaseLoad allows a distribution load to have any type configuration like single phase, two-phase or three-phase.
    """

    # Percentage of the reactive power of the load which is constant.
    q_constant_power_pct = PerCent
    # Percentage of the active power of the load which has constant impedance.
    p_constant_impedance_pct = PerCent
    # Voltage dependence of the reactive part of the qConstantCurrentPct.
    q_volt_dependance_factor = db.FloatProperty()
    # Voltage dependence of the active part of the pConstantCurrentPct.
    p_volt_dependance_factor = db.FloatProperty()
    # Percentage of the reactive power of the load which has constant impedance.
    q_constant_impedance_pct = PerCent
    # Percentage of the active power of the load which is constant.
    p_constant_power_pct = PerCent
    # Percentage of the reactive power of the load which has constant current.
    q_constant_current_pct = PerCent
    # Percentage of the active power of the load which has constant current.
    p_constant_current_pct = PerCent
#    energy_consumer = db.ReferenceProperty()

class ExternalCustomerAgreement(Agreement):
    """ A type of customer agreement involving an external agency. For example, a customer may form a contracts with an Energy Service Supplier if Direct Access is permitted.
    """

    pass

class CustomerBillingInfo(Document):
    """ The creation of the monthly customer billing statements is the method employed to notify Customers of charges, adjustments and credits applied to their account for Services and Products. The actuall billing occurs through an ErpInvoice. The CustomerBillingInfo includes information from the payment, collection, meter reading, installed meter, service, site, customer, customer account, customer agreement, services and pricing subject areas. Each component price shows up as a separate line item on the ErpInvoice. The Customer Billing Statement may include collection and account messages, marketing/civic event messages and bill inserts. One Customer Billing Statement is produced for all Agreements under a CustomerAccount per billing cycle date defined in 'CustomerAccount.billingCycle'. The history of CustomerBillingInfo, Invoices and Payments is to be maintained in associated ActivityRecords.
    """

    # Outstanding balance on the CustomerAccount as of the statement date.
    out_balance = Money
    # Calculated date upon which a customer billing amount is due, used in the invoicing process to determine when a Customer's Payment is delinquent. It takes into consideration the regulatory criteria and the Customer's requested due date. In the absence of a Customer requested due date, the due date is typically calculated from the regulated number of days and the 'billingDate'.
    due_date = AbsoluteDate
    # Kind of bill customer receives.
    kind = CustomerBillingKind
    # Date of the last payment received from the customer. It is retained in the Customer Billing system, although the details of each payment are tracked in the ERP system.
    last_payment_date = AbsoluteDate
    # Monthly amortized amount due during each billing cycle for the CustomerAccount balance for which the Payment Plan is set-up.
    pymt_plan_amt = Money
    # Amount of the last payment received from the customer. It is retained in the Customer Billing system, although the details of each payment are tracked in the ERP system.
    last_payment_amt = Money
    # Type of payment plan.
    pymt_plan_type = db.StringProperty()
    # Business date designated for the billing run which produced this CustomerBillingInfo.
    billing_date = AbsoluteDate
#    erp_invoice_line_items = db.ListProperty(db.Key)

#    @property
#    def customer_billing_infos(self):
#        return ErpInvoiceLineItem.gql("WHERE erp_invoice_line_items = :1", self.key())
#    customer_account = db.ReferenceProperty()

class OutageHistory(Document):
    """ A document collecting OutageReports, that allows utilities to examine the number of outages suffered by a customer. Also provides data to calculate the total supply interruption to any customer over a given period.
    """

    # The 'outage_reports' property has been implicitly created by
    # the outage_history' property of OutageReport.
    pass

class ServiceGuarantee(Document):
    """ A service guarantee, often imposed by a regulator, defines conditions that, if not satisfied, will result in the utility making a monetary payment to the customer. Note that guarantee's identifier is in the 'name' attribute and the status of the guarantee is in the 'Status.status' attribute. Example service requirements include: 1) If power is not restored within 24 hours, customers can claim $50 for residential customers or $100 for commercial and industrial customers. In addition for each extra period of 12 hours the customer's supply has not been activated, the customer can claim $25. 2) If a customer has a question about their electricity bill, the utility will investigate and respond to the inquiry within 15 working days. If utility fails to meet its guarantee, utility will automatically pay the customer $50.
    """

    # The amount to be paid by the service provider to the customer for each vilations of the 'service Requirement'.
    pay_amount = Money
    # Explanation of the requirement and conditions for satisfying it.
    service_requirement = db.StringProperty()
    # The end of the period in which this service guantee applies.
    end_date = db.DateProperty()
    # The beginning of the period in which this service guantee applies.
    start_date = db.DateProperty()
    # True if utility must autmatically pay the specified amount whenever the condition is not satisified, otherwise customer must make a claim to receive payment.
    automatic_pay = db.BooleanProperty()

class WorkBillingInfo(Document):
    """ Billing information for work performed for the customer. The history of Work Billing Info, Invoices, and Payments is to be maintained in associated ActivityRecords.
    """

    # Amount of price on deposit.
    deposit = Money
    # Date by which payment for bill is expected from client.
    due_date = db.DateProperty()
    # Amount of bill.
    work_price = db.FloatProperty()
    # Date bill was issued to client.
    issue_date = db.DateProperty()
    # Date payment was received from client.
    received_date = db.DateProperty()
    # Estimated cost for work.
    cost_estimate = Money
    # Discount from standard price.
    discount = db.FloatProperty()
#    customer_account = db.ReferenceProperty()
    # The 'works' property has been implicitly created by
    # the work_billing_info' property of Work.
    pass
#    erp_line_items = db.ListProperty(db.Key)

#    @property
#    def work_billing_infos(self):
#        return ErpInvoiceLineItem.gql("WHERE erp_line_items = :1", self.key())

class SubscribePowerCurve(Curve):
    """ Price curve for specifying the cost of energy (X) at points in time (y1) according to a prcing structure, which is based on a tariff.
    """

#    pricing_structure = db.ReferenceProperty()

class PowerQualityPricing(Document):
    """ Pricing can be based on power quality.
    """

    # Value of uninterrupted service (Cost per active power).
    value_uninterrupted_service_p = db.FloatProperty()
    # Threshold minimum power factor for this PricingStructure, specified in instances where a special charge is levied if the actual power factor for a Service falls below the value specified here.
    power_factor_min = db.FloatProperty()
    # Voltage limit violation cost (Cost per unit Voltage).
    volt_limit_viol_cost = db.FloatProperty()
    # Normal low voltage limit.
    normal_low_volt_limit = Voltage
    # Emergency low voltage limit.
    emergency_low_volt_limit = Voltage
    # Value of uninterrupted service (Cost per energy).
    value_uninterrupted_service_energy = db.FloatProperty()
    # Voltage imbalance violation cost (Cost per unit Voltage).
    volt_imbalance_viol_cost = db.FloatProperty()
    # Emergency high voltage limit.
    emergency_high_volt_limit = Voltage
    # Normal high voltage limit.
    normal_high_volt_limit = Voltage
#    pricing_structure = db.ReferenceProperty()
#    service_delivery_points = db.ListProperty(db.Key)

#    @property
#    def power_quality_pricings(self):
#        return ServiceDeliveryPoint.gql("WHERE service_delivery_points = :1", self.key())

class StandardIndustryCode(Document):
    """ The Standard Industrial Classification (SIC) are the codes that identify the type of products/service an industry is involved in, and used for statutory reporting purposes. For example, in the USA these codes are located by the federal government, and then published in a book entitled 'The Standard Industrial Classification Manual'. The codes are arranged in a hierarchical structure. Note that Residential Service Agreements are not classified according to the SIC codes.
    """

    # Standard alphanumeric code assigned to a particular product/service within an industry.
    code = db.StringProperty()
    # The 'customer_agreements' property has been implicitly created by
    # the standard_industry_code' property of CustomerAgreement.
    pass


