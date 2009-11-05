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

""" A curve of load  versus time (X-axis) showing the active power values (Y1-axis) and reactive power (Y2-axis) for each unit of the period covered. This curve represents a typical pattern of load over the time period for a given day type and season. 
"""

# <<< imports
# @generated
from cpsm.load_model.season_day_type_schedule import SeasonDayTypeSchedule

from cpsm.load_model.conform_load_group import ConformLoadGroup


from google.appengine.ext import db
# >>> imports

class ConformLoadSchedule(SeasonDayTypeSchedule):
    """ A curve of load  versus time (X-axis) showing the active power values (Y1-axis) and reactive power (Y2-axis) for each unit of the period covered. This curve represents a typical pattern of load over the time period for a given day type and season. 
    """
    # <<< conform_load_schedule.attributes
    # @generated
    # >>> conform_load_schedule.attributes

    # <<< conform_load_schedule.references
    # @generated
    # The ConformLoadGroup where the ConformLoadSchedule belongs. 
    conform_load_group = db.ReferenceProperty(ConformLoadGroup,
        collection_name="conform_load_schedules")

    # >>> conform_load_schedule.references

    # <<< conform_load_schedule.operations
    # @generated
    # >>> conform_load_schedule.operations

# EOF -------------------------------------------------------------------------
