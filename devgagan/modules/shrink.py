
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random
import requests
import string
import aiohttp
from devgagan import app
from devgagan.core.func import *
from datetime import datetime, timedelta
from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_DB, WEBSITE_URL, AD_API, LOG_GROUP  
 
 
tclient = AsyncIOMotorClient(MONGO_DB)
tdb = tclient["telegram_bot"]
token = tdb["tokens"]
 
 
async def create_ttl_index():
    await token.create_index("expires_at", expireAfterSeconds=0)
 
 
 
Param = {}
 
 
async def generate_random_param(length=8):
    """Generate a random parameter."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
 
 
async def get_shortened_url(deep_link):
    api_url = f"https://{WEBSITE_URL}/api?api={AD_API}&url={deep_link}"
 
     
    async with aiohttp.ClientSession() as session:
        async with session.get(api_url) as response:
            if response.status == 200:
                data = await response.json()   
                if data.get("status") == "success":
                    return data.get("shortenedUrl")
    return None
 
 
async def is_user_verified(user_id):
    """Check if a user has an active session."""
    session = await token.find_one({"user_id": user_id})
    return session is not None
 
 
@app.on_message(filters.command("start"))
async def token_handler(client, message):
    """Handle the /token command."""
    join = await subscribe(client, message)
    if join == 1:
        return
    chat_id = "save_restricted_content_bots"
    msg = await app.get_messages(chat_id, 796)
    user_id = message.chat.id
    if len(message.command) <= 1:
        join_button = InlineKeyboardButton("Join Channel", url="https://t.me/+GK7fjpwYseo1Yzg0")
        premium = InlineKeyboardButton("Get Premium", url="https://t.me/dame2907")   
        keyboard = InlineKeyboardMarkup([
            [join_button],   
            [premium]    
        ])
         
        await message.reply_photo(photo="https://graph.org/file/b0c891545d4adb77a4f95.jpg",
            caption=(
                "**Hey There 👋 Welcome to Restricted Content Saver Bot**\n\n"
                "✳️ Save Restricted Posts from Public/Private Channels/Groups.\n\n"
                "✳️ Download Media From YT, INSTA & Other Social Platforms\n\n"
                "✳️ Simply Send The Post Link Of A Public Channel.\n\n"
                "✳️ For Private Channels, Login Using /login & Send Post Link.\n\n"
                "✳️ Send /help To Know More.\n\n"
            ),
            reply_markup=keyboard
        )
        return  
 
    param = message.command[1] if len(message.command) > 1 else None
    freecheck = await chk_user(message, user_id)
    if freecheck != 1:
        await message.reply("You are a premium user no need of token 😉")
        return
 
     
    if param:
        if user_id in Param and Param[user_id] == param:
             
            await token.insert_one({
                "user_id": user_id,
                "param": param,
                "created_at": datetime.utcnow(),
                "expires_at": datetime.utcnow() + timedelta(hours=3),
            })
            del Param[user_id]   
            await message.reply("✅ You have been verified successfully! Enjoy your session for next 3 hours.")
            return
        else:
            await message.reply("❌ Invalid or expired verification link. Please generate a new token.")
            return
 
@app.on_message(filters.command("token"))
async def smart_handler(client, message):
    user_id = message.chat.id
     
    freecheck = await chk_user(message, user_id)
    if freecheck != 1:
        await message.reply("You are a premium user no need of token 😉")
        return
    if await is_user_verified(user_id):
        await message.reply("✅ Your free session is already active enjoy!")
    else:
         
        param = await generate_random_param()
        Param[user_id] = param   
 
         
        deep_link = f"https://t.me/{client.me.username}?start={param}"
 
         
        shortened_url = await get_shortened_url(deep_link)
        if not shortened_url:
            await message.reply("❌ Failed to generate the token link. Please try again.")
            return
 
         
        button = InlineKeyboardMarkup(
            [[InlineKeyboardButton("Verify the token now...", url=shortened_url)]]
        )
        await message.reply("Click the button below to verify your free access token: \n\n> What will you get ? \n1. No time bound upto 3 hours \n2. Batch command limit will be FreeLimit + 20 \n3. All functions unlocked", reply_markup=button)
 
