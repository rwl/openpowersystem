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

""" Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system. 
"""

# <<< imports
# @generated
from ucte.core.conducting_equipment import ConductingEquipment


from ucte.domain import Susceptance
from ucte.domain import Resistance
from ucte.domain import Reactance
from ucte.domain import Conductance
from ucte.domain import LongLength

from google.appengine.ext import db
# >>> imports

class Conductor(ConductingEquipment):
    """ Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system. 
    """
    # <<< conductor.attributes
    # @generated
    # Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section. This is for Short Circuit only. 
    b0ch = Susceptance

    # Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section. 
    bch = Susceptance

    # Zero sequence series resistance of the entire line section. This is for Short Circuit only. 
    r0 = Resistance

    # Zero sequence series reactance of the entire line section. This is for Short Circuit only. 
    x0 = Reactance

    # Positive sequence shunt (charging) conductance, uniformly distributed, of the entire line section. This is for Short Circuit only. 
    gch = Conductance

    # Positive sequence series reactance of the entire line section. 
    x = Reactance

    # Segment length for calculating line section capabilities Required only for ACLineSegement objects involved in MutualCoupling. 
    length = LongLength

    # Positive sequence series resistance of the entire line section. 
    r = Resistance

    # Zero sequence shunt (charging) conductance, uniformly distributed, of the entire line section. This is for Short Circuit only. 
    g0ch = Conductance

    # >>> conductor.attributes

    # <<< conductor.references
    # @generated
    # >>> conductor.references

    # <<< conductor.operations
    # @generated
    # >>> conductor.operations

# EOF -------------------------------------------------------------------------
