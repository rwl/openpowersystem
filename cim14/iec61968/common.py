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

from cim14.iec61970.domain import Seconds
from cim14.iec61970.domain import StringQuantity
from cim14.iec61970.domain import AbsoluteDate

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

ns_prefix = "cim.IEC61968.Common"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#IEC61968.Common"

class TelephoneNumber(IdentifiedObject):
    """ Telephone number.
    """

    # Country code.
    country_code = db.StringProperty()
    # (if applicable) City code.
    city_code = db.StringProperty()
    # Main (local) part of this telephone number.
    local_number = db.StringProperty()
    # (if applicable) Extension for this telephone number.
    extension = db.StringProperty()
    # Area or region code.
    area_code = db.StringProperty()
#    organisation = db.ReferenceProperty()
#    location = db.ReferenceProperty()

class Location(IdentifiedObject):
    """ The place, scene, or point of something where someone or something has been, is, and/or will be at a given moment in time. It may be: - Spatial location of an actual or planned structure, or a set of point-oriented structures (as a substation, structure, building, town, etc.) or diagram objects, which may be defined as a point or polygon, or, - Path of an underground or overhead conductor, or a linear diagram object.
    """

    # Utility-specific code for the location.
    corporate_code = db.StringProperty()
    # (if applicable) Direction that allows field crews to quickly find a given asset. For a given location, such as a street address, this is the relative direction in wich to find the asset. For example, a Streetlight may be located at the 'NW' (northwest) corner of the customer's site, or a ServiceDeliveryPoint may be located on the second floor of an appartment building.
    direction = db.StringProperty()
    # True if the first and last point (in the sequence of associated PositionPoints) are to be connected, thus forming a polygon rather than merely a sequence of line segments.
    is_polygon = db.BooleanProperty()
    # (if applicable) Reference to geographical information source, often external to the utility.
    geo_info_reference = db.StringProperty()
    # Category by utility's corporate standards and practices, relative to the location itself (e.g., geographical, functional accounting, etc., not a given property that happens to exist at that location).
    category = db.StringProperty()
    # Secondary address of the location. For example, PO Box address may have different ZIP code than that in the 'mainAddress'.
    secondary_address = db.ReferenceProperty()
    # Status of this location.
    status = db.ReferenceProperty()
    # Main address of the location.
    main_address = db.ReferenceProperty()
#    gml_selectors = db.ListProperty(db.Key)

#    @property
#    def locations(self):
#        return GmlSelector.gql("WHERE gml_selectors = :1", self.key())
    # The 'to_location_roles' property has been implicitly created by
    # the from_location' property of LocLocRole.
    pass
    # The 'erp_person_roles' property has been implicitly created by
    # the location' property of ErpPersonLocRole.
    pass
    # The 'change_items' property has been implicitly created by
    # the location' property of ChangeItem.
    pass
    # The 'power_system_resource_roles' property has been implicitly created by
    # the location' property of PsrLocRole.
    pass
#    land_properties = db.ListProperty(db.Key)

#    @property
#    def locations(self):
#        return LandProperty.gql("WHERE land_properties = :1", self.key())
#    red_lines = db.ListProperty(db.Key)

#    @property
#    def locations(self):
#        return RedLine.gql("WHERE red_lines = :1", self.key())
    # The 'erp_organisation_roles' property has been implicitly created by
    # the location' property of OrgLocRole.
    pass
#    hazards = db.ListProperty(db.Key)

#    @property
#    def locations(self):
#        return Hazard.gql("WHERE hazards = :1", self.key())
    # The 'from_location_roles' property has been implicitly created by
    # the to_location' property of LocLocRole.
    pass
#    measurements = db.ListProperty(db.Key)

#    @property
#    def locations(self):
#        return Measurement.gql("WHERE measurements = :1", self.key())
    # The 'asset_roles' property has been implicitly created by
    # the location' property of AssetLocRole.
    pass
    # The 'document_roles' property has been implicitly created by
    # the location' property of DocLocRole.
    pass
    # The 'position_points' property has been implicitly created by
    # the location' property of PositionPoint.
    pass
