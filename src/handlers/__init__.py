import nio
import simplematrixbotlib as botlib

from .help import help_handler


def setup(bot: botlib.Bot, prefix: str):
    @bot.listener.on_message_event
    async def help_command(room: nio.rooms.MatrixRoom, message: nio.events.room_events.Event):
        match = botlib.MessageMatch(room, message, bot, prefix=prefix)

        if match.is_not_from_this_bot() and match.prefix() and match.command('help'):
            await help_handler(bot=bot, room_id=room.room_id, sender=message.sender, admin_id=bot.config.admin_id)

