import os
from pyrogram.client import Client

app = Client(
    "AniPlay",
    api_id= int(os.environ.get("APP_ID", "4682685")),
    api_hash= os.environ.get("API_HASH", "3eba5d471162181b8a3f7f5c0a23c307"),
    bot_token= os.environ.get("TOKEN", "6017558004:AAGKT-Y0moOFsaisHhBoTEZYgyPgcL3s7No")
)
