import simplematrixbotlib as botlib


async def help_handler(room_id: str, bot: botlib.Bot, sender: str, admin_id: str):
    msg: str = 'Hi **{}**\n\n' \
               'Prefix: `!`\n' \
               'Its a simplematrixbotlib template!\n' \
               'Admin contact: **{}**'

    await bot.api.send_markdown_message(room_id=room_id, message=msg.format(sender, admin_id))
