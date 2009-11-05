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

""" A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system. If the instance is an ACLineSegment, the resistance and reactance is mandatory.  However, if the line segment is for a DistributionLineSegment, these are not mandatory. 
"""

# <<< imports
# @generated
from cdpsm.iec61970.wires.conductor import Conductor


from cdpsm.iec61970.domain import Resistance
from cdpsm.iec61970.domain import Reactance
from cdpsm.iec61970.domain import Susceptance

from google.appengine.ext import db
# >>> imports

class ACLineSegment(Conductor):
    """ A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system. If the instance is an ACLineSegment, the resistance and reactance is mandatory.  However, if the line segment is for a DistributionLineSegment, these are not mandatory. 
    """
    # <<< acline_segment.attributes
    # @generated
    # Positive sequence series resistance of the entire line section. 
    r = Resistance

    # Zero sequence series reactance of the entire line section. 
    x0 = Reactance

    # Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.  This value represents the full charging over the full length of the line. 
    bch = Susceptance

    # Positive sequence series reactance of the entire line section. 
    x = Reactance

    # Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section. 
    b0ch = Susceptance

    # Zero sequence series resistance of the entire line section. 
    r0 = Resistance

    # >>> acline_segment.attributes

    # <<< acline_segment.references
    # @generated
    # >>> acline_segment.references

    # <<< acline_segment.operations
    # @generated
    # >>> acline_segment.operations

# EOF -------------------------------------------------------------------------
