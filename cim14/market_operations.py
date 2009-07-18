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
from cim14.iec61968.informative.inf_erpsupport import ErpOrganisation
from cim14.iec61970.core import Curve
from cim14.iec61968.common import Agreement
from cim14 import Element
from cim14.energy_scheduling import Profile
from cim14.iec61968.common import Document
from cim14.iec61970.core import PowerSystemResource
from cim14.iec61970.core import RegularIntervalSchedule
from cim14.iec61970.meas import Limit

from cim14.iec61970.domain import ActivePower
from cim14.iec61970.domain import Money
from cim14.iec61970.domain import Minutes
from cim14.iec61970.domain import CostPerEnergyUnit

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

ns_prefix = "cim.MarketOperations"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#MarketOperations"

class RegisteredResource(IdentifiedObject):
    """ A resource that is registered through the RTO participant registration system. Examples include generating unit, customer meter, and a non-physical generator or load.
    """

    # Unique name obtained via RTO registration
    rto_id = db.StringProperty()
#    resource_groups = db.ListProperty(db.Key)

#    @property
#    def registered_resources(self):
#        return ResourceGroup.gql("WHERE resource_groups = :1", self.key())
#    organisation = db.ReferenceProperty()
#    pnode = db.ReferenceProperty()
    # The 'meters' property has been implicitly created by
    # the registered_resource' property of Meter.
    pass
#    market_products = db.ListProperty(db.Key)

#    @property
#    def registered_resources(self):
#        return MarketProduct.gql("WHERE market_products = :1", self.key())
#    markets = db.ListProperty(db.Key)

#    @property
#    def registered_resources(self):
#        return Market.gql("WHERE markets = :1", self.key())

class RTO(ErpOrganisation):
    """ Regional transmission operator.
    """

    # The 'security_constraints_linear' property has been implicitly created by
    # the rto' property of SecurityConstraintSum.
    pass
#    resource_group_reqs = db.ListProperty(db.Key)

#    @property
#    def rtos(self):
#        return ResourceGroupReq.gql("WHERE resource_group_reqs = :1", self.key())
    # The 'security_constraints' property has been implicitly created by
    # the rto' property of SecurityConstraints.
    pass
    # The 'markets' property has been implicitly created by
    # the rto' property of Market.
    pass
    # The 'pnodes' property has been implicitly created by
    # the rto' property of Pnode.
    pass

class Meter(IdentifiedObject):
    """ This is generic logical meter object.
    """

#    registered_resource = db.ReferenceProperty()

class ContingencyConstraintLimit(Curve):
    """ Possibly time-varying max MW or MVA and optionally Min MW limit or MVA limit (Y1 and Y2, respectively) assigned to a constraint for a specific contingency. Use CurveSchedule XAxisUnits to specify MW or MVA.
    """

#    mwlimit_schedules = db.ReferenceProperty()
#    contingency = db.ReferenceProperty()
#    security_constraint_sum = db.ReferenceProperty()

class BidPriceCurve(Curve):
    """ Relationship between unit operating price in $/hour (Y-axis) and unit output in MW (X-axis).
    """

    # The 'product_bids' property has been implicitly created by
    # the bid_price_curve' property of ProductBid.
    pass

class FTR(Agreement):
    """ Financial Transmission Rights (FTR) regarding transmission capacity at a flowgate.
    """

    # Peak, Off-peak, 24-hour
    class = db.StringProperty()
    # Type of rights being offered (product) allowed to be auctioned (option, obligation).
    ftr_type = db.StringProperty()
    # Fixed (covers re-configuration, grandfathering) or Optimized (up for sale/purchase
    optimized = db.StringProperty()
    # Buy, Sell
    action = db.StringProperty()
    # Quantity, typically MWs - Seller owns all rights being offered, MWs over time on same Point of Receipt, Point of Delivery, or Resource.
    base_energy = ActivePower
#    flowgate = db.ReferenceProperty()
#    pnodes = db.ListProperty(db.Key)

#    @property
#    def ftrs(self):
#        return Pnode.gql("WHERE pnodes = :1", self.key())
#    energy_price_curve = db.ReferenceProperty()

class ChargeProfileData(Element):
    # The date and time of an interval.
    time_stamp = db.DateProperty()
    # The value of an interval given a profile type (amount, price, or quantity), subject to the UOM.
    value = db.FloatProperty()
    # The sequence number of the profile.
    sequence = db.IntegerProperty()
#    charge_profile = db.ReferenceProperty()
#    bill_determinant = db.ReferenceProperty()

class TransmissionReliabilityMargin(IdentifiedObject):
    """ Transmission Reliability Margin (TRM) is defined as that amount of transmission transfer capability necessary to ensure that the interconnected transmission network is secure under a reasonable range of uncertainties in system conditions.
    """

    # Value of the TRM
    trm_value = db.FloatProperty()
    # the type of TRM
    trm_type = db.StringProperty()
    # unit of the TRM value. Could be MW or Percentage.
    value_unit = db.StringProperty()
    # The 'flowgate' property has been implicitly created by
    # the transmission_reliability_margin' property of Flowgate.
    pass

