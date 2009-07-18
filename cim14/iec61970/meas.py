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
from cim14.iec61970.core import Equipment

from cim14.iec61970.scada import Source
from cim14.iec61970.domain import PerCent

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

Validity = db.StringProperty(choices=("good", "questionable", "invalid"))

ns_prefix = "cim.IEC61970.Meas"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#IEC61970.Meas"

class ValueAliasSet(IdentifiedObject):
    """ Describes the translation of a set of values into a name and is intendend to facilitate cusom translations. Each ValueAliasSet has a name, description etc. A specific Measurement may represent a discrete state like Open, Closed, Intermediate etc. This requires a translation from the MeasurementValue.value number to a string, e.g. 0->'Invalid', 1->'Open', 2->'Closed', 3->'Intermediate'. Each ValueToAlias member in ValueAliasSet.Value describe a mapping for one particular value to a name.
    """

    # The 'commands' property has been implicitly created by
    # the value_alias_set' property of Command.
    pass
    # The 'discretes' property has been implicitly created by
    # the value_alias_set' property of Discrete.
    pass
    # The 'values' property has been implicitly created by
    # the value_alias_set' property of ValueToAlias.
    pass

class LimitSet(IdentifiedObject):
    """ Specifies a set of Limits that are associated with a Measurement. A Measurement may have several LimitSets corresponding to seasonal or other changing conditions. The condition is captured in the name and description attributes. The same LimitSet may be used for several Measurements. In particular percentage limits are used this way.
    """

    # Tells if the limit values are in percentage of normalValue or the specified Unit for Measurements and Controls.
    is_percentage_limits = db.BooleanProperty()

class Measurement(IdentifiedObject):
    """ A Measurement represents any measured, calculated or non-measured non-calculated quantity. Any piece of equipment may contain Measurements, e.g. a substation may have temperature measurements and door open indications, a transformer may have oil temperature and tank pressure measurements, a bay may contain a number of power flow measurements and a Breaker may contain a switch status measurement.  The PSR - Measurement association is intended to capture this use of Measurement and is included in the naming hierarchy based on EquipmentContainer. The naming hierarchy typically has Measurements as leafs, e.g. Substation-VoltageLevel-Bay-Switch-Measurement. Some Measurements represent quantities related to a particular sensor location in the network, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is not captured in the PSR - Measurement association. Instead it is captured by the Measurement - Terminal association that is used to define the sensing location in the network topology. The location is defined by the connection of the Terminal to ConductingEquipment.  Two possible paths exist: 1) Measurement-Terminal- ConnectivityNode-Terminal-ConductingEquipment 2) Measurement-Terminal-ConductingEquipment Alternative 2 is the only allowed use.  When the sensor location is needed both Measurement-PSR and Measurement-Terminal are used. The Measurement-Terminal association is never used alone.
    """

    # Specifies the type of Measurement, e.g. IndoorTemperature, OutDoorTemperature, BusVoltage, GeneratorVoltage, LineFlow etc.
    measurement_type = db.StringProperty()
#    asset = db.ReferenceProperty()
#    unit = db.ReferenceProperty()
#    documents = db.ListProperty(db.Key)

#    @property
#    def measurements(self):
#        return Document.gql("WHERE documents = :1", self.key())
#    power_system_resource = db.ReferenceProperty()
#    terminal = db.ReferenceProperty()
#    locations = db.ListProperty(db.Key)

#    @property
#    def measurements(self):
#        return Location.gql("WHERE locations = :1", self.key())
#    for_tie_point = db.ReferenceProperty()
    # The 'dynamic_schedules' property has been implicitly created by
    # the measurement' property of DynamicSchedule.
    pass
#    pnode = db.ReferenceProperty()
#    by_tie_point = db.ReferenceProperty()
    # The 'violation_limits' property has been implicitly created by
    # the measurement' property of ViolationLimit.
    pass
    # The 'change_items' property has been implicitly created by
    # the measurement' property of ChangeItem.
    pass

