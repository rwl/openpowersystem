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

""" Contains the core PowerSystemResource and ConductingEquipment entities shared by all applications plus common collections of those entities. Not all applications require all the Core entities.  This package does not depend on any other package except the Domain package, but most of the other packages have associations and generalizations that depend on it.
"""

# <<< imports
# @generated
from ucte import Element

from ucte.domain import Voltage

from google.appengine.ext import db
# >>> imports

# <<< properties
# @generated
# >>> properties

# <<< constants
# @generated
NS_PREFIX = "cim"
NS_URI = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_Core"
# >>> constants

class IdentifiedObject(Element):
    """ This is a root class to provide common naming attributes for all classes needing naming attributes
    """
    # <<< identified_object.attributes
    # @generated
    # The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy.
    description = db.StringProperty()

    # The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy. This attribute is required on all instances in this Profile that inherit from IdentifiedObject except for the following Classes: 1) BaseVoltage; 2) Terminal; 3) TransformerWinding; 4) RatioTapChanger; 5) PhaseTapChanger; 6) OperationalLImitSet; 7) CurrentLimit; and, 8) VoltageLimit.
    name = db.StringProperty()

    # The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy. In the UCTE profile the aliasName is used to hold the EIC code.    The code length is 16 characters.    Not all CIM classes have an EIC code so the attribute is optional.
    alias_name = db.StringProperty()

    # >>> identified_object.attributes

    # <<< identified_object.references
    # @generated
    # >>> identified_object.references

    # <<< identified_object.operations
    # @generated
    # >>> identified_object.operations

class CurveData(Element):
    """ Data point values for defining a curve or schedule
    """
    # <<< curve_data.attributes
    # @generated
    # The data value of the  first Y-axis variable, depending on the Y-axis units
    y1value = db.FloatProperty()

    # The data value of the X-axis variable,  depending on the X-axis units
    xvalue = db.FloatProperty()

    # The data value of the second Y-axis variable (if present), depending on the Y-axis units
    y2value = db.FloatProperty()

    # >>> curve_data.attributes

    # <<< curve_data.references
    # @generated
    # The Curve defined by this CurveData.
    curve_schedule = db.ReferenceProperty(db.Model, collection_name="curve_schedule_datas")

    # >>> curve_data.references

    # <<< curve_data.operations
    # @generated
    # >>> curve_data.operations

class Curve(IdentifiedObject):
    """ Relationship between an independent variable (X-axis) and one or two dependent  variables (Y1-axis and Y2-axis). Curves can also serve as schedules.
    """
    # <<< curve.attributes
    # @generated
    # >>> curve.attributes

    # <<< curve.references
    # @generated
    # Virtual property. The point data values that define a curve
    pass # curve_schedule_datas

    # >>> curve.references

    # <<< curve.operations
    # @generated
    # >>> curve.operations

class ConnectivityNodeContainer(IdentifiedObject):
    """ A base class for all objects that may contain ConnectivityNodes or TopologicalNodes. The TopologicalNode will normally belong only to a VoltageLevel instance within a Substation.   All instances of TopologicalNode that are not X-nodes will require an association to a containing VoltageLevel instance.  The BaseVoltage of the VoltageLevel should match that of the TopologicalNode itself. A TopologicalNode object used for an X-node will not be contained, thus this association is specified as optional in the profile. The TopologicalNode will normally belong only to a VoltageLevel within a Substation. In the case of X-nodes, the TopologicalNode is not contained.
    """
    # <<< connectivity_node_container.attributes
    # @generated
    # >>> connectivity_node_container.attributes

    # <<< connectivity_node_container.references
    # @generated
    # Virtual property. The topological nodes which belong to this connectivity node container.
    pass # topological_node

    # >>> connectivity_node_container.references

    # <<< connectivity_node_container.operations
    # @generated
    # >>> connectivity_node_container.operations

class Equipment(IdentifiedObject):
    """ The parts of a power system that are physical devices, electronic or mechanical
    """
    # <<< equipment.attributes
    # @generated
    # Indicates if the equipment is real equipment (false) or an equivalent. If this is missing, it is assumed to be False.  It is required for Equipment connected to the X-Node. All classes derived from Equipment are to include this attribute except for the TransformerWinding class.     For transformers the PowerTransformer class will be used to specify the real or equivalent status and the contained TransformerWinding class instances need not and should not specify this attribute.
    equivalent = db.BooleanProperty()

    # >>> equipment.attributes

    # <<< equipment.references
    # @generated
    # The association is used in the naming hierarchy. For a TransformerWinding and ACLineSegment, the association Equipment.MemberOf_EquipmentContainer is not used.  The TransformerWinding instance is instead contained within a PowerTransformer unless the association refers to a different substation than what is used in the PowerTransformer association.
    member_of_equipment_container = db.ReferenceProperty(db.Model, collection_name="contains_equipments")

    # >>> equipment.references

    # <<< equipment.operations
    # @generated
    # >>> equipment.operations

