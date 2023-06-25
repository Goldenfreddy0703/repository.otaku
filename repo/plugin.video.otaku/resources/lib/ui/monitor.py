from resources.lib.ui import control
from kodi_six import xbmc


class SettingsMonitor(xbmc.Monitor):
    def __init__(self):
        while (not self.abortRequested()):
            xbmc.sleep(1000)

    def onSettingsChanged(self):
        control.setGlobalProp("calendarRefresh", True)
