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

""" Schedule of values at points in time. 
"""

# <<< imports
# @generated
from cpsm.core.identified_object import IdentifiedObject


from cpsm.domain import UnitSymbol

from google.appengine.ext import db
# >>> imports

class BasicIntervalSchedule(IdentifiedObject):
    """ Schedule of values at points in time. 
    """
    # <<< basic_interval_schedule.attributes
    # @generated
    # The time for the first time point. 
    start_time = db.DateTimeProperty()

    # Value1 units of measure. 
    value1_unit = UnitSymbol

    # Value2 units of measure. 
    value2_unit = UnitSymbol

    # >>> basic_interval_schedule.attributes

    # <<< basic_interval_schedule.references
    # @generated
    # >>> basic_interval_schedule.references

    # <<< basic_interval_schedule.operations
    # @generated
    # >>> basic_interval_schedule.operations

# EOF -------------------------------------------------------------------------
