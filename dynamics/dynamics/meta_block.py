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

""" A block is a meta-data representation of a control block.   It has an external interface and an optinal internal interface. Blocks internals can be ommitted if the block is well understood by both exchange parties.    When well understood by both partice the block can be treated as a primitive block.   All dynamic models must be defined to the level of primtive blocks in order for the model to be consumed and used for dynamic simulation. Examples of primitive blocks include a well known IEEE exciter model, a summation block, or an integrator block. 
"""

# <<< imports
# @generated
from dynamics.element import Element



from google.appengine.ext import db
# >>> imports

class MetaBlock(Element):
    """ A block is a meta-data representation of a control block.   It has an external interface and an optinal internal interface. Blocks internals can be ommitted if the block is well understood by both exchange parties.    When well understood by both partice the block can be treated as a primitive block.   All dynamic models must be defined to the level of primtive blocks in order for the model to be consumed and used for dynamic simulation. Examples of primitive blocks include a well known IEEE exciter model, a summation block, or an integrator block. 
    """
    # <<< meta_block.attributes
    # @generated
    # This block is a proprietary block. Only inputs, outputs and parameters are exchanged. 
    proprietary = db.BooleanProperty()

    # >>> meta_block.attributes

    # <<< meta_block.references
    # @generated
    # >>> meta_block.references

    # <<< meta_block.operations
    # @generated
    # >>> meta_block.operations

# EOF -------------------------------------------------------------------------
