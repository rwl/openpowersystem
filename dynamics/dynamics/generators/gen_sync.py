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
from dynamics.dynamics.rotating_machine import RotatingMachine



from google.appengine.ext import db
# >>> imports

class GenSync(RotatingMachine):
    """ Synchronous generator model. A single standard synchronous model is defined for the CIM, with several variations indicated by the 'model type' attribute.  This model can be used for all types of synchronous machines (salient pole, solid iron rotor, etc.). 
    """
    # <<< gen_sync.attributes
    # @generated
    # >>> gen_sync.attributes

    # <<< gen_sync.references
    # @generated
    # >>> gen_sync.references

    # <<< gen_sync.operations
    # @generated
    # >>> gen_sync.operations

# EOF -------------------------------------------------------------------------
