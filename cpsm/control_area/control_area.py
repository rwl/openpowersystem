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


# <<< imports
# @generated
from cpsm.core.power_system_resource import PowerSystemResource


from cpsm.domain import ActivePower
from cpsm.control_area import ControlAreaTypeKind

from google.appengine.ext import db
# >>> imports

class ControlArea(PowerSystemResource):
    """ A <b>control area </b>is a grouping of <b>generating units</b> and/or loads and a cutset of tie lines (as <b>terminals</b>) which may be used for a variety of purposes including automatic generation control, powerflow solution area interchange control specification, and input to load forecasting.   Note that any number of overlapping control area specifications can be superimposed on the physical model. 
    """
    # <<< control_area.attributes
    # @generated
    # The specified positive net interchange into the control area. 
    net_interchange = ActivePower

    # The type of control area defintion used to determine if this is used for automatic generation control, for planning interchange control, or other purposes. 
    type = ControlAreaTypeKind

    # >>> control_area.attributes

    # <<< control_area.references
    # @generated
    # Virtual property. The generating unit specificaitons for the control area.  
    pass # control_area_generating_unit

    # The energy area that is forecast from this control area specification. 
    energy_area = db.ReferenceProperty(db.Model,
        collection_name="_control_area_set") # control_area

    # Virtual property. The tie flows associated with the control area.  
    pass # tie_flow

    # >>> control_area.references

    # <<< control_area.operations
    # @generated
    # >>> control_area.operations

# EOF -------------------------------------------------------------------------
