# Copyright (C) 2009 Richard W. Lincoln
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation; version 2 dated June, 1991.
#
# This software is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANDABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA



# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

Resistance = db.FloatProperty(0)

PU = db.FloatProperty(0)

Money = db.FloatProperty(0)

Seconds = db.FloatProperty(0)

ActivePower = db.FloatProperty(0)

IntegerQuantity = db.IntegerProperty(0)

ApparentPower = db.FloatProperty(0)

PerCent = db.FloatProperty(0)

Conductance = db.FloatProperty(0)

Volume = db.FloatProperty(0)

Voltage = db.FloatProperty(0)

AbsoluteDate = db.StringProperty()

Frequency = db.FloatProperty(0)

ReactivePower = db.FloatProperty(0)

CurrentFlow = db.FloatProperty(0)

RealEnergy = db.FloatProperty(0)

AngleRadians = db.FloatProperty(0)

Reactance = db.FloatProperty(0)

Temperature = db.FloatProperty(0)

Length = db.FloatProperty(0)

WaterLevel = db.FloatProperty(0)

Impedance = db.FloatProperty(0)

Hours = db.FloatProperty(0)

FloatQuantity = db.FloatProperty(0)

AngleDegrees = db.FloatProperty(0)

ActivePowerChangeRate = db.FloatProperty(0)

Weight = db.FloatProperty(0)

Capacitance = db.FloatProperty(0)

Minutes = db.FloatProperty(0)

Susceptance = db.FloatProperty(0)

StringQuantity = db.StringProperty()

VoltagePerReactivePower = db.FloatProperty(0)

Pressure = db.FloatProperty(0)

RotationSpeed = db.FloatProperty(0)

CostRate = db.FloatProperty(0)

CostPerEnergyUnit = db.FloatProperty(0)

KWActivePower = db.FloatProperty(0)

Damping = db.FloatProperty(0)

Inductance = db.FloatProperty(0)

Admittance = db.FloatProperty(0)

MonetaryAmountRate = db.StringProperty(choices=("usd_per_s", "eur_per_s"))

UnitMultiplier = db.StringProperty(choices=("micro", "none", "c", "n", "m", "t", "g", "m", "p", "k", "d"))

Currency = db.StringProperty(choices=("rur", "inr", "cad", "dkk", "cny", "usd", "sek", "aud", "jpy", "gbp", "eur", "nok", "chf", "other"))

MonetaryAmountPerEnergyUnit = db.StringProperty(choices=("eur_per_wh", "usd_per_wh"))

UnitSymbol = db.StringProperty(choices=("_c", "m2", "hz-1", "rad", "vah", "v_var", "ohm", "w_hz", "s", "v", "n", "none", "varh", "hz", "s-1", "h", "a", "h", "w_s", "deg", "var", "f", "m3", "j", "s", "wh", "w", "va", "min", "j_s", "g", "m", "kg_j", "pa"))

MonetaryAmountPerHeatUnit = db.StringProperty(choices=("eur_per_j", "usd_per_j"))

ns_prefix = "cim.IEC61970.Domain"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#IEC61970.Domain"


