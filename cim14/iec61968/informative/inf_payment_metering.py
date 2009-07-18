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

from cim14 import Element
from cim14.iec61968.common import Document
from cim14.iec61968.metering import DeviceFunction
from cim14.iec61970.core import IdentifiedObject
from cim14.iec61968.common import Agreement
from cim14.iec61968.common import Organisation

from cim14.iec61968.payment_metering import TransactionKind
from cim14.iec61970.domain import Money
from cim14.iec61968.payment_metering import TenderKind
from cim14.iec61968.payment_metering import CreditKind
from cim14.iec61968.payment_metering import ChargeKind

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

ns_prefix = "cim.IEC61968.Informative.InfPaymentMetering"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#IEC61968.Informative.InfPaymentMetering"

class TransactionSummary(Element):
    """ The record of detail of payment transactions pertaining to one shift of operation (one record per 'transactionKind').
    """

    # 'Transaction.kind' for which 'transactionsTotal' is given.
    transaction_kind = TransactionKind
    # Totalised amount transacted during the shift for this specific 'transactionKind', i.e., sum of 'Transaction.line.amount' per 'Transaction.kind'. Cumulative amount of rounding errors due to process rounding not reflected in 'LineDetail.amount' for 'transactionKind', i.e., sum of 'Transaction.line.rounding' per 'Transaction.kind'.
    line = db.ReferenceProperty()
#    shift = db.ReferenceProperty()

class BankStatement(Document):
    """ A type of Document that records bank deposits made by Vendor of revenue collected at PointOfSale.
    """

    # The amount that is deposited into the bank via BankAccount.
    deposit_amount = Money
    # The date and time the deposit is made.
    deposit_date_time = db.DateProperty()
    # The amount on this statement that is to be credited to MerchantAccount.
    merchant_credit_amount = Money
    # True if mechantCreditAmount has been cerdited to MerchantAccount; typically happens when bank statement details are captured into payment system.
    posted = db.BooleanProperty()
#    merchant_account = db.ReferenceProperty()
#    vendor = db.ReferenceProperty()
#    bank_account = db.ReferenceProperty()

class SDPAccountingFunction(DeviceFunction):
    """ Service delivery point accounting function, particularly for payment meter.
    """

    # The value is the balance of the sum of credits minus the sum of charges from the CreditRegisters and the ChargeRegisters. The sum might be complex function. The units are either in currency units or service units, depending on the value of accountingMode.
    available_credit = db.ReferenceProperty()
    # The value is a predefined set point for the level of the availableCredit to reach when the service will be interrupted. In the case of a prepayment meter the interruption is typically implemented by means of an electro-mechanical switch and the value is typically set = 0. The units are either in currency units or service units, depending on the value of accountingMode.
    credit_expiry_level = db.ReferenceProperty()
    # The value is a predefined set point for the level of the availableCredit to reach when a warning will be indicated to the customer. It serves to warn the customer that it is time to purchase more credit in the case of a prepayment meter implementation. The units are either in currency units or service units, depending on the value of accountingMode.
    low_credit_warning_level = db.ReferenceProperty()
    # The 'charge_registers' property has been implicitly created by
    # the spaccounting_function' property of ChargeRegister.
    pass
    # The 'credit_registers' property has been implicitly created by
    # the sdpaccounting_function' property of CreditRegister.
    pass
#    service_kind = db.ReferenceProperty()

class ReceiptSummary(Element):
    """ Record of detail of receipts pertaining to one shift of operation (one record per 'tenderKind').
    """

    # 'Tender.kind' for which 'receiptsTotal' is given.
    tender_kind = TenderKind
    # Totalised amount receipted during the shift for 'tenderKind', i.e., sum of ('Tender.amount' - 'Tender.change') per 'Tender.kind'.
    line = db.ReferenceProperty()
#    shift = db.ReferenceProperty()

class CreditRegister(IdentifiedObject):
    """ Accumulated credits transacted per CreditKind for a given function. There could be several of these registers, one for each CreditKind; depending on the application.
    """

    # Several different types of credit are typically implemented in the case of a prepayment meter.  For example: credit transferred by means of a token carrier, or credit advanced automatically inside the meter under certain conditions, or credit held in reserved to be released under emergency conditions, or credit granted by local authority as a basic life support mechanism and may be dispensed automatically by the meter under certain conditions or credit available under severe climate conditions such as during winter over a weekend.
    credit_kind = CreditKind
    # Credit amount in favour of the customer. The units are either in currency units or service units, depending on the value of 'AccountingUnit.accountingMode'.
    credit_amount = db.ReferenceProperty()
#    sdpaccounting_function = db.ReferenceProperty()

class TSPAgreement(Agreement):
    """ A contractual agreement between a supplier (utility) and a transaction service provider (a type of organisation) that governs the terms and conditions, under which authorisation the transaction service provider may process transactions on behalf of the supplier.
    """

    pass

class Bank(Organisation):
    """ Organisation that is a commercial bank, agency, or other institution that offers a similar service.
    """

    # International bank account number defined in ISO 13616; for countries where IBAN is not in operation, the existing BIC or SWIFT codes may be used instead (see ISO 9362).
    iban = db.StringProperty()
    # Bank identifier code as defined in ISO 9362; for use in countries wher IBAN is not yet in operation.
    bic = db.StringProperty()
    # Codified reference to the particular branch of the bank where BankAccount is held.
    branch_code = db.StringProperty()
    # The 'bank_accounts' property has been implicitly created by
    # the bank' property of BankAccount.
    pass

class ChargeRegister(IdentifiedObject):
    """ Accumulated charges transacted per ChargeKind for a given function. There could be several of these registers, one for each ChargeKind; depending on the application.
    """

    # Several different types of charges are typically implemented in the case of a prepayment meter. For example: a charge according to a tariff for consumption and possibly a demand component, or a charge for a debt that is loaded in the meter to be recovered on a time basis, or a standing charge to be levied at the end of each billing period, or a tax charge loaded in the meter to be recovered on a consumption basis or a time basis.
    charge_kind = ChargeKind
    # Charge amount in favour of the supplier. The units are either in currency units or service units, depending on the value of 'AccountingUnit.accountingMode'.
    charge_amount = db.ReferenceProperty()
#    spaccounting_function = db.ReferenceProperty()

class Token(IdentifiedObject):
    """ The token that is transferred to the payment meter.
    """

    # Free-format note relevant to this token.
    comment = db.StringProperty()
    # Coded representation of the token that is transferred to the payment meter.
    code = db.StringProperty()
#    point_of_sale = db.ReferenceProperty()


