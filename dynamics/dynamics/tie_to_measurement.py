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

""" Ties a block input to a specific state variable measurment.  Thus giving a unit type, a location in the network (typically a terminal).   A specific value is not given, just enough information to obtain the value from the model during a solution. This has nothing to do with SCADA. 
"""

# <<< imports
# @generated
from dynamics.element import Element



from google.appengine.ext import db
# >>> imports

class TieToMeasurement(Element):
    """ Ties a block input to a specific state variable measurment.  Thus giving a unit type, a location in the network (typically a terminal).   A specific value is not given, just enough information to obtain the value from the model during a solution. This has nothing to do with SCADA. 
    """
    # <<< tie_to_measurement.attributes
    # @generated
    # >>> tie_to_measurement.attributes

    # <<< tie_to_measurement.references
    # @generated
    # >>> tie_to_measurement.references

    # <<< tie_to_measurement.operations
    # @generated
    # >>> tie_to_measurement.operations

# EOF -------------------------------------------------------------------------
