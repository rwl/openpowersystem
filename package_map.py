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

""" Defines a map of class names to their module.
"""

pkg_map = {
    "Element": "ucte",
    "Model": "ucte",
    "IEC61970CIMVersion": "ucte",
    "SvVoltage": "ucte.state_variables",
    "SvShuntCompensatorSections": "ucte.state_variables",
    "StateVariable": "ucte.state_variables",
    "SvTapStep": "ucte.state_variables",
    "SvPowerFlow": "ucte.state_variables",
    "Curve": "ucte.core",
    "ConnectivityNodeContainer": "ucte.core",
    "VoltageLevel": "ucte.core",
    "Equipment": "ucte.core",
    "BaseVoltage": "ucte.core",
    "EquipmentContainer": "ucte.core",
    "IdentifiedObject": "ucte.core",
    "Substation": "ucte.core",
    "ConductingEquipment": "ucte.core",
    "SubGeographicalRegion": "ucte.core",
    "Terminal": "ucte.core",
    "GeographicalRegion": "ucte.core",
    "CurveData": "ucte.core",
    "ControlArea": "ucte.control_area",
    "ControlAreaGeneratingUnit": "ucte.control_area",
    "TieFlow": "ucte.control_area",
    "WindGeneratingUnit": "ucte.generation.production",
    "GeneratingUnit": "ucte.generation.production",
    "FossilFuel": "ucte.generation.production",
    "NuclearGeneratingUnit": "ucte.generation.production",
    "HydroGeneratingUnit": "ucte.generation.production",
    "ThermalGeneratingUnit": "ucte.generation.production",
    "HydroPump": "ucte.generation.production",
    "LoadResponseCharacteristic": "ucte.load_model",
    "TopologicalNode": "ucte.topology",
    "TopologicalIsland": "ucte.topology",
    "EquivalentEquipment": "ucte.equivalents",
    "BusbarSection": "ucte.wires",
    "TapChanger": "ucte.wires",
    "TransformerWinding": "ucte.wires",
    "RegulatingControl": "ucte.wires",
    "ReactiveCapabilityCurve": "ucte.wires",
    "ACLineSegment": "ucte.wires",
    "PhaseTapChanger": "ucte.wires",
    "MutualCoupling": "ucte.wires",
    "SynchronousMachine": "ucte.wires",
    "RatioTapChanger": "ucte.wires",
    "PowerTransformer": "ucte.wires",
    "EnergyConsumer": "ucte.wires",
    "Switch": "ucte.wires",
    "RegulatingCondEq": "ucte.wires",
    "VoltageControlZone": "ucte.wires",
    "Line": "ucte.wires",
    "ShuntCompensator": "ucte.wires",
    "Conductor": "ucte.wires",
    "CurrentLimit": "ucte.operational_limits",
    "VoltageLimit": "ucte.operational_limits",
    "OperationalLimit": "ucte.operational_limits",
    "OperationalLimitSet": "ucte.operational_limits",
    "OperationalLimitType": "ucte.operational_limits",
}
