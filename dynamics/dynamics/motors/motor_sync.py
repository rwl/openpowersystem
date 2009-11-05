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

class MotorSync(RotatingMachine):
    """ A large industrial motor or group of similar motors.  They are represented as <b>generators with negative Pgen</b> in the static (power flow) data. 
    """
    # <<< motor_sync.attributes
    # @generated
    # >>> motor_sync.attributes

    # <<< motor_sync.references
    # @generated
    # >>> motor_sync.references

    # <<< motor_sync.operations
    # @generated
    # >>> motor_sync.operations

# EOF -------------------------------------------------------------------------
