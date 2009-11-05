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

""" TimePoints for a schedule where the time between the points is constant. 
"""

# <<< imports
# @generated
from cpsm.element import Element

from cpsm.core.regular_interval_schedule import RegularIntervalSchedule


from google.appengine.ext import db
# >>> imports

class RegularTimePoint(Element):
    """ TimePoints for a schedule where the time between the points is constant. 
    """
    # <<< regular_time_point.attributes
    # @generated
    # The first value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule. 
    value1 = db.FloatProperty()

    # The position of the RegularTimePoint in the sequence. Note that time points don't have to be sequential, i.e. time points may be omitted. The actual time for a RegularTimePoint is computed by multiplying the RegularIntervalSchedule.timeStep with the RegularTimePoint.sequenceNumber and add the BasicIntervalSchedule.startTime. 
    sequence_number = db.IntegerProperty()

    # The second value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule. 
    value2 = db.FloatProperty()

    # >>> regular_time_point.attributes

    # <<< regular_time_point.references
    # @generated
    # A RegularTimePoint belongs to a RegularIntervalSchedule. 
    interval_schedule = db.ReferenceProperty(RegularIntervalSchedule,
        collection_name="time_points")

    # >>> regular_time_point.references

    # <<< regular_time_point.operations
    # @generated
    # >>> regular_time_point.operations

# EOF -------------------------------------------------------------------------
