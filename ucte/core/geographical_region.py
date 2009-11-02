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

""" A geographical region of a power system network model. 
"""

# <<< imports
# @generated
from ucte.core.identified_object import IdentifiedObject



from google.appengine.ext import db
# >>> imports

class GeographicalRegion(IdentifiedObject):
    """ A geographical region of a power system network model. 
    """
    # <<< geographical_region.attributes
    # @generated
    # >>> geographical_region.attributes

    # <<< geographical_region.references
    # @generated
    # Virtual property. The association is used in the naming hierarchy.  
    pass # regions

    # >>> geographical_region.references

    # <<< geographical_region.operations
    # @generated
    # >>> geographical_region.operations

# EOF -------------------------------------------------------------------------
