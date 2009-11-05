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


from google.appengine.ext import db

ns_prefix = "cim"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_Generators"


SynchronousGeneratorType = db.StringProperty(default="typeJ",
    choices=("typeJ", "typeF", "transient", "roundRotor", "salientPole"))


IfdBaseType = db.StringProperty(default="iffl",
    choices=("iffl", "other", "ifnl", "ifag"))


ParametersFormType = db.StringProperty(default="equivalentCircuit",
    choices=("equivalentCircuit", "timeConstantReactance"))

# EOF -------------------------------------------------------------------------