class UnitInitialConditions(IdentifiedObject):
    """ Resource status at the end of a given clearing period.
    """

    # Cumulative number of status changes of the resource.
    cum_status_changes = db.IntegerProperty()
    # Resource status at the end of previous clearing period:  0 - off-line  1 - on-line production  2 - in shutdown process  3 - in startup process
    resource_status = db.IntegerProperty()
    # Time in market trading intervals the resource is in the state as of the end of the previous clearing period.
    time_in_status = Minutes
    # Resource MW output at the end of previous clearing period.
    resource_mw = ActivePower
    # Time and date for resourceStatus
    status_date = db.DateProperty()
#    generating_unit = db.ReferenceProperty()

class Pnode(IdentifiedObject):
    """ A pricing node is directly associated with a connectivity node.  It is a pricing location for which market participants submit their bids, offers, buy/sell CRRs, and settle.
    """

    # End date-time of the period in which the price node definition is valid
    end_period = db.DateProperty()
    # True=Public; False=Private Public Pnodes: Prices are published for DA/RT and FTR Markets. Private Pnodes: Location is not usable by Market for Bidding/FTRs/Transactions
    is_public = db.BooleanProperty()
    # Price node type: Hub (H), Zone (Z), Control Area (C), ?, Bus (B)
    type = db.StringProperty()
    # Price node usage:  'Control Area' 'Regulation Region' 'Price Zone' 'Spin Region' 'Non-Spin Region' 'Price Hub'
    usage = db.StringProperty()
    # Start date-time of the period in which the price node definition is valid.
    begin_period = db.DateProperty()
#    connectivity_node = db.ReferenceProperty()
#    rto = db.ReferenceProperty()
    # The 'measurements' property has been implicitly created by
    # the pnode' property of Measurement.
    pass
    # The 'receipt_transaction_bids' property has been implicitly created by
    # the receipt_pnode' property of TransactionBid.
    pass
#    pnode_clearing = db.ReferenceProperty()
#    ftrs = db.ListProperty(db.Key)

#    @property
#    def pnodes(self):
#        return FTR.gql("WHERE ftrs = :1", self.key())
    # The 'registered_resources' property has been implicitly created by
    # the pnode' property of RegisteredResource.
    pass
    # The 'delivery_transaction_bids' property has been implicitly created by
    # the delivery_pnode' property of TransactionBid.
    pass

class CapacityBenefitMargin(Profile):
    """ Capacity Benefit Margin (CBM) is defined as that amount of transmission transfer capability reserved by load serving entities to ensure access to generation from interconnected systems to meet generation reliability requirements. Reservation fo CBM by a load serving entity allows that entity to reduce its installed generating capacity below that which may otherwise have been necessary without interconnections to meet its generation reliability requirements.  CBM is modeled as a profile with values in different time periods which are represented by the profile data.
    """

#    season = db.ReferenceProperty()
#    flowgate = db.ListProperty(db.Key)

#    @property
#    def capacity_benefit_margin(self):
#        return Flowgate.gql("WHERE flowgate = :1", self.key())

class EnergyPriceCurve(Curve):
    """ Relationship between a price in $/hour (Y-axis) and a MW value (X-axis).
    """

    # The 'ftrs' property has been implicitly created by
    # the energy_price_curve' property of FTR.
    pass
#    energy_transactions = db.ListProperty(db.Key)

#    @property
#    def energy_price_curves(self):
#        return EnergyTransaction.gql("WHERE energy_transactions = :1", self.key())

class MarketProduct(IdentifiedObject):
    """ A product traded by an RTO (e.g., energy, 10 minute spinning reserve).  Ancillary service product examples include: Regulation Up Regulation Dn Spinning Reserve Non-Spinning Reserve Operating Reserve
    """

    # The 'reserve_reqs' property has been implicitly created by
    # the market_product' property of ReserveReq.
    pass
    # The 'product_bids' property has been implicitly created by
    # the market_product' property of ProductBid.
    pass
#    registered_resources = db.ListProperty(db.Key)

#    @property
#    def market_products(self):
#        return RegisteredResource.gql("WHERE registered_resources = :1", self.key())
#    market = db.ReferenceProperty()

class BilateralTransaction(Element):
    """ Bilateral transaction
    """

    # Maximum total transmission (congestion) charges in monetary units
    total_tran_charge_max = Money
    # Transaction scope: 'Internal' 'External'
    scope = db.StringProperty()
    # Market type (default=DA) DA - Day Ahead RT - Real Time HA - Hour Ahead
    market_type = db.StringProperty()
    # Minimum curtailment time in number of trading intervals
    curtail_time_min = db.IntegerProperty()
    # Maximum purchase time in number of trading intervals
    purchase_time_max = db.IntegerProperty()
    # Maximum curtailment time in number of trading intervals
    curtail_time_max = db.IntegerProperty()
    # Transaction type (default 1)  1 - Fixed  2 - Dispatchable continuous  3 - Dispatchable block-loading
    transaction_type = db.StringProperty()
    # Minimum purchase time in number of trading intervals
    purchase_time_min = db.IntegerProperty()

