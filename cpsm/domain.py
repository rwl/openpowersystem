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

""" The domain package is a data dictionary of quantities and units that define datatypes for attributes (properties) that may be used by any class in any other package.  This package contains the definition of primitive datatypes, including units of measure and permissible values. Each datatype contains a value attribute and an optional unit of measure, which is specified as a static variable initialized to the textual description of the unit of measure. The value of the 'units' string may be country or customer specific. Typical values are given. Permissible values for enumerations are listed in the documentation for the attribute using UML constraint syntax inside curly braces. Lengths of variable strings are listed in the descriptive text where required.The domain package is a data dictionary of quantities and units that define datatypes for attributes (properties) that may be used by any class in any other package.  This package contains the definition of primitive datatypes, including units of measure and permissible values. Each datatype contains a value attribute and an optional unit of measure, which is specified as a static variable initialized to the textual description of the unit of measure. The value of the 'units' string may be country or customer specific. Typical values are given. Permissible values for enumerations are listed in the documentation for the attribute using UML constraint syntax inside curly braces. Lengths of variable strings are listed in the descriptive text where required.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------



# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

#------------------------------------------------------------------------------
#  Properties:
#------------------------------------------------------------------------------
# http://www.w3.org/2001/XMLSchema#floatElectrical current (positive flow is out of the ConductingEquipment into the ConnectivityNode)Electrical current (positive flow is out of the ConductingEquipment into the ConnectivityNode)"
CurrentFlow = db.FloatProperty()
# http://www.w3.org/2001/XMLSchema#floatProduct of RMS value of the voltage and the RMS value of the in-phase component of the currentProduct of RMS value of the voltage and the RMS value of the in-phase component of the current"
ActivePower = db.FloatProperty()
# http://www.w3.org/2001/XMLSchema#floatTime, in secondsTime, in seconds"
Seconds = db.FloatProperty()
# http://www.w3.org/2001/XMLSchema#floatImaginary part of admittance.Imaginary part of admittance."
Susceptance = db.FloatProperty()
# http://www.w3.org/2001/XMLSchema#floatFactor by which voltage must be multiplied to give corresponding power lost from a circuit. Real part of admittance.Factor by which voltage must be multiplied to give corresponding power lost from a circuit. Real part of admittance."
Conductance = db.FloatProperty()
# http://www.w3.org/2001/XMLSchema#floatResistance (real part of impedance).Resistance (real part of impedance)."
Resistance = db.FloatProperty()
# http://www.w3.org/2001/XMLSchema#floatNormally 0 - 100 on a defined baseNormally 0 - 100 on a defined base"
PerCent = db.FloatProperty()
# http://www.w3.org/2001/XMLSchema#floatProduct of RMS value of the voltage and the RMS value of the quadrature component of the current.Product of RMS value of the voltage and the RMS value of the quadrature component of the current."
ReactivePower = db.FloatProperty()
# http://www.w3.org/2001/XMLSchema#floatMeasurement of angle in degreesMeasurement of angle in degrees"
AngleDegrees = db.FloatProperty()
# http://www.w3.org/2001/XMLSchema#floatElectrical voltage.Electrical voltage."
Voltage = db.FloatProperty()
# http://www.w3.org/2001/XMLSchema#floatProduct of the RMS value of the voltage and the RMS value of the currentProduct of the RMS value of the voltage and the RMS value of the current"
ApparentPower = db.FloatProperty()
# http://www.w3.org/2001/XMLSchema#floatReactance (imaginary part of impedance), at rated frequency.Reactance (imaginary part of impedance), at rated frequency."
Reactance = db.FloatProperty()
# http://www.w3.org/2001/XMLSchema#floatVoltage variation with reactive powerVoltage variation with reactive power"
VoltagePerReactivePower = db.FloatProperty()

UnitSymbol = db.StringProperty(choices=("w/s", "none", "s", "h", "j/s", "va", "wh", "ohm", "m3", "hz-1", "w", "min", "rad", "g", "j", "h", "f", "kg/j", "vah", "s-1", "deg_c", "deg", "pa", "var", "s", "w/hz", "m", "m2", "hz", "a", "n", "v/var", "varh", "v"))

#------------------------------------------------------------------------------
#  Constants:
#------------------------------------------------------------------------------

NS_PREFIX = "cim"
NS_URI = "http://iec.ch/TC57/2008/CIM-schema-cim13#Package_Domain"



# EOF -------------------------------------------------------------------------
