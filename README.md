<h1 align="center">
  Winter Release
</h1>

## 🔧 Features
- Extract content from both public and private channels/groups.
- Rename and forward content to other channels or users.
- Custom captions and thumbnails.
- Auto-remove default video thumbnails.
- Delete or replace words in filenames and captions.
- Auto-pin messages if enabled.
- download yt/insta/Twitter/fb ect normal ytdlp supported sites that supports best format
- Login via phone number.
- **Supports 4GB file uploads**: The bot can handle large file uploads, up to 4GB in size.
- **Enhanced Timer**: Distinct timers for free and paid users to limit usage and improve service.
- **Improved Looping**: Optimized looping for processing multiple files or links, reducing delays and enhancing performance.
- **Premium Access**: Premium users enjoy faster processing speeds and priority queue management.
- ads setup shorlink ads token system

## ⚡ Commands

- **`start`**: 🚀 Start the bot.
- **`batch`**: 🫠 Extract in bulk.
- **`login`**: 🔑 Get into the bot.
- **`logout`**: 🚪 Get out of the bot.
- **`token`**: 🎲 Get 3 hours of free access.
- **`adl`**: 👻 Download audio from 30+ sites.
- **`dl`**: 💀 Download videos from 30+ sites.
- **`transfer`**: 💘 Gift premium to others.
- **`myplan`**: ⌛ Get your plan details.
- **`add`**: ➕ Add user to premium.
- **`rem`**: ➖ Remove user from premium.
- **`session`**: 🧵 Generate Pyrogramv2 session.
- **`settings`**: ⚙️ Personalize settings.
- **`stats`**: 📊 Get stats of the bot.
- **`plan`**: 🗓️ Check our premium plans.
- **`terms`**: 🥺 Terms and conditions.
- **`speedtest`**: 🚅 Check the server speed.
- **`get`**: 🗄️ Get all user IDs.
- **`lock`**: 🔒 Protect channel from extraction.
- **`gcast`**: ⚡ Broadcast message to bot users.
- **`help`**: ❓ Help if you're new.
- **`cancel`**: 🚫 Cancel batch process.


## ⚙️ Required Variables

<details>
<summary><b>Click to view required variables</b></summary>

To run the bot, you'll need to configure a few sensitive variables. Here's how to set them up securely:

- **`API_ID`**: Your API ID from [telegram.org](https://my.telegram.org/auth).
- **`API_HASH`**: Your API Hash from [telegram.org](https://my.telegram.org/auth).
- **`BOT_TOKEN`**: Get your bot token from [@BotFather](https://t.me/botfather).
- **`OWNER_ID`**: Use [@missrose_bot](https://t.me/missrose_bot) to get your user ID by sending `/info`.
- **`CHANNEL_ID`**: The ID of the channel for forced subscription.
- **`LOG_GROUP`**: A group or channel where the bot logs messages. Forward a message to [@userinfobot](https://t.me/userinfobot) to get your channel/group ID.
- **`MONGO_DB`**: A MongoDB URL for storing session data (recommended for security).
  
### Additional Configuration Options:
- **`STRING`**: (Optional) Add your **premium account session string** here to allow 4GB file uploads. This is **optional** and can be left empty if not used.
- **`FREEMIUM_LIMIT`**: Default is `0`. Set this to any value you want to allow free users to extract content. If set to `0`, free users will not have access to any extraction features.
- **`PREMIUM_LIMIT`**: Default is `500`. This is the batch limit for premium users. You can customize this to allow premium users to process more links/files in one batch.
- **`YT_COOKIES`**: Yt cookies for downloading yt videos 
- **`INSTA_COOKIES`**: If you want to enable instagram downloading fill cookiesn

** How to get cookies ??** : use mozila firfox if on android or use chrome on desktop and download extension get this cookie or any Netscape Cookies (HTTP Cookies) extractor and use that 

### Monetization (Optional):
- **`WEBSITE_URL`**: (Optional) This is the domain for your monetization short link service. Provide the shortener's domain name, for example: `upshrink.com`. Do **not** include `www` or `https://`. The default link shortener is already set.
- **`AD_API`**: (Optional) The API key from your link shortener service (e.g., **Upshrink**, **AdFly**, etc.) to monetize links. Enter the API provided by your shortener.

> **Important:** Always keep your credentials secure! Never hard-code them in the repository. Use environment variables or a `.env` file.

</details>

---