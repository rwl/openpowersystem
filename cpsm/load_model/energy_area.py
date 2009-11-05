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

""" The class describes an area having energy production or consumption. The class is the basis for further specialization. 
"""

# <<< imports
# @generated
from cpsm.core.identified_object import IdentifiedObject



from google.appengine.ext import db
# >>> imports

class EnergyArea(IdentifiedObject):
    """ The class describes an area having energy production or consumption. The class is the basis for further specialization. 
    """
    # <<< energy_area.attributes
    # @generated
    # >>> energy_area.attributes

    # <<< energy_area.references
    # @generated
    # The control area specification that is used for the load forecast.  
    control_area = db.ReferenceProperty(db.Model,
        collection_name="_energy_area_set") # energy_area

    # >>> energy_area.references

    # <<< energy_area.operations
    # @generated
    # >>> energy_area.operations

# EOF -------------------------------------------------------------------------
