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

""" State variable for transformer tap step.     Normally a profile specifies only one of the attributes 'position'or 'continuousPosition'. SvTapStep is only meant to be used for taps that change under load. 
"""

# <<< imports
# @generated
from ucte.state_variables.state_variable import StateVariable



from google.appengine.ext import db
# >>> imports

class SvTapStep(StateVariable):
    """ State variable for transformer tap step.     Normally a profile specifies only one of the attributes 'position'or 'continuousPosition'. SvTapStep is only meant to be used for taps that change under load. 
    """
    # <<< sv_tap_step.attributes
    # @generated
    # The floating point tap position. 
    continuous_position = db.FloatProperty(default=0.0)

    # >>> sv_tap_step.attributes

    # <<< sv_tap_step.references
    # @generated
    # The tap changer associated with the tap step state. 
    tap_changer = db.ReferenceProperty(db.Model,
        collection_name="_sv_tap_step_set") # sv_tap_step

    # >>> sv_tap_step.references

    # <<< sv_tap_step.operations
    # @generated
    # >>> sv_tap_step.operations

# EOF -------------------------------------------------------------------------
