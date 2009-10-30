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

ns_prefix = "cim"
ns_uri = "http://iec.ch/TC57/2008/CIM-schema-cim13#Package_Equivalents"

class EquivalentNetwork(ConnectivityNodeContainer):
    """ A class that represents an external meshed network that has been reduced to an electrically equivalent model. The ConnectivityNodes contained in the equivalent are intended to reflect internal nodes of the equivalent. The boundary Connectivity nodes where the equivalent connects outside itself are NOT contained by the equivalent.
    """

#    equivalent_equipments = db.ReferenceProperty()

class EquivalentEquipment(ConductingEquipment):
    """ The class represents equivalent objects that are the result of a network reduction. The class is the base for equivalent objects of diferent types.
    """

#    equivalent_network = db.ReferenceProperty()

class EquivalentShunt(EquivalentEquipment):
    """ The class represents equivalent shunts.
    """

    # Positive sequence shunt susceptance.
    b = Susceptance
    # Positive sequence shunt conductance.
    g = Conductance

class EquivalentBranch(EquivalentEquipment):
    """ The class represents equivalent branches.
    """

    # Positive sequence series reactance of the reduced branch.
    x = Reactance
    # Positive sequence series resistance of the reduced branch.
    r = Resistance


