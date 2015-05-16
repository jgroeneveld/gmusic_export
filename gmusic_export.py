# https://github.com/simon-weber/Unofficial-Google-Music-API

import json
import re
import credentials
from gmusicapi import Mobileclient


api = Mobileclient()
api.login(credentials.MAIL, credentials.PASS)

playlists = api.get_all_user_playlist_contents()

def run():
    for pl in playlists:
        write_playlist(pl)

def write_playlist(pl):
    name = pl["name"]
    tracks = pl["tracks"]
    f = open("playlists/" + encode(name) + ".txt", "w")
    print name
    print "======="
    for t in tracks:
        line = t["trackId"]
        if "track" in t:
            line = t["track"]["artist"] + " - " + t["track"]["title"]
        print line
        f.write(line.encode('utf8', 'replace') + "\n")

    print ""
    f.close()

def encode(name):
    return re.sub("[^a-z0-9A-Z]", "_", name)




run()
# print json.dumps(playlists)
