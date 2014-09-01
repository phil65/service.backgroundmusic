import sys
import os, datetime
import xbmc, xbmcgui, xbmcaddon, xbmcplugin

__addon__        = xbmcaddon.Addon()
__addonid__      = __addon__.getAddonInfo('id')
__addonversion__ = __addon__.getAddonInfo('version')
__language__     = __addon__.getLocalizedString

Addon_Data_Path = os.path.join( xbmc.translatePath("special://profile/addon_data/%s" % __addonid__ ).decode("utf-8") )
def log(txt):
    if isinstance(txt, str):
        txt = txt.decode("utf-8")
    message = u'%s: %s' % (__addonid__, txt)
    xbmc.log(msg=message.encode("utf-8"), level=xbmc.LOGDEBUG)

class Daemon:
    def __init__( self ):
        log("version %s started" % __addonversion__ )
        self.run_backend()
        
    def run_backend(self):
        self._stop = False
        xbmc.sleep(1000)
        if not xbmc.getCondVisibility("Player.HasMedia"):
            xbmc.Player().play(__addon__.getSetting("playlistpath"))                     
        while (not self._stop) and (not xbmc.abortRequested):
            if not xbmc.getCondVisibility("Player.HasMedia"):
                if __addon__.getSetting("playonce") == "false":
            #    xbmc.PlayList( xbmc.PLAYLIST_MUSIC ).load(__addon__.getSetting("playlistpath"))                     
                    xbmc.Player().play(__addon__.getSetting("playlistpath"))                     
            else:
                xbmc.sleep(500)     
            xbmc.sleep(1000)     

         
if ( __name__ == "__main__" ):
    Daemon()
log('finished')
