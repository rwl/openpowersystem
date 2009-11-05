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

""" The class is the root or first level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling. 
"""

# <<< imports
# @generated
from cpsm.load_model.energy_area import EnergyArea



from google.appengine.ext import db
# >>> imports

class LoadArea(EnergyArea):
    """ The class is the root or first level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling. 
    """
    # <<< load_area.attributes
    # @generated
    # >>> load_area.attributes

    # <<< load_area.references
    # @generated
    # Virtual property. The SubLoadAreas in the LoadArea.  
    pass # sub_load_areas

    # >>> load_area.references

    # <<< load_area.operations
    # @generated
    # >>> load_area.operations

# EOF -------------------------------------------------------------------------
