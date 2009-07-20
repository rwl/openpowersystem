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

import os
import cgi
import logging

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.ext import db

from cim_parser import CIMParser

from django.utils import simplejson

class MainPage(webapp.RequestHandler):
  def get(self):
#    terminals_query = Terminal.all().order('-date')
#    terminals = terminals_query.fetch(10)
    terminals = []

#    if users.get_current_user():
#      url = users.create_logout_url(self.request.uri)
#      url_linktext = 'Logout'
#      upload = True
#    else:
#      url = users.create_login_url(self.request.uri)
#      url_linktext = 'Login'
#      upload = False
#
#    template_values = {'terminals': terminals,
#                       'url': url,
#                       'url_linktext': url_linktext,
#                       'upload': upload}
#
#    path = os.path.join(os.path.dirname(__file__), 'index.html')
#
#    self.response.out.write(template.render(path, template_values))

#    path = os.path.join(os.path.dirname(__file__), 'upload.html')
#    self.response.out.write(template.render(path, {}))

    self.redirect('/app/ops.html')


class UploadPage(webapp.RequestHandler):
  def post(self):

    if users.get_current_user():
        rdf_data = self.request.get('fname')
        ns_cim = self.request.get('ns_cim')

        parser = CIMParser()
        parser(rdf_data)

    self.redirect('/')


class JSONHandler(webapp.RequestHandler):
  def post(self):
    args = simplejson.loads(self.request.body)
    json_func = getattr(self, 'json_%s' % args[u"method"])
    json_params = args[u"params"]
    json_method_id = args[u"id"]
    result = json_func(json_params)
    # reuse args to send result back
    args.pop(u"method")
    args["result"] = result[0]
    args["error"] = None # IMPORTANT!!
    self.response.headers['Content-Type'] = 'application/json'
    self.response.set_status(200)
    self.response.out.write(simplejson.dumps(args))

  def json_upper(self,args):
    return [args[0].upper()]

application = webapp.WSGIApplication([('/', MainPage),
                                      ('/upload', UploadPage),
                                      ('/json', JSONHandler)],
                                     debug=True)

def main():
  logging.getLogger().setLevel(logging.DEBUG)

  run_wsgi_app(application)

if __name__ == "__main__":
  main()
