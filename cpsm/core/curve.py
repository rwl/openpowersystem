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

""" Relationship between an independent variable (X-axis) and one or two dependent  variables (Y1-axis and Y2-axis). Curves can also serve as schedules. 
"""

# <<< imports
# @generated
from cpsm.core.identified_object import IdentifiedObject


from cpsm.domain import UnitSymbol
from cpsm.core import CurveStyle

from google.appengine.ext import db
# >>> imports

class Curve(IdentifiedObject):
    """ Relationship between an independent variable (X-axis) and one or two dependent  variables (Y1-axis and Y2-axis). Curves can also serve as schedules. 
    """
    # <<< curve.attributes
    # @generated
    # The Y2-axis units of measure. 
    y2_unit = UnitSymbol

    # The X-axis units of measure. 
    x_unit = UnitSymbol

    # The style or shape of the curve. 
    curve_style = CurveStyle

    # The Y1-axis units of measure. 
    y1_unit = UnitSymbol

    # >>> curve.attributes

    # <<< curve.references
    # @generated
    # Virtual property. The point data values that define a curve  
    pass # curve_schedule_datas

    # >>> curve.references

    # <<< curve.operations
    # @generated
    # >>> curve.operations

# EOF -------------------------------------------------------------------------
