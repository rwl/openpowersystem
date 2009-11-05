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

""" A modeling construct to provide a root class for all Equipment classes 
"""

# <<< imports
# @generated
from cdpsm.iec61970.core.connectivity_node_container import ConnectivityNodeContainer



from google.appengine.ext import db
# >>> imports

class EquipmentContainer(ConnectivityNodeContainer):
    """ A modeling construct to provide a root class for all Equipment classes 
    """
    # <<< equipment_container.attributes
    # @generated
    # >>> equipment_container.attributes

    # <<< equipment_container.references
    # @generated
    # Virtual property. The association is used in the naming hierarchy. 
    pass # equipments

    # >>> equipment_container.references

    # <<< equipment_container.operations
    # @generated
    # >>> equipment_container.operations

# EOF -------------------------------------------------------------------------
