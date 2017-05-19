import weechat
import time
weechat.register("list_buffs", "FlashCode", "1.0", "GPL3", "List all the buffers", "", "")

# read infolist "buffer", to get list of buffers
infolist = weechat.infolist_get("buffer", "", "")
if infolist:
    while weechat.infolist_next(infolist):
        name = weechat.infolist_string(infolist, "name")
        weechat.prnt("", "buffer: %s" % name)
    weechat.infolist_free(infolist)


