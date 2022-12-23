from Bot.database.users_sql import num_users
from Bot.database.chats_sql import num_chats
from pyrogram import Client, filters
from pyrogram.types import Message
from Config import OWNER_ID


@Client.on_message(filters.user(OWNER_ID) & ~filters.edited & filters.command("stats"))
async def _stats(_, msg: Message):
    chats = num_chats()
    users = num_users()
    await msg.reply(f"🍀 Chats Stats 🍀\n\n 🙋‍♂️ Users : : {users} \n👥 Groups : {chats}", quote=True)
