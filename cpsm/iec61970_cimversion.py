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

""" This is the IEC 61970 CIM version number assigned to this UML model file. 
"""

# <<< imports
# @generated
from cpsm.element import Element



from google.appengine.ext import db
# >>> imports

class IEC61970CIMVersion(Element):
    """ This is the IEC 61970 CIM version number assigned to this UML model file. 
    """
    # <<< iec61970_cimversion.attributes
    # @generated
    version = db.StringProperty()

    date = db.DateTimeProperty()

    # >>> iec61970_cimversion.attributes

    # <<< iec61970_cimversion.references
    # @generated
    # >>> iec61970_cimversion.references

    # <<< iec61970_cimversion.operations
    # @generated
    # >>> iec61970_cimversion.operations

# EOF -------------------------------------------------------------------------
