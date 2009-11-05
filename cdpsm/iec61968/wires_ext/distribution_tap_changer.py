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

""" Additional ratio tap changer parameters common to distribution line regulators. 'tculControlMode' would always be 'volt'. If 'monitoredPhase' is not specified, then if the controlled DistributionTransformerWinding is single-phase, the PT primary is assumed to be connected across that winding, which is the normal case. If the controlled winding is three-phase, then the 'monitoredPhase' is assumed to be 'AN', unless otherwise specified. Whenever 'ctRatio' and 'ptRatio' are specified, it's customary to specify the R and X in 'volts' referred to the PT secondary circuit, otherwise R and X are in feeder primary ohms. If 'ptRatio' is not specified, then 'targetVoltage', 'limitVoltage', and 'bandVoltage' are on the feeder primary base, phase-neutral or phase-phase depending on the 'monitoredPhase'. Otherwise, these attributes are all on the PT secondary base. 
"""

# <<< imports
# @generated
from cdpsm.iec61970.wires.ratio_tap_changer import RatioTapChanger


from cdpsm.iec61970.domain import Resistance
from cdpsm.iec61970.core import PhaseCode
from cdpsm.iec61970.domain import Voltage
from cdpsm.iec61970.domain import Reactance

from google.appengine.ext import db
# >>> imports

class DistributionTapChanger(RatioTapChanger):
    """ Additional ratio tap changer parameters common to distribution line regulators. 'tculControlMode' would always be 'volt'. If 'monitoredPhase' is not specified, then if the controlled DistributionTransformerWinding is single-phase, the PT primary is assumed to be connected across that winding, which is the normal case. If the controlled winding is three-phase, then the 'monitoredPhase' is assumed to be 'AN', unless otherwise specified. Whenever 'ctRatio' and 'ptRatio' are specified, it's customary to specify the R and X in 'volts' referred to the PT secondary circuit, otherwise R and X are in feeder primary ohms. If 'ptRatio' is not specified, then 'targetVoltage', 'limitVoltage', and 'bandVoltage' are on the feeder primary base, phase-neutral or phase-phase depending on the 'monitoredPhase'. Otherwise, these attributes are all on the PT secondary base. 
    """
    # <<< distribution_tap_changer.attributes
    # @generated
    # Line drop compensator resistance setting for normal (forward) power flow. 
    line_drop_r = Resistance

    # Phase voltage controlling this regulator, measured at regulator location. 
    monitored_phase = PhaseCode

    # If true, the line drop compensation is to be applied. 
    line_drop_compensation = db.BooleanProperty()

    # Built-in voltage transducer ratio. 
    pt_ratio = db.FloatProperty()

    # Built-in current transducer ratio. 
    ct_ratio = db.FloatProperty()

    # Line drop compensator resistance setting for reverse power flow. 
    reverse_line_drop_r = Resistance

    # Maximum allowed regulated voltage on the PT secondary base, regardless of line drop compensation. Sometimes referred to as first-house protection. 
    limit_voltage = Voltage

    # Line drop compensator reactance setting for reverse power flow. 
    reverse_line_drop_x = Reactance

    # Voltage range (max - min) on the PT secondary base, centered on 'targetVoltage'. 
    band_voltage = Voltage

    # Target voltage on the PT secondary base. 
    target_voltage = Voltage

    # Line drop compensator reactance setting for normal (forward) power flow. 
    line_drop_x = Reactance

    # >>> distribution_tap_changer.attributes

    # <<< distribution_tap_changer.references
    # @generated
    # >>> distribution_tap_changer.references

    # <<< distribution_tap_changer.operations
    # @generated
    # >>> distribution_tap_changer.operations

# EOF -------------------------------------------------------------------------
