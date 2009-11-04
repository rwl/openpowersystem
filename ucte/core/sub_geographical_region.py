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

""" A subset of a geographical region of a power system network model. 
"""

# <<< imports
# @generated
from ucte.core.identified_object import IdentifiedObject

from ucte.core.geographical_region import GeographicalRegion


from google.appengine.ext import db
# >>> imports

class SubGeographicalRegion(IdentifiedObject):
    """ A subset of a geographical region of a power system network model. 
    """
    # <<< sub_geographical_region.attributes
    # @generated
    # >>> sub_geographical_region.attributes

    # <<< sub_geographical_region.references
    # @generated
    # Virtual property. The association is used in the naming hierarchy.  
    pass # substations

    # The association is used in the naming hierarchy. 
    region = db.ReferenceProperty(GeographicalRegion,
        collection_name="regions")

    # >>> sub_geographical_region.references

    # <<< sub_geographical_region.operations
    # @generated
    # >>> sub_geographical_region.operations

# EOF -------------------------------------------------------------------------
