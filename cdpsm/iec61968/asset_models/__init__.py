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

""" This package is an extension of Assets package and contains the core information classes that support asset management and different network and work planning applications with specialized documentation classes describing assets of a particular product model made by a manufacturer. There are typically many instances of an asset associated with a single asset model. It also contains 'lightweight' *Info classes, which hold model attributes that can be referenced by not only Assets but also by ConductingEquipments. 
"""

from google.appengine.ext import db

ns_prefix = "cim"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_AssetModels"


CableOuterJacketKind = db.StringProperty(default="insulating",
    choices=("insulating", "other", "semiconducting", "polyethylene", "none", "linearLowDensityPolyethylene", "pvc"))


CableShieldMaterialKind = db.StringProperty(default="other",
    choices=("other", "lead", "steel", "aluminum", "copper"))


ConductorInsulationKind = db.StringProperty(default="crosslinkedPolyethylene",
    choices=("crosslinkedPolyethylene", "butyl", "treeRetardantCrosslinkedPolyethylene", "asbestosAndVarnishedCambric", "highPressureFluidFilled", "ethylenePropyleneRubber", "ozoneResistantRubber", "oilPaper", "varnishedDacronGlass", "highMolecularWeightPolyethylene", "other", "varnishedCambricCloth", "treeResistantHighMolecularWeightPolyethylene", "unbeltedPilc", "beltedPilc", "rubber", "lowCapacitanceRubber", "siliconRubber"))


ConductorMaterialKind = db.StringProperty(default="steel",
    choices=("steel", "other", "aluminum", "copper", "acsr"))


ConductorUsageKind = db.StringProperty(default="secondary",
    choices=("secondary", "other", "distribution", "transmission"))


CableConstructionKind = db.StringProperty(default="solid",
    choices=("solid", "stranded", "other", "segmental", "compacted", "sector", "compressed"))

# EOF -------------------------------------------------------------------------
