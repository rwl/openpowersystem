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

class ExcST5B(ExcitationSystem):
    """ IEEE (2005) ST5B Model  The Type ST5B excitation system is a variation of the Type ST1A model, with alternative overexcitation and underexcitation inputs and additional limits. The corresponding stabilizer models that can be used with these models are the Type PSS2B, PSS3B, or PSS4B. 
    """
    # <<< exc_st5_b.attributes
    # @generated
    # OEL lead time constant 
    toc2 = Seconds

    # OEL lead time constant 
    toc1 = Seconds

    # Regulator lead time constant 
    tc1 = Seconds

    # Minimum regulator output (&lt; 0.) 
    vrmin = db.FloatProperty()

    # Regulator lead time constant. 
    tc2 = Seconds

    # Rectifier regulation factor (&gt;= 0.) 
    kc = db.FloatProperty()

    # Regulator lag time constant (&gt;= 0.) 
    tb2 = Seconds

    # OEL lag time constant (&gt;= 0.) 
    tob1 = Seconds

    # Maximum regulator output (&gt; 0.) 
    vrmax = db.FloatProperty()

    # OEL lag time constant (&gt;= 0.) 
    tob2 = Seconds

    # Regulator lag time constant (&gt;= 0.) 
    tb1 = Seconds

    # UEL lag time constant (&gt;= 0.) 
    tub1 = Seconds

    # UEL lag time constant (&gt;= 0.) 
    tub2 = Seconds

    # UEL lead time constant. 
    tuc1 = Seconds

    # UEL lead time constant 
    tuc2 = Seconds

    # Regulator gain (&gt; 0.) 
    kr = db.FloatProperty()

    # Filter time constant (&gt;= 0.) 
    tr = Seconds

    # Firing circuit time constant (&gt;= 0.) 
    t1 = Seconds

    # >>> exc_st5_b.attributes

    # <<< exc_st5_b.references
    # @generated
    # >>> exc_st5_b.references

    # <<< exc_st5_b.operations
    # @generated
    # >>> exc_st5_b.operations

# EOF -------------------------------------------------------------------------
