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

from cim14.iec61970.domain import Voltage
from cim14.iec61970.domain import UnitSymbol
from cim14.iec61970.domain import UnitMultiplier
from cim14.iec61970.domain import PerCent
from cim14.iec61970.domain import Seconds
from cim14.iec61970.domain import ApparentPower

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

CompanyType = db.StringProperty(choices=("pool", "municipal", "is_private"))

BreakerConfiguration = db.StringProperty(choices=("single_breaker", "no_breaker", "breaker_and_ahalf", "double_breaker"))

PhaseCode = db.StringProperty(choices=("abn", "bc", "acn", "bn", "ac", "abc", "an", "ab", "c", "b", "abcn", "a", "cn", "n", "bcn"))

CurveStyle = db.StringProperty(choices=("straight_line_yvalues", "constant_yvalue", "formula", "ramp_yvalue"))

BusbarConfiguration = db.StringProperty(choices=("double_bus", "main_with_transfer", "single_bus", "ring_bus"))

ns_prefix = "cim.IEC61970.Core"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#IEC61970.Core"

class RegularTimePoint(Element):
    """ TimePoints for a schedule where the time between the points is constant.
    """

    # The first value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule.
    value1 = db.FloatProperty()
    # The position of the RegularTimePoint in the sequence. Note that time points don't have to be sequential, i.e. time points may be omitted. The actual time for a RegularTimePoint is computed by multiplying the RegularIntervalSchedule.timeStep with the RegularTimePoint.sequenceNumber and add the BasicIntervalSchedule.startTime.
    sequence_number = db.IntegerProperty()
    # The second value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule.
    value2 = db.FloatProperty()
#    interval_schedule = db.ReferenceProperty()

class OperatingShare(Element):
    """ Specifies the contract relationship between a PowerSystemResource and a contract participant.
    """

    # Percentage ownership for this device.   The percentage indicates the percentage ownership of the PSROwner for the PowerSystemResource.  The total percentage ownership for a PowerSystemResource should add to 100%.
    percentage = PerCent
#    power_system_resource = db.ReferenceProperty()
#    operating_participant = db.ReferenceProperty()

class IdentifiedObject(Element):
    """ This is a root class to provide common naming attributes for all classes needing naming attributes
    """

    # A Model Authority issues mRIDs. Given that each Model Authority has a unique id and this id is part of the mRID, then the mRID is globally unique.
    m_rid = db.StringProperty()
    # The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy.
    name = db.StringProperty()
    # The pathname is a system unique name composed from all IdentifiedObject.localNames in a naming hierarchy path from the object to the root.
    path_name = db.StringProperty()
    # The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy.
    description = db.StringProperty()
    # The localName is a human readable name of the object. It is only used with objects organized in a naming hierarchy. The simplest naming hierarchy has just one parent (the root) giving a flat naming hierarchy. However, the naming hierarchy usually has several levels, e.g. Substation, VoltageLevel, Equipment etc. Children of the same parent have names that are unique among them. If the uniqueness requirement cannot be met IdentifiedObject.localName shall not be used, use IdentifiedObject.name  instead.
    local_name = db.StringProperty()
    # The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy.
    alias_name = db.StringProperty()
#    modeling_authority_set = db.ReferenceProperty()

class IrregularTimePoint(Element):
    """ TimePoints for a schedule where the time between the points varies.
    """

    # The second value at the time. The meaning of the value is defined by the class inhering the IrregularIntervalSchedule.
    value2 = db.FloatProperty()
    # The time is relative the BasicTimeSchedule.startTime.
    time = Seconds
    # The first value at the time. The meaning of the value is defined by the class inhering the IrregularIntervalSchedule.
    value1 = db.FloatProperty()
#    interval_schedule = db.ReferenceProperty()

class CurveData(Element):
    """ Data point values for defining a curve or schedule
    """

    # The data value of the second Y-axis variable (if present), depending on the Y-axis units
    y2value = db.FloatProperty()
    # The data value of the X-axis variable,  depending on the X-axis units
    xvalue = db.FloatProperty()
    # The data value of the  first Y-axis variable, depending on the Y-axis units
    y1value = db.FloatProperty()
#    curve = db.ReferenceProperty()

class PowerSystemResource(IdentifiedObject):
    """ A power system resource can be an item of equipment such as a Switch, an EquipmentContainer containing many individual items of equipment such as a  Substation, or an organisational entity such as Company or SubControlArea.  This provides for the nesting of collections of PowerSystemResources within other PowerSystemResources. For example, a Switch could be a member of a Substation and a Substation could be a member of a division of a Company.
    """

#    activity_records = db.ListProperty(db.Key)

