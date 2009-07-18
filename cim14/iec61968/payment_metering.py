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
from cim14.iec61968.common import Agreement
from cim14.iec61968.common import Organisation
from cim14.iec61968.common import Document

from cim14.iec61970.domain import AbsoluteDate
from cim14.iec61970.domain import RealEnergy
from cim14.iec61970.domain import Money
from cim14.iec61970.domain import PerCent
from cim14.iec61970.domain import UnitMultiplier
from cim14.iec61970.domain import Currency

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

ChequeKind = db.StringProperty(choices=("postal_order", "other", "bank_order"))

TenderKind = db.StringProperty(choices=("cheque", "cash", "card", "other", "unspecified"))

ChargeKind = db.StringProperty(choices=("consumption_charge", "auxiliary_charge", "other", "tax_charge", "demand_charge"))

TransactionKind = db.StringProperty(choices=("token_sale_payment", "token_free_issue", "transaction_reversal", "other", "token_exchange", "token_grant", "token_cancellation", "auxiliary_charge_payment", "account_payment", "diverse_payment", "service_charge_payment", "tax_charge_payment", "meter_configuration_token"))

SupplierKind = db.StringProperty(choices=("retailer", "other", "utility"))

CreditKind = db.StringProperty(choices=("reserve_credit", "lifeline_credit", "other", "grant_credit", "token_credit", "advance_credit"))

ns_prefix = "cim.IEC61968.PaymentMetering"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#IEC61968.PaymentMetering"

class PointOfSale(IdentifiedObject):
    """ Logical point where transactions take place with operational interaction between Cashier and the payment system; in certain cases PointOfSale interacts directly with the end customer, in which case Cashier might not be a real person: for example a self-service kiosk or over the internet.
    """

    # Local description for where this pont of sale is physically located.
    location = db.StringProperty()
    # The 'cashier_shifts' property has been implicitly created by
    # the point_of_sale' property of CashierShift.
    pass
    # The 'tokens' property has been implicitly created by
    # the point_of_sale' property of Token.
    pass
#    vendor = db.ReferenceProperty()

class Cheque(Element):
    """ The actual tender when it is a type of cheque.
    """

    # The magnetic ink character recognition number printed on the cheque.
    micr_number = db.StringProperty()
    # Cheque reference number as printed on the cheque.
    cheque_number = db.StringProperty()
    # Kind of cheque.
    kind = ChequeKind
    # Date when cheque becomes valid.
    date = AbsoluteDate
    # Details of the account holder and bank.
    bank_account_detail = db.ReferenceProperty()
#    tender = db.ReferenceProperty()

class Vendor(IdentifiedObject):
    """ The entity that owns PointOfSale and contracts with Cashier to receipt payments and vend tokens using the payment system. Vendor has a private contract with and is managed by Merchant who is a type of Organisation. Vendor is accountable to Merchant for revenue collected, who is in turn accountable to Supplier.
    """

#    merchant_account = db.ReferenceProperty()
    # The 'cashiers' property has been implicitly created by
    # the vendor' property of Cashier.
    pass
    # The 'bank_statements' property has been implicitly created by
    # the vendor' property of BankStatement.
    pass
    # The 'point_of_sales' property has been implicitly created by
    # the vendor' property of PointOfSale.
    pass
    # The 'vendor_shifts' property has been implicitly created by
    # the vendor' property of VendorShift.
    pass

class Transaction(IdentifiedObject):
    """ The record of details of payment for service or token sale.
    """

    # Number of service units not reflected in 'serviceUnitsEnergy' due to process rounding or truncating errors.
    service_units_error = RealEnergy
    # Kind of transaction.
    kind = TransactionKind
    # Reference to the entity that is the source of 'amount' (for example: customer for token purchase; or supplier for free issue token).
    donor_reference = db.StringProperty()
    # Actual amount of service units that is being paid for.
    service_units_energy = RealEnergy
    # Formal reference for use with diverse payment (traffic fine for example).
    diverse_reference = db.StringProperty()
    # Reference to the entity that is the recipient of 'amount' (for example, supplier for service charge payment; or tax receiver for VAT).
    receiver_reference = db.StringProperty()
    # (if 'kind' is transactionReversal) Reference to the original transaction that is being reversed by this transaction.
    reversed_id = db.StringProperty()
    # Transaction amount, rounding, date and note for this transaction line.
    line = db.ReferenceProperty()
