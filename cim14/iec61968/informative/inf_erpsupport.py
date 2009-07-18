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
from cim14.iec61968.common import Document
from cim14.iec61968.informative.inf_common import Role
from cim14.iec61968.informative.inf_common import BankAccount
from cim14.iec61968.common import Organisation
from cim14.iec61968.common import TelephoneNumber

from cim14.iec61970.domain import Money
from cim14.iec61970.domain import AbsoluteDate

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

BillMediaKind = db.StringProperty(choices=("electronic", "other", "paper"))

ErpInvoiceLineItemKind = db.StringProperty(choices=("other", "recalculation", "initial"))

ErpInvoiceKind = db.StringProperty(choices=("sales", "purchase"))

ErpAccountKind = db.StringProperty(choices=("normal", "statistical", "estimate", "reversal"))

ns_prefix = "cim.IEC61968.Informative.InfERPSupport"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#IEC61968.Informative.InfERPSupport"

class ErpLedgerEntry(IdentifiedObject):
    """ Details of an individual entry in a ledger, which was posted from a journal on the posted date.
    """

    # Date and time journal entry was recorded.
    transaction_date_time = db.DateProperty()
    # Kind of account for this entry.
    account_kind = ErpAccountKind
    # The amount of the debit or credit for this account.
    amount = Money
    # Account identifier for this entry.
    account_id = db.StringProperty()
    # Date and time this entry was posted to the ledger.
    posted_date_time = db.DateProperty()
    status = db.ReferenceProperty()
#    settlements = db.ListProperty(db.Key)

#    @property
#    def erp_ledger_entries(self):
#        return Settlement.gql("WHERE settlements = :1", self.key())
#    erp_jounal_entry = db.ReferenceProperty()
#    erp_ledger = db.ReferenceProperty()
#    erp_ledger_entry = db.ReferenceProperty()
#    user_attributes = db.ListProperty(db.Key)

#    @property
#    def erp_ledger_entries(self):
#        return UserAttribute.gql("WHERE user_attributes = :1", self.key())

class ErpLedger(Document):
    """ In accounting transactions, a ledger is a book containing accounts to which debits and credits are posted from journals, where transactions are initially recorded. Journal entries are periodically posted to the ledger. Ledger Actual represents actual amounts by account within ledger within company or business area. Actual amounts may be generated in a source application and then loaded to a specific ledger within the enterprise general ledger or budget application.
    """

    # The 'erp_ledger_entries' property has been implicitly created by
    # the erp_ledger' property of ErpLedgerEntry.
    pass

class ErpRecLineItem(IdentifiedObject):
    """ Individual entry of an ErpReceivable, it is a particular transaction representing an invoice, credit memo or debit memo to a customer.
    """

    status = db.ReferenceProperty()
#    erp_receivable = db.ReferenceProperty()
#    erp_payments = db.ListProperty(db.Key)

#    @property
#    def erp_rec_line_items(self):
#        return ErpPayment.gql("WHERE erp_payments = :1", self.key())
#    erp_invoice_line_item = db.ReferenceProperty()
#    erp_journal_entries = db.ListProperty(db.Key)

#    @property
#    def erp_rec_line_items(self):
#        return ErpJournalEntry.gql("WHERE erp_journal_entries = :1", self.key())

class DocOrgRole(Role):
    """ Roles played between Organisations and Documents.
    """

#    document = db.ReferenceProperty()
#    erp_organisation = db.ReferenceProperty()

class ErpIssueInventory(IdentifiedObject):
    """ Can be used to request an application to process an issue or request information about an issue.
    """

    status = db.ReferenceProperty()
#    type_material = db.ReferenceProperty()
#    type_asset = db.ReferenceProperty()

class ErpInventory(IdentifiedObject):
    """ Utility inventory-related information about an item or part (and not for description of the item and its attributes). It is used by ERP applications to enable the synchronization of Inventory data that exists on separate Item Master databases. This data is not the master data that describes the attributes of the item such as dimensions, weight, or unit of measure - it describes the item as it exists at a specific location.
    """

    status = db.ReferenceProperty()
#    asset = db.ReferenceProperty()

class ErpPurchaseOrder(Document):
    """ A document that communicates an order to purchase goods from a buyer to a supplier. The PurchaseOrder carries information to and from the buyer and supplier. It is a legally binding document once both Parties agree to the contents and the specified terms and conditions of the order.
    """

    # The 'erp_poline_items' property has been implicitly created by
    # the erp_purchase_order' property of ErpPOLineItem.
    pass

