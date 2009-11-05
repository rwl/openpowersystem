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

""" An active power (Y1-axis) and reactive power (Y2-axis) schedule (curves) versus time (X-axis) for non-conforming loads, e.g., large industrial load or power station service (where modeled) 
"""

# <<< imports
# @generated
from cpsm.load_model.season_day_type_schedule import SeasonDayTypeSchedule

from cpsm.load_model.non_conform_load_group import NonConformLoadGroup


from google.appengine.ext import db
# >>> imports

class NonConformLoadSchedule(SeasonDayTypeSchedule):
    """ An active power (Y1-axis) and reactive power (Y2-axis) schedule (curves) versus time (X-axis) for non-conforming loads, e.g., large industrial load or power station service (where modeled) 
    """
    # <<< non_conform_load_schedule.attributes
    # @generated
    # >>> non_conform_load_schedule.attributes

    # <<< non_conform_load_schedule.references
    # @generated
    # The NonConformLoadGroup where the NonConformLoadSchedule belongs. 
    non_conform_load_group = db.ReferenceProperty(NonConformLoadGroup,
        collection_name="non_conform_load_schedules")

    # >>> non_conform_load_schedule.references

    # <<< non_conform_load_schedule.operations
    # @generated
    # >>> non_conform_load_schedule.operations

# EOF -------------------------------------------------------------------------