#    electronic_addresses = db.ListProperty(db.Key)

#    @property
#    def locations(self):
#        return ElectronicAddress.gql("WHERE electronic_addresses = :1", self.key())
    # The 'telephone_numbers' property has been implicitly created by
    # the location' property of TelephoneNumber.
    pass
#    dimensions_info = db.ReferenceProperty()
#    routes = db.ListProperty(db.Key)

#    @property
#    def locations(self):
#        return Route.gql("WHERE routes = :1", self.key())
#    gml_observatins = db.ListProperty(db.Key)

#    @property
#    def locations(self):
#        return GmlObservation.gql("WHERE gml_observatins = :1", self.key())
#    activity_records = db.ListProperty(db.Key)

#    @property
#    def locations(self):
#        return ActivityRecord.gql("WHERE activity_records = :1", self.key())
#    crews = db.ListProperty(db.Key)

#    @property
#    def locations(self):
#        return Crew.gql("WHERE crews = :1", self.key())

class ActivityRecord(IdentifiedObject):
    """ Records activity for an entity at a point in time; activity may be for an event that has already occurred or for a planned activity.
    """

    # Severity level of event resulting in this activity record.
    severity = db.StringProperty()
    # Reason for event resulting in this activity record, typically supplied when user initiated.
    reason = db.StringProperty()
    # Category of event resulting in this activity record.
    category = db.StringProperty()
    # Date and time this activity record has been created (different from the 'status.dateTime', which is the time of a status change of the associated object, if applicable).
    created_date_time = db.DateProperty()
    # Inofrmation on consequence of event resulting in this activity record.
    status = db.ReferenceProperty()
#    organisations = db.ListProperty(db.Key)

#    @property
#    def activity_records(self):
#        return ErpOrganisation.gql("WHERE organisations = :1", self.key())
#    market_factors = db.ListProperty(db.Key)

#    @property
#    def activity_records(self):
#        return MarketFactors.gql("WHERE market_factors = :1", self.key())
#    locations = db.ListProperty(db.Key)

#    @property
#    def activity_records(self):
#        return Location.gql("WHERE locations = :1", self.key())
#    assets = db.ListProperty(db.Key)

#    @property
#    def activity_records(self):
#        return Asset.gql("WHERE assets = :1", self.key())
#    power_system_resources = db.ListProperty(db.Key)

#    @property
#    def activity_records(self):
#        return PowerSystemResource.gql("WHERE power_system_resources = :1", self.key())
#    documents = db.ListProperty(db.Key)

#    @property
#    def activity_records(self):
#        return Document.gql("WHERE documents = :1", self.key())
#    scheduled_event = db.ReferenceProperty()
#    erp_persons = db.ListProperty(db.Key)

#    @property
#    def activity_records(self):
#        return ErpPerson.gql("WHERE erp_persons = :1", self.key())

class PositionPoint(Element):
    """ Set of spatial coordinates that determine a point. A sequence of PositionPoints can be used to describe: - physical location of non-point oriented objects like cables or lines, or - area of an object like a substation, a geographical zone or a diagram object.
    """

    # X axis position.
    x_position = db.StringProperty()
    # Y axis position.
    y_position = db.StringProperty()
    # Zero-relative sequence number of this point within a series of points.
    sequence_number = db.IntegerProperty()
    # (if applicable) Z axis position.
    z_position = db.StringProperty()
#    location = db.ReferenceProperty()

class StreetAddress(Element):
    """ General purpose street address information.
    """

    # Street detail.
    street_detail = db.ReferenceProperty()
    # Town detail.
    town_detail = db.ReferenceProperty()
    # Status of this address.
    status = db.ReferenceProperty()

class TownDetail(Element):
    """ Town details, in the context of address.
    """

    # Town name.
    name = db.StringProperty()
    # Town section. For example, it is common for there to be 36 sections per township.
    section = db.StringProperty()
    # Name of the state or province.
    state_or_province = db.StringProperty()
    # Town code.
    code = db.StringProperty()
    # Name of the country.
    country = db.StringProperty()