class ErpPayableLineItem(IdentifiedObject):
    """ Of an ErpPayable, a line item references an ErpInvoiceLineitem or other source such as credit memos.
    """

    status = db.ReferenceProperty()
#    erp_journal_entries = db.ListProperty(db.Key)

#    @property
#    def erp_payable_line_items(self):
#        return ErpJournalEntry.gql("WHERE erp_journal_entries = :1", self.key())
#    erp_payable = db.ReferenceProperty()
#    erp_invoice_line_item = db.ReferenceProperty()
#    erp_payments = db.ListProperty(db.Key)

#    @property
#    def erp_payable_line_items(self):
#        return ErpPayment.gql("WHERE erp_payments = :1", self.key())

class ErpQuote(Document):
    """ Document describing the prices of goods or services provided by a supplier. It includes the terms of the purchase, delivery proposals, identification of goods or services ordered, as well as their quantities.
    """

    # The 'erp_quote_line_items' property has been implicitly created by
    # the erp_quote' property of ErpQuoteLineItem.
    pass

class ErpBOM(Document):
    """ Information that generally describes the Bill of Material Structure and its contents for a utility.  This is used by ERP systems to transfer Bill of Material information between two business applications.
    """

    # The 'erp_bom_item_datas' property has been implicitly created by
    # the erp_bom' property of ErpBomItemData.
    pass
#    design = db.ReferenceProperty()

class ErpInvoice(Document):
    """ A roll up of invoice line items. The whole invoice has a due date and amount to be paid, with information such as customer, banks etc. being obtained through associations. The invoice roll up is based on individual line items that each contain amounts and descriptions for specific services or products.
    """

    # The date of which the invoice is issued.
    transaction_date = db.DateProperty()
    # The type of invoice transfer.
    transfer_type = db.StringProperty()
    # Calculated date upon which the Invoice amount is due.
    due_date = AbsoluteDate
    # Kind of invoice (default is 'sales').
    kind = ErpInvoiceKind
    # The number of an invoice to be reference by this invoice.
    reference_number = db.StringProperty()
    # Total amount due on this invoice based on line items and applicable adjustments.
    amount = Money
    # Kind of media by which the CustomerBillingInfo was delivered.
    bill_media_kind = BillMediaKind
    # True if payment is to be paid by a Customer to accept a particular ErpQuote (with associated Design) and have work initiated, at which time an associated ErpInvoice should automatically be generated. EprPayment.subjectStatus satisfies terms specificed in the ErpQuote.
    pro_forma = db.BooleanProperty()
    # Date on which the customer billing statement/invoice was printed/mailed.
    mailed_date = AbsoluteDate
#    customer_account = db.ReferenceProperty()
    # The 'erp_invoice_line_items' property has been implicitly created by
    # the erp_invoice' property of ErpInvoiceLineItem.
    pass

class ErpLedBudLineItem(IdentifiedObject):
    """ Individual entry of a given Ledger Budget, typically containing information such as amount, accounting date, accounting period, and is associated with the applicable general ledger account.
    """

    status = db.ReferenceProperty()
#    erp_led_bud_line_item = db.ReferenceProperty()
#    erp_ledger_budget = db.ReferenceProperty()

class ErpPayment(Document):
    """ Payment infromation and status for any individual line item of an ErpInvoice (e.g., when payment is from a customer). ErpPayable is also updated when payment is to a supplier and ErpReceivable is updated when payment is from a customer. Multiple payments can be made against a single line item and an individual payment can apply to more that one line item.
    """

    # Payment terms (e.g., net 30).
    terms_payment = db.StringProperty()
#    erp_rec_line_items = db.ListProperty(db.Key)

#    @property
#    def erp_payments(self):
#        return ErpRecLineItem.gql("WHERE erp_rec_line_items = :1", self.key())
#    erp_invoice_line_items = db.ListProperty(db.Key)

#    @property
#    def erp_payments(self):
#        return ErpInvoiceLineItem.gql("WHERE erp_invoice_line_items = :1", self.key())
#    erp_payable_line_items = db.ListProperty(db.Key)

#    @property
#    def erp_payments(self):
#        return ErpPayableLineItem.gql("WHERE erp_payable_line_items = :1", self.key())

class ErpEngChangeOrder(Document):
    """ General Utility Engineering Change Order information.
    """

    pass

