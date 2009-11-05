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

""" This is a root class to provide common naming attributes for all classes needing naming attributes 
"""

# <<< imports
# @generated
from cpsm.element import Element



from google.appengine.ext import db
# >>> imports

class IdentifiedObject(Element):
    """ This is a root class to provide common naming attributes for all classes needing naming attributes 
    """
    # <<< identified_object.attributes
    # @generated
    # The pathname is a system unique name composed from all IdentifiedObject.localNames in a naming hierarchy path from the object to the root. 
    path_name = db.StringProperty()

    # The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. 
    description = db.StringProperty()

    # The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy. 
    alias_name = db.StringProperty()

    # The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy. 
    name = db.StringProperty()

    # >>> identified_object.attributes

    # <<< identified_object.references
    # @generated
    # >>> identified_object.references

    # <<< identified_object.operations
    # @generated
    # >>> identified_object.operations

# EOF -------------------------------------------------------------------------
