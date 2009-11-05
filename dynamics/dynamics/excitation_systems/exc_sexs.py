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

class ExcSEXS(ExcitationSystem):
    """ Simplified Excitation System Model 
    """
    # <<< exc_sexs.attributes
    # @generated
    # Gain (&gt; 0.) 
    k = db.FloatProperty()

    # Ta/Tb - gain reduction ratio of lag-lead element 
    tatb = db.FloatProperty()

    # Field voltage clipping minimum limit 
    efdmin = db.FloatProperty()

    # Time constant of gain block (&gt; 0.) 
    te = Seconds

    # PI controller phase lead time constant 
    tc = Seconds

    # PI controller gain (&gt; 0. if Tc &gt; 0.) 
    kc = db.FloatProperty()

    # Denominator time constant of lag-lead block 
    tb = Seconds

    # Minimum field voltage output 
    emin = db.FloatProperty()

    # Maximum field voltage output 
    emax = db.FloatProperty()

    # Field voltage clipping maximum limit 
    efdmax = db.FloatProperty()

    # >>> exc_sexs.attributes

    # <<< exc_sexs.references
    # @generated
    # >>> exc_sexs.references

    # <<< exc_sexs.operations
    # @generated
    # >>> exc_sexs.operations

# EOF -------------------------------------------------------------------------