#    @property
#    def power_system_resources(self):
#        return ActivityRecord.gql("WHERE activity_records = :1", self.key())
#    outage_schedule = db.ReferenceProperty()
#    schedule_steps = db.ListProperty(db.Key)

#    @property
#    def power_system_resources(self):
#        return SwitchingStep.gql("WHERE schedule_steps = :1", self.key())
#    reporting_group = db.ListProperty(db.Key)

#    @property
#    def power_system_resource(self):
#        return ReportingGroup.gql("WHERE reporting_group = :1", self.key())
#    circuit_sections = db.ListProperty(db.Key)

#    @property
#    def power_system_resources(self):
#        return CircuitSection.gql("WHERE circuit_sections = :1", self.key())
    # The 'measurements' property has been implicitly created by
    # the power_system_resource' property of Measurement.
    pass
#    network_data_sets = db.ListProperty(db.Key)

#    @property
#    def power_system_resources(self):
#        return NetworkDataSet.gql("WHERE network_data_sets = :1", self.key())
    # The 'operating_share' property has been implicitly created by
    # the power_system_resource' property of OperatingShare.
    pass
#    psr_lists = db.ListProperty(db.Key)

#    @property
#    def power_system_resources(self):
#        return PsrList.gql("WHERE psr_lists = :1", self.key())
    # The 'safety_documents' property has been implicitly created by
    # the power_system_resource' property of SafetyDocument.
    pass
#    circuits = db.ListProperty(db.Key)

#    @property
#    def power_system_resources(self):
#        return Circuit.gql("WHERE circuits = :1", self.key())
#    psrtype = db.ReferenceProperty()
#    psrstatus = db.ReferenceProperty()
    # The 'asset_roles' property has been implicitly created by
    # the power_system_resource' property of AssetPsrRole.
    pass
    # The 'document_roles' property has been implicitly created by
    # the power_system_resource' property of DocPsrRole.
    pass
    # The 'erp_organisation_roles' property has been implicitly created by
    # the power_system_resource' property of OrgPsrRole.
    pass
    # The 'change_items' property has been implicitly created by
    # the power_system_resource' property of ChangeItem.
    pass
    # The 'location_roles' property has been implicitly created by
    # the power_system_resource' property of PsrLocRole.
    pass

class PsrList(IdentifiedObject):
    """ Arbitrary list of PowerSystemResources. Can be used for various purposes, including grouping for report generation.
    """

    # Type of power system resources in this list.
    type_psrlist = db.StringProperty()
#    power_system_resources = db.ListProperty(db.Key)

#    @property
#    def psr_lists(self):
#        return PowerSystemResource.gql("WHERE power_system_resources = :1", self.key())

class OperatingParticipant(IdentifiedObject):
    """ An operator of multiple PowerSystemResource objects. Note multple OperatingParticipants may operate the same PowerSystemResource object.   This can be used for modeling jointly owned units where each owner operates as a contractual share.
    """

    # The 'operating_share' property has been implicitly created by
    # the operating_participant' property of OperatingShare.
    pass

class ConnectivityNodeContainer(PowerSystemResource):
    """ A base class for all objects that may contain ConnectivityNodes or TopologicalNodes.
    """

    # The 'connectivity_nodes' property has been implicitly created by
    # the connectivity_node_container' property of ConnectivityNode.
    pass
    # The 'topological_node' property has been implicitly created by
    # the connectivity_node_container' property of TopologicalNode.
    pass

class ModelingAuthoritySet(IdentifiedObject):
    """ A Modeling Authority Set is a group of objects in a network model where the data is supplied and maintained by the same Modeling Authority.
    """

    # The 'identified_objects' property has been implicitly created by
    # the modeling_authority_set' property of IdentifiedObject.
    pass
#    modeling_authority = db.ReferenceProperty()

class GeographicalRegion(IdentifiedObject):
    """ A geographical region of a power system network model.
    """

    # The 'regions' property has been implicitly created by
    # the region' property of SubGeographicalRegion.
    pass

class Unit(IdentifiedObject):
    """ Quantity being measured. The Unit.name shall be unique among all specified quantities and describe the quantity. The Unit.aliasName is meant to be used for localization.
    """

    # The 'protection_equipments' property has been implicitly created by
    # the unit' property of ProtectionEquipment.
    pass
    # The 'measurements' property has been implicitly created by
    # the unit' property of Measurement.
    pass
    # The 'controls' property has been implicitly created by
    # the unit' property of Control.
    pass

class BasicIntervalSchedule(IdentifiedObject):
    """ Schedule of values at points in time.
    """

    # Value2 units of measure.
    value2_unit = UnitSymbol
    # Value1 units of measure.
    value1_unit = UnitSymbol
    # Multiplier for value2.
    value2_multiplier = UnitMultiplier
    # Multiplier for value1.
    value1_multiplier = UnitMultiplier
    # The time for the first time point.
    start_time = db.DateProperty()

