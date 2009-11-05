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

""" RegulatingCondEq is a type of ConductingEquipment that can regulate Measurements and have a RegulationSchedule. 
"""

# <<< imports
# @generated
from cpsm.core.conducting_equipment import ConductingEquipment

from cpsm.wires.regulating_control import RegulatingControl


from google.appengine.ext import db
# >>> imports

class RegulatingCondEq(ConductingEquipment):
    """ RegulatingCondEq is a type of ConductingEquipment that can regulate Measurements and have a RegulationSchedule. 
    """
    # <<< regulating_cond_eq.attributes
    # @generated
    # >>> regulating_cond_eq.attributes

    # <<< regulating_cond_eq.references
    # @generated
    # copy from ... 
    regulating_control = db.ReferenceProperty(RegulatingControl,
        collection_name="regulating_cond_eq")

    # >>> regulating_cond_eq.references

    # <<< regulating_cond_eq.operations
    # @generated
    # >>> regulating_cond_eq.operations

# EOF -------------------------------------------------------------------------