class PassThroughBill(Document):
    """ Pass Through Bill is used for: 1)Two sided charge transactions with or without ISO involvement (hence the ?pass thru?) 2) Specific direct charges or payments that are calculated outside or provided directly to settlements 3) Specific charge bill determinants that are externally supplied and used in charge calculations
    """

    # Disputed transaction indicator
    is_disputed = db.BooleanProperty()
    # Bill period end date
    bill_end = db.DateProperty()
    # The previous bill period start date
    previous_start = db.DateProperty()
    # The settlement run type, for example: prelim, final, and rerun.
    bill_run_type = db.StringProperty()
    # The product identifier for determining the charge type of the transaction.
    product_code = db.StringProperty()
    # The date the transaction occurs.
    transaction_date = db.DateProperty()
    # The trade date
    trade_date = db.DateProperty()
    # The time zone code
    time_zone = db.StringProperty()
    # A flag indicating whether there is a profile data associated with the PTB.
    is_profiled = db.BooleanProperty()
    # The start date of service provided, if periodic.
    service_start = db.DateProperty()
    # The tax on services taken.
    tax_amount = Money
    # The effective date of the transaction
    effective_date = db.DateProperty()
    # The company to which the PTB transaction is paid.
    paid_to = db.StringProperty()
    # The price of product/service.
    price = Money
    # The company to which the PTB transaction is sold.
    sold_to = db.StringProperty()
    # The type of transaction. For example, charge customer, bill customer, matching AR/AP, or bill determinant
    transaction_type = db.StringProperty()
    # The end date of service provided, if periodic.
    service_end = db.DateProperty()
    # The company by which the PTB transaction service is provided.
    provided_by = db.StringProperty()
    # The previous bill period end date
    previous_end = db.DateProperty()
    # Bill period start date
    bill_start = db.DateProperty()
    # The charge amount of the product/service.
    amount = Money
    # The company to which the PTB transaction is billed.
    billed_to = db.StringProperty()
#    market_statement_line_item = db.ReferenceProperty()
    # The 'charge_profiles' property has been implicitly created by
    # the pass_trough_bill' property of ChargeProfile.
    pass
#    user_attributes = db.ListProperty(db.Key)

#    @property
#    def pass_through_bills(self):
#        return UserAttribute.gql("WHERE user_attributes = :1", self.key())

class RampRateCurve(Curve):
    """ Ramp rate as a function of resource MW output
    """

    # How ramp rate is applied (e.g., raise or lower, as when applied to a generation resource)
    ramp_rate_type = db.StringProperty()
#    generating_unit = db.ListProperty(db.Key)

#    @property
#    def ramp_rate_curves(self):
#        return RegisteredGenerator.gql("WHERE generating_unit = :1", self.key())

class Bid(Document):
    """ Represents both bids to purchase and offers to sell energy or ancillary services in an RTO-sponsored market.
    """

    # Stop time and date for which bid is applicable.
    stop_time = db.DateProperty()
    # Start time and date for which bid applies.
    start_time = db.DateProperty()
    market_type = db.StringProperty()
#    bid_clearing = db.ReferenceProperty()
#    market = db.ReferenceProperty()
    # The 'product_bids' property has been implicitly created by
    # the bid' property of ProductBid.
    pass

class ChargeProfile(Profile):
    """ A type of profile for financial charges
    """

    # The unit of measure applied to the value attribute of the profile data.
    unit_of_measure = db.StringProperty()
    # The calculation frequency, daily or monthly.
    frequency = db.StringProperty()
    # The type of profile.  It could be amount, price, or quantity.
    type = db.StringProperty()
    # The number of intervals in the profile data.
    number_interval = db.IntegerProperty()
    # The 'charge_profile_data' property has been implicitly created by
    # the charge_profile' property of ChargeProfileData.
    pass
#    pass_trough_bill = db.ReferenceProperty()
#    bill_determinant = db.ReferenceProperty()

class ResourceGroupReq(IdentifiedObject):
    """ Ancillary service requirements for a market.
    """

#    rtos = db.ListProperty(db.Key)

#    @property
#    def resource_group_reqs(self):
#        return RTO.gql("WHERE rtos = :1", self.key())
#    resource_group = db.ReferenceProperty()

class Market(IdentifiedObject):
    """ Market (e.g., DAM, HAM)  zzMarket operation control parameters.
    """

    # Market start time.
    start = db.DateProperty()
    # Market end time.
    end = db.DateProperty()
    # True if daylight savings time (DST) is in effect.
    dst = db.BooleanProperty()
    # Trading time interval length.
    time_interval_length = Minutes
    # Local time zone.
    local_time_zone = db.StringProperty()
    # Ramping time interval for energy.
    ramp_interval_energy = Minutes
    # Ramping time interval for spinning reserve.
    ramp_interval_spin_res = Minutes
    # The type of a market.
    type = db.StringProperty()
    # Ramping time interval for regulation.
    ramp_interval_reg = Minutes
    # Ramping time interval for non-spinning reserve.
    ramp_interval_non_spin_res = Minutes
    # The 'market_products' property has been implicitly created by
    # the market' property of MarketProduct.
    pass
