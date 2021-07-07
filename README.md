# YouTube Music Playlist Restore
Easily restore your YouTube Music Playlists from a Google Takeout.

## First-time setup
* Clone this repo
* Install the required modules:
```
pip3 install --user -r requirements.txt
```
### Generate authentication headers
* Go to [YouTube Music](https://music.youtube.com) and ensure you are logged in.
* Open Developer Tools (F12, Ctrl+Shift+I) and select the Network tab
* Find an authenticated POST request. The simplest way is to filter by `/browse` using the search bar of Developer Tools. It should start with `browse?`.
* Click on the name of any matching request. In the "Headers" tab, scroll to the section "Request Headers" and copy the line starting with but not including `cookie:`
* Run setup.py and paste the cookie there. You should be good to go!

## Usage
* Open your latest Google Takeout in 7-Zip or WinRAR or whatever program you use and locate the .csv files for your YouTube Music Playlists. Copy them into the "playlists" folder
* Remove any csv files that match playlists that already exist on your account (e.g. "Liked Videos")
* Run ./transfer.py
