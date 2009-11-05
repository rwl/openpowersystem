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

""" Set of spatial coordinates that determine a point. A sequence of PositionPoints can be used to describe: - physical location of non-point oriented objects like cables or lines, or - area of an object like a substation, a geographical zone or a diagram object. 
"""

# <<< imports
# @generated
from cdpsm.element import Element

from cdpsm.iec61968.common.location import Location


from google.appengine.ext import db
# >>> imports

class PositionPoint(Element):
    """ Set of spatial coordinates that determine a point. A sequence of PositionPoints can be used to describe: - physical location of non-point oriented objects like cables or lines, or - area of an object like a substation, a geographical zone or a diagram object. 
    """
    # <<< position_point.attributes
    # @generated
    # Zero-relative sequence number of this point within a series of points. 
    sequence_number = db.IntegerProperty()

    # X axis position. 
    x_position = db.StringProperty()

    # Y axis position. 
    y_position = db.StringProperty()

    # >>> position_point.attributes

    # <<< position_point.references
    # @generated
    # Location that this position point describes. 
    location = db.ReferenceProperty(Location,
        collection_name="position_points")

    # >>> position_point.references

    # <<< position_point.operations
    # @generated
    # >>> position_point.operations

# EOF -------------------------------------------------------------------------
