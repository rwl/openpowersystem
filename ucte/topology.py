# Copyright (C) 2009 Richard W. Lincoln
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation; version 2 dated June, 1991.
#
# This software is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANDABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
""" An extension to the Core Package that in association with the Terminal class models Connectivity, that is the physical definition of how equipment is connected together. In addition it models Topology, that is the logical definition of how equipment is connected via closed switches. The Topology definition is independent of the other electrical characteristics.An extension to the Core Package that in association with the Terminal class models Connectivity, that is the physical definition of how equipment is connected together. In addition it models Topology, that is the logical definition of how equipment is connected via closed switches. The Topology definition is independent of the other electrical characteristics.
"""

from ucte.core import IdentifiedObject

from ucte.domain import ApparentPower

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

ns_prefix = "cim"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_Topology"

class TopologicalNode(IdentifiedObject):
    """ A set of connectivity nodes that, in the current network state, are connected together through any type of closed switches, including  jumpers. Topological nodes can change as the current network state changes (i.e., switches, breakers, etc. change state).A set of connectivity nodes that, in the current network state, are connected together through any type of closed switches, including  jumpers. Topological nodes can change as the current network state changes (i.e., switches, breakers, etc. change state).
    """

    # The short circuit apparent power drawn at this node when faulted.This is for Short Circuit only.The short circuit apparent power drawn at this node when faulted.This is for Short Circuit only.
    s_short_circuit = ApparentPower
    # The topological node is equivalent and not real equipment.If this is missing, it is assumed to be False.  If it is an X-Node, this equivalent is required.The topological node is equivalent and not real equipment.If this is missing, it is assumed to be False.  If it is an X-Node, this equivalent is required.
    equivalent = db.BooleanProperty()
    # The ratio of zero sequence reactance per positive sequence reactance.This is for Short Circuit only.The ratio of zero sequence reactance per positive sequence reactance.This is for Short Circuit only.
    x0_per_x = db.FloatProperty()
    # The ratio of zero sequence resistance to positive sequence resistance.This is for Short Circuit only.The ratio of zero sequence resistance to positive sequence resistance.This is for Short Circuit only.
    r0_per_r = db.FloatProperty()
    # Ratio of positive sequence reactance per postive sequence resistance.This is for Short Circuit only.Ratio of positive sequence reactance per postive sequence resistance.This is for Short Circuit only.
    x_per_r = db.FloatProperty()
#    control_area = db.ReferenceProperty()
#    base_voltage = db.ReferenceProperty()
#    sv_voltage = db.ReferenceProperty()
#    topological_island = db.ReferenceProperty()
#    angle_ref_topological_island = db.ReferenceProperty()
#    connectivity_node_container = db.ReferenceProperty()
    # The 'terminal' property has been implicitly created by
    # the topological_node' property of Terminal.
    pass

class TopologicalIsland(IdentifiedObject):
    """ An electrically connected subset of the network. Topological islands can change as the current network state changes (i.e., disconnect switches, breakers, etc. change state).An electrically connected subset of the network. Topological islands can change as the current network state changes (i.e., disconnect switches, breakers, etc. change state).
    """

    # The 'topological_nodes' property has been implicitly created by
    # the topological_island' property of TopologicalNode.
    pass
#    angle_ref_topological_node = db.ReferenceProperty()