#    registered_resources = db.ListProperty(db.Key)

#    @property
#    def markets(self):
#        return RegisteredResource.gql("WHERE registered_resources = :1", self.key())
#    rto = db.ReferenceProperty()
    # The 'settlements' property has been implicitly created by
    # the market' property of Settlement.
    pass
    # The 'bids' property has been implicitly created by
    # the market' property of Bid.
    pass
    # The 'market_factors' property has been implicitly created by
    # the market' property of MarketFactors.
    pass

class ConstraintTerm(IdentifiedObject):
    """ A constraint term is one element of a linear constraint.
    """

    # The function is an enumerated value that can be 'active', 'reactive', or 'VA' to indicate the type of flow.
    function = db.StringProperty()
    factor = db.StringProperty()
#    security_constraint_sum = db.ReferenceProperty()

class MarketStatementLineItem(IdentifiedObject):
    """ An individual line item on a statement.
    """

    # The unit of measure for the quantity element of the line item.
    quantity_uom = db.StringProperty()
    # Previous settlement price.
    previsou_price = db.FloatProperty()
    # Net ISO settlement amount.
    net_isoamount = db.FloatProperty()
    # Previous ISO settlement quantity.
    previous_isoquantity = db.FloatProperty()
    # Current ISO settlement quantity.
    current_isoquantity = db.FloatProperty()
    # Net settlement quantity, subject to the UOM.
    net_quantity = db.FloatProperty()
    # Previous ISO settlement amount.
    previous_isoamount = db.FloatProperty()
    # Net settlement price.
    net_price = db.FloatProperty()
    # Previous settlement amount.
    previous_amount = db.FloatProperty()
    # Net settlement amount.
    net_amount = db.FloatProperty()
    # Previous settlement quantity, subject to the UOM.
    previous_quantity = db.FloatProperty()
    # Current settlement quantity, subject to the UOM.
    current_quantity = db.FloatProperty()
    # Net ISO settlement quantity.
    net_isoquantity = db.FloatProperty()
    # Current ISO settlement amount.
    current_isoamount = db.FloatProperty()
    # The number of intervals.
    interval_number = db.StringProperty()
    # Current settlement price.
    current_price = db.FloatProperty()
    # The date of which the settlement is run.
    interval_date = db.DateProperty()
    # Current settlement amount.
    current_amount = db.FloatProperty()
    # The 'component_market_statement_line_item' property has been implicitly created by
    # the container_market_statement_line_item' property of MarketStatementLineItem.
    pass
#    user_attributes = db.ListProperty(db.Key)

#    @property
#    def erp_statement_line_items(self):
#        return UserAttribute.gql("WHERE user_attributes = :1", self.key())
#    pass_through_bill = db.ReferenceProperty()
#    market_statement = db.ReferenceProperty()
#    container_market_statement_line_item = db.ReferenceProperty()

class MWLimitSchedule(Curve):
    """ Maximum MW and optionally Minimum MW (Y1 and Y2, respectively)
    """

#    security_constraint_limit = db.ReferenceProperty()

class ProductBid(IdentifiedObject):
    """ Component of a bid that pertains to one market product.
    """

#    bid = db.ReferenceProperty()
#    product_bid_clearing = db.ReferenceProperty()
#    bid_price_curve = db.ReferenceProperty()
#    market_product = db.ReferenceProperty()

class SecurityConstraints(IdentifiedObject):
    """ Typical for regional transmission operators (RTOs), these constraints include transmission as well as generation group constraints identified in both base case and critical contingency cases.
    """

    # Maximum MW limit
    max_mw = ActivePower
    # Minimum MW limit (only for transmission constraints).
    min_mw = ActivePower
    # Actual branch or group of branches MW flow (only for transmission constraints)
    actual_mw = ActivePower
#    rto = db.ReferenceProperty()

class MarketStatement(Document):
    """ A statement is a roll up of statement line items. Each statement along with its line items provide the details of specific charges at any given time.
    """

    # The date of which this statement is issued.
    transaction_date = db.DateProperty()
    # The start of a bill period.
    start = db.DateProperty()
    # The end of a bill period.
    end = db.DateProperty()
    # The version number of previous statement (in the case of true up).
    reference_number = db.StringProperty()
    # The date of which Settlement is run.
    trade_date = db.DateProperty()
    # The 'market_statement_line_item' property has been implicitly created by
    # the market_statement' property of MarketStatementLineItem.
    pass

class SensitivityPriceCurve(Curve):
    """ Optionally, this curve expresses elasticity of the associated requirement.  For example, used to reduce requirements when clearing price exceeds reasonable values when the supply quantity becomes scarce.  For example, a single point value of $1000/MW for a spinning reserve will cause a reduction in the required spinning reserve.  X axis is constrained quantity (e.g., MW) Y1 axis is money per constrained quantity
    """

#    reserve_req = db.ReferenceProperty()

class Settlement(Document):
    """ Specifies a settlement run.
    """

    # The trade date on which the settlement is run.
    trade_date = db.DateProperty()
