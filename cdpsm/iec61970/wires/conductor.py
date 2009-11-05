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

""" Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system. 
"""

# <<< imports
# @generated
from cdpsm.iec61970.core.conducting_equipment import ConductingEquipment


from cdpsm.iec61970.domain import Length

from google.appengine.ext import db
# >>> imports

class Conductor(ConductingEquipment):
    """ Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system. 
    """
    # <<< conductor.attributes
    # @generated
    # Segment length for calculating line section capabilities 
    length = Length

    # >>> conductor.attributes

    # <<< conductor.references
    # @generated
    # >>> conductor.references

    # <<< conductor.operations
    # @generated
    # >>> conductor.operations

# EOF -------------------------------------------------------------------------
