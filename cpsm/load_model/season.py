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

""" A specified time period of the year, e.g., Spring, Summer, Fall, Winter 
"""

# <<< imports
# @generated
from cpsm.element import Element


from cpsm.load_model import SeasonName

from google.appengine.ext import db
# >>> imports

class Season(Element):
    """ A specified time period of the year, e.g., Spring, Summer, Fall, Winter 
    """
    # <<< season.attributes
    # @generated
    # Date season ends 
    end_date = db.DateTimeProperty()

    # Date season starts 
    start_date = db.DateTimeProperty()

    # Name of the Season 
    name = SeasonName

    # >>> season.attributes

    # <<< season.references
    # @generated
    # Virtual property. Schedules that use this Season.  
    pass # season_day_type_schedules

    # >>> season.references

    # <<< season.operations
    # @generated
    # >>> season.operations

# EOF -------------------------------------------------------------------------
