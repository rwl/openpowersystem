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

from cim14 import Element
from cim14.iec61970.core import PowerSystemResource
from cim14.iec61970.control_area import ControlArea
from cim14.iec61970.core import IdentifiedObject
from cim14.iec61968.common import Agreement
from cim14.iec61970.core import RegularIntervalSchedule
from cim14.iec61970.core import Curve
from cim14.iec61968.common import Document

from cim14.iec61970.domain import Frequency
from cim14.iec61970.domain import RealEnergy
from cim14.iec61970.domain import ActivePower
from cim14.iec61970.domain import Money

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

AreaControlMode = db.StringProperty(choices=("cf", "tlb", "off", "ctl"))

ns_prefix = "cim.EnergyScheduling"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#EnergyScheduling"

class TieLine(Element):
#    customer_consumer = db.ReferenceProperty()
#    control_area_operators = db.ListProperty(db.Key)

#    @property
#    def tie_lines(self):
#        return ControlAreaOperator.gql("WHERE control_area_operators = :1", self.key())
#    side_a_sub_control_area = db.ReferenceProperty()
#    side_a_host_control_area = db.ReferenceProperty()
#    side_b_host_control_area = db.ReferenceProperty()
#    side_b_sub_control_area = db.ReferenceProperty()
#    dynamic_energy_transaction = db.ReferenceProperty()

class TransmissionCorridor(PowerSystemResource):
    """ A corridor containing one or more rights of way
    """

    # The 'transmission_right_of_ways' property has been implicitly created by
    # the transmission_corridor' property of TransmissionRightOfWay.
    pass
    # The 'contained_in' property has been implicitly created by
    # the for' property of TransmissionPath.
    pass

class SubControlArea(ControlArea):
    """ SubControlArea replacement classed moved into EnergySchedulingPackage.  An area defined for the purpose of tracking interchange with surrounding areas via tie points; may or may not serve as a control area.
    """

    # The 'flowgate' property has been implicitly created by
    # the sub_control_area' property of Flowgate.
    pass
    # The 'part_of' property has been implicitly created by
    # the member_of' property of ServicePoint.
    pass
    # The 'export_energy_transactions' property has been implicitly created by
    # the export_sub_control_area' property of EnergyTransaction.
    pass
    # The 'side_a_tie_lines' property has been implicitly created by
    # the side_a_sub_control_area' property of TieLine.
    pass
    # The 'generating_units' property has been implicitly created by
    # the sub_control_area' property of GeneratingUnit.
    pass
#    host_control_area = db.ReferenceProperty()
    # The 'import_energy_transactions' property has been implicitly created by
    # the import_sub_control_area' property of EnergyTransaction.
    pass
    # The 'side_b_tie_lines' property has been implicitly created by
    # the side_b_sub_control_area' property of TieLine.
    pass

class EnergySchedulingVersion(Element):
    date = db.DateProperty()
    # v 4 moved SubControlArea
    version = db.StringProperty()

class TransmissionRightOfWay(PowerSystemResource):
    """ A collection of transmission lines that are close proximity to each other.
    """

#    transmission_corridor = db.ReferenceProperty()
    # The 'lines' property has been implicitly created by
    # the transmission_right_of_way' property of Line.
    pass

class HostControlArea(IdentifiedObject):
    """ A HostControlArea has a set of tie points and a set of generator controls (i.e., AGC). It also has a total load, including transmission and distribution losses.
    """

    # The area's present control mode: (CF = constant frequency) or (CTL = constant tie-line) or (TLB = tie-line bias) or (OFF = off control)
    area_control_mode = AreaControlMode
    # The present power system frequency set point for automatic generation control
    freq_set_point = Frequency
    # The 'receive_dynamic_schedules' property has been implicitly created by
    # the receive_host_control_area' property of DynamicSchedule.
    pass
    # The 'side_a_tie_lines' property has been implicitly created by
    # the side_a_host_control_area' property of TieLine.
    pass
    # The 'side_b_tie_lines' property has been implicitly created by
    # the side_b_host_control_area' property of TieLine.
    pass
    # The 'send_dynamic_schedules' property has been implicitly created by
    # the send_host_control_area' property of DynamicSchedule.
    pass
    # The 'sub_control_areas' property has been implicitly created by
    # the host_control_area' property of SubControlArea.
    pass
    # The 'inadvertent_accounts' property has been implicitly created by
    # the host_control_area' property of InadvertentAccount.
    pass
#    controls = db.ReferenceProperty()
#    area_reserve_spec = db.ReferenceProperty()

class EnergyProduct(Agreement):
    """ An EnergyProduct is offered commercially as a ContractOrTariff.
    """

#    generation_provider = db.ReferenceProperty()
    # The 'energy_transactions' property has been implicitly created by
    # the energy_product' property of EnergyTransaction.
    pass
#    resold_by_marketers = db.ListProperty(db.Key)

#    @property
#    def resells_energy_product(self):
#        return Marketer.gql("WHERE resold_by_marketers = :1", self.key())
#    service_point = db.ListProperty(db.Key)

#    @property
#    def energy_products(self):
#        return ServicePoint.gql("WHERE service_point = :1", self.key())
#    title_held_by_marketer = db.ReferenceProperty()

class ProfileData(Element):
    """ Data for profile.
    """

    # Stop date/time for this profile.
    stop_date_time = db.DateProperty()
    # Energy level for the profile
    energy_level = RealEnergy
    # Active power capacity level for the profile.
    capacity_level = ActivePower
    # Sequence to provide item numbering for the profile. { greater than or equal to 1 }
    sequence_number = db.IntegerProperty()
    # Start date/time for this profile.
    start_date_time = db.DateProperty()
#    profile = db.ListProperty(db.Key)