#    cashier_shift = db.ReferenceProperty()
#    vendor_shift = db.ReferenceProperty()
#    auxiliary_account = db.ReferenceProperty()
#    customer_account = db.ReferenceProperty()
#    pricing_structure = db.ReferenceProperty()
#    receipt = db.ReferenceProperty()
    # The 'user_attributes' property has been implicitly created by
    # the transaction' property of UserAttribute.
    pass
#    meter_asset = db.ReferenceProperty()

class ConsumptionTariffInterval(Element):
    """ One of a sequence of intervals defined in terms of consumption quantity of a service such as electricity, water, gas, etc. It is typically used in association with TariffProfile to define the steps or blocks in a step tariff structure, where startValue simultaneously defines the entry value of this step and the closing value of the previous step. Where consumption is &gt;= startValue it falls within this interval and where consumption is &lt; startValue it falls within the previous interval.
    """

    # The lowest level of consumption that defines the starting point of this interval. The interval extends to the start of the next interval or until it is reset to the start of the first interval by TariffProfile.tariffCycle.
    start_value = RealEnergy
    # A sequential reference that defines the identity of this interval and its relative position with respect to other intervals in a sequence of intervals.
    sequence_number = db.IntegerProperty()
#    charges = db.ListProperty(db.Key)

#    @property
#    def consumption_tariff_intervals(self):
#        return Charge.gql("WHERE charges = :1", self.key())
#    tariff_profiles = db.ListProperty(db.Key)

#    @property
#    def consumption_tariff_intervals(self):
#        return TariffProfile.gql("WHERE tariff_profiles = :1", self.key())

class BankAccountDetail(Element):
    """ Details of a bank account.
    """

    # Operational account reference number.
    account_number = db.StringProperty()
    # Name of bank where account is held.
    bank_name = db.StringProperty()
    # National identity number (or equivalent) of account holder.
    holder_id = db.StringProperty()
    # Branch of bank where account is held.
    branch_code = db.StringProperty()
    # Name of account holder.
    holder_name = db.StringProperty()

class Cashier(IdentifiedObject):
    """ The operator of the point of sale for the duration of CashierShift. Cashier is under the exclusive management control of Vendor.
    """

    # The 'cashier_shifts' property has been implicitly created by
    # the cashier' property of CashierShift.
    pass
#    vendor = db.ReferenceProperty()
    # The 'electronic_addresses' property has been implicitly created by
    # the cashier' property of ElectronicAddress.
    pass

class MerchantAgreement(Agreement):
    """ A formal controlling contractual agreement between Supplier and Merchant, in terms of which Merchant is authorised to vend tokens and receipt payments on behalf of Supplier. Merchant is accountable to Supplier for revenue collected at PointOfSale.
    """

    # The 'merchant_accounts' property has been implicitly created by
    # the merchant_agreement' property of MerchantAccount.
    pass

class TimeTariffInterval(Element):
    """ One of a sequence of time intervals defined in terms of real time. It is typically used in association with TariffProfile to define the intervals in a time of use tariff structure, where startDateTime simultaneously determines the starting point of this interval and the ending point of the previous interval.
    """

    # A reatime marker that defines the starting time (typically it is the time of day) for this interval. The interval extends to the start of the next interval or until it is reset to the start of the first interval by TariffProfile.tariffCycle.
    start_date_time = db.DateProperty()
    # A sequential reference that defines the identity of this interval and its relative position with respect to other intervals in a sequence of intervals.
    sequence_number = db.IntegerProperty()
#    charges = db.ListProperty(db.Key)

