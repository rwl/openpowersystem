#------------------------------------------------------------------------------
# Copyright (C) 2009 Richard Lincoln
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
#------------------------------------------------------------------------------

""" Defines request handlers for OpenPowerSystem.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

import os
import cgi
import logging

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.ext import db

from ucte.core.geographical_region import GeographicalRegion
from ucte.wires.synchronous_machine import SynchronousMachine
from ucte.wires.acline_segment import ACLineSegment
from ucte.state_variables.sv_power_flow import SvPowerFlow
from ucte.operational_limits.voltage_limit import VoltageLimit
from ucte.topology.topological_node import TopologicalNode
from ucte.generation.production.thermal_generating_unit import ThermalGeneratingUnit

from django.utils import simplejson

from openpowersystem.parser import Parser

#------------------------------------------------------------------------------
#  Logging:
#------------------------------------------------------------------------------

logger = logging.getLogger()

#------------------------------------------------------------------------------
#  "MainPage" class:
#------------------------------------------------------------------------------

class MainPage(webapp.RequestHandler):
    """ Defines a request handler for the root url.
    """
    def get(self):
#        terminals_query = Terminal.all().order('-date')
#        terminals = terminals_query.fetch(10)
        terminals = []

#        if users.get_current_user():
#            url = users.create_logout_url(self.request.uri)
#            url_linktext = 'Logout'
#            upload = True
#        else:
#            url = users.create_login_url(self.request.uri)
#            url_linktext = 'Login'
#            upload = False
#
#        template_values = {'terminals': terminals,
#                           'url': url,
#                           'url_linktext': url_linktext,
#                           'upload': upload}
#
#        path = os.path.join(os.path.dirname(__file__), 'index.html')
#
#        self.response.out.write(template.render(path, template_values))

#        path = os.path.join(os.path.dirname(__file__), 'upload.html')
#        self.response.out.write(template.render(path, {}))

        self.redirect('/content/OpenPowerSystem.html')

#------------------------------------------------------------------------------
#  "UploadPage" class:
#------------------------------------------------------------------------------

class UploadPage(webapp.RequestHandler):
    """ Defines a request handler for uploading files.
    """
    def post(self):
#        if users.get_current_user():
        rdf_data = self.request.get('uploadFormElement')
        profile = self.request.get('profileType')

#        logging.debug("Profile Type: %s" % profile)

        Parser(profile).parse(rdf_data)

        self.redirect('/')

#------------------------------------------------------------------------------
#  "JSONHandler" class:
#------------------------------------------------------------------------------

class JSONHandler(webapp.RequestHandler):
    def __init__(self):
        webapp.RequestHandler.__init__(self)
        self.methods = RPCMethods()

    def post(self):
        args = simplejson.loads(self.request.body)
        method_name = args[u"method"]

        if method_name:
            # Deny requests to execute any private or protected methods.
            if method_name[0] == '_':
                self.error(403) # access denied
                return
            else:
                func = getattr(self.methods, method_name, None)
        else:
            func = None

        if not func:
            self.error(404) # file not found
            return

        params = args[u"params"]
        method_id = args[u"id"]
        result = func(params)

        # Reuse args to send result back.
        args.pop(u"method")
        args["result"] = result[0]
        args["error"] = None # IMPORTANT!!
        self.response.headers['Content-Type'] = 'application/json'
        self.response.set_status(200)
        self.response.out.write(simplejson.dumps(args))

#------------------------------------------------------------------------------
#  "RPCMethods" class:
#------------------------------------------------------------------------------

class RPCMethods(object):
    """ Defines methods available for RPC.
    """
    def get_geographical_region_names(self, args):
#        regions = db.GqlQuery("SELECT * FROM GeographicalRegion ORDER BY name DESC LIMIT 10")
        regions = GeographicalRegion.all()
#        regions = GeographicalRegion.gql("ORDER BY name DESC LIMIT 10")

        names = [region.uri for region in regions]
        return [names]

# EOF -------------------------------------------------------------------------
