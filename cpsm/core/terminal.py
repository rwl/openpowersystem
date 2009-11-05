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

""" An electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called 'connectivity nodes'. 
"""

# <<< imports
# @generated
from cpsm.core.identified_object import IdentifiedObject

from cpsm.topology.connectivity_node import ConnectivityNode
from cpsm.core.conducting_equipment import ConductingEquipment


from google.appengine.ext import db
# >>> imports

class Terminal(IdentifiedObject):
    """ An electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called 'connectivity nodes'. 
    """
    # <<< terminal.attributes
    # @generated
    # >>> terminal.attributes

    # <<< terminal.references
    # @generated
    # Virtual property. One or more measurements may be associated with a terminal in the network. Measurement-Terminal defines where the measurement is placed in the network topology. Some Measurements represent quantities related to a particular sensor position, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is captured by the Measurement - Terminal association that makes it possible to place the sensing position at a  well defined place. The place is defined by the connection of the Terminal to ConductingEquipment.  
    pass # measurements

    # Virtual property. The terminal is regulated by a control.  
    pass # regulating_control

    # Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals. 
    connectivity_node = db.ReferenceProperty(ConnectivityNode,
        collection_name="terminals")

    # ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes 
    conducting_equipment = db.ReferenceProperty(ConductingEquipment,
        collection_name="terminals")

    # >>> terminal.references

    # <<< terminal.operations
    # @generated
    # >>> terminal.operations

# EOF -------------------------------------------------------------------------
