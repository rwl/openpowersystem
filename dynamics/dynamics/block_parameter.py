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

""" Specification of a paramter for use in a dynamic block. This is a paramters like a time constant that could be unique for each instance of, for example, an exciter in the model. 
"""

# <<< imports
# @generated
from dynamics.element import Element



from google.appengine.ext import db
# >>> imports

class BlockParameter(Element):
    """ Specification of a paramter for use in a dynamic block. This is a paramters like a time constant that could be unique for each instance of, for example, an exciter in the model. 
    """
    # <<< block_parameter.attributes
    # @generated
    # The paramter value for this instance of a dynamic block usage. 
    value = db.FloatProperty()

    # >>> block_parameter.attributes

    # <<< block_parameter.references
    # @generated
    # >>> block_parameter.references

    # <<< block_parameter.operations
    # @generated
    # >>> block_parameter.operations

# EOF -------------------------------------------------------------------------
