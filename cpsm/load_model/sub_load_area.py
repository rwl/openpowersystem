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

""" The class is the second level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling. 
"""

# <<< imports
# @generated
from cpsm.load_model.energy_area import EnergyArea

from cpsm.load_model.load_area import LoadArea


from google.appengine.ext import db
# >>> imports

class SubLoadArea(EnergyArea):
    """ The class is the second level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling. 
    """
    # <<< sub_load_area.attributes
    # @generated
    # >>> sub_load_area.attributes

    # <<< sub_load_area.references
    # @generated
    # Virtual property. The Loadgroups in the SubLoadArea.  
    pass # load_groups

    # The LoadArea where the SubLoadArea belongs. 
    load_area = db.ReferenceProperty(LoadArea,
        collection_name="sub_load_areas")

    # >>> sub_load_area.references

    # <<< sub_load_area.operations
    # @generated
    # >>> sub_load_area.operations

# EOF -------------------------------------------------------------------------
