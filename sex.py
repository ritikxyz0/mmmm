=========================================================

CLONIFY USERBOT - CLEAN VERSION (NO EMOJI, NO VC)

PRIVATE USE ONLY

=========================================================

pip install -U pyrogram tgcrypto yt-dlp requests beautifulsoup4

import os import random import requests import yt_dlp from bs4 import BeautifulSoup from pyrogram import Client, filters from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

---------------- CONFIG ----------------

API_ID = 39496551            # apna API_ID daalo API_HASH = "36495414098630fed4555734bcc9748b"   # apna API_HASH daalo SESSION = "clonify" DOWNLOAD_DIR = "downloads"

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

---------------- CLIENT ----------------

app = Client( SESSION, api_id=API_ID, api_hash=API_HASH )

---------------- KEYBOARD ----------------

keyboard = InlineKeyboardMarkup([ [InlineKeyboardButton("CLOSE", callback_data="close")] ])

---------------- HELPERS ----------------

def search_xnxx(title: str): try: url = f"https://www.xnxx.com/search/{title.replace(' ', '%20')}" r = requests.get(url, timeout=20) soup = BeautifulSoup(r.text, "html.parser") cards = soup.find_all("div", class_="thumb-block") if not cards: return None card = random.choice(cards) a = card.find("a", href=True) if not a: return None link = a['href'] if not link.startswith("http"): link = "https://www.xnxx.com" + link return link except Exception as e: print(e) return None

def download_video(link: str): ydl_opts = { "format": "best", "outtmpl": f"{DOWNLOAD_DIR}/%(id)s.%(ext)s", "quiet": True, "nocheckcertificate": True, } with yt_dlp.YoutubeDL(ydl_opts) as ydl: info = ydl.extract_info(link, download=True) return f"{DOWNLOAD_DIR}/{info['id']}.{info['ext']}"

---------------- CALLBACK ----------------

@app.on_callback_query(filters.regex("^close$")) async def close_btn(_, q): await q.message.delete()

---------------- COMMANDS ----------------

@app.on_message(filters.command("porn") & filters.me) async def porn_cmd(_, msg): if len(msg.command) < 2: return await msg.reply("Usage: /porn keyword")

title = " ".join(msg.command[1:])
link = search_xnxx(title)

if not link:
    return await msg.reply("No video found")

video = download_video(link)

await msg.reply_video(
    video,
    caption=f"{title}",
    reply_markup=keyboard
)

@app.on_message(filters.command("xnxx") & filters.me) async def xnxx_cmd(_, msg): if len(msg.command) < 2: return await msg.reply("Usage: /xnxx keyword")

title = " ".join(msg.command[1:])
link = search_xnxx(title)

if not link:
    return await msg.reply("No result found")

video = download_video(link)
await msg.reply_video(video, caption=title)

---------------- START ----------------

if name == "main": print("Userbot started") app.run()