#    @property
#    def time_tariff_intervals(self):
#        return Charge.gql("WHERE charges = :1", self.key())
#    tariff_profiles = db.ListProperty(db.Key)

#    @property
#    def time_tariff_intervals(self):
#        return TariffProfile.gql("WHERE tariff_profiles = :1", self.key())

class Transactor(IdentifiedObject):
    """ The entity that ultimately executes the transaction and who is in control of the process; typically this is embodied in secure software running on a server that may employ secure hardware encryption devices for secure transaction processing.
    """

#    merchant_accounts = db.ListProperty(db.Key)

#    @property
#    def transactors(self):
#        return MerchantAccount.gql("WHERE merchant_accounts = :1", self.key())

class ServiceSupplier(Organisation):
    """ Organisation that provides services to Customers.
    """

    # Kind of supplier.
    kind = SupplierKind
    # Unique transaction reference prefix number issued to an entity by the International Standards Organisation for the purpose of tagging onto electronic financial transactions, as defined in ISO/IEC 7812-1 and ISO/IEC 7812-2.
    issuer_identification_number = db.StringProperty()
    # The 'service_delivery_points' property has been implicitly created by
    # the service_supplier' property of ServiceDeliveryPoint.
    pass
    # The 'bank_accounts' property has been implicitly created by
    # the service_supplier' property of BankAccount.
    pass
    # The 'customer_agreements' property has been implicitly created by
    # the service_supplier' property of CustomerAgreement.
    pass

class Receipt(IdentifiedObject):
    """ Record of total receipted payment from customer.
    """

    # True if this receipted payment is manually bankable, otherwise it is an electronic funds transfer.
    is_bankable = db.BooleanProperty()
    # Receipted amount with rounding, date and note.
    line = db.ReferenceProperty()
    # The 'transactions' property has been implicitly created by
    # the receipt' property of Transaction.
    pass
#    cashier_shift = db.ReferenceProperty()
#    vendor_shift = db.ReferenceProperty()
    # The 'tenders' property has been implicitly created by
    # the receipt' property of Tender.
    pass

class Due(Element):
    """ Details on amounts due for an account.
    """

    # Part of 'current' that constitutes the arrears portion.
    arrears = Money
    # Current total amount now due: current = principle + arrears + interest + charges. Typically the rule for settlement priority is: interest dues, then arrears dues, then current dues, then charge dues.
    current = Money
    # Part of 'current' that constitutes the portion of the principle amount currently due.
    principle = Money
    # Part of 'current' that constitutes the charge portion: 'charges' = 'Charge.fixedPortion' + 'Charge.variablePortion'.
    charges = Money
    # Part of 'current' that constitutes the interest portion.
    interest = Money

class Charge(IdentifiedObject):
    """ A charge element associated with other entities such as tariff structures, auxiliary agreements or other charge elements. The total charge amount applicable to this instance of Charge is the sum of fixedPortion plus percentagePortion.
    """

    # The kind of charge to be applied.
    kind = ChargeKind
    # The variable portion of this charge element, calculated as a percentage of the total amount of a parent charge.
    variable_portion = PerCent
    # The fixed portion of this charge element.
    fixed_portion = db.ReferenceProperty()
#    time_tariff_intervals = db.ListProperty(db.Key)

#    @property
#    def charges(self):
#        return TimeTariffInterval.gql("WHERE time_tariff_intervals = :1", self.key())
#    parent_charge = db.ReferenceProperty()
#    auxiliary_accounts = db.ListProperty(db.Key)

#    @property
#    def charges(self):
#        return AuxiliaryAccount.gql("WHERE auxiliary_accounts = :1", self.key())
    # The 'child_charges' property has been implicitly created by
    # the parent_charge' property of Charge.
    pass
#    consumption_tariff_intervals = db.ListProperty(db.Key)

#    @property
#    def charges(self):
#        return ConsumptionTariffInterval.gql("WHERE consumption_tariff_intervals = :1", self.key())

