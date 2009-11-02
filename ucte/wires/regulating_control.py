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

""" Specifies a set of equipment that works together to control a power system quantity such as voltage or flow. Regulating control scheme in which this equipment participates. 
"""

# <<< imports
# @generated
from ucte.core.identified_object import IdentifiedObject

from ucte.core.terminal import Terminal

from ucte.wires import RegulatingControlModeKind

from google.appengine.ext import db
# >>> imports

class RegulatingControl(IdentifiedObject):
    """ Specifies a set of equipment that works together to control a power system quantity such as voltage or flow. Regulating control scheme in which this equipment participates. 
    """
    # <<< regulating_control.attributes
    # @generated
    # The regulating control mode presently available.  This specifications allows for determining the kind of regualation without need for obtaining the units from a schedule. 
    mode = RegulatingControlModeKind

    # The regulation is performed in a discrete mode. 
    discrete = db.BooleanProperty()

    # The target value specified for case input.   This value can be used for the target value wihout the use of schedules. The value has the units appropriate to the mode attribute. 
    target_value = db.FloatProperty()

    # This is the case input target range.   This performs the same function as the value2 attribute on the regulation schedule in the case that schedules are not used.   The units of those appropriate for the mode. 
    target_range = db.FloatProperty()

    # >>> regulating_control.attributes

    # <<< regulating_control.references
    # @generated
    # The terminal associated with this regulating control. 
    terminal = db.ReferenceProperty(Terminal, collection_name="regulating_control")

    # Virtual property. copy from reg cond eq  
    pass # regulating_cond_eq

    # Virtual property. copy from reg conduting eq  
    pass # tap_changer

    # >>> regulating_control.references

    # <<< regulating_control.operations
    # @generated
    # >>> regulating_control.operations

# EOF -------------------------------------------------------------------------
