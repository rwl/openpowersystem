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
""" Contains the core PowerSystemResource and ConductingEquipment entities shared by all applications plus common collections of those entities. Not all applications require all the Core entities.  This package does not depend on any other package except the Domain package, but most of the other packages have associations and generalizations that depend on it.Contains the core PowerSystemResource and ConductingEquipment entities shared by all applications plus common collections of those entities. Not all applications require all the Core entities.  This package does not depend on any other package except the Domain package, but most of the other packages have associations and generalizations that depend on it.
"""

from ucte import Element

from ucte.domain import Voltage

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

ns_prefix = "cim"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_Core"

class IdentifiedObject(Element):
    """ This is a root class to provide common naming attributes for all classes needing naming attributesThis is a root class to provide common naming attributes for all classes needing naming attributes
    """

    # The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy.The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy.
    description = db.StringProperty()
    # The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy.This attribute is required on all instances in this Profile that inherit from IdentifiedObject except for the following Classes: 1) BaseVoltage; 2) Terminal; 3) TransformerWinding; 4) RatioTapChanger; 5) PhaseTapChanger; 6) OperationalLImitSet; 7) CurrentLimit; and, 8) VoltageLimit.The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy.This attribute is required on all instances in this Profile that inherit from IdentifiedObject except for the following Classes: 1) BaseVoltage; 2) Terminal; 3) TransformerWinding; 4) RatioTapChanger; 5) PhaseTapChanger; 6) OperationalLImitSet; 7) CurrentLimit; and, 8) VoltageLimit.
    name = db.StringProperty()
    # The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy.In the UCTE profile the aliasName is used to hold the EIC code.    The code length is 16 characters.    Not all CIM classes have an EIC code so the attribute is optional.   The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy.In the UCTE profile the aliasName is used to hold the EIC code.    The code length is 16 characters.    Not all CIM classes have an EIC code so the attribute is optional.   
    alias_name = db.StringProperty()

class CurveData(Element):
    """ Data point values for defining a curve or scheduleData point values for defining a curve or schedule
    """

    # The data value of the  first Y-axis variable, depending on the Y-axis unitsThe data value of the  first Y-axis variable, depending on the Y-axis units
    y1value = db.FloatProperty()
    # The data value of the X-axis variable,  depending on the X-axis unitsThe data value of the X-axis variable,  depending on the X-axis units
    xvalue = db.FloatProperty()
    # The data value of the second Y-axis variable (if present), depending on the Y-axis unitsThe data value of the second Y-axis variable (if present), depending on the Y-axis units
    y2value = db.FloatProperty()
#    curve_schedule = db.ReferenceProperty()

class Curve(IdentifiedObject):
    """ Relationship between an independent variable (X-axis) and one or two dependent  variables (Y1-axis and Y2-axis). Curves can also serve as schedules.Relationship between an independent variable (X-axis) and one or two dependent  variables (Y1-axis and Y2-axis). Curves can also serve as schedules.
    """

    # The 'curve_schedule_datas' property has been implicitly created by
    # the curve_schedule' property of CurveData.
    pass

class ConnectivityNodeContainer(IdentifiedObject):
    """ A base class for all objects that may contain ConnectivityNodes or TopologicalNodes.The TopologicalNode will normally belong only to a VoltageLevel instance within a Substation.   All instances of TopologicalNode that are not X-nodes will require an association to a containing VoltageLevel instance.  The BaseVoltage of the VoltageLevel should match that of the TopologicalNode itself. A TopologicalNode object used for an X-node will not be contained, thus this association is specified as optional in the profile. The TopologicalNode will normally belong only to a VoltageLevel within a Substation. In the case of X-nodes, the TopologicalNode is not contained.    A base class for all objects that may contain ConnectivityNodes or TopologicalNodes.The TopologicalNode will normally belong only to a VoltageLevel instance within a Substation.   All instances of TopologicalNode that are not X-nodes will require an association to a containing VoltageLevel instance.  The BaseVoltage of the VoltageLevel should match that of the TopologicalNode itself. A TopologicalNode object used for an X-node will not be contained, thus this association is specified as optional in the profile. The TopologicalNode will normally belong only to a VoltageLevel within a Substation. In the case of X-nodes, the TopologicalNode is not contained.    
    """

    # The 'topological_node' property has been implicitly created by
    # the connectivity_node_container' property of TopologicalNode.
    pass

class Equipment(IdentifiedObject):
    """ The parts of a power system that are physical devices, electronic or mechanicalThe parts of a power system that are physical devices, electronic or mechanical
    """

    # Indicates if the equipment is real equipment (false) or an equivalent.If this is missing, it is assumed to be False.  It is required for Equipment connected to the X-Node. All classes derived from Equipment are to include this attribute except for the TransformerWinding class.     For transformers the PowerTransformer class will be used to specify the real or equivalent status and the contained TransformerWinding class instances need not and should not specify this attribute.Indicates if the equipment is real equipment (false) or an equivalent.If this is missing, it is assumed to be False.  It is required for Equipment connected to the X-Node. All classes derived from Equipment are to include this attribute except for the TransformerWinding class.     For transformers the PowerTransformer class will be used to specify the real or equivalent status and the contained TransformerWinding class instances need not and should not specify this attribute.
    equivalent = db.BooleanProperty()
