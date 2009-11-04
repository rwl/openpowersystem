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

""" Mechanism for changing transformer winding tap positions. 
"""

# <<< imports
# @generated
from ucte.core.identified_object import IdentifiedObject

from ucte.wires.regulating_control import RegulatingControl

from ucte.domain import PerCent
from ucte.domain import Voltage

from google.appengine.ext import db
# >>> imports

class TapChanger(IdentifiedObject):
    """ Mechanism for changing transformer winding tap positions. 
    """
    # <<< tap_changer.attributes
    # @generated
    # Tap step increment, in per cent of nominal voltage, per step position. This could be supplanted by more detailed model information in either the PhaseTapChanger if modeled or in detailed per tap step table information. This is required for RatioTapChanger. It is Optional for most phase shifters since these are not used to regulate voltages 
    step_voltage_increment = PerCent

    # Voltage at which the winding operates at the neutral tap setting. 
    neutral_u = Voltage

    # Lowest possible tap step position, retard from neutral 
    low_step = db.IntegerProperty()

    # The neutral tap step position for this winding. This attribute is used to define the neutral step for a tap changer or a phase tap changer.  The neutralStep value cannot be higher than the highStep value or lower than the lowStep value.  
    neutral_step = db.IntegerProperty()

    # Highest possible tap step position, advance from neutral 
    high_step = db.IntegerProperty()

    # >>> tap_changer.attributes

    # <<< tap_changer.references
    # @generated
    # The tap step state associated with the tap changer.  
    sv_tap_step = db.ReferenceProperty(db.Model,
        collection_name="_tap_changer_set") # tap_changer

    # 
    regulating_control = db.ReferenceProperty(RegulatingControl,
        collection_name="tap_changer")

    # >>> tap_changer.references

    # <<< tap_changer.operations
    # @generated
    # >>> tap_changer.operations

# EOF -------------------------------------------------------------------------
