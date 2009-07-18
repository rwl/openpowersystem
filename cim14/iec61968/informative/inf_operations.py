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

from cim14.iec61968.common import Document
from cim14.iec61968.informative.inf_common import Role
from cim14.iec61970.core import IdentifiedObject
from cim14.iec61968.common import ActivityRecord

from cim14.iec61970.domain import Minutes
from cim14.iec61970.domain import Voltage

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

OutageKind = db.StringProperty(choices=("fixed", "forced", "flexible"))

CircuitConnectionKind = db.StringProperty(choices=("nominally_connected", "electrically_connected", "as_built", "other"))

TroubleReportingKind = db.StringProperty(choices=("letter", "email", "other", "call"))

SwitchingStepStatusKind = db.StringProperty(choices=("confirmed", "skipped", "proposed", "instructed", "aborted"))

ns_prefix = "cim.IEC61968.Informative.InfOperations"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#IEC61968.Informative.InfOperations"

class OperationalRestriction(Document):
    """ A document that can be associated with a device to describe any sort of restrictions compared with the original manufacturer's specification e.g. temporary maximum loadings, maximum switching current, do not operate if bus couplers are open etc etc.  In the UK, for example, if a breaker or switch ever mal-operates, this is reported centrally and utilities use their asset systems to identify all the installed devices of the same manufacturer's type. They then apply operational restrictions in the operational systems to warn operators of potential problems. After appropriate inspection and maintenance, the operational restrictions may be removed.
    """

    # Date and time restriction is applied.
    start_date_time = db.DateProperty()
    # Reason for applying restriction.
    reason = db.StringProperty()
    # Date and time restriction is lifted.
    end_date_time = db.DateProperty()

class ErpPersonScheduleStepRole(Role):
    """ Roles played between Persons and Schedule Steps.
    """

#    switching_step = db.ReferenceProperty()
#    erp_person = db.ReferenceProperty()

class OutageReport(Document):
    """ Document with statistics of an outage.
    """

    # Total Customer Minutes Lost (CML).
    total_cml = Minutes
    # Average Customer Minutes Lost (CML) for this outage.
    average_cml = Minutes
    # Total number of outaged customers.
    customer_count = db.IntegerProperty()
    # Total outage duration.
    outage_duration = Minutes
#    outage_record = db.ReferenceProperty()
#    outage_history = db.ReferenceProperty()

class IncidentCode(IdentifiedObject):
    """ Classification of incident types. Multiple incident codes may apply to a given incident. The primary overall incident cause is recorded in 'IncidentRecord.category', and the main code in 'name'.
    """

    # Additional level of classification detail (as extension to the main code found in 'name').
    sub_code = db.StringProperty()
#    incident_records = db.ListProperty(db.Key)

#    @property
#    def incident_codes(self):
#        return IncidentRecord.gql("WHERE incident_records = :1", self.key())

class ComplianceEvent(ActivityRecord):
    """ Compliance events are used for reporting regulatory or contract compliance issues and/or variances. These might be created as a consequence of local business processes and associated rules. It is anticipated that this class will be customised extensively to meet local implementation needs. Use inherited 'category' to indicate that, for example, expected performance will not be met or reported as mandated.
    """

    # The deadline for compliance.
    deadline = db.DateProperty()
    # Type of compliance event indicating, for example, types of regulatory and/or contractual compliance events where expected performance will not be met or reported as mandated.
    compliance_type = db.StringProperty()

class OutageCode(IdentifiedObject):
    """ Classification of outage types. Multiple outage codes may apply to a given outage or outage step.The primary overall outage type is recorded in OutageRecord.outageType. There may be more than one classification per outage step and/or per outage record. Example codes/subcodes include: weather/ice, weather/lightning, wildlife/squirrel, wildlife/bird, burned/overload, burned/weather, wire down/accident, wire down/tree, wire down/vandalism, etc. The typical 'outage code' is in the inherited 'name' attribute. The code is described in the inherited 'description' attribute.
    """

    # The main code is stored in the inherited .name. This sub-code provides an additional level of classification detail.
    sub_code = db.StringProperty()
#    outage_records = db.ListProperty(db.Key)

