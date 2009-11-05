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
from cdpsm.iec61970.core.identified_object import IdentifiedObject

from cdpsm.iec61970.core.conducting_equipment import ConductingEquipment
from cdpsm.iec61970.topology.connectivity_node import ConnectivityNode


from google.appengine.ext import db
# >>> imports

class Terminal(IdentifiedObject):
    """ An electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called 'connectivity nodes'. 
    """
    # <<< terminal.attributes
    # @generated
    # The orientation of the terminal connections for a multiple terminal conducting equipment.  The sequence numbering starts with 1 and additional terminals should follow in increasing order.   The first terminal is the 'starting point' for a two terminal branch.   In the case of class TransformerWinding only one terminal is used so its sequenceNumber must be 1. 
    sequence_number = db.IntegerProperty()

    # The terminal connection status.   True implies the terminal is connected, and false implies the terminal is not connected. This is the result of topoplogical processing of a detailed Connectivity node and Switch model whether present in the model or not.   A terminal that is not connected cannot support a current flow.   A terminal that is connected may have flow.  In general a multi-terminal device may simultaneously have connected and disconnected terminals.  No other aspect of the algorithm 
    connected = db.BooleanProperty()

    # >>> terminal.attributes

    # <<< terminal.references
    # @generated
    # ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes 
    conducting_equipment = db.ReferenceProperty(ConductingEquipment,
        collection_name="terminals")

    # Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals. 
    connectivity_node = db.ReferenceProperty(ConnectivityNode,
        collection_name="terminals")

    # >>> terminal.references

    # <<< terminal.operations
    # @generated
    # >>> terminal.operations

# EOF -------------------------------------------------------------------------
