# gmusic_export

Exports all Google Music playlists to import into Spotify via http://www.ivyishere.org/ivy/run

Your own music will not be readable and only the track ids will be written. 
To get the names, open the playlist in chrome, zoom out as much as possible and run this javascript

```
var playlist = document.querySelectorAll('.song-table tr.song-row');
for(var i =0; i<playlist.length ; i++) {
  var l = playlist[i];
  var title = l.querySelectorAll('td[data-col="title"] .content')[0].textContent;
  var artist = l.querySelectorAll('td[data-col="artist"] .content')[0].textContent;
  console.log(artist + ' - ' + title);
}
```

You might need to scroll down and repeat until all tracks have been listed.
