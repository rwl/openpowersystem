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

""" Output state of a block.   This is a public interface external to the block.    One or more block outputs should be specified in order to link blocks together.    Certain block kinds might require a specific output.   For example, an exciter block might require an output called 'Ea'. 
"""

# <<< imports
# @generated
from dynamics.dynamics.meta_block_connectable import MetaBlockConnectable



from google.appengine.ext import db
# >>> imports

class MetaBlockOutput(MetaBlockConnectable):
    """ Output state of a block.   This is a public interface external to the block.    One or more block outputs should be specified in order to link blocks together.    Certain block kinds might require a specific output.   For example, an exciter block might require an output called 'Ea'. 
    """
    # <<< meta_block_output.attributes
    # @generated
    # >>> meta_block_output.attributes

    # <<< meta_block_output.references
    # @generated
    # >>> meta_block_output.references

    # <<< meta_block_output.operations
    # @generated
    # >>> meta_block_output.operations

# EOF -------------------------------------------------------------------------
