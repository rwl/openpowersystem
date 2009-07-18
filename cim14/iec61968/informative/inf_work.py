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
from cim14.iec61970.core import IdentifiedObject
from cim14.iec61968.informative.inf_assets import ProcedureDataSet
from cim14.iec61968.informative.inf_common import ScheduledEvent
from cim14.iec61968.common import Location
from cim14.iec61968.common import ActivityRecord

from cim14.iec61970.core import PhaseCode
from cim14.iec61970.domain import Money
from cim14.iec61970.domain import AbsoluteDate
from cim14.iec61970.domain import IntegerQuantity
from cim14.iec61970.domain import Hours
from cim14.iec61970.domain import CostRate
from cim14.iec61970.domain import PerCent
from cim14.iec61970.domain import Length

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

ConditionFactorKind = db.StringProperty(choices=("material", "travel", "other", "account_allocation", "labor"))

WorkActionKind = db.StringProperty(choices=("install", "abandon", "remove", "transfer"))

DesignKind = db.StringProperty(choices=("other", "as_built", "estimated"))

ns_prefix = "cim.IEC61968.Informative.InfWork"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#IEC61968.Informative.InfWork"

class Request(Document):
    """ A request for work, service or project.
    """

    # The corporate code for this request.
    corporate_code = db.StringProperty()
    # Based on the current 'Status.status', the action that is needed before this Request can transition to the desired state, such as initiating the requested Work. For example, missing or additionally needed information may be required from the requesting organisation before a work Design may be created.
    action_needed = db.StringProperty()
    # The priority of this request.
    priority = db.StringProperty()
#    erp_quote_line_item = db.ReferenceProperty()
#    organisation = db.ReferenceProperty()
    # The 'works' property has been implicitly created by
    # the request' property of Work.
    pass
#    projects = db.ListProperty(db.Key)

#    @property
#    def requests(self):
#        return Project.gql("WHERE projects = :1", self.key())

class CostType(IdentifiedObject):
    """ A categorization for resources, often costs, in accounting transactions. Examples include: material components, building in service, coal sales, overhead, etc.
    """

    # True if an amount can be assigned to the resource element (e.g., building in service, transmission plant, software development capital); false otherwise (e.g., internal labor, material components).
    amount_assignment_flag = db.BooleanProperty()
    # A codified representation of the resource element.
    code = db.StringProperty()
    # The level of the resource element in the hierarchy of resource elements (recursive relationship).
    level = db.StringProperty()
    # The stage for which this costType applies: estimated design, estimated actual or actual actual.
    stage = db.StringProperty()
    status = db.ReferenceProperty()
#    parent_cost_type = db.ReferenceProperty()
    # The 'child_cost_types' property has been implicitly created by
    # the parent_cost_type' property of CostType.
    pass
    # The 'compatible_units' property has been implicitly created by
    # the cost_type' property of CompatibleUnit.
    pass
#    erp_journal_entries = db.ListProperty(db.Key)

#    @property
#    def cost_types(self):
#        return ErpJournalEntry.gql("WHERE erp_journal_entries = :1", self.key())
    # The 'work_cost_details' property has been implicitly created by
    # the cost_type' property of WorkCostDetail.
    pass

class Usage(IdentifiedObject):
    """ The way material and assets are used to perform a certain type of work task. The way is described in text in the inheritied description attribute.
    """

    status = db.ReferenceProperty()
#    work_task = db.ReferenceProperty()
#    work_equipment_asset = db.ReferenceProperty()
#    material_item = db.ReferenceProperty()

class QualificationRequirement(IdentifiedObject):
    """ Certain skills are required and must be certified in order for a person (typically a member of a crew) to be qualified to work on types of equipment.
    """

    # Qualification identifier.
    qualification_id = db.StringProperty()
#    culabor_items = db.ListProperty(db.Key)

#    @property
#    def qualification_requirements(self):
#        return CULaborItem.gql("WHERE culabor_items = :1", self.key())
#    skills = db.ListProperty(db.Key)

#    @property
#    def qualification_requirements(self):
#        return Skill.gql("WHERE skills = :1", self.key())
#    specifications = db.ListProperty(db.Key)

#    @property
#    def qualification_requirements(self):
#        return Specification.gql("WHERE specifications = :1", self.key())
#    work_tasks = db.ListProperty(db.Key)

#    @property
#    def qualification_requirements(self):
#        return WorkTask.gql("WHERE work_tasks = :1", self.key())

