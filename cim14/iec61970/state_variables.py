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

from cim14 import Element

from cim14.iec61970.domain import AngleRadians
from cim14.iec61970.domain import Voltage
from cim14.iec61970.domain import ActivePower
from cim14.iec61970.domain import ReactivePower

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

ns_prefix = "cim.IEC61970.StateVariables"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#IEC61970.StateVariables"

class StateVariable(Element):
    """ An abstract class for state variables.
    """

    pass

class SvVoltage(StateVariable):
    """ State variable for voltage.
    """

    # The voltage angle in radians of the topological node.
    angle = AngleRadians
    # The voltage magnitude of the topological node.
    v = Voltage
#    topological_node = db.ReferenceProperty()

class SvShuntCompensatorSections(StateVariable):
    """ State variable for the number of sections in service for a shunt compensator.
    """

    # The number of sections in service.
    sections = db.IntegerProperty()
    # The number of sections in service as a continous variable.
    continuous_sections = db.FloatProperty()
#    shunt_compensator = db.ReferenceProperty()

class SvTapStep(StateVariable):
    """ State variable for transformer tap step.     Normally a profile specifies only one of the attributes 'position'or 'tapRatio'.
    """

    # The integer tap position.
    position = db.IntegerProperty()
    # The floating point tap position.
    continuous_position = db.FloatProperty()
#    tap_changer = db.ReferenceProperty()

class SvPowerFlow(StateVariable):
    """ State variable for power flow.
    """

    # The active power flow into the terminal.
    p = ActivePower
    # The reactive power flow into the terminal.
    q = ReactivePower
#    terminal = db.ReferenceProperty()

class SvInjection(StateVariable):
    """ Injectixon state variable.
    """

    # The activive power injected into the bus at this location.
    p_net_injection = ActivePower
    # The activive power injected into the bus at this location.
    q_net_injection = ReactivePower
#    topological_node = db.ReferenceProperty()

class SvStatus(StateVariable):
    """ State variable for status.
    """

    # The in service status as a result of topology processing.
    in_service = db.BooleanProperty()
#    conducting_equipment = db.ReferenceProperty()