#    member_of_equipment_container = db.ReferenceProperty()

class BaseVoltage(IdentifiedObject):
    """ Collection of BaseVoltages which is used to verify that the BusbarSection.BaseVoltage and other voltage attributes in the CIM are given a value existing in the collection.The profile requires a BaseVoltage associaton on ConductingEquipment subtypes of classes ACLineSegment and TransformerWinding. The association is not used for any other subtypes. The base voltage of the TopologicalNode should match the BaseVoltage of the containing VoltageLevel if such a containing VoltageLevel is specified.Collection of BaseVoltages which is used to verify that the BusbarSection.BaseVoltage and other voltage attributes in the CIM are given a value existing in the collection.The profile requires a BaseVoltage associaton on ConductingEquipment subtypes of classes ACLineSegment and TransformerWinding. The association is not used for any other subtypes. The base voltage of the TopologicalNode should match the BaseVoltage of the containing VoltageLevel if such a containing VoltageLevel is specified.
    """

    # The PowerSystemResource's base voltage.The PowerSystemResource's base voltage.
    nominal_voltage = Voltage
    # If true, this is a direct current base voltage and items assigned to this base voltage are also associated with a direct current capabilities.   False indicates alternating current.If true, this is a direct current base voltage and items assigned to this base voltage are also associated with a direct current capabilities.   False indicates alternating current.
    is_dc = db.BooleanProperty()
    # The 'conducting_equipment' property has been implicitly created by
    # the base_voltage' property of ConductingEquipment.
    pass
    # The 'voltage_level' property has been implicitly created by
    # the base_voltage' property of VoltageLevel.
    pass
    # The 'topological_node' property has been implicitly created by
    # the base_voltage' property of TopologicalNode.
    pass

class EquipmentContainer(ConnectivityNodeContainer):
    """ A modeling construct to provide a root class for all Equipment classesFor a TransformerWinding the association Equipment.MemberOf_EquipmentContainer is not used.  The TransformerWinding instance is instead contained within a PowerTransformer unless the association refers to a different substation than what is used in the PowerTransformer Association. For a TransformerWinding and ACLineSegment, the association Equipment.MemberOf_EquipmentContainer is not used.  The TransformerWinding instance is instead contained within a PowerTransformer unless the association refers to a different substation than what is used in the PowerTransformer association. A modeling construct to provide a root class for all Equipment classesFor a TransformerWinding the association Equipment.MemberOf_EquipmentContainer is not used.  The TransformerWinding instance is instead contained within a PowerTransformer unless the association refers to a different substation than what is used in the PowerTransformer Association. For a TransformerWinding and ACLineSegment, the association Equipment.MemberOf_EquipmentContainer is not used.  The TransformerWinding instance is instead contained within a PowerTransformer unless the association refers to a different substation than what is used in the PowerTransformer association. 
    """

    # The 'contains_equipments' property has been implicitly created by
    # the member_of_equipment_container' property of Equipment.
    pass

class Substation(EquipmentContainer):
    """ A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk is passed for the purposes of switching or modifying its characteristics.A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk is passed for the purposes of switching or modifying its characteristics.
    """

    # The 'contains_voltage_levels' property has been implicitly created by
    # the member_of_substation' property of VoltageLevel.
    pass
#    region = db.ReferenceProperty()

class ConductingEquipment(Equipment):
    """ The parts of the power system that are designed to carry current or that are conductively connected therewith. ConductingEquipment is contained within an EquipmentContainer that may be a Substation, or a VoltageLevel or a Bay within a Substation.The parts of the power system that are designed to carry current or that are conductively connected therewith. ConductingEquipment is contained within an EquipmentContainer that may be a Substation, or a VoltageLevel or a Bay within a Substation.
    """

#    base_voltage = db.ReferenceProperty()
    # The 'terminals' property has been implicitly created by
    # the conducting_equipment' property of Terminal.
    pass

class SubGeographicalRegion(IdentifiedObject):
    """ A subset of a geographical region of a power system network model.A subset of a geographical region of a power system network model.
    """

    # The 'substations' property has been implicitly created by
    # the region' property of Substation.
    pass
#    region = db.ReferenceProperty()