class DiagnosisDataSet(ProcedureDataSet):
    """ The result of a problem (typically an asset failure) diagnosis.
    """

    # Effect of problem.
    effect = db.StringProperty()
    # Root origin of problem determined during diagnosis.
    root_origin = db.StringProperty()
    # Code for diagnosed probem category.
    final_code = db.StringProperty()
    # Date and time preliminary assessment of problem was performed.
    preliminary_date = db.DateProperty()
    # Remarks pertaining to root cause findings during problem diagnosis.
    root_remark = db.StringProperty()
    # Phase(s) diagnosed.
    phase_code = PhaseCode
    # Cause of problem determined during diagnosis.
    final_cause = db.StringProperty()
    # Root cause of problem determined during diagnosis.
    root_cause = db.StringProperty()
    # Remarks pertaining to preliminary assessment of problem.
    preliminary_remark = db.StringProperty()
    # Date and time diagnosis was completed.
    final_date = db.DateProperty()
    # Origin of problem determined during diagnosis.
    final_origin = db.StringProperty()
    # Failuer mode, for example: Failure to Insulate; Failure to conduct; Failure to contain oil; Failure to provide ground plane; Other.
    failure_mode = db.StringProperty()
    # Remarks pertaining to findings during problem diagnosis.
    final_remark = db.StringProperty()
    # Code for problem category determined during preliminary assessment.
    preliminary_code = db.StringProperty()

class TypeMaterial(Document):
    """ Documentation for a generic material item that may be used for design, work and other purposes. Any number of MaterialItems manufactured by various vendors may be used to perform this TypeMaterial. Note that class analagous to 'AssetModel' is not used for material items. This is because in some cases, for example, a utility sets up a Master material record for a 3 inch long half inch diameter steel bolt and they do not necessarily care what specific supplier is providing the material item. As different vendors are used to supply the part, the Stock Code of the material item can stay the same. In other cases, each time the vendor changes, a new stock code is set up so they can track material used by vendor. Therefore a Material Item 'Model' is not typically needed.
    """

    # The category of cost to which this Material Item belongs.
    cost_type = db.StringProperty()
    # The value, unit of measure, and multiplier for the quantity.
    quantity = db.StringProperty()
    # The estimated unit cost of this type of material, either for a unit cost or cost per unit length. Cost is for material or asset only and does not include labor to install/construct or configure it.
    est_unit_cost = Money
    # True if item is a stock item (default).
    stock_item = db.BooleanProperty()
    # The 'erp_issue_inventories' property has been implicitly created by
    # the type_material' property of ErpIssueInventory.
    pass
    # The 'erp_req_line_items' property has been implicitly created by
    # the type_material' property of ErpReqLineItem.
    pass
    # The 'material_items' property has been implicitly created by
    # the type_material' property of MaterialItem.
    pass
    # The 'cumaterial_items' property has been implicitly created by
    # the type_material' property of CUMaterialItem.
    pass

class CULaborCode(IdentifiedObject):
    """ Labor code associated with various compatible unit labor items.
    """

    # Labor code.
    code = db.StringProperty()
    status = db.ReferenceProperty()
    # The 'culabor_items' property has been implicitly created by
    # the culabor_code' property of CULaborItem.
    pass

class EquipmentItem(IdentifiedObject):
    """ An equipment item, such as a vehicle, used for a work order.
    """

    # The cost for vehicle usage.
    cost = Money
    # Code for type of vehicle.
    code = db.StringProperty()
    status = db.ReferenceProperty()
#    work_task = db.ReferenceProperty()
#    work_cost_detail = db.ReferenceProperty()

class ShiftPattern(IdentifiedObject):
    """ The patterns of shifts worked by people or crews.
    """

    # Number of cycles for a temporary shift.
    cycle_count = db.IntegerProperty()
    # Type of assignement intended to be worked on this shift, for example, temporary, standard, etc.
    assignment_type = db.StringProperty()
    # Date and time interval for which this shift pattern is valid (when it became effective and when it expires).
    validity_interval = db.ReferenceProperty()
    status = db.ReferenceProperty()
#    crews = db.ListProperty(db.Key)

#    @property
#    def shift_patterns(self):
#        return Crew.gql("WHERE crews = :1", self.key())

class AccessPermit(Document):
    """ A permit is sometimes needed to provide legal access to land or equipment. For example, local authority permission for road works.
    """

    # Permit identifier.
    permit_id = db.StringProperty()
    # Permit expiration date.
    expiration_date = AbsoluteDate
    # Total cost of permit.
    payment = db.FloatProperty()
    # Date that permit became official.
    date_effective = AbsoluteDate
    # Permit application number that is used by municipality, state, province, etc.
    application_number = db.StringProperty()

class Appointment(ScheduledEvent):
    """ Meeting time and location.
    """

    # Information about the appointment.
    remark = db.StringProperty()
    # True if requested to call customer when someone is about to arrive at their premises.
    call_ahead = db.BooleanProperty()
    # Date and time reserved for appointment.
    meeting_interval = db.ReferenceProperty()
    # Address for appointment.
    address = db.ReferenceProperty()
#    call_back = db.ReferenceProperty()
#    erp_persons = db.ListProperty(db.Key)

