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

""" MeasurementValueSource describes the alternative sources updating a MeasurementValue. User conventions for how to use the MeasurementValueSource attributes are described in the introduction to IEC 61970-301. 
"""

# <<< imports
# @generated
from cpsm.core.identified_object import IdentifiedObject



from google.appengine.ext import db
# >>> imports

class MeasurementValueSource(IdentifiedObject):
    """ MeasurementValueSource describes the alternative sources updating a MeasurementValue. User conventions for how to use the MeasurementValueSource attributes are described in the introduction to IEC 61970-301. 
    """
    # <<< measurement_value_source.attributes
    # @generated
    # >>> measurement_value_source.attributes

    # <<< measurement_value_source.references
    # @generated
    # Virtual property. The MeasurementValues updated by the source  
    pass # measurement_values

    # >>> measurement_value_source.references

    # <<< measurement_value_source.operations
    # @generated
    # >>> measurement_value_source.operations

# EOF -------------------------------------------------------------------------
