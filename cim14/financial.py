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

from cim14.iec61968.informative.inf_erpsupport import ErpOrganisation
from cim14.iec61970.core import IdentifiedObject
from cim14.iec61968.common import Agreement
from cim14 import Element


# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

ns_prefix = "cim.Financial"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Financial"

class GenerationProvider(ErpOrganisation):
    """ The energy seller in the energy marketplace.
    """

    # The 'generating_units' property has been implicitly created by
    # the operated_by_generation_provider' property of GeneratingUnit.
    pass
    # The 'service_point' property has been implicitly created by
    # the generation_provider' property of ServicePoint.
    pass
    # The 'energy_products' property has been implicitly created by
    # the generation_provider' property of EnergyProduct.
    pass

class TransmissionProduct(IdentifiedObject):
#    location_for = db.ListProperty(db.Key)

#    @property
#    def located_on(self):
#        return TransmissionPath.gql("WHERE location_for = :1", self.key())
#    offers = db.ListProperty(db.Key)

#    @property
#    def offered_as(self):
#        return TransmissionService.gql("WHERE offers = :1", self.key())
#    transmission_provider = db.ReferenceProperty()

class CustomerConsumer(ErpOrganisation):
    """ The energy buyer in the energy marketplace.
    """

    # The 'service_point' property has been implicitly created by
    # the customer_consumer' property of ServicePoint.
    pass
    # The 'tie_lines' property has been implicitly created by
    # the customer_consumer' property of TieLine.
    pass

class ControlAreaOperator(ErpOrganisation):
    """ Operates the Control Area. Approves and implements energy transactions. Verifies both Inter-Control Area and Intra-Control Area transactions for the power system before granting approval (and implementing) the transactions.
    """

#    controlled_by = db.ReferenceProperty()
    # The 'ancillary_service' property has been implicitly created by
    # the control_area_operator' property of AncillaryService.
    pass
#    tie_lines = db.ListProperty(db.Key)

#    @property
#    def control_area_operators(self):
#        return TieLine.gql("WHERE tie_lines = :1", self.key())

class IntSchedAgreement(Agreement):
    """ A type of agreement that provides the default method by which interchange schedules are to be integrated to obtain hourly energy schedules for accounting.
    """

#    organisations = db.ListProperty(db.Key)

#    @property
#    def int_sched_agreement(self):
#        return ErpOrganisation.gql("WHERE organisations = :1", self.key())

class Marketer(ErpOrganisation):
    """ Matches buyers and sellers, and secures transmission (and other ancillary services) needed to complete the energy transaction.
    """

    # The 'holds_title_to_energy_products' property has been implicitly created by
    # the title_held_by_marketer' property of EnergyProduct.
    pass
#    resold_by = db.ReferenceProperty()
    # The 'held_by' property has been implicitly created by
    # the holds' property of ServiceReservation.
    pass
#    resells_energy_product = db.ListProperty(db.Key)

#    @property
#    def resold_by_marketers(self):
#        return EnergyProduct.gql("WHERE resells_energy_product = :1", self.key())

class FinancialVersion(Element):
    date = db.DateProperty()
    version = db.StringProperty()

class OpenAccessProduct(Agreement):
    """ Contracts for services offered commercially.
    """

    # The 'ancillary_services' property has been implicitly created by
    # the open_access_product' property of AncillaryService.
    pass
    # The 'provided_by_transmission_service' property has been implicitly created by
    # the trans_contract_for' property of TransmissionService.
    pass

class TransmissionProvider(ErpOrganisation):
    """ Provider of the transmission capacity (interconnecting wires between Generation and Consumption) required to fulfill and Energy Transaction's energy exchange. Posts information for transmission paths and AvailableTransmissionCapacities on a reservation node. Buys and sells its products and services on the same reservation node.
    """

    # The 'service_point' property has been implicitly created by
    # the transmission_provider' property of ServicePoint.
    pass
    # The 'transmission_products' property has been implicitly created by
    # the transmission_provider' property of TransmissionProduct.
    pass
#    flowgate = db.ListProperty(db.Key)

#    @property
#    def transmission_provider(self):
#        return Flowgate.gql("WHERE flowgate = :1", self.key())
    # The 'for_' property has been implicitly created by
    # the has_loss_' property of LossProfile.
    pass
    # The 'offered_by' property has been implicitly created by
    # the offers' property of TransmissionService.
    pass
    # The 'sold_by' property has been implicitly created by
    # the sells' property of ServiceReservation.
    pass
#    ancillary_services = db.ListProperty(db.Key)

#    @property
#    def transmission_providers(self):
#        return AncillaryService.gql("WHERE ancillary_services = :1", self.key())


