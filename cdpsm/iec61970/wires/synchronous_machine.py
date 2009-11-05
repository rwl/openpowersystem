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

""" An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump. 
"""

# <<< imports
# @generated
from cdpsm.iec61970.core.conducting_equipment import ConductingEquipment

from cdpsm.iec61970.generation.production.generating_unit import GeneratingUnit

from cdpsm.iec61970.domain import ReactivePower
from cdpsm.iec61970.wires import SynchronousMachineOperatingMode
from cdpsm.iec61970.wires import SynchronousMachineType

from google.appengine.ext import db
# >>> imports

class SynchronousMachine(ConductingEquipment):
    """ An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump. 
    """
    # <<< synchronous_machine.attributes
    # @generated
    # Default base reactive power value. This value represents the initial reactive power that can be used by any application function. 
    base_q = ReactivePower

    # Current mode of operation. 
    operating_mode = SynchronousMachineOperatingMode

    # Modes that this synchronous machine can operate in. 
    type = SynchronousMachineType

    # Maximum reactive power limit. This is the maximum (nameplate) limit for the unit. 
    max_q = ReactivePower

    # Minimum reactive power limit for the unit. 
    min_q = ReactivePower

    # >>> synchronous_machine.attributes

    # <<< synchronous_machine.references
    # @generated
    # A synchronous machine may operate as a generator and as such becomes a member of a generating unit 
    generating_unit = db.ReferenceProperty(GeneratingUnit,
        collection_name="synchronous_machines")

    # >>> synchronous_machine.references

    # <<< synchronous_machine.operations
    # @generated
    # >>> synchronous_machine.operations

# EOF -------------------------------------------------------------------------
