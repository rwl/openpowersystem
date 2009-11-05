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

""" A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set. 
"""

# <<< imports
# @generated
from cdpsm.iec61970.core.equipment import Equipment


from cdpsm.iec61970.domain import ActivePower
from cdpsm.iec61970.generation.production import GeneratorControlSource

from google.appengine.ext import db
# >>> imports

class GeneratingUnit(Equipment):
    """ A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set. 
    """
    # <<< generating_unit.attributes
    # @generated
    # The net rated maximum capacity determined by subtracting the auxiliary power used to operate the internal plant machinery from the rated gross maximum capacity 
    rated_net_max_p = ActivePower

    # The source of controls for a generating unit. 
    gen_control_source = GeneratorControlSource

    # Default Initial active power  which is used to store a powerflow result for the initial active power for this unit in this network configuration 
    initial_p = ActivePower

    # >>> generating_unit.attributes

    # <<< generating_unit.references
    # @generated
    # Virtual property. A synchronous machine may operate as a generator and as such becomes a member of a generating unit  
    pass # synchronous_machines

    # >>> generating_unit.references

    # <<< generating_unit.operations
    # @generated
    # >>> generating_unit.operations

# EOF -------------------------------------------------------------------------
