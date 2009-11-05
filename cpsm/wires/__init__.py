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

""" An extension to the Core and Topology package that models information on the electrical characteristics of Transmission and Distribution networks. This package is used by network applications such as State Estimation, Load Flow and Optimal Power Flow. 
"""

from google.appengine.ext import db

ns_prefix = "cim"
ns_uri = "http://iec.ch/TC57/2008/CIM-schema-cim13#Package_Wires"


SynchronousMachineOperatingMode = db.StringProperty(default="generator",
    choices=("generator", "condenser"))


TapChangerKind = db.StringProperty(default="voltageAndPhaseControl",
    choices=("voltageAndPhaseControl", "phaseControl", "fixed", "voltageControl"))


SVCControlMode = db.StringProperty(default="voltage",
    choices=("voltage", "off", "reactivePower"))


WindingType = db.StringProperty(default="primary",
    choices=("primary", "tertiary", "secondary", "quaternary"))


SynchronousMachineType = db.StringProperty(default="generator",
    choices=("generator", "generator_or_condenser", "condenser"))


TransformerControlMode = db.StringProperty(default="local",
    choices=("local", "active", "volt", "off", "reactive"))

# EOF -------------------------------------------------------------------------
