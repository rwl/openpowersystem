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

""" A collection of power system resources (within a given substation) including conducting equipment, protection relays, measurements, and telemetry. 
"""

# <<< imports
# @generated
from cdpsm.iec61970.core.equipment_container import EquipmentContainer

from cdpsm.iec61970.core.voltage_level import VoltageLevel


from google.appengine.ext import db
# >>> imports

class Bay(EquipmentContainer):
    """ A collection of power system resources (within a given substation) including conducting equipment, protection relays, measurements, and telemetry. 
    """
    # <<< bay.attributes
    # @generated
    # >>> bay.attributes

    # <<< bay.references
    # @generated
    # The association is used in the naming hierarchy. 
    voltage_level = db.ReferenceProperty(VoltageLevel,
        collection_name="bays")

    # >>> bay.references

    # <<< bay.operations
    # @generated
    # >>> bay.operations

# EOF -------------------------------------------------------------------------