class TariffProfile(Document):
    """ A schedule of charges; structure associated with Tariff that allows the definition of complex tarif structures such as step and time of use when used in conjunction with TimeTariffInterval and Charge. Inherited 'status.value' is defined in the context of the utility's business rules, for example: active, inactive, etc.
    """

    # The frequency at which the tariff charge schedule is repeated Examples are: once off on a specified date and time; hourly; daily; weekly; monthly; 3-monthly; 6-monthly; 12-monthly; etc. At the end of each cycle, the business rules are reset to start from the beginning again.
    tariff_cycle = db.StringProperty()
#    tariffs = db.ListProperty(db.Key)

#    @property
#    def tariff_profiles(self):
#        return Tariff.gql("WHERE tariffs = :1", self.key())
#    consumption_tariff_intervals = db.ListProperty(db.Key)

#    @property
#    def tariff_profiles(self):
#        return ConsumptionTariffInterval.gql("WHERE consumption_tariff_intervals = :1", self.key())
#    time_tariff_intervals = db.ListProperty(db.Key)

#    @property
#    def tariff_profiles(self):
#        return TimeTariffInterval.gql("WHERE time_tariff_intervals = :1", self.key())

class MerchantAccount(Document):
    """ The operating account controlled by MerchantAgreement, against which Vendor may vend tokens or receipt payments. Transactions via VendorShift debit the account and bank deposits via BankStatement credit the account.
    """

    # The current operating balance of this account.
    current_balance = Money
    # The balance of this account after taking into account any pending debits from VendorShift.merchantDebitAmount and pending credits from BankStatement.merchantCreditAmount or credits (see also BankStatement attributes and VendorShift attributes).
    provisional_balance = Money
    # The 'vendors' property has been implicitly created by
    # the merchant_account' property of Vendor.
    pass
    # The 'bank_statements' property has been implicitly created by
    # the merchant_account' property of BankStatement.
    pass
    # The 'vendor_shifts' property has been implicitly created by
    # the merchant_account' property of VendorShift.
    pass
#    merchant_agreement = db.ReferenceProperty()
#    transactors = db.ListProperty(db.Key)

#    @property
#    def merchant_accounts(self):
#        return Transactor.gql("WHERE transactors = :1", self.key())

class Card(Element):
    """ Documentation of the tender when it is a type of card (credit, debit, etc).
    """

    # The date when this card expires.
    expiry_date = AbsoluteDate
    # The primary account number.
    pan = db.StringProperty()
    # The card verification number.
    cv_number = db.StringProperty()
    # Name of account holder.
    account_holder_name = db.StringProperty()
#    tender = db.ReferenceProperty()

class AuxiliaryAccount(Document):
    """ Variable and dynamic part of AuxiliaryAgreement, generally representing the current state of the account related to the outstanding balance defined in AuxiliaryAgreement.
    """

    # The initial principle amount, with which this account was instantiated.
    principle_amount = Money
    # The total amount currently remaining on this account that is required to be paid in order to settle the account to zero. This excludes any due amounts not yet paid.
    balance = Money
    # Details of the last credit transaction performed on this account.
    last_credit = db.ReferenceProperty()
    # Current amounts now due for payment on this account.
    due = db.ReferenceProperty()
    # Details of the last debit transaction performed on this account.
    last_debit = db.ReferenceProperty()
    # The 'payment_transactions' property has been implicitly created by
    # the auxiliary_account' property of Transaction.
    pass
#    auxiliary_agreement = db.ReferenceProperty()
#    charges = db.ListProperty(db.Key)

#    @property
#    def auxiliary_accounts(self):
#        return Charge.gql("WHERE charges = :1", self.key())

class AccountingUnit(Element):
    """ Unit for accounting; use either 'energyUnit' or 'currencyUnit' to specify the unit for 'value'.
    """

    # Value expressed in applicable units.
    value = db.FloatProperty()
    # Multiplier for the 'energyUnit' or 'monetaryUnit'.
    multiplier = UnitMultiplier
    # Unit of service.
    energy_unit = RealEnergy
    # Unit of currency.
    monetary_unit = Currency

