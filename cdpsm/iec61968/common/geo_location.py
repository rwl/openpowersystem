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

""" Geographical location. 
"""

# <<< imports
# @generated
from cdpsm.iec61968.common.location import Location



from google.appengine.ext import db
# >>> imports

class GeoLocation(Location):
    """ Geographical location. 
    """
    # <<< geo_location.attributes
    # @generated
    # >>> geo_location.attributes

    # <<< geo_location.references
    # @generated
    # Virtual property. All power system resources at this geographical location.  
    pass # power_system_resources

    # >>> geo_location.references

    # <<< geo_location.operations
    # @generated
    # >>> geo_location.operations

# EOF -------------------------------------------------------------------------
