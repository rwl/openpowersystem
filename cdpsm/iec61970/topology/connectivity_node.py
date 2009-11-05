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

""" Connectivity nodes are points where terminals of conducting equipment are connected together with zero impedance. 
"""

# <<< imports
# @generated
from cdpsm.iec61970.core.identified_object import IdentifiedObject

from cdpsm.iec61970.core.connectivity_node_container import ConnectivityNodeContainer


from google.appengine.ext import db
# >>> imports

class ConnectivityNode(IdentifiedObject):
    """ Connectivity nodes are points where terminals of conducting equipment are connected together with zero impedance. 
    """
    # <<< connectivity_node.attributes
    # @generated
    # >>> connectivity_node.attributes

    # <<< connectivity_node.references
    # @generated
    # Virtual property. Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.  
    pass # terminals

    # Container of this connectivity node. 
    connectivity_node_container = db.ReferenceProperty(ConnectivityNodeContainer,
        collection_name="connectivity_nodes")

    # >>> connectivity_node.references

    # <<< connectivity_node.operations
    # @generated
    # >>> connectivity_node.operations

# EOF -------------------------------------------------------------------------