class AccountMovement(Element):
    """ Credit/debit movements for an account.
    """

    # Reason for credit/debit transaction on an account. Example: payment received/arrears interest levied.
    reason = db.StringProperty()
    # Amount that was credited to/debited from an account. For example: payment received/interest charge on arrears.
    amount = Money
    # Date and time when the credit/debit transaction was performed.
    date_time = db.DateProperty()

class Shift(IdentifiedObject):
    """ Generally referring to a period of operation or work performed. Whether shift is open/closed can be derived from attributes 'activiryInterval.start' and 'activityInterval.end'. The grand total for receipts (i.e., cumulative total of all actual receipted amounts during this shift; bankable + non-bankable; excludes rounding error totals) can be derived from Receipt attributes: =sum(Receipt.receiptAmount) ; includes bankable and non-bankable receipts. Must also reconcile against: =sum(receiptsGrandTotalBankable + receiptsGrandTotalNonBankable). must also reconcile against ReceiptSummary: =sum(ReceiptSummary.receiptsTotal). The attributes with 'GrandTotal' defined in this class may need to be used when the source data is periodically flushed from the system and then these cannot be derived.
    """

    # Cumulative amount in error due to process rounding not reflected in transactionsGandTotal. Values are obtained from Transaction attributes: =sum(Transaction.transactionRounding).
    transactions_grand_total_rounding = Money
    # Cumulative total of transacted amounts during this shift. Values are obtained from Transaction attributes: =sum(Transaction.transactionAmount). It must also reconcile against TransactionSummary: =sum(TransactionSummary.transactionsTotal).
    transactions_grand_total = Money
    # Total of amounts receipted during this shift that can be manually banked (cash and cheques for example). Values are obtained from Receipt attributes: =sum(Receipt.receiptAmount) for all Receipt.bankable = true.
    receipts_grand_total_bankable = Money
    # Total of amounts receipted during this shift that cannot be manually banked (card payments for example). Values are obtained from Receipt attributes: =sum(Receipt.receiptAmount) for all Receipt.bankable = false.
    receipts_grand_total_non_bankable = Money
    # Cumulative amount in error due to process rounding not reflected in receiptsGrandTotal. Values are obtained from Receipt attributes: =sum(Receipt.receiptRounding).
    receipts_grand_total_rounding = Money
    # Interval for activity of this shift.
    activity_interval = db.ReferenceProperty()
    # The 'receipt_summaries' property has been implicitly created by
    # the shift' property of ReceiptSummary.
    pass
    # The 'transaction_summaries' property has been implicitly created by
    # the shift' property of TransactionSummary.
    pass

class LineDetail(Element):
    """ Details on an amount line, with rounding, date and note.
    """

    # Totalised monetary value of all errors due to process rounding or truncating that is not reflected in 'amount'.
    rounding = Money
    # Free format note relevant to this line.
    note = db.StringProperty()
    # Date and time when this line was created in the application process.
    date_time = db.DateProperty()
    # Amount for this line item.
    amount = Money

class Tender(IdentifiedObject):
    """ Tender is what is 'offered' by the customer towards making a payment and is often more than the required payment (hence the need for 'change'). The payment is thus that part of the Tender that goes towards settlement of a particular transaction. Tender is modelled as an aggregation of Cheque and Card. Both these tender types can exist in a single tender bid thus 'accountHolderName' must exist separately in each of Cheque and Card as each could have a different account holder name.
    """

    # Amount tendered by customer.
    amount = Money
    # Difference between amount tendered by customer and the amount charged by point of sale.
    change = Money
    # Kind of tender from customer.
    kind = TenderKind
#    receipt = db.ReferenceProperty()
#    card = db.ReferenceProperty()
#    cheque = db.ReferenceProperty()

