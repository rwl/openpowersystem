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

""" Relationship between the generating unit's gross active power output on the X-axis (measured at the terminals of the machine(s)) and the generating unit's net active power output on the Y-axis (based on utility-defined measurements at the power station). Station service loads, when modeled, should be treated as non-conforming bus loads. There may be more than one curve, depending on the auxiliary equipment that is in service. 
"""

# <<< imports
# @generated
from cpsm.core.curve import Curve

from cpsm.generation.production.generating_unit import GeneratingUnit


from google.appengine.ext import db
# >>> imports

class GrossToNetActivePowerCurve(Curve):
    """ Relationship between the generating unit's gross active power output on the X-axis (measured at the terminals of the machine(s)) and the generating unit's net active power output on the Y-axis (based on utility-defined measurements at the power station). Station service loads, when modeled, should be treated as non-conforming bus loads. There may be more than one curve, depending on the auxiliary equipment that is in service. 
    """
    # <<< gross_to_net_active_power_curve.attributes
    # @generated
    # >>> gross_to_net_active_power_curve.attributes

    # <<< gross_to_net_active_power_curve.references
    # @generated
    # A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit 
    generating_unit = db.ReferenceProperty(GeneratingUnit,
        collection_name="gross_to_net_active_power_curves")

    # >>> gross_to_net_active_power_curve.references

    # <<< gross_to_net_active_power_curve.operations
    # @generated
    # >>> gross_to_net_active_power_curve.operations

# EOF -------------------------------------------------------------------------