#    @property
#    def appointments(self):
#        return ErpPerson.gql("WHERE erp_persons = :1", self.key())

class Project(Document):
    """ A collection of related work. For construction projects and maintenance projects, multiple phases may be performed.
    """

    # Overall project budget.
    budget = Money
    # The 'works' property has been implicitly created by
    # the project' property of Work.
    pass
#    business_case = db.ReferenceProperty()
#    erp_project_accounting = db.ReferenceProperty()
#    parent_project = db.ReferenceProperty()
    # The 'sub_projects' property has been implicitly created by
    # the parent_project' property of Project.
    pass
#    requests = db.ListProperty(db.Key)

#    @property
#    def projects(self):
#        return Request.gql("WHERE requests = :1", self.key())

class DesignLocationCU(IdentifiedObject):
    """ Compatible unit at a given design location.
    """

    # A code that helps direct accounting (capital, expense, or accounting treatment).
    cu_account = db.StringProperty()
    # The quantity of the CU being assigned to this location.
    cu_quantity = IntegerQuantity
    # As the same CU can be used for different purposes and accounting purposes, usage must be specified. Examples include: distribution, transmission, substation.
    cu_usage = db.StringProperty()
    # True if associated electrical equipment is intended to be energized while work is being performed.
    energization_flag = db.BooleanProperty()
    # Year when a CU that represents an asset is removed.
    year_removal = db.DateProperty()
    # A code that instructs the crew what action to perform.
    cu_action = WorkActionKind
    status = db.ReferenceProperty()
#    compatible_units = db.ListProperty(db.Key)

#    @property
#    def design_location_cus(self):
#        return CompatibleUnit.gql("WHERE compatible_units = :1", self.key())
#    design_location = db.ReferenceProperty()
#    cugroups = db.ListProperty(db.Key)

#    @property
#    def design_location_cus(self):
#        return CUGroup.gql("WHERE cugroups = :1", self.key())
#    work_tasks = db.ListProperty(db.Key)

#    @property
#    def design_location_cus(self):
#        return WorkTask.gql("WHERE work_tasks = :1", self.key())
#    condition_factors = db.ListProperty(db.Key)

#    @property
#    def design_location_cus(self):
#        return ConditionFactor.gql("WHERE condition_factors = :1", self.key())
#    designs = db.ListProperty(db.Key)

#    @property
#    def design_locations_cus(self):
#        return Design.gql("WHERE designs = :1", self.key())

class Assignment(Document):
    """ An assignment is given to an ErpPerson, Crew, Organisation, Equipment Item, Tool, etc. and may be used to perform Work, WorkTasks, Procedures, etc. TimeSchedules may be set up directly for Assignments or indirectly via the associated WorkTask. Note that these associations are all inherited through the recursive relationship on Document.
    """

    # Date and time assignment became effective.
    effective_date = db.DateProperty()
    # Date and time assignment expires.
    expiration_date = db.DateProperty()
#    crews = db.ListProperty(db.Key)

#    @property
#    def assignments(self):
#        return Crew.gql("WHERE crews = :1", self.key())

class CUMaterialItem(IdentifiedObject):
    """ Compatible unit of a consumable supply item. For example, nuts, bolts, brackets, glue, etc.
    """

    # Code for material.
    corporate_code = db.StringProperty()
    # Quantity of the TypeMaterial for this CU, used to determine estimated costs based on a per unit cost or a cost per unit length specified in the TypeMaterial.
    quantity = IntegerQuantity
    status = db.ReferenceProperty()
#    type_material = db.ReferenceProperty()
#    compatible_units = db.ListProperty(db.Key)

#    @property
#    def cumaterial_items(self):
#        return CompatibleUnit.gql("WHERE compatible_units = :1", self.key())
#    property_units = db.ListProperty(db.Key)

#    @property
#    def cumaterial_items(self):
#        return PropertyUnit.gql("WHERE property_units = :1", self.key())

class WorkLocation(Location):
    """ Information about a particular location for various forms of work such as a one call request.
    """

    # The names of streets at the nearest intersection to work area.
    nearest_intersection = db.StringProperty()
    # Name, identifier, or description of the subdivision, if applicable, in which work is to occur.
    subdivision = db.StringProperty()
    # Name, identifier, or description of the block, if applicable, in which work is to occur.
    block = db.StringProperty()
    # Name, identifier, or description of the lot, if applicable, in which work is to occur.
    lot = db.StringProperty()
#    one_call_request = db.ReferenceProperty()
#    design_locations = db.ListProperty(db.Key)

#    @property
#    def work_locations(self):
#        return DesignLocation.gql("WHERE design_locations = :1", self.key())