class BaseVoltage(IdentifiedObject):
    """ Collection of BaseVoltages which is used to verify that the BusbarSection.BaseVoltage and other voltage attributes in the CIM are given a value existing in the collection. The profile requires a BaseVoltage associaton on ConductingEquipment subtypes of classes ACLineSegment and TransformerWinding. The association is not used for any other subtypes. The base voltage of the TopologicalNode should match the BaseVoltage of the containing VoltageLevel if such a containing VoltageLevel is specified.
    """
    # <<< base_voltage.attributes
    # @generated
    # The PowerSystemResource's base voltage.
    nominal_voltage = Voltage

    # If true, this is a direct current base voltage and items assigned to this base voltage are also associated with a direct current capabilities.   False indicates alternating current.
    is_dc = db.BooleanProperty()

    # >>> base_voltage.attributes

    # <<< base_voltage.references
    # @generated
    # Virtual property. Use association to ConductingEquipment only when there is no VoltageLevel container used.
    pass # conducting_equipment

    # Virtual property. The VoltageLevels having this BaseVoltage.
    pass # voltage_level

    # Virtual property. The topological nodes at the base voltage.
    pass # topological_node

    # >>> base_voltage.references

    # <<< base_voltage.operations
    # @generated
    # >>> base_voltage.operations

class EquipmentContainer(ConnectivityNodeContainer):
    """ A modeling construct to provide a root class for all Equipment classes For a TransformerWinding the association Equipment.MemberOf_EquipmentContainer is not used.  The TransformerWinding instance is instead contained within a PowerTransformer unless the association refers to a different substation than what is used in the PowerTransformer Association. For a TransformerWinding and ACLineSegment, the association Equipment.MemberOf_EquipmentContainer is not used.  The TransformerWinding instance is instead contained within a PowerTransformer unless the association refers to a different substation than what is used in the PowerTransformer association.
    """
    # <<< equipment_container.attributes
    # @generated
    # >>> equipment_container.attributes

    # <<< equipment_container.references
    # @generated
    # Virtual property. The association is used in the naming hierarchy.
    pass # contains_equipments

    # >>> equipment_container.references

    # <<< equipment_container.operations
    # @generated
    # >>> equipment_container.operations

class Substation(EquipmentContainer):
    """ A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk is passed for the purposes of switching or modifying its characteristics.
    """
    # <<< substation.attributes
    # @generated
    # >>> substation.attributes

    # <<< substation.references
    # @generated
    # Virtual property. The association is used in the naming hierarchy.
    pass # contains_voltage_levels

    # The association is used in the naming hierarchy.
    region = db.ReferenceProperty(db.Model, collection_name="substations")

    # >>> substation.references

    # <<< substation.operations
    # @generated
    # >>> substation.operations

class ConductingEquipment(Equipment):
    """ The parts of the power system that are designed to carry current or that are conductively connected therewith. ConductingEquipment is contained within an EquipmentContainer that may be a Substation, or a VoltageLevel or a Bay within a Substation.
    """
    # <<< conducting_equipment.attributes
    # @generated
    # >>> conducting_equipment.attributes

    # <<< conducting_equipment.references
    # Use association to ConductingEquipment only when there is no VoltageLevel container used. The profile requires a BaseVoltage associaton on ConductingEquipment subtypes of classes ACLineSegment and TransformerWinding. The association is not used for any other subtypes.
    base_voltage = db.ReferenceProperty(BaseVoltage, collection_name="conducting_equipments")

    # Virtual property. ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes
    pass # terminals

    # >>> conducting_equipment.references

    # <<< conducting_equipment.operations
    # @generated
    # >>> conducting_equipment.operations

class SubGeographicalRegion(IdentifiedObject):
    """ A subset of a geographical region of a power system network model.
    """
    # <<< sub_geographical_region.attributes
    # @generated
    # >>> sub_geographical_region.attributes

    # <<< sub_geographical_region.references
    # @generated
    # Virtual property. The association is used in the naming hierarchy.
    pass # substations

    # The association is used in the naming hierarchy.
    region = db.ReferenceProperty(db.Model, collection_name="regions")

    # >>> sub_geographical_region.references

    # <<< sub_geographical_region.operations
    # @generated
    # >>> sub_geographical_region.operations

