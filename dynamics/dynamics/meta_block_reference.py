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

""" References a control block at the internal meta dynamics model level.    These references are contained in other blocks and reference the single instance of the meta model that defines a particular block definition. One would not expect to see bock references contained within a primitive block. 
"""

# <<< imports
# @generated
from dynamics.element import Element



from google.appengine.ext import db
# >>> imports

class MetaBlockReference(Element):
    """ References a control block at the internal meta dynamics model level.    These references are contained in other blocks and reference the single instance of the meta model that defines a particular block definition. One would not expect to see bock references contained within a primitive block. 
    """
    # <<< meta_block_reference.attributes
    # @generated
    # should be enum, initial conditions vs. simulation equations 
    equation_type = db.IntegerProperty()

    # >>> meta_block_reference.attributes

    # <<< meta_block_reference.references
    # @generated
    # >>> meta_block_reference.references

    # <<< meta_block_reference.operations
    # @generated
    # >>> meta_block_reference.operations

# EOF -------------------------------------------------------------------------
