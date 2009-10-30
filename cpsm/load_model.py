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
""" This package is responsible for modeling the energy consumers and the system load as curves and associated curve data. Special circumstances that may affect the load, such as seasons and daytypes, are also included here.  This information is used by Load Forecasting and Load Management.
"""

from cpsm.wires import EnergyConsumer
from cpsm.core import IdentifiedObject
from cpsm import Element
from cpsm.core import RegularIntervalSchedule


# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

SeasonName = db.StringProperty(choices=("fall", "winter", "spring", "summer"))

ns_prefix = "cim"
ns_uri = "http://iec.ch/TC57/2008/CIM-schema-cim13#Package_LoadModel"

class NonConformLoad(EnergyConsumer):
    """ NonConformLoad represent loads that do not follow a daily load change pattern and changes are not correlated with the daily load change pattern.
    """

#    load_group = db.ReferenceProperty()

class DayType(IdentifiedObject):
    """ Group of similar days, e.g., Mon/Tue/Wed, Thu/Fri, Sat/Sun, Holiday1, Holiday2
    """

#    season_day_type_schedules = db.ReferenceProperty()

class Season(Element):
    """ A specified time period of the year, e.g., Spring, Summer, Fall, Winter
    """

    # Date season ends
    end_date = db.DateProperty()
    # Date season starts
    start_date = db.DateProperty()
    # Name of the Season
    name = SeasonName
#    season_day_type_schedules = db.ReferenceProperty()

class StationSupply(EnergyConsumer):
    """ Station supply with load derived from the station output.
    """

    pass

class SeasonDayTypeSchedule(RegularIntervalSchedule):
    """ The schedule specialize RegularIntervalSchedule with type curve data for a specific type of day and season. This means that curves of this type cover a 24 hour period.
    """

#    day_type = db.ReferenceProperty()
#    season = db.ReferenceProperty()

class LoadGroup(IdentifiedObject):
    """ The class is the third level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.
    """

#    sub_load_area = db.ReferenceProperty()

class EnergyArea(IdentifiedObject):
    """ The class describes an area having energy production or consumption. The class is the basis for further specialization.
    """

#    control_area = db.ReferenceProperty()

class LoadResponseCharacteristic(IdentifiedObject):
    """ Models the characteristic response of the load demand due to to changes in system conditions such as voltage and frequency. This is not related to demand response.
    """

    # Exponent of per unit frequency effecting active power
    p_frequency_exponent = db.FloatProperty()
    # Exponent of per unit voltage effecting reactive power.   This model used only when 'useExponentModel' is true.
    q_voltage_exponent = db.FloatProperty()
    # Exponent of per unit frequency effecting reactive power
    q_frequency_exponent = db.FloatProperty()
    # Exponent of per unit voltage effecting real power.   This model used only when 'useExponentModel' is true.
    p_voltage_exponent = db.FloatProperty()
#    energy_consumer = db.ReferenceProperty()

class ConformLoad(EnergyConsumer):
    """ ConformLoad represent loads that follow a daily load change pattern where the pattern can be used to scale the load with a system load.
    """

#    load_group = db.ReferenceProperty()

class NonConformLoadGroup(LoadGroup):
    """ Loads that do not follow a daily and seasonal load variation pattern.
    """

#    non_conform_load_schedules = db.ReferenceProperty()
#    energy_consumers = db.ReferenceProperty()

class ConformLoadSchedule(SeasonDayTypeSchedule):
    """ A curve of load  versus time (X-axis) showing the active power values (Y1-axis) and reactive power (Y2-axis) for each unit of the period covered. This curve represents a typical pattern of load over the time period for a given day type and season.
    """

#    conform_load_group = db.ReferenceProperty()

class CustomerLoad(ConformLoad):
    """ A meter for measuring customer energy consumption. The typeName attribute indicates the type of customer meter.
    """

    pass

class Load(ConformLoad):
    """ A generic equivalent for an energy consumer on a transmission or distribution voltage level. It may be under load management and also has cold load pick up characteristics.
    """

    pass

class ConformLoadGroup(LoadGroup):
    """ Load that follows a daily and seasonal load variation pattern.
    """

#    energy_consumers = db.ReferenceProperty()
#    conform_load_schedules = db.ReferenceProperty()

class LoadArea(EnergyArea):
    """ The class is the root or first level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.
    """

#    sub_load_areas = db.ReferenceProperty()

class SubLoadArea(EnergyArea):
    """ The class is the second level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.
    """

#    load_groups = db.ReferenceProperty()
#    load_area = db.ReferenceProperty()

class NonConformLoadSchedule(SeasonDayTypeSchedule):
    """ An active power (Y1-axis) and reactive power (Y2-axis) schedule (curves) versus time (X-axis) for non-conforming loads, e.g., large industrial load or power station service (where modeled)
    """

#    non_conform_load_group = db.ReferenceProperty()

class InductionMotorLoad(NonConformLoad):
    """ Large three phase induction motor load. The typeName attribute indicates the type of induction motor (1 = wound rotor) (2 = squirrel cage).
    """

    pass


