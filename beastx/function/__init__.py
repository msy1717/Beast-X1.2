import asyncio , json , datetime , random , os , pytz , time
from PIL import Image, ImageDraw, ImageFont

ZONE = pytz.timezone( os.environ.get("TIMEZONE", "Asia/Kolkata") )
TIME = datetime.datetime.now(ZONE).strftime('%I:%M %p')
