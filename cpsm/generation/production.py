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

""" The production package is responsible for classes which describe various kinds of generators. These classes also provide production costing information which is used to economically allocate demand among committed units and calculate reserve quantities.The production package is responsible for classes which describe various kinds of generators. These classes also provide production costing information which is used to economically allocate demand among committed units and calculate reserve quantities.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from cpsm.core import Curve
from cpsm.core import Equipment

from cpsm.domain import ActivePower

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

#------------------------------------------------------------------------------
#  Properties:
#------------------------------------------------------------------------------

GeneratorControlSource = db.StringProperty(choices=("off_agc", "unavailable", "on_agc", "plant_control"))

#------------------------------------------------------------------------------
#  Constants:
#------------------------------------------------------------------------------

NS_PREFIX = "cim"
NS_URI = "http://iec.ch/TC57/2008/CIM-schema-cim13#Package_Production"

#------------------------------------------------------------------------------
#  "GrossToNetActivePowerCurve" class:
#------------------------------------------------------------------------------

class GrossToNetActivePowerCurve(Curve):
    """ Relationship between the generating unit's gross active power output on the X-axis (measured at the terminals of the machine(s)) and the generating unit's net active power output on the Y-axis (based on utility-defined measurements at the power station). Station service loads, when modeled, should be treated as non-conforming bus loads. There may be more than one curve, depending on the auxiliary equipment that is in service.Relationship between the generating unit's gross active power output on the X-axis (measured at the terminals of the machine(s)) and the generating unit's net active power output on the Y-axis (based on utility-defined measurements at the power station). Station service loads, when modeled, should be treated as non-conforming bus loads. There may be more than one curve, depending on the auxiliary equipment that is in service.
    """

    
    # A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unitA generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit
    generating_unit = db.ReferenceProperty(collection_name="gross_to_net_active_power_curves")

    # <<< gross_to_net_active_power_curve
    # @generated
    # >>> gross_to_net_active_power_curve


#------------------------------------------------------------------------------
#  "GeneratingUnit" class:
#------------------------------------------------------------------------------

class GeneratingUnit(Equipment):
    """ A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.
    """

    
    # This is the maximum operating active power limit the dispatcher can enter for this unitThis is the maximum operating active power limit the dispatcher can enter for this unit
    max_operating_p = ActivePower

    # Generating unit economic participation factorGenerating unit economic participation factor
    normal_pf = db.FloatProperty()

    # The unit's gross rated maximum capacity (Book Value).The unit's gross rated maximum capacity (Book Value).
    rated_gross_max_p = ActivePower

    # The gross rated minimum generation level which the unit can safely operate at while delivering power to the transmission gridThe gross rated minimum generation level which the unit can safely operate at while delivering power to the transmission grid
    rated_gross_min_p = ActivePower

    # The source of controls for a generating unit.The source of controls for a generating unit.
    gen_control_source = GeneratorControlSource

    # The net rated maximum capacity determined by subtracting the auxiliary power used to operate the internal plant machinery from the rated gross maximum capacityThe net rated maximum capacity determined by subtracting the auxiliary power used to operate the internal plant machinery from the rated gross maximum capacity
    rated_net_max_p = ActivePower

    # Generating unit economic participation factorGenerating unit economic participation factor
    long_pf = db.FloatProperty()

    # Default Initial active power  which is used to store a powerflow result for the initial active power for this unit in this network configurationDefault Initial active power  which is used to store a powerflow result for the initial active power for this unit in this network configuration
    initial_p = ActivePower

    # Generating unit economic participation factorGenerating unit economic participation factor
    short_pf = db.FloatProperty()

    # This is the minimum operating active power limit the dispatcher can enter for this unit.This is the minimum operating active power limit the dispatcher can enter for this unit.
    min_operating_p = ActivePower

    # Virtual property. A synchronous machine may operate as a generator and as such becomes a member of a generating unitA synchronous machine may operate as a generator and as such becomes a member of a generating unit
    pass #contains_synchronous_machines

    # Virtual property. A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unitA generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit
    pass #gross_to_net_active_power_curves

    # Virtual property. ControlArea specifications for this generating unit.ControlArea specifications for this generating unit.
    pass #control_area_generating_unit

    # <<< generating_unit
    # @generated
    # >>> generating_unit


#------------------------------------------------------------------------------
#  "HydroGeneratingUnit" class:
#------------------------------------------------------------------------------

class HydroGeneratingUnit(GeneratingUnit):
    """ A generating unit whose prime mover is a hydraulic turbine (e.g., Francis, Pelton, Kaplan)A generating unit whose prime mover is a hydraulic turbine (e.g., Francis, Pelton, Kaplan)
    """

    pass
    # <<< hydro_generating_unit
    # @generated
    # >>> hydro_generating_unit


#------------------------------------------------------------------------------
#  "ThermalGeneratingUnit" class:
#------------------------------------------------------------------------------

class ThermalGeneratingUnit(GeneratingUnit):
    """ A generating unit whose prime mover could be a steam turbine, combustion turbine, or diesel engine.A generating unit whose prime mover could be a steam turbine, combustion turbine, or diesel engine.
    """

    pass
    # <<< thermal_generating_unit
    # @generated
    # >>> thermal_generating_unit




# EOF -------------------------------------------------------------------------
