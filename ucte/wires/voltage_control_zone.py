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

""" An area of the power system network which is defined for secondary voltage control purposes. A voltage control zone consists of a collection of substations with a designated bus bar section whose voltage will be controlled. 
"""

# <<< imports
# @generated
from ucte.core.identified_object import IdentifiedObject



from google.appengine.ext import db
# >>> imports

class VoltageControlZone(IdentifiedObject):
    """ An area of the power system network which is defined for secondary voltage control purposes. A voltage control zone consists of a collection of substations with a designated bus bar section whose voltage will be controlled. 
    """
    # <<< voltage_control_zone.attributes
    # @generated
    # >>> voltage_control_zone.attributes

    # <<< voltage_control_zone.references
    # @generated
    # A VoltageControlZone is controlled by a designated BusbarSection.  
    busbar_section = db.ReferenceProperty(db.Model,
        collection_name="_voltage_control_zone_set") # voltage_control_zone

    # >>> voltage_control_zone.references

    # <<< voltage_control_zone.operations
    # @generated
    # >>> voltage_control_zone.operations

# EOF -------------------------------------------------------------------------
