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

""" Generic user of energy - a  point of consumption on the power system model 
"""

# <<< imports
# @generated
from ucte.core.conducting_equipment import ConductingEquipment

from ucte.load_model.load_response_characteristic import LoadResponseCharacteristic


from google.appengine.ext import db
# >>> imports

class EnergyConsumer(ConductingEquipment):
    """ Generic user of energy - a  point of consumption on the power system model 
    """
    # <<< energy_consumer.attributes
    # @generated
    # >>> energy_consumer.attributes

    # <<< energy_consumer.references
    # @generated
    # The load response characteristic of this load. 
    load_response = db.ReferenceProperty(LoadResponseCharacteristic,
        collection_name="energy_consumer")

    # >>> energy_consumer.references

    # <<< energy_consumer.operations
    # @generated
    # >>> energy_consumer.operations

# EOF -------------------------------------------------------------------------
