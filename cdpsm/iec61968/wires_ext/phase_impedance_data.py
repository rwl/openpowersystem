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

""" Triplet of resistance, reactance, and susceptance matrix element values. 
"""

# <<< imports
# @generated
from cdpsm.element import Element

from cdpsm.iec61968.wires_ext.per_length_phase_impedance import PerLengthPhaseImpedance

from cdpsm.iec61970.domain import Reactance
from cdpsm.iec61970.domain import Susceptance
from cdpsm.iec61970.domain import Resistance

from google.appengine.ext import db
# >>> imports

class PhaseImpedanceData(Element):
    """ Triplet of resistance, reactance, and susceptance matrix element values. 
    """
    # <<< phase_impedance_data.attributes
    # @generated
    # Reactance matrix element value, per length of unit. 
    x = Reactance

    # Column-wise element index, assuming a symmetrical matrix. Ranges from 1 to N + N*(N-1)/2. 
    sequence_number = db.IntegerProperty()

    # Susceptance matrix element value, per length of unit. 
    b = Susceptance

    # Resistance matrix element value, per length of unit. 
    r = Resistance

    # >>> phase_impedance_data.attributes

    # <<< phase_impedance_data.references
    # @generated
    # Conductor phase impedance to which this data belongs. 
    phase_impedance = db.ReferenceProperty(PerLengthPhaseImpedance,
        collection_name="phase_impedance_data")

    # >>> phase_impedance_data.references

    # <<< phase_impedance_data.operations
    # @generated
    # >>> phase_impedance_data.operations

# EOF -------------------------------------------------------------------------
