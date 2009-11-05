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

""" Classifying instances of the same class, e.g. overhead and underground ACLineSegments. This classification mechanism is intended to provide flexibility outside the scope of this standard, i.e. provide customisation that is non standard. 
"""

# <<< imports
# @generated
from cdpsm.iec61970.core.identified_object import IdentifiedObject



from google.appengine.ext import db
# >>> imports

class PSRType(IdentifiedObject):
    """ Classifying instances of the same class, e.g. overhead and underground ACLineSegments. This classification mechanism is intended to provide flexibility outside the scope of this standard, i.e. provide customisation that is non standard. 
    """
    # <<< psrtype.attributes
    # @generated
    # >>> psrtype.attributes

    # <<< psrtype.references
    # @generated
    # Virtual property. Power system resources classified with this PSRType.  
    pass # power_system_resources

    # >>> psrtype.references

    # <<< psrtype.operations
    # @generated
    # >>> psrtype.operations

# EOF -------------------------------------------------------------------------
