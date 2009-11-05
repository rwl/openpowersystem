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

""" A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  Negative values for mVArPerSection and nominalMVAr indicate that the compensator is a reactor. 
"""

# <<< imports
# @generated
from cpsm.wires.regulating_cond_eq import RegulatingCondEq


from cpsm.domain import Voltage
from cpsm.domain import ReactivePower

from google.appengine.ext import db
# >>> imports

class ShuntCompensator(RegulatingCondEq):
    """ A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  Negative values for mVArPerSection and nominalMVAr indicate that the compensator is a reactor. 
    """
    # <<< shunt_compensator.attributes
    # @generated
    # For a capacitor bank, the maximum number of sections that may be switched in. 
    maximum_sections = db.IntegerProperty()

    # For a capacitor bank, the normal number of sections switched in. This number should correspond to the nominal reactive power (nomQ). 
    normal_sections = db.IntegerProperty()

    # The nominal voltage at which the nominal reactive power was measured. This should normally be within 10% of the voltage at which the capacitor is connected to the network. 
    nom_u = Voltage

    # For a capacitor bank, the size in reactive power of each switchable section at the nominal voltage. 
    reactive_per_section = ReactivePower

    # >>> shunt_compensator.attributes

    # <<< shunt_compensator.references
    # @generated
    # >>> shunt_compensator.references

    # <<< shunt_compensator.operations
    # @generated
    # >>> shunt_compensator.operations

# EOF -------------------------------------------------------------------------
