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

""" State variable for transformer tap step.     This class is to be used for taps of LTC (load tap changing) transformers, not fixed tap transformers.  Normally a profile specifies only one of the attributes 'position'or 'tapRatio'. 
"""

# <<< imports
# @generated
from cdpsm.element import Element



from google.appengine.ext import db
# >>> imports

class SvTapStep(Element):
    """ State variable for transformer tap step.     This class is to be used for taps of LTC (load tap changing) transformers, not fixed tap transformers.  Normally a profile specifies only one of the attributes 'position'or 'tapRatio'. 
    """
    # <<< sv_tap_step.attributes
    # @generated
    # The floating point tap position. 
    continuous_position = db.FloatProperty()

    # The integer tap position. 
    position = db.IntegerProperty()

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
