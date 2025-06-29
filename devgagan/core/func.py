import os
import re
import math
import time
import asyncio
import cv2
from datetime import datetime as dt
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait, InviteHashInvalid, InviteHashExpired, UserAlreadyParticipant, UserNotParticipant

# ====== CONFIGURATION ======
API_ID = 24363932
API_HASH = "d84176e864496c3cd2542c1a0de42c4a"
BOT_TOKEN = "7920155198:AAEWhAaW3sNMfIZzILwjCYRMIifjRK3yqVQ"
CHANNEL_ID = -1002600575573
OWNER_ID = [123456789]  # Replace with your Telegram user id(s) as a list

# ====== MOCK PREMIUM USERS (replace with your DB logic) ======
async def premium_users():
    return set(OWNER_ID)  # For demo, only owner is premium

# ====== UTILITY FUNCTIONS ======

async def chk_user(message, user_id):
    user = await premium_users()
    if user_id in user or user_id in OWNER_ID:
        return 0
    else:
        return 1

async def gen_link(app, chat_id):
    link = await app.export_chat_invite_link(chat_id)
    return link

async def subscribe(app, message):
    update_channel = CHANNEL_ID
    url = await gen_link(app, update_channel)
    if update_channel:
        try:
            user = await app.get_chat_member(update_channel, message.from_user.id)
            if user.status == "kicked":
                await message.reply_text("You are Banned. Contact -- @dame2907")
                return 1
        except UserNotParticipant:
            caption = f"Join our channel to use the bot"
            await message.reply_photo(
                photo="https://i.postimg.cc/wMqkMBwh/Join-Banner.png",
                caption=caption,
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Join Now...", url=f"{url}")]])
            )
            return 1
        except Exception:
            await message.reply_text("Something Went Wrong. Contact @dame2907")
            return 1

async def get_seconds(time_string):
    def extract_value_and_unit(ts):
        value = ""
        unit = ""
        index = 0
        while index < len(ts) and ts[index].isdigit():
            value += ts[index]
            index += 1
        unit = ts[index:].lstrip()
        if value:
            value = int(value)
        return value, unit

    value, unit = extract_value_and_unit(time_string)
    if unit == 's':
        return value
    elif unit == 'min':
        return value * 60
    elif unit == 'hour':
        return value * 3600
    elif unit == 'day':
        return value * 86400
    elif unit == 'month':
        return value * 86400 * 30
    elif unit == 'year':
        return value * 86400 * 365
    else:
        return 0

def humanbytes(size):
    if not size:
        return "0 B"
    power = 2**10
    n = 0
    Dic_powerN = {0: '', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size >= power and n < 4:
        size /= power
        n += 1
    return f"{size:.2f} {Dic_powerN[n]}B"

def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "d, ") if days else "") + \
        ((str(hours) + "h, ") if hours else "") + \
        ((str(minutes) + "m, ") if minutes else "") + \
        ((str(seconds) + "s, ") if seconds else "") + \
        ((str(milliseconds) + "ms, ") if milliseconds else "")
    return tmp[:-2] 

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60      
    return "%d:%02d:%02d" % (hour, minutes, seconds)

async def userbot_join(userbot, invite_link):
    try:
        await userbot.join_chat(invite_link)
        return "Successfully joined the Channel"
    except UserAlreadyParticipant:
        return "User is already a participant."
    except (InviteHashInvalid, InviteHashExpired):
        return "Could not join. Maybe your link is expired or Invalid."
    except FloodWait:
        return "Too many requests, try again later."
    except Exception as e:
        print(e)
        return "Could not join, try joining manually."

def get_link(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)   
    try:
        link = [x[0] for x in url][0]
        if link:
            return link
        else:
            return False
    except Exception:
        return False

