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

""" The class is the third level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling. 
"""

# <<< imports
# @generated
from cpsm.core.identified_object import IdentifiedObject

from cpsm.load_model.sub_load_area import SubLoadArea


from google.appengine.ext import db
# >>> imports

class LoadGroup(IdentifiedObject):
    """ The class is the third level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling. 
    """
    # <<< load_group.attributes
    # @generated
    # >>> load_group.attributes

    # <<< load_group.references
    # @generated
    # The SubLoadArea where the Loadgroup belongs. 
    sub_load_area = db.ReferenceProperty(SubLoadArea,
        collection_name="load_groups")

    # >>> load_group.references

    # <<< load_group.operations
    # @generated
    # >>> load_group.operations

# EOF -------------------------------------------------------------------------
