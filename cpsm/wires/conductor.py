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
from cpsm.core.conducting_equipment import ConductingEquipment


from cpsm.domain import Resistance
from cpsm.domain import Reactance
from cpsm.domain import Susceptance

from google.appengine.ext import db
# >>> imports

class Conductor(ConductingEquipment):
    """ Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system. 
    """
    # <<< conductor.attributes
    # @generated
    # Positive sequence series resistance of the entire line section. 
    r = Resistance

    # Positive sequence series reactance of the entire line section. 
    x = Reactance

    # Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section. 
    bch = Susceptance

    # >>> conductor.attributes

    # <<< conductor.references
    # @generated
    # >>> conductor.references

    # <<< conductor.operations
    # @generated
    # >>> conductor.operations

# EOF -------------------------------------------------------------------------