class PropertyUnit(IdentifiedObject):
    """ Unit of property for reporting purposes.
    """

    # Activity code identifies a specific and distinguishable work action.
    activity_code = WorkActionKind
    # Used for property record accounting. For example, in the USA, this would be a FERC account.
    property_account = db.StringProperty()
    # A code that identifies appropriate type of property accounts such as distribution, streetlgihts, communications.
    accounting_usage = db.StringProperty()
    status = db.ReferenceProperty()
#    work_cost_details = db.ListProperty(db.Key)

#    @property
#    def property_units(self):
#        return WorkCostDetail.gql("WHERE work_cost_details = :1", self.key())
#    cumaterial_items = db.ListProperty(db.Key)

#    @property
#    def property_units(self):
#        return CUMaterialItem.gql("WHERE cumaterial_items = :1", self.key())
    # The 'compatible_units' property has been implicitly created by
    # the property_unit' property of CompatibleUnit.
    pass

class CUContractorItem(IdentifiedObject):
    """ Compatible unit contractor item.
    """

    # Activity code identifies a specific and distinguishable unit of work.
    activity_code = db.StringProperty()
    # The amount that a given contractor will charge for performing this unit of work.
    bid_amount = Money
    status = db.ReferenceProperty()
#    compatible_units = db.ListProperty(db.Key)

#    @property
#    def cucontractor_items(self):
#        return CompatibleUnit.gql("WHERE compatible_units = :1", self.key())

class MaintenanceDataSet(ProcedureDataSet):
    """ The result of a maintenance activity, a type of Procedure, for a given attribute of an asset is documentated in an MaintenanceDataSet.
    """

    # Description of the condition of the asset just prior to maintenance being performed.
    condition_before = db.StringProperty()
    # Code for the type of maintenance performed.
    maint_code = db.StringProperty()
    # Date and time maintenance procedure was completed.
    maint_date = db.DateProperty()
    # Condition of asset just following maintenance procedure.
    condition_after = db.StringProperty()

class WorkFlowStep(IdentifiedObject):
    """ A pre-defined set of work steps for a given type of work.
    """

    # Used to define dependencies of each work flow step, which is for the instance of WorkTask associated with a given instance of WorkFlow.
    sequence_number = db.IntegerProperty()
    status = db.ReferenceProperty()
    # The 'work_tasks' property has been implicitly created by
    # the work_flow_step' property of WorkTask.
    pass
#    work = db.ReferenceProperty()

class Capability(IdentifiedObject):
    """ Capabilities of a crew.
    """

    # Capability performance factor.
    performance_factor = db.StringProperty()
    # Category by utility's work management standards and practices.
    category = db.StringProperty()
    # Date and time interval for which this capability is valid (when it became effective and when it expires).
    validity_interval = db.ReferenceProperty()
    status = db.ReferenceProperty()
#    crew = db.ReferenceProperty()
#    crafts = db.ListProperty(db.Key)

#    @property
#    def capabilities(self):
#        return Craft.gql("WHERE crafts = :1", self.key())
#    work_tasks = db.ListProperty(db.Key)

#    @property
#    def capabilities(self):
#        return WorkTask.gql("WHERE work_tasks = :1", self.key())

class InspectionDataSet(ProcedureDataSet):
    """ Documents the result of one inspection, a type of Procedure, for a given attribute of an asset.
    """

    # Date and time this inspections was completed.
    inspect_date = db.DateProperty()
    # A general description of the conditions of the location where the asset resides.
    location_condition = db.StringProperty()
    # The 'according_to_schedules' property has been implicitly created by
    # the for_inspection_data_set' property of ScheduleParameterInfo.
    pass

class CULaborItem(IdentifiedObject):
    """ Compatible unit labor item.
    """

    # Estimated time to perform work.
    labor_duration = Hours
    # Activity code identifies a specific and distinguishable unit of work.
    activity_code = db.StringProperty()
    # The labor rate applied for work.
    labor_rate = CostRate
    status = db.ReferenceProperty()
#    qualification_requirements = db.ListProperty(db.Key)

#    @property
#    def culabor_items(self):
#        return QualificationRequirement.gql("WHERE qualification_requirements = :1", self.key())
#    compatible_units = db.ListProperty(db.Key)

#    @property
#    def culabor_items(self):
#        return CompatibleUnit.gql("WHERE compatible_units = :1", self.key())
#    culabor_code = db.ReferenceProperty()

class CompatibleUnit(Document):
    """ A pre-planned job model containing labor, material, and accounting requirements for standardized job planning.
    """

    # The quantity, unit of measure, and multiplier at the CU level that applies to the materials.
    quantity = db.StringProperty()
    # Estimated total cost for perfoming CU.
    est_cost = Money
#    cuwork_equipment_items = db.ListProperty(db.Key)

#    @property
#    def compatible_units(self):
#        return CUWorkEquipmentItem.gql("WHERE cuwork_equipment_items = :1", self.key())
#    procedures = db.ListProperty(db.Key)