#    @property
#    def outage_codes(self):
#        return OutageRecord.gql("WHERE outage_records = :1", self.key())
#    outage_steps = db.ListProperty(db.Key)

#    @property
#    def outage_codes(self):
#        return OutageStep.gql("WHERE outage_steps = :1", self.key())

class NetworkDataSet(IdentifiedObject):
    """ Categorized as a type of document, model of a portion of the electrical network that includes a list of the equipment, along with relevant connectivity, electrical characteristics, geographical location, and various parameters associated with the equipment.
    """

    # Category of network data set.
    category = db.StringProperty()
    status = db.ReferenceProperty()
#    land_bases = db.ListProperty(db.Key)

#    @property
#    def network_data_sets(self):
#        return LandBase.gql("WHERE land_bases = :1", self.key())
#    power_system_resources = db.ListProperty(db.Key)

#    @property
#    def network_data_sets(self):
#        return PowerSystemResource.gql("WHERE power_system_resources = :1", self.key())
#    circuits = db.ListProperty(db.Key)

#    @property
#    def network_data_sets(self):
#        return Circuit.gql("WHERE circuits = :1", self.key())
#    documents = db.ListProperty(db.Key)

#    @property
#    def network_data_sets(self):
#        return Document.gql("WHERE documents = :1", self.key())
#    change_sets = db.ListProperty(db.Key)

#    @property
#    def network_data_sets(self):
#        return ChangeSet.gql("WHERE change_sets = :1", self.key())
#    circuit_sections = db.ListProperty(db.Key)

#    @property
#    def network_data_sets(self):
#        return CircuitSection.gql("WHERE circuit_sections = :1", self.key())
    # The 'change_items' property has been implicitly created by
    # the network_data_set' property of ChangeItem.
    pass

class LandBase(Document):
    """ Land base data.
    """

#    change_sets = db.ListProperty(db.Key)

#    @property
#    def land_bases(self):
#        return ChangeSet.gql("WHERE change_sets = :1", self.key())
#    network_data_sets = db.ListProperty(db.Key)

#    @property
#    def land_bases(self):
#        return NetworkDataSet.gql("WHERE network_data_sets = :1", self.key())

class PlannedOutage(Document):
    """ Planned outage involves network operations which will affect the supply of power to customers. Note that the list of Power System Resources for the PlannedOutage may be the same or a superset of the ones per OutageStep.
    """

    # Kind of outage.
    kind = OutageKind
    # The 'outage_schedules' property has been implicitly created by
    # the planned_outage' property of OutageSchedule.
    pass
    # The 'customer_datas' property has been implicitly created by
    # the planned_outage' property of Customer.
    pass

class CircuitSection(IdentifiedObject):
    """ Section of circuit located between two sectionalizing devices. It may contain other circuit sections, for example, a lateral tapped off a primary.
    """

    # Kind of this circuit section.
    connection_kind = CircuitConnectionKind
#    power_system_resources = db.ListProperty(db.Key)

#    @property
#    def circuit_sections(self):
#        return PowerSystemResource.gql("WHERE power_system_resources = :1", self.key())
#    member_of_circuit_section = db.ReferenceProperty()
    # The 'linear_conductors' property has been implicitly created by
    # the circuit_section' property of LinearConductorAsset.
    pass
    # The 'contains_circuit_sections' property has been implicitly created by
    # the member_of_circuit_section' property of CircuitSection.
    pass
#    network_data_sets = db.ListProperty(db.Key)

#    @property
#    def circuit_sections(self):
#        return NetworkDataSet.gql("WHERE network_data_sets = :1", self.key())
#    circuits = db.ListProperty(db.Key)

#    @property
#    def circuit_sections(self):
#        return Circuit.gql("WHERE circuits = :1", self.key())