class ErpInventoryCount(IdentifiedObject):
    """ This is related to Inventory physical counts organized by AssetModel. Note that a count of a type of asset can be accomplished by the association inherited by AssetModel (from Document) to Asset. It enables ERP applications to transfer an inventory count between ERP and the actual physical inventory location. This count may be a cycle count or a physical count.
    """

    status = db.ReferenceProperty()
#    material_item = db.ReferenceProperty()
#    asset_model = db.ReferenceProperty()

class ErpTimeSheet(Document):
    """ Time sheet for employees and contractors. Note that ErpTimeSheet inherits the relationship to ErpPerson from Document.
    """

    # The 'erp_time_entries' property has been implicitly created by
    # the erp_time_sheet' property of ErpTimeEntry.
    pass

class OrgOrgRole(Role):
    """ Roles played between Organisations and other Organisations. This includes role ups for ogranisations, cost centers, profit centers, regulatory reporting, etc. Note that the parent and child relationship is indicated by the name on each end of the association.
    """

    # Identifiers of the organisation held by another organisation, such as a government agency (federal, state, province, city, county), financial institution (Dun and Bradstreet), etc.
    client_id = db.StringProperty()
#    parent_organisation = db.ReferenceProperty()
#    child_organisation = db.ReferenceProperty()

class ErpItemMaster(IdentifiedObject):
    """ Any unique purchased part for manufactured product tracked by ERP systems for a utility. Item, as used by the OAG, refers to the basic information about an item, including its attributes, cost, and locations. It does not include item quantities. Compare to the Inventory, which includes all quantities and other location-specific information.
    """

    status = db.ReferenceProperty()
#    asset = db.ReferenceProperty()

class ErpProjectAccounting(Document):
    """ Utility Project Accounting information, used by ERP applications to enable all relevant sub-systems that submit single sided transactions to transfer information with a Project Accounting Application. This would include, but not necessarily be limited to: Accounts Payable, Accounts Receivable, Budget, Order Management, Purchasing, Time and Labor, Travel and Expense.
    """

    # The 'works' property has been implicitly created by
    # the erp_project_accounting' property of Work.
    pass
    # The 'work_cost_details' property has been implicitly created by
    # the erp_project_accounting' property of WorkCostDetail.
    pass
    # The 'projects' property has been implicitly created by
    # the erp_project_accounting' property of Project.
    pass
    # The 'erp_time_entries' property has been implicitly created by
    # the erp_project_accounting' property of ErpTimeEntry.
    pass

class ErpReceivable(Document):
    """ Transaction representing an invoice, credit memo or debit memo to a customer. It is an open (unpaid) item in the Accounts Receivable ledger.
    """

    # The 'erp_rec_line_items' property has been implicitly created by
    # the erp_receivable' property of ErpRecLineItem.
    pass

class ErpBankAccount(BankAccount):
    """ Relationship under a particular name, usually evidenced by a deposit against which withdrawals can be made. Types of bank accounts include: demand, time, custodial, joint, trustee, corporate, special, and regular accounts. A statement of transactions during a fiscal period and the resulting balance is maintained on each account. For Payment metering, the account is associated with Bank and Supplier, reflecting details of the bank account used for depositing revenue collected by TokenVendor. The name of the account holder should be specified in 'name' attribute.
    """

    # Bank ABA.
    bank_aba = db.StringProperty()

class OrgErpPersonRole(Role):
    """ Roles played between Persons and Organisations.
    """

    # Identifiers of the person held by an organisation, such as a government agency (federal, state, province, city, county), financial institutions, etc.
    client_id = db.StringProperty()
#    erp_organisation = db.ReferenceProperty()
#    erp_person = db.ReferenceProperty()

class ErpTimeEntry(IdentifiedObject):
    """ An individual entry on an ErpTimeSheet.
    """

    status = db.ReferenceProperty()
#    erp_time_sheet = db.ReferenceProperty()
#    erp_project_accounting = db.ReferenceProperty()

class ErpPayable(Document):
    """ A transaction that represents an invoice from a supplier. A payable (or voucher) is an open item, approved and ready for payment, in the Accounts Payable ledger.
    """

    # The 'erp_payable_line_items' property has been implicitly created by
    # the erp_payable' property of ErpPayableLineItem.
    pass
#    contractor_items = db.ListProperty(db.Key)

