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

""" A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  Negative values for mVArPerSection and nominalMVAr indicate that the compensator is a reactor. mVArPerSection and nominalMVAr is now bPerSection. 
"""

# <<< imports
# @generated
from ucte.wires.regulating_cond_eq import RegulatingCondEq


from ucte.domain import Susceptance
from ucte.domain import Conductance

from google.appengine.ext import db
# >>> imports

class ShuntCompensator(RegulatingCondEq):
    """ A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  Negative values for mVArPerSection and nominalMVAr indicate that the compensator is a reactor. mVArPerSection and nominalMVAr is now bPerSection. 
    """
    # <<< shunt_compensator.attributes
    # @generated
    # Zero sequence shunt (charging) susceptance per section This is for Short Circuit only. 
    b0_per_section = Susceptance

    # For a capacitor bank, the maximum number of sections that may be switched in. 
    maximum_sections = db.IntegerProperty(default=0)

    # Zero sequence shunt (charging) conductance per section This is for Short Circuit only. 
    g0_per_section = Conductance

    # Positive sequence shunt (charging) susceptance per section 
    b_per_section = Susceptance

    # Positive sequence shunt (charging) conductance per section 
    g_per_section = Conductance

    # >>> shunt_compensator.attributes

    # <<< shunt_compensator.references
    # @generated
    # The state for the number of shunt compensator sections in service.  
    sv_shunt_compensator_sections = db.ReferenceProperty(db.Model,
        collection_name="_shunt_compensator_set") # shunt_compensator

    # >>> shunt_compensator.references

    # <<< shunt_compensator.operations
    # @generated
    # >>> shunt_compensator.operations

# EOF -------------------------------------------------------------------------