#    @property
#    def compatible_units(self):
#        return Procedure.gql("WHERE procedures = :1", self.key())
#    cugroup = db.ReferenceProperty()
#    cuassets = db.ListProperty(db.Key)

#    @property
#    def compatible_units(self):
#        return CUAsset.gql("WHERE cuassets = :1", self.key())
#    cost_type = db.ReferenceProperty()
#    cucontractor_items = db.ListProperty(db.Key)

#    @property
#    def compatible_units(self):
#        return CUContractorItem.gql("WHERE cucontractor_items = :1", self.key())
#    culabor_items = db.ListProperty(db.Key)

#    @property
#    def compatible_units(self):
#        return CULaborItem.gql("WHERE culabor_items = :1", self.key())
#    cuallowable_action = db.ReferenceProperty()
#    property_unit = db.ReferenceProperty()
#    design_location_cus = db.ListProperty(db.Key)

#    @property
#    def compatible_units(self):
#        return DesignLocationCU.gql("WHERE design_location_cus = :1", self.key())
#    cumaterial_items = db.ListProperty(db.Key)

#    @property
#    def compatible_units(self):
#        return CUMaterialItem.gql("WHERE cumaterial_items = :1", self.key())

class MaterialItem(IdentifiedObject):
    """ The physical consumable supply used for work and other purposes. It includes items such as nuts, bolts, brackets, glue, etc.
    """

    # The quantity of material used.
    quantity = IntegerQuantity
    # External reference identifier for this actual material item such as a purchase order number, a serial number, etc.
    external_ref_id = db.StringProperty()
    # Description of the cost.
    cost_description = db.StringProperty()
    # The category of cost to which this Material Item belongs.
    cost_type = db.StringProperty()
    # Code for material.
    material_code = db.StringProperty()
    # The account to which this actual material item is charged.
    account = db.StringProperty()
    # The actual cost of this particular material in this particular quantity.
    actual_cost = Money
    status = db.ReferenceProperty()
#    type_material = db.ReferenceProperty()
    # The 'erp_inventory_counts' property has been implicitly created by
    # the material_item' property of ErpInventoryCount.
    pass
    # The 'usages' property has been implicitly created by
    # the material_item' property of Usage.
    pass
#    design_location = db.ReferenceProperty()
#    work_cost_detail = db.ReferenceProperty()
#    erp_rec_delv_line_items = db.ListProperty(db.Key)

#    @property
#    def material_items(self):
#        return ErpRecDelvLineItem.gql("WHERE erp_rec_delv_line_items = :1", self.key())
    # The 'erp_poline_items' property has been implicitly created by
    # the material_item' property of ErpPOLineItem.
    pass
#    work_task = db.ReferenceProperty()

class OneCallRequest(Document):
    """ A request for other utilities to mark their underground facilities prior to commencement of construction and/or maintenance.
    """

    # True if explosives have been or are planned to be used.
    explosives_used = db.BooleanProperty()
    # True if work location has been marked, for example for a dig area.
    marked_indicator = db.BooleanProperty()
    # Instructions for marking a dig area, if applicable.
    marking_instruction = db.StringProperty()
    # The 'work_locations' property has been implicitly created by
    # the one_call_request' property of WorkLocation.
    pass

class WorkCostSummary(Document):
    """ A roll up by cost category for the entire cost of a work order. For example, total labor.
    """

#    work_cost_detail = db.ReferenceProperty()

class WorkStatusEntry(ActivityRecord):
    """ A type of ActivityRecord that records information about the status of an item, such as a Work or WorkTask, at a point in time.
    """

    # Estimated percentage of completion of this individual work task or overall work order.
    percent_complete = PerCent

class MiscCostItem(IdentifiedObject):
    """ Various cost items that are not associated with compatible units. Examples include rental equipment, labor, materials, contractor costs, permits - anything not covered in a CU.
    """

    # This drives the accounting treatment for this misc. item.
    account = db.StringProperty()
    # External Reference ID (e.g. PO#, Serial #)
    external_ref_id = db.StringProperty()
    # The cost per unit for this misc. item.
    cost_per_unit = Money
    # The cost category for accounting, such as material, labor, vehicle, contractor, equipment, overhead.
    cost_type = db.StringProperty()
    # The quantity of the misc. item being assigned to this location.
    quantity = IntegerQuantity
    status = db.ReferenceProperty()
#    work_task = db.ReferenceProperty()
#    design_location = db.ReferenceProperty()
#    work_cost_detail = db.ReferenceProperty()

class Crew(IdentifiedObject):
    """ A crew is a group of people (ErpPersons) with specific skills, tools, and vehicles.
    """

    # Category by utility's work management standards and practices.
    category = db.StringProperty()
#    work_tasks = db.ListProperty(db.Key)

