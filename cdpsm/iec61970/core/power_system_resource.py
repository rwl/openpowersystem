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

""" A power system resource can be an item of equipment such as a Switch, an EquipmentContainer containing many individual items of equipment such as a  Substation, or an organisational entity such as Company or SubControlArea.  This provides for the nesting of collections of PowerSystemResources within other PowerSystemResources. For example, a Switch could be a member of a Substation and a Substation could be a member of a division of a Company. 
"""

# <<< imports
# @generated
from cdpsm.iec61970.core.identified_object import IdentifiedObject

from cdpsm.iec61968.common.geo_location import GeoLocation
from cdpsm.iec61970.core.psrtype import PSRType


from google.appengine.ext import db
# >>> imports

class PowerSystemResource(IdentifiedObject):
    """ A power system resource can be an item of equipment such as a Switch, an EquipmentContainer containing many individual items of equipment such as a  Substation, or an organisational entity such as Company or SubControlArea.  This provides for the nesting of collections of PowerSystemResources within other PowerSystemResources. For example, a Switch could be a member of a Substation and a Substation could be a member of a division of a Company. 
    """
    # <<< power_system_resource.attributes
    # @generated
    # >>> power_system_resource.attributes

    # <<< power_system_resource.references
    # @generated
    # Geographical location of this power system resource. 
    geo_location = db.ReferenceProperty(GeoLocation,
        collection_name="power_system_resources")

    # PSRType (custom classification) for this PowerSystemResource. 
    psrtype = db.ReferenceProperty(PSRType,
        collection_name="power_system_resources")

    # >>> power_system_resource.references

    # <<< power_system_resource.operations
    # @generated
    # >>> power_system_resource.operations

# EOF -------------------------------------------------------------------------
