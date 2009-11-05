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


# <<< imports
# @generated
from dynamics.element import Element



from google.appengine.ext import db
# >>> imports

class GenLoad(Element):
    """ Representation of a small generator as a negative load rather than a dynamic generator model. This practice is also referred to as 'netting' the generation with the load, i.e. taking the net value of load minus generation as the new load value.  For dynamic modeling purposes, each generator that does not have a dynamic load model must have a genLoad record. 
    """
    # <<< gen_load.attributes
    # @generated
    # >>> gen_load.attributes

    # <<< gen_load.references
    # @generated
    # >>> gen_load.references

    # <<< gen_load.operations
    # @generated
    # >>> gen_load.operations

# EOF -------------------------------------------------------------------------
