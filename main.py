import logging
from pyrogram import Client, idle
import Config
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid


logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


API_ID = "14055090"
API_HASH = "a46f7b439d0afa45b7a69fc450f754e9"
BOT_TOKEN = "5977358711:AAErw1WEA-jbPsV6M7goEWNCY8youJTNfg8"
DATABASE_URL = "mongodb+srv://rishbro:rishbro@cluster0.eiqoy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
MUST_JOIN = "EmoBotDevolopers"
OWNER_ID = "5171347305"

app = Client(
    "Telegraph-Bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="Bot"),
)


# Run Bot
if __name__ == "__main__":
    try:
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    uname = app.get_me().username
    print(f"@{uname} Started Successfully!")
    idle()
    app.stop()
    print("Bot stopped.")
