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
from cim14.iec61970.core import IdentifiedObject

from cim14.iec61970.domain import ActivePower

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

ns_prefix = "cim.Reservation"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Reservation"

class TransmissionPath(Element):
    """ An electrical connection, link, or line consisting of one or more parallel transmission elements between two areas of the interconnected electric systems, or portions thereof. TransmissionCorridor and TransmissionRightOfWay refer to legal aspects. The TransmissionPath refers to the segments between a TransmissionProvider's ServicePoints.
    """

    # Flag which indicates if the transmission path is also a designated interconnection 'parallel path'
    parallel_path_flag = db.BooleanProperty()
    # The available transmission capability of a transmission path for the reference direction
    avail_transfer_capability = ActivePower
    # The total transmission capability of a transmission path in the reference direction
    total_transfer_capability = ActivePower
#    offered_on = db.ListProperty(db.Key)

#    @property
#    def offering(self):
#        return TransmissionService.gql("WHERE offered_on = :1", self.key())
#    delivery_point_for = db.ReferenceProperty()
#    point_of_receipt_for = db.ReferenceProperty()
#    located_on = db.ListProperty(db.Key)

#    @property
#    def location_for(self):
#        return TransmissionProduct.gql("WHERE located_on = :1", self.key())
#    for = db.ReferenceProperty()

class TiePoint(IdentifiedObject):
    """ Site of an interface between interchange areas. The tie point can be a network branch (e.g., transmission line or transformer) or a switching device. For transmission lines, the interchange area boundary is usually at a designated point such as the middle of the line. Line end metering is then corrected for line losses.
    """

    # The MW rating of the tie point
    tie_point_mwrating = ActivePower
    # The 'by_measurements' property has been implicitly created by
    # the by_tie_point' property of Measurement.
    pass
    # The 'for_measurements' property has been implicitly created by
    # the for_tie_point' property of Measurement.
    pass
#    declared_service_point = db.ReferenceProperty()

class AncillaryService(IdentifiedObject):
    """ All of these services relate  to various aspects of insuring that the production of energy matches consumption of energy at any given time.  They are very critical to the security and reliability of the interconnected network. Some examples of AncillaryServices include Operating/Supplemental Reserve, Energy Imbalance Service, Operating/Spinning Reserve, Reactive Supply and Voltage Control, and Regulation and Frequency Response.
    """

#    open_access_product = db.ReferenceProperty()
#    control_area_operator = db.ReferenceProperty()
#    reserved_by_service_reservation = db.ReferenceProperty()
#    transmission_providers = db.ListProperty(db.Key)

#    @property
#    def ancillary_services(self):
#        return TransmissionProvider.gql("WHERE transmission_providers = :1", self.key())

class ServiceReservation(Element):
    """ A ServiceReservation is a reservation for either AncillaryServices or TransmissionServices. In the case of TransmissionServices, this is the right to some amount of AvailableTransmissionCapacity for a product on a path in a direction for some specific period of time
    """

    # The 'reserves_ancillary_services' property has been implicitly created by
    # the reserved_by_service_reservation' property of AncillaryService.
    pass
#    reserves_transmission_service = db.ListProperty(db.Key)

#    @property
#    def reserved_by_service_reservation(self):
#        return TransmissionService.gql("WHERE reserves_transmission_service = :1", self.key())
#    holds = db.ReferenceProperty()
#    resells = db.ReferenceProperty()
#    sells = db.ReferenceProperty()

class ServicePoint(IdentifiedObject):
    """ Each ServicePoint is contained within (or on the boundary of) an ElectronicIinterchangeArea. ServicePoints are defined termination points of a transmission path (down to distribution level or to a customer - generation or consumption or both).
    """

    # The 'has_apod_' property has been implicitly created by
    # the delivery_point_for' property of TransmissionPath.
    pass
#    customer_consumer = db.ReferenceProperty()
    # The 'has_apor_' property has been implicitly created by
    # the point_of_receipt_for' property of TransmissionPath.
    pass
#    transmission_provider = db.ReferenceProperty()
#    declare_tie_point = db.ReferenceProperty()
#    generation_provider = db.ReferenceProperty()
#    member_of = db.ReferenceProperty()
#    energy_products = db.ListProperty(db.Key)

#    @property
#    def service_point(self):
#        return EnergyProduct.gql("WHERE energy_products = :1", self.key())

class TransmissionService(IdentifiedObject):
    """ Transmission products along posted transmission path.
    """

#    reserved_by_service_reservation = db.ListProperty(db.Key)

#    @property
#    def reserves_transmission_service(self):
#        return ServiceReservation.gql("WHERE reserved_by_service_reservation = :1", self.key())
#    offering = db.ListProperty(db.Key)

#    @property
#    def offered_on(self):
#        return TransmissionPath.gql("WHERE offering = :1", self.key())
#    trans_contract_for = db.ReferenceProperty()
#    scheduled_by = db.ListProperty(db.Key)

#    @property
#    def schedule_for(self):
#        return AvailableTransmissionCapacity.gql("WHERE scheduled_by = :1", self.key())
#    offers = db.ReferenceProperty()
#    offered_as = db.ListProperty(db.Key)

#    @property
#    def offers(self):
#        return TransmissionProduct.gql("WHERE offered_as = :1", self.key())

class ReservationVersion(Element):
    date = db.DateProperty()
    version = db.StringProperty()