#    @property
#    def erp_payables(self):
#        return ContractorItem.gql("WHERE contractor_items = :1", self.key())

class ErpPerson(IdentifiedObject):
    """ General purpose information for name and other information to contact people.
    """

    # Person's first name.
    first_name = db.StringProperty()
    # A suffix for the person's name, such as II, III, etc.
    suffix = db.StringProperty()
    # A prefix or title for the person's name, such as Miss, Mister, Doctor, etc.
    prefix = db.StringProperty()
    # Unique identifier for person relative to its governing authority, for example a federal tax identifier (such as a Social Security number in the United States).
    government_id = db.StringProperty()
    # Person's last (family, sir) name.
    last_name = db.StringProperty()
    # Middle name(s) or initial(s).
    m_name = db.StringProperty()
    # Special service needs for the person (contact) are described; examples include life support, etc.
    special_need = db.StringProperty()
    # Category of this person relative to utility operations, classified according to the utility's corporate standards and practices. Examples include employee, contractor, agent, not affiliated, etc. Note that this field is not used to indicate whether this person is a customer of the utility. Often an employee or contractor is also a customer. Customer information is gained with relationship to Organisation and CustomerData. In similar fashion, this field does not indicate the various roles this person may fill as part of utility operations.
    category = db.StringProperty()
    status = db.ReferenceProperty()
#    crafts = db.ListProperty(db.Key)

#    @property
#    def erp_persons(self):
#        return Craft.gql("WHERE crafts = :1", self.key())
#    labor_items = db.ListProperty(db.Key)

#    @property
#    def erp_persons(self):
#        return LaborItem.gql("WHERE labor_items = :1", self.key())
#    erp_personnel = db.ReferenceProperty()
    # The 'location_roles' property has been implicitly created by
    # the erp_person' property of ErpPersonLocRole.
    pass
    # The 'electronic_addresses' property has been implicitly created by
    # the erp_person' property of ElectronicAddress.
    pass
    # The 'switching_step_roles' property has been implicitly created by
    # the erp_person' property of ErpPersonScheduleStepRole.
    pass
#    activity_records = db.ListProperty(db.Key)

#    @property
#    def erp_persons(self):
#        return ActivityRecord.gql("WHERE activity_records = :1", self.key())
    # The 'land_property_roles' property has been implicitly created by
    # the erp_person' property of PersonPropertyRole.
    pass
    # The 'erp_organisation_roles' property has been implicitly created by
    # the erp_person' property of OrgErpPersonRole.
    pass
#    call_backs = db.ListProperty(db.Key)

#    @property
#    def erp_persons(self):
#        return CallBack.gql("WHERE call_backs = :1", self.key())
    # The 'change_items' property has been implicitly created by
    # the erp_person' property of ChangeItem.
    pass
    # The 'skills' property has been implicitly created by
    # the erp_person' property of Skill.
    pass
#    erp_competency = db.ReferenceProperty()
#    erp_telephone_numbers = db.ListProperty(db.Key)

#    @property
#    def erp_persons(self):
#        return ErpTelephoneNumber.gql("WHERE erp_telephone_numbers = :1", self.key())
#    customer_data = db.ReferenceProperty()
    # The 'document_roles' property has been implicitly created by
    # the erp_person' property of DocErpPersonRole.
    pass
#    crews = db.ListProperty(db.Key)

#    @property
#    def crew_members(self):
#        return Crew.gql("WHERE crews = :1", self.key())
    # The 'measurement_values' property has been implicitly created by
    # the erp_person' property of MeasurementValue.
    pass
#    appointments = db.ListProperty(db.Key)

#    @property
#    def erp_persons(self):
#        return Appointment.gql("WHERE appointments = :1", self.key())

class ErpQuoteLineItem(IdentifiedObject):
    """ Of an ErpQuote, the item or product quoted along with quantity, price and other descriptive information.
    """

    status = db.ReferenceProperty()
#    asset_model_catalogue_item = db.ReferenceProperty()
#    design = db.ReferenceProperty()
#    erp_quote = db.ReferenceProperty()
#    erp_invoice_line_item = db.ReferenceProperty()
#    erp_req_line_item = db.ReferenceProperty()
#    request = db.ReferenceProperty()