class Quality61850(Element):
    """ Quality flags in this class are as defined in IEC 61850, except for estimatorReplaced, which has been included in this class for convenience.
    """

    # A correlation function has detected that the value is not consitent with other values. Typically set by a network State Estimator.
    suspect = db.BooleanProperty()
    # Measurement value is old and possibly invalid, as it has not been successfully updated during a specified time interval.
    old_data = db.BooleanProperty()
    # Measurement value is transmitted for test purposes.
    test = db.BooleanProperty()
    # Measurement value is beyond a predefined range of value.
    out_of_range = db.BooleanProperty()
    # Measurement value is blocked and hence unavailable for transmission.
    operator_blocked = db.BooleanProperty()
    # Validity of the measurement value.
    validity = Validity
    # Measurement value may be incorrect due to a reference being out of calibration.
    bad_reference = db.BooleanProperty()
    # Value has been replaced by State Estimator. estimatorReplaced is not an IEC61850 quality bit but has been put in this class for convenience.
    estimator_replaced = db.BooleanProperty()
    # Source gives information related to the origin of a value. The value may be acquired from the process, defaulted or substituted.
    source = Source
    # To prevent some overload of the communication it is sensible to detect and suppress oscillating (fast changing) binary inputs. If a signal changes in a defined time (tosc) twice in the same direction (from 0 to 1 or from 1 to 0) then oscillation is detected and the detail quality identifier 'oscillatory' is set. If it is detected a configured numbers of transient changes could be passed by. In this time the validity status 'questionable' is set. If after this defined numbers of changes the signal is still in the oscillating state the value shall be set either to the opposite state of the previous stable value or to a defined default value. In this case the validity status 'questionable' is reset and 'invalid' is set as long as the signal is oscillating. If it is configured such that no transient changes should be passed by then the validity status 'invalid' is set immediately in addition to the detail quality identifier 'oscillatory' (used for status information only).
    oscillatory = db.BooleanProperty()
    # Measurement value is beyond the capability of being  represented properly. For example, a counter value overflows from maximum count back to a value of zero.
    over_flow = db.BooleanProperty()
    # This identifier indicates that a supervision function has detected an internal or external failure, e.g. communication failure.
    failure = db.BooleanProperty()

class CurrentTransformer(Equipment):
    """ Instrument transformer used to measure electrical qualities of the circuit that is being protected and/or monitored. Typically used as current transducer for the purpose of metering or protection. A typical secondary current rating would be 5A.
    """

    # CT classification; i.e. class 10P.
    ct_class = db.StringProperty()
    # Percent of rated current for which the CT remains accurate within specified limits.
    accuracy_limit = db.StringProperty()
    # For multi-ratio CT's, the maximum permissable ratio attainable.
    max_ratio = db.FloatProperty()
    # Number of cores.
    core_count = db.IntegerProperty()
    # Intended usage of the CT; i.e. metering, protection.
    usage = db.StringProperty()
    # CT accuracy classification.
    accuracy_class = db.StringProperty()
#    current_transformer_type_asset = db.ReferenceProperty()
#    current_transformer_asset = db.ReferenceProperty()

class Control(IdentifiedObject):
    """ Control is used for supervisory/device control. It represents control outputs that are used to change the state in a process, e.g. close or open breaker, a set point value or a raise lower command.
    """

    # Indicates that a client is currently sending control commands that has not completed
    operation_in_progress = db.BooleanProperty()
    # The last time a control output was sent
    time_stamp = db.DateProperty()
#    control_type = db.ReferenceProperty()
#    remote_control = db.ReferenceProperty()
#    unit = db.ReferenceProperty()
#    regulating_cond_eq = db.ReferenceProperty()

class ControlType(IdentifiedObject):
    """ Specifies the type of Control, e.g. BreakerOn/Off, GeneratorVoltageSetPoint, TieLineFlow etc. The ControlType.name shall be unique among all specified types and describe the type. The ControlType.aliasName is meant to be used for localization.
    """

    # The 'controls' property has been implicitly created by
    # the control_type' property of Control.
    pass

