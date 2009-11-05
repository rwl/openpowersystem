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

""" A generic equivalent for an energy supplier on a transmission or distribution voltage level. 
"""

# <<< imports
# @generated
from cdpsm.iec61970.core.conducting_equipment import ConductingEquipment


from cdpsm.iec61970.domain import Reactance
from cdpsm.iec61970.domain import Voltage
from cdpsm.iec61970.domain import AngleRadians

from google.appengine.ext import db
# >>> imports

class EnergySource(ConductingEquipment):
    """ A generic equivalent for an energy supplier on a transmission or distribution voltage level. 
    """
    # <<< energy_source.attributes
    # @generated
    # Positive sequence Thevenin reactance. 
    x = Reactance

    # Phase-to-phase open circuit voltage magnitude. 
    voltage_magnitude = Voltage

    # Phase angle of a-phase open circuit. 
    voltage_angle = AngleRadians

    # Phase-to-phase nominal voltage. 
    nominal_voltage = Voltage

    # >>> energy_source.attributes

    # <<< energy_source.references
    # @generated
    # >>> energy_source.references

    # <<< energy_source.operations
    # @generated
    # >>> energy_source.operations

# EOF -------------------------------------------------------------------------
