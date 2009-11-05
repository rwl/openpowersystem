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
from dynamics.dynamics.excitation_systems.excitation_system import ExcitationSystem


from dynamics.domain import Seconds

from google.appengine.ext import db
# >>> imports

class ExcSCRX(ExcitationSystem):
    """ Simple excitation system model representing generic characteristics of many excitation systems; intended for use where negative field current may be a problem 
    """
    # <<< exc_scrx.attributes
    # @generated
    # Time constant of gain block (&gt; 0.) 
    te = Seconds

    # Denominator time constant of lag-lead block 
    tb = Seconds

    # Maximum field voltage output 
    emax = db.FloatProperty()

    # Power source switch:     1 ? fixed voltage     0 ? generator terminal voltage 
    cswitch = db.BooleanProperty()

    # Rc/Rfd - ratio of field discharge resistance to field winding resistance 
    rcrfd = db.FloatProperty()

    # Ta/Tb - gain reduction ratio of lag-lead element 
    tatb = db.FloatProperty()

    # Gain (&gt; 0.) 
    k = db.FloatProperty()

    # Minimum field voltage output 
    emin = db.FloatProperty()

    # >>> exc_scrx.attributes

    # <<< exc_scrx.references
    # @generated
    # >>> exc_scrx.references

    # <<< exc_scrx.operations
    # @generated
    # >>> exc_scrx.operations

# EOF -------------------------------------------------------------------------