class MeasurementValue(IdentifiedObject):
    """ The current state for a measurement. A state value is an instance of a measurement from a specific source. Measurements can be associated with many state values, each representing a different source for the measurement.
    """

    # The time when the value was last updated
    time_stamp = db.DateProperty()
    # The limit, expressed as a percentage of the sensor maximum, that errors will not exceed when the sensor is used under  reference conditions.
    sensor_accuracy = PerCent
    # The 'gml_values' property has been implicitly created by
    # the measurement_value' property of GmlValue.
    pass
#    measurement_value_source = db.ReferenceProperty()
#    erp_person = db.ReferenceProperty()
#    measurement_value_quality = db.ReferenceProperty()
#    procedure_data_sets = db.ListProperty(db.Key)

#    @property
#    def measurement_values(self):
#        return ProcedureDataSet.gql("WHERE procedure_data_sets = :1", self.key())
#    remote_source = db.ReferenceProperty()

class ValueToAlias(IdentifiedObject):
    """ Describes the translation of one particular value into a name, e.g. 1->'Open'
    """

    # The value that is mapped
    value = db.IntegerProperty()
#    value_alias_set = db.ReferenceProperty()

class MeasurementValueSource(IdentifiedObject):
    """ MeasurementValueSource describes the alternative sources updating a MeasurementValue. User conventions for how to use the MeasurementValueSource attributes are described in the introduction to IEC 61970-301.
    """

    # The 'measurement_values' property has been implicitly created by
    # the measurement_value_source' property of MeasurementValue.
    pass

class PotentialTransformer(Equipment):
    """ Instrument transformer (also known as Voltage Transformer) used to measure electrical qualities of the circuit that is being protected and/or monitored. Typically used as voltage transducer for the purpose of metering, protection, or sometimes auxiliary substation supply. A typical secondary voltage rating would be 120V.
    """

    # Nominal ratio between the primary and secondary voltage.
    nominal_ratio = db.FloatProperty()
    # PT classification.
    pt_class = db.StringProperty()
    # PT accuracy classification.
    accuracy_class = db.StringProperty()
#    potential_transformer_asset = db.ReferenceProperty()
#    potential_transformer_type_asset = db.ReferenceProperty()

class Limit(IdentifiedObject):
    """ Specifies one limit value for a Measurement. A Measurement typically has several limits that are kept together by the LimitSet class. The actual meaning and use of a Limit instance (i.e., if it is an alarm or warning limit or if it is a high or low limit) is not captured in the Limit class. However the name of a Limit instance may indicate both meaning and use.
    """

#    procedures = db.ListProperty(db.Key)

#    @property
#    def limits(self):
#        return Procedure.gql("WHERE procedures = :1", self.key())

class AccumulatorLimit(Limit):
    """ Limit values for Accumulator measurements
    """

    # The value to supervise against. The value is positive.
    value = db.IntegerProperty()
#    limit_set = db.ReferenceProperty()

class AccumulatorLimitSet(LimitSet):
    """ An AccumulatorLimitSet specifies a set of Limits that are associated with an Accumulator measurement.
    """

#    measurements = db.ListProperty(db.Key)

#    @property
#    def limit_sets(self):
#        return Accumulator.gql("WHERE measurements = :1", self.key())
    # The 'limits' property has been implicitly created by
    # the limit_set' property of AccumulatorLimit.
    pass

class SetPoint(Control):
    """ A SetPoint is an analog control used for supervisory control.
    """

    # Normal value for Control.value e.g. used for percentage scaling
    normal_value = db.FloatProperty()
    # Normal value range minimum for any of the Control.value. Used for scaling, e.g. in bar graphs.
    min_value = db.FloatProperty()
    # Normal value range maximum for any of the Control.value. Used for scaling, e.g. in bar graphs.
    max_value = db.FloatProperty()
    # The value representing the actuator output
    value = db.FloatProperty()
#    analog = db.ReferenceProperty()

class AccumulatorValue(MeasurementValue):
    """ AccumulatorValue represents a accumulated (counted) MeasurementValue.
    """

    # The value to supervise. The value is positive.
    value = db.IntegerProperty()
#    accumulator = db.ReferenceProperty()

class AnalogValue(MeasurementValue):
    """ AnalogValue represents an analog MeasurementValue.
    """

    # The value to supervise.
    value = db.FloatProperty()
    # The 'alt_generating_unit' property has been implicitly created by
    # the analog_value' property of AltGeneratingUnitMeas.
    pass