class TroubleTicket(Document):
    """ A document used to report electrical trouble. The trouble may either be an outage or non-outage problem, such as power quality. It must always be associated with an Incident Record. Note that a separate Activity Record is created for each call associated with an instance of Trouble Ticket. The time of a call is stored in ActivityRecord.createdOn and comments are recorded in ActivityRecord.remarks.
    """

    # Date and time at which this source of trouble started.
    start_date_time = db.DateProperty()
    # Date and time trouble call first received. The date and time of subsequent calls by the same customer for the same trouble are recorded in associated Activity Records.
    first_call_date_time = db.DateProperty()
    # True if person reporting trouble requested a call back to confirm power has been restored. The person and their contact information is maintained in the assoicated Customer informaiton. Call back results are recorded in assoicated 'ActivityRecord.Status.remarks'.
    inform_after_restored = db.BooleanProperty()
    # Priority of trouble call.
    priority = db.StringProperty()
    # Estimated restoration date and time last provided to the customer.
    estimated_restore_date_time = db.DateProperty()
    # True if person reporting trouble requested a call back when sigificant information became available about cause of the outage and the estimated restoration time. The person and their contact information are maintained in the assoicated Customer information. Call back results are recorded in assoicated 'ActivityRecord.Status.remarks'.
    inform_before_restored = db.BooleanProperty()
    # Advice already given to the customer at time when trouble was first reported.
    advice = db.StringProperty()
    # Time of restoration of resolution of trouble.
    restoration_time = db.DateProperty()
    # Code for a reported hazard condition.
    hazard_code = db.StringProperty()
    # True if requested to customer when someone is about to arrive at their premises.
    call_back = db.BooleanProperty()
    # Means the customer used to report trouble (default is 'call').
    reporting_kind = TroubleReportingKind
#    call_backs = db.ListProperty(db.Key)

#    @property
#    def trouble_tickets(self):
#        return CallBack.gql("WHERE call_backs = :1", self.key())
#    customer_data = db.ReferenceProperty()
#    incident_record = db.ReferenceProperty()

class OutageNotification(Document):
    """ A document containing information to be sent to customers notifying that an outage will take place. This is used to generate mailing lists for customers.
    """

    # Details of the outage 'reason'.
    reason = db.StringProperty()
    # Likely duration of the interruption(s).
    duration = Minutes
    # Number of possible interruptions that the customer may expect for this event.
    expected_interruption_count = db.IntegerProperty()
#    customer_datas = db.ListProperty(db.Key)

#    @property
#    def outage_notifications(self):
#        return Customer.gql("WHERE customer_datas = :1", self.key())

class OutageStep(IdentifiedObject):
    """ Holds an outage start and end time for each supply point of an outage record. The supply point for a given step is the associated PowerSystemResource instance.
    """

    # True if injuries reported by caller or engineer.
    injury = db.BooleanProperty()
    # Average Customer Minutes Lost (CML) for this supply point for this outage.
    average_cml = Minutes
    # Number of customers with high reliability required.
    special_customer_count = db.IntegerProperty()
    # Number of customers connected to the PowerSystemResource.
    total_customer_count = db.IntegerProperty()
    job_priority = db.StringProperty()
    # Estimated time of restoration.
    estimated_restore_date_time = db.DateProperty()
    # True if fatalities reported by caller or engineer.
    fatality = db.BooleanProperty()
    # True if damage reported by caller or engineer.
    damage = db.BooleanProperty()
    # Number of customers with critical needs, e.g., with a dialysis machine.
    critical_customer_count = db.IntegerProperty()
    # True if shocks reported by caller or engineer.
    shock_reported = db.BooleanProperty()
    # Number of customers phoning in.
    caller_count = db.IntegerProperty()
    # Total Customer Minutes Lost (CML) for this supply point for this outage.
    total_cml = Minutes
    status = db.ReferenceProperty()
    # Date and time interval between loss and restoration of power.
    no_power_interval = db.ReferenceProperty()
    # The 'conducting_equipment_roles' property has been implicitly created by
    # the outage_step' property of OutageStepPsrRole.
    pass
#    outage_record = db.ReferenceProperty()
#    outage_codes = db.ListProperty(db.Key)

#    @property
#    def outage_steps(self):
#        return OutageCode.gql("WHERE outage_codes = :1", self.key())
#    crews = db.ListProperty(db.Key)

#    @property
#    def outage_steps(self):
#        return Crew.gql("WHERE crews = :1", self.key())

