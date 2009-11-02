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

""" A generating unit whose prime mover could be a steam turbine, combustion turbine, or diesel engine. 
"""

# <<< imports
# @generated
from ucte.generation.production.generating_unit import GeneratingUnit



from google.appengine.ext import db
# >>> imports

class ThermalGeneratingUnit(GeneratingUnit):
    """ A generating unit whose prime mover could be a steam turbine, combustion turbine, or diesel engine. 
    """
    # <<< thermal_generating_unit.attributes
    # @generated
    # >>> thermal_generating_unit.attributes

    # <<< thermal_generating_unit.references
    # @generated
    # A thermal generating unit may have one or more fossil fuels The UCTE profile allows only one type of fuel per ThermalGeneratingUnit. 
    fossil_fuels = db.ReferenceProperty(db.Model, collection_name="_thermal_generating_unit_set")

    # >>> thermal_generating_unit.references

    # <<< thermal_generating_unit.operations
    # @generated
    # >>> thermal_generating_unit.operations

# EOF -------------------------------------------------------------------------
