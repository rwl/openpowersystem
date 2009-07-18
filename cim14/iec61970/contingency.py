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


# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

ContingencyEquipmentStatusKind = db.StringProperty(choices=("out_of_service", "in_service"))

ns_prefix = "cim.IEC61970.Contingency"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#IEC61970.Contingency"

class ContingencyElement(IdentifiedObject):
    """ An element of a system event to be studied by contingency analysis, representing a change in status of a single piece of equipment.
    """

#    contingency = db.ReferenceProperty()

class Contingency(IdentifiedObject):
    """ An event threatening system reliability, consisting of one or more contingency elements.
    """

    # Set true if must study this contingency.
    must_study = db.BooleanProperty()
    # The 'contingency_element' property has been implicitly created by
    # the contingency' property of ContingencyElement.
    pass
    # The 'contingency_constraint_limit' property has been implicitly created by
    # the contingency' property of ContingencyConstraintLimit.
    pass

class ContingencyEquipment(ContingencyElement):
    """ A equipment to which the in service status is to change such as a power transformer or AC line segment.
    """

    # The status for the associated equipment when in the contingency state.   This status is independent of the case to which the contingency is originally applied, but defines the equipment status when the contingency is applied.
    contingent_status = ContingencyEquipmentStatusKind
#    equipment = db.ReferenceProperty()