class OutageStepPsrRole(Role):
    """ Roles played between Power System Resources and Outage Steps. Examples roles include: normal supply, actual supply, interrupting device, restoration device.
    """

#    conducting_equipment = db.ReferenceProperty()
#    outage_step = db.ReferenceProperty()

class IncidentRecord(Document):
    """ Document describing the incident reported in a TroubleTicket. If the incident has to do with an outage, this will be associated with an OutageRecord. Primary cause of the incident is captured in 'category'.
    """

    # Date and time incident was resolved for all customers impacted by this incident.
    end_date_time = db.DateProperty()
    # Date and time first customer was impacted by the incident.
    start_date_time = db.DateProperty()
    # The 'trouble_tickets' property has been implicitly created by
    # the incident_record' property of TroubleTicket.
    pass
#    incident_codes = db.ListProperty(db.Key)

#    @property
#    def incident_records(self):
#        return IncidentCode.gql("WHERE incident_codes = :1", self.key())

class SwitchingSchedule(Document):
    """ Document describing a sequence of steps to perform an item of work, for example to isolate some plant with regard to safety, equipment ratings, and standards of customer service. Note 1: SwitchingSchedule is intended to describe the full operational details for switching for real time operation which includes other operations such as grounding, applying safety documents etc.  Note 2: The association to ErpPerson suits the UK practice of quoting specific names (e.g the crew foreman). The association to Crew is for US practice.
    """

    # Reason for switching.
    reason = db.StringProperty()
    # Start date and time of switching.
    start_date_time = db.DateProperty()
    # Completion date and time of switching.
    end_date_time = db.DateProperty()
#    crews = db.ListProperty(db.Key)

#    @property
#    def switching_schedules(self):
#        return Crew.gql("WHERE crews = :1", self.key())
    # The 'schedule_steps' property has been implicitly created by
    # the switching_schedule' property of SwitchingStep.
    pass
#    work_task = db.ReferenceProperty()

class OutageRecord(Document):
    """ A document describing details of an outage in part of the electrical network, typically produced by a SCADA system following a breaker trip, or within a Trouble Call System by grouping customer calls. This has an associated OutageStep for each supply point. Primary cause of the outage is captured in 'category'. In some countries all outage restoration is performed using a SwitchingSchedule which complements the OutageRecord and records the ErpPersons (crew) and any planned Work. In other systems, it may be acceptable to manage outages including new WorkTasks without switching schedules. Note: The relationship between OutageRecord and ErpPerson and Crew is inherited as each is a type of Document.
    """

    # Overall action taken to resolve outage (details are in 'WorkTasks').
    action_taken = db.StringProperty()
    # Value of ErpOrganisation.mode at the time of OutageRecord.startDateTime.
    mode = db.StringProperty()
    # The damage code relative to the associated PowerSystemResource(s) and/or Asset(s). Examples include broken, burnout, failure, flashed (burned), manually operated, wire down, no damage - rolling blackout, none.
    damage_code = db.StringProperty()
    # True if planned, false otherwise (for example due to a breaker trip).
    is_planned = db.BooleanProperty()
    # Date and time restoration was completed for all customers impacted by this outage.
    end_date_time = db.DateProperty()
    # The 'outage_steps' property has been implicitly created by
    # the outage_record' property of OutageStep.
    pass
#    outage_codes = db.ListProperty(db.Key)

#    @property
#    def outage_records(self):
#        return OutageCode.gql("WHERE outage_codes = :1", self.key())
#    outage_report = db.ReferenceProperty()

class Circuit(IdentifiedObject):
    """ Static collection of conducting equipment originating at a main distribution center and supplying one or more secondary distribution centers, one or more branch-circuit distribution centers, or any combination of these two types of equipment. It is the source to the next normally open point.
    """

    # Rated voltage of the circuit.
    rated_voltage = Voltage
    # Kind of this circuit.
    connection_kind = CircuitConnectionKind
#    power_system_resources = db.ListProperty(db.Key)

#    @property
#    def circuits(self):
#        return PowerSystemResource.gql("WHERE power_system_resources = :1", self.key())
#    network_data_sets = db.ListProperty(db.Key)

