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
from cim14 import Element

from cim14.iec61970.domain import Seconds
from cim14.iec61970.domain import AbsoluteDate

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

DiagramKind = db.StringProperty(choices=("geographic", "design_sketch", "schematic", "other", "internal_view"))

SkillLevelKind = db.StringProperty(choices=("other", "apprentice", "standard", "master"))

ChangeItemKind = db.StringProperty(choices=("modify", "add", "delete"))

MarketRoleKind = db.StringProperty(choices=("energy_service_consumer", "transmission_service_provider", "transmission_owner", "interchange_authority", "transmission_operator", "transmission_planner", "standards_developer", "planning_authority", "load_serving_entity", "competitive_retailer", "compliance_monitor", "resource_planner", "generator_owner", "distribution_provider", "reliability_authority", "balancing_authority", "other", "purchasing_selling_entity", "generator_operator"))

ns_prefix = "cim.IEC61968.Informative.InfCommon"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#IEC61968.Informative.InfCommon"

class ScheduledEvent(IdentifiedObject):
    """ Signifies an event to trigger one or more activities, such as reading a meter, recalculating a bill, requesting work, when generating units must be scheduled for maintenance, when a transformer is scheduled to be refurbished, etc.
    """

    # Duration of the scheduled event, for example, the time to ramp between values.
    duration = Seconds
    # Category of scheduled event.
    category = db.StringProperty()
    status = db.ReferenceProperty()
#    activity_record = db.ReferenceProperty()
#    time_point = db.ReferenceProperty()
#    assets = db.ListProperty(db.Key)

#    @property
#    def scheduled_events(self):
#        return Asset.gql("WHERE assets = :1", self.key())
#    schedule_parameter_info = db.ReferenceProperty()
#    document = db.ReferenceProperty()

class ChangeItem(IdentifiedObject):
    """ Description for a single change within an ordered list of changes.
    """

    # Kind of change for the associated object.
    kind = ChangeItemKind
    # Relative order of this ChangeItem in an ordered sequence of changes.
    sequence_number = db.IntegerProperty()
    status = db.ReferenceProperty()
#    power_system_resource = db.ReferenceProperty()
#    measurement = db.ReferenceProperty()
#    document = db.ReferenceProperty()
#    change_set = db.ReferenceProperty()
#    network_data_set = db.ReferenceProperty()
#    gml_selector = db.ReferenceProperty()
#    location = db.ReferenceProperty()
#    erp_person = db.ReferenceProperty()
#    asset = db.ReferenceProperty()
#    organisation = db.ReferenceProperty()
#    gml_observation = db.ReferenceProperty()

class Role(IdentifiedObject):
    """ Enumeration of potential roles that might be played by one object relative to another.
    """

    # Category of role.
    category = db.StringProperty()
    status = db.ReferenceProperty()

class Craft(IdentifiedObject):
    """ Craft of a person or a crew. Examples include overhead electric, underground electric, high pressure gas, etc. This ensures necessary knowledge and skills before being allowed to perform certain types of work.
    """

    # Category by utility's work mangement standards and practices.
    category = db.StringProperty()
    status = db.ReferenceProperty()
#    erp_persons = db.ListProperty(db.Key)

#    @property
#    def crafts(self):
#        return ErpPerson.gql("WHERE erp_persons = :1", self.key())
#    capabilities = db.ListProperty(db.Key)

#    @property
#    def crafts(self):
#        return Capability.gql("WHERE capabilities = :1", self.key())
#    skills = db.ListProperty(db.Key)

#    @property
#    def crafts(self):
#        return Skill.gql("WHERE skills = :1", self.key())

class ScheduleParameterInfo(IdentifiedObject):
    """ Schedule parameters for an activity that is to occur, is occurring, or has completed.
    """

    # Estimated date and time for activity execution (with earliest possibility of activity initiation and latest possibility of activity completion).
    estimated_window = db.DateProperty()
    status = db.ReferenceProperty()
    # Requested date and time interval for activity execution.
    requested_window = db.ReferenceProperty()
    # The 'scheduled_events' property has been implicitly created by
    # the schedule_parameter_info' property of ScheduledEvent.
    pass
