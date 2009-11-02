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

""" This class represents the zero sequence line mutual coupling. This class is Optional and only used for Short Circuit. 
"""

# <<< imports
# @generated
from ucte.core.identified_object import IdentifiedObject

from ucte.core.terminal import Terminal
from ucte.core.terminal import Terminal

from ucte.domain import LongLength
from ucte.domain import Conductance
from ucte.domain import Resistance
from ucte.domain import Susceptance

from google.appengine.ext import db
# >>> imports

class MutualCoupling(IdentifiedObject):
    """ This class represents the zero sequence line mutual coupling. This class is Optional and only used for Short Circuit. 
    """
    # <<< mutual_coupling.attributes
    # @generated
    # Distance from the second line's specified terminal to end of coupled region Must be greater than the value of distance21 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number. 
    distance22 = LongLength

    # Zero sequence mutual coupling shunt (charging) conductance, uniformly distributed, of the entire line section. 
    g0ch = Conductance

    # Distance from the second line's specified terminal to start of coupled region Cannot be equal to distance22 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number. 
    distance21 = LongLength

    # Zero sequence branch-to-branch mutual impedance coupling, resistance 
    r0 = Resistance

    # Zero sequence mutual coupling shunt (charging) susceptance, uniformly distributed, of the entire line section. 
    b0ch = Susceptance

    # Zero sequence branch-to-branch mutual impedance coupling, reactance 
    x0 = Resistance

    # Distance from the first line's specified terminal to start of coupled region Cannot be equal to distance12 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number. 
    distance11 = LongLength

    # Distance from the first line's from specified terminal to end of coupled region Must be greater than the value of distance11 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number. 
    distance12 = LongLength

    # >>> mutual_coupling.attributes

    # <<< mutual_coupling.references
    # @generated
    # The starting terminal for the calculation of distances along the first branch of the mutual coupling.  Normally MutualCoupling would only be used for terminals of AC line segments.  The first and second terminals of a mutual coupling should point to different AC line segments. 
    first_terminal = db.ReferenceProperty(Terminal, collection_name="has_first_mutual_coupling")

    # The starting terminal for the calculation of distances along the second branch of the mutual coupling. 
    second_terminal = db.ReferenceProperty(Terminal, collection_name="has_second_mutual_coupling")

    # >>> mutual_coupling.references

    # <<< mutual_coupling.operations
    # @generated
    # >>> mutual_coupling.operations

# EOF -------------------------------------------------------------------------
