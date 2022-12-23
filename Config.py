import os

ENVIRONMENT = bool(os.environ.get('ENVIRONMENT', False))

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    try:
        OWNER_ID = int(os.environ.get('OWNER_ID', 0))
    except ValueError:
        raise Exception("Your OWNER_ID is not a valid integer.")
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = "14104754"
    API_HASH = "fc8f5ab24f0ceaa02998220981dc91b4"
    BOT_TOKEN = "5674301319:AAGGFd3RxXNK1gfBm40uIXz5CZJApBYibcw"
    DATABASE_URL = "mongodb+srv://rishbro:rishbro@cluster0.eiqoy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    MUST_JOIN = "SDBOTS_Inifinity"
    OWNER_ID = "5171347305"
