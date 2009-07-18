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

from cim14.iec61970.core import IdentifiedObject
from cim14.iec61970.core import IrregularIntervalSchedule


# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

SwitchState = db.StringProperty(choices=("open", "close"))

ns_prefix = "cim.IEC61970.Outage"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#IEC61970.Outage"

class SwitchingOperation(IdentifiedObject):
    """ A SwitchingOperation is used to define individual switch operations for an OutageSchedule. This OutageSchedule may be associated with another item of Substation such as a Transformer, Line, or Generator; or with the Switch itself as a PowerSystemResource. A Switch may be referenced by many OutageSchedules.
    """

    # The switch position that shall result from this SwitchingOperation
    new_state = SwitchState
    # Time of operation in same units as OutageSchedule.xAxixUnits.
    operation_time = db.DateProperty()
#    outage_schedule = db.ReferenceProperty()
#    switches = db.ListProperty(db.Key)

#    @property
#    def switching_operations(self):
#        return Switch.gql("WHERE switches = :1", self.key())

class OutageSchedule(IrregularIntervalSchedule):
    """ The period of time that a piece of equipment is out of service, for example, for maintenance or testing; including the equipment's active power rating while under maintenance. The X-axis represents absolute time and the Y-axis represents the equipment's available rating while out of service.
    """

#    planned_outage = db.ReferenceProperty()
#    power_system_resource = db.ReferenceProperty()
    # The 'switching_operations' property has been implicitly created by
    # the outage_schedule' property of SwitchingOperation.
    pass

class ClearanceTag(IdentifiedObject):
    """ A clearance tag that is used to authorize and schedule work on conducting equipment in the field. Tagged equipment is not available for commercial service.
    """

    # The time at which the clearance tag is scheduled to be set.
    work_start_time = db.DateProperty()
    # Set true if equipment phasing must be checked
    phase_check_req_flag = db.BooleanProperty()
    # Set true if equipment must be deenergized
    deenergize_req_flag = db.BooleanProperty()
    # The time at which the clearance tag is scheduled to be removed
    work_end_time = db.DateProperty()
    # The time at which the clearance tag was issued
    tag_issue_time = db.DateProperty()
    # Description of the work to be performed
    work_description = db.StringProperty()
    # Set true if equipment must be grounded
    ground_req_flag = db.BooleanProperty()
    # The name of the person who is authorized to issue the tag
    authority_name = db.StringProperty()
#    conducting_equipment = db.ReferenceProperty()
#    safety_documents = db.ListProperty(db.Key)

#    @property
#    def clearance_tags(self):
#        return SafetyDocument.gql("WHERE safety_documents = :1", self.key())
#    clearance_tag_type = db.ReferenceProperty()

class ClearanceTagType(IdentifiedObject):
    """ Type of ClearanceTag. Could indicate the type of work to be performed and/or the type of supervisory control.
    """

    # The 'clearance_tags' property has been implicitly created by
    # the clearance_tag_type' property of ClearanceTag.
    pass


