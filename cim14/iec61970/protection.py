# Copyright (C) 2009 Richard W. Lincoln
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation; version 2 dated June, 1991.
#
# This software is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANDABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA

from cim14.iec61970.core import Equipment
from cim14.iec61970.core import IdentifiedObject

from cim14.iec61970.domain import Frequency
from cim14.iec61970.domain import Voltage
from cim14.iec61970.domain import AngleRadians
from cim14.iec61970.domain import Seconds
from cim14.iec61970.domain import CurrentFlow

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

ns_prefix = "cim.IEC61970.Protection"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#IEC61970.Protection"

class ProtectionEquipment(Equipment):
    """ An electrical device designed to respond to input conditions in a prescribed manner and after specified conditions are met to cause contact operation or similar abrupt change in associated electric control circuits, or simply to display the detected condition. Protection equipment are associated with conducting equipment and usually operate circuit breakers.
    """

    # The minimum allowable value.
    low_limit = db.FloatProperty()
    # Direction same as positive active power flow value.
    power_direction_flag = db.BooleanProperty()
    # The maximum allowable value.
    high_limit = db.FloatProperty()
    # The time delay from detection of abnormal conditions to relay operation.
    relay_delay_time = Seconds
#    conducting_equipments = db.ListProperty(db.Key)

#    @property
#    def protection_equipments(self):
#        return ConductingEquipment.gql("WHERE conducting_equipments = :1", self.key())
#    unit = db.ReferenceProperty()
#    protected_switches = db.ListProperty(db.Key)

#    @property
#    def protection_equipments(self):
#        return ProtectedSwitch.gql("WHERE protected_switches = :1", self.key())

class FaultIndicator(Equipment):
    """ A FaultIndicator is typically only an indicator (which may or may not be remotely monitored), and not a piece of equipment that actually initiates a protection event. It is used for FLISR (Fault Location, Isolation and Restoration) purposes, assisting with the dispatch of crews to 'most likely' part of the network (i.e. assists with determining circuit section where the fault most likely happened).
    """

#    fault_indicator_type_asset = db.ReferenceProperty()
    # The 'fault_indicator_assets' property has been implicitly created by
    # the fault_indicator' property of FaultIndicatorAsset.
    pass

class SurgeProtector(Equipment):
    """ Shunt device, installed on the network, usually in the proximity of electrical equipment in order to protect the said equipment against transient voltage spikes caused by lightning or switching activity.
    """

#    surge_protector_asset = db.ReferenceProperty()
#    surge_protector_type_asset = db.ReferenceProperty()

class RecloseSequence(IdentifiedObject):
    """ A reclose sequence (open and close) is defined for each possible reclosure of a breaker.
    """

    # Indicates the ordinal position of the reclose step relative to other steps in the sequence.
    reclose_step = db.IntegerProperty()
    # Indicates the time lapse before the reclose step will execute a reclose.
    reclose_delay = Seconds
#    protected_switch = db.ReferenceProperty()

class SynchrocheckRelay(ProtectionEquipment):
    """ A device that operates when two AC circuits are within the desired limits of frequency, phase angle, and voltage, to permit or to cause the paralleling of these two circuits. Used to prevent the paralleling of non-synchronous topological islands.
    """

    # The maximum allowable frequency difference across the open device
    max_freq_diff = Frequency
    # The maximum allowable difference voltage across the open device
    max_volt_diff = Voltage
    # The maximum allowable voltage vector phase angle difference across the open device
    max_angle_diff = AngleRadians

class CurrentRelay(ProtectionEquipment):
    """ A device that checks current flow values in any direction or designated direction
    """

    # Inverse time delay #2 for current limit #2
    time_delay2 = Seconds
    # Current limit #2 for inverse time pickup
    current_limit2 = CurrentFlow
    # Inverse time delay #1 for current limit #1
    time_delay1 = Seconds
    # Inverse time delay #3 for current limit #3
    time_delay3 = Seconds
    # Current limit #1 for inverse time pickup
    current_limit1 = CurrentFlow
    # Set true if the current relay has inverse time characteristic.
    inverse_time_flag = db.BooleanProperty()
    # Current limit #3 for inverse time pickup
    current_limit3 = CurrentFlow


