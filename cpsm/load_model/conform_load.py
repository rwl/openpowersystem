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

""" ConformLoad represent loads that follow a daily load change pattern where the pattern can be used to scale the load with a system load. 
"""

# <<< imports
# @generated
from cpsm.wires.energy_consumer import EnergyConsumer

from cpsm.load_model.conform_load_group import ConformLoadGroup


from google.appengine.ext import db
# >>> imports

class ConformLoad(EnergyConsumer):
    """ ConformLoad represent loads that follow a daily load change pattern where the pattern can be used to scale the load with a system load. 
    """
    # <<< conform_load.attributes
    # @generated
    # >>> conform_load.attributes

    # <<< conform_load.references
    # @generated
    # Group of this ConformLoad. 
    load_group = db.ReferenceProperty(ConformLoadGroup,
        collection_name="energy_consumers")

    # >>> conform_load.references

    # <<< conform_load.operations
    # @generated
    # >>> conform_load.operations

# EOF -------------------------------------------------------------------------
