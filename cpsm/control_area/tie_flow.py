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
from cpsm.element import Element

from cpsm.control_area.control_area import ControlArea


from google.appengine.ext import db
# >>> imports

class TieFlow(Element):
    """ A flow specification in terms of location and direction for a control area. 
    """
    # <<< tie_flow.attributes
    # @generated
    # The flow is positive into the terminal.  A flow is positive if it is an import into the control area. 
    positive_flow_in = db.BooleanProperty()

    # >>> tie_flow.attributes

    # <<< tie_flow.references
    # @generated
    # The control area of the tie flows. 
    control_area = db.ReferenceProperty(ControlArea,
        collection_name="tie_flow")

    # >>> tie_flow.references

    # <<< tie_flow.operations
    # @generated
    # >>> tie_flow.operations

# EOF -------------------------------------------------------------------------
