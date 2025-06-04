#!/usr/bin/env python3
import argparse
from yt_dlp import YoutubeDL
# do pip install yt-dlp and choco install ffmpeg (or brew install ffmpeg) if you don't have them already
def download_audio(playlist_url, start, end, output_template):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_template,      # examples: "%(playlist_index)s - %(title)s.%(ext)s" "%(title)s - %(uploader)s.%(ext)s" "%(uploader)s/%(title)s.%(ext)s" "%(playlist_title)s/%(playlist_index)03d - %(title)s.%(ext)s" "%(id)s.%(ext)s" "%(playlist_index)03d - %(title)s.%(ext)s" "%(upload_date)s - %(title)s.%(ext)s"
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ignoreerrors': True,            # skip unavailable trash
        'playliststart': start,
        'playlistend': end,
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

if __name__ == '__main__':
    p = argparse.ArgumentParser(description="Download MP3s from a YouTube playlist slice")
    p.add_argument('url', help="YouTube playlist URL")
    p.add_argument('-s', '--start', type=int, default=1, help="Playlist start index (1-based)")
    p.add_argument('-e', '--end',   type=int, default=None, help="Playlist end index")
    p.add_argument('-o', '--output', default='%(playlist_index)03d - %(title)s.%(ext)s',help="Output filename template")
    args = p.parse_args()
    download_audio(args.url, args.start, args.end, args.output) # usage: python ytPlaylistDownloader.py <playlist_url> -s <start_index> -e <end_index> -o <output_template> (make sure the playlist is public)
# .     .       .  .   . .   .   . .    +  .
#   .     .  :     .    .. :. .___---------___.
#        .  .   .    .  :.:. _".^ .^ ^.  '.. :"-_. .
#     .  :       .  .  .:../:            . .^  :.:\.
#         .   . :: +. :.:/: .   .    .        . . .:\
#  .  :    .     . _ :::/:               .  ^ .  . .:\
#   .. . .   . - : :.:./.                        .  .:\
#   .      .     . :..|:                    .  .  ^. .:|
#     .       . : : ..||        .                . . !:|
#   .     . . . ::. ::\(                           . :)/
#  .   .     : . : .:.|. ######              .#######::|
#   :.. .  :-  : .:  ::|.#######           ..########:|
#  .  .  .  ..  .  .. :\ ########          :######## :/
#   .        .+ :: : -.:\ ########       . ########.:/
#     .  .+   . . . . :.:\. #######       #######..:/
#       :: . . . . ::.:..:.\           .   .   ..:/
#    .   .   .  .. :  -::::.\.       | |     . .:/
#       .  :  .  .  .-:.":.::.\             ..:/
#  .      -.   . . . .: .:::.:.\.           .:/
# .   .   .  :      : ....::_:..:\   ___.  :/
#    .   .  .   .:. .. .  .: :.:.:\       :/
#      +   .   .   : . ::. :.:. .:.|\  .:/|
#      .         +   .  .  ...:: ..|  --.:|
# .      . . .   .  .  . ... :..:.."(  ..)"
#  .   .       .      :  .   .: ::/  .  .::\