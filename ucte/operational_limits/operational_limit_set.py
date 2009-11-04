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

""" A set of limits associated with equipmnet.  Sets of limits might apply to a specific temperature, or season for example. A set of limits may contain may different severiteis of limit levels that would apply to the same equipment.   The set may contain limits of different types such as apparent power and current limits or high and low voltage limits  that are logically applied together as a set. 
"""

# <<< imports
# @generated
from ucte.core.identified_object import IdentifiedObject

from ucte.core.terminal import Terminal


from google.appengine.ext import db
# >>> imports

class OperationalLimitSet(IdentifiedObject):
    """ A set of limits associated with equipmnet.  Sets of limits might apply to a specific temperature, or season for example. A set of limits may contain may different severiteis of limit levels that would apply to the same equipment.   The set may contain limits of different types such as apparent power and current limits or high and low voltage limits  that are logically applied together as a set. 
    """
    # <<< operational_limit_set.attributes
    # @generated
    # >>> operational_limit_set.attributes

    # <<< operational_limit_set.references
    # @generated
    # The terminal specifically associated to this operational limit set.  If no terminal is associated, all terminals of the equipment are implied. For UCTE profile, the terminal associated with the limit is always required, and thus there is no need to exchange the associated Equipment which can always be derived from the terminal. 
    terminal = db.ReferenceProperty(Terminal,
        collection_name="operational_limit_set")

    # Virtual property. Values of equipment limits.  
    pass # operational_limit_value

    # >>> operational_limit_set.references

    # <<< operational_limit_set.operations
    # @generated
    # >>> operational_limit_set.operations

# EOF -------------------------------------------------------------------------
