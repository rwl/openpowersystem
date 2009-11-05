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

cdpsm_pkg_map = {
    "Element": "cdpsm.element",
    "Model": "cdpsm.model",
    "DistributionTransformerWinding": "cdpsm.iec61968.wires_ext.distribution_transformer_winding",
    "DistributionLineSegment": "cdpsm.iec61968.wires_ext.distribution_line_segment",
    "WindingPiImpedance": "cdpsm.iec61968.wires_ext.winding_pi_impedance",
    "DistributionTapChanger": "cdpsm.iec61968.wires_ext.distribution_tap_changer",
    "PerLengthSequenceImpedance": "cdpsm.iec61968.wires_ext.per_length_sequence_impedance",
    "TransformerBank": "cdpsm.iec61968.wires_ext.transformer_bank",
    "PerLengthPhaseImpedance": "cdpsm.iec61968.wires_ext.per_length_phase_impedance",
    "DistributionTransformer": "cdpsm.iec61968.wires_ext.distribution_transformer",
    "PhaseImpedanceData": "cdpsm.iec61968.wires_ext.phase_impedance_data",
    "TransformerInfo": "cdpsm.iec61968.asset_models.transformer_info",
    "ToWindingSpec": "cdpsm.iec61968.asset_models.to_winding_spec",
    "WireArrangement": "cdpsm.iec61968.asset_models.wire_arrangement",
    "CableInfo": "cdpsm.iec61968.asset_models.cable_info",
    "OpenCircuitTest": "cdpsm.iec61968.asset_models.open_circuit_test",
    "ConcentricNeutralCableInfo": "cdpsm.iec61968.asset_models.concentric_neutral_cable_info",
    "ConductorInfo": "cdpsm.iec61968.asset_models.conductor_info",
    "DistributionWindingTest": "cdpsm.iec61968.asset_models.distribution_winding_test",
    "WireType": "cdpsm.iec61968.asset_models.wire_type",
    "WindingInfo": "cdpsm.iec61968.asset_models.winding_info",
    "OverheadConductorInfo": "cdpsm.iec61968.asset_models.overhead_conductor_info",
    "TapeShieldCableInfo": "cdpsm.iec61968.asset_models.tape_shield_cable_info",
    "ShortCircuitTest": "cdpsm.iec61968.asset_models.short_circuit_test",
    "GeoLocation": "cdpsm.iec61968.common.geo_location",
    "Location": "cdpsm.iec61968.common.location",
    "PositionPoint": "cdpsm.iec61968.common.position_point",
    "IEC61970CIMVersion": "cdpsm.iec61970.iec61970_cimversion",
    "BusbarSection": "cdpsm.iec61970.wires.busbar_section",
    "LoadBreakSwitch": "cdpsm.iec61970.wires.load_break_switch",
    "TapChanger": "cdpsm.iec61970.wires.tap_changer",
    "Fuse": "cdpsm.iec61970.wires.fuse",
    "Junction": "cdpsm.iec61970.wires.junction",
    "ACLineSegment": "cdpsm.iec61970.wires.acline_segment",
    "Disconnector": "cdpsm.iec61970.wires.disconnector",
    "EnergySource": "cdpsm.iec61970.wires.energy_source",
    "SynchronousMachine": "cdpsm.iec61970.wires.synchronous_machine",
    "RatioTapChanger": "cdpsm.iec61970.wires.ratio_tap_changer",
    "EnergyConsumer": "cdpsm.iec61970.wires.energy_consumer",
    "Switch": "cdpsm.iec61970.wires.switch",
    "Line": "cdpsm.iec61970.wires.line",
    "ShuntCompensator": "cdpsm.iec61970.wires.shunt_compensator",
    "Breaker": "cdpsm.iec61970.wires.breaker",
    "Conductor": "cdpsm.iec61970.wires.conductor",
    "ConnectivityNodeContainer": "cdpsm.iec61970.core.connectivity_node_container",
    "VoltageLevel": "cdpsm.iec61970.core.voltage_level",
    "Bay": "cdpsm.iec61970.core.bay",
    "Equipment": "cdpsm.iec61970.core.equipment",
    "BaseVoltage": "cdpsm.iec61970.core.base_voltage",
    "PSRType": "cdpsm.iec61970.core.psrtype",
    "EquipmentContainer": "cdpsm.iec61970.core.equipment_container",
    "IdentifiedObject": "cdpsm.iec61970.core.identified_object",
    "Substation": "cdpsm.iec61970.core.substation",
    "ConductingEquipment": "cdpsm.iec61970.core.conducting_equipment",
    "SubGeographicalRegion": "cdpsm.iec61970.core.sub_geographical_region",
    "Terminal": "cdpsm.iec61970.core.terminal",
    "GeographicalRegion": "cdpsm.iec61970.core.geographical_region",
    "PowerSystemResource": "cdpsm.iec61970.core.power_system_resource",
    "GeneratingUnit": "cdpsm.iec61970.generation.production.generating_unit",
    "LoadResponseCharacteristic": "cdpsm.iec61970.load_model.load_response_characteristic",
    "SvTapStep": "cdpsm.iec61970.state_variables.sv_tap_step",
    "ConnectivityNode": "cdpsm.iec61970.topology.connectivity_node",
}

# EOF -------------------------------------------------------------------------
