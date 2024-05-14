from telethon import events, Button
from telethon.tl import types
from handlers.searcher import search_single


async def handle_search_message(event: events.NewMessage.Event):
    msg = event.message.message
    song_items = search_single(msg)

    # Buttons for each song item
    buttons = []
    for song_item in song_items:
        # Create a new row for each button
        button = [Button.inline(f'{song_item.track_name} - {song_item.artist_name}', data=f"song:{song_item.id}")]
        buttons.append(button)

    # Reply message with buttons
    reply_message = "❌ Ничего не найдено. Попробуйте еще раз!"
    if buttons:
        reply_message = "🔎 Вот, что я нашел: "
        await event.reply(reply_message, buttons=buttons)
    else:
        await event.respond('❌')
        await event.reply(reply_message, )
