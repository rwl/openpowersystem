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

""" Specifies a set of equipment that works together to control a power system quantity such as voltage or flow. 
"""

# <<< imports
# @generated
from cpsm.core.power_system_resource import PowerSystemResource

from cpsm.core.terminal import Terminal
from cpsm.wires.regulation_schedule import RegulationSchedule


from google.appengine.ext import db
# >>> imports

class RegulatingControl(PowerSystemResource):
    """ Specifies a set of equipment that works together to control a power system quantity such as voltage or flow. 
    """
    # <<< regulating_control.attributes
    # @generated
    # >>> regulating_control.attributes

    # <<< regulating_control.references
    # @generated
    # The terminal associated with this regulating control. 
    terminal = db.ReferenceProperty(Terminal,
        collection_name="regulating_control")

    # Schedule for this Regulating regulating control. 
    regulation_schedule = db.ReferenceProperty(RegulationSchedule,
        collection_name="regulating_control")

    # Virtual property. copy from reg conduting eq  
    pass # tap_changer

    # Virtual property. copy from reg cond eq  
    pass # regulating_cond_eq

    # >>> regulating_control.references

    # <<< regulating_control.operations
    # @generated
    # >>> regulating_control.operations

# EOF -------------------------------------------------------------------------
