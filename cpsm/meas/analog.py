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

""" Analog represents an analog Measurement. 
"""

# <<< imports
# @generated
from cpsm.meas.measurement import Measurement



from google.appengine.ext import db
# >>> imports

class Analog(Measurement):
    """ Analog represents an analog Measurement. 
    """
    # <<< analog.attributes
    # @generated
    # If true then this measurement is an active power, reactive power or current with the convention that a positive value measured at the Terminal means power is flowing into the related PowerSystemResource. 
    positive_flow_in = db.BooleanProperty()

    # >>> analog.attributes

    # <<< analog.references
    # @generated
    # Virtual property. The values connected to this measurement.  
    pass # contain_measurement_values

    # >>> analog.references

    # <<< analog.operations
    # @generated
    # >>> analog.operations

# EOF -------------------------------------------------------------------------
