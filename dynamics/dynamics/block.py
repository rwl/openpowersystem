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

""" A specific usage of a dynamics block, supplied with parameters and any linkages to the power system static model that are required.     Sometimes a block is used to simply specify a location of input or output from dyanmics equations to the static model. 
"""

# <<< imports
# @generated
from dynamics.element import Element



from google.appengine.ext import db
# >>> imports

class Block(Element):
    """ A specific usage of a dynamics block, supplied with parameters and any linkages to the power system static model that are required.     Sometimes a block is used to simply specify a location of input or output from dyanmics equations to the static model. 
    """
    # <<< block.attributes
    # @generated
    in_service = db.BooleanProperty()

    # >>> block.attributes

    # <<< block.references
    # @generated
    # >>> block.references

    # <<< block.operations
    # @generated
    # >>> block.operations

# EOF -------------------------------------------------------------------------
