from utils import BOT_TOKEN, CLIENT, songcallback,\
    albumcallback, newmessage, artistcallback,\
    playlistcallback


if __name__ == '__main__':
    print('[BOT] Starting session...')
    CLIENT.start(bot_token=BOT_TOKEN)
    print('[BOT] Status: online')
    CLIENT.run_until_disconnected()
