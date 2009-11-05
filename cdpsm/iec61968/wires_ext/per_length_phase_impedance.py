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

""" Impedance and admittance parameters per unit length for n-wire unbalanced lines, in matrix form. 
"""

# <<< imports
# @generated
from cdpsm.iec61970.core.identified_object import IdentifiedObject



from google.appengine.ext import db
# >>> imports

class PerLengthPhaseImpedance(IdentifiedObject):
    """ Impedance and admittance parameters per unit length for n-wire unbalanced lines, in matrix form. 
    """
    # <<< per_length_phase_impedance.attributes
    # @generated
    # Number of phase, neutral, and other wires retained. Constrains the number of matrix elements and the phase codes that can be used with this matrix. 
    conductor_count = db.IntegerProperty()

    # >>> per_length_phase_impedance.attributes

    # <<< per_length_phase_impedance.references
    # @generated
    # Virtual property. All data that belong to this conductor phase impedance.  
    pass # phase_impedance_data

    # Virtual property. All conductor segments described by this phase impedance. 
    pass # conductor_segments

    # >>> per_length_phase_impedance.references

    # <<< per_length_phase_impedance.operations
    # @generated
    # >>> per_length_phase_impedance.operations

# EOF -------------------------------------------------------------------------
