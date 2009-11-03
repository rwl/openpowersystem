===============
OpenPowerSystem
===============

Open map of the global power system defined according to profiles of the IEC
Common Information Model.

License
-------

GNU Affero General Public License

Developers
----------

Download the Google App Engine SDK and extract the archive. Add

 * .../google_appengine,
 * .../google_appengine/lib/django,
 * .../google_appengine/lib/webob, and
 * .../google_appengine/lib/yaml/lib

to the PYTHON_PATH. Run

::

  $ dev_appserver.py path/to/OpenPowerSystem/

Browse http://localhost:8080. Changes are recognised automatically. Upload the
finished application with the command::

  $ appcfg.py update path/to/OpenPowerSystem/

To re-build the Pyjamas app run;

::

  $ pyjsbuild -o ../content OpenPowerSystem

in the 'pyjs' directory.

N.B. The 'content' attribute in the .html loader must be the module name.

Author
------

Richard Lincoln (r.w.lincoln@gmail.com)
