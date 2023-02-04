from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
👋Hello {}

I can upload media to telegra.ph and give you back the link with ease. Try sending multiple media, and it still won't stop me.
I can also be used in groups !!
To see `Supported Media Types` tap the related button below.
Use the other buttons to know more about me and my usage.

Powerd By : @SdBotz
    """

    # Help Message
    HELP = """
🆘**HOW TO USE ME**🆘

See `Supported Media Types` by clicking that related button below.

🍁**How to use me here?**🍁
Just send the media and leave rest on me. 

🌺**How to use in group?**🌺
Add to me the group.
Then reply to a media with /telegraph to get the telegra.ph link.

☘️**Commands**☘️

>> /t
>> /tg
>> /telegraph

More features in development. Keep track by joining @SDBOTS_Inifinity.
    """

    # About Message
    ABOUT = """
☃️**About This Bot**☃️

🍁Bot created by @SDBOTS_Inifinity & @EmoBotDevolopers

📦Source Code : [Click Here](https://github.com/RishBropromax/Telegraph-Uploader)

☘️Framework : [Pyrogram](docs.pyrogram.org)

🔰Language : [Python](www.python.org)

🧑‍💻Developer : @ImRishmika

🆘Support : [SD Bᴏᴛs Cʜᴀᴛ ⚡️](https://t.me/+RiZlGUJfgBM3NjQ1)
    """

    SUPPORTED_MEDIA_TYPES = """
✅ **SUPPORTED MEDIA TYPES** ✅

1) Image
2) Sticker
3) Gifs or Animation
4) Video
5) Video Note
6) Document (Video/Photo/Gif)

Note : Telegraph has a size limit of 5 MB.
    """

    # Home Button
    home_buttons = [
        [
            InlineKeyboardButton("⚡️SD Bᴏᴛs⚡️", url="https://t.me/SDBOTs_inifinity"),
        ],
        [
            InlineKeyboardButton("⚡️SD Bᴏᴛs⚡️", url="https://t.me/SDBOTs_inifinity")
        ],
        [InlineKeyboardButton("🧩 Supported Media Types 🧩", callback_data="supported_media_types")],
        [InlineKeyboardButton("🔐 Close 🔐", callback_data="close")],
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("⚡️SD Bᴏᴛs⚡️", url="https://t.me/SDBOTs_inifinity")
        ],
        [
            InlineKeyboardButton("🔥 Emo Bots 🔥" url="t.me/EmoBotDevolopers") 
        ],
        [InlineKeyboardButton("🧩 Supported Media Types 🧩", callback_data="supported_media_types")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("📥 About 📥", callback_data="about")
        ],
        [InlineKeyboardButton("Close 🔐", callback_data="close")]
    ]

    # Supported Media Buttons
    supported_media_buttons = [
        [InlineKeyboardButton("⚡️SD Bᴏᴛs⚡️", url="https://t.me/SDBOTs_inifinity")],
        [InlineKeyboardButton("</> ємσ вσт ∂єνσℓσρєʀѕ", url="https://t.me/EmoBotDevolopers")],
        [InlineKeyboardButton("Close 🔐", callback_data="close")],
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
    ]
