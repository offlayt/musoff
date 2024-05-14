from telethon import Button

from handlers import SPOTIFY


class Artist:
    def __init__(self, artist_id):
        self.spotify = SPOTIFY.artist(artist_id)
        self.id = self.spotify['id']
        self.artist_name = self.spotify['name']
        self.followers_count = self.spotify['followers']['total']
        self.genres = self.spotify['genres']
        self.uri = self.spotify['uri']
        self.artist_profile = self.spotify['images'][0]['url']
        self.spotify_link = self.spotify['external_urls']['handlers']

    async def artist_telethon_template(self):
        message = f'''
👤 Артист : `{self.artist_name}`
🩷 Подписчики : `{self.followers_count}`
🎶 Жанры : `{self.genres}`

[Скачать аватар]({self.artist_profile})
[ID]({self.uri})
            '''

        buttons = [[Button.inline(f'🖼️ Аватар артиста', data=f"download_artist_image:{self.id}")],
                   [Button.inline(f"👀 Популярные треки", data=f"artist_top_tracks:{self.id}")],
                   [Button.inline(f'🧑‍🎨 Альбомы артиста', data=f"artist_albums:{self.id}")],
                   [Button.url(f'🎵 Слушать в Spotify', self.spotify_link)],
                   ]

        return message, buttons

    async def artist_top_tracks_template(self):
        top_tracks = SPOTIFY.artist_top_tracks(self.id)
        buttons = [[Button.inline(f"{track['name']} - {track['artists'][0]['name']}",
                                 data=f"song:{track['id']}")] for track in top_tracks['tracks']]
        return self.artist_name, buttons

    async def artist_albums_template(self):
        top_tracks = SPOTIFY.artist_albums(self.id)
        buttons = [[Button.inline(f"{album['name']} - {album['artists'][0]['name']}",
                                 data=f"artist:{album['id']}")] for album in top_tracks['items']]
        return self.artist_name, buttons