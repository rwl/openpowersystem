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

""" Transformer Pi-model impedance that accurately reflects impedance for transformers with 2 or 3 windings. For transformers with 4 or more windings, you must use TransformerInfo. 
"""

# <<< imports
# @generated
from cdpsm.iec61970.core.identified_object import IdentifiedObject


from cdpsm.iec61970.domain import Reactance
from cdpsm.iec61970.domain import Conductance
from cdpsm.iec61970.domain import Resistance
from cdpsm.iec61970.domain import Susceptance

from google.appengine.ext import db
# >>> imports

class WindingPiImpedance(IdentifiedObject):
    """ Transformer Pi-model impedance that accurately reflects impedance for transformers with 2 or 3 windings. For transformers with 4 or more windings, you must use TransformerInfo. 
    """
    # <<< winding_pi_impedance.attributes
    # @generated
    # Positive sequence series reactance of the winding.  For a two winding transformer, the full reactance of the transformer should be entered on the primary (high voltage) winding. 
    x = Reactance

    # Magnetizing branch conductance (G mag). 
    g = Conductance

    # Zero sequence series resistance of the winding. 
    r0 = Resistance

    # DC resistance of the winding. 
    r = Resistance

    # Magnetizing branch susceptance (B mag).  The value can be positive or negative. 
    b = Susceptance

    # Zero sequence magnetizing branch conductance. 
    g0 = Conductance

    # Zero sequence series reactance of the winding. 
    x0 = Reactance

    # Zero sequence magnetizing branch susceptance. 
    b0 = Susceptance

    # >>> winding_pi_impedance.attributes

    # <<< winding_pi_impedance.references
    # @generated
    # Virtual property. All windings having this Pi impedance. 
    pass # windings

    # >>> winding_pi_impedance.references

    # <<< winding_pi_impedance.operations
    # @generated
    # >>> winding_pi_impedance.operations

# EOF -------------------------------------------------------------------------
