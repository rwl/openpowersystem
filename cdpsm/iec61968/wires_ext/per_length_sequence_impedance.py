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

""" Sequence impedance and admittance parameters per unit length, for transposed lines of 1, 2, or 3 phases. For 1-phase lines, define x=x0=xself. For 2-phase lines, define x=xs-xm and x0=xs+xm. 
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

class PerLengthSequenceImpedance(IdentifiedObject):
    """ Sequence impedance and admittance parameters per unit length, for transposed lines of 1, 2, or 3 phases. For 1-phase lines, define x=x0=xself. For 2-phase lines, define x=xs-xm and x0=xs+xm. 
    """
    # <<< per_length_sequence_impedance.attributes
    # @generated
    # Positive sequence series reactance, per unit of length. 
    x = Reactance

    # Positive sequence shunt (charging) conductance, per unit of length. 
    gch = Conductance

    # Zero sequence series resistance, per unit of length. 
    r0 = Resistance

    # Zero sequence series reactance, per unit of length. 
    x0 = Reactance

    # Zero sequence shunt (charging) conductance, per unit of length. 
    g0ch = Conductance

    # Zero sequence shunt (charging) susceptance, per unit of length. 
    b0ch = Susceptance

    # Positive sequence series resistance, per unit of length. 
    r = Resistance

    # Positive sequence shunt (charging) susceptance, per unit of length. 
    bch = Susceptance

    # >>> per_length_sequence_impedance.attributes

    # <<< per_length_sequence_impedance.references
    # @generated
    # Virtual property. All conductor segments described by this sequence impedance. 
    pass # conductor_segments

    # >>> per_length_sequence_impedance.references

    # <<< per_length_sequence_impedance.operations
    # @generated
    # >>> per_length_sequence_impedance.operations

# EOF -------------------------------------------------------------------------
