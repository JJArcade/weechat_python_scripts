import weechat
import time
weechat.register("song_reqs", "FlashCode", "1.0", "GPL3", "fast request of songs", "", "")

# Load songs
songs_file = open("/home/jess/Documents/songs/songs.txt")
songs = []
request_raw = "!songrequest %s"

for a in songs_file.readlines():
    temp = request_raw % a[:len(a)-1]
    songs.append(temp)
    weechat.prnt("", temp)
    weechat.command(weechat.current_buffer(), temp)
    time.sleep(.5)
