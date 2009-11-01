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


#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from cpsm.core import PowerSystemResource
from cpsm import Element

from cpsm.domain import ActivePower

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

#------------------------------------------------------------------------------
#  Properties:
#------------------------------------------------------------------------------

ControlAreaTypeKind = db.StringProperty(choices=("forecast", "interchange", "agc"))

#------------------------------------------------------------------------------
#  Constants:
#------------------------------------------------------------------------------

NS_PREFIX = "cim"
NS_URI = "http://iec.ch/TC57/2008/CIM-schema-cim13#Package_ControlArea"

#------------------------------------------------------------------------------
#  "ControlArea" class:
#------------------------------------------------------------------------------

class ControlArea(PowerSystemResource):
    """ A <b>control area </b>is a grouping of <b>generating units</b> and/or loads and a cutset of tie lines (as <b>terminals</b>) which may be used for a variety of purposes including automatic generation control, powerflow solution area interchange control specification, and input to load forecasting.   Note that any number of overlapping control area specifications can be superimposed on the physical model.A <b>control area </b>is a grouping of <b>generating units</b> and/or loads and a cutset of tie lines (as <b>terminals</b>) which may be used for a variety of purposes including automatic generation control, powerflow solution area interchange control specification, and input to load forecasting.   Note that any number of overlapping control area specifications can be superimposed on the physical model.
    """

    
    # The specified positive net interchange into the control area.The specified positive net interchange into the control area.
    net_interchange = ActivePower

    # The type of control area defintion used to determine if this is used for automatic generation control, for planning interchange control, or other purposes.The type of control area defintion used to determine if this is used for automatic generation control, for planning interchange control, or other purposes.
    type = ControlAreaTypeKind

    # Virtual property. The generating unit specificaitons for the control area.The generating unit specificaitons for the control area.
    pass #control_area_generating_unit

    # The energy area that is forecast from this control area specification.The energy area that is forecast from this control area specification.
    energy_area = db.ReferenceProperty()

    # Virtual property. The tie flows associated with the control area.The tie flows associated with the control area.
    pass #tie_flow

    # <<< control_area
    # @generated
    # >>> control_area


#------------------------------------------------------------------------------
#  "TieFlow" class:
#------------------------------------------------------------------------------

class TieFlow(Element):
    """ A flow specification in terms of location and direction for a control area.A flow specification in terms of location and direction for a control area.
    """

    
    # The flow is positive into the terminal.  A flow is positive if it is an import into the control area.The flow is positive into the terminal.  A flow is positive if it is an import into the control area.
    positive_flow_in = db.BooleanProperty()

    # The control area of the tie flows.The control area of the tie flows.
    control_area = db.ReferenceProperty(collection_name="tie_flow")

    # <<< tie_flow
    # @generated
    # >>> tie_flow


#------------------------------------------------------------------------------
#  "ControlAreaGeneratingUnit" class:
#------------------------------------------------------------------------------

class ControlAreaGeneratingUnit(Element):
    """ A control area generating unit. This class is needed so that alternate control area definitions may include the same generating unit.   Note only one instance within a control area should reference a specific generating unit.A control area generating unit. This class is needed so that alternate control area definitions may include the same generating unit.   Note only one instance within a control area should reference a specific generating unit.
    """

    
    # The parent control area for the generating unit specifications.The parent control area for the generating unit specifications.
    control_area = db.ReferenceProperty(collection_name="control_area_generating_unit")

    # The generating unit specified for this control area.  Note that a control area should include a GeneratingUnit only once.The generating unit specified for this control area.  Note that a control area should include a GeneratingUnit only once.
    generating_unit = db.ReferenceProperty(collection_name="control_area_generating_unit")

    # <<< control_area_generating_unit
    # @generated
    # >>> control_area_generating_unit




# EOF -------------------------------------------------------------------------
