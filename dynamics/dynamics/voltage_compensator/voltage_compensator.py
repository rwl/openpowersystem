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
from dynamics.element import Element


from dynamics.domain import Resistance
from dynamics.domain import Reactance

from google.appengine.ext import db
# >>> imports

class VoltageCompensator(Element):
    """ A voltage compensator adjusts the terminal voltage feedback to the excitation system by adding a quantity that is proportional to the terminal current of the generator. It is linked to a specific generator by the Bus number and Unit ID 
    """
    # <<< voltage_compensator.attributes
    # @generated
    # Compensating (compounding) resistance 
    rcomp = Resistance

    # Compensating (compounding) reactance 
    xcomp = Reactance

    # >>> voltage_compensator.attributes

    # <<< voltage_compensator.references
    # @generated
    # >>> voltage_compensator.references

    # <<< voltage_compensator.operations
    # @generated
    # >>> voltage_compensator.operations

# EOF -------------------------------------------------------------------------
