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

""" NonConformLoad represent loads that do not follow a daily load change pattern and changes are not correlated with the daily load change pattern. 
"""

# <<< imports
# @generated
from cpsm.wires.energy_consumer import EnergyConsumer

from cpsm.load_model.non_conform_load_group import NonConformLoadGroup


from google.appengine.ext import db
# >>> imports

class NonConformLoad(EnergyConsumer):
    """ NonConformLoad represent loads that do not follow a daily load change pattern and changes are not correlated with the daily load change pattern. 
    """
    # <<< non_conform_load.attributes
    # @generated
    # >>> non_conform_load.attributes

    # <<< non_conform_load.references
    # @generated
    # Group of this ConformLoad. 
    load_group = db.ReferenceProperty(NonConformLoadGroup,
        collection_name="energy_consumers")

    # >>> non_conform_load.references

    # <<< non_conform_load.operations
    # @generated
    # >>> non_conform_load.operations

# EOF -------------------------------------------------------------------------
