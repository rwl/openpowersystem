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
""" Contains entities that describe dynamic measurement data exchanged between applications.Contains entities that describe dynamic measurement data exchanged between applications.
"""

from cdpsm import Element


# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

ns_prefix = "cim"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_IEC61970"

class IEC61970CIMVersion(Element):
    """ This is the IEC 61970 CIM version number assigned to this UML model file.This is the IEC 61970 CIM version number assigned to this UML model file.
    """

    # Form is YYYY-MM-DD for example for January 5, 2009 it is 2009-01-05.Form is YYYY-MM-DD for example for January 5, 2009 it is 2009-01-05.
    date = db.DateProperty()
    # Form is IEC61970CIMXXvYY where XX is the major CIM package version and the YY is the minor version.   For ecample IEC61970CIM13v18.Form is IEC61970CIMXXvYY where XX is the major CIM package version and the YY is the minor version.   For ecample IEC61970CIM13v18.
    version = db.StringProperty()


