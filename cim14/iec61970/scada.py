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
from cim14.iec61970.core import IdentifiedObject

from cim14.iec61970.domain import Seconds

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

RemoteUnitType = db.StringProperty(choices=("control_center", "ied", "rtu", "substation_control_system"))

Source = db.StringProperty(choices=("substituted", "process", "defaulted"))

ns_prefix = "cim.IEC61970.SCADA"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#IEC61970.SCADA"

class CommunicationLink(PowerSystemResource):
    """ The connection to remote units is through one or more communication links. Reduntant links may exist. The CommunicationLink class inherit PowerSystemResource. The intention is to allow CommunicationLinks to have Measurements. These Measurements can be used to model link status as operational, out of service, unit failure etc.
    """

#    remote_units = db.ListProperty(db.Key)

#    @property
#    def communication_links(self):
#        return RemoteUnit.gql("WHERE remote_units = :1", self.key())

class RemotePoint(IdentifiedObject):
    """ For a RTU remote points correspond to telemetered values or control outputs. Other units (e.g. control centers) usually also contain calculated values.
    """

#    remote_unit = db.ReferenceProperty()

class RemoteUnit(PowerSystemResource):
    """ A remote unit can be a RTU, IED, substation control system, control center etc. The communication with the remote unit can be through various standard protocols (e.g. IEC 61870, IEC 61850) or non standard protocols (e.g. DNP, RP570 etc.). A remote unit contain remote data points that might be telemetered, collected or calculated. The RemoteUnit class inherit PowerSystemResource. The intention is to allow RemotUnits to have Measurements. These Measurements can be used to model unit status as operational, out of service, unit failure etc.
    """

    # Type of remote unit.
    remote_unit_type = RemoteUnitType
#    communication_links = db.ListProperty(db.Key)

#    @property
#    def remote_units(self):
#        return CommunicationLink.gql("WHERE communication_links = :1", self.key())
    # The 'remote_points' property has been implicitly created by
    # the remote_unit' property of RemotePoint.
    pass

class RemoteSource(RemotePoint):
    """ Remote sources are state variables that are telemetered or calculated within the remote unit.
    """

    # The smallest change in value to be reported.
    deadband = db.FloatProperty()
    # The time interval between scans.
    scan_interval = Seconds
    # The maximum value the telemetry item can return.
    sensor_maximum = db.FloatProperty()
    # The minimum value the telemetry item can return.
    sensor_minimum = db.FloatProperty()
#    measurement_value = db.ReferenceProperty()

class RemoteControl(RemotePoint):
    """ Remote controls are ouputs that are sent by the remote unit to actuators in the process.
    """

    # The maximum set point value accepted by the remote control point.
    actuator_maximum = db.FloatProperty()
    # The minimum set point value accepted by the remote control point.
    actuator_minimum = db.FloatProperty()
    # Set to true if the actuator is remotely controlled.
    remote_controlled = db.BooleanProperty()
#    control = db.ReferenceProperty()


