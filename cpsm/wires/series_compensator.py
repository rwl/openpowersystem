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

""" A Series Compensator is a series capacitor or reactor or an AC transmission line without charging susceptance. 
"""

# <<< imports
# @generated
from cpsm.core.conducting_equipment import ConductingEquipment


from cpsm.domain import Resistance
from cpsm.domain import Reactance

from google.appengine.ext import db
# >>> imports

class SeriesCompensator(ConductingEquipment):
    """ A Series Compensator is a series capacitor or reactor or an AC transmission line without charging susceptance. 
    """
    # <<< series_compensator.attributes
    # @generated
    # Positive sequence resistance. 
    r = Resistance

    # Positive sequence reactance. 
    x = Reactance

    # >>> series_compensator.attributes

    # <<< series_compensator.references
    # @generated
    # >>> series_compensator.references

    # <<< series_compensator.operations
    # @generated
    # >>> series_compensator.operations

# EOF -------------------------------------------------------------------------
