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

from cim14.iec61970.core import RegularIntervalSchedule
from cim14.iec61970.core import IdentifiedObject
from cim14 import Element
from cim14.iec61970.wires import EnergyConsumer
from cim14.iec61970.core import PowerSystemResource

from cim14.iec61970.domain import PerCent

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

SeasonName = db.StringProperty(choices=("spring", "winter", "summer", "fall"))

ns_prefix = "cim.IEC61970.LoadModel"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#IEC61970.LoadModel"

class SeasonDayTypeSchedule(RegularIntervalSchedule):
    """ The schedule specialize RegularIntervalSchedule with type curve data for a specific type of day and season. This means that curves of this type cover a 24 hour period.
    """

#    day_type = db.ReferenceProperty()
#    season = db.ReferenceProperty()

class LoadGroup(IdentifiedObject):
    """ The class is the third level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.
    """

    # The 'registered_loads' property has been implicitly created by
    # the load_area' property of RegisteredLoad.
    pass
#    sub_load_area = db.ReferenceProperty()

class Season(Element):
    """ A specified time period of the year, e.g., Spring, Summer, Fall, Winter
    """

    # Date season ends
    end_date = db.DateProperty()
    # Name of the Season
    name = SeasonName
    # Date season starts
    start_date = db.DateProperty()
    # The 'season_day_type_schedules' property has been implicitly created by
    # the season' property of SeasonDayTypeSchedule.
    pass
    # The 'capacity_benefit_margin' property has been implicitly created by
    # the season' property of CapacityBenefitMargin.
    pass
    # The 'violation_limits' property has been implicitly created by
    # the season' property of ViolationLimit.
    pass

class NonConformLoad(EnergyConsumer):
    """ NonConformLoad represent loads that do not follow a daily load change pattern and changes are not correlated with the daily load change pattern.
    """

#    load_group = db.ReferenceProperty()

class EnergyArea(IdentifiedObject):
    """ The class describes an area having energy production or consumption. The class is the basis for further specialization.
    """

#    control_area = db.ReferenceProperty()

class DayType(IdentifiedObject):
    """ Group of similar days, e.g., Mon/Tue/Wed, Thu/Fri, Sat/Sun, Holiday1, Holiday2
    """

    # The 'season_day_type_schedules' property has been implicitly created by
    # the day_type' property of SeasonDayTypeSchedule.
    pass

class StationSupply(EnergyConsumer):
    """ Station supply with load derived from the station output.
    """

    pass

class ConformLoad(EnergyConsumer):
    """ ConformLoad represent loads that follow a daily load change pattern where the pattern can be used to scale the load with a system load.
    """

#    load_group = db.ReferenceProperty()

class PowerCutZone(PowerSystemResource):
    """ An area or zone of the power system which is used for load shedding purposes.
    """

    # Second level (amount) of load to cut as a percentage of total zone load
    cut_level2 = PerCent
    # First level (amount) of load to cut as a percentage of total zone load
    cut_level1 = PerCent
    # The 'energy_consumers' property has been implicitly created by
    # the power_cut_zone' property of EnergyConsumer.
    pass

class LoadResponseCharacteristic(IdentifiedObject):
    """ Models the characteristic response of the load demand due to to changes in system conditions such as voltage and frequency. This is not related to demand response.
    """

    # Portion of active power load modeled as constant impedance.  Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP.
    p_constant_impedance = db.FloatProperty()
    # Portion of reactive power load modeled as constant power. Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP.
    q_constant_power = db.FloatProperty()
    # Exponent of per unit voltage effecting real power.   This model used only when 'useExponentModel' is true.
    p_voltage_exponent = db.FloatProperty()
    # Portion of reactive power load modeled as constant current. Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP.
    q_constant_current = db.FloatProperty()
    # Exponent of per unit frequency effecting reactive power
    q_frequency_exponent = db.FloatProperty()
    # Exponent of per unit frequency effecting active power
    p_frequency_exponent = db.FloatProperty()
    # Portion of active power load modeled as constant current. Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP.
    p_constant_current = db.FloatProperty()
    # Portion of reactive power load modeled as constant impedance.  Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP.
    q_constant_impedance = db.FloatProperty()
    # Indicates the exponential voltage dependency model (pVoltateExponent and qVoltageExponent) is to be used.   If false, the coeficient model (consisting of pConstantImpedance, pConstantCurrent, pConstantPower, qConstantImpedance, qConstantCurrent, and qConstantPower) is to be used.
    exponent_model = db.BooleanProperty()
    # Exponent of per unit voltage effecting reactive power.   This model used only when 'useExponentModel' is true.
    q_voltage_exponent = db.FloatProperty()
    # Portion of active power load modeled as constant power. Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP.
    p_constant_power = db.FloatProperty()
    # The 'energy_consumer' property has been implicitly created by
    # the load_response' property of EnergyConsumer.
    pass

class ConformLoadGroup(LoadGroup):
    """ Load that follows a daily and seasonal load variation pattern.
    """

    # The 'energy_consumers' property has been implicitly created by
    # the load_group' property of ConformLoad.
    pass
    # The 'conform_load_schedules' property has been implicitly created by
    # the conform_load_group' property of ConformLoadSchedule.
    pass

class NonConformLoadSchedule(SeasonDayTypeSchedule):
    """ An active power (Y1-axis) and reactive power (Y2-axis) schedule (curves) versus time (X-axis) for non-conforming loads, e.g., large industrial load or power station service (where modeled)
    """

#    non_conform_load_group = db.ReferenceProperty()

class SubLoadArea(EnergyArea):
    """ The class is the second level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.
    """

    # The 'load_groups' property has been implicitly created by
    # the sub_load_area' property of LoadGroup.
    pass
#    load_area = db.ReferenceProperty()

class ConformLoadSchedule(SeasonDayTypeSchedule):
    """ A curve of load  versus time (X-axis) showing the active power values (Y1-axis) and reactive power (Y2-axis) for each unit of the period covered. This curve represents a typical pattern of load over the time period for a given day type and season.
    """

#    conform_load_group = db.ReferenceProperty()

class NonConformLoadGroup(LoadGroup):
    """ Loads that do not follow a daily and seasonal load variation pattern.
    """

    # The 'energy_consumers' property has been implicitly created by
    # the load_group' property of NonConformLoad.
    pass
    # The 'non_conform_load_schedules' property has been implicitly created by
    # the non_conform_load_group' property of NonConformLoadSchedule.
    pass

class LoadArea(EnergyArea):
    """ The class is the root or first level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.
    """

    # The 'sub_load_areas' property has been implicitly created by
    # the load_area' property of SubLoadArea.
    pass