class ErpJournalEntry(IdentifiedObject):
    """ Details of an individual entry in a journal, which is to be posted to a ledger on the posting date.
    """

    # Date and time this entry is to be posted to the ledger.
    posting_date_time = db.DateProperty()
    # The amount of the debit or credit for this account.
    amount = Money
    # The identifer of the source for this entry.
    source_id = db.StringProperty()
    # Date and time journal entry was recorded.
    transaction_date_time = db.DateProperty()
    # Account identifier for this entry.
    account_id = db.StringProperty()
    status = db.ReferenceProperty()
#    erp_rec_line_items = db.ListProperty(db.Key)

#    @property
#    def erp_journal_entries(self):
#        return ErpRecLineItem.gql("WHERE erp_rec_line_items = :1", self.key())
#    erp_journal = db.ReferenceProperty()
#    erp_payable_line_items = db.ListProperty(db.Key)

#    @property
#    def erp_journal_entries(self):
#        return ErpPayableLineItem.gql("WHERE erp_payable_line_items = :1", self.key())
#    erp_ledger_entry = db.ReferenceProperty()
#    erp_invoice_line_item = db.ReferenceProperty()
#    cost_types = db.ListProperty(db.Key)

#    @property
#    def erp_journal_entries(self):
#        return CostType.gql("WHERE cost_types = :1", self.key())

class ErpBomItemData(IdentifiedObject):
    """ An individual item on a bill of materials.
    """

#    type_asset = db.ReferenceProperty()
#    erp_bom = db.ReferenceProperty()
#    design_location = db.ReferenceProperty()

class ErpCompetency(IdentifiedObject):
    """ Information that describes aptitudes of a utility employee. Unlike Skills that an ErpPerson must be certified to perform before undertaking certain type of assignments (to be able to perfrom a Craft), ErpCompetency has more to do with typical Human Resource (HR) matters such as schooling, training, etc.
    """

    # The 'erp_persons' property has been implicitly created by
    # the erp_competency' property of ErpPerson.
    pass

class ErpSalesOrder(Document):
    """ General purpose Sales Order is used for utility service orders, etc. As used by the OAG, the SalesOrder is a step beyond a PurchaseOrder in that the receiving entity of the order also communicates SalesInformoration about the Order along with the Order itself.
    """

    pass

class ErpLedgerBudget(Document):
    """ Information for utility Ledger Budgets. They support the transfer budget amounts between all possible source applications throughout an enterprise and a general ledger or budget application.
    """

    # The 'erp_led_bud_line_items' property has been implicitly created by
    # the erp_ledger_budget' property of ErpLedBudLineItem.
    pass

class ErpOrganisation(Organisation):
    """ Identifies organisations that might have roles as utilities, contractors, suppliers, manufacturers, customers, etc. Organisations may also have parent-child relationships to identify departments within an organisation, or parent company relationships. The organization may be internal (e.g., departments) or external to the utility. There may be multiple organizations of a given 'category', each with a unique 'code'.
    """

    # True if organisation 'opted out', i.e., has requested that their contact information not be shared with other organisations for purposes of solicitation.
    opt_out = db.BooleanProperty()
    # Operational mode of the organisation, often required for outage reporting purposes. Some utilities use text to describe various modes (like nominal, emergency, storm, other), while others use severity ratings (for example, 0 is a nominal condition and 5 is the most severe condition).
    mode = db.StringProperty()
    # True if organisation is cost center.
    is_cost_center = db.BooleanProperty()
    # Designated code for organisation.
    code = db.StringProperty()
    # True if organisation is profit center.
    is_profit_center = db.BooleanProperty()
    # Unique identifier for organisation relative to its governing authority, for example a federal tax identifier.
    government_id = db.StringProperty()
    # Category by utility's corporate standards and practices.
    category = db.StringProperty()
    # Unique identifier for a given organisation (business). In the USA, this is a 'Dunns' or D&amp;B number. This identifier is typically in addition to the identifiers that organizations assign (on an internal basis) to each of their locations. Note that a unique identifier can be set up for each location of an organisation. This requirement is supported through the recursive Organisation-Organisation relationship, where each child Organisation can have a specified physical location.
    industry_id = db.StringProperty()
    # The 'registered_resources' property has been implicitly created by
    # the organisation' property of RegisteredResource.
    pass
    # The 'parent_organisation_roles' property has been implicitly created by
    # the child_organisation' property of OrgOrgRole.
    pass
    # The 'location_roles' property has been implicitly created by
    # the erp_organisation' property of OrgLocRole.
    pass
    # The 'requests' property has been implicitly created by
    # the organisation' property of Request.
    pass
    # The 'erp_person_roles' property has been implicitly created by
    # the erp_organisation' property of OrgErpPersonRole.
    pass
    # The 'change_items' property has been implicitly created by
    # the organisation' property of ChangeItem.
    pass
    # The 'child_organisation_roles' property has been implicitly created by
    # the parent_organisation' property of OrgOrgRole.
    pass