#    analog = db.ReferenceProperty()
    # The 'alt_tie_meas' property has been implicitly created by
    # the analog_value' property of AltTieMeas.
    pass

class DiscreteValue(MeasurementValue):
    """ DiscreteValue represents a discrete MeasurementValue.
    """

    # The value to supervise.
    value = db.IntegerProperty()
#    discrete = db.ReferenceProperty()

class Accumulator(Measurement):
    """ Accumulator represents a accumulated (counted) Measurement, e.g. an energy value.
    """

    # Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values.
    max_value = db.IntegerProperty()
    # The 'accumulator_values' property has been implicitly created by
    # the accumulator' property of AccumulatorValue.
    pass
#    limit_sets = db.ListProperty(db.Key)

#    @property
#    def measurements(self):
#        return AccumulatorLimitSet.gql("WHERE limit_sets = :1", self.key())

class AnalogLimitSet(LimitSet):
    """ An AnalogLimitSet specifies a set of Limits that are associated with an Analog measurement.
    """

#    measurements = db.ListProperty(db.Key)

#    @property
#    def limit_sets(self):
#        return Analog.gql("WHERE measurements = :1", self.key())
    # The 'limits' property has been implicitly created by
    # the limit_set' property of AnalogLimit.
    pass

class MeasurementValueQuality(Quality61850):
    """ Measurement quality flags. Bits 0-10 are defined for substation automation in draft IEC 61850 part 7-3. Bits 11-15 are reserved for future expansion by that document. Bits 16-31 are reserved for EMS applications.
    """

#    measurement_value = db.ReferenceProperty()

class StringMeasurementValue(MeasurementValue):
    """ StringMeasurementValue represents a measurement value of type string.
    """

    # The value to supervise.
    value = db.StringProperty()
#    string_measurement = db.ReferenceProperty()

class StringMeasurement(Measurement):
    """ StringMeasurement represents a measurement with values of type string.
    """

    # The 'string_measurement_values' property has been implicitly created by
    # the string_measurement' property of StringMeasurementValue.
    pass

class Command(Control):
    """ A Command is a discrete control used for supervisory control.
    """

    # The value representing the actuator output
    value = db.IntegerProperty()
    # Normal value for Control.value e.g. used for percentage scaling
    normal_value = db.IntegerProperty()
#    value_alias_set = db.ReferenceProperty()
#    discrete = db.ReferenceProperty()

class AnalogLimit(Limit):
    """ Limit values for Analog measurements
    """

    # The value to supervise against.
    value = db.FloatProperty()
#    limit_set = db.ReferenceProperty()

class Discrete(Measurement):
    """ Discrete represents a discrete Measurement, i.e. a Measurement reprsenting discrete values, e.g. a Breaker position.
    """

    # Normal measurement value, e.g., used for percentage calculations.
    normal_value = db.IntegerProperty()
    # Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values.
    max_value = db.IntegerProperty()
    # Normal value range minimum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values
    min_value = db.IntegerProperty()
#    command = db.ReferenceProperty()
    # The 'discrete_values' property has been implicitly created by
    # the discrete' property of DiscreteValue.
    pass
#    value_alias_set = db.ReferenceProperty()

class Analog(Measurement):
    """ Analog represents an analog Measurement.
    """

    # Normal value range minimum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values
    min_value = db.FloatProperty()
    # If true then this measurement is an active power, reactive power or current with the convention that a positive value measured at the Terminal means power is flowing into the related PowerSystemResource.
    positive_flow_in = db.BooleanProperty()
    # Normal measurement value, e.g., used for percentage calculations.
    normal_value = db.FloatProperty()
    # Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values.
    max_value = db.FloatProperty()
#    limit_sets = db.ListProperty(db.Key)

#    @property
#    def measurements(self):
#        return AnalogLimitSet.gql("WHERE limit_sets = :1", self.key())
    # The 'analog_values' property has been implicitly created by
    # the analog' property of AnalogValue.
    pass
#    set_point = db.ReferenceProperty()


