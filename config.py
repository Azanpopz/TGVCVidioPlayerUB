import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_ID = int(os.environ.get("API_ID", "1778836"))
    API_HASH = os.environ.get("API_HASH", "7bcf61fcd32b8652cd5876b02dcf57ae")
    LOG_ID = int(os.environ.get("LOG_ID", -1001565141207"))
    SESSION_STRING = os.environ.get("SESSION_STRING", "BQA8Omi7tl41FSWCOa5PFzSQrZqdypRTx5mq7oLULKDYplnPNrUeL5nC-luRC4A1V5BRVDeEKHOwjCJpNrvvstOlRV2gXPttxVyCknunSkxhQHK_aUQgM_prv3enFlBj1yfdjzyypGCOhaRKpQuM5y3RKmMlQ-w2aAL9noUyjDA1BuVY5YC2ZcxAWcz3lALmnC09P4BA0ANPHuArI8Bd6mZeP4AZb0mRhynnejmWL9pM3iW2pe2KRjpt54W-Q1vXZTGNVf1uzx7Z0iJNSPFa3YVOkgwoeUYgLE3VKH2imU3Fi4wtURMGVmWZAu3udl_xvA-S1cJn23ha7XJ2mCyfKfA0TQHpigA")

class Database:
    VIDEO_CALL = {}
    RADIO_CALL = {}
    FFMPEG_PROCESSES = {}
