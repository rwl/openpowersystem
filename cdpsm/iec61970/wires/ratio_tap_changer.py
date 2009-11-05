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

""" A tap changer that changes the voltage ratio impacting the voltage magnitude but not direclty the phase angle across the transformer.. 
"""

# <<< imports
# @generated
from cdpsm.iec61970.wires.tap_changer import TapChanger


from cdpsm.iec61970.wires import TransformerControlMode

from google.appengine.ext import db
# >>> imports

class RatioTapChanger(TapChanger):
    """ A tap changer that changes the voltage ratio impacting the voltage magnitude but not direclty the phase angle across the transformer.. 
    """
    # <<< ratio_tap_changer.attributes
    # @generated
    # Specifies the regulation control mode (voltage or reactive) of the RatioTapChanger. 
    tcul_control_mode = TransformerControlMode

    # >>> ratio_tap_changer.attributes

    # <<< ratio_tap_changer.references
    # @generated
    # Winding to which this ratio tap changer belongs. 
    winding = db.ReferenceProperty(db.Model,
        collection_name="_ratio_tap_changer_set") # ratio_tap_changer

    # >>> ratio_tap_changer.references

    # <<< ratio_tap_changer.operations
    # @generated
    # >>> ratio_tap_changer.operations

# EOF -------------------------------------------------------------------------
