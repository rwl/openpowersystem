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

from cim14.iec61970.core import IdentifiedObject

from cim14.iec61970.domain import ActivePower
from cim14.iec61970.domain import AngleRadians
from cim14.iec61970.domain import Voltage
from cim14.iec61970.domain import ApparentPower
from cim14.iec61970.domain import ReactivePower

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

ns_prefix = "cim.IEC61970.Topology"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#IEC61970.Topology"

class BusNameMarker(IdentifiedObject):
    """ Used to apply user standard names to topology buses. Typically used for 'bus/branch' case generation. Associated with one or more ConnectivityNodes that are normally a part of the bus name.    The associated ConnectivityNodes are to be connected by non-retained switches. For a ring bus station configuration, all busbar connectivity nodes in the ring are typically associated.   For a breaker and a half scheme, both busbars would be associated.  For a ring bus, all busbars would be associated.  For a 'straight' busbar configuration, only the main connectivity node at the busbar would be associated.
    """

#    control_area = db.ReferenceProperty()
#    reporting_group = db.ReferenceProperty()
    # The 'connectivity_node' property has been implicitly created by
    # the bus_name_marker' property of ConnectivityNode.
    pass

class TopologicalNode(IdentifiedObject):
    """ A set of connectivity nodes that, in the current network state, are connected together through any type of closed switches, including  jumpers. Topological nodes can change as the current network state changes (i.e., switches, breakers, etc. change state).
    """

    # The observability status of the node.
    observability_flag = db.BooleanProperty()
    # Ratio of positive sequence reactance per postive sequence resistance.
    x_per_r = db.FloatProperty()
    # The ratio of zero sequence reactance per positive sequence reactance.
    x0_per_x = db.FloatProperty()
    # True if node is load carrying
    load_carrying = db.BooleanProperty()
    # Net injection active power
    net_injection_p = ActivePower
    # Phase angle of node
    phase_angle = AngleRadians
    # Voltage of node
    voltage = Voltage
    # The ratio of zero sequence resistance to positive sequence resistance.
    r0_per_r = db.FloatProperty()
    # The short circuit apparent power drawn at this node when faulted.
    s_short_circuit = ApparentPower
    # True if node energized
    energized = db.BooleanProperty()
    # Net injection reactive power
    net_injection_q = ReactivePower
#    angle_ref_topological_island = db.ReferenceProperty()
#    connectivity_node_container = db.ReferenceProperty()
    # The 'connectivity_nodes' property has been implicitly created by
    # the topological_node' property of ConnectivityNode.
    pass
#    sv_voltage = db.ReferenceProperty()
#    reporting_group = db.ReferenceProperty()
#    sv_injection = db.ReferenceProperty()
#    control_area = db.ReferenceProperty()
    # The 'terminal' property has been implicitly created by
    # the topological_node' property of Terminal.
    pass
#    topological_island = db.ReferenceProperty()

class TopologicalIsland(IdentifiedObject):
    """ An electrically connected subset of the network. Topological islands can change as the current network state changes (i.e., disconnect switches, breakers, etc. change state).
    """

    # The 'topological_nodes' property has been implicitly created by
    # the topological_island' property of TopologicalNode.
    pass
#    angle_ref_topological_node = db.ReferenceProperty()

class ConnectivityNode(IdentifiedObject):
    """ Connectivity nodes are points where terminals of conducting equipment are connected together with zero impedance.
    """

#    topological_node = db.ReferenceProperty()
#    connectivity_node_container = db.ReferenceProperty()
#    pnode = db.ReferenceProperty()
#    bus_name_marker = db.ReferenceProperty()
#    loss_penalty_factors = db.ListProperty(db.Key)

#    @property
#    def connectivity_nodes(self):
#        return LossPenaltyFactor.gql("WHERE loss_penalty_factors = :1", self.key())
    # The 'terminals' property has been implicitly created by
    # the connectivity_node' property of Terminal.
    pass
    # The 'node_constraint_terms' property has been implicitly created by
    # the connectivity_node' property of NodeConstraintTerm.
    pass


