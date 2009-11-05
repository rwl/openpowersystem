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

""" AnalogValue represents an analog MeasurementValue. 
"""

# <<< imports
# @generated
from cpsm.meas.measurement_value import MeasurementValue

from cpsm.meas.analog import Analog


from google.appengine.ext import db
# >>> imports

class AnalogValue(MeasurementValue):
    """ AnalogValue represents an analog MeasurementValue. 
    """
    # <<< analog_value.attributes
    # @generated
    # >>> analog_value.attributes

    # <<< analog_value.references
    # @generated
    # Measurement to which this value is connected. 
    member_of_measurement = db.ReferenceProperty(Analog,
        collection_name="contain_measurement_values")

    # >>> analog_value.references

    # <<< analog_value.operations
    # @generated
    # >>> analog_value.operations

# EOF -------------------------------------------------------------------------
