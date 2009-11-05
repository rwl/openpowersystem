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

""" Load that follows a daily and seasonal load variation pattern. 
"""

# <<< imports
# @generated
from cpsm.load_model.load_group import LoadGroup



from google.appengine.ext import db
# >>> imports

class ConformLoadGroup(LoadGroup):
    """ Load that follows a daily and seasonal load variation pattern. 
    """
    # <<< conform_load_group.attributes
    # @generated
    # >>> conform_load_group.attributes

    # <<< conform_load_group.references
    # @generated
    # Virtual property. Conform loads assigned to this ConformLoadGroup.  
    pass # energy_consumers

    # Virtual property. The ConformLoadSchedules in the ConformLoadGroup.  
    pass # conform_load_schedules

    # >>> conform_load_group.references

    # <<< conform_load_group.operations
    # @generated
    # >>> conform_load_group.operations

# EOF -------------------------------------------------------------------------