class UserAttribute(Element):
    """ Generic name-value pair class, with optional sequence number and units for value; can be used to model parts of information exchange when concrete types are not known in advance.
    """

    # Value of an attribute, including unit information.
    value = StringQuantity
    # Sequence number for this attribute in a list of attributes.
    sequence_number = db.IntegerProperty()
    # Name of an attribute.
    name = db.StringProperty()
#    property_specification = db.ReferenceProperty()
#    procedure_data_sets = db.ListProperty(db.Key)

#    @property
#    def properties(self):
#        return ProcedureDataSet.gql("WHERE procedure_data_sets = :1", self.key())
#    property_assets = db.ListProperty(db.Key)

#    @property
#    def properties(self):
#        return Asset.gql("WHERE property_assets = :1", self.key())
#    erp_ledger_entries = db.ListProperty(db.Key)

#    @property
#    def user_attributes(self):
#        return ErpLedgerEntry.gql("WHERE erp_ledger_entries = :1", self.key())
#    erp_statement_line_items = db.ListProperty(db.Key)

#    @property
#    def user_attributes(self):
#        return MarketStatementLineItem.gql("WHERE erp_statement_line_items = :1", self.key())
#    bill_determinants = db.ListProperty(db.Key)

#    @property
#    def user_attributes(self):
#        return BillDeterminant.gql("WHERE bill_determinants = :1", self.key())
#    pass_through_bills = db.ListProperty(db.Key)

#    @property
#    def user_attributes(self):
#        return PassThroughBill.gql("WHERE pass_through_bills = :1", self.key())
#    rating_specification = db.ReferenceProperty()
#    transaction = db.ReferenceProperty()
#    erp_invoice_line_items = db.ListProperty(db.Key)

#    @property
#    def user_attributes(self):
#        return ErpInvoiceLineItem.gql("WHERE erp_invoice_line_items = :1", self.key())
#    rating_assets = db.ListProperty(db.Key)

#    @property
#    def ratings(self):
#        return Asset.gql("WHERE rating_assets = :1", self.key())
#    procedure = db.ReferenceProperty()

class Document(IdentifiedObject):
    """ Parent class for different groupings of information collected and managed as a part of a business process. It will frequently contain references to other objects, such as assets, people and power system resources.
    """

    # Date and time this document was last modified. Documents may potentially be modified many times during their lifetime.
    last_modified_date_time = db.DateProperty()
    # Document subject.
    subject = db.StringProperty()
    # Document title.
    title = db.StringProperty()
    # Revision number for this document.
    revision_number = db.StringProperty()
    # Date and time that this document was created.
    created_date_time = db.DateProperty()
    # Utility-specific categorisation of this document, according to their corporate standards, practices, and existing IT systems (e.g., for management of assets, maintenance, work, outage, customers, etc.).
    category = db.StringProperty()
    # Status of this document. For status of subject metter this document represents (e.g., Agreement, Work), use 'status' attribute. Example values for 'docStatus.status' are draft, approved, cancelled, etc.
    doc_status = db.ReferenceProperty()
    # Status of subject metter (e.g., Agreement, Work) this document represents. For status of the document itself, use 'docStatus' attribute.
    status = db.ReferenceProperty()
    # The 'from_document_roles' property has been implicitly created by
    # the to_document' property of DocDocRole.
    pass
#    schedule_parameter_infos = db.ListProperty(db.Key)

#    @property
#    def documents(self):
#        return ScheduleParameterInfo.gql("WHERE schedule_parameter_infos = :1", self.key())
    # The 'change_items' property has been implicitly created by
    # the document' property of ChangeItem.
    pass
#    network_data_sets = db.ListProperty(db.Key)

#    @property
#    def documents(self):
#        return NetworkDataSet.gql("WHERE network_data_sets = :1", self.key())
#    activity_records = db.ListProperty(db.Key)

