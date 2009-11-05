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

""" A component part of a system extending between adjacent substations or from a substation to an adjacent interconnection point. 
"""

# <<< imports
# @generated
from cdpsm.iec61970.core.equipment_container import EquipmentContainer

from cdpsm.iec61970.core.sub_geographical_region import SubGeographicalRegion


from google.appengine.ext import db
# >>> imports

class Line(EquipmentContainer):
    """ A component part of a system extending between adjacent substations or from a substation to an adjacent interconnection point. 
    """
    # <<< line.attributes
    # @generated
    # >>> line.attributes

    # <<< line.references
    # @generated
    # A Line can be contained by a SubGeographical Region. 
    region = db.ReferenceProperty(SubGeographicalRegion,
        collection_name="lines")

    # >>> line.references

    # <<< line.operations
    # @generated
    # >>> line.operations

# EOF -------------------------------------------------------------------------
