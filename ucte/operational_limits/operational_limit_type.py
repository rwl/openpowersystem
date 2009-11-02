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

""" A type of limit.  The meaning of a specific limit is described in this class. 
"""

# <<< imports
# @generated
from ucte.core.identified_object import IdentifiedObject


from ucte.operational_limits import OperationalLimitDirectionKind
from ucte.domain import Seconds

from google.appengine.ext import db
# >>> imports

class OperationalLimitType(IdentifiedObject):
    """ A type of limit.  The meaning of a specific limit is described in this class. 
    """
    # <<< operational_limit_type.attributes
    # @generated
    # The direction of the limit. 
    direction = OperationalLimitDirectionKind

    # The nominal acceptable duration of the limit.  Limits are commonly expressed in terms of the a time limit for which the limit is normally acceptable.   The actual acceptable duration of a specific limit may depend on other local factors such as temperature or wind speed. 
    acceptable_duration = Seconds

    # >>> operational_limit_type.attributes

    # <<< operational_limit_type.references
    # @generated
    # Virtual property. The operational limits associated with this type of limit.  
    pass # operational_limit

    # >>> operational_limit_type.references

    # <<< operational_limit_type.operations
    # @generated
    # >>> operational_limit_type.operations

# EOF -------------------------------------------------------------------------
