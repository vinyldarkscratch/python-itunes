# pyitunes

A simple python wrapper for accessing the iTunes Store API [iTunes Store
API]

## Installation

To install with `pip`, just run this in your terminal:

    $ pip install pitunes

Or clone the code from [Github](https://github.com/vinyldarkscratch/pitunes) and:

    $ python setup.py install

## Caching

This module caches responses from the iTunes API to speed up repeated
queries against the same resources. Note, however, that there's no
persistent caching that happens between Python processes. Ie, once a
python process exits, the cache is cleared.

## Examples

### Search

```
from __future__ import print_function
import itunes

# Search band U2
artist = itunes.search_artist('u2')[0]
for album in artist.get_albums():
    for track in album.get_tracks():
        print(album.name, album.url, track.name, track.duration, track.preview_url)

# Search U2 videos
videos = itunes.search(query='u2', media='musicVideo')
for video in videos:
    print(video.name, video.preview_url, video.artwork)

# Search Volta album by Björk
album = itunes.search_album('Volta Björk')[0]

# Global Search 'Beatles'
items = itunes.search(query='beatles')
for item in items:
    print('[' + item.type + ']', item.artist, item.name, item.url, item.release_date)

# Search 'Angry Birds' game
item = itunes.search(query='angry birds', media='software')[0]
vars(item)

# Search 'Family Guy Season 1'
item = itunes.search_season('Family Guy Season 1')[0]
vars(item)

# Search 'Episode 5 of Family Guy Season 1'
items = itunes.search_episode('Family Guy Season 1')
for ep in items:
    if ep.episode_number == 5:
        vars(ep)
```

### Lookup by iTunes ID

```
import itunes

# Lookup Achtung Baby album by U2
U2_ACHTUNGBABY_ID = 475390461
album = itunes.lookup(U2_ACHTUNGBABY_ID)

print(album.url)
print(album.artwork)

artist = album.artist
tracks = album.get_tracks()

# Lookup song One from Achtung Baby album by U2
U2_ONE_ID = 475391315
track = itunes.lookup(U2_ONE_ID)

artist = track.artist
album = track.get_album()
```

### Lookup by UPC

```
import itunes

# Lookup Arcade EP by glitch_d using UPC
ARCADE_EP_UPC = 5057917815772
album = itunes.lookup_upc(ARCADE_EP_UPC)

print(album.url)
print(album.artwork)

artist = album.artist
tracks = album.get_tracks()
```

## Tests

    $ py.test tests

## References

- [iTunes Store API](http://www.apple.com/itunes/affiliates/resources/documentation/itunes-store-web-service-search-api.html)
- [pip](http://www.pip-installer.org/)
- [Github](https://github.com/vinyldarkscratch/python-itunes)