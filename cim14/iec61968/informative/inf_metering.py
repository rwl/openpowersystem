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

from cim14.iec61970.core import IdentifiedObject
from cim14.iec61968.metering import DeviceFunction


# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

ns_prefix = "cim.IEC61968.Informative.InfMetering"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#IEC61968.Informative.InfMetering"

class ComPort(IdentifiedObject):
    """ Port information used for communication connectivity purposes. The 'port' names the physical association to another device from the perspective of the parent asset. For example, a communications module may need to list the meters which it can talk to as meter serial number '123' is on 'port 0', S/N '456' is on port '1', etc. A meter or load control device may need to know that a hot-water heater load is on 'port 0', and an air-conditioner on 'port 1'.
    """

    pass

class MeteringFunctionConfiguration(IdentifiedObject):
    """ The configuration of data for a given meter function.
    """

    # The 'electric_metering_functions' property has been implicitly created by
    # the metering_function_configuration' property of ElectricMeteringFunction.
    pass

class WaterMeteringFunction(DeviceFunction):
    """ Functionality performed by a water meter. It's entirely possible that the metering system would carry information to/from water meters even though it was built primarily to carry the higher-value electric meter data.
    """

    pass

class GasMeteringFunction(DeviceFunction):
    """ Functionality performed by a gas meter. It's entirely possible that the metering system would carry information to/from gas meters even though it was built primarily to carry the higher-value electric meter data.
    """

    pass


