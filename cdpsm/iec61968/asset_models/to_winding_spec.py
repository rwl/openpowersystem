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

""" For short-circuit tests, specifies the winding and tap for all short-circuited windings.  For open-circuit tests, specifies the winding, tap, induced voltage, and induced angle for any non-excited windings that were measured during the test. This won't apply if only the exciting current and no-load losses were measured. 
"""

# <<< imports
# @generated
from cdpsm.iec61970.core.identified_object import IdentifiedObject

from cdpsm.iec61968.asset_models.winding_info import WindingInfo

from cdpsm.iec61970.domain import Voltage
from cdpsm.iec61970.domain import AngleDegrees

from google.appengine.ext import db
# >>> imports

class ToWindingSpec(IdentifiedObject):
    """ For short-circuit tests, specifies the winding and tap for all short-circuited windings.  For open-circuit tests, specifies the winding, tap, induced voltage, and induced angle for any non-excited windings that were measured during the test. This won't apply if only the exciting current and no-load losses were measured. 
    """
    # <<< to_winding_spec.attributes
    # @generated
    # Tap step number for the 'to' winding of the test pair. 
    to_tap_step = db.IntegerProperty()

    # (if open-circuit test) Voltage measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited. 
    voltage = Voltage

    # (if open-circuit test) Phase shift measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited. 
    phase_shift = AngleDegrees

    # >>> to_winding_spec.attributes

    # <<< to_winding_spec.references
    # @generated
    open_circuit_tests = db.ListProperty(db.Key)

    short_circuit_tests = db.ListProperty(db.Key)

    # Winding short-circuited in a short-circuit test, or measured for induced voltage and angle in an open-circuit test. 
    to_winding = db.ReferenceProperty(WindingInfo,
        collection_name="to_winding_specs")

    # >>> to_winding_spec.references

    # <<< to_winding_spec.operations
    # @generated
    # >>> to_winding_spec.operations

# EOF -------------------------------------------------------------------------
