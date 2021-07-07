#!/usr/bin/env python3
from ytmusicapi import YTMusic
import os
import csv

ytmusic = YTMusic('headers_auth.json')

root = "playlists"

for item in os.listdir(root):
    if os.path.isfile(os.path.join(root, item)):
        print(os.path.join(root, item))
        with open(os.path.join(root, item)) as playlistcsv:
            reader = csv.reader(playlistcsv)
            items = []
            for row in reader:
                if (len(row) == 7) and (row[0] != 'Playlist Id'):
                    title = row[4]
                    description = row[5]
                    visibility = row[6]
                elif (len(row) == 2) and (row[0] != 'Video Id'):
                    items.append(row[0])
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
