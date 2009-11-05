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

""" Tape shield cable data. 
"""

# <<< imports
# @generated
from cdpsm.iec61968.asset_models.cable_info import CableInfo


from cdpsm.iec61970.domain import Length
from cdpsm.iec61970.domain import PerCent

from google.appengine.ext import db
# >>> imports

class TapeShieldCableInfo(CableInfo):
    """ Tape shield cable data. 
    """
    # <<< tape_shield_cable_info.attributes
    # @generated
    # Thickness of the tape shield, before wrapping. 
    tape_thickness = Length

    # Percentage of the tape shield width that overlaps in each wrap, typically 10% to 25%. 
    tape_lap = PerCent

    # >>> tape_shield_cable_info.attributes

    # <<< tape_shield_cable_info.references
    # @generated
    # >>> tape_shield_cable_info.references

    # <<< tape_shield_cable_info.operations
    # @generated
    # >>> tape_shield_cable_info.operations

# EOF -------------------------------------------------------------------------