class PSRType(IdentifiedObject):
    """ Classifying instances of the same class, e.g. overhead and underground ACLineSegments. This classification mechanism is intended to provide flexibility outside the scope of this standard, i.e. provide customisation that is non standard.
    """

    # The 'power_system_resources' property has been implicitly created by
    # the psrtype' property of PowerSystemResource.
    pass

class EquipmentContainer(ConnectivityNodeContainer):
    """ A modeling construct to provide a root class for all Equipment classes
    """

    # The 'equipments' property has been implicitly created by
    # the equipment_container' property of Equipment.
    pass

class Equipment(PowerSystemResource):
    """ The parts of a power system that are physical devices, electronic or mechanical
    """

    # The equipment is normally in service.
    normal_ily_in_service = db.BooleanProperty()
    # Indicates if the equipment is real equipment (false) or an equivalent.
    equivalent = db.BooleanProperty()
    # The 'contingency_equipment' property has been implicitly created by
    # the equipment' property of ContingencyEquipment.
    pass
#    customer_agreements = db.ListProperty(db.Key)

#    @property
#    def equipments(self):
#        return CustomerAgreement.gql("WHERE customer_agreements = :1", self.key())
    # The 'operational_limit_set' property has been implicitly created by
    # the equipment' property of OperationalLimitSet.
    pass
#    equipment_container = db.ReferenceProperty()

class ReportingGroup(IdentifiedObject):
    """ A reporting group is used for various ad-hoc groupings used for reporting.
    """

    # The 'bus_name_marker' property has been implicitly created by
    # the reporting_group' property of BusNameMarker.
    pass
#    reporting_super_group = db.ReferenceProperty()
    # The 'topological_node' property has been implicitly created by
    # the reporting_group' property of TopologicalNode.
    pass
#    power_system_resource = db.ListProperty(db.Key)

#    @property
#    def reporting_group(self):
#        return PowerSystemResource.gql("WHERE power_system_resource = :1", self.key())

class ReportingSuperGroup(IdentifiedObject):
    """ A reporting super group, groups reporting groups for a higher level report.
    """

    # The 'reporting_group' property has been implicitly created by
    # the reporting_super_group' property of ReportingGroup.
    pass

class SubGeographicalRegion(IdentifiedObject):
    """ A subset of a geographical region of a power system network model.
    """

    # The 'substations' property has been implicitly created by
    # the region' property of Substation.
    pass
#    region = db.ReferenceProperty()
    # The 'lines' property has been implicitly created by
    # the region' property of Line.
    pass

class ModelingAuthority(IdentifiedObject):
    """ A Modeling Authority is an entity responsible for supplying and maintaining the data defining a specific set of objects in a network model.
    """

    # The 'modeling_authority_sets' property has been implicitly created by
    # the modeling_authority' property of ModelingAuthoritySet.
    pass

class Curve(IdentifiedObject):
    """ Relationship between an independent variable (X-axis) and one or two dependent  variables (Y1-axis and Y2-axis). Curves can also serve as schedules.
    """

    # Multiplier for Y2-axis.
    y2_multiplier = UnitMultiplier
    # The Y2-axis units of measure.
    y2_unit = UnitSymbol
    # Multiplier for Y1-axis
    y1_multiplier = UnitMultiplier
    # The Y1-axis units of measure.
    y1_unit = UnitSymbol
    # The style or shape of the curve.
    curve_style = CurveStyle
    # Multiplier for X-axis.
    x_multiplier = UnitMultiplier
    # The X-axis units of measure.
    x_unit = UnitSymbol
    # The 'curve_datas' property has been implicitly created by
    # the curve' property of CurveData.
    pass

class BaseVoltage(IdentifiedObject):
    """ Collection of BaseVoltages which is used to verify that the BusbarSection.BaseVoltage and other voltage attributes in the CIM are given a value existing in the collection.
    """

    # If true, this is a direct current base voltage and items assigned to this base voltage are also associated with a direct current capabilities.   False indicates alternating current.
    is_dc = db.BooleanProperty()
    # The PowerSystemResource's base voltage.
    nominal_voltage = Voltage
    # The 'voltage_level' property has been implicitly created by
    # the base_voltage' property of VoltageLevel.
    pass
    # The 'conducting_equipment' property has been implicitly created by
    # the base_voltage' property of ConductingEquipment.
    pass

class Bay(EquipmentContainer):
    """ A collection of power system resources (within a given substation) including conducting equipment, protection relays, measurements, and telemetry.
    """

    # Indicates the presence/absence of active/reactive power measurements.
    bay_power_meas_flag = db.BooleanProperty()
    # Bus bar configuration.
    bus_bar_configuration = BusbarConfiguration
    # Breaker configuration.
    breaker_configuration = BreakerConfiguration
    # Indicates the presence/absence of energy measurements.
    bay_energy_meas_flag = db.BooleanProperty()
