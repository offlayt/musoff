from telethon import Button
from handlers import SPOTIFY


class Playlist:
    def __init__(self, link):
        self.spotify = SPOTIFY.playlist(link)
        self.id = self.spotify['id']
        self.spotify_link = self.spotify['external_urls']['handlers']
        self.playlist_name = self.spotify['name']
        self.description = self.spotify['description']
        self.owner_name = self.spotify['owner']['display_name']
        self.followers_count = self.spotify['followers']['total']
        self.track_count = len(self.spotify['tracks']['items'])
        self.playlist_image = self.spotify['images'][0]['url']
        self.uri = self.spotify['uri']

    async def playlist_template(self):
        message = f'''
▶️ Плейлист: {self.playlist_name}
📝 Описание: {self.description}
👤 Создатель: {self.owner_name}
🩷 Подписчики: {self.followers_count}
🔢 Всего треков: {self.track_count}

[Скачать обложку]({self.playlist_image})
[ID]({self.uri})    
'''

        buttons = [[Button.inline(f'📩 Скачать плейлист', data=f"download_playlist_songs:{self.id}")],
                   [Button.inline(f'🖼️ Скачать обложку плейлиста', data=f"download_playlist_image:{self.id}")],
                   [Button.url(f'🎵 Слушать в Spotify', self.spotify_link)],
                   ]
        return message, buttons

    @staticmethod
    def get_playlist_tracks(link):
        return SPOTIFY.playlist_tracks(link, limit=50)['items']
