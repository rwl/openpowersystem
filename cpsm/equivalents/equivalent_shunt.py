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


# <<< imports
# @generated
from cpsm.equivalents.equivalent_equipment import EquivalentEquipment


from cpsm.domain import Susceptance
from cpsm.domain import Conductance

from google.appengine.ext import db
# >>> imports

class EquivalentShunt(EquivalentEquipment):
    """ The class represents equivalent shunts. 
    """
    # <<< equivalent_shunt.attributes
    # @generated
    # Positive sequence shunt susceptance. 
    b = Susceptance

    # Positive sequence shunt conductance. 
    g = Conductance

    # >>> equivalent_shunt.attributes

    # <<< equivalent_shunt.references
    # @generated
    # >>> equivalent_shunt.references

    # <<< equivalent_shunt.operations
    # @generated
    # >>> equivalent_shunt.operations

# EOF -------------------------------------------------------------------------
