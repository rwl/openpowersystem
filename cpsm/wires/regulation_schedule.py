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

""" A pre-established pattern over time for a controlled variable, e.g., busbar voltage. 
"""

# <<< imports
# @generated
from cpsm.core.regular_interval_schedule import RegularIntervalSchedule



from google.appengine.ext import db
# >>> imports

class RegulationSchedule(RegularIntervalSchedule):
    """ A pre-established pattern over time for a controlled variable, e.g., busbar voltage. 
    """
    # <<< regulation_schedule.attributes
    # @generated
    # >>> regulation_schedule.attributes

    # <<< regulation_schedule.references
    # @generated
    # Virtual property. Regulating controls that have this Schedule.  
    pass # regulating_control

    # >>> regulation_schedule.references

    # <<< regulation_schedule.operations
    # @generated
    # >>> regulation_schedule.operations

# EOF -------------------------------------------------------------------------
