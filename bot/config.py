
import os



class Config(object):
    SESSION_NAME = "AHCompressorBot"
    APP_ID = "3845818"
    API_HASH = "95937bcf6bc0938f263fc7ad96959c6d"
    LOG_CHANNEL = -1001763491746
    UPDATES_CHANNEL = None # Without `@` LOL
    # array to store the channel ID who are authorized to use the bot
    # dont u fucking remove this id 😤
    TG_BOT_TOKEN = "5302929820:AAEsKXElRmQ1vcwYwRYmQIYstnKPzLQF0-w"
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "/downloads"
    # Telegram maximum file upload size
    BOT_USERNAME = "gear100bot"
    MAX_FILE_SIZE = 2097152000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 2097152000
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = "https://placehold.it/90x90"
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = None
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # add config vars for the display progress
    FINISHED_PROGRESS_STR = "▣"
    UN_FINISHED_PROGRESS_STR = "▢"
    LOG_FILE_ZZGEVC = "Log.txt"
      # because, https://t.me/c/1494623325/5603
    SHOULD_USE_BUTTONS = False