#    activity_records = db.ListProperty(db.Key)

#    @property
#    def organisations(self):
#        return ActivityRecord.gql("WHERE activity_records = :1", self.key())
#    int_sched_agreement = db.ListProperty(db.Key)

#    @property
#    def organisations(self):
#        return IntSchedAgreement.gql("WHERE int_sched_agreement = :1", self.key())
    # The 'land_property_roles' property has been implicitly created by
    # the erp_organisation' property of OrgPropertyRole.
    pass
    # The 'power_system_resource_roles' property has been implicitly created by
    # the erp_organisation' property of OrgPsrRole.
    pass
    # The 'asset_roles' property has been implicitly created by
    # the erp_organisation' property of OrgAssetRole.
    pass
#    violation_limits = db.ListProperty(db.Key)

#    @property
#    def organisations(self):
#        return ViolationLimit.gql("WHERE violation_limits = :1", self.key())
    # The 'document_roles' property has been implicitly created by
    # the erp_organisation' property of DocOrgRole.
    pass
#    crews = db.ListProperty(db.Key)

#    @property
#    def organisations(self):
#        return Crew.gql("WHERE crews = :1", self.key())

class ErpInvoiceLineItem(Document):
    """ An individual line item on an invoice.
    """

    # The previous line item charge amount.
    previous_amount = db.FloatProperty()
    # Line item number on invoice statement.
    line_number = db.StringProperty()
    # GL account code, must be a valid combination.
    account_gl = db.StringProperty()
    # The amount due for this line item.
    line_amount = db.FloatProperty()
    # The start of a bill period for the line item.
    start = db.DateProperty()
    # The end of a bill period for the line item.
    end = db.DateProperty()
    # Kind of line item.
    kind = ErpInvoiceLineItemKind
    # Date line item will be posted to the General Ledger.
    date_gl = db.DateProperty()
    # The version number of the bill run.
    line_version = db.StringProperty()
    # The net line item charge amount.
    net_amount = db.FloatProperty()
    # The 'component_erp_invoice_line_items' property has been implicitly created by
    # the container_erp_invoice_line_item' property of ErpInvoiceLineItem.
    pass
#    erp_payable_line_item = db.ReferenceProperty()
#    erp_rec_delv_line_item = db.ReferenceProperty()
#    customer_billing_infos = db.ListProperty(db.Key)

#    @property
#    def erp_invoice_line_items(self):
#        return CustomerBillingInfo.gql("WHERE customer_billing_infos = :1", self.key())
#    erp_payments = db.ListProperty(db.Key)

#    @property
#    def erp_invoice_line_items(self):
#        return ErpPayment.gql("WHERE erp_payments = :1", self.key())
#    erp_rec_line_item = db.ReferenceProperty()
#    market_factors = db.ListProperty(db.Key)

#    @property
#    def erp_invoices(self):
#        return MarketFactors.gql("WHERE market_factors = :1", self.key())
#    settlements = db.ListProperty(db.Key)

#    @property
#    def erp_invoice_line_items(self):
#        return Settlement.gql("WHERE settlements = :1", self.key())
#    erp_invoice = db.ReferenceProperty()
#    erp_quote_line_item = db.ReferenceProperty()
#    work_billing_infos = db.ListProperty(db.Key)

#    @property
#    def erp_line_items(self):
#        return WorkBillingInfo.gql("WHERE work_billing_infos = :1", self.key())
#    user_attributes = db.ListProperty(db.Key)

#    @property
#    def erp_invoice_line_items(self):
#        return UserAttribute.gql("WHERE user_attributes = :1", self.key())
    # The 'erp_journal_entries' property has been implicitly created by
    # the erp_invoice_line_item' property of ErpJournalEntry.
    pass
#    container_erp_invoice_line_item = db.ReferenceProperty()

class DocErpPersonRole(Role):
    """ Roles played between Persons and Documents.
    """

#    erp_person = db.ReferenceProperty()
#    document = db.ReferenceProperty()

