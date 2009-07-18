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

from cim14.iec61970.core import PowerSystemResource
from cim14 import Element

from cim14.iec61970.domain import ActivePower

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

ControlAreaTypeKind = db.StringProperty(choices=("forecast", "interchange", "agc"))

ns_prefix = "cim.IEC61970.ControlArea"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#IEC61970.ControlArea"

class ControlArea(PowerSystemResource):
    """ A <b>control area </b>is a grouping of <b>generating units</b> and/or loads and a cutset of tie lines (as <b>terminals</b>) which may be used for a variety of purposes including automatic generation control, powerflow solution area interchange control specification, and input to load forecasting.   Note that any number of overlapping control area specifications can be superimposed on the physical model.
    """

    # The specified positive net interchange into the control area.
    net_interchange = ActivePower
    # The type of control area defintion used to determine if this is used for automatic generation control, for planning interchange control, or other purposes.
    type = ControlAreaTypeKind
    # Active power net interchange tolerance
    p_tolerance = ActivePower
    # The 'control_area_generating_unit' property has been implicitly created by
    # the control_area' property of ControlAreaGeneratingUnit.
    pass
    # The 'tie_flow' property has been implicitly created by
    # the control_area' property of TieFlow.
    pass
    # The 'bus_name_marker' property has been implicitly created by
    # the control_area' property of BusNameMarker.
    pass
#    energy_area = db.ReferenceProperty()
    # The 'topological_node' property has been implicitly created by
    # the control_area' property of TopologicalNode.
    pass

class AltTieMeas(Element):
    """ A prioritized measurement to be used for the tie flow as part of the control area specification.
    """

    # Priority of a measurement usage.   Lower numbers have first priority.
    priority = db.IntegerProperty()
#    tie_flow = db.ReferenceProperty()
#    analog_value = db.ReferenceProperty()

class TieFlow(Element):
    """ A flow specification in terms of location and direction for a control area.
    """

    # The flow is positive into the terminal.  A flow is positive if it is an import into the control area.
    positive_flow_in = db.BooleanProperty()
    # The 'alt_tie_meas' property has been implicitly created by
    # the tie_flow' property of AltTieMeas.
    pass
#    control_area = db.ReferenceProperty()
#    terminal = db.ReferenceProperty()

class AltGeneratingUnitMeas(Element):
    """ A prioritized measurement to be used for the generating unit in the control area specificaiton.
    """

    # Priority of a measurement usage.   Lower numbers have first priority.
    priority = db.IntegerProperty()
#    analog_value = db.ReferenceProperty()
#    control_area_generating_unit = db.ReferenceProperty()

class ControlAreaGeneratingUnit(Element):
    """ A control area generating unit. This class is needed so that alternate control area definitions may include the same generating unit.   Note only one instance within a control area should reference a specific generating unit.
    """

    # The 'alt_generating_unit_meas' property has been implicitly created by
    # the control_area_generating_unit' property of AltGeneratingUnitMeas.
    pass
#    control_area = db.ReferenceProperty()
#    generating_unit = db.ReferenceProperty()