#    market = db.ReferenceProperty()
#    erp_invoice_line_items = db.ListProperty(db.Key)

#    @property
#    def settlements(self):
#        return ErpInvoiceLineItem.gql("WHERE erp_invoice_line_items = :1", self.key())
#    erp_ledger_entries = db.ListProperty(db.Key)

#    @property
#    def settlements(self):
#        return ErpLedgerEntry.gql("WHERE erp_ledger_entries = :1", self.key())

class BillDeterminant(Document):
    # The version of configuration of calculation logic in the settlement.
    config_version = db.StringProperty()
    # Number of intervals of bill determiant in trade day, eg 300 for five minute intervals.
    number_interval = db.IntegerProperty()
    # The level of precision in the current value.
    precision_level = db.StringProperty()
    # The UOM for the current value of the Bill Determinant.
    unit_of_measure = db.StringProperty()
    # Level in charge calculation order.
    calculation_level = db.StringProperty()
    # The 'charge_profile_data' property has been implicitly created by
    # the bill_determinant' property of ChargeProfileData.
    pass
#    charge_profile = db.ReferenceProperty()
#    user_attributes = db.ListProperty(db.Key)

#    @property
#    def bill_determinants(self):
#        return UserAttribute.gql("WHERE user_attributes = :1", self.key())

class MarketFactors(Document):
    """ Aggregation of market information relative for a specific time interval.
    """

    # The start of the time interval for which requirement is defined.
    interval_start_time = db.DateProperty()
#    market = db.ReferenceProperty()
#    erp_invoices = db.ListProperty(db.Key)

#    @property
#    def market_factors(self):
#        return ErpInvoiceLineItem.gql("WHERE erp_invoices = :1", self.key())
#    activity_records = db.ListProperty(db.Key)

#    @property
#    def market_factors(self):
#        return ActivityRecord.gql("WHERE activity_records = :1", self.key())

class DefaultConstraintLimit(Curve):
    """ Possibly time-varying max MW or MVA and optionally Min MW limit or MVA limit (Y1 and Y2, respectively) applied as a default value if no specific constraint limits are specified for a contingency analysis. Use CurveSchedule XAxisUnits to specify MW or MVA.
    """

#    security_constraint_sum = db.ReferenceProperty()

class SchedulingCoordinator(ErpOrganisation):
    """ In certain ISO/RTO operations, market participants are represented by Scheduling Coordinators (SCs) that are registered with the ISO/RTO. One participant can register multiple SCs with the ISO/RTO.  Many participants can do business with the ISO/RTO using a single SC. Each generator resource can only be scheduled by one SC. One SC can schedule multiple generators. A load scheduling point can be used by multiple SCs. Each SC can schedule load at multiple scheduling points. Each SC can have more than one load schedule at any load scheduling point as long as each load schedule at the same load scheduling point has a separate resource ID and settlement-quality meter. An inter-tie scheduling point can be used by multiple SCs. Each SC can schedule interchange at multiple inter-tie scheduling points. An SC can have multiple interchange schedules at the same inter-tie scheduling point by assigning a unique interchange identifier to each interchange schedule.
    """

    pass

class BidSet(IdentifiedObject):
    """ As set of mutually exclusive bids for which a maximum of one may be scheduled. Of these generating bids, only one generating bid can be scheduled at a time.
    """

    # The 'generating_bids' property has been implicitly created by
    # the bid_set' property of GeneratingBid.
    pass

class LoadReductionPriceCurve(Curve):
    """ This is the price sensitivity that bidder expresses for allowing market load interruption.  Relationship between price (Y1-axis) vs. MW (X-axis).
    """

    # The 'load_bids' property has been implicitly created by
    # the load_reduction_price_curve' property of LoadBid.
    pass

class BidClearing(Element):
    """ Bid clearing results posted for a given settlement period.
    """

    # Energy lost opportunity cost in monetary units.
    lost_op_cost = Money
    # Start up cost in case of energy commodity in monetary units.
    start_up_cost = Money
    # No-load cost in monetary units.
    no_load_cost = Money
#    bid = db.ReferenceProperty()

class Flowgate(PowerSystemResource):
    """ A flowgate, is single or group of transmission elements intended to model MW flow impact relating to transmission limitations and transmission service usage.
    """

    # Flag to indicate if Flowgate qualified as coordinated Flowgate
    coordinated_flag = db.BooleanProperty()
    # Flag to indicate if Flowgate qualified as reciprocal Flowgate
    reciprocal_flag = db.BooleanProperty()
    # Date at which point Flowgate becomes active.  Used to insert future Flowgates or Flowgates returning from an outage condition.
    in_service_date = db.DateProperty()
    # Percentage of counterflow to remove/exclude from the AFC calculation.  Integer.  Must be 100 or less.
    counter_flow_value = db.IntegerProperty()
    # Flag to indicate if Flowgate is utilized for coordination of ATC.
    atc_flag = db.BooleanProperty()
    # Date at which point Flowgate becomes inactive. Used to insert outage condition.
    out_of_service_date = db.DateProperty()
    # Standard Reliabilty Entity (e.g. in North America NERC) that has agreed per a reciprocal agreement to manage coordination on the Flowgate.  Will always be either True or False - if not a reciprocal Flowgate, will be false.
    managing_entity_flag = db.BooleanProperty()
    # The Registered Name utilized in the IDC and/or Book of Flowgates
    idc_operational_name = db.StringProperty()
    # Percentage of positive impact to include in the AFC calculation.  Integer.  Must be 100 or less.
    positive_impact_value = db.IntegerProperty()
    # Date upon which study of Flowgate to determine coordinated status was performed.  May be null is no study undertaken yet.
    coordination_study_date = db.DateProperty()
    # The registered Flowgate ID Assigned by the IDC and/or Book of Flowgate.
    idc_assigned_id = db.IntegerProperty()
    # Date at which point Flowgate should be removed from the Interchange Distribution Calculatin (IDC).
    deletion_date = db.DateProperty()
