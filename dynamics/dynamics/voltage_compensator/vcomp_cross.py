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


# <<< imports
# @generated
from dynamics.dynamics.voltage_compensator.voltage_compensator import VoltageCompensator


from dynamics.domain import Reactance
from dynamics.domain import Resistance

from google.appengine.ext import db
# >>> imports

class VcompCross(VoltageCompensator):
    """ Voltage Compensation Model for Cross-Compound Generating Unit 
    """
    # <<< vcomp_cross.attributes
    # @generated
    # Cross-Compensating (compounding) reactance 
    xcomp2 = Reactance

    # Cross-Compensating (compounding) resistance 
    rcomp2 = Resistance

    # >>> vcomp_cross.attributes

    # <<< vcomp_cross.references
    # @generated
    # >>> vcomp_cross.references

    # <<< vcomp_cross.operations
    # @generated
    # >>> vcomp_cross.operations

# EOF -------------------------------------------------------------------------
