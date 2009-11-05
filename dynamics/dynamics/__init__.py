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

""" This package models generalized dynamic models. Standard models and user defined dynamics models are included.  In some ways this duplicates the partial modeling that was done in the GenerationDynamics package, but it far exceeds that package in terms of flexibility and extensibility.   This package does not attempt to fully specficfy all possible dynamics models in specific UML, but rather builds a framework in which to exchange standard or custom dyanmics models based on 'well known' block functions. 
"""

from google.appengine.ext import db

ns_prefix = "cim"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_Dynamics"


BlockKind = db.StringProperty(default="dotDotDot",
    choices=("dotDotDot", "govenor", "automaticVoltageControl", "turbine", "exciter", "powerSystemStabilizer", "energySource"))

# EOF -------------------------------------------------------------------------
