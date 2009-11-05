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

""" An overcurrent protective device with a circuit opening fusible part that is heated and severed by the passage of overcurrent through it. A fuse is considered a switching device because it breaks current. 
"""

# <<< imports
# @generated
from cdpsm.iec61970.wires.switch import Switch


from cdpsm.iec61970.domain import CurrentFlow

from google.appengine.ext import db
# >>> imports

class Fuse(Switch):
    """ An overcurrent protective device with a circuit opening fusible part that is heated and severed by the passage of overcurrent through it. A fuse is considered a switching device because it breaks current. 
    """
    # <<< fuse.attributes
    # @generated
    # Fault interrupting current rating. 
    rating_current = CurrentFlow

    # >>> fuse.attributes

    # <<< fuse.references
    # @generated
    # >>> fuse.references

    # <<< fuse.operations
    # @generated
    # >>> fuse.operations

# EOF -------------------------------------------------------------------------
