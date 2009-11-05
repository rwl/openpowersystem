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

""" Open-circuit test results may include no-load losses, exciting current, phase shifts, and induced voltage. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence. For induced voltage and phase shifts, use the associated ToWindingSpec class. 
"""

# <<< imports
# @generated
from cdpsm.iec61968.asset_models.distribution_winding_test import DistributionWindingTest


from cdpsm.iec61970.domain import KWActivePower
from cdpsm.iec61970.domain import PerCent

from google.appengine.ext import db
# >>> imports

class OpenCircuitTest(DistributionWindingTest):
    """ Open-circuit test results may include no-load losses, exciting current, phase shifts, and induced voltage. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence. For induced voltage and phase shifts, use the associated ToWindingSpec class. 
    """
    # <<< open_circuit_test.attributes
    # @generated
    # Losses measured from a zero-sequence open-circuit (excitation) test. 
    no_load_loss_zero = KWActivePower

    # Losses measured from a positive-sequence or single-phase open-circuit (excitation) test. 
    no_load_loss = KWActivePower

    # Exciting current measured from a positive-sequence or single-phase open-circuit (excitation) test. 
    exciting_current = PerCent

    # Exciting current measured from a zero-sequence open-circuit (excitation) test. 
    exciting_current_zero = PerCent

    # >>> open_circuit_test.attributes

    # <<< open_circuit_test.references
    # @generated
    measured_winding_specs = db.ListProperty(db.Key)

    # >>> open_circuit_test.references

    # <<< open_circuit_test.operations
    # @generated
    # >>> open_circuit_test.operations

# EOF -------------------------------------------------------------------------