class AuxiliaryAgreement(Agreement):
    """ An ad-hoc auxiliary account agreement associated with a customer agreement, not part of the customer's account, but typically subject to formal agreement between customer and supplier (utility). Typically this is used to collect revenue owing by the customer for other services or arrears accrued with the utility for other services. It is typically linked to a prepaid token purchase transaction, thus forcing the customer to make a payment towards settlement of the auxiliary account balance whenever he needs to purchase a prepaid token for electricity. The present status of AuxiliaryAgreement can be defined in the context of the utility's business rules, for example: enabled, disabled, pending, over recovered, under recovered, written off, etc.
    """

    # A local reference to this AuxiliaryAgreement defined in the context of the implementation and not related to IdentifiedObject.mRID.
    aux_ref = db.StringProperty()
    # The percentage of the transaction amount that must be collected from each vending transaction towards settlement of this AuxiliaryAgreement when payments are not in arrears. Note that there may be multiple tokens vended per vending transaction, but this is not relevant.
    vend_portion = PerCent
    # The percentage of the transaction amount that must be collected from each vending transaction towards settlement of this AuxiliaryAgreement when payments are in arrears. Note that there may be multiple tokens vended per vending transaction, but this is not relevant.
    vend_portion_arrear = PerCent
    # The fixed amount that must be collected from each vending transaction towards settlement of this AuxiliaryAgreement. Note that there may be multiple tokens vended per vending transaction, but this is not relevant.
    fixed_amount = Money
    # The interest per annum to be charged prorata on AuxiliaryAccount.dueArrears at the end of each payCycle.
    arrears_interest = PerCent
    # The minimum amount that must be paid at any transaction towards settling this AuxiliryAgreement or reducing the balance.
    min_amount = Money
    # The frequency for automatically recurring auxiliary charges, where AuxiliaryAccount.initialCharge is recursively added to AuxiliaryAccount.dueCurrent at the start of each auxCycle. For example: on a specified date and time; hourly; daily; weekly; monthly; 3-monthly; 6-monthly; 12-monthly; etc.
    aux_cycle = db.StringProperty()
    # Sub-category of this AuxiliaryAgreement as sub-classification of the inherited 'category'.
    sub_category = db.StringProperty()
    # The contractually expected payment frequency (by the customer). Examples are: ad-hoc; on specified date; hourly, daily, weekly, monthly. etc.
    pay_cycle = db.StringProperty()
    # The coded priority indicating the priority that this AuxiliaryAgreement has above other AuxiliaryAgreements (associated with the same customer agreement) when it comes to competing for settlement from a payment transaction or token purchase.
    aux_priority_code = db.StringProperty()
    # The 'auxiliary_accounts' property has been implicitly created by
    # the auxiliary_agreement' property of AuxiliaryAccount.
    pass
#    customer_agreement = db.ReferenceProperty()

class VendorShift(Shift):
    """ The operating shift for a vendor during which he may transact against the merchant's account. It aggregates transactions and receipts during the shift and periodically debits a merchant account. The totals in VendorShift should always = sum of totals aggregated in all cashier shifts that were open under the particular vendor shift.
    """

    # The amount that is to be debited from the merchant account for this vendor shift. This amount reflects the sum(PaymentTransaction.transactionAmount).
    merchant_debit_amount = Money
    # = true if merchantDebitAmount has been debited from MerchantAccount; typically happens at the end of VendorShift when it closes.
    posted = db.BooleanProperty()
    # The 'transactions' property has been implicitly created by
    # the vendor_shift' property of Transaction.
    pass
    # The 'receipts' property has been implicitly created by
    # the vendor_shift' property of Receipt.
    pass
#    vendor = db.ReferenceProperty()
#    merchant_account = db.ReferenceProperty()

class CashierShift(Shift):
    """ The operating shift for a cashier, during which he may transact against the CashierShift, subject to VendorShift being open.
    """

    # The amount of cash that the cashier brings with him to start his shift and that he will take away at the end of his shift; i.e. the cash float does not get banked.
    cash_float = Money
    # The 'transactions' property has been implicitly created by
    # the cashier_shift' property of Transaction.
    pass
#    point_of_sale = db.ReferenceProperty()
#    cashier = db.ReferenceProperty()
    # The 'receipts' property has been implicitly created by
    # the cashier_shift' property of Receipt.
    pass


