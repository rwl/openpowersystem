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

from cim14.iec61968.common import Document

from cim14.iec61970.domain import Weight

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

CorporateStandardKind = db.StringProperty(choices=("standard", "other", "experimental", "under_evaluation"))

AssetModelUsageKind = db.StringProperty(choices=("other", "substation", "unknown", "customer_substation", "distribution_overhead", "distribution_underground", "streetlight", "transmission"))

ns_prefix = "cim.IEC61968.AssetModels"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#IEC61968.AssetModels"

class AssetModel(Document):
    """ Documentation for a particular product model made by a manufacturer. There are typically many instances of an asset associated with a single asset model.
    """

    # Manufacturer's model number.
    model_number = db.StringProperty()
    # Total manufactured weight of asset.
    weight_total = Weight
    # Version number for product model, which indicates vintage of the product.
    model_version = db.StringProperty()
    # Kind of coporate standard for this asset model.
    corporate_standard_kind = CorporateStandardKind
    # Intended usage for this asset model.
    usage_kind = AssetModelUsageKind
#    type_asset = db.ReferenceProperty()
    # The 'asset_model_catalogue_items' property has been implicitly created by
    # the asset_model' property of AssetModelCatalogueItem.
    pass
    # The 'erp_inventory_counts' property has been implicitly created by
    # the asset_model' property of ErpInventoryCount.
    pass

class EndDeviceModel(AssetModel):
    """ Documentation for particular end device product model made by a manufacturer.
    """

    # The 'end_device_assets' property has been implicitly created by
    # the end_device_model' property of EndDeviceAsset.
    pass
#    end_device_type_asset = db.ReferenceProperty()