class Terminal(IdentifiedObject):
    """ An electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called 'connectivity nodes'. The SvPowerFlow is only associated with the Terminal objects of shunt injection classes such as EnergyConsumer and SynchronousMachine.   The flows at any ShuntCompensator can always be computed from connected voltage magnitude, number of sections and local attributes.  Branch flows are not exchanged since they can be readily be computed from the voltages, impedances, and for transformers additionally the tap parameters including the SvTapStep.  For UCTE profile, the terminal associated with the limit is always required, and thus there is no need to exchange the associated Equipment which can always be derived from the terminal. The SvPowerFlow is only associated with the Terminal objects of shunt injection classes EnergyConsumer and  SynchronousMachine.  Branch flows are not exchanged since they can be readily computed from the voltages, impedances, and for transformers additionally the tap parameters including the SvTapStep.  Similarly, Switch flows are not included because they can typically be uniquely computed, except in the case of meshed networks of Switch objects.  Terminals of the ShuntCompensator class are not associated because the injection value can be computed from the solved voltage, number of sections, Termianl.connected state, and the impedance per section attributes on the ShuntCompensator.
    """
    # <<< terminal.attributes
    # @generated
    # The orientation of the terminal connections for a multiple terminal conducting equipment.  The sequence numbering starts with 1 and additional terminals should follow in increasing order.   The first terminal is the 'starting point' for a two terminal branch.   In the case of class TransformerWinding only one terminal is used so its sequenceNumber must be 1. For UCTE profile, the terminal sequence number is not required.   And, when used, follows the UML description. The orientation of the terminal connections for a multiple terminal conducting equipment.  The sequence numbering starts with 1 and additional terminals should follow in increasing order.   The first terminal is the 'starting point' for a two terminal branch.   In the case of class TransformerWinding only one terminal is used so its sequenceNumber must be 1.
    sequence_number = db.IntegerProperty()

    # The terminal connection status.   True implies the terminal is connected, and false implies the terminal is not connected. This is the result of topoplogical processing of a detailed Connectivity node and Switch model whether present in the model or not.   A terminal that is not connected cannot support a current flow.   A terminal that is connected may have flow.  In general a multi-terminal device may simultaneously have connected and disconnected terminals.  No other aspect of the algorithm for topological analysis is implied.
    connected = db.BooleanProperty()

    # >>> terminal.attributes

    # <<< terminal.references
    # @generated
    # Virtual property. Mutual couplings associated with the branch as the first branch.
    pass # has_first_mutual_coupling

    # Virtual property. The operatinal limits sets that applie specifically to this terminal.  Other operational limits sets may apply to this terminal through the association to Equipment.
    pass # operational_limit_set

    # The power flow state associated with the terminal.
    sv_power_flow = db.ReferenceProperty(collection_name="_terminal_set")

    # Virtual property. The terminal is regulated by a control.
    pass # regulating_control

    # Virtual property. The control area tie flows to which this terminal associates.
    pass # tie_flow

    # ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes
    conducting_equipment_ = db.ReferenceProperty(db.Model, collection_name="terminals")

    # The topological node associated with the terminal.   This can be used as an alternative to the connectivity node path to topological node, thus making it unneccesary to model connedtivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would proably not be used.
    topological_node = db.ReferenceProperty(db.Model, collection_name="terminal")

    # Virtual property. Mutual couplings with the branch associated as the first branch.
    pass # has_second_mutual_coupling

    # >>> terminal.references

    # <<< terminal.operations
    # @generated
    # >>> terminal.operations

class GeographicalRegion(IdentifiedObject):
    """ A geographical region of a power system network model.
    """
    # <<< geographical_region.attributes
    # @generated
    # >>> geographical_region.attributes

    # <<< geographical_region.references
    # @generated
    # Virtual property. The association is used in the naming hierarchy.
    pass # regions

    # >>> geographical_region.references

    # <<< geographical_region.operations
    # @generated
    # >>> geographical_region.operations

class VoltageLevel(EquipmentContainer):
    """ A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these.
    """
    # <<< voltage_level.attributes
    # @generated
    # >>> voltage_level.attributes

    # <<< voltage_level.references
    # @generated
    # The base voltage used for all equipment within the VoltageLevel.
    base_voltage = db.ReferenceProperty(db.Model, collection_name="voltage_level")

    # The association is used in the naming hierarchy.
    member_of_substation = db.ReferenceProperty(db.Model, collection_name="contains_voltage_levels")

    # >>> voltage_level.references

    # <<< voltage_level.operations
    # @generated
    # >>> voltage_level.operations



# EOF -------------------------------------------------------------------------
