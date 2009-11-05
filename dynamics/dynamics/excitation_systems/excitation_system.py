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

class ExcitationSystem(Element):
    """ An excitation system provides the field voltage (Efd) for a synchronous machine model. It is linked to a specific generator by the Bus number and Unit ID. 
    """
    # <<< excitation_system.attributes
    # @generated
    # >>> excitation_system.attributes

    # <<< excitation_system.references
    # @generated
    # >>> excitation_system.references

    # <<< excitation_system.operations
    # @generated
    # >>> excitation_system.operations

# EOF -------------------------------------------------------------------------
