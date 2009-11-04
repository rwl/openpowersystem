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

""" The fossil fuel consumed by the non-nuclear thermal generating units, e.g., coal, oil, gas The UCTE profile allows only one type of fuel per ThermalGeneratingUnit. The UCTE profile allows only one type of fuel per ThermalGeneratingUnit. 
"""

# <<< imports
# @generated
from ucte.core.identified_object import IdentifiedObject


from ucte.generation.production import FuelType

from google.appengine.ext import db
# >>> imports

class FossilFuel(IdentifiedObject):
    """ The fossil fuel consumed by the non-nuclear thermal generating units, e.g., coal, oil, gas The UCTE profile allows only one type of fuel per ThermalGeneratingUnit. The UCTE profile allows only one type of fuel per ThermalGeneratingUnit. 
    """
    # <<< fossil_fuel.attributes
    # @generated
    # The type of fossil fuel, such as coal, oil, or gas. 
    fossil_fuel_type = FuelType

    # >>> fossil_fuel.attributes

    # <<< fossil_fuel.references
    # @generated
    # A thermal generating unit may have one or more fossil fuels  
    thermal_generating_unit = db.ReferenceProperty(db.Model,
        collection_name="_fossil_fuel_set") # fossil_fuels

    # >>> fossil_fuel.references

    # <<< fossil_fuel.operations
    # @generated
    # >>> fossil_fuel.operations

# EOF -------------------------------------------------------------------------
