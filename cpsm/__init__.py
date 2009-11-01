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

""" An extension to the Core and Wires packages that models information on the current and planned network configuration. These entities are optional within typical network applications.An extension to the Core and Wires packages that models information on the current and planned network configuration. These entities are optional within typical network applications.
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

#------------------------------------------------------------------------------
#  Constants:
#------------------------------------------------------------------------------

NS_PREFIX = "cim"
NS_URI = "http://iec.ch/TC57/2008/CIM-schema-cim13#"

#------------------------------------------------------------------------------
#  "Element" class:
#------------------------------------------------------------------------------

class Element(db.Model):
    
    uri = db.StringProperty()

    # 
    model = db.ReferenceProperty(collection_name="elements")

    # <<< element
    # @generated
    # >>> element


#------------------------------------------------------------------------------
#  "Model" class:
#------------------------------------------------------------------------------

class Model(db.Model):
    
    uri = db.StringProperty()

    # Virtual property. 
    pass #elements

    # <<< model
    # @generated
    # >>> model


#------------------------------------------------------------------------------
#  "IEC61970CIMVersion" class:
#------------------------------------------------------------------------------

class IEC61970CIMVersion(Element):
    """ This is the IEC 61970 CIM version number assigned to this UML model file.This is the IEC 61970 CIM version number assigned to this UML model file.
    """

    
    version = db.StringProperty()

    date = db.DateProperty()

    # <<< iec61970_cimversion
    # @generated
    # >>> iec61970_cimversion




# EOF -------------------------------------------------------------------------
