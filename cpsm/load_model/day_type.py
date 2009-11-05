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

""" Group of similar days, e.g., Mon/Tue/Wed, Thu/Fri, Sat/Sun, Holiday1, Holiday2 
"""

# <<< imports
# @generated
from cpsm.core.identified_object import IdentifiedObject



from google.appengine.ext import db
# >>> imports

class DayType(IdentifiedObject):
    """ Group of similar days, e.g., Mon/Tue/Wed, Thu/Fri, Sat/Sun, Holiday1, Holiday2 
    """
    # <<< day_type.attributes
    # @generated
    # >>> day_type.attributes

    # <<< day_type.references
    # @generated
    # Virtual property. Schedules that use this DayType.  
    pass # season_day_type_schedules

    # >>> day_type.references

    # <<< day_type.operations
    # @generated
    # >>> day_type.operations

# EOF -------------------------------------------------------------------------
