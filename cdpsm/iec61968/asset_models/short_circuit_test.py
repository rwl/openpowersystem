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

""" Short-circuit test results include load losses and leakage impedances. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence. There must be at least one short-circuited ('to') winding. 
"""

# <<< imports
# @generated
from cdpsm.iec61968.asset_models.distribution_winding_test import DistributionWindingTest


from cdpsm.iec61970.domain import KWActivePower
from cdpsm.iec61970.domain import Impedance

from google.appengine.ext import db
# >>> imports

class ShortCircuitTest(DistributionWindingTest):
    """ Short-circuit test results include load losses and leakage impedances. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence. There must be at least one short-circuited ('to') winding. 
    """
    # <<< short_circuit_test.attributes
    # @generated
    # Load losses from a zero-sequence short-circuit test. 
    load_loss_zero = KWActivePower

    # Leakage impedance measured from a zero-sequence short-circuit test. 
    leakage_impedance_zero = Impedance

    # Leakage impedance measured from a positive-sequence or single-phase short-circuit test. 
    leakage_impedance = Impedance

    # Load losses from a positive-sequence or single-phase short-circuit test. 
    load_loss = KWActivePower

    # >>> short_circuit_test.attributes

    # <<< short_circuit_test.references
    # @generated
    shorted_winding_specs = db.ListProperty(db.Key)

    # >>> short_circuit_test.references

    # <<< short_circuit_test.operations
    # @generated
    # >>> short_circuit_test.operations

# EOF -------------------------------------------------------------------------
