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


# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

WorkKind = db.StringProperty(choices=("disconnect", "service", "other", "maintenance", "meter", "inspection", "reconnect", "construction"))

ns_prefix = "cim.IEC61968.Work"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#IEC61968.Work"

class Work(Document):
    """ Document used to request, initiate, track and record work. This is synonymous with Work Breakdown Structure (WBS), which is traversed through the (currently informative) recursive association of Work. Note that the work name is equal to the WBS name, which is given in the inherited 'name' attribute.
    """

    # Kind of work.
    kind = WorkKind
    # Priority of work.
    priority = db.StringProperty()
    # Date and time work was requested.
    request_date_time = db.DateProperty()
#    work_billing_info = db.ReferenceProperty()
#    project = db.ReferenceProperty()
    # The 'designs' property has been implicitly created by
    # the work' property of Design.
    pass
#    customers = db.ListProperty(db.Key)

#    @property
#    def works(self):
#        return Customer.gql("WHERE customers = :1", self.key())
    # The 'work_flow_steps' property has been implicitly created by
    # the work' property of WorkFlowStep.
    pass
#    business_case = db.ReferenceProperty()
#    work_cost_details = db.ListProperty(db.Key)

#    @property
#    def works(self):
#        return WorkCostDetail.gql("WHERE work_cost_details = :1", self.key())
#    request = db.ReferenceProperty()
    # The 'work_tasks' property has been implicitly created by
    # the work' property of WorkTask.
    pass
#    erp_project_accounting = db.ReferenceProperty()


