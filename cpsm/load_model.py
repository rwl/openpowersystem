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

""" This package is responsible for modeling the energy consumers and the system load as curves and associated curve data. Special circumstances that may affect the load, such as seasons and daytypes, are also included here.  This information is used by Load Forecasting and Load Management.This package is responsible for modeling the energy consumers and the system load as curves and associated curve data. Special circumstances that may affect the load, such as seasons and daytypes, are also included here.  This information is used by Load Forecasting and Load Management.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from cpsm.wires import EnergyConsumer
from cpsm.core import IdentifiedObject
from cpsm import Element
from cpsm.core import RegularIntervalSchedule


# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

#------------------------------------------------------------------------------
#  Properties:
#------------------------------------------------------------------------------

SeasonName = db.StringProperty(choices=("fall", "winter", "spring", "summer"))

#------------------------------------------------------------------------------
#  Constants:
#------------------------------------------------------------------------------

NS_PREFIX = "cim"
NS_URI = "http://iec.ch/TC57/2008/CIM-schema-cim13#Package_LoadModel"

#------------------------------------------------------------------------------
#  "NonConformLoad" class:
#------------------------------------------------------------------------------

class NonConformLoad(EnergyConsumer):
    """ NonConformLoad represent loads that do not follow a daily load change pattern and changes are not correlated with the daily load change pattern.NonConformLoad represent loads that do not follow a daily load change pattern and changes are not correlated with the daily load change pattern.
    """

    
    # Group of this ConformLoad.Group of this ConformLoad.
    load_group = db.ReferenceProperty(collection_name="energy_consumers")

    # <<< non_conform_load
    # @generated
    # >>> non_conform_load


#------------------------------------------------------------------------------
#  "DayType" class:
#------------------------------------------------------------------------------

class DayType(IdentifiedObject):
    """ Group of similar days, e.g., Mon/Tue/Wed, Thu/Fri, Sat/Sun, Holiday1, Holiday2Group of similar days, e.g., Mon/Tue/Wed, Thu/Fri, Sat/Sun, Holiday1, Holiday2
    """

    
    # Virtual property. Schedules that use this DayType.Schedules that use this DayType.
    pass #season_day_type_schedules

    # <<< day_type
    # @generated
    # >>> day_type


#------------------------------------------------------------------------------
#  "Season" class:
#------------------------------------------------------------------------------

class Season(Element):
    """ A specified time period of the year, e.g., Spring, Summer, Fall, WinterA specified time period of the year, e.g., Spring, Summer, Fall, Winter
    """

    
    # Date season endsDate season ends
    end_date = db.DateProperty()

    # Date season startsDate season starts
    start_date = db.DateProperty()

    # Name of the SeasonName of the Season
    name = SeasonName

    # Virtual property. Schedules that use this Season.Schedules that use this Season.
    pass #season_day_type_schedules

    # <<< season
    # @generated
    # >>> season


#------------------------------------------------------------------------------
#  "StationSupply" class:
#------------------------------------------------------------------------------

class StationSupply(EnergyConsumer):
    """ Station supply with load derived from the station output.Station supply with load derived from the station output.
    """

    pass
    # <<< station_supply
    # @generated
    # >>> station_supply


#------------------------------------------------------------------------------
#  "SeasonDayTypeSchedule" class:
#------------------------------------------------------------------------------

class SeasonDayTypeSchedule(RegularIntervalSchedule):
    """ The schedule specialize RegularIntervalSchedule with type curve data for a specific type of day and season. This means that curves of this type cover a 24 hour period.The schedule specialize RegularIntervalSchedule with type curve data for a specific type of day and season. This means that curves of this type cover a 24 hour period.
    """

    
    # DayType for the Schedule.DayType for the Schedule.
    day_type = db.ReferenceProperty(collection_name="season_day_type_schedules")

    # Season for the Schedule.Season for the Schedule.
    season = db.ReferenceProperty(collection_name="season_day_type_schedules")

    # <<< season_day_type_schedule
    # @generated
    # >>> season_day_type_schedule


#------------------------------------------------------------------------------
#  "LoadGroup" class:
#------------------------------------------------------------------------------

class LoadGroup(IdentifiedObject):
    """ The class is the third level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.The class is the third level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.
    """

    
    # The SubLoadArea where the Loadgroup belongs.The SubLoadArea where the Loadgroup belongs.
    sub_load_area = db.ReferenceProperty(collection_name="load_groups")

    # <<< load_group
    # @generated
    # >>> load_group


#------------------------------------------------------------------------------
#  "EnergyArea" class:
#------------------------------------------------------------------------------

class EnergyArea(IdentifiedObject):
    """ The class describes an area having energy production or consumption. The class is the basis for further specialization.The class describes an area having energy production or consumption. The class is the basis for further specialization.
    """

    
    # The control area specification that is used for the load forecast.The control area specification that is used for the load forecast.
    control_area = db.ReferenceProperty()

    # <<< energy_area
    # @generated
    # >>> energy_area


#------------------------------------------------------------------------------
#  "LoadResponseCharacteristic" class:
#------------------------------------------------------------------------------

class LoadResponseCharacteristic(IdentifiedObject):
    """ Models the characteristic response of the load demand due to to changes in system conditions such as voltage and frequency. This is not related to demand response.Models the characteristic response of the load demand due to to changes in system conditions such as voltage and frequency. This is not related to demand response.
    """

    
    # Exponent of per unit frequency effecting active powerExponent of per unit frequency effecting active power
    p_frequency_exponent = db.FloatProperty()

    # Exponent of per unit voltage effecting reactive power.   This model used only when 'useExponentModel' is true.Exponent of per unit voltage effecting reactive power.   This model used only when 'useExponentModel' is true.
    q_voltage_exponent = db.FloatProperty()

    # Exponent of per unit frequency effecting reactive powerExponent of per unit frequency effecting reactive power
    q_frequency_exponent = db.FloatProperty()

    # Exponent of per unit voltage effecting real power.   This model used only when 'useExponentModel' is true.Exponent of per unit voltage effecting real power.   This model used only when 'useExponentModel' is true.
    p_voltage_exponent = db.FloatProperty()

    # Virtual property. The set of loads that have the response characteristics.The set of loads that have the response characteristics.
    pass #energy_consumer

    # <<< load_response_characteristic
    # @generated
    # >>> load_response_characteristic


#------------------------------------------------------------------------------
#  "ConformLoad" class:
#------------------------------------------------------------------------------

class ConformLoad(EnergyConsumer):
    """ ConformLoad represent loads that follow a daily load change pattern where the pattern can be used to scale the load with a system load.ConformLoad represent loads that follow a daily load change pattern where the pattern can be used to scale the load with a system load.
    """

    
    # Group of this ConformLoad.Group of this ConformLoad.
    load_group = db.ReferenceProperty(collection_name="energy_consumers")

    # <<< conform_load
    # @generated
    # >>> conform_load


#------------------------------------------------------------------------------
#  "NonConformLoadGroup" class:
#------------------------------------------------------------------------------

class NonConformLoadGroup(LoadGroup):
    """ Loads that do not follow a daily and seasonal load variation pattern.Loads that do not follow a daily and seasonal load variation pattern.
    """

    
    # Virtual property. The NonConformLoadSchedules in the NonConformLoadGroup.The NonConformLoadSchedules in the NonConformLoadGroup.
    pass #non_conform_load_schedules

    # Virtual property. Conform loads assigned to this ConformLoadGroup.Conform loads assigned to this ConformLoadGroup.
    pass #energy_consumers

    # <<< non_conform_load_group
    # @generated
    # >>> non_conform_load_group


#------------------------------------------------------------------------------
#  "ConformLoadSchedule" class:
#------------------------------------------------------------------------------

class ConformLoadSchedule(SeasonDayTypeSchedule):
    """ A curve of load  versus time (X-axis) showing the active power values (Y1-axis) and reactive power (Y2-axis) for each unit of the period covered. This curve represents a typical pattern of load over the time period for a given day type and season.A curve of load  versus time (X-axis) showing the active power values (Y1-axis) and reactive power (Y2-axis) for each unit of the period covered. This curve represents a typical pattern of load over the time period for a given day type and season.
    """

    
    # The ConformLoadGroup where the ConformLoadSchedule belongs.The ConformLoadGroup where the ConformLoadSchedule belongs.
    conform_load_group = db.ReferenceProperty(collection_name="conform_load_schedules")

    # <<< conform_load_schedule
    # @generated
    # >>> conform_load_schedule


#------------------------------------------------------------------------------
#  "CustomerLoad" class:
#------------------------------------------------------------------------------

class CustomerLoad(ConformLoad):
    """ A meter for measuring customer energy consumption. The typeName attribute indicates the type of customer meter.A meter for measuring customer energy consumption. The typeName attribute indicates the type of customer meter.
    """

    pass
    # <<< customer_load
    # @generated
    # >>> customer_load


#------------------------------------------------------------------------------
#  "Load" class:
#------------------------------------------------------------------------------

class Load(ConformLoad):
    """ A generic equivalent for an energy consumer on a transmission or distribution voltage level. It may be under load management and also has cold load pick up characteristics.A generic equivalent for an energy consumer on a transmission or distribution voltage level. It may be under load management and also has cold load pick up characteristics.
    """

    pass
    # <<< load
    # @generated
    # >>> load


#------------------------------------------------------------------------------
#  "ConformLoadGroup" class:
#------------------------------------------------------------------------------

class ConformLoadGroup(LoadGroup):
    """ Load that follows a daily and seasonal load variation pattern.Load that follows a daily and seasonal load variation pattern.
    """

    
    # Virtual property. Conform loads assigned to this ConformLoadGroup.Conform loads assigned to this ConformLoadGroup.
    pass #energy_consumers

    # Virtual property. The ConformLoadSchedules in the ConformLoadGroup.The ConformLoadSchedules in the ConformLoadGroup.
    pass #conform_load_schedules

    # <<< conform_load_group
    # @generated
    # >>> conform_load_group


#------------------------------------------------------------------------------
#  "LoadArea" class:
#------------------------------------------------------------------------------

class LoadArea(EnergyArea):
    """ The class is the root or first level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.The class is the root or first level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.
    """

    
    # Virtual property. The SubLoadAreas in the LoadArea.The SubLoadAreas in the LoadArea.
    pass #sub_load_areas

    # <<< load_area
    # @generated
    # >>> load_area


#------------------------------------------------------------------------------
#  "SubLoadArea" class:
#------------------------------------------------------------------------------

class SubLoadArea(EnergyArea):
    """ The class is the second level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.The class is the second level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.
    """

    
    # Virtual property. The Loadgroups in the SubLoadArea.The Loadgroups in the SubLoadArea.
    pass #load_groups

    # The LoadArea where the SubLoadArea belongs.The LoadArea where the SubLoadArea belongs.
    load_area = db.ReferenceProperty(collection_name="sub_load_areas")

    # <<< sub_load_area
    # @generated
    # >>> sub_load_area


#------------------------------------------------------------------------------
#  "NonConformLoadSchedule" class:
#------------------------------------------------------------------------------

class NonConformLoadSchedule(SeasonDayTypeSchedule):
    """ An active power (Y1-axis) and reactive power (Y2-axis) schedule (curves) versus time (X-axis) for non-conforming loads, e.g., large industrial load or power station service (where modeled)An active power (Y1-axis) and reactive power (Y2-axis) schedule (curves) versus time (X-axis) for non-conforming loads, e.g., large industrial load or power station service (where modeled)
    """

    
    # The NonConformLoadGroup where the NonConformLoadSchedule belongs.The NonConformLoadGroup where the NonConformLoadSchedule belongs.
    non_conform_load_group = db.ReferenceProperty(collection_name="non_conform_load_schedules")

    # <<< non_conform_load_schedule
    # @generated
    # >>> non_conform_load_schedule


#------------------------------------------------------------------------------
#  "InductionMotorLoad" class:
#------------------------------------------------------------------------------

class InductionMotorLoad(NonConformLoad):
    """ Large three phase induction motor load. The typeName attribute indicates the type of induction motor (1 = wound rotor) (2 = squirrel cage).Large three phase induction motor load. The typeName attribute indicates the type of induction motor (1 = wound rotor) (2 = squirrel cage).
    """

    pass
    # <<< induction_motor_load
    # @generated
    # >>> induction_motor_load




# EOF -------------------------------------------------------------------------