#    @property
#    def crews(self):
#        return WorkTask.gql("WHERE work_tasks = :1", self.key())
    # The 'vehicles' property has been implicitly created by
    # the crew' property of Vehicle.
    pass
    # The 'capabilities' property has been implicitly created by
    # the crew' property of Capability.
    pass
#    route = db.ReferenceProperty()
    # The 'work_equipment_assets' property has been implicitly created by
    # the crew' property of WorkEquipmentAsset.
    pass
#    shift_patterns = db.ListProperty(db.Key)

#    @property
#    def crews(self):
#        return ShiftPattern.gql("WHERE shift_patterns = :1", self.key())
#    switching_schedules = db.ListProperty(db.Key)

#    @property
#    def crews(self):
#        return SwitchingSchedule.gql("WHERE switching_schedules = :1", self.key())
    # The 'tools' property has been implicitly created by
    # the crew' property of Tool.
    pass
#    outage_steps = db.ListProperty(db.Key)

#    @property
#    def crews(self):
#        return OutageStep.gql("WHERE outage_steps = :1", self.key())
#    locations = db.ListProperty(db.Key)

#    @property
#    def crews(self):
#        return Location.gql("WHERE locations = :1", self.key())
#    crew_members = db.ListProperty(db.Key)

#    @property
#    def crews(self):
#        return ErpPerson.gql("WHERE crew_members = :1", self.key())
#    organisations = db.ListProperty(db.Key)

#    @property
#    def crews(self):
#        return ErpOrganisation.gql("WHERE organisations = :1", self.key())
#    assignments = db.ListProperty(db.Key)

#    @property
#    def crews(self):
#        return Assignment.gql("WHERE assignments = :1", self.key())

class WorkCostDetail(Document):
    """ A collection of all of the individual cost items collected from multiple sources.
    """

    # True if 'amount' attribute is a debit, false if it is a credit.
    debit_flag = db.BooleanProperty()
    # The type of cost.
    type_work_cost = db.StringProperty()
    # Amount in designated currency for work, either a total or an individual element. As defined in the attribute 'type,' multiple instances are applicable to each work for: planned cost, actual cost, authorized cost, budgeted cost, forecasted cost, other.
    amount = Money
    # Date that amount is posted to the work.
    transaction_date = db.DateProperty()
#    erp_project_accounting = db.ReferenceProperty()
#    design = db.ReferenceProperty()
    # The 'material_items' property has been implicitly created by
    # the work_cost_detail' property of MaterialItem.
    pass
#    work_cost_summary = db.ReferenceProperty()
#    overhead_cost = db.ReferenceProperty()
    # The 'labor_items' property has been implicitly created by
    # the work_cost_detail' property of LaborItem.
    pass
#    works = db.ListProperty(db.Key)

#    @property
#    def work_cost_details(self):
#        return Work.gql("WHERE works = :1", self.key())
    # The 'misc_cost_items' property has been implicitly created by
    # the work_cost_detail' property of MiscCostItem.
    pass
    # The 'equipment_items' property has been implicitly created by
    # the work_cost_detail' property of EquipmentItem.
    pass
#    cost_type = db.ReferenceProperty()
    # The 'contractor_items' property has been implicitly created by
    # the work_cost_detail' property of ContractorItem.
    pass
#    work_task = db.ReferenceProperty()
#    property_units = db.ListProperty(db.Key)

#    @property
#    def work_cost_details(self):
#        return PropertyUnit.gql("WHERE property_units = :1", self.key())

class CUAllowableAction(IdentifiedObject):
    """ Allowed actions: Install, Remove, Transfer, Abandon, etc.
    """

    status = db.ReferenceProperty()
    # The 'compatible_units' property has been implicitly created by
    # the cuallowable_action' property of CompatibleUnit.
    pass

class BusinessCase(Document):
    """ Business justification for capital expenditures, usually addressing operations and maintenance costs as well.
    """

    # A codified representation of the business case (i.e., codes for highway relocation, replace substation transformers, etc.).
    corporate_code = db.StringProperty()
    # The 'projects' property has been implicitly created by
    # the business_case' property of Project.
    pass
    # The 'works' property has been implicitly created by
    # the business_case' property of Work.
    pass

class LaborItem(IdentifiedObject):
    """ Labor used for work order.
    """

    # Activity code identifies a specific and distinguishable unit of work.
    activity_code = db.StringProperty()
    # Time required to perform work.
    labor_duration = Hours
    # The labor rate applied for work.
    labor_rate = CostRate
    # Total cost for labor. Note that this may not be able to be derived from labor rate and time charged.
    cost = Money
    status = db.ReferenceProperty()
#    erp_persons = db.ListProperty(db.Key)

#    @property
#    def labor_items(self):
#        return ErpPerson.gql("WHERE erp_persons = :1", self.key())
#    work_cost_detail = db.ReferenceProperty()
#    work_task = db.ReferenceProperty()

