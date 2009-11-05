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

""" OIoeratuibak kimit on current. 
"""

# <<< imports
# @generated
from cpsm.operational_limits.operational_limit import OperationalLimit


from cpsm.domain import CurrentFlow

from google.appengine.ext import db
# >>> imports

class CurrentLimit(OperationalLimit):
    """ OIoeratuibak kimit on current. 
    """
    # <<< current_limit.attributes
    # @generated
    # Limit on current flow. 
    value = CurrentFlow

    # >>> current_limit.attributes

    # <<< current_limit.references
    # @generated
    # >>> current_limit.references

    # <<< current_limit.operations
    # @generated
    # >>> current_limit.operations

# EOF -------------------------------------------------------------------------
