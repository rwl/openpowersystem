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

""" The schedule specialize RegularIntervalSchedule with type curve data for a specific type of day and season. This means that curves of this type cover a 24 hour period. 
"""

# <<< imports
# @generated
from cpsm.core.regular_interval_schedule import RegularIntervalSchedule

from cpsm.load_model.day_type import DayType
from cpsm.load_model.season import Season


from google.appengine.ext import db
# >>> imports

class SeasonDayTypeSchedule(RegularIntervalSchedule):
    """ The schedule specialize RegularIntervalSchedule with type curve data for a specific type of day and season. This means that curves of this type cover a 24 hour period. 
    """
    # <<< season_day_type_schedule.attributes
    # @generated
    # >>> season_day_type_schedule.attributes

    # <<< season_day_type_schedule.references
    # @generated
    # DayType for the Schedule. 
    day_type = db.ReferenceProperty(DayType,
        collection_name="season_day_type_schedules")

    # Season for the Schedule. 
    season = db.ReferenceProperty(Season,
        collection_name="season_day_type_schedules")

    # >>> season_day_type_schedule.references

    # <<< season_day_type_schedule.operations
    # @generated
    # >>> season_day_type_schedule.operations

# EOF -------------------------------------------------------------------------
