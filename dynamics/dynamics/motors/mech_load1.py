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
from dynamics.dynamics.motors.mechanical_load import MechanicalLoad



from google.appengine.ext import db
# >>> imports

class MechLoad1(MechanicalLoad):
    """ Mechanical load model 1 
    """
    # <<< mech_load1.attributes
    # @generated
    # Speed squared coefficient 
    b = db.FloatProperty()

    # Speed squared coefficient 
    a = db.FloatProperty()

    # Speed to the exponent coefficient 
    d = db.FloatProperty()

    # Exponent 
    e = db.FloatProperty()

    # >>> mech_load1.attributes

    # <<< mech_load1.references
    # @generated
    # >>> mech_load1.references

    # <<< mech_load1.operations
    # @generated
    # >>> mech_load1.operations

# EOF -------------------------------------------------------------------------
