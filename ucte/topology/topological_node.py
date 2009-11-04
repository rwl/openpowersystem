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

""" A set of connectivity nodes that, in the current network state, are connected together through any type of closed switches, including  jumpers. Topological nodes can change as the current network state changes (i.e., switches, breakers, etc. change state). 
"""

# <<< imports
from ucte.core.identified_object import IdentifiedObject

from ucte.control_area.control_area import ControlArea
from ucte.core.base_voltage import BaseVoltage
from ucte.topology.topological_island import TopologicalIsland
from ucte.core.connectivity_node_container import ConnectivityNodeContainer

from ucte.state_variables.sv_voltage import SvVoltage

from ucte.domain import ApparentPower

from google.appengine.ext import db
# >>> imports

class TopologicalNode(IdentifiedObject):
    """ A set of connectivity nodes that, in the current network state, are connected together through any type of closed switches, including  jumpers. Topological nodes can change as the current network state changes (i.e., switches, breakers, etc. change state). 
    """
    # <<< topological_node.attributes
    # @generated
    # The short circuit apparent power drawn at this node when faulted. This is for Short Circuit only. 
    s_short_circuit = ApparentPower

    # The topological node is equivalent and not real equipment. If this is missing, it is assumed to be False.  If it is an X-Node, this equivalent is required. 
    equivalent = db.BooleanProperty(default=False)

    # The ratio of zero sequence reactance per positive sequence reactance. This is for Short Circuit only. 
    x0_per_x = db.FloatProperty(default=0.0)

    # The ratio of zero sequence resistance to positive sequence resistance. This is for Short Circuit only. 
    r0_per_r = db.FloatProperty(default=0.0)

    # Ratio of positive sequence reactance per postive sequence resistance. This is for Short Circuit only. 
    x_per_r = db.FloatProperty(default=0.0)

    # >>> topological_node.attributes

    # <<< topological_node.references
    # The control area into which the node is included.
    control_area = db.ReferenceProperty(ControlArea, collection_name="topological_node")

    # The base voltage of the topologocial node. The base voltage of the TopologicalNode should match the BaseVoltage of the containing VoltageLevel if such a containing VoltageLevel is specified.
    base_voltage = db.ReferenceProperty(BaseVoltage, collection_name="topological_node")

    # The state voltage associated with the topological node.
    sv_voltage = db.ReferenceProperty(SvVoltage, collection_name="_topological_node_set")

    # A topological node belongs to a topological island
    topological_island = db.ReferenceProperty(TopologicalIsland, collection_name="topological_nodes")

    # The island for which the node is an angle reference.   Normally there is one angle reference node for each island.
    angle_ref_topological_island = db.ReferenceProperty(db.Model, collection_name="_topological_nodes")

    # The connectivity node container to which the toplogical node belongs. The TopologicalNode will normally belong only to a VoltageLevel instance within a Substation.   All instances of TopologicalNode that are not X-nodes will require an association to a containing VoltageLevel instance.  The BaseVoltage of the VoltageLevel should match that of the TopologicalNode itself. A TopologicalNode object used for an X-node will not be contained, thus this association is specified as optional in the profile.
    connectivity_node_container = db.ReferenceProperty(ConnectivityNodeContainer, collection_name="topological_node")

    # Virtual property. The terminals associated with the topological node.   This can be used as an alternative to the connectivity node path to terminal, thus making it unneccesary to model connedtivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would proably not be used.
    pass # terminal

    # >>> topological_node.references

    # <<< topological_node.operations
    # @generated
    # >>> topological_node.operations

# EOF -------------------------------------------------------------------------
