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

""" A generic device designed to close, or open, or both, one or more electric circuits. 
"""

# <<< imports
# @generated
from cdpsm.iec61970.core.conducting_equipment import ConductingEquipment



from google.appengine.ext import db
# >>> imports

class Switch(ConductingEquipment):
    """ A generic device designed to close, or open, or both, one or more electric circuits. 
    """
    # <<< switch.attributes
    # @generated
    # The attribute is used in cases when no Measurement for the status value is present. If the Switch has a status measurment the Discrete.normalValue is expected to match with the Switch.normalOpen. 
    normal_open = db.BooleanProperty()

    # >>> switch.attributes

    # <<< switch.references
    # @generated
    # >>> switch.references

    # <<< switch.operations
    # @generated
    # >>> switch.operations

# EOF -------------------------------------------------------------------------
