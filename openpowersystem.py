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

class MainPage(webapp.RequestHandler):
  def get(self):
#    terminals_query = Terminal.all().order('-date')
#    terminals = terminals_query.fetch(10)
    terminals = []

    if users.get_current_user():
      url = users.create_logout_url(self.request.uri)
      url_linktext = 'Logout'
      upload = True
    else:
      url = users.create_login_url(self.request.uri)
      url_linktext = 'Login'
      upload = False

    template_values = {'terminals': terminals,
                       'url': url,
                       'url_linktext': url_linktext,
                       'upload': upload}

    path = os.path.join(os.path.dirname(__file__), 'index.html')

    self.response.out.write(template.render(path, template_values))

class UploadPage(webapp.RequestHandler):
  def post(self):

    if users.get_current_user():
        rdf_data = self.request.get('fname')
        ns_cim = self.request.get('ns_cim')

        parser = CIMParser()
        parser(rdf_data)

    self.redirect('/')

application = webapp.WSGIApplication([('/', MainPage),
                                      ('/upload', UploadPage)],
                                     debug=True)

def main():
  logging.getLogger().setLevel(logging.DEBUG)

  run_wsgi_app(application)

if __name__ == "__main__":
  main()