class Design(Document):
    """ A design for consideration by customers, potential customers, or internal work. Note that the Version of design is the revision attribute that is inherited from Document.
    """

    # Estimated cost (not price) of design.
    cost_estimate = Money
    # Kind of this design.
    kind = DesignKind
    # Price to customer for implementing design.
    price = Money
    # The 'erp_boms' property has been implicitly created by
    # the design' property of ErpBOM.
    pass
#    erp_quote_line_item = db.ReferenceProperty()
#    design_locations = db.ListProperty(db.Key)

#    @property
#    def designs(self):
#        return DesignLocation.gql("WHERE design_locations = :1", self.key())
#    work = db.ReferenceProperty()
#    condition_factors = db.ListProperty(db.Key)

#    @property
#    def designs(self):
#        return ConditionFactor.gql("WHERE condition_factors = :1", self.key())
    # The 'work_cost_details' property has been implicitly created by
    # the design' property of WorkCostDetail.
    pass
    # The 'work_tasks' property has been implicitly created by
    # the design' property of WorkTask.
    pass
#    design_locations_cus = db.ListProperty(db.Key)

#    @property
#    def designs(self):
#        return DesignLocationCU.gql("WHERE design_locations_cus = :1", self.key())

class WorkTask(Document):
    """ A set of tasks is required to implement a design.
    """

    # If specified, override schedule and perform this task in accordance with instructions specified here.
    sched_override = db.StringProperty()
    # The priority of this work task.
    priority = db.StringProperty()
#    qualification_requirements = db.ListProperty(db.Key)

#    @property
#    def work_tasks(self):
#        return QualificationRequirement.gql("WHERE qualification_requirements = :1", self.key())
#    design = db.ReferenceProperty()
#    design_location_cus = db.ListProperty(db.Key)

#    @property
#    def work_tasks(self):
#        return DesignLocationCU.gql("WHERE design_location_cus = :1", self.key())
    # The 'misc_cost_items' property has been implicitly created by
    # the work_task' property of MiscCostItem.
    pass
    # The 'switching_schedules' property has been implicitly created by
    # the work_task' property of SwitchingSchedule.
    pass
#    capabilities = db.ListProperty(db.Key)

#    @property
#    def work_tasks(self):
#        return Capability.gql("WHERE capabilities = :1", self.key())
    # The 'usages' property has been implicitly created by
    # the work_task' property of Usage.
    pass
#    overhead_cost = db.ReferenceProperty()
#    work_flow_step = db.ReferenceProperty()
    # The 'material_items' property has been implicitly created by
    # the work_task' property of MaterialItem.
    pass
    # The 'labor_items' property has been implicitly created by
    # the work_task' property of LaborItem.
    pass
#    crews = db.ListProperty(db.Key)

#    @property
#    def work_tasks(self):
#        return Crew.gql("WHERE crews = :1", self.key())
#    work = db.ReferenceProperty()
    # The 'contractor_items' property has been implicitly created by
    # the work_task' property of ContractorItem.
    pass
    # The 'equipment_items' property has been implicitly created by
    # the work_task' property of EquipmentItem.
    pass
    # The 'work_cost_details' property has been implicitly created by
    # the work_task' property of WorkCostDetail.
    pass
    # The 'assets' property has been implicitly created by
    # the work_task' property of Asset.
    pass

class NonStandardItem(Document):
    """ This document provides information for non-standard items like customer contributions (e.g., customer digs trench), vouchers (e.g., credit), and contractor bids.
    """

    # The category of non-standard work.
    code = db.StringProperty()
    # The projected cost for this item.
    amount = Money

class ConditionFactor(IdentifiedObject):
    """ This is to specify the various condition factors for a design that may alter the cost estimate or the allocation.
    """

    # Kind of this condition factor.
    kind = ConditionFactorKind
    # The actual value of the condition factor, such as labor flat fee or percentage.
    cf_value = db.StringProperty()
    status = db.ReferenceProperty()
#    designs = db.ListProperty(db.Key)

#    @property
#    def condition_factors(self):
#        return Design.gql("WHERE designs = :1", self.key())
#    design_location_cus = db.ListProperty(db.Key)

#    @property
#    def condition_factors(self):
#        return DesignLocationCU.gql("WHERE design_location_cus = :1", self.key())
#    design_locations = db.ListProperty(db.Key)

#    @property
#    def condition_factors(self):
#        return DesignLocation.gql("WHERE design_locations = :1", self.key())

class CUGroup(IdentifiedObject):
    """ A Compatible Unit Group identifies a set of compatible units which may be jointly utilized for estimating and designating jobs.
    """

    status = db.ReferenceProperty()
    # The 'compatible_units' property has been implicitly created by
    # the cugroup' property of CompatibleUnit.
    pass
#    design_location_cus = db.ListProperty(db.Key)

#    @property
#    def cugroups(self):
#        return DesignLocationCU.gql("WHERE design_location_cus = :1", self.key())
#    child_cugroups = db.ListProperty(db.Key)

