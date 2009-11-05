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

""" This is a source connection for a block input at the dynamics meta-data level.   The subtypes represent different ways to obtain the numbers.  Note that a block output is NOT derived from this class since block outputs can only be computed from references to other blocks via the BlockOutputReference class. 
"""

# <<< imports
# @generated
from dynamics.element import Element



from google.appengine.ext import db
# >>> imports

class MetaBlockConnectable(Element):
    """ This is a source connection for a block input at the dynamics meta-data level.   The subtypes represent different ways to obtain the numbers.  Note that a block output is NOT derived from this class since block outputs can only be computed from references to other blocks via the BlockOutputReference class. 
    """
    # <<< meta_block_connectable.attributes
    # @generated
    # >>> meta_block_connectable.attributes

    # <<< meta_block_connectable.references
    # @generated
    # >>> meta_block_connectable.references

    # <<< meta_block_connectable.operations
    # @generated
    # >>> meta_block_connectable.operations

# EOF -------------------------------------------------------------------------