#    @property
#    def circuits(self):
#        return NetworkDataSet.gql("WHERE network_data_sets = :1", self.key())
#    circuit_sections = db.ListProperty(db.Key)

#    @property
#    def circuits(self):
#        return CircuitSection.gql("WHERE circuit_sections = :1", self.key())

class ChangeSet(IdentifiedObject):
    """ The updates required in a transaction for an existing data set are grouped into a single ChangeSet. In data sets (e.g., NetworkDataSet), each major step in the ChangeSet is described through a separate ChangeItem associated with the data set. Within each data set, each inidividual object change is described with a seperate ChangeItem associated with the object.
    """

    status = db.ReferenceProperty()
#    land_bases = db.ListProperty(db.Key)

#    @property
#    def change_sets(self):
#        return LandBase.gql("WHERE land_bases = :1", self.key())
    # The 'change_items' property has been implicitly created by
    # the change_set' property of ChangeItem.
    pass
#    documents = db.ListProperty(db.Key)

#    @property
#    def change_sets(self):
#        return Document.gql("WHERE documents = :1", self.key())
#    network_data_sets = db.ListProperty(db.Key)

#    @property
#    def change_sets(self):
#        return NetworkDataSet.gql("WHERE network_data_sets = :1", self.key())

class OrgPsrRole(Role):
    """ Roles played between Organisations and Power System Resources.
    """

#    erp_organisation = db.ReferenceProperty()
#    power_system_resource = db.ReferenceProperty()

class CallBack(IdentifiedObject):
    """ Information about a planned CallBack or a CallBack that has occurred, from the utility to a customer regarding the status and plans about resolving trouble, performing work, etc.
    """

    # Comments by customer during this call back.
    comment = db.StringProperty()
    # Additional contact details that are not provided for ErpPerson with ErpTelephoneNumber.
    contact_detail = db.StringProperty()
    # Advice already given to the customer during this call back.
    advice = db.StringProperty()
    # Descriptiion of the problem reported during this call back.
    problem_info = db.StringProperty()
    # (if callback already occured) Date and time when this call back occurred.
    date_time = db.DateProperty()
    status = db.ReferenceProperty()
    # The 'appointments' property has been implicitly created by
    # the call_back' property of Appointment.
    pass
#    erp_persons = db.ListProperty(db.Key)

#    @property
#    def call_backs(self):
#        return ErpPerson.gql("WHERE erp_persons = :1", self.key())
#    trouble_tickets = db.ListProperty(db.Key)

#    @property
#    def call_backs(self):
#        return TroubleTicket.gql("WHERE trouble_tickets = :1", self.key())

class SwitchingStep(IdentifiedObject):
    """ A single step within a SwitchingSchedule. Could be a switching operation (applying a network alteration), or issuing a safety document. Note: Inherited attribute IdentifiedObject.name is used to hold the sequence number.
    """

    # The time and date that the Required Control Action was issued.
    instructed_date_time = db.DateProperty()
    # Desired end state for the associated PowerSystemResource as a result of this schedule step.
    desired_end_state = db.StringProperty()
    # Information regarding this switching schedule step.
    text = db.StringProperty()
    # The time and date that the Required Control Action was completed.
    completed_date_time = db.DateProperty()
    # Control actions required to perform this step.
    required_control_action = db.StringProperty()
    # Status of this SwitchingStep.
    status_kind = SwitchingStepStatusKind
#    erp_person_role = db.ReferenceProperty()
#    power_system_resources = db.ListProperty(db.Key)

#    @property
#    def schedule_steps(self):
#        return PowerSystemResource.gql("WHERE power_system_resources = :1", self.key())
#    switching_schedule = db.ReferenceProperty()
#    safety_document = db.ReferenceProperty()

class SafetyDocument(Document):
    """ Document used during the course of work on the electrical system for safety purposes. Note: ClearanceTag is a special case of a Safety Document.
    """

    # The 'schedule_steps' property has been implicitly created by
    # the safety_document' property of SwitchingStep.
    pass
#    clearance_tags = db.ListProperty(db.Key)

#    @property
#    def safety_documents(self):
#        return ClearanceTag.gql("WHERE clearance_tags = :1", self.key())
#    power_system_resource = db.ReferenceProperty()


