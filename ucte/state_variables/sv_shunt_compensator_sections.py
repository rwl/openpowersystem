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

""" State variable for the number of sections in service for a shunt compensator. A SvShuntCompensator is always associated with any instance of ShuntCompensator.   The sections or continuousSections values are specified depending upon the value of the associated RegulatingControl.discrete attribute.  If no RegulatingControl is associated, then the ShuntCompensator is treated as discrete.    In discrete mode, the 'sections' attribute must be present.   In the not 'discrete' mode (continuous mode) the 'continuousSections' attribute must be present.     In the case the Terminal.connected value is 'false' the specificed number of sections is not meaningful to the powerflow solution and powerflow implementations should interpret this as zero injection.   Note that an SvShuntCompensatorSections should be supplied even for ShuntCompensators whose Terminal.connected status is 'false' to keep total number of ShuntCompensator and SvShuntCompensatorSection objects in the model the same. 
"""

# <<< imports
# @generated
from ucte.state_variables.state_variable import StateVariable



from google.appengine.ext import db
# >>> imports

class SvShuntCompensatorSections(StateVariable):
    """ State variable for the number of sections in service for a shunt compensator. A SvShuntCompensator is always associated with any instance of ShuntCompensator.   The sections or continuousSections values are specified depending upon the value of the associated RegulatingControl.discrete attribute.  If no RegulatingControl is associated, then the ShuntCompensator is treated as discrete.    In discrete mode, the 'sections' attribute must be present.   In the not 'discrete' mode (continuous mode) the 'continuousSections' attribute must be present.     In the case the Terminal.connected value is 'false' the specificed number of sections is not meaningful to the powerflow solution and powerflow implementations should interpret this as zero injection.   Note that an SvShuntCompensatorSections should be supplied even for ShuntCompensators whose Terminal.connected status is 'false' to keep total number of ShuntCompensator and SvShuntCompensatorSection objects in the model the same. 
    """
    # <<< sv_shunt_compensator_sections.attributes
    # @generated
    # The number of sections in service as a continous variable. 
    continuous_sections = db.FloatProperty(default=0.0)

    # >>> sv_shunt_compensator_sections.attributes

    # <<< sv_shunt_compensator_sections.references
    # @generated
    # The shunt compensator for which the state applies. 
    shunt_compensator = db.ReferenceProperty(db.Model,
        collection_name="_sv_shunt_compensator_sections_set") # sv_shunt_compensator_sections

    # >>> sv_shunt_compensator_sections.references

    # <<< sv_shunt_compensator_sections.operations
    # @generated
    # >>> sv_shunt_compensator_sections.operations

# EOF -------------------------------------------------------------------------
