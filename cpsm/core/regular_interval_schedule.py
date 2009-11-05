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

""" The schedule has TimePoints where the time between them is constant. 
"""

# <<< imports
# @generated
from cpsm.core.basic_interval_schedule import BasicIntervalSchedule


from cpsm.domain import Seconds

from google.appengine.ext import db
# >>> imports

class RegularIntervalSchedule(BasicIntervalSchedule):
    """ The schedule has TimePoints where the time between them is constant. 
    """
    # <<< regular_interval_schedule.attributes
    # @generated
    # The time for the last time point. 
    end_time = db.DateTimeProperty()

    # The time between each pair of subsequent RegularTimePoints. 
    time_step = Seconds

    # >>> regular_interval_schedule.attributes

    # <<< regular_interval_schedule.references
    # @generated
    # Virtual property. The point data values that define a curve  
    pass # time_points

    # >>> regular_interval_schedule.references

    # <<< regular_interval_schedule.operations
    # @generated
    # >>> regular_interval_schedule.operations

# EOF -------------------------------------------------------------------------
