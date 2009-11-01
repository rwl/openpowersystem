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


#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from cpsm.core import ConnectivityNodeContainer
from cpsm.core import ConductingEquipment

from cpsm.domain import Susceptance
from cpsm.domain import Conductance
from cpsm.domain import Reactance
from cpsm.domain import Resistance

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

#------------------------------------------------------------------------------
#  Properties:
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  Constants:
#------------------------------------------------------------------------------

NS_PREFIX = "cim"
NS_URI = "http://iec.ch/TC57/2008/CIM-schema-cim13#Package_Equivalents"

#------------------------------------------------------------------------------
#  "EquivalentNetwork" class:
#------------------------------------------------------------------------------

class EquivalentNetwork(ConnectivityNodeContainer):
    """ A class that represents an external meshed network that has been reduced to an electrically equivalent model. The ConnectivityNodes contained in the equivalent are intended to reflect internal nodes of the equivalent. The boundary Connectivity nodes where the equivalent connects outside itself are NOT contained by the equivalent.A class that represents an external meshed network that has been reduced to an electrically equivalent model. The ConnectivityNodes contained in the equivalent are intended to reflect internal nodes of the equivalent. The boundary Connectivity nodes where the equivalent connects outside itself are NOT contained by the equivalent.
    """

    
    # Virtual property. The associated reduced equivalents.The associated reduced equivalents.
    pass #equivalent_equipments

    # <<< equivalent_network
    # @generated
    # >>> equivalent_network


#------------------------------------------------------------------------------
#  "EquivalentEquipment" class:
#------------------------------------------------------------------------------

class EquivalentEquipment(ConductingEquipment):
    """ The class represents equivalent objects that are the result of a network reduction. The class is the base for equivalent objects of diferent types.The class represents equivalent objects that are the result of a network reduction. The class is the base for equivalent objects of diferent types.
    """

    
    # The equivalent where the reduced model belongs.The equivalent where the reduced model belongs.
    equivalent_network = db.ReferenceProperty(collection_name="equivalent_equipments")

    # <<< equivalent_equipment
    # @generated
    # >>> equivalent_equipment


#------------------------------------------------------------------------------
#  "EquivalentShunt" class:
#------------------------------------------------------------------------------

class EquivalentShunt(EquivalentEquipment):
    """ The class represents equivalent shunts.The class represents equivalent shunts.
    """

    
    # Positive sequence shunt susceptance.Positive sequence shunt susceptance.
    b = Susceptance

    # Positive sequence shunt conductance.Positive sequence shunt conductance.
    g = Conductance

    # <<< equivalent_shunt
    # @generated
    # >>> equivalent_shunt


#------------------------------------------------------------------------------
#  "EquivalentBranch" class:
#------------------------------------------------------------------------------

class EquivalentBranch(EquivalentEquipment):
    """ The class represents equivalent branches.The class represents equivalent branches.
    """

    
    # Positive sequence series reactance of the reduced branch.Positive sequence series reactance of the reduced branch.
    x = Reactance

    # Positive sequence series resistance of the reduced branch.Positive sequence series resistance of the reduced branch.
    r = Resistance

    # <<< equivalent_branch
    # @generated
    # >>> equivalent_branch




# EOF -------------------------------------------------------------------------
