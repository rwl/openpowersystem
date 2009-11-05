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

""" Apparent power limit. 
"""

# <<< imports
# @generated
from cpsm.operational_limits.operational_limit import OperationalLimit


from cpsm.domain import ApparentPower

from google.appengine.ext import db
# >>> imports

class ApparentPowerLimit(OperationalLimit):
    """ Apparent power limit. 
    """
    # <<< apparent_power_limit.attributes
    # @generated
    # The apparent power limit. 
    value = ApparentPower

    # >>> apparent_power_limit.attributes

    # <<< apparent_power_limit.references
    # @generated
    # >>> apparent_power_limit.references

    # <<< apparent_power_limit.operations
    # @generated
    # >>> apparent_power_limit.operations

# EOF -------------------------------------------------------------------------
