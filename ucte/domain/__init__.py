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

""" The domain package is a data dictionary of quantities and units that define datatypes for attributes (properties) that may be used by any class in any other package.  This package contains the definition of primitive datatypes, including units of measure and permissible values. Each datatype contains a value attribute and an optional unit of measure, which is specified as a static variable initialized to the textual description of the unit of measure. The value of the 'units' string may be country or customer specific. Typical values are given. Permissible values for enumerations are listed in the documentation for the attribute using UML constraint syntax inside curly braces. Lengths of variable strings are listed in the descriptive text where required. 
"""

from google.appengine.ext import db

ns_prefix = "cim"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_Domain"

# Long unit of length. 
LongLength = db.FloatProperty(default=0.0)

# Amount of money 
Money = db.FloatProperty(default=0.0)

# Resistance (real part of impedance). 
Resistance = db.FloatProperty(default=0.0)

# Product of the RMS value of the voltage and the RMS value of the current 
ApparentPower = db.FloatProperty(default=0.0)

# Phase angle in radians 
AngleRadians = db.FloatProperty(default=0.0)

# Product of RMS value of the voltage and the RMS value of the in-phase component of the current 
ActivePower = db.FloatProperty(default=0.0)

# Imaginary part of admittance. 
Susceptance = db.FloatProperty(default=0.0)

# Electrical current (positive flow is out of the ConductingEquipment into the ConnectivityNode) 
CurrentFlow = db.FloatProperty(default=0.0)

# Factor by which voltage must be multiplied to give corresponding power lost from a circuit. Real part of admittance. 
Conductance = db.FloatProperty(default=0.0)

# Reactance (imaginary part of impedance), at rated frequency. 
Reactance = db.FloatProperty(default=0.0)

# Time, in seconds 
Seconds = db.FloatProperty(default=0.0)

# Electrical voltage. 
Voltage = db.FloatProperty(default=0.0)

# Product of RMS value of the voltage and the RMS value of the quadrature component of the current. 
ReactivePower = db.FloatProperty(default=0.0)

# Measurement of angle in degrees 
AngleDegrees = db.FloatProperty(default=0.0)

# Normally 0 - 100 on a defined base 
PerCent = db.FloatProperty(default=0.0)

# EOF -------------------------------------------------------------------------
