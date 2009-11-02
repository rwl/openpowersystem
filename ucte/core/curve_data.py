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

""" Data point values for defining a curve or schedule 
"""

# <<< imports
# @generated
from ucte.element import Element

from ucte.core.curve import Curve


from google.appengine.ext import db
# >>> imports

class CurveData(Element):
    """ Data point values for defining a curve or schedule 
    """
    # <<< curve_data.attributes
    # @generated
    # The data value of the  first Y-axis variable, depending on the Y-axis units 
    y1value = db.FloatProperty()

    # The data value of the X-axis variable,  depending on the X-axis units 
    xvalue = db.FloatProperty()

    # The data value of the second Y-axis variable (if present), depending on the Y-axis units 
    y2value = db.FloatProperty()

    # >>> curve_data.attributes

    # <<< curve_data.references
    # @generated
    # The Curve defined by this CurveData. 
    curve_schedule = db.ReferenceProperty(Curve, collection_name="curve_schedule_datas")

    # >>> curve_data.references

    # <<< curve_data.operations
    # @generated
    # >>> curve_data.operations

# EOF -------------------------------------------------------------------------