#    @property
#    def profile_datas(self):
#        return Profile.gql("WHERE profile = :1", self.key())

class DynamicSchedule(RegularIntervalSchedule):
    """ A continuously variable component of a control area's active power net interchange schedule. Dynamic schedules are sent and received by control areas.
    """

    # The 'active' or 'inactive' status of the dynamic schedule
    dyn_sched_status = db.StringProperty()
    # Dynamic schedule sign reversal required (yes/no)
    dyn_sched_sign_rev = db.BooleanProperty()
#    receive_host_control_area = db.ReferenceProperty()
#    measurement = db.ReferenceProperty()
#    send_host_control_area = db.ReferenceProperty()

class AvailableTransmissionCapacity(Curve):
    """ Amount of possible flow by direction.
    """

#    schedule_for = db.ListProperty(db.Key)

#    @property
#    def scheduled_by(self):
#        return TransmissionService.gql("WHERE schedule_for = :1", self.key())

class AreaReserveSpec(Element):
    """ The control area's reserve specification
    """

    # Lower active power regulating margin requirement, the amount of generation that can be dropped by control in 10 minutes
    lower_reg_margin_reqt = ActivePower
    # Operating active power reserve requirement, where operating reserve is the generating capability that is fully available within 30 minutes. Operating reserve is composed of primary reserve (t less than 10 min) and secondary reserve (10 less than t less than 30 min).
    op_reserve_reqt = ActivePower
    # Primary active power reserve requirement, where primary reserve is generating capability that is fully available within 10 minutes. Primary reserve is composed of spinning reserve and quick-start reserve.
    primary_reserve_reqt = ActivePower
    # Spinning active power reserve requirement, spinning reserve is generating capability that is presently synchronized to the network and is fully available within 10 minutes
    spinning_reserve_reqt = ActivePower
    # The Identification or name of the control area's reserve specification. A particular specification could correspond to pre-defined power system conditions, e.g., emergency situations.
    area_reserve_spec_name = db.StringProperty()
    # Raise active power regulating margin requirement, the amount of generation that can be picked up by control in 10 minutes
    raise_reg_margin_reqt = ActivePower
    # The 'host_control_areas' property has been implicitly created by
    # the area_reserve_spec' property of HostControlArea.
    pass
#    reserve_energy_transaction = db.ReferenceProperty()

class InadvertentAccount(Curve):
    """ An account for tracking inadvertent interchange versus time for each control area. A control area may have more than one inadvertent account in order to track inadvertent over one or more specific tie points in addition to the usual overall net inadvertent. Separate accounts would also be used to track designated time periods, such as on-peak and off-peak.
    """

#    host_control_area = db.ReferenceProperty()

class EnergyTransaction(Document):
    """ Specifies the schedule for energy transfers between interchange areas that are necessary to satisfy the associated interchange transaction.
    """

    # Delivery point active power
    delivery_point_p = ActivePower
    # Receipt point active power
    receipt_point_p = ActivePower
    # Maximum congestion charges in monetary units
    congest_charge_max = Money
    # Firm interchange flag indicates whether or not this energy transaction can be changed without potential financial consequences.
    firm_interchange_flag = db.BooleanProperty()
    reason = db.StringProperty()
    # Transaction minimum active power if dispatchable
    energy_min = ActivePower
#    import_sub_control_area = db.ReferenceProperty()
    # The 'loss_profiles' property has been implicitly created by
    # the energy_transaction' property of LossProfile.
    pass
    # The 'energy_profiles' property has been implicitly created by
    # the energy_transaction' property of EnergyProfile.
    pass
#    energy_product = db.ReferenceProperty()
    # The 'energy_trans_id' property has been implicitly created by
    # the energy_trans_id' property of TransactionBid.
    pass
    # The 'curtailment_profiles' property has been implicitly created by
    # the energy_transaction' property of CurtailmentProfile.
    pass
#    export_sub_control_area = db.ReferenceProperty()
#    energy_price_curves = db.ListProperty(db.Key)

#    @property
#    def energy_transactions(self):
#        return EnergyPriceCurve.gql("WHERE energy_price_curves = :1", self.key())

class Profile(IdentifiedObject):
    """ A profile is a simpler curve type.
    """

#    profile_datas = db.ListProperty(db.Key)

#    @property
#    def profile(self):
#        return ProfileData.gql("WHERE profile_datas = :1", self.key())

class Reserve(EnergyTransaction):
    # The 'area_reserve_spec' property has been implicitly created by
    # the reserve_energy_transaction' property of AreaReserveSpec.
    pass

class Dynamic(EnergyTransaction):
    """ A dynamic energy transaction has more complex relationships than a simple block type. It behaves like a pseudo tie line.
    """

    # The 'tie_lines' property has been implicitly created by
    # the dynamic_energy_transaction' property of TieLine.
    pass

class EnergyProfile(Profile):
    """ Specifies the start time, stop time, level for an EnergyTransaction.
    """

#    transaction_bid = db.ReferenceProperty()
#    energy_transaction = db.ReferenceProperty()

class LossProfile(Profile):
    """ LossProfile is associated with an EnerrgyTransaction and must be completely contained within the time frame of the EnergyProfile associated with this EnergyTransaction.
    """

#    energy_transaction = db.ReferenceProperty()
#    has_loss_ = db.ReferenceProperty()

class Block(EnergyTransaction):
    """ A block is a simple transaction type, with no additional relationships.
    """

    pass

class CurtailmentProfile(Profile):
    """ Curtailing entity must be providing at least one service to the EnergyTransaction. The CurtailmentProfile must be completely contained within the EnergyProfile timeframe for this EnergyTransaction.
    """

#    energy_transaction = db.ReferenceProperty()