#    @property
#    def documents(self):
#        return ActivityRecord.gql("WHERE activity_records = :1", self.key())
    # The 'power_system_resource_roles' property has been implicitly created by
    # the document' property of DocPsrRole.
    pass
    # The 'location_roles' property has been implicitly created by
    # the document' property of DocLocRole.
    pass
#    change_sets = db.ListProperty(db.Key)

#    @property
#    def documents(self):
#        return ChangeSet.gql("WHERE change_sets = :1", self.key())
    # The 'erp_person_roles' property has been implicitly created by
    # the document' property of DocErpPersonRole.
    pass
    # The 'asset_roles' property has been implicitly created by
    # the document' property of DocAssetRole.
    pass
    # The 'scheduled_events' property has been implicitly created by
    # the document' property of ScheduledEvent.
    pass
#    electronic_address = db.ReferenceProperty()
#    measurements = db.ListProperty(db.Key)

#    @property
#    def documents(self):
#        return Measurement.gql("WHERE measurements = :1", self.key())
    # The 'to_document_roles' property has been implicitly created by
    # the from_document' property of DocDocRole.
    pass
    # The 'erp_organisation_roles' property has been implicitly created by
    # the document' property of DocOrgRole.
    pass

class ElectronicAddress(IdentifiedObject):
    """ Electronic address information.
    """

    # Password needed to log in.
    password = db.StringProperty()
    # Radio address.
    radio = db.StringProperty()
    # Email address.
    email = db.StringProperty()
    # World Wide Web address.
    web = db.StringProperty()
    # User ID needed to log in, which can be for an individual person, an organisation, a location, etc.
    user_id = db.StringProperty()
    # Address on local area network.
    lan = db.StringProperty()
    # Status of this electronic address.
    status = db.ReferenceProperty()
#    organisation = db.ReferenceProperty()
#    locations = db.ListProperty(db.Key)

#    @property
#    def electronic_addresses(self):
#        return Location.gql("WHERE locations = :1", self.key())
#    document = db.ReferenceProperty()
#    cashier = db.ReferenceProperty()
#    asset = db.ReferenceProperty()
    # The 'erp_telephone_numbers' property has been implicitly created by
    # the electronic_address' property of ErpTelephoneNumber.
    pass
#    erp_person = db.ReferenceProperty()

class Status(Element):
    """ Current status information relevant to an entity.
    """

    # Date and time for which status 'value' applies.
    date_time = db.DateProperty()
    # Pertinent information regarding the current 'value', as free form text.
    remark = db.StringProperty()
    # Reason code or explanation for why an object went to the current status 'value'.
    reason = db.StringProperty()
    # Status value at 'dateTime'; prior status changes may have been kept in instances of ActivityRecords associated with the object to which this Status applies.
    value = db.StringProperty()

class PostalAddress(Element):
    """ General purpose postal address information.
    """

    # Postal code for the address.
    postal_code = db.StringProperty()
    # Post office box.
    po_box = db.StringProperty()
    # Town detail.
    town_detail = db.ReferenceProperty()
    # Street detail.
    street_detail = db.ReferenceProperty()

class DateTimeInterval(Element):
    """ Interval of date and time.
    """

    # Date and time that this interval started.
    start = db.DateProperty()
    # Date and time that this interval ended.
    end = db.DateProperty()

class Organisation(IdentifiedObject):
    """ Organisation that might have roles as utility, contractor, supplier, manufacturer, customer, etc.
    """

    # Street address.
    street_address = db.ReferenceProperty()
    # Postal address, potentially different than 'streetAddress' (e.g., another city).
    postal_address = db.ReferenceProperty()
#    business_roles = db.ListProperty(db.Key)

#    @property
#    def organisations(self):
#        return BusinessRole.gql("WHERE business_roles = :1", self.key())
    # The 'telephone_numbers' property has been implicitly created by
    # the organisation' property of TelephoneNumber.
    pass
#    market_roles = db.ListProperty(db.Key)

