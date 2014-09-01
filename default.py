import sys
import os, datetime
import xbmc, xbmcgui, xbmcaddon, xbmcplugin, xbmcvfs

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

def startPlaylist():
    if not xbmc.getCondVisibility("Player.HasMedia"):
        playlistpath = __addon__.getSetting("playlistpath")
        if xbmcvfs.exists(playlistpath):
            xbmc.Player().play(playlistpath)
            xbmcPlaylist = xbmc.PlayList(xbmc.PLAYLIST_MUSIC)
            xbmcPlaylist.shuffle()


class Daemon:
    def __init__( self ):
        log("version %s started" % __addonversion__ )
        self.Player = BgMusic_Player( enabled = True )
        self.run_backend()
        
    def run_backend(self):
        self._stop = False
        xbmc.sleep(1000)
        startPlaylist()                    
        while (not self._stop) and (not xbmc.abortRequested):
            if __addon__.getSetting("playonce") == "false":
                log("start playlist")
                startPlaylist()
                xbmc.sleep(1000) 
            log("backend active")    
            xbmc.sleep(1000)     

class BgMusic_Player( xbmc.Player ):
    def __init__(self, *args, **kwargs):
        xbmc.Player.__init__( self )
        self.enabled = kwargs['enabled']
        
    def onPlayBackEnded( self ):
        # Will be called when xbmc stops playing a file
        if not __addon__.getSetting("playonce") == "false":
            pass
    
    def onPlayBackStopped( self ):
        # Will be called when user stops xbmc playing a file
        if not __addon__.getSetting("playonce") == "false":
            pass
         
if ( __name__ == "__main__" ):
    Daemon()
log('finished')
