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

""" The ControlArea package models area specifications which can be used for a variety of purposes.  The package as a whole models potentially overlapping control area specifications for the purpose of actual generation control, load forecast area load capture, or powerflow based analysis. 
"""

# <<< imports
# @generated
from ucte.core import IdentifiedObject
from ucte import Element

from ucte.domain import ActivePower

from google.appengine.ext import db
# >>> imports

# <<< properties
# @generated
# >>> properties

# <<< constants
# @generated
NS_PREFIX = "cim"
NS_URI = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_ControlArea"
# >>> constants

class ControlArea(IdentifiedObject):
    """ A <b>control area </b>is a grouping of <b>generating units</b> and/or loads and a cutset of tie lines (as <b>terminals</b>) which may be used for a variety of purposes including automatic generation control, powerflow solution area interchange control specification, and input to load forecasting.   Note that any number of overlapping control area specifications can be superimposed on the physical model. 
    """
    # <<< control_area.attributes
    # @generated
    # Active power net interchange tolerance 
    p_tolerance = ActivePower

    # The specified positive net interchange into the control area. 
    net_interchange = ActivePower

    # >>> control_area.attributes

    # <<< control_area.references
    # @generated
    # Virtual property. The topological nodes included in the control area.  
    pass # topological_node

    # Virtual property. The tie flows associated with the control area.  
    pass # tie_flow

    # Virtual property. The generating unit specificaitons for the control area.  
    pass # control_area_generating_unit

    # >>> control_area.references

    # <<< control_area.operations
    # @generated
    # >>> control_area.operations

class ControlAreaGeneratingUnit(Element):
    """ A control area generating unit. This class is needed so that alternate control area definitions may include the same generating unit.   Note only one instance within a control area should reference a specific generating unit. 
    """
    # <<< control_area_generating_unit.attributes
    # @generated
    # >>> control_area_generating_unit.attributes

    # <<< control_area_generating_unit.references
    # @generated
    # The parent control area for the generating unit specifications. 
    control_area = db.ReferenceProperty(db.Model, collection_name="control_area_generating_unit")

    # The generating unit specified for this control area.  Note that a control area should include a GeneratingUnit only once. 
    generating_unit = db.ReferenceProperty(db.Model, collection_name="control_area_generating_unit")

    # >>> control_area_generating_unit.references

    # <<< control_area_generating_unit.operations
    # @generated
    # >>> control_area_generating_unit.operations

class TieFlow(Element):
    """ A flow specification in terms of location and direction for a control area. 
    """
    # <<< tie_flow.attributes
    # @generated
    # The flow is positive into the terminal.  A flow is positive if it is an import into the control area. The power flow is positive into the Terminal of the ConductingEquipment. 
    positive_flow_in = db.BooleanProperty()

    # >>> tie_flow.attributes

    # <<< tie_flow.references
    # @generated
    # The control area of the tie flows. 
    control_area = db.ReferenceProperty(db.Model, collection_name="tie_flow")

    # The terminal to which this tie flow belongs. 
    terminal = db.ReferenceProperty(db.Model, collection_name="tie_flow")

    # >>> tie_flow.references

    # <<< tie_flow.operations
    # @generated
    # >>> tie_flow.operations



# EOF -------------------------------------------------------------------------
