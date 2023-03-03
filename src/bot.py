import os
import logging

from aiogram import (
    Dispatcher,
    Bot
)
from aiogram.types import (
    Message,
    ContentType
)
from aiogram import exceptions

TOKEN = os.getenv("TOKEN")
if TOKEN is None:
    raise RuntimeError("TOKEN is invalid!")

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(content_types=[ContentType.NEW_CHAT_MEMBERS, ContentType.LEFT_CHAT_MEMBER])
async def user_join_exit_handler(message: Message):
    try:
        msg = "joined"
        if message.left_chat_member:
            msg = "exited"
        logging.info(message.from_user['first_name'] + " " + msg)
        await message.delete()
    except (exceptions.MessageCantBeDeleted, exceptions.BotKicked) as e:
        logging.info(f"Error! Message cannot be deleted! Reason: {e}")

@dp.message_handler(commands=["start", "help"])
async def help_message_handler(message: Message):
    return await message.reply("Add me to a group and I'll clean that 'User has Joined' messages!")