def video_metadata(file):
    default_values = {'width': 1, 'height': 1, 'duration': 1}
    try:
        vcap = cv2.VideoCapture(file)
        if not vcap.isOpened():
            return default_values  
        width = round(vcap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = round(vcap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = vcap.get(cv2.CAP_PROP_FPS)
        frame_count = vcap.get(cv2.CAP_PROP_FRAME_COUNT)
        if fps <= 0:
            return default_values  
        duration = round(frame_count / fps)
        if duration <= 0:
            return default_values  
        vcap.release()
        return {'width': width, 'height': height, 'duration': duration}
    except Exception as e:
        print(f"Error in video_metadata: {e}")
        return default_values

def hhmmss(seconds):
    return time.strftime('%H:%M:%S', time.gmtime(seconds))

async def screenshot(video, duration, sender):
    if os.path.exists(f'{sender}.jpg'):
        return f'{sender}.jpg'
    time_stamp = hhmmss(int(duration)/2)
    out = dt.now().isoformat("_", "seconds") + ".jpg"
    cmd = [
        "ffmpeg",
        "-ss", f"{time_stamp}", 
        "-i", f"{video}",
        "-frames:v", "1", 
        f"{out}",
        "-y"
    ]
    process = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    if os.path.isfile(out):
        return out
    else:
        return None  

# ====== ADAM PROGRESS BAR ======
def make_progress_bar(current, total, length=18):
    percent = current / total if total else 0
    filled_length = int(length * percent)
    bar = '█' * filled_length + '░' * (length - filled_length)
    return bar

def format_progress(
    action, 
    current, 
    total, 
    speed=None, 
    eta=None, 
    filename=None
):
    percent = (current / total * 100) if total else 0
    current_h = humanbytes(current)
    total_h = humanbytes(total)
    speed_str = f"⚡ {humanbytes(speed)}/s" if speed else ""
    eta_str = f"⏳ {eta}" if eta else ""
    emoji = "🚀" if action == "upload" else "📥"
    action_text = "UPLOADING" if action == "upload" else "DOWNLOADING"

    # Filename formatting
    fname = ""
    if filename:
        truncated = (filename[:24] + '...') if len(filename) > 27 else filename
        fname = f"║  🔹 {truncated.ljust(27)}║\n"

    # Speed/ETA line
    speed_eta = ""
    if speed_str or eta_str:
        speed_eta = f"║  {speed_str}{' | ' if speed_str and eta_str else ''}{eta_str.ljust(22)}║\n"

    msg = (
        f"╔{'═'*34}╗\n"
        f"║   {emoji}  ADAM BOT  {emoji}   ║\n"
        f"╠{'═'*34}╣\n"
        f"{fname}"
        f"║                                ║\n"
        f"║   {make_progress_bar(current, total)}   ║\n"
        f"║        {percent:6.2f}%              ║\n"
        f"║                                ║\n"
        f"║   ↕ {current_h} / {total_h}           ║\n"
        f"{speed_eta}"
        f"╚{'═'*34}╝\n"
        f"\n✨ Powered by ADAM ✨"
    )
    return msg

# ====== BOT SETUP ======
app = Client("adam_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start") & filters.private)
async def start_cmd(client, message):
    await message.reply_text(
        "👋 Welcome to **ADAM**!\n\n"
        "Use /upload to see the progress bar demo.",
        parse_mode="markdown"
    )

@app.on_message(filters.command("upload") & filters.private)
async def upload_demo(client, message):
    # Simulate a file upload with progress bar
    total = 50 * 1024 * 1024  # 50 MB
    current = 0
    chunk = 2 * 1024 * 1024   # 2 MB per step
    speed = 1 * 1024 * 1024   # 1 MB/s
    filename = "demo_video.mp4"
    progress_msg = await message.reply_text(format_progress("upload", 0, total, speed, "00:00", filename))
    start_time = time.time()
    while current < total:
        await asyncio.sleep(2)  # simulate upload delay
        current += chunk
        if current > total:
            current = total
        elapsed = time.time() - start_time
        eta = convert(int((total - current) / speed)) if speed else "?"
        await progress_msg.edit_text(format_progress("upload", current, total, speed, eta, filename))
    await progress_msg.edit_text("✅ Upload complete!\n\n✨ Powered by ADAM ✨")

# ====== RUN BOT ======
if __name__ == "__main__":
    print("ADAM bot is running...")
    app.run()
