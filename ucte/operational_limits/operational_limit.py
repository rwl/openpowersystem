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

""" A value associated with a specific kind of limit. 
"""

# <<< imports
# @generated
from ucte.core.identified_object import IdentifiedObject

from ucte.operational_limits.operational_limit_set import OperationalLimitSet
from ucte.operational_limits.operational_limit_type import OperationalLimitType


from google.appengine.ext import db
# >>> imports

class OperationalLimit(IdentifiedObject):
    """ A value associated with a specific kind of limit. 
    """
    # <<< operational_limit.attributes
    # @generated
    # >>> operational_limit.attributes

    # <<< operational_limit.references
    # @generated
    # The limit set to which the limit values belong. 
    operational_limit_set = db.ReferenceProperty(OperationalLimitSet, collection_name="operational_limit_value")

    # The limit type associated with this limit. 
    operational_limit_type = db.ReferenceProperty(OperationalLimitType, collection_name="operational_limit")

    # >>> operational_limit.references

    # <<< operational_limit.operations
    # @generated
    # >>> operational_limit.operations

# EOF -------------------------------------------------------------------------
