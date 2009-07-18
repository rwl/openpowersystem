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

from cim14.iec61968.informative.inf_common import Role
from cim14.iec61968.common import Agreement
from cim14.iec61970.core import IdentifiedObject
from cim14.iec61968.common import Location


# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

DemographicKind = db.StringProperty(choices=("urban", "other", "rural"))

ZoneKind = db.StringProperty(choices=("special_restriction_land", "weather_zone", "other", "electrical_network"))

LandPropertyKind = db.StringProperty(choices=("customer_premise", "building", "external", "store", "grid_supply_point", "substation", "depot"))

ns_prefix = "cim.IEC61968.Informative.InfLocations"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#IEC61968.Informative.InfLocations"

class PsrLocRole(Role):
    """ Roles played between Power System Resources and Locations.
    """

#    power_system_resource = db.ReferenceProperty()
#    location = db.ReferenceProperty()

class OrgPropertyRole(Role):
    """ Roles played between Organisations and a given piece of property. For example, the Organisation may be the owner, renter, occupier, taxiing authority, etc.
    """

#    land_property = db.ListProperty(db.Key)

#    @property
#    def erp_organisation_roles(self):
#        return LandProperty.gql("WHERE land_property = :1", self.key())
#    erp_organisation = db.ReferenceProperty()

class LocationGrant(Agreement):
    """ A grant provides a right, as defined by type, for a parcel of land. Note that the association to Location, Asset, Organisation, etc. for the Grant is inherited from Agreement, a type of Document.
    """

    # Property related information that describes the Grant's land parcel. For example, it may be a deed book number, deed book page number, and parcel number.
    property_data = db.StringProperty()
#    land_property = db.ReferenceProperty()

class RightOfWay(Agreement):
    """ A right-of-way (ROW) is for land where it is lawful to use for a public road, an electric power line, etc. Note that the association to Location, Asset, Organisation, etc. for the Grant is inherited from Agreement, a type of Document.
    """

    # Property related information that describes the ROW's land parcel. For example, it may be a deed book number, deed book page number, and parcel number.
    property_data = db.StringProperty()
#    land_properties = db.ListProperty(db.Key)

#    @property
#    def right_of_ways(self):
#        return LandProperty.gql("WHERE land_properties = :1", self.key())

class OrgLocRole(Role):
    """ Roles played between Organisations and Locations, for example a service territory or school district. Note that roles dealing with use of a specific piece of property should be defined based on the relationship between OccupationsOfProperty and Location.
    """

#    location = db.ReferenceProperty()
#    erp_organisation = db.ReferenceProperty()

class RedLine(IdentifiedObject):
    """ This class is used for handling the accompanying annotations, time stamp, author, etc. of designs, drawings and maps. A red line can be associated with any Location object.
    """

    status = db.ReferenceProperty()
#    locations = db.ListProperty(db.Key)

#    @property
#    def red_lines(self):
#        return Location.gql("WHERE locations = :1", self.key())

class Hazard(IdentifiedObject):
    """ A hazard is any object or condition that is a danger for causing loss or perils to an asset and/or people. Examples of hazards are trees growing under overhead power lines, a park being located by a substation (i.e., children climb fence to recover a ball), a lake near an overhead distribution line (fishing pole/line contacting power lines), etc.
    """

    # Category by utility's corporate standards and practices.
    category = db.StringProperty()
    status = db.ReferenceProperty()
#    assets = db.ListProperty(db.Key)

#    @property
#    def hazards(self):
#        return Asset.gql("WHERE assets = :1", self.key())
#    locations = db.ListProperty(db.Key)

#    @property
#    def hazards(self):
#        return Location.gql("WHERE locations = :1", self.key())

class PersonPropertyRole(Role):
    """ The role of a person relative to a given piece of property. Examples of roles include: owner, renter, contractor, etc.
    """

#    erp_person = db.ReferenceProperty()
#    land_property = db.ReferenceProperty()

class ErpPersonLocRole(Role):
    """ Roles played between People and Locations. Some Locations are somewhat static, like the person's home address. Other may be dynamic, for example when the person is part of a crew driving around in truck.
    """

#    erp_person = db.ReferenceProperty()
#    location = db.ReferenceProperty()

class Route(IdentifiedObject):
    """ Route that is followed, for example by service crews.
    """

    # Category by utility's work management standards and practices.
    category = db.StringProperty()
    status = db.ReferenceProperty()
    # The 'crews' property has been implicitly created by
    # the route' property of Crew.
    pass
#    locations = db.ListProperty(db.Key)

#    @property
#    def routes(self):
#        return Location.gql("WHERE locations = :1", self.key())

class Zone(Location):
    """ Area divided off from other areas. It may be part of the electrical network, a land area where special restrictions apply, weather areas, etc. For weather, it is an area where a set of relatively homogenous weather measurements apply.
    """

    # Kind of this zone.
    kind = ZoneKind

class AssetLocRole(Role):
    """ Roles played between Assets and Locations.
    """

#    location = db.ReferenceProperty()
#    asset = db.ReferenceProperty()

class LandProperty(IdentifiedObject):
    """ Information about a particular piece of (land) property such as its use. Ownership of the property may be determined through associations to Organisations and/or ErpPersons.
    """

    # Kind of (land) property, categorised according to its main functional use from the utility's perspective.
    kind = LandPropertyKind
    # Demographics around the site.
    demographic_kind = DemographicKind
    # Reference allocated by the governing organisation (such as municipality) to this piece of land that has a formal reference to Surveyor General's records. The governing organisation is specified in associated Organisation.
    external_record_reference = db.StringProperty()
    status = db.ReferenceProperty()
    # The 'location_grants' property has been implicitly created by
    # the land_property' property of LocationGrant.
    pass
#    asset_containers = db.ListProperty(db.Key)

#    @property
#    def land_properties(self):
#        return AssetContainer.gql("WHERE asset_containers = :1", self.key())
#    locations = db.ListProperty(db.Key)

#    @property
#    def land_properties(self):
#        return Location.gql("WHERE locations = :1", self.key())
#    erp_organisation_roles = db.ListProperty(db.Key)

#    @property
#    def land_property(self):
#        return OrgPropertyRole.gql("WHERE erp_organisation_roles = :1", self.key())
    # The 'erp_site_level_datas' property has been implicitly created by
    # the land_property' property of ErpSiteLevelData.
    pass
#    right_of_ways = db.ListProperty(db.Key)

#    @property
#    def land_properties(self):
#        return RightOfWay.gql("WHERE right_of_ways = :1", self.key())
    # The 'erp_person_roles' property has been implicitly created by
    # the land_property' property of PersonPropertyRole.
    pass

class DocLocRole(Role):
    """ Roles played between Documents and Locations. For example, as ErpAddress is a type of Location and WorkBilling is a type of Document, a role is the address for which to mail the invoice. As a TroubleTicket is a type of Document, one instance of Location may be the address for which the trouble is reported.
    """

#    location = db.ReferenceProperty()
#    document = db.ReferenceProperty()

class LocLocRole(Role):
    """ The relationship between one Location and another Location. One 'roleType' is 'Directions,' for which an additional attribute serves for providing a textual description for navigating from one location to another location.
    """

    # Detailed directional information.
    direction_info = db.StringProperty()
#    from_location = db.ReferenceProperty()
#    to_location = db.ReferenceProperty()