#    transmission_provider = db.ListProperty(db.Key)

#    @property
#    def flowgate(self):
#        return TransmissionProvider.gql("WHERE transmission_provider = :1", self.key())
#    sub_control_area = db.ReferenceProperty()
    # The 'ftrs' property has been implicitly created by
    # the flowgate' property of FTR.
    pass
#    lines = db.ListProperty(db.Key)

#    @property
#    def flowgates(self):
#        return Line.gql("WHERE lines = :1", self.key())
#    capacity_benefit_margin = db.ListProperty(db.Key)

#    @property
#    def flowgate(self):
#        return CapacityBenefitMargin.gql("WHERE capacity_benefit_margin = :1", self.key())
#    transmission_reliability_margin = db.ReferenceProperty()
    # The 'violation_limits' property has been implicitly created by
    # the flowgate' property of ViolationLimit.
    pass
#    power_transormers = db.ListProperty(db.Key)

#    @property
#    def flowgates(self):
#        return PowerTransformer.gql("WHERE power_transormers = :1", self.key())

class NotificationTimeCurve(Curve):
    """ Notification time curve as a function of down time.  Relationship between crew notification time (Y1-axis) and unit startup time (Y2-axis) vs. unit elapsed down time (X-axis).
    """

    # The 'generating_bids' property has been implicitly created by
    # the notification_time_curve' property of GeneratingBid.
    pass

class BaseCaseConstraintLimit(Curve):
    """ Possibly time-varying max MW or MVA and optionally Min MW limit or MVA limit (Y1 and Y2, respectively) assigned to a contingency analysis base case. Use CurveSchedule XAxisUnits to specify MW or MVA. To be used only if the BaseCaseConstraintLimit differs from the DefaultConstraintLimit.
    """

#    security_constraint_sum = db.ReferenceProperty()

class StartUpTimeCurve(Curve):
    """ Startup time curve as a function of down time, where time is specified in seconds.  Relationship between unit startup time (Y1-axis) vs. unit elapsed down time (X-axis).
    """

    # The 'generating_bids' property has been implicitly created by
    # the start_up_time_curve' property of GeneratingBid.
    pass

class ResourceGroup(IdentifiedObject):
    """ A logical grouping of resources that are used to model location of types of requirements for ancillary services such as spinning reserve zones, regulation zones, etc.
    """

    # The 'resource_group_reqs' property has been implicitly created by
    # the resource_group' property of ResourceGroupReq.
    pass
#    registered_resources = db.ListProperty(db.Key)

#    @property
#    def resource_groups(self):
#        return RegisteredResource.gql("WHERE registered_resources = :1", self.key())

class ReserveReqCurve(RegularIntervalSchedule):
    """ A curve relating  reserve requirement versus time, showing the values of a specific reserve requirement for each unit of the period covered. The  curve can be based on 'absolute' time or on 'normalized' time.  X is time, typically expressed in absolute time Y1 is reserve requirement, typically expressed in MW
    """

#    reserve_req = db.ReferenceProperty()

class StartUpCostCurve(Curve):
    """ Startup costs and time as a function of down time.  Relationship between unit startup cost (Y1-axis) and unit startup time (Y2-axis) vs. unit elapsed down time (X-axis).
    """

    # The 'generating_bids' property has been implicitly created by
    # the start_up_cost_curve' property of GeneratingBid.
    pass
#    registered_generators = db.ListProperty(db.Key)

#    @property
#    def start_up_cost_curves(self):
#        return RegisteredGenerator.gql("WHERE registered_generators = :1", self.key())

class ViolationLimit(Limit):
    """ A type of limit that indicates if it is enforced and, through association, the organisation responsible for setting the limit.
    """

    # True if limit is enforced.
    enforced = db.BooleanProperty()
#    season = db.ReferenceProperty()
#    organisations = db.ListProperty(db.Key)

#    @property
#    def violation_limits(self):
#        return ErpOrganisation.gql("WHERE organisations = :1", self.key())
#    measurement = db.ReferenceProperty()
#    flowgate = db.ReferenceProperty()

class LossPenaltyFactor(MarketFactors):
    """ Loss penalty factor applied to a ConnectivityNode for a given time interval.
    """

#    connectivity_nodes = db.ListProperty(db.Key)

