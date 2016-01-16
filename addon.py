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
	'C1'""",
	'Edu TV',
	'NTV',
	'TV5',
	'Eagle News',
	'SBN',
	'NBS 1',
	'TV8',
	'TM',
	'Suld TV',
	'Mass TV',
	'Fashion TV',
	'TV9',
	'Olloo TV',
	'Seven Channel',
	'Star HD',
	'Eco Channel',
	'ETV',
	'VTV',
	'Royal HD',
	'MNC',
	'Эх Орон',
	'ZA',
	'Like HD',
	'HTV',
	'TB1',
	'4K KMG',
	'OTV',
	'TV10',
	'Молор',
	'SCH'"""
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
	'http://103.60.97.11/e1/c1_480p.stream/playlist.m3u8'""",
	'http://103.60.97.11/e1/edu_480p.stream/playlist.m3u8',
	'http://103.60.97.11/e1/ntv_480p.stream/playlist.m3u8',
	'http://103.60.97.11/e1/tv5.stream/playlist.m3u8',
	'http://103.60.97.11/e1/eagle_480p.stream/playlist.m3u8',
	'http://103.60.97.11/e1/sbn.stream/playlist.m3u8',
	'http://103.60.97.11/e1/nbs.stream/playlist.m3u8',
	'http://103.60.97.11/e1/tv8.stream/playlist.m3u8',
	'http://103.60.97.11/e1/tm.stream/playlist.m3u8',
	'http://103.60.97.11/e1/suld_480p.stream/playlist.m3u8',
	'http://103.60.97.11/e1/mass.stream/playlist.m3u8',
	'http://103.60.97.11/e1/ftv.stream/playlist.m3u8',
	'http://103.60.97.11/e1/tv9_480p.stream/playlist.m3u8',
	'http://103.60.97.11/e1/olloo.stream/playlist.m3u8',
	'http://103.60.97.11/e1/seven.stream/playlist.m3u8',
	'http://103.60.97.11/e1/star.stream/playlist.m3u8',
	'http://103.60.97.11/e1/eco.stream/playlist.m3u8',
	'http://103.60.97.11/e1/etv.stream/playlist.m3u8',
	'http://103.60.97.11/e1/shine_delhii.stream/playlist.m3u8',
	'http://103.60.97.11/e1/royalhd.stream/playlist.m3u8',
	'http://103.60.97.11/e1/mnc.stream/playlist.m3u8',
	'http://103.60.97.11/e1/ehoron.stream/playlist.m3u8',
	'http://103.60.97.11/e1/za.stream/playlist.m3u8',
	'http://103.60.97.11/e1/like.stream/playlist.m3u8',
	'http://103.60.97.11/e1/htv.stream/playlist.m3u8',
	'http://103.60.97.11/e1/tv1.stream/playlist.m3u8',
	'http://103.60.97.11/e1/kmg1.stream/playlist.m3u8',
	'http://103.60.97.11/e1/otv.stream/playlist.m3u8',
	'http://103.60.97.11/e1/tv10.stream/playlist.m3u8',
	'http://103.60.97.11/e1/molor_480p.stream/playlist.m3u8',
	'http://103.60.97.11/e1/sch.stream/playlist.m3u8'"""
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
	'c1_512x512.png'""",
	'edu_512x512.png',
	'ntv_512x512.png',
	'tv5_512x512.png',
	'eagle_512x512.png',
	'sbn_512x512.png',
	'nbs_512x512.png',
	'tv8_512x512.png',
	'tm_512x512.png',
	'suld_512x512.png',
	'mass_512x512.png',
	'fashion_512x512.png',
	'tv9_512x512.png',
	'olloo_512x512.png',
	'seven_512x512.png',
	'star_512x512.png',
	'eco_512x512.png',
	'etv_512x512.png',
	'shine_delhii_512x512.png',
	'royalhd_512x512.png',
	'mnc_512x512.png',
	'ehoron_512x512.png',
	'za_512x512.png',
	'like_512x512.png',
	'htv_512x512.png',
	'tv1_512x512.png',
	'kmg1_512x512.png',
	'otv_512x512.png',
	'tv10_512x512.png',
	'molor_512x512.png',
	'sch_512x512.png'"""
]

for name,url,icon in zip(names,urls,icons):
	li = xbmcgui.ListItem(label=name, path=url)
	li.setThumbnailImage(os.path.join(image_dir,icon))
	li.setIconImage(os.path.join(image_dir,icon))
	li.setInfo(type='Video', infoLabels={ "Title": name })
	li.setProperty('IsPlayable', 'true')
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)
