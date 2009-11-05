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

""" A mechanical switching device capable of making, carrying, and breaking currents under normal operating conditions. 
"""

# <<< imports
# @generated
from cdpsm.iec61970.wires.switch import Switch


from cdpsm.iec61970.domain import CurrentFlow

from google.appengine.ext import db
# >>> imports

class LoadBreakSwitch(Switch):
    """ A mechanical switching device capable of making, carrying, and breaking currents under normal operating conditions. 
    """
    # <<< load_break_switch.attributes
    # @generated
    # Current carrying capacity of a wire or cable under stated thermal conditions. 
    rated_current = CurrentFlow

    # >>> load_break_switch.attributes

    # <<< load_break_switch.references
    # @generated
    # >>> load_break_switch.references

    # <<< load_break_switch.operations
    # @generated
    # >>> load_break_switch.operations

# EOF -------------------------------------------------------------------------
