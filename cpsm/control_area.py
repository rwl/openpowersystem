# Copyright (C) 2009 Richard W. Lincoln
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation; version 2 dated June, 1991.
#
# This software is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANDABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA

from cpsm.core import PowerSystemResource
from cpsm import Element

from cpsm.domain import ActivePower

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

ControlAreaTypeKind = db.StringProperty(choices=("forecast", "interchange", "agc"))

ns_prefix = "cim"
ns_uri = "http://iec.ch/TC57/2008/CIM-schema-cim13#Package_ControlArea"

class ControlArea(PowerSystemResource):
    """ A <b>control area </b>is a grouping of <b>generating units</b> and/or loads and a cutset of tie lines (as <b>terminals</b>) which may be used for a variety of purposes including automatic generation control, powerflow solution area interchange control specification, and input to load forecasting.   Note that any number of overlapping control area specifications can be superimposed on the physical model.
    """

    # The specified positive net interchange into the control area.
    net_interchange = ActivePower
    # The type of control area defintion used to determine if this is used for automatic generation control, for planning interchange control, or other purposes.
    type = ControlAreaTypeKind
#    control_area_generating_unit = db.ReferenceProperty()
#    energy_area = db.ReferenceProperty()
#    tie_flow = db.ReferenceProperty()

class TieFlow(Element):
    """ A flow specification in terms of location and direction for a control area.
    """

    # The flow is positive into the terminal.  A flow is positive if it is an import into the control area.
    positive_flow_in = db.BooleanProperty()
#    control_area = db.ReferenceProperty()

class ControlAreaGeneratingUnit(Element):
    """ A control area generating unit. This class is needed so that alternate control area definitions may include the same generating unit.   Note only one instance within a control area should reference a specific generating unit.
    """

#    control_area = db.ReferenceProperty()
#    generating_unit = db.ReferenceProperty()


