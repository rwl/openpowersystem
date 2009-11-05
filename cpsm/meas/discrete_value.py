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

""" DiscreteValue represents a discrete MeasurementValue. 
"""

# <<< imports
# @generated
from cpsm.meas.measurement_value import MeasurementValue

from cpsm.meas.discrete import Discrete


from google.appengine.ext import db
# >>> imports

class DiscreteValue(MeasurementValue):
    """ DiscreteValue represents a discrete MeasurementValue. 
    """
    # <<< discrete_value.attributes
    # @generated
    # >>> discrete_value.attributes

    # <<< discrete_value.references
    # @generated
    # Measurement to which this value is connected. 
    member_of_measurement = db.ReferenceProperty(Discrete,
        collection_name="contain_measurement_values")

    # >>> discrete_value.references

    # <<< discrete_value.operations
    # @generated
    # >>> discrete_value.operations

# EOF -------------------------------------------------------------------------
