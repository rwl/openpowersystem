from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.VerticalPanel import VerticalPanel

from OpenMaps import OLMap

class OL:
    def onModuleLoad(self):
        self.map = OLMap("http://labs.metacarta.com/wms/vmap0",
                         width="60%", height="80%")

        RootPanel().add(self.map)

if __name__ == '__main__':
    app = OL()
    app.onModuleLoad()

