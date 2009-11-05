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
from cpsm.generation.production.generating_unit import GeneratingUnit


from google.appengine.ext import db
# >>> imports

class ControlAreaGeneratingUnit(Element):
    """ A control area generating unit. This class is needed so that alternate control area definitions may include the same generating unit.   Note only one instance within a control area should reference a specific generating unit. 
    """
    # <<< control_area_generating_unit.attributes
    # @generated
    # >>> control_area_generating_unit.attributes

    # <<< control_area_generating_unit.references
    # @generated
    # The parent control area for the generating unit specifications. 
    control_area = db.ReferenceProperty(ControlArea,
        collection_name="control_area_generating_unit")

    # The generating unit specified for this control area.  Note that a control area should include a GeneratingUnit only once. 
    generating_unit = db.ReferenceProperty(GeneratingUnit,
        collection_name="control_area_generating_unit")

    # >>> control_area_generating_unit.references

    # <<< control_area_generating_unit.operations
    # @generated
    # >>> control_area_generating_unit.operations

# EOF -------------------------------------------------------------------------
