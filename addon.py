import sys
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin
import os

addon_handle = int(sys.argv[1])
base_url = sys.argv[0]

__settings__ = xbmcaddon.Addon(id='plugin.video.mongolian-live-tv')
rootDir = xbmc.translatePath(__settings__.getAddonInfo('path')).decode('utf-8')
image_dir = os.path.join(rootDir, 'resources', 'media')

print image_dir

xbmcplugin.setContent(addon_handle, 'videos')

names = [
	'MNB 1',
	'MNB 2',
	'UBS',
	'UBS Global',
	'UBS Music',
	'Movie Box',
	'Dream Box',
	'Sport Box',
	'C1',
	'Edu TV'
]
urls = [
	'http://103.60.97.11/e1/mnb_480p.stream/playlist.m3u8',
	'http://103.60.97.11/e1/mn2.stream/playlist.m3u8',
	'http://103.60.97.11/e1/ubs_480p.stream/playlist.m3u8',
	'http://103.60.97.11/e1/ubs_global.stream/playlist.m3u8',
	'http://103.60.97.11/e1/ubs_music.stream/playlist.m3u8',
	'http://103.60.97.11/e1/moviebox_480p.stream/playlist.m3u8',
	'http://103.60.97.11/e1/dreambox.stream/playlist.m3u8',
	'http://103.60.97.11/e1/sportbox_hd_480p.stream/playlist.m3u8',
	'http://103.60.97.11/e1/c1_480p.stream/playlist.m3u8',
	'http://103.60.97.11/e1/edu_480p.stream/playlist.m3u8'
]
icons=[
	'mnb_512x512.png',
	'mn2_512x512.png',
	'ubs_512x512.png',
	'ubs_global_512x512.png', 
	'ubs_music_512x512.png',
	'moviebox_512x512.png',
	'dreambox_512x512.png',
	'sportbox_hd_512x512.png',
	'c1_512x512.png',
	'edu_512x512.png'
]

for name,url,icon in zip(names,urls,icons):
	li = xbmcgui.ListItem(label=name, path=url)
	li.setThumbnailImage(os.path.join(image_dir,icon))
	li.setIconImage(os.path.join(image_dir,icon))
	li.setInfo(type='Video', infoLabels={ "Title": name })
	li.setProperty('IsPlayable', 'true')
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)
