import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_ID = int(os.environ.get("API_ID", "3938951"))
    API_HASH = os.environ.get("API_HASH", "6561686ba611b2d46efedef7debd6fa5")
    LOG_ID = int(os.environ.get("LOG_ID", "-1001550013674"))
    SESSION_STRING = os.environ.get("SESSION_STRING", "BQA2JaRNbwdqRYuWwNdvnrv7jL9vu840jC7cULPlGEtAu_aES9-IKBRvyPh-ek5xU900tTo-pLyqt0-f0usxlLst9gTF5G_3kgx3-AbK4yVO__6C0MlWP2ATcCDPsFR7ZFiicV2-4Bp8ZzwA38UqzBPYbRQkuXY6XtGuMoSnQY_5kv5qck60qQELLcqXUZaFiRN2aIOxirnfmEvwElLu6GtRnUWYbTBCT7sfUyU3C7wPoAs5h1K1cNJH9yT1OuDvsfbZqAblKPdiNI4SfAp9JW_RTPZf9-bqUoL98T46kSlK04Fl1gfbp2BcLiXGQRpGHKUQHhhfzq79fVidGV_lKF20SM-CxQA")

class Database:
    VIDEO_CALL = {}
    RADIO_CALL = {}
    FFMPEG_PROCESSES = {}
