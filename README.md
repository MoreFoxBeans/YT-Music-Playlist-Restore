# YouTube Music Playlist Restore
Easily restore your YouTube Music Playlists from a Google Takeout.

## First-time setup
1. Download the code
2. Follow the "Copy Authentication Headers" section of [ytmusicapi/setup](https://ytmusicapi.readthedocs.io/en/latest/setup.html)
3. Run "setup.py" in CMD and follow the instructions there.

## Usage
1. Open your latest Google Takeout in 7-zip or WinRAR or whatever program you use and locate the .csv files for your YouTube Music Playlists.
2. Create a "playlists" folder in your YT-Music-Playlist-Restore folder and copy the csv files into it.
3. Remove any csv files that match playlists that already exist on your account (e.g. "Liked Videos")
4. Run transfer.py
