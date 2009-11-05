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
from dynamics.dynamics.loads.aggregate_load import AggregateLoad



from google.appengine.ext import db
# >>> imports

class LoadStatic(AggregateLoad):
    """ General Static Load Model. A static load model represents the sensitivity of the real and reactive power consumed by the load to the amplitude and frequency of the bus voltage. 
    """
    # <<< load_static.attributes
    # @generated
    ep2 = db.FloatProperty()

    ep1 = db.FloatProperty()

    kp2 = db.FloatProperty()

    ep3 = db.FloatProperty()

    kp1 = db.FloatProperty()

    kq4 = db.FloatProperty()

    kq3 = db.FloatProperty()

    kq2 = db.FloatProperty()

    kq1 = db.FloatProperty()

    eq1 = db.FloatProperty()

    eq2 = db.FloatProperty()

    kp4 = db.FloatProperty()

    kp3 = db.FloatProperty()

    eq3 = db.FloatProperty()

    kqf = db.FloatProperty()

    kpf = db.FloatProperty()

    # >>> load_static.attributes

    # <<< load_static.references
    # @generated
    # >>> load_static.references

    # <<< load_static.operations
    # @generated
    # >>> load_static.operations

# EOF -------------------------------------------------------------------------
