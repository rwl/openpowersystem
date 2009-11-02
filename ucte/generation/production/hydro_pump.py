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

""" A synchronous motor-driven pump, typically associated with a pumped storage plant A HydroPump is included in the profile to indicate the associated SynchronousMachine can run in pump mode. 
"""

# <<< imports
# @generated
from ucte.core.identified_object import IdentifiedObject



from google.appengine.ext import db
# >>> imports

class HydroPump(IdentifiedObject):
    """ A synchronous motor-driven pump, typically associated with a pumped storage plant A HydroPump is included in the profile to indicate the associated SynchronousMachine can run in pump mode. 
    """
    # <<< hydro_pump.attributes
    # @generated
    # >>> hydro_pump.attributes

    # <<< hydro_pump.references
    # @generated
    # The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating. 
    driven_by_synchronous_machine = db.ReferenceProperty(db.Model, collection_name="_hydro_pump_set")

    # >>> hydro_pump.references

    # <<< hydro_pump.operations
    # @generated
    # >>> hydro_pump.operations

# EOF -------------------------------------------------------------------------
