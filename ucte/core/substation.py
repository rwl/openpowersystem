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

""" A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk is passed for the purposes of switching or modifying its characteristics. 
"""

# <<< imports
# @generated
from ucte.core.equipment_container import EquipmentContainer

from ucte.core.sub_geographical_region import SubGeographicalRegion


from google.appengine.ext import db
# >>> imports

class Substation(EquipmentContainer):
    """ A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk is passed for the purposes of switching or modifying its characteristics. 
    """
    # <<< substation.attributes
    # @generated
    # >>> substation.attributes

    # <<< substation.references
    # @generated
    # Virtual property. The association is used in the naming hierarchy.  
    pass # contains_voltage_levels

    # The association is used in the naming hierarchy. 
    region = db.ReferenceProperty(SubGeographicalRegion,
        collection_name="substations")

    # >>> substation.references

    # <<< substation.operations
    # @generated
    # >>> substation.operations

# EOF -------------------------------------------------------------------------