class Terminal(IdentifiedObject):
    """ An electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called 'connectivity nodes'.The SvPowerFlow is only associated with the Terminal objects of shunt injection classes such as EnergyConsumer and SynchronousMachine.   The flows at any ShuntCompensator can always be computed from connected voltage magnitude, number of sections and local attributes.  Branch flows are not exchanged since they can be readily be computed from the voltages, impedances, and for transformers additionally the tap parameters including the SvTapStep.  For UCTE profile, the terminal associated with the limit is always required, and thus there is no need to exchange the associated Equipment which can always be derived from the terminal. The SvPowerFlow is only associated with the Terminal objects of shunt injection classes EnergyConsumer and  SynchronousMachine.  Branch flows are not exchanged since they can be readily computed from the voltages, impedances, and for transformers additionally the tap parameters including the SvTapStep.  Similarly, Switch flows are not included because they can typically be uniquely computed, except in the case of meshed networks of Switch objects.  Terminals of the ShuntCompensator class are not associated because the injection value can be computed from the solved voltage, number of sections, Termianl.connected state, and the impedance per section attributes on the ShuntCompensator. An electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called 'connectivity nodes'.The SvPowerFlow is only associated with the Terminal objects of shunt injection classes such as EnergyConsumer and SynchronousMachine.   The flows at any ShuntCompensator can always be computed from connected voltage magnitude, number of sections and local attributes.  Branch flows are not exchanged since they can be readily be computed from the voltages, impedances, and for transformers additionally the tap parameters including the SvTapStep.  For UCTE profile, the terminal associated with the limit is always required, and thus there is no need to exchange the associated Equipment which can always be derived from the terminal. The SvPowerFlow is only associated with the Terminal objects of shunt injection classes EnergyConsumer and  SynchronousMachine.  Branch flows are not exchanged since they can be readily computed from the voltages, impedances, and for transformers additionally the tap parameters including the SvTapStep.  Similarly, Switch flows are not included because they can typically be uniquely computed, except in the case of meshed networks of Switch objects.  Terminals of the ShuntCompensator class are not associated because the injection value can be computed from the solved voltage, number of sections, Termianl.connected state, and the impedance per section attributes on the ShuntCompensator. 
    """

    # The orientation of the terminal connections for a multiple terminal conducting equipment.  The sequence numbering starts with 1 and additional terminals should follow in increasing order.   The first terminal is the 'starting point' for a two terminal branch.   In the case of class TransformerWinding only one terminal is used so its sequenceNumber must be 1.For UCTE profile, the terminal sequence number is not required.   And, when used, follows the UML description. The orientation of the terminal connections for a multiple terminal conducting equipment.  The sequence numbering starts with 1 and additional terminals should follow in increasing order.   The first terminal is the 'starting point' for a two terminal branch.   In the case of class TransformerWinding only one terminal is used so its sequenceNumber must be 1.The orientation of the terminal connections for a multiple terminal conducting equipment.  The sequence numbering starts with 1 and additional terminals should follow in increasing order.   The first terminal is the 'starting point' for a two terminal branch.   In the case of class TransformerWinding only one terminal is used so its sequenceNumber must be 1.For UCTE profile, the terminal sequence number is not required.   And, when used, follows the UML description. The orientation of the terminal connections for a multiple terminal conducting equipment.  The sequence numbering starts with 1 and additional terminals should follow in increasing order.   The first terminal is the 'starting point' for a two terminal branch.   In the case of class TransformerWinding only one terminal is used so its sequenceNumber must be 1.
    sequence_number = db.IntegerProperty()
    # The terminal connection status.   True implies the terminal is connected, and false implies the terminal is not connected. This is the result of topoplogical processing of a detailed Connectivity node and Switch model whether present in the model or not.   A terminal that is not connected cannot support a current flow.   A terminal that is connected may have flow.  In general a multi-terminal device may simultaneously have connected and disconnected terminals.  No other aspect of the algorithm for topological analysis is implied.The terminal connection status.   True implies the terminal is connected, and false implies the terminal is not connected. This is the result of topoplogical processing of a detailed Connectivity node and Switch model whether present in the model or not.   A terminal that is not connected cannot support a current flow.   A terminal that is connected may have flow.  In general a multi-terminal device may simultaneously have connected and disconnected terminals.  No other aspect of the algorithm for topological analysis is implied.
    connected = db.BooleanProperty()
    # The 'has_first_mutual_coupling' property has been implicitly created by
    # the first_terminal' property of MutualCoupling.
    pass
    # The 'operational_limit_set' property has been implicitly created by
    # the terminal' property of OperationalLimitSet.
    pass
#    sv_power_flow = db.ReferenceProperty()
    # The 'regulating_control' property has been implicitly created by
    # the terminal' property of RegulatingControl.
    pass
    # The 'tie_flow' property has been implicitly created by
    # the terminal' property of TieFlow.
    pass
#    conducting_equipment = db.ReferenceProperty()
#    topological_node = db.ReferenceProperty()
    # The 'has_second_mutual_coupling' property has been implicitly created by
    # the second_terminal' property of MutualCoupling.
    pass

class GeographicalRegion(IdentifiedObject):
    """ A geographical region of a power system network model.A geographical region of a power system network model.
    """

    # The 'regions' property has been implicitly created by
    # the region' property of SubGeographicalRegion.
    pass

class VoltageLevel(EquipmentContainer):
    """ A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these.A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these.
    """

#    base_voltage = db.ReferenceProperty()
#    member_of_substation = db.ReferenceProperty()


