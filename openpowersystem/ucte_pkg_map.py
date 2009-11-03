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

""" Defines a map of class names to their module.
"""

ucte_pkg_map = {
    "Element": "ucte.element",
    "Model": "ucte.model",
    "IEC61970CIMVersion": "ucte.iec61970_cimversion",
    "SvVoltage": "ucte.state_variables.sv_voltage",
    "SvShuntCompensatorSections": "ucte.state_variables.sv_shunt_compensator_sections",
    "StateVariable": "ucte.state_variables.state_variable",
    "SvTapStep": "ucte.state_variables.sv_tap_step",
    "SvPowerFlow": "ucte.state_variables.sv_power_flow",
    "Curve": "ucte.core.curve",
    "ConnectivityNodeContainer": "ucte.core.connectivity_node_container",
    "VoltageLevel": "ucte.core.voltage_level",
    "Equipment": "ucte.core.equipment",
    "BaseVoltage": "ucte.core.base_voltage",
    "EquipmentContainer": "ucte.core.equipment_container",
    "IdentifiedObject": "ucte.core.identified_object",
    "Substation": "ucte.core.substation",
    "ConductingEquipment": "ucte.core.conducting_equipment",
    "SubGeographicalRegion": "ucte.core.sub_geographical_region",
    "Terminal": "ucte.core.terminal",
    "GeographicalRegion": "ucte.core.geographical_region",
    "CurveData": "ucte.core.curve_data",
    "ControlArea": "ucte.control_area.control_area",
    "ControlAreaGeneratingUnit": "ucte.control_area.control_area_generating_unit",
    "TieFlow": "ucte.control_area.tie_flow",
    "WindGeneratingUnit": "ucte.generation.production.wind_generating_unit",
    "GeneratingUnit": "ucte.generation.production.generating_unit",
    "FossilFuel": "ucte.generation.production.fossil_fuel",
    "NuclearGeneratingUnit": "ucte.generation.production.nuclear_generating_unit",
    "HydroGeneratingUnit": "ucte.generation.production.hydro_generating_unit",
    "ThermalGeneratingUnit": "ucte.generation.production.thermal_generating_unit",
    "HydroPump": "ucte.generation.production.hydro_pump",
    "LoadResponseCharacteristic": "ucte.load_model.load_response_characteristic",
    "TopologicalNode": "ucte.topology.topological_node",
    "TopologicalIsland": "ucte.topology.topological_island",
    "EquivalentEquipment": "ucte.equivalents.equivalent_equipment",
    "BusbarSection": "ucte.wires.busbar_section",
    "TapChanger": "ucte.wires.tap_changer",
    "TransformerWinding": "ucte.wires.transformer_winding",
    "RegulatingControl": "ucte.wires.regulating_control",
    "ReactiveCapabilityCurve": "ucte.wires.reactive_capability_curve",
    "ACLineSegment": "ucte.wires.acline_segment",
    "PhaseTapChanger": "ucte.wires.phase_tap_changer",
    "MutualCoupling": "ucte.wires.mutual_coupling",
    "SynchronousMachine": "ucte.wires.synchronous_machine",
    "RatioTapChanger": "ucte.wires.ratio_tap_changer",
    "PowerTransformer": "ucte.wires.power_transformer",
    "EnergyConsumer": "ucte.wires.energy_consumer",
    "Switch": "ucte.wires.switch",
    "RegulatingCondEq": "ucte.wires.regulating_cond_eq",
    "VoltageControlZone": "ucte.wires.voltage_control_zone",
    "Line": "ucte.wires.line",
    "ShuntCompensator": "ucte.wires.shunt_compensator",
    "Conductor": "ucte.wires.conductor",
    "CurrentLimit": "ucte.operational_limits.current_limit",
    "VoltageLimit": "ucte.operational_limits.voltage_limit",
    "OperationalLimit": "ucte.operational_limits.operational_limit",
    "OperationalLimitSet": "ucte.operational_limits.operational_limit_set",
    "OperationalLimitType": "ucte.operational_limits.operational_limit_type",
}

# EOF -------------------------------------------------------------------------
