import argparse
from pytube import YouTube
import moviepy.editor as mp
import sys
import time
# import logging
import progressbar
from pytube import Playlist



parser = argparse.ArgumentParser()

parser.add_argument("-U", "--url", help="python3 {target} --url Target"
.format(
	target=sys.argv[0]
))
parser.add_argument("-I", "--itag", help="python3 {target} --url Target --itag 152"
.format(
	target=sys.argv[0]
))

parser.add_argument("-p", "--path", help="python3 {target} --url Target --itag 152 --path"
.format(
	target=sys.argv[0]
))




playlis = parser.add_argument_group("playlist", "--LIST URL --CANT: MUSICA-DE TU-LISTA:[15] --RES 18. [res=itag] \nUSAGE: python3 {target} -- list youtube/URL/list.com --cant 12 --res 150".format(target=sys.argv[0])
	)
playlis.add_argument("--list", "-L", help="python3 {target} -- list".format(target=sys.argv[0]))
playlis.add_argument("--cant", "-C", help="python3 {target} -- list --cant".format(target=sys.argv[0]))
playlis.add_argument("--res", "-R", help="python3 {target} -- list --cant --res".format(target=sys.argv[0]))
playlis.add_argument("--path-save", "-S", help="python3 {target} -- list --cant --res --PATH".format(target=sys.argv[0]))






args = parser.parse_args()


if not len(sys.argv) > 1:
	if sys.version_info.major >= 3:

		parser.print_help()

if args.url:
	links = sys.argv[2]
	yt = YouTube(links)

	title = yt.title
	print("Search Music: ", title+"\n\n")

	resolucoe = yt.streams.all()

	progressbar.streams.wrap_stderr()
	# logging.basicConfig()

	for i in progressbar.progressbar(resolucoe, redirect_stdout=True):

		print("Format: "+'itag: {itag}, mime_type: {mime_type}, res:{res} abr: {abr}, acodec: {acodec}, type: {type}'
		.format(
			itag=i.itag,
			mime_type=i.mime_type,
			res=i.resolution,
			abr= i.abr,
			acodec=i.audio_codec,
			type=i.type
		)
	)
	time.sleep(0.2)
if args.itag:
	if len(sys.argv) > 5:
		path = sys.argv[6]
	else:
		path = './'
	Dowload_FIle = sys.argv[4]
	
	if(Dowload_FIle == ""):
		exit()
	else:
		print("Downloading ...... : {title}"
		.format(
			title=title
		))
		stream = yt.streams.get_by_itag(Dowload_FIle)
		widgets=[
		' [', progressbar.Timer(), '] ',
		progressbar.Bar(),
		' (', progressbar.ETA(), ') ',
		]
		for i in progressbar.progressbar(stream.download(path), widgets=widgets):
			time.sleep(0.3)
		print("\n\nDownloading is Compled\n\n")
# Playlist Downloads

if args.list:

	link_playlist=sys.argv[2]
	Cantidad_music=sys.argv[4]

	playlist = Playlist(link_playlist)
	for url in playlist.video_urls[:int(Cantidad_music)]:

		yt = YouTube(url)
		video_name = yt.title

		print("\n\n",video_name)
		print(url)

		
	resolucoes = yt.streams
	for i in resolucoes:
		print("\nFormat: "+'itag: {itag}, mime_type: {mime_type}, res:{res} abr: {abr}, acodec: {acodec}, type: {type}'
		.format(
				itag=i.itag,
				mime_type=i.mime_type,
				res=i.resolution,
				abr= i.abr,
				acodec=i.audio_codec,
				type=i.type
			)
		)

		
if args.res:
	Dowload_playlist = sys.argv[6]
	if len(sys.argv) > 7:
		path_sys = path = sys.argv[8]
	else:
		path = './'
		

	for video in yt.videos:
		print(f'Downloading Playlist ...  {yt.title}')
		video.streams.get_by_itag(int(Dowload_playlist)).download(path_sys)



    
    # name = path+"/"+title
    #     #Cargamos el fichero .mp4
    # clip = mp.VideoFileClip("{name}.mp4".format(name=name))

    #     #Lo escribimos como audio y `.mp3`
    # clip.audio.write_audiofile('{name}.mp3'.format(name=name), bitrate="320k")
