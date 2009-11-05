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


# <<< imports
# @generated
from dynamics.element import Element



from google.appengine.ext import db
# >>> imports

class AggregateLoad(Element):
    """ Aggregate loads are used to represent all or part of the real and reactive load from a load in the static (power flow) data. This load is usually the aggregation of many individual load devices. The load models are approximate representation of the aggregate response of the load devices to system disturbances.   Models of loads for dynamic analysis may themselves be either static or dynamic. A static load model represents the sensitivity of the real and reactive power consumed by the load to the amplitude and frequency of the bus voltage. A dynamic load model can used to represent the aggregate response of the motor components of the load.   Large industrial motors or groups of similar motors may be represented by individual motor models (synchronous or asynchronous) which are usually represented as generators with negative Pgen in the static (power flow) data. 
    """
    # <<< aggregate_load.attributes
    # @generated
    # >>> aggregate_load.attributes

    # <<< aggregate_load.references
    # @generated
    # >>> aggregate_load.references

    # <<< aggregate_load.operations
    # @generated
    # >>> aggregate_load.operations

# EOF -------------------------------------------------------------------------