#    for_inspection_data_set = db.ReferenceProperty()
#    documents = db.ListProperty(db.Key)

#    @property
#    def schedule_parameter_infos(self):
#        return Document.gql("WHERE documents = :1", self.key())

class Diagram(Document):
    """ GML and/or other means are used for rendering objects on various types of displays(geographic, schematic, other) and maps associated with various coordinate systems.
    """

    # Kind of this diagram.
    kind = DiagramKind
#    gml_coordinate_system = db.ReferenceProperty()
#    gml_diagram_objects = db.ListProperty(db.Key)

#    @property
#    def diagrams(self):
#        return GmlDiagramObject.gql("WHERE gml_diagram_objects = :1", self.key())
#    design_locations = db.ListProperty(db.Key)

#    @property
#    def diagrams(self):
#        return DesignLocation.gql("WHERE design_locations = :1", self.key())

class BankAccount(Document):
    """ Bank account.
    """

    # Account reference number.
    account_number = db.StringProperty()
#    bank = db.ReferenceProperty()
#    service_supplier = db.ReferenceProperty()
    # The 'bank_statements' property has been implicitly created by
    # the bank_account' property of BankStatement.
    pass

class BusinessRole(IdentifiedObject):
    """ A business role that this organisation plays. A single organisation typically performs many functions, each one described as a role.
    """

    # Category by utility's corporate standards and practices.
    category = db.StringProperty()
    status = db.ReferenceProperty()
#    organisations = db.ListProperty(db.Key)

#    @property
#    def business_roles(self):
#        return Organisation.gql("WHERE organisations = :1", self.key())

class Skill(Document):
    """ Proficiency level of a craft, which is required to operate or maintain a particular type of asset and/or perform certain types of work.
    """

    # Date and time skill certification expires.
    expiration_date_time = db.DateProperty()
    # Date and time skill became effective.
    effective_date_time = db.DateProperty()
    # Level of skill for a Craft.
    level = SkillLevelKind
    # Date of certification.
    certified_date = AbsoluteDate
#    crafts = db.ListProperty(db.Key)

#    @property
#    def skills(self):
#        return Craft.gql("WHERE crafts = :1", self.key())
#    qualification_requirements = db.ListProperty(db.Key)

#    @property
#    def skills(self):
#        return QualificationRequirement.gql("WHERE qualification_requirements = :1", self.key())
#    erp_person = db.ReferenceProperty()

class BusinessPlan(Document):
    """ A BusinessPlan is an organized sequence of predetermined actions required to complete a future organizational objective. It is a type of document that typically references a schedule, physical and/or logical resources (assets and/or PowerSystemResources), locations, etc.
    """

    pass

class MarketRole(IdentifiedObject):
    """ Role an organisation plays in a market. Examples include one or more of values defined in MarketRoleKind.
    """

    # Kind of role an organisation plays in a market.
    kind = MarketRoleKind
    status = db.ReferenceProperty()
#    organisations = db.ListProperty(db.Key)

#    @property
#    def market_roles(self):
#        return Organisation.gql("WHERE organisations = :1", self.key())

class Ratio(Element):
    """ Fraction specified explicitly with a numerator and denominator, which can be used to calculate the quotient.
    """

    # The part of a fraction that is above the line and signifies the number to be divided by the denominator.
    numerator = db.FloatProperty()
    # The part of a fraction that is below the line and that functions as the divisor of the numerator.
    denominator = db.FloatProperty()

class DocDocRole(Role):
    """ Roles played between Documents and other Documents.
    """

#    to_document = db.ReferenceProperty()
#    from_document = db.ReferenceProperty()

class DocPsrRole(Role):
    """ Potential roles that might played by a document relative to a type of PowerSystemResource.
    """

#    document = db.ReferenceProperty()
#    power_system_resource = db.ReferenceProperty()

class Map(Diagram):
    """ A type of diagram that is usually printed on paper. It normally depicts part of the earth's surface, showing utility assets, right of ways, topological data, coordinates, grids, etc. Maps vary depending on whether they are used for dispatch, design, schematic, etc.
    """

    # Page number for particular set of maps specified by 'category'.
    page_number = db.IntegerProperty()
    # Map grid number.
    map_loc_grid = db.StringProperty()


