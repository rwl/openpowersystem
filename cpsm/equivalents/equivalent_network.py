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


# <<< imports
# @generated
from cpsm.core.connectivity_node_container import ConnectivityNodeContainer



from google.appengine.ext import db
# >>> imports

class EquivalentNetwork(ConnectivityNodeContainer):
    """ A class that represents an external meshed network that has been reduced to an electrically equivalent model. The ConnectivityNodes contained in the equivalent are intended to reflect internal nodes of the equivalent. The boundary Connectivity nodes where the equivalent connects outside itself are NOT contained by the equivalent. 
    """
    # <<< equivalent_network.attributes
    # @generated
    # >>> equivalent_network.attributes

    # <<< equivalent_network.references
    # @generated
    # Virtual property. The associated reduced equivalents.  
    pass # equivalent_equipments

    # >>> equivalent_network.references

    # <<< equivalent_network.operations
    # @generated
    # >>> equivalent_network.operations

# EOF -------------------------------------------------------------------------
