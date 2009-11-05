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

""" A meter for measuring customer energy consumption. The typeName attribute indicates the type of customer meter. 
"""

# <<< imports
# @generated
from cpsm.load_model.conform_load import ConformLoad



from google.appengine.ext import db
# >>> imports

class CustomerLoad(ConformLoad):
    """ A meter for measuring customer energy consumption. The typeName attribute indicates the type of customer meter. 
    """
    # <<< customer_load.attributes
    # @generated
    # >>> customer_load.attributes

    # <<< customer_load.references
    # @generated
    # >>> customer_load.references

    # <<< customer_load.operations
    # @generated
    # >>> customer_load.operations

# EOF -------------------------------------------------------------------------
