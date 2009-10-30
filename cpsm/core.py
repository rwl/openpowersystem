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
""" Contains the core PowerSystemResource and ConductingEquipment entities shared by all applications plus common collections of those entities. Not all applications require all the Core entities.
"""

from cpsm import Element

from cpsm.domain import Voltage
from cpsm.domain import Seconds
from cpsm.domain import UnitSymbol

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

CurveStyle = db.StringProperty(choices=("ramp_yvalue", "formula", "constant_yvalue", "straight_line_yvalues"))

ns_prefix = "cim"
ns_uri = "http://iec.ch/TC57/2008/CIM-schema-cim13#Package_Core"

class IdentifiedObject(Element):
    """ This is a root class to provide common naming attributes for all classes needing naming attributes
    """

    # The pathname is a system unique name composed from all IdentifiedObject.localNames in a naming hierarchy path from the object to the root.
    path_name = db.StringProperty()
    # The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy.
    description = db.StringProperty()
    # The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy.
    alias_name = db.StringProperty()
    # The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy.
    name = db.StringProperty()

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

class CurveData(Element):
    """ Data point values for defining a curve or schedule
    """

    # The data value of the second Y-axis variable (if present), depending on the Y-axis units
    y2value = db.FloatProperty()
    # The data value of the X-axis variable,  depending on the X-axis units
    xvalue = db.FloatProperty()
    # The data value of the  first Y-axis variable, depending on the Y-axis units
    y1value = db.FloatProperty()
#    curve_schedule = db.ReferenceProperty()

class Terminal(IdentifiedObject):
    """ An electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called 'connectivity nodes'.
    """

#    measurements = db.ReferenceProperty()
#    regulating_control = db.ReferenceProperty()
#    connectivity_node = db.ReferenceProperty()
#    conducting_equipment = db.ReferenceProperty()

class BaseVoltage(IdentifiedObject):
    """ Collection of BaseVoltages which is used to verify that the BusbarSection.BaseVoltage and other voltage attributes in the CIM are given a value existing in the collection.
    """

    # The PowerSystemResource's base voltage.
    nominal_voltage = Voltage
#    conducting_equipment = db.ReferenceProperty()
#    voltage_level = db.ReferenceProperty()

class Unit(IdentifiedObject):
    """ Quantity being measured. The Unit.name shall be unique among all specified quantities and describe the quantity. The Unit.aliasName is meant to be used for localization.
    """

#    measurements = db.ReferenceProperty()

class SubGeographicalRegion(IdentifiedObject):
    """ A subset of a geographical region of a power system network model.
    """

#    region = db.ReferenceProperty()
#    lines = db.ReferenceProperty()
#    substations = db.ReferenceProperty()

class Curve(IdentifiedObject):
    """ Relationship between an independent variable (X-axis) and one or two dependent  variables (Y1-axis and Y2-axis). Curves can also serve as schedules.
    """

    # The Y2-axis units of measure.
    y2_unit = UnitSymbol
    # The X-axis units of measure.
    x_unit = UnitSymbol
    # The style or shape of the curve.
    curve_style = CurveStyle
    # The Y1-axis units of measure.
    y1_unit = UnitSymbol
#    curve_schedule_datas = db.ReferenceProperty()

class PowerSystemResource(IdentifiedObject):
    """ A power system resource can be an item of equipment such as a Switch, an EquipmentContainer containing many individual items of equipment such as a  Substation, or an organisational entity such as Company or SubControlArea.  This provides for the nesting of collections of PowerSystemResources within other PowerSystemResources. For example, a Switch could be a member of a Substation and a Substation could be a member of a division of a Company.
    """

#    contains_measurements = db.ReferenceProperty()

class BasicIntervalSchedule(IdentifiedObject):
    """ Schedule of values at points in time.
    """

    # The time for the first time point.
    start_time = db.DateProperty()
    # Value1 units of measure.
    value1_unit = UnitSymbol
    # Value2 units of measure.
    value2_unit = UnitSymbol

class GeographicalRegion(IdentifiedObject):
    """ A geographical region of a power system network model.
    """

#    regions = db.ReferenceProperty()

class RegularIntervalSchedule(BasicIntervalSchedule):
    """ The schedule has TimePoints where the time between them is constant.
    """

    # The time for the last time point.
    end_time = db.DateProperty()
    # The time between each pair of subsequent RegularTimePoints.
    time_step = Seconds
#    time_points = db.ReferenceProperty()

class ConnectivityNodeContainer(PowerSystemResource):
    """ A base class for all objects that may contain ConnectivityNodes.
    """

#    connectivity_nodes = db.ReferenceProperty()

class EquipmentContainer(ConnectivityNodeContainer):
    """ A modeling construct to provide a root class for all Equipment classes
    """

#    contains_equipments = db.ReferenceProperty()

class VoltageLevel(EquipmentContainer):
    """ A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these.
    """

    # The bus bar's low voltage limit
    low_voltage_limit = Voltage
    # The bus bar's high voltage limit
    high_voltage_limit = Voltage
#    member_of_substation = db.ReferenceProperty()
#    base_voltage = db.ReferenceProperty()
#    contains_bays = db.ReferenceProperty()

class Bay(EquipmentContainer):
    """ A collection of power system resources (within a given substation) including conducting equipment, protection relays, measurements, and telemetry.
    """

#    member_of_voltage_level = db.ReferenceProperty()

class Equipment(PowerSystemResource):
    """ The parts of a power system that are physical devices, electronic or mechanical
    """

#    member_of_equipment_container = db.ReferenceProperty()
#    operational_limit_set = db.ReferenceProperty()

class Substation(EquipmentContainer):
    """ A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk is passed for the purposes of switching or modifying its characteristics.
    """

#    region = db.ReferenceProperty()
#    contains_voltage_levels = db.ReferenceProperty()

class ConductingEquipment(Equipment):
    """ The parts of the power system that are designed to carry current or that are conductively connected therewith. ConductingEquipment is contained within an EquipmentContainer that may be a Substation, or a VoltageLevel or a Bay within a Substation.
    """

#    base_voltage = db.ReferenceProperty()
#    terminals = db.ReferenceProperty()


