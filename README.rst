===============
OpenPowerSystem
===============

Open map of the global power system defined according to profiles of the IEC
Common Information Model.

License
-------

GNU Affero General Public License

Author
------

Richard Lincoln (r.w.lincoln@gmail.com)

Developers
----------

Download the Google App Engine SDK and extract the archive. Add

 * .../google_appengine,
 * .../google_appengine/lib/django,
 * .../google_appengine/lib/webob, and
 * .../google_appengine/lib/yaml/lib

to the PYTHON_PATH. Run

::

  $ dev_appserver.py path/to/openpowersystem/

Browse http://localhost:8080. Changes are recognised automatically. Upload the
finished application with the command::

  $ appcfg.py update path/to/openpowersystem/