#    @property
#    def loss_penalty_factors(self):
#        return ConnectivityNode.gql("WHERE connectivity_nodes = :1", self.key())

class ProductBidClearing(MarketFactors):
    """ Product Bid clearing results posted for a given settlement period.
    """

    # Cleared MWs.
    cleared_mw = ActivePower
    # The 'product_bids' property has been implicitly created by
    # the product_bid_clearing' property of ProductBid.
    pass

class AncillaryServiceClearing(MarketFactors):
    """ Ancillary services clearing results are posted for a given settlement period.
    """

    # Market clearing price (MCP) in monetary units.
    mcp = Money
    # Cleared MWs.
    cleared_mw = ActivePower
    # Requirement type:  'En' - Energy  'Ru' - Regulation Up  'Rd' - Regulation Dn  'Sr' - Spinning Reserve  'Nr' - Non-Spinning Reserve  'Or' - Operating Reserve
    commodity_type = db.StringProperty()
#    market_case_clearing = db.ReferenceProperty()

class ReserveReq(ResourceGroupReq):
    """ Requirements for minimum amount of reserve and/or regulation to be supplied by a set of qualified resources.
    """

#    sensitivity_price_curve = db.ReferenceProperty()
#    market_product = db.ReferenceProperty()
#    reserve_req_curve = db.ReferenceProperty()

class RegisteredGenerator(RegisteredResource):
    # This is the minimum operating MW limit the dispatcher can enter for this unit.
    minimum_operating_mw = ActivePower
    # This is the maximum operating MW limit the dispatcher can enter for this unit
    maximum_operating_mw = ActivePower
    # High limit for secondary (AGC) control
    high_control_limit = ActivePower
    # Low limit for secondary (AGC) control
    low_control_limit = ActivePower
    # Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value regardless of the current operating point.
    maximum_allowable_spinning_reserve = ActivePower
#    start_up_cost_curves = db.ListProperty(db.Key)

#    @property
#    def registered_generators(self):
#        return StartUpCostCurve.gql("WHERE start_up_cost_curves = :1", self.key())
    # The 'generating_bids' property has been implicitly created by
    # the registered_generator' property of GeneratingBid.
    pass
    # The 'unit_initial_conditions' property has been implicitly created by
    # the generating_unit' property of UnitInitialConditions.
    pass
#    ramp_rate_curves = db.ListProperty(db.Key)

#    @property
#    def generating_unit(self):
#        return RampRateCurve.gql("WHERE ramp_rate_curves = :1", self.key())
#    generating_unit = db.ReferenceProperty()

class SecurityConstraintSum(MarketFactors):
    """ Typically provided by RTO systems, constraints identified in both base case and critical contingency cases have to be transferred. A constraint has N (>=1) constraint terms. A term is represented by an instance of TerminalConstraintTerm.  The constraint expression is: minValue <= c1*x1 + c2*x2 + .... cn*xn + k <= maxValue where: - cn is ConstraintTerm.factor  - xn is the flow at the terminal Flow into the associated equipment is positive for the purpose of ConnectivityNode NodeConstraintTerm  k is SecurityConstraintsLinear.resourceMW The units of k are assumed to be same as the units of the flows, xn.  The constants, cn, are dimensionless. With these conventions, cn and k are all positive for a typical constraint such as 'weighted sum of generation must be less than limit'. Furthermore, cn are all 1.0 for a case such as 'interface flow must be less than limit', assuming the terminals are chosen on the importing side of the interface.
    """

    # The 'constraint_terms' property has been implicitly created by
    # the security_constraint_sum' property of ConstraintTerm.
    pass
#    rto = db.ReferenceProperty()
    # The 'contingency_constraint_limits' property has been implicitly created by
    # the security_constraint_sum' property of ContingencyConstraintLimit.
    pass
#    default_constraint_limit = db.ReferenceProperty()
#    base_case_constraint_limit = db.ReferenceProperty()

class RegisteredLoad(RegisteredResource):
#    load_area = db.ReferenceProperty()
    # The 'load_bids' property has been implicitly created by
    # the registered_load' property of LoadBid.
    pass

class ResourceBid(Bid):
    """ Energy bid for generation, load, or virtual type for the whole of the market-trading period (i.e., one day in day ahead market or one hour in the real time market)
    """

    # Maximum amount of energy per day which can be produced during the trading period in MWh
    energy_max_day = ActivePower
    # Energy product (commodity) type:  'En' - Energy  'Ru' - Regulation Up  'Rd' - Regulation Dn  'Sr' - Spinning Reserve  'Nr' - Non-Spinning Reserve  'Or' - Operating Reserve
    commodity_type = db.StringProperty()
    # Maximum number of startups per week.
    start_ups_max_week = db.IntegerProperty()
    # Maximum number of shutdowns per week.
    shut_downs_max_week = db.IntegerProperty()
    # Maximum number of shutdowns per day.
    shut_downs_max_day = db.IntegerProperty()
    # Maximum number of startups per day.
    start_ups_max_day = db.IntegerProperty()
    # Minimum amount of energy per day which has to be produced during the trading period in MWh
    energy_min_day = ActivePower
    # True if bid is virtual.  Bid is assumed to be non-virtual if attribute is absent
    virtual = db.BooleanProperty()

