#------------------------------------------------------------------------------
# Copyright (C) 2009 Richard Lincoln
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the Free
# Software Foundation; version 2 dated June, 1991.
#
# This software is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANDABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#------------------------------------------------------------------------------

""" Contains the core PowerSystemResource and ConductingEquipment entities shared by all applications plus common collections of those entities. Not all applications require all the Core entities.Contains the core PowerSystemResource and ConductingEquipment entities shared by all applications plus common collections of those entities. Not all applications require all the Core entities.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from cpsm import Element

from cpsm.domain import Voltage
from cpsm.domain import Seconds
from cpsm.domain import UnitSymbol

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

#------------------------------------------------------------------------------
#  Properties:
#------------------------------------------------------------------------------

CurveStyle = db.StringProperty(choices=("ramp_yvalue", "formula", "constant_yvalue", "straight_line_yvalues"))

#------------------------------------------------------------------------------
#  Constants:
#------------------------------------------------------------------------------

NS_PREFIX = "cim"
NS_URI = "http://iec.ch/TC57/2008/CIM-schema-cim13#Package_Core"

#------------------------------------------------------------------------------
#  "IdentifiedObject" class:
#------------------------------------------------------------------------------

class IdentifiedObject(Element):
    """ This is a root class to provide common naming attributes for all classes needing naming attributesThis is a root class to provide common naming attributes for all classes needing naming attributes
    """


    # The pathname is a system unique name composed from all IdentifiedObject.localNames in a naming hierarchy path from the object to the root.The pathname is a system unique name composed from all IdentifiedObject.localNames in a naming hierarchy path from the object to the root.
    path_name = db.StringProperty()

    # The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy.The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy.
    description = db.StringProperty()

    # The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy.The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy.
    alias_name = db.StringProperty()

    # The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy.The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy.
    name = db.StringProperty()

    # <<< identified_object
    # @generated
    # >>> identified_object


#------------------------------------------------------------------------------
#  "RegularTimePoint" class:
#------------------------------------------------------------------------------

class RegularTimePoint(Element):
    """ TimePoints for a schedule where the time between the points is constant.TimePoints for a schedule where the time between the points is constant.
    """


    # The first value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule.The first value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule.
    value1 = db.FloatProperty()

    # The position of the RegularTimePoint in the sequence. Note that time points don't have to be sequential, i.e. time points may be omitted. The actual time for a RegularTimePoint is computed by multiplying the RegularIntervalSchedule.timeStep with the RegularTimePoint.sequenceNumber and add the BasicIntervalSchedule.startTime.The position of the RegularTimePoint in the sequence. Note that time points don't have to be sequential, i.e. time points may be omitted. The actual time for a RegularTimePoint is computed by multiplying the RegularIntervalSchedule.timeStep with the RegularTimePoint.sequenceNumber and add the BasicIntervalSchedule.startTime.
    sequence_number = db.IntegerProperty()

    # The second value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule.The second value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule.
    value2 = db.FloatProperty()

    # A RegularTimePoint belongs to a RegularIntervalSchedule.A RegularTimePoint belongs to a RegularIntervalSchedule.
    interval_schedule = db.ReferenceProperty(collection_name="time_points")

    # <<< regular_time_point
    # @generated
    # >>> regular_time_point


#------------------------------------------------------------------------------
#  "CurveData" class:
#------------------------------------------------------------------------------

class CurveData(Element):
    """ Data point values for defining a curve or scheduleData point values for defining a curve or schedule
    """


    # The data value of the second Y-axis variable (if present), depending on the Y-axis unitsThe data value of the second Y-axis variable (if present), depending on the Y-axis units
    y2value = db.FloatProperty()

    # The data value of the X-axis variable,  depending on the X-axis unitsThe data value of the X-axis variable,  depending on the X-axis units
    xvalue = db.FloatProperty()

    # The data value of the  first Y-axis variable, depending on the Y-axis unitsThe data value of the  first Y-axis variable, depending on the Y-axis units
    y1value = db.FloatProperty()

    # The Curve defined by this CurveData.The Curve defined by this CurveData.
    curve_schedule = db.ReferenceProperty(collection_name="curve_schedule_datas")

    # <<< curve_data
    # @generated
    # >>> curve_data


#------------------------------------------------------------------------------
#  "Terminal" class:
#------------------------------------------------------------------------------

class Terminal(IdentifiedObject):
    """ An electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called 'connectivity nodes'.An electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called 'connectivity nodes'.
    """


    # Virtual property. One or more measurements may be associated with a terminal in the network. Measurement-Terminal defines where the measurement is placed in the network topology. Some Measurements represent quantities related to a particular sensor position, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is captured by the Measurement - Terminal association that makes it possible to place the sensing position at a  well defined place. The place is defined by the connection of the Terminal to ConductingEquipment.One or more measurements may be associated with a terminal in the network. Measurement-Terminal defines where the measurement is placed in the network topology. Some Measurements represent quantities related to a particular sensor position, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is captured by the Measurement - Terminal association that makes it possible to place the sensing position at a  well defined place. The place is defined by the connection of the Terminal to ConductingEquipment.
    pass #measurements

    # Virtual property. The terminal is regulated by a control.The terminal is regulated by a control.
    pass #regulating_control

    # Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.
#    connectivity_node = db.ReferenceProperty(collection_name="terminals")

    # ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodesConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes
    conducting_equipment = db.ReferenceProperty(collection_name="terminals")

    # <<< terminal
    # @generated
    # >>> terminal


#------------------------------------------------------------------------------
#  "BaseVoltage" class:
#------------------------------------------------------------------------------

class BaseVoltage(IdentifiedObject):
    """ Collection of BaseVoltages which is used to verify that the BusbarSection.BaseVoltage and other voltage attributes in the CIM are given a value existing in the collection.Collection of BaseVoltages which is used to verify that the BusbarSection.BaseVoltage and other voltage attributes in the CIM are given a value existing in the collection.
    """


    # The PowerSystemResource's base voltage.The PowerSystemResource's base voltage.
    nominal_voltage = Voltage

    # Virtual property. Use association to ConductingEquipment only when there is no VoltageLevel container used.Use association to ConductingEquipment only when there is no VoltageLevel container used.
    pass #conducting_equipment

    # Virtual property. The VoltageLevels having this BaseVoltage.The VoltageLevels having this BaseVoltage.
    pass #voltage_level

    # <<< base_voltage
    # @generated
    # >>> base_voltage


#------------------------------------------------------------------------------
#  "Unit" class:
#------------------------------------------------------------------------------

class Unit(IdentifiedObject):
    """ Quantity being measured. The Unit.name shall be unique among all specified quantities and describe the quantity. The Unit.aliasName is meant to be used for localization.Quantity being measured. The Unit.name shall be unique among all specified quantities and describe the quantity. The Unit.aliasName is meant to be used for localization.
    """


    # Virtual property. The Measurements having the UnitThe Measurements having the Unit
    pass #measurements

    # <<< unit
    # @generated
    # >>> unit


#------------------------------------------------------------------------------
#  "SubGeographicalRegion" class:
#------------------------------------------------------------------------------

class SubGeographicalRegion(IdentifiedObject):
    """ A subset of a geographical region of a power system network model.A subset of a geographical region of a power system network model.
    """


    # The association is used in the naming hierarchy.The association is used in the naming hierarchy.
    region = db.ReferenceProperty(collection_name="regions")

    # Virtual property. A Line can be contained by a SubGeographical Region.A Line can be contained by a SubGeographical Region.
    pass #lines

    # Virtual property. The association is used in the naming hierarchy.The association is used in the naming hierarchy.
    pass #substations

    # <<< sub_geographical_region
    # @generated
    # >>> sub_geographical_region


#------------------------------------------------------------------------------
#  "Curve" class:
#------------------------------------------------------------------------------

class Curve(IdentifiedObject):
    """ Relationship between an independent variable (X-axis) and one or two dependent  variables (Y1-axis and Y2-axis). Curves can also serve as schedules.Relationship between an independent variable (X-axis) and one or two dependent  variables (Y1-axis and Y2-axis). Curves can also serve as schedules.
    """


    # The Y2-axis units of measure.The Y2-axis units of measure.
    y2_unit = UnitSymbol

    # The X-axis units of measure.The X-axis units of measure.
    x_unit = UnitSymbol

    # The style or shape of the curve.The style or shape of the curve.
    curve_style = CurveStyle

    # The Y1-axis units of measure.The Y1-axis units of measure.
    y1_unit = UnitSymbol

    # Virtual property. The point data values that define a curveThe point data values that define a curve
    pass #curve_schedule_datas

    # <<< curve
    # @generated
    # >>> curve


#------------------------------------------------------------------------------
#  "PowerSystemResource" class:
#------------------------------------------------------------------------------

class PowerSystemResource(IdentifiedObject):
    """ A power system resource can be an item of equipment such as a Switch, an EquipmentContainer containing many individual items of equipment such as a  Substation, or an organisational entity such as Company or SubControlArea.  This provides for the nesting of collections of PowerSystemResources within other PowerSystemResources. For example, a Switch could be a member of a Substation and a Substation could be a member of a division of a Company.A power system resource can be an item of equipment such as a Switch, an EquipmentContainer containing many individual items of equipment such as a  Substation, or an organisational entity such as Company or SubControlArea.  This provides for the nesting of collections of PowerSystemResources within other PowerSystemResources. For example, a Switch could be a member of a Substation and a Substation could be a member of a division of a Company.
    """


    # Virtual property. The Measurements that are included in the naming hierarchy where the PSR is the containing objectThe Measurements that are included in the naming hierarchy where the PSR is the containing object
    pass #contains_measurements

    # <<< power_system_resource
    # @generated
    # >>> power_system_resource


#------------------------------------------------------------------------------
#  "BasicIntervalSchedule" class:
#------------------------------------------------------------------------------

class BasicIntervalSchedule(IdentifiedObject):
    """ Schedule of values at points in time.Schedule of values at points in time.
    """


    # The time for the first time point.The time for the first time point.
    start_time = db.DateProperty()

    # Value1 units of measure.Value1 units of measure.
    value1_unit = UnitSymbol

    # Value2 units of measure.Value2 units of measure.
    value2_unit = UnitSymbol

    # <<< basic_interval_schedule
    # @generated
    # >>> basic_interval_schedule


#------------------------------------------------------------------------------
#  "GeographicalRegion" class:
#------------------------------------------------------------------------------

class GeographicalRegion(IdentifiedObject):
    """ A geographical region of a power system network model.A geographical region of a power system network model.
    """


    # Virtual property. The association is used in the naming hierarchy.The association is used in the naming hierarchy.
    pass #regions

    # <<< geographical_region
    # @generated
    # >>> geographical_region


#------------------------------------------------------------------------------
#  "RegularIntervalSchedule" class:
#------------------------------------------------------------------------------

class RegularIntervalSchedule(BasicIntervalSchedule):
    """ The schedule has TimePoints where the time between them is constant.The schedule has TimePoints where the time between them is constant.
    """


    # The time for the last time point.The time for the last time point.
    end_time = db.DateProperty()

    # The time between each pair of subsequent RegularTimePoints.The time between each pair of subsequent RegularTimePoints.
    time_step = Seconds

    # Virtual property. The point data values that define a curveThe point data values that define a curve
    pass #time_points

    # <<< regular_interval_schedule
    # @generated
    # >>> regular_interval_schedule


#------------------------------------------------------------------------------
#  "ConnectivityNodeContainer" class:
#------------------------------------------------------------------------------

class ConnectivityNodeContainer(PowerSystemResource):
    """ A base class for all objects that may contain ConnectivityNodes.A base class for all objects that may contain ConnectivityNodes.
    """


    # Virtual property. Connectivity nodes contained by this container.Connectivity nodes contained by this container.
    pass #connectivity_nodes

    # <<< connectivity_node_container
    # @generated
    # >>> connectivity_node_container


#------------------------------------------------------------------------------
#  "EquipmentContainer" class:
#------------------------------------------------------------------------------

class EquipmentContainer(ConnectivityNodeContainer):
    """ A modeling construct to provide a root class for all Equipment classesA modeling construct to provide a root class for all Equipment classes
    """


    # Virtual property. The association is used in the naming hierarchy.The association is used in the naming hierarchy.
    pass #contains_equipments

    # <<< equipment_container
    # @generated
    # >>> equipment_container


#------------------------------------------------------------------------------
#  "VoltageLevel" class:
#------------------------------------------------------------------------------

class VoltageLevel(EquipmentContainer):
    """ A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these.A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these.
    """


    # The bus bar's low voltage limitThe bus bar's low voltage limit
    low_voltage_limit = Voltage

    # The bus bar's high voltage limitThe bus bar's high voltage limit
    high_voltage_limit = Voltage

    # The association is used in the naming hierarchy.The association is used in the naming hierarchy.
    member_of_substation = db.ReferenceProperty(collection_name="contains_voltage_levels")

    # The base voltage used for all equipment within the VoltageLevel.The base voltage used for all equipment within the VoltageLevel.
    base_voltage = db.ReferenceProperty(collection_name="voltage_level")

    # Virtual property. The association is used in the naming hierarchy.The association is used in the naming hierarchy.
    pass #contains_bays

    # <<< voltage_level
    # @generated
    # >>> voltage_level


#------------------------------------------------------------------------------
#  "Bay" class:
#------------------------------------------------------------------------------

class Bay(EquipmentContainer):
    """ A collection of power system resources (within a given substation) including conducting equipment, protection relays, measurements, and telemetry.A collection of power system resources (within a given substation) including conducting equipment, protection relays, measurements, and telemetry.
    """


    # The association is used in the naming hierarchy.The association is used in the naming hierarchy.
    member_of_voltage_level = db.ReferenceProperty(collection_name="contains_bays")

    # <<< bay
    # @generated
    # >>> bay


#------------------------------------------------------------------------------
#  "Equipment" class:
#------------------------------------------------------------------------------

class Equipment(PowerSystemResource):
    """ The parts of a power system that are physical devices, electronic or mechanicalThe parts of a power system that are physical devices, electronic or mechanical
    """


    # The association is used in the naming hierarchy.The association is used in the naming hierarchy.
    member_of_equipment_container = db.ReferenceProperty(collection_name="contains_equipments")

    # Virtual property. The equipment limit sets associated with the equipment.The equipment limit sets associated with the equipment.
    pass #operational_limit_set

    # <<< equipment
    # @generated
    # >>> equipment


#------------------------------------------------------------------------------
#  "Substation" class:
#------------------------------------------------------------------------------

class Substation(EquipmentContainer):
    """ A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk is passed for the purposes of switching or modifying its characteristics.A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk is passed for the purposes of switching or modifying its characteristics.
    """


    # The association is used in the naming hierarchy.The association is used in the naming hierarchy.
    region = db.ReferenceProperty(collection_name="substations")

    # Virtual property. The association is used in the naming hierarchy.The association is used in the naming hierarchy.
    pass #contains_voltage_levels

    # <<< substation
    # @generated
    # >>> substation


#------------------------------------------------------------------------------
#  "ConductingEquipment" class:
#------------------------------------------------------------------------------

class ConductingEquipment(Equipment):
    """ The parts of the power system that are designed to carry current or that are conductively connected therewith. ConductingEquipment is contained within an EquipmentContainer that may be a Substation, or a VoltageLevel or a Bay within a Substation.The parts of the power system that are designed to carry current or that are conductively connected therewith. ConductingEquipment is contained within an EquipmentContainer that may be a Substation, or a VoltageLevel or a Bay within a Substation.
    """


    # Use association to ConductingEquipment only when there is no VoltageLevel container used.Use association to ConductingEquipment only when there is no VoltageLevel container used.
    base_voltage = db.ReferenceProperty(collection_name="conducting_equipment")

    # Virtual property. ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodesConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes
    pass #terminals

    # <<< conducting_equipment
    # @generated
    # >>> conducting_equipment




# EOF -------------------------------------------------------------------------