class ErpRequisition(Document):
    """ General information that applies to a utility requisition that is a request for the purchase of goods or services. Typically, a requisition leads to the creation of a purchase order to a specific supplier.
    """

    # The 'erp_req_line_items' property has been implicitly created by
    # the erp_requisition' property of ErpReqLineItem.
    pass

class ErpReceiveDelivery(Document):
    """ Transaction for an Organisation receiving goods or services that may be used to indicate receipt of goods in conjunction with a purchase order. A receivable is an open (unpaid) item in the Accounts Receivable ledger.
    """

    # The 'erp_rec_delv_line_items' property has been implicitly created by
    # the erp_receive_delivery' property of ErpRecDelvLineItem.
    pass

class ErpChartOfAccounts(Document):
    """ Accounting structure of a business. Each account represents a financial aspect of a business, such as its Accounts Payable, or the value of its inventory, or its office supply expenses.
    """

    pass

class ErpPersonnel(IdentifiedObject):
    """ Information that applies to the basic data about a utility person, used by ERP applications to transfer Personnel data for a worker.
    """

    status = db.ReferenceProperty()
    # The 'erp_persons' property has been implicitly created by
    # the erp_personnel' property of ErpPerson.
    pass

class ErpRecDelvLineItem(IdentifiedObject):
    """ Of an ErpReceiveDelivery, this is an individually received good or service by the Organisation receiving goods or services. It may be used to indicate receipt of goods in conjunction with a purchase order line item.
    """

    status = db.ReferenceProperty()
#    material_items = db.ListProperty(db.Key)

#    @property
#    def erp_rec_delv_line_items(self):
#        return MaterialItem.gql("WHERE material_items = :1", self.key())
#    erp_invoice_line_item = db.ReferenceProperty()
#    erp_receive_delivery = db.ReferenceProperty()
#    erp_poline_item = db.ReferenceProperty()
#    assets = db.ListProperty(db.Key)

#    @property
#    def erp_rec_delivery_items(self):
#        return Asset.gql("WHERE assets = :1", self.key())

class ErpTelephoneNumber(TelephoneNumber):
    """ The telephone number for a person or organisation.
    """

    # The purpose of the telephone: home, mobile, home fax, office, office fax, switchboard, other.
    usage = db.StringProperty()
    status = db.ReferenceProperty()
#    electronic_address = db.ReferenceProperty()
#    erp_persons = db.ListProperty(db.Key)

#    @property
#    def erp_telephone_numbers(self):
#        return ErpPerson.gql("WHERE erp_persons = :1", self.key())

class ErpSiteLevelData(IdentifiedObject):
    """ For a utility, general information that describes physical locations of organizations or the location codes and their meanings. This enables ERP applications to ensure that the physical location identifiers are synchronized between the business applications.
    """

    status = db.ReferenceProperty()
#    land_property = db.ReferenceProperty()

class ErpReqLineItem(IdentifiedObject):
    """ Information that describes a requested item and its attributes.
    """

    # Quantity of item requisitioned.
    quantity = db.IntegerProperty()
    code = db.StringProperty()
    delivery_date = AbsoluteDate
    # Cost of material
    cost = Money
    status = db.ReferenceProperty()
#    type_material = db.ReferenceProperty()
#    type_asset = db.ReferenceProperty()
#    erp_requisition = db.ReferenceProperty()
#    erp_quote_line_item = db.ReferenceProperty()
#    erp_poline_item = db.ReferenceProperty()

class ErpJournal(Document):
    """ Book for recording accounting transactions as they occur. Transactions and adjustments are first recorded in a journal, which is like a diary of instructions, advising which account to be charged and by how much. A journal represents a change in the balances of a business's financial accounts. Many tasks or transactions throughout an enterprise will result in the creation of a journal. Some examples are creating a customer invoice, paying a vendor, transferring inventory, or paying employees.
    """

    # The 'erp_journal_entries' property has been implicitly created by
    # the erp_journal' property of ErpJournalEntry.
    pass

class ErpPOLineItem(Document):
    """ Of an ErpPurchaseOrder, this is an individually ordered item or product along with the quantity, price and other descriptive information.
    """

#    erp_rec_del_line_item = db.ReferenceProperty()
#    erp_req_line_item = db.ReferenceProperty()
#    erp_purchase_order = db.ReferenceProperty()
#    asset_model_catalogue_item = db.ReferenceProperty()
#    material_item = db.ReferenceProperty()