class TerminalConstraintTerm(ConstraintTerm):
    """ A constraint term associated with a specific terminal on a physical piece of equipment.
    """

#    terminal = db.ReferenceProperty()

class PnodeClearing(MarketFactors):
    """ Pricing node clearing results posted for a given settlement period.
    """

    # Cost component of Locational Marginal Pricing (LMP) in monetary units per MW.
    cost_lmp = CostPerEnergyUnit
    # Loss component of Location Marginal Price (LMP) in monetary units per MW.
    loss_lmp = CostPerEnergyUnit
    # Congestion component of Location Marginal Price (LMP) in monetary units per MW.
    congest_lmp = CostPerEnergyUnit
#    pnode = db.ReferenceProperty()

class TransactionBid(Bid):
    """ Bilateral or scheduled transactions for energy and ancillary services considered by market clearing process
    """

    energy_trans_id = db.StringProperty()
#    delivery_pnode = db.ReferenceProperty()
#    energy_trans_id = db.ReferenceProperty()
    # The 'energy_profiles' property has been implicitly created by
    # the transaction_bid' property of EnergyProfile.
    pass
#    receipt_pnode = db.ReferenceProperty()

class NodeConstraintTerm(ConstraintTerm):
    """ To be used only to constrain a quantity that cannot be associated with a terminal. For example, a registered generating unit that is not electrically connected to the network.
    """

#    connectivity_node = db.ReferenceProperty()

class SecurityConstraintsClearing(MarketFactors):
    """ Binding security constrained clearing results posted for a given settlement period.
    """

    # Optimal MW flow
    mw_flow = ActivePower
    # Security constraint shadow price.
    shadow_price = Money
    # Binding MW limit.
    mw_limit = ActivePower

class MarketCaseClearing(MarketFactors):
    """ Market case clearing results are posted for a given settlement period.
    """

    # Settlement period:  'DA - Bid-in'  'DA - Reliability'  'DA - Amp1'  'DA - Amp2'  'RT - Ex-Ante'  'RT - Ex-Post'  'RT - Amp1'  'RT - Amp2'
    case_type = db.StringProperty()
    # Bid clearing results posted time and date.
    posted_date = db.DateProperty()
    # Last time and date clearing results were manually modified.
    modified_date = db.DateProperty()
    # The 'ancillary_service_clearing' property has been implicitly created by
    # the market_case_clearing' property of AncillaryServiceClearing.
    pass

class LoadBid(ResourceBid):
    # The fixed cost associated with committing a load reduction.
    shutdown_cost = Money
    # Time period that is required from an order to reduce a load to the time that it takes to get to the minimum load reduction.
    req_notice_time = Minutes
    # Shortest period load reduction must be maintained before load can be restored to normal levels.
    min_load_reduction_interval = Minutes
    # Shortest time that load must be left at normal levels before a new load reduction.
    min_time_bet_load_red = Minutes
    # Cost in $ at the minimum reduced load
    min_load_reduction_cost = Money
    # Minimum MW for a load reduction (e.g., MW rating of a discrete pump.
    min_load_reduction = ActivePower
    # Minimum MW load below which it may not be reduced.
    min_load = ActivePower
#    registered_load = db.ReferenceProperty()
#    load_reduction_price_curve = db.ReferenceProperty()

class GeneratingBid(ResourceBid):
    # Low economic MW limit that must be greater than or equal to the minimum operating MW limit
    minimum_economic_mw = ActivePower
    # Bid operating mode ('C' - cycling, 'F' - fixed, 'M' - must run, 'U' - unavailable)
    operating_mode = db.StringProperty()
    # Minimum time interval between unit shutdown and startup
    minimum_down_time = Minutes
    # Maximum high economic MW limit, that should not exceed the maximum operating MW limit
    maximum_economic_mw = ActivePower
    # Power rating available for unit under emergency conditions greater than or equal to maximum economic limit.
    max_emergency_mw = ActivePower
    # Maximum up time.
    up_time_max = Minutes
    # Time it takes to get the unit on-line, from the time that the prime mover mechanical power is applied
    startup_time = Minutes
    # Maximum down time.
    down_time_max = Minutes
    # Resource fixed no load cost.
    no_load_cost = Money
    # Time required for crew notification prior to start up of the unit.
    notification_time = Minutes
    # Resource startup type:  1 - Fixed startup time and fixed startup cost  2 - Startup time as a function of down time and fixed startup cost  3 - Startup cost as a function of down time
    start_up_type = db.IntegerProperty()
    # Minimum up time.
    up_time_min = Minutes
    # Minimum power rating for unit under emergency conditions, which is less than or equal to the economic minimum.
    min_emergency_mw = ActivePower
#    bid_set = db.ReferenceProperty()
#    notification_time_curve = db.ReferenceProperty()
#    start_up_cost_curve = db.ReferenceProperty()
#    start_up_time_curve = db.ReferenceProperty()
#    registered_generator = db.ReferenceProperty()


