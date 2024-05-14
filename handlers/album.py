from telethon import Button
from handlers import SPOTIFY


class Album:
    def __init__(self, link):
        self.spotify = SPOTIFY.album(link)
        self.id = self.spotify['id']
        self.album_name = self.spotify['name']
        self.artists_list = self.spotify['artists']
        self.artist_name = self.artists_list[0]['name']
        self.spotify_link = self.spotify['external_urls']['handlers']
        self.album_cover = self.spotify['images'][0]['url']
        self.release_date = self.spotify['release_date']
        self.total_tracks = self.spotify['total_tracks']
        self.track_list = [x['id'] for x in self.spotify['tracks']['items']]
        self.uri = self.spotify['uri']

    async def album_telegram_template(self):
        message = f'''
💿 Альбом : `{self.album_name}`
🎤 Артист : `{self.artist_name}`
🎧 Всего треков : `{self.total_tracks}`
📅 Дата релиза : `{self.release_date}`

[Скачать обложку]({self.album_cover})
[ID]({self.uri})   
        '''

        buttons = [[Button.inline(f'📩 Скачать альбом', data=f"download_album_songs:{self.id}")],
                   [Button.inline(f'🖼️ Скачать обложку', data=f"download_album_image:{self.id}")],
                   [Button.inline(f'🧑‍🎨 Авторы альбома', data=f"album_artist:{self.id}")],
                   [Button.url(f'🎵 Слушать в Spotify', self.spotify_link)],
                   ]

        return message, self.album_cover, buttons

    async def artist_buttons_telethon_templates(self):
        message = f"{self.album_name} album Artist's"
        buttons = [[Button.inline(artist['name'], data=f"artist:{artist['id']}")]
                   for artist in self.artists_list]
        return message, buttons
