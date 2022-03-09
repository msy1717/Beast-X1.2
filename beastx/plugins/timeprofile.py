import asyncio , json , datetime , random , os , pytz , time
from PIL import Image, ImageDraw, ImageFont

ZONE = pytz.timezone( os.environ.get("TIMEZONE", "Asia/Kolkata") )
TIME = datetime.datetime.now(ZONE).strftime('%I:%M %p')

async def drawProfile():
    img = Image.open("resources/image.jpg")
    font = ImageFont.truetype("resources/ds-digit.ttf", 360)
    to_edit = ImageDraw.Draw( img )
    to_edit.text((690, 550), TIME , (0, 255, 255), font = font )
    img.save("resources/new.jpg")
    return "resources/new.jpg"   #return the saved path .
  