#    @property
#    def organisations(self):
#        return MarketRole.gql("WHERE market_roles = :1", self.key())
    # The 'electronic_addresses' property has been implicitly created by
    # the organisation' property of ElectronicAddress.
    pass

class TimePoint(IdentifiedObject):
    """ A point in time within a sequence of points in time relative to a TimeSchedule.
    """

    # (if sequence-based) Relative sequence number for this time point.
    sequence_number = db.IntegerProperty()
    # Absolute date and time for this time point. For calendar-based time point, it is typically manually entered, while for interval-based or sequence-based time point it is derived.
    absolute_time = db.DateProperty()
    # (if interval-based) A point in time relative to scheduled start time in 'TimeSchedule.scheduleInterval.start'.
    relative_time_interval = Seconds
    # Status of this time point.
    status = db.ReferenceProperty()
    # Interval defining the window of time that this time point is valid (for example, seasonal, only on weekends, not on weekends, only 8:00 to 5:00, etc.).
    window = db.ReferenceProperty()
    # The 'scheduled_events' property has been implicitly created by
    # the time_point' property of ScheduledEvent.
    pass
#    time_schedule = db.ReferenceProperty()

class StreetDetail(Element):
    """ Street details, in the context of address.
    """

    # Suffix to the street name. For example: North, South, East, West.
    suffix = db.StringProperty()
    # (if applicable) In certain cases the physical location of the place of interest does not have a direct point of entry from the street, but may be located inside a larger structure such as a building, complex, office block, apartment, etc.
    building_name = db.StringProperty()
    # Name of the street.
    name = db.StringProperty()
    # True if this street is within the legal geographical boundaries of the specified town (default).
    within_town_limits = db.BooleanProperty()
    # Prefix to the street name. For example: North, South, East, West.
    prefix = db.StringProperty()
    # (if applicable) Utilities often make use of external reference systems, such as those of the town-planner's department or surveyor general's mapping system, that allocate global reference codes to streets.
    code = db.StringProperty()
    # Designator of the specific location on the street.
    number = db.StringProperty()
    # Additional address information, for example a mailstop.
    address_general = db.StringProperty()
    # Type of street. Examples include: street, circle, boulevard, avenue, road, drive, etc.
    type = db.StringProperty()
    # Number of the apartment or suite.
    suite_number = db.StringProperty()

class TimeSchedule(Document):
    """ Description of anything that changes through time. Time schedule is used to perform a single-valued function of time. Use inherited 'category' attribute to give additional information on this schedule, such as: periodic (hourly, daily, weekly, monthly, etc.), day of the month, by date, calendar (specific times and dates).
    """

    # Interval at which the scheduled action repeats (e.g., first Monday of every month, last day of the month, etc.).
    recurrence_pattern = db.StringProperty()
    # True if this schedule is deactivated (disabled).
    disabled = db.BooleanProperty()
    # The offset from midnight (i.e., 0 hours, 0 minutes, 0 seconds) for the periodic time points to begin. For example, for an interval meter that is set up for five minute intervals ('recurrencePeriod'=300=5 min), setting 'offset'=120=2 min would result in scheduled events to read the meter executing at 2, 7, 12, 17, 22, 27, 32, 37, 42, 47, 52, and 57 minutes past each hour.
    offset = Seconds
    # Duration between time points, from the beginning of one period to the beginning of the next period. Note that a device like a meter may have multiple interval periods (e.g., 1, 5, 15, 30, or 60 minutes).
    recurrence_period = Seconds
    # Schedule date and time interval.
    schedule_interval = db.ReferenceProperty()
    # The 'time_points' property has been implicitly created by
    # the time_schedule' property of TimePoint.
    pass

class Agreement(Document):
    """ Formal agreement between two parties defining the terms and conditions for a set of services. The specifics of the services are, in turn, defined via one or more service agreements.
    """

    # Date this agreement was consumated among associated persons and/or organisations.
    sign_date = AbsoluteDate
    # Date and time interval this agreement is valid (from going into effect to termination).
    validity_interval = db.ReferenceProperty()