#    @property
#    def parent_cugroups(self):
#        return CUGroup.gql("WHERE child_cugroups = :1", self.key())
#    parent_cugroups = db.ListProperty(db.Key)

#    @property
#    def child_cugroups(self):
#        return CUGroup.gql("WHERE parent_cugroups = :1", self.key())

class ContractorItem(IdentifiedObject):
    """ Contractor information for work task.
    """

    # The amount that a given contractor will charge for performing this unit of work.
    bid_amount = Money
    # The total amount charged.
    cost = Money
    # Activity code identifies a specific and distinguishable unit of work.
    activity_code = db.StringProperty()
    status = db.ReferenceProperty()
#    erp_payables = db.ListProperty(db.Key)

#    @property
#    def contractor_items(self):
#        return ErpPayable.gql("WHERE erp_payables = :1", self.key())
#    work_cost_detail = db.ReferenceProperty()
#    work_task = db.ReferenceProperty()

class CUAsset(IdentifiedObject):
    """ Compatible unit for various types of assets such as transformers switches, substation fences, poles, etc..
    """

    # Quantity of the type asset within the CU.
    quantity = IntegerQuantity
    # The code for this type of asset.
    type_asset_code = db.StringProperty()
    status = db.ReferenceProperty()
#    type_asset = db.ReferenceProperty()
#    compatible_units = db.ListProperty(db.Key)

#    @property
#    def cuassets(self):
#        return CompatibleUnit.gql("WHERE compatible_units = :1", self.key())

class DesignLocation(IdentifiedObject):
    """ A logical part of the design (e.g., pole and all equipment on a pole). This includes points and spans.
    """

    # The legth of the span from the previous pole to this pole.
    span_length = Length
    status = db.ReferenceProperty()
#    diagrams = db.ListProperty(db.Key)

#    @property
#    def design_locations(self):
#        return Diagram.gql("WHERE diagrams = :1", self.key())
    # The 'erp_bom_item_datas' property has been implicitly created by
    # the design_location' property of ErpBomItemData.
    pass
    # The 'misc_cost_items' property has been implicitly created by
    # the design_location' property of MiscCostItem.
    pass
    # The 'design_location_cus' property has been implicitly created by
    # the design_location' property of DesignLocationCU.
    pass
    # The 'material_items' property has been implicitly created by
    # the design_location' property of MaterialItem.
    pass
#    condition_factors = db.ListProperty(db.Key)

#    @property
#    def design_locations(self):
#        return ConditionFactor.gql("WHERE condition_factors = :1", self.key())
#    work_locations = db.ListProperty(db.Key)

#    @property
#    def design_locations(self):
#        return WorkLocation.gql("WHERE work_locations = :1", self.key())
#    designs = db.ListProperty(db.Key)

#    @property
#    def design_locations(self):
#        return Design.gql("WHERE designs = :1", self.key())

class OverheadCost(IdentifiedObject):
    """ Overhead cost applied to work order.
    """

    # The overhead cost to be applied.
    cost = Money
    # Overhead code.
    code = db.StringProperty()
    status = db.ReferenceProperty()
    # The 'work_tasks' property has been implicitly created by
    # the overhead_cost' property of WorkTask.
    pass
    # The 'work_cost_details' property has been implicitly created by
    # the overhead_cost' property of WorkCostDetail.
    pass

class Regulation(Document):
    """ Special requirements and/or regulations may pertain to certain types of assets or work. For example, fire protection and scaffolding.
    """

    # External reference to regulation, if applicable.
    reference_number = db.StringProperty()

class InfoQuestion(Document):
    """ Questions and answers associated with a type of document for purposes of clarification. Questions may be predefined or ad hoc.
    """

    # Answer to question.
    answer = db.StringProperty()
    # Remarks to qualify the question in this situation.
    question_remark = db.StringProperty()
    # The question code. If blank, refer to questionText.
    question_code = db.StringProperty()
    # The category of the question.
    question_category = db.StringProperty()
    # The date and time the quesiton was answered.
    answer_date_time = db.DateProperty()
    # Remarks to qualify the answer.
    answer_remark = db.StringProperty()
    # For non-coded questions, the question is provided here.
    question_text = db.StringProperty()

class CUWorkEquipmentItem(IdentifiedObject):
    """ Compatible unit for various types of WorkEquipmentAssets, including vehicles.
    """

    # The equipment type code.
    equip_code = db.StringProperty()
    # Standard usage rate for the type of vehicle.
    rate = CostRate
    status = db.ReferenceProperty()
#    compatible_units = db.ListProperty(db.Key)

#    @property
#    def cuwork_equipment_items(self):
#        return CompatibleUnit.gql("WHERE compatible_units = :1", self.key())
#    type_asset = db.ReferenceProperty()


