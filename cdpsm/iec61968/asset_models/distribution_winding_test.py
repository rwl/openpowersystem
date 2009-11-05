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

""" Test results for one or more transformer windings. These may include short-circuit or open-circuit (excitation) tests. Short-circuit test results include load losses and leakage impedances. Open-circuit test results may include no-load losses, exciting current, phase shifts, and induced voltage. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence. 
"""

# <<< imports
# @generated
from cdpsm.iec61970.core.identified_object import IdentifiedObject

from cdpsm.iec61968.asset_models.winding_info import WindingInfo


from google.appengine.ext import db
# >>> imports

class DistributionWindingTest(IdentifiedObject):
    """ Test results for one or more transformer windings. These may include short-circuit or open-circuit (excitation) tests. Short-circuit test results include load losses and leakage impedances. Open-circuit test results may include no-load losses, exciting current, phase shifts, and induced voltage. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence. 
    """
    # <<< distribution_winding_test.attributes
    # @generated
    # Tap step number for the 'from' winding of the test pair. 
    from_tap_step = db.IntegerProperty()

    # >>> distribution_winding_test.attributes

    # <<< distribution_winding_test.references
    # @generated
    # Winding that voltage or current is applied to during the test. 
    from_winding = db.ReferenceProperty(WindingInfo,
        collection_name="winding_tests")

    # >>> distribution_winding_test.references

    # <<< distribution_winding_test.operations
    # @generated
    # >>> distribution_winding_test.operations

# EOF -------------------------------------------------------------------------
