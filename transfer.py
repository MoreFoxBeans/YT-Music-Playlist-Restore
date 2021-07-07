#!/usr/bin/env python3
from ytmusicapi import YTMusic
import os
import csv
import fnmatch

ytmusic = YTMusic('headers_auth.json')

root = "playlists"

for file in os.listdir(root):
    if fnmatch.fnmatch(file, '*.csv'):
        print(os.path.join(root, file))
        with open(os.path.join(root, file)) as playlistcsv:
            reader = csv.reader(playlistcsv)
            items = []
            for line in reader:
                if (len(line) == 7) and (line[0] != 'Playlist Id'):
                    title = line[4]
                    description = line[5]
                    visibility = line[6]
                elif (len(line) == 2) and (line[0] != 'Video Id'):
                    items.append(line[0])
        try:
            playlistId = ytmusic.create_playlist(title, description, visibility.upper())
            print('[ OK ] Created playlist "' + title + '" with description "' + description + '"')
            for item in items:
                try:
                    ytmusic.add_playlist_items(playlistId, [item])
                    try:
                        song = ytmusic.get_song(item)
                        print('[ OK ] Added song "' + song['videoDetails']['title'] + '"!')
                    except:
                        print('[ OK ] Added song!')
                except:
                    print('[WARN] Failed to add song! Is it private or removed?')
        except Exception as e:
            print('[WARN] Failed to create playlist "' + title + '"!')
            print('========== EXCEPTION ==========')
            print(str(e))
            print('======== END EXCEPTION ========')