#    substation = db.ReferenceProperty()
#    voltage_level = db.ReferenceProperty()

class RegularIntervalSchedule(BasicIntervalSchedule):
    """ The schedule has TimePoints where the time between them is constant.
    """

    # The time for the last time point.
    end_time = db.DateProperty()
    # The time between each pair of subsequent RegularTimePoints.
    time_step = Seconds
    # The 'time_points' property has been implicitly created by
    # the interval_schedule' property of RegularTimePoint.
    pass

class BasePower(IdentifiedObject):
    """ The BasePower class defines the base power used in the per unit calculations.
    """

    # Definition of base power.
    base_power = ApparentPower

class Terminal(IdentifiedObject):
    """ An electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called 'connectivity nodes'.
    """

    # The terminal connection status.   True implies the terminal is connected, and false implies the terminal is not connected. This is the result of topoplogical processing of a detailed Connectivity node and Switch model whether present in the model or not.   A terminal that is not connected cannot support a current flow.   A terminal that is connected may have flow.  In general a multi-terminal device may simultaneously have connected and disconnected terminals.  No other aspect of the algorithm
    connected = db.BooleanProperty()
    # The 'measurements' property has been implicitly created by
    # the terminal' property of Measurement.
    pass
    # The 'terminal_constraints' property has been implicitly created by
    # the terminal' property of TerminalConstraintTerm.
    pass
    # The 'has_second_mutual_coupling' property has been implicitly created by
    # the second_terminal' property of MutualCoupling.
    pass
    # The 'operational_limit_set' property has been implicitly created by
    # the terminal' property of OperationalLimitSet.
    pass
    # The 'tie_flow' property has been implicitly created by
    # the terminal' property of TieFlow.
    pass
#    sv_power_flow = db.ReferenceProperty()
    # The 'regulating_control' property has been implicitly created by
    # the terminal' property of RegulatingControl.
    pass
#    conducting_equipment = db.ReferenceProperty()
#    connectivity_node = db.ReferenceProperty()
    # The 'has_first_mutual_coupling' property has been implicitly created by
    # the first_terminal' property of MutualCoupling.
    pass
#    topological_node = db.ReferenceProperty()
    # The 'branch_group_terminal' property has been implicitly created by
    # the terminal' property of BranchGroupTerminal.
    pass
#    bushing_asset = db.ReferenceProperty()

class Substation(EquipmentContainer):
    """ A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk is passed for the purposes of switching or modifying its characteristics.
    """

#    region = db.ReferenceProperty()
    # The 'voltage_levels' property has been implicitly created by
    # the substation' property of VoltageLevel.
    pass
#    substation_asset = db.ReferenceProperty()
    # The 'bays' property has been implicitly created by
    # the substation' property of Bay.
    pass

class VoltageLevel(EquipmentContainer):
    """ A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these.
    """

    # The bus bar's low voltage limit
    low_voltage_limit = Voltage
    # The bus bar's high voltage limit
    high_voltage_limit = Voltage
    # The 'bays' property has been implicitly created by
    # the voltage_level' property of Bay.
    pass
#    base_voltage = db.ReferenceProperty()
#    substation = db.ReferenceProperty()

class IrregularIntervalSchedule(BasicIntervalSchedule):
    """ The schedule has TimePoints where the time between them varies.
    """

    # The 'time_points' property has been implicitly created by
    # the interval_schedule' property of IrregularTimePoint.
    pass

class ConductingEquipment(Equipment):
    """ The parts of the power system that are designed to carry current or that are conductively connected therewith. ConductingEquipment is contained within an EquipmentContainer that may be a Substation, or a VoltageLevel or a Bay within a Substation.
    """

    # Describes the phases carried by a conducting equipment.
    phases = PhaseCode
    # The 'electrical_assets' property has been implicitly created by
    # the conducting_equipment' property of ElectricalAsset.
    pass
#    protection_equipments = db.ListProperty(db.Key)

#    @property
#    def conducting_equipments(self):
#        return ProtectionEquipment.gql("WHERE protection_equipments = :1", self.key())
    # The 'outage_step_roles' property has been implicitly created by
    # the conducting_equipment' property of OutageStepPsrRole.
    pass
#    sv_status = db.ReferenceProperty()
    # The 'clearance_tags' property has been implicitly created by
    # the conducting_equipment' property of ClearanceTag.
    pass
#    base_voltage = db.ReferenceProperty()
    # The 'terminals' property has been implicitly created by
    # the conducting_equipment' property of Terminal.
    pass


