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

""" This package contains the information classes that support distribution management in general.This package contains the information classes that support distribution management in general.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from cdpsm.iec61970.core import IdentifiedObject
from cdpsm import Element


# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

#------------------------------------------------------------------------------
#  Properties:
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  Constants:
#------------------------------------------------------------------------------

NS_PREFIX = "cim"
NS_URI = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_Common"

#------------------------------------------------------------------------------
#  "Location" class:
#------------------------------------------------------------------------------

class Location(IdentifiedObject):
    """ The place, scene, or point of something where someone or something has been, is, and/or will be at a given moment in time. It may be: - Spatial location of an actual or planned structure, or a set of point-oriented structures (as a substation, structure, building, town, etc.) or diagram objects, which may be defined as a point or polygon, or, - Path of an underground or overhead conductor, or a linear diagram object.The place, scene, or point of something where someone or something has been, is, and/or will be at a given moment in time. It may be: - Spatial location of an actual or planned structure, or a set of point-oriented structures (as a substation, structure, building, town, etc.) or diagram objects, which may be defined as a point or polygon, or, - Path of an underground or overhead conductor, or a linear diagram object.
    """

    
    # Virtual property. Sequence of position points describing this location.Sequence of position points describing this location.
    pass #position_points

    # <<< location
    # @generated
    # >>> location


#------------------------------------------------------------------------------
#  "PositionPoint" class:
#------------------------------------------------------------------------------

class PositionPoint(Element):
    """ Set of spatial coordinates that determine a point. A sequence of PositionPoints can be used to describe: - physical location of non-point oriented objects like cables or lines, or - area of an object like a substation, a geographical zone or a diagram object.Set of spatial coordinates that determine a point. A sequence of PositionPoints can be used to describe: - physical location of non-point oriented objects like cables or lines, or - area of an object like a substation, a geographical zone or a diagram object.
    """

    
    # Zero-relative sequence number of this point within a series of points.Zero-relative sequence number of this point within a series of points.
    sequence_number = db.IntegerProperty()

    # X axis position.X axis position.
    x_position = db.StringProperty()

    # Y axis position.Y axis position.
    y_position = db.StringProperty()

    # Location that this position point describes.Location that this position point describes.
    location = db.ReferenceProperty(collection_name="position_points")

    # <<< position_point
    # @generated
    # >>> position_point


#------------------------------------------------------------------------------
#  "GeoLocation" class:
#------------------------------------------------------------------------------

class GeoLocation(Location):
    """ Geographical location.Geographical location.
    """

    
    # Virtual property. All power system resources at this geographical location.All power system resources at this geographical location.
    pass #power_system_resources

    # <<< geo_location
    # @generated
    # >>> geo_location




# EOF -------------------------------------------------------------------------
