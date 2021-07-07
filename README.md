# YouTube Music Playlist Restore
Easily restore your YouTube Music Playlists from a Google Takeout.

## First-time setup
* Clone this repo
* Install required modules:
```
pip3 install --user -r requirements.txt
```
### Generate authentication headers automatically
* Follow instructions in the ["Copy Authentication Headers" section of ytmusicapi/setup](https://ytmusicapi.readthedocs.io/en/latest/setup.html#copy-authentication-headers)
* Run ./setup.py and follow the instructions there
### OR generate authentication headers manually (best for Mac)
* Follow instructions in the ["Manual file creation" section of ytmusicapi/setup](https://ytmusicapi.readthedocs.io/en/latest/setup.html#manual-file-creation)

## Usage
* Open your latest Google Takeout in 7-zip or WinRAR or whatever program you use and locate the .csv files for your YouTube Music Playlists.
* Copy the csv files into the playlists folder.
* Remove any csv files that match playlists that already exist on your account (e.g. "Liked Videos")
* Run ./transfer.py
