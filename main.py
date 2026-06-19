import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

import sys

import subprocess

import asyncio



# --- BẮT ĐẦU ĐOẠN CODE ĐÁNH LỪA RENDER ---
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is alive and running well!")

def run_dummy_server():
    # Lấy port từ Render cấp, nếu không có thì dùng 10000
    port = int(os.environ.get("PORT", 10000))
    server_address = ('0.0.0.0', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Bật server ảo để pass qua Render health check trên port {port}...")
    httpd.serve_forever()

# Chạy server ảo ở một luồng (thread) chạy ngầm song song với bot
threading.Thread(target=run_dummy_server, daemon=True).start()
# --- KẾT THÚC ĐOẠN CODE ĐÁNH LỪA RENDER ---

def install_package(package_name, import_name=None):

    if import_name is None:

        import_name = package_name

    try:

        __import__(import_name)

    except ImportError:

        print(f"Đang cài đặt {package_name}...")

        try:

            subprocess.check_call([sys.executable, "-m", "pip", "install", package_name, "--quiet"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            print(f"✅ Đã cài đặt {package_name}")

        except:

            print(f"❌ Lỗi cài đặt {package_name}")



install_package("requests")

install_package("aiohttp")

install_package("pyTelegramBotAPI", "telebot")

install_package("urllib3")

install_package("beautifulsoup4", "bs4")

install_package("lxml")
install_package("pyotp")

install_package("playwright", "playwright")



import requests

import aiohttp

from requests.adapters import HTTPAdapter

from urllib3.util.retry import Retry

import json

import time

import threading

import re

import html as html_module

import urllib3

import signal

import atexit

import random

import urllib.parse

from datetime import datetime, timedelta

from concurrent.futures import ThreadPoolExecutor, as_completed

from decimal import Decimal, ROUND_HALF_UP

import telebot

from telebot import types

from bs4 import BeautifulSoup

from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps

import emoji

import colorsys

ANHDIE = ''

ANHLIVE = ''

LOCAL_ANH = "mark.jpg"          # không dùng nữa (giữ lại để tránh lỗi fallback)

LOCAL_ANH_LIVE = "mark2.jpg"   # không dùng nữa (giữ lại để tránh lỗi fallback)

LOCAL_ANH1 = "mark1.jpg"       # Mark cười - lúc "ĐÃ BỊ KHÓA" (add UID lần đầu, status DIE)

LOCAL_ANH3 = "mark3.jpg"       # Mark lè lưỡi - lúc "ĐÃ DIE" (theo dõi LIVE→DIE)

def create_session_with_retry():

    session = requests.Session()

    retry = Retry(

        total=1,

        backoff_factor=0.1,

        status_forcelist=[500, 502, 503, 504],

        allowed_methods=["GET", "POST"]

    )

    adapter = HTTPAdapter(

        max_retries=retry,

        pool_connections=400,

        pool_maxsize=400

    )

    session.mount("http://", adapter)

    session.mount("https://", adapter)

    return session



fb_check_session = create_session_with_retry()

# ===== FAST CHECK CONFIG =====
FAST_API_TIMEOUT = 5
FAST_AVATAR_TIMEOUT = 4
FAST_CACHE_TTL = 20

info_fast_session = create_session_with_retry()
_fast_info_cache = {}

def _fast_cache_get(key):
    try:
        item = _fast_info_cache.get(str(key))
        if not item:
            return None
        if time.time() - item.get("ts", 0) > FAST_CACHE_TTL:
            _fast_info_cache.pop(str(key), None)
            return None
        return item.get("data")
    except Exception:
        return None

def _fast_cache_set(key, data):
    try:
        if len(_fast_info_cache) > 1000:  # Giới hạn cache tránh memory leak
            oldest = min(_fast_info_cache, key=lambda k: _fast_info_cache[k].get("ts", 0))
            _fast_info_cache.pop(oldest, None)
        _fast_info_cache[str(key)] = {"ts": time.time(), "data": data}
    except Exception:
        pass

TOKEN = "8972733821:AAGBSn1Jyy9HdLRIaO9Lw9QDAIUv14o9erw"

BOSS_ID = 7203678858

api_key = os.getenv("DEEPSEEK_API_KEY")
if not api_key:
    print("LỖI: Chưa cấu hình DEEPSEEK_API_KEY")
DEEPSEEK_API_KEY = api_key

# ── Giá VIP Bot Con ──────────────────────────────────────────
BOTCON_VIP_PLANS = {
    "1":  {"months": 1,  "price": 50000,  "label": "1 tháng",  "discount": 0},
    "3":  {"months": 3,  "price": 126000, "label": "3 tháng",  "discount": 10},
    "6":  {"months": 6,  "price": 221000, "label": "6 tháng",  "discount": 15},
    "12": {"months": 12, "price": 400000, "label": "12 tháng", "discount": 20},
}



ADMIN_IDS = {BOSS_ID}



bot = telebot.TeleBot(TOKEN, parse_mode=None, threaded=True, num_threads=20)

telebot.apihelper.RETRY_ON_ERROR = True

telebot.apihelper.RETRY_TIMEOUT = 2

telebot.apihelper.MAX_RETRIES = 3



FILES = {

    "users": "data_users.json",

    "tracking": "data_tracking.json",

    "tracking_tiktok": "data_tracking_tiktok.json",

    "history": "data_history.json",

    "admins": "admin.txt",

    "all_users": "all_users.json",

    "revenue": "data_revenue.json",

    "config": "data_config.json",

    "uid_memory": "uid_memory.json",

    "prompt": "prompt.txt",

    "prompt_admin": "prompt_admin.txt",

    "prompt_user_twoface": "prompt_user_twoface.txt",

    "prompt_ai_unrestricted": "prompt_ai_unrestricted.txt",

    "prompt_feedback_agent": "prompt_feedback_agent.txt",

    "thongbao_prompt": "thongbao_prompt.txt",

    "prompt_code_logic": "prompt_code_logic.txt",

    "cookie": "cookie.txt",

    "codes": "codes.json",

    "ytb_channels": "youtube_channels.json",

    "sub_bots": "data_sub_bots.json"

}



active_chats = {}   # sẽ được gán lại bởi SmartStateDict ở phần module bot con

support_queue = {}

FB_COOKIE = "" 

temp_user_state = {}  # sẽ được gán lại bởi SmartStateDict ở phần module bot con

# ==================== CAU HINH YOUTUBE ====================
YOUTUBE_API_KEY = "AIzaSyDWLEYtA6x9dUeWxkpvN3kfpZ4Eu4IAjJ4"  # Thay API key cua ban
YTB_CHECK_INTERVAL = 20
YTB_RETRY_COUNT = 3
YTB_RETRY_DELAY = 5
YTB_CONFIRM_DIE_COUNT = 5

def load_ytb_data():
    return load_json(FILES["ytb_channels"])

def save_ytb_data(d):
    save_json(FILES["ytb_channels"], d)

def ytb_extract_identifier(url):
    import re as _r
    pats = [r'youtube\.com/@([^/?&#]+)', r'youtube\.com/c/([^/?&#]+)',
            r'youtube\.com/channel/([^/?&#]+)', r'youtube\.com/user/([^/?&#]+)']
    for p in pats:
        m = _r.search(p, url)
        if m: return m.group(1)
    return None

def ytb_get_channel_info(identifier):
    try:
        if identifier.startswith("UC"):
            u = f"https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={identifier}&key={YOUTUBE_API_KEY}"
        else:
            u = f"https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&forHandle={identifier}&key={YOUTUBE_API_KEY}"
        r = requests.get(u, timeout=10).json()
        if "items" in r and r["items"]:
            it = r["items"][0]
            th = it["snippet"]["thumbnails"]
            av = th.get("high", {}).get("url") or th.get("medium", {}).get("url") or th.get("default", {}).get("url")
            st = it.get("statistics", {})
            return {"channel_id": it["id"], "title": it["snippet"]["title"],
                    "subscriber_count": st.get("subscriberCount", "N/A"),
                    "video_count": st.get("videoCount", "N/A"),
                    "view_count": st.get("viewCount", "N/A"),
                    "avatar": av, "custom_url": it["snippet"].get("customUrl", "")}
        return None
    except Exception as e:
        print(f"[YTB] Loi get_channel_info: {e}")
        return None

def ytb_check_channel_alive(channel_id):
    for attempt in range(YTB_RETRY_COUNT):
        try:
            u = f"https://www.googleapis.com/youtube/v3/channels?part=snippet&id={channel_id}&key={YOUTUBE_API_KEY}"
            r = requests.get(u, timeout=10).json()
            if "error" in r:
                if r["error"].get("code") == 403:
                    time.sleep(60)
                    continue
                return False
            return bool(r.get("items"))
        except Exception as e:
            print(f"[YTB] Loi check lan {attempt+1}: {e}")
            if attempt < YTB_RETRY_COUNT - 1:
                time.sleep(YTB_RETRY_DELAY)
    return False

def _ytb_send_notify(chat_id_str, ch, url, channel_id, alive):
    status_icon = "\U0001F7E2" if alive else "\U0001F534"
    action = "SONG LAI" if alive else "DA DIE"
    time_key = "Thoi gian" if alive else "Die luc"
    time_val = ch.get("last_check", "N/A") if alive else ch.get("die_time", "N/A")
    msg = (f"{status_icon} <b>KENH YTB {action}!</b>\n\n"
           f"\U0001F4FA Ten: {ch['title']}\n"
           f"\U0001F517 Link: {url}\n"
           f"\U0001F194 ID: {channel_id}\n"
           f"\u23F0 {time_key}: {time_val}")
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.row(
        types.InlineKeyboardButton("\u2705 Done", callback_data=f"ytb_done_{channel_id}"),
        types.InlineKeyboardButton("\u274C Huy keo", callback_data=f"ytb_del_{channel_id}")
    )
    markup.add(types.InlineKeyboardButton("\U0001F514 Tiep Tuc Theo Doi", callback_data=f"ytb_keep_{channel_id}"))
    try:
        avatar = ch.get("avatar")
        cid = int(chat_id_str)
        if avatar:
            avatar_bytes, _ = _download_image_bytes(avatar, preferred_keys=['avatar', 'thumbnail', 'url'])
            if avatar_bytes:
                from io import BytesIO
                bot.send_photo(cid, BytesIO(avatar_bytes), caption=msg, parse_mode="HTML", reply_markup=markup)
                return
        bot.send_message(cid, msg, parse_mode="HTML", reply_markup=markup)
    except Exception as ex:
        print(f"[YTB] Loi gui thong bao: {ex}")

def ytb_monitoring_thread():
    print("[YTB] Bat dau giam sat kenh YouTube...")
    while True:
        try:
            data = load_ytb_data()
            if not data:
                time.sleep(YTB_CHECK_INTERVAL)
                continue
            changed = False
            for chat_id_str, channels in data.items():
                for url, ch in list(channels.items()):
                    channel_id = ch.get("channel_id")
                    if not channel_id: continue
                    current_status = ch.get("status", "live")
                    fail_count = ch.get("fail_count", 0)
                    is_alive = ytb_check_channel_alive(channel_id)
                    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    if is_alive:
                        if current_status == "die":
                            ch["status"] = "live"; ch["fail_count"] = 0; ch["last_check"] = now
                            changed = True
                            _ytb_send_notify(chat_id_str, ch, url, channel_id, True)
                        else:
                            ch["fail_count"] = 0; ch["last_check"] = now; changed = True
                    else:
                        fail_count += 1; ch["fail_count"] = fail_count; ch["last_check"] = now; changed = True
                        if fail_count == YTB_CONFIRM_DIE_COUNT and current_status == "live":
                            ch["status"] = "die"; ch["die_time"] = now
                            _ytb_send_notify(chat_id_str, ch, url, channel_id, False)
            if changed:
                save_ytb_data(data)
        except Exception as e:
            print(f"[YTB] Loi monitoring: {e}")
        time.sleep(YTB_CHECK_INTERVAL)

# ==================== KET THUC YTB ====================


# Link ảnh DIE mặc định

ANHDIE = "https://ibb.co/1fzJjDTz"

# Link ảnh LIVE (Mark sống) mặc định - Admin dùng /setanhlive để thay đổi

ANHLIVE = "https://ibb.co/1fzJjDTz"



# Thư mục cache cho ảnh tạm (sử dụng thư mục hiện tại thay vì /tmp cho Android/Termux)

CACHE_DIR = os.path.join(os.getcwd(), "cache_images")

try:

    if not os.path.exists(CACHE_DIR):

        os.makedirs(CACHE_DIR)

except Exception as e:

    print(f"⚠️ Không tạo được cache dir: {e}")

    CACHE_DIR = "."  # Fallback về thư mục hiện tại

# ==================== BACKGROUND DIR CHO INFO IMAGE ====================
BACKGROUND_DIR = os.path.join(os.getcwd(), "backgrounds")
try:
    if not os.path.exists(BACKGROUND_DIR):
        os.makedirs(BACKGROUND_DIR)
except:
    BACKGROUND_DIR = "."

# ==================== HÀM CHECK INFO FB / INSTAGRAM / TIKTOK (checkinfo.py) ====================

import logging
logger_info = logging.getLogger("checkinfo")

def detect_social_platform(link):
    link_lower = link.lower()
    if 'facebook.com' in link_lower or 'fb.com' in link_lower or 'fb.me' in link_lower:
        return 'facebook'
    elif 'instagram.com' in link_lower or 'instagr.am' in link_lower:
        return 'instagram'
    elif 'tiktok.com' in link_lower or 'vm.tiktok.com' in link_lower:
        return 'tiktok'
    else:
        return None

def extract_instagram_username(link):
    patterns = [r'instagram\.com/([^/?]+)', r'instagr\.am/([^/?]+)']
    for pattern in patterns:
        match = re.search(pattern, link)
        if match:
            return match.group(1)
    return None

def extract_tiktok_username(link):
    patterns = [r'tiktok\.com/@([^/?]+)', r'tiktok\.com/(@[^/?]+)']
    for pattern in patterns:
        match = re.search(pattern, link)
        if match:
            username = match.group(1)
            return username.replace('@', '')
    return None

def _normalize_facebook_link(link):
    """Chuẩn hoá mọi input FB: UID số, link đủ/thiếu https, username."""
    s = str(link or "").strip()
    if not s:
        return ""
    if s.isdigit():
        return f"https://www.facebook.com/profile.php?id={s}"
    low = s.lower()
    if any(x in low for x in ('facebook.com', 'fb.com', 'fb.me', 'm.facebook.com', 'mbasic.facebook.com')):
        if not s.startswith('http'):
            s = 'https://' + s.lstrip('/')
        return s
    if re.match(r'^[A-Za-z0-9.]{2,80}$', s) and not s.replace('.', '').isdigit():
        return f"https://www.facebook.com/{s}"
    return s


def _extract_facebook_vanity_slug(link):
    s = str(link or "").strip()
    if not s:
        return None
    if re.match(r'^[A-Za-z0-9.]{2,80}$', s) and not s.isdigit():
        return s
    m = re.search(
        r'(?:facebook|fb)\.com/(?!profile\.php|people/|groups/|pages/|share/|watch/|reel/|photo\.php|story\.php|events/)([A-Za-z0-9.]+)',
        s, re.I)
    if m and not m.group(1).isdigit():
        return m.group(1)
    return None


def _facebook_profile_urls(identifier, include_mbasic=False):
    """URL scrape profile — tự sinh theo UID số hoặc username bất kỳ."""
    ident = str(identifier or "").strip()
    if not ident:
        return []
    if ident.isdigit():
        urls = [
            f"https://www.facebook.com/profile.php?id={ident}",
            f"https://m.facebook.com/profile.php?id={ident}",
            f"https://www.facebook.com/{ident}",
            f"https://m.facebook.com/{ident}",
        ]
        if include_mbasic:
            urls = [f"https://mbasic.facebook.com/profile.php?id={ident}"] + urls
        return urls
    slug = _extract_facebook_vanity_slug(ident) or ident
    if 'facebook.com' in slug:
        urls = [slug, slug.replace('www.facebook.com', 'm.facebook.com')]
        if include_mbasic:
            urls = [slug.replace('www.facebook.com', 'mbasic.facebook.com'),
                    slug.replace('m.facebook.com', 'mbasic.facebook.com')] + urls
        return urls
    urls = [
        f"https://www.facebook.com/{slug}",
        f"https://m.facebook.com/{slug}",
    ]
    if include_mbasic:
        urls = [f"https://mbasic.facebook.com/{slug}"] + urls
    return urls


def _extract_facebook_username(link, uid):
    slug = _extract_facebook_vanity_slug(link)
    if slug:
        return slug
    if uid and not str(uid).isdigit():
        return str(uid)
    return "Không rõ"


def _extract_facebook_uid_fast(link):
    s = str(link).strip()
    if s.isdigit():
        return s

    patterns = [
        r'[?&]id=(\d+)',
        r'facebook\.com/(\d+)(?:[/?]|$)',
        r'fb\.com/(\d+)(?:[/?]|$)',
        r'fb\.me/(\d+)(?:[/?]|$)',
    ]
    for p in patterns:
        m = re.search(p, s, re.I)
        if m:
            return m.group(1)
    return None


# ==================== FACEBOOK INFO CHECK (async) ====================
_fb_info_loop = None
_fb_info_thread = None

_FB_CRAWLER_HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "Accept-Language": "en-US,en;q=0.9",
}

_FB_MOBILE_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
    "sec-ch-ua-mobile": "?1",
}


def _fb_info_ensure_loop():
    global _fb_info_loop, _fb_info_thread
    if _fb_info_loop is not None and _fb_info_loop.is_running():
        return

    def _run(loop):
        asyncio.set_event_loop(loop)
        loop.run_forever()

    _fb_info_loop = asyncio.new_event_loop()
    _fb_info_thread = threading.Thread(target=_run, args=(_fb_info_loop,), daemon=True)
    _fb_info_thread.start()


def _fb_empty_info(uid_or_slug=""):
    return {
        "platform": "facebook",
        "id": str(uid_or_slug or "Không rõ"),
        "name": "Không rõ",
        "username": "Không rõ",
        "gender": "Không rõ",
        "relationship": "Không rõ",
        "location": "Không rõ",
        "country": "Không rõ",
        "hometown": "Không rõ",
        "work": "Không rõ",
        "locale": "Không rõ",
        "bio": "Không rõ",
        "follower": "0",
        "following": "0",
        "friends": "0",
        "posts": "0",
        "created_time": "Không rõ",
        "updated_time": "Không rõ",
        "timezone": "Không rõ",
        "birthday": "Không rõ",
        "verified": "Không",
        "live_status": "Không rõ",
        "avatar_url": "",
        "link": f"facebook.com/{uid_or_slug}" if uid_or_slug else "Không rõ",
        "profile_url": f"https://www.facebook.com/{uid_or_slug}" if uid_or_slug else "",
    }


def _fb_safe_text(value, default="Không rõ"):
    if value is None:
        return default
    s = str(value).strip()
    if s in ("", "null", "None", "0" if default != "0" else "__never__"):
        return default
    return s


def _fb_escape_md(text):
    if text is None:
        return "Không rõ"
    s = str(text)
    for ch in ['\\', '*', '_', '`', '[']:
        s = s.replace(ch, '\\' + ch)
    return s


def _fb_is_valid_profile_html(html):
    if not html or len(html) < 1500:
        return False
    low = html.lower()
    if "<title>error</title>" in low:
        return False
    if "log in to facebook" in low[:12000] or "login.php" in low[:8000]:
        return False
    og = re.search(r'property="og:title"\s+content="([^"]+)"', html)
    if og:
        title = html_module.unescape(og.group(1)).strip()
        if title and len(title) > 1:
            bad = ("login", "đăng nhập", "facebook -", "error", "checkpoint")
            if not any(x in title.lower() for x in bad):
                return True
    if re.search(r'"follower_count":\d+', html) or re.search(r'"gender":"(?:MALE|FEMALE)"', html):
        return True
    title_m = re.search(r'<title>([^<]{2,80})</title>', html, re.I)
    if title_m:
        title = html_module.unescape(title_m.group(1)).strip()
        bad = ("error", "login", "đăng nhập", "facebook", "checkpoint")
        if title and not any(x in title.lower() for x in bad):
            return True
    return False


def _fb_sanitize_profile_info(info):
    info = info or {}
    uid = str(info.get("id") or "").strip()
    name = str(info.get("name") or "").strip()
    if uid and name == uid:
        info["name"] = "Không rõ"
    if name in ("Facebook User", uid):
        info["name"] = "Không rõ"
    ct = str(info.get("created_time") or "")
    if ct and ct != "Không rõ":
        try:
            parsed = datetime.strptime(ct, "%d/%m/%Y")
            if parsed.year > datetime.now().year or parsed > datetime.now():
                info["created_time"] = "Không rõ"
        except Exception:
            pass
    return info


def _fb_format_count(value):
    if value in (None, "", "Không rõ"):
        return "Không rõ"
    try:
        raw = str(value).strip().upper().replace(" ", "")
        mult = 1
        if raw.endswith("K"):
            mult = 1000
            raw = raw[:-1]
        elif raw.endswith("M"):
            mult = 1000000
            raw = raw[:-1]
        raw = raw.replace(".", "").replace(",", ".")
        num = int(float(raw) * mult)
        return f"{num:,}".replace(",", ".")
    except Exception:
        return _fb_safe_text(value, "Không rõ")


def _fb_merge_profile(info, profile):
    if not profile or profile.get("status") == "ERROR":
        return info
    field_map = {
        "name": "name",
        "avatar": "avatar_url",
        "bio": "bio",
        "category": "work",
        "gender": "gender",
        "locale": "locale",
        "created_time": "created_time",
        "birthday": "birthday",
    }
    count_map = {
        "followers": "follower",
        "following": "following",
        "friends": "friends",
    }
    empty = (None, "", "Không rõ", "Facebook User")
    for src, dst in field_map.items():
        val = profile.get(src)
        if val not in empty and info.get(dst) in empty + ("0", "Không"):
            info[dst] = str(val)
    for src, dst in count_map.items():
        val = profile.get(src)
        if val not in (None, ""):
            info[dst] = str(val)
    if profile.get("verified"):
        info["verified"] = "Có"
    return info


def format_facebook_info_report(info):
    """Trả về chuỗi báo cáo Facebook đầy đủ (VIP / cookie)."""
    info = info or {}
    live = info.get("live_status", "Không rõ")
    if live == "LIVE":
        status_line = "🟢 LIVE"
    elif live == "DIE":
        status_line = "🔴 DIE"
    else:
        status_line = str(live)

    uid = _fb_safe_text(info.get("id"), "Không rõ")
    profile_url = info.get("profile_url") or f"https://www.facebook.com/{uid}"
    cookie_note = ""
    if info.get("cookie_status") == "public_fallback":
        cookie_note = "⚠️ Cookie không lấy được dữ liệu — hiển thị phần công khai.\n\n"

    body = (
        f"👤 Tên: {_fb_escape_md(_fb_safe_text(info.get('name')))}\n"
        f"🆔 UID: {uid}\n"
        f"📝 Username: {_fb_escape_md(_fb_safe_text(info.get('username')))}\n\n"
        f"🚻 Giới tính: {_fb_escape_md(_fb_safe_text(info.get('gender')))}\n"
        f"💑 Tình trạng: {_fb_escape_md(_fb_safe_text(info.get('relationship')))}\n"
        f"📍 Nơi ở: {_fb_escape_md(_fb_safe_text(info.get('location')))}\n"
        f"🌍 Quốc gia: {_fb_escape_md(_fb_safe_text(info.get('country')))}\n"
        f"🏡 Quê quán: {_fb_escape_md(_fb_safe_text(info.get('hometown')))}\n"
        f"💼 Công việc: {_fb_escape_md(_fb_safe_text(info.get('work')))}\n"
        f"🌐 Ngôn ngữ: {_fb_escape_md(_fb_safe_text(info.get('locale')))}\n"
        f"📖 Giới thiệu: {_fb_escape_md(_fb_safe_text(info.get('bio')))}\n\n"
        f"👥 Followers: {_fb_format_count(info.get('follower'))}\n"
        f"👤 Following: {_fb_format_count(info.get('following'))}\n"
        f"🤝 Bạn bè: {_fb_format_count(info.get('friends'))}\n"
        f"📝 Bài viết: {_fb_format_count(info.get('posts'))}\n\n"
        f"📅 Ngày tạo: {_fb_escape_md(_fb_safe_text(info.get('created_time')))}\n"
        f"🔄 Cập nhật: {_fb_escape_md(_fb_safe_text(info.get('updated_time')))}\n"
        f"🎂 Sinh nhật: {_fb_escape_md(_fb_safe_text(info.get('birthday')))}\n"
        f"🕒 Timezone: {_fb_escape_md(_fb_safe_text(info.get('timezone')))}\n"
        f"✅ Xác minh: {_fb_escape_md(_fb_safe_text(info.get('verified'), 'Không'))}\n"
        f"📈 Trạng thái: {status_line}\n\n"
        f"🔗 [Mở Profile]({profile_url})\n"
        f"⏰ {datetime.now().strftime('%H:%M:%S - %d/%m/%Y')}"
    )
    return f"👑 CHECK INFO FB (VIP — Cookie Clone)\n━━━━━━━━━━━━━\n{cookie_note}{body}"


def format_facebook_info_basic(info):
    """Báo cáo Facebook cơ bản — API/scrape công khai, không cookie."""
    info = info or {}
    live = info.get("live_status", "Không rõ")
    if live == "LIVE":
        status_line = "🟢 LIVE"
    elif live == "DIE":
        status_line = "🔴 DIE"
    else:
        status_line = str(live)

    uid = _fb_safe_text(info.get("id"), "Không rõ")
    profile_url = info.get("profile_url") or f"https://www.facebook.com/{uid}"

    return (
        f"📋 CHECK INFO FB (CƠ BẢN)\n"
        f"━━━━━━━━━━━━━\n"
        f"👤 Tên: {_fb_escape_md(_fb_safe_text(info.get('name')))}\n"
        f"🆔 UID: {uid}\n"
        f"📝 Username: {_fb_escape_md(_fb_safe_text(info.get('username')))}\n\n"
        f"👥 Followers: {_fb_format_count(info.get('follower'))}\n"
        f"🌐 Ngôn ngữ: {_fb_escape_md(_fb_safe_text(info.get('locale')))}\n"
        f"📈 Trạng thái: {status_line}\n\n"
        f"🔗 [Mở Profile]({profile_url})\n"
        f"⏰ {datetime.now().strftime('%H:%M:%S - %d/%m/%Y')}\n\n"
        f"⭐ Nâng cấp VIP để xem Full qua cookie clone:\n"
        f"giới tính, following, sinh nhật, nơi ở, bạn bè..."
    )


def _fb_can_use_premium(user_id):
    if user_id in ADMIN_IDS:
        return True
    is_vip, _ = check_vip(user_id)
    if is_vip:
        return True
    cfg = get_config()
    return bool(cfg.get("free_features", {}).get("check_info_vip", False))


async def _async_http_get_text(session, url, headers=None, cookies=None):
    try:
        async with session.get(
            url,
            headers=headers or _FB_CRAWLER_HEADERS,
            cookies=cookies,
            allow_redirects=True,
        ) as resp:
            if resp.status == 200:
                text = await resp.text()
                if text and len(text) > 1000:
                    return text
    except Exception:
        pass
    return None


async def _async_resolve_facebook_uid(norm_link):
    uid = _extract_facebook_uid_fast(norm_link)
    if uid:
        return uid
    try:
        loop = asyncio.get_running_loop()
        resolved = await loop.run_in_executor(
            None, lambda: get_uid_from_link(norm_link)[0]
        )
        if resolved:
            return str(resolved)
    except Exception:
        pass
    return None


async def _async_fetch_profile_html(session, uid, norm_link, use_cookie=False):
    ident = norm_link or uid
    cookie_dict = {}
    if use_cookie:
        try:
            cookie_string = _get_fb_cookie_string()
            cookie_dict = _cookie_string_to_dict(cookie_string)
        except Exception:
            pass

    mobile = getattr(fb_extractor, "mobile_headers", None) or _FB_MOBILE_HEADERS
    urls_all = _facebook_profile_urls(ident, include_mbasic=bool(cookie_dict))
    urls_public = _facebook_profile_urls(ident, include_mbasic=False)

    if cookie_dict:
        cookie_urls = [u for u in urls_all if "mbasic.facebook.com" in u or "m.facebook.com" in u]
        cookie_urls += [u for u in urls_all if u not in cookie_urls]
        for url in cookie_urls:
            html = await _async_http_get_text(
                session, url, headers=mobile, cookies=cookie_dict)
            if html and _fb_is_valid_profile_html(html):
                return html, "cookie"

    for url in urls_public:
        html = await _async_http_get_text(
            session, url, headers=_FB_CRAWLER_HEADERS, cookies=None)
        if html and _fb_is_valid_profile_html(html):
            return html, "public"

    return None, None


async def async_fetch_facebook_info(link, mode="basic"):
    """Lấy thông tin Facebook — mode: basic (public) | premium (cookie clone)."""
    raw = str(link or "").strip()
    norm_link = _normalize_facebook_link(raw) or raw
    mode = "premium" if mode == "premium" else "basic"
    cache_key = f"fb:{mode}:{norm_link.lower()}"
    cached = _fast_cache_get(cache_key)
    if cached:
        return cached, None

    use_cookie = mode == "premium"
    if use_cookie and not _get_fb_cookie_string():
        return None, (
            "❌ Chưa cấu hình cookie clone.\n\n"
            "Admin cần nạp cookie: `/cookie <nội_dung_cookie>`"
        )

    try:
        uid = None
        scrape_key = None
        profile = {}
        html = None

        timeout = aiohttp.ClientTimeout(total=25, connect=8)
        connector = aiohttp.TCPConnector(ssl=False, limit=20)
        async with aiohttp.ClientSession(timeout=timeout, connector=connector) as session:
            uid = await _async_resolve_facebook_uid(norm_link)
            scrape_key = uid or _extract_facebook_vanity_slug(norm_link)
            if not scrape_key:
                return None, "❌ Không lấy được UID từ link Facebook"

            if uid and str(uid).isdigit():
                uid_cache = _fast_cache_get(f"fb_uid:{mode}:{uid}")
                if uid_cache:
                    _fast_cache_set(cache_key, uid_cache)
                    return uid_cache, None

            info = _fb_empty_info(uid or scrape_key)
            info["id"] = str(uid or scrape_key)
            info["username"] = _extract_facebook_username(norm_link, info["id"])
            info["link"] = f"facebook.com/{uid or scrape_key}"
            info["profile_url"] = (
                f"https://www.facebook.com/profile.php?id={uid}"
                if uid and str(uid).isdigit()
                else f"https://www.facebook.com/{scrape_key}"
            )
            info["fetch_mode"] = mode

            html, fetch_source = await _async_fetch_profile_html(
                session, uid or scrape_key, norm_link, use_cookie=use_cookie)
            if use_cookie:
                if fetch_source == "cookie":
                    info["cookie_status"] = "ok"
                elif fetch_source == "public":
                    info["cookie_status"] = "public_fallback"
                else:
                    info["cookie_status"] = "failed"
            loop = asyncio.get_running_loop()

            if html:
                vanity = _extract_facebook_vanity_slug(norm_link)
                if vanity and str(vanity).isdigit():
                    vanity = None
                if not vanity:
                    vanity = scrape_key if scrape_key and not str(scrape_key).isdigit() else None
                profile = await loop.run_in_executor(
                    None,
                    lambda: fb_extractor.extract_profile_info(html, vanity_url_name=vanity) or {},
                )
                info = _fb_merge_profile(info, profile)

            if info.get("name") in (None, "", "Không rõ", "Facebook User"):
                name = await loop.run_in_executor(
                    None, lambda: get_uid_from_link(norm_link)[1]
                )
                if name:
                    info["name"] = name

            if uid and str(uid).isdigit():
                live = await loop.run_in_executor(None, lambda: check_uid_live_die(uid))
                info["live_status"] = live if live in ("LIVE", "DIE") else "Không rõ"
            elif html and info.get("name") not in (None, "", "Không rõ", "Facebook User"):
                info["live_status"] = "LIVE"
            else:
                info["live_status"] = "DIE"

            avatar_url = info.get("avatar_url") or (profile.get("avatar") if profile else "")
            if not avatar_url or "84628273_176159830277856" in str(avatar_url):
                av_key = uid if uid and str(uid).isdigit() else scrape_key
                fetched_av = await loop.run_in_executor(
                    None, lambda: get_facebook_avatar_url(av_key)
                )
                if fetched_av:
                    avatar_url = fetched_av
            if not avatar_url and uid and str(uid).isdigit():
                avatar_url = f"https://graph.facebook.com/v3.3/{uid}/picture?type=large"
            info["avatar_url"] = avatar_url or ""

            if info.get("username") in (None, "", "Không rõ"):
                info["username"] = _extract_facebook_username(norm_link, info.get("id"))

            info = _fb_sanitize_profile_info(info)

        _fast_cache_set(cache_key, info)
        if uid and str(uid).isdigit():
            _fast_cache_set(f"fb_uid:{mode}:{uid}", info)
        return info, None
    except Exception as e:
        return None, f"❌ Lỗi: {str(e)}"


def get_facebook_info_full(link, mode="basic"):
    """Wrapper đồng bộ — mode: basic | premium."""
    _fb_info_ensure_loop()
    mode = "premium" if mode == "premium" else "basic"
    future = asyncio.run_coroutine_threadsafe(
        async_fetch_facebook_info(link, mode=mode), _fb_info_loop)
    try:
        return future.result(timeout=50)
    except Exception as e:
        return None, f"❌ Lỗi: {str(e)}"


def get_facebook_info_text(link, mode="basic"):
    """Trả về chuỗi báo cáo Facebook."""
    info, error = get_facebook_info_full(link, mode=mode)
    if error:
        return error
    if mode == "premium":
        return format_facebook_info_report(info)
    return format_facebook_info_basic(info)

def _parse_ig_user_data(user_data, username):
    """Chuẩn hoá dữ liệu user từ bất kỳ API nào về cùng 1 format."""
    follower = (user_data.get("follower_count")
                or user_data.get("edge_followed_by", {}).get("count", 0))
    following = (user_data.get("following_count")
                 or user_data.get("edge_follow", {}).get("count", 0))
    media = (user_data.get("media_count")
             or user_data.get("edge_owner_to_timeline_media", {}).get("count", 0))
    hd_versions = user_data.get("hd_profile_pic_versions", [])
    avatar = (
        max(hd_versions, key=lambda x: x.get("width", 0)).get("url", "") if hd_versions
        else user_data.get("profile_pic_url_hd")
        or user_data.get("hd_profile_pic_url_info", {}).get("url")
        or user_data.get("profile_pic_url", "")
    )
    bio_links = user_data.get("bio_links", [])
    ext_url = user_data.get("external_url") or (bio_links[0].get("url") if bio_links else "Không có")
    return {
        "platform": "instagram",
        "name": user_data.get("full_name") or "Không rõ",
        "username": user_data.get("username") or username,
        "id": str(user_data.get("id") or user_data.get("pk") or "Không rõ"),
        "avatar_url": avatar,
        "biography": user_data.get("biography") or "Không có",
        "follower_count": follower,
        "following_count": following,
        "media_count": media,
        "is_verified": "Có" if user_data.get("is_verified") else "Không",
        "is_private": "Có" if user_data.get("is_private") else "Không",
        "is_business": "Có" if user_data.get("is_business") else "Không",
        "external_url": ext_url or "Không có",
        "category": user_data.get("category_name") or user_data.get("category") or "Không có",
        "link": f"instagram.com/{username}",
    }


def get_instagram_info_full(link):
    """Lấy thông tin Instagram - ưu tiên API mới, fallback sang IG native."""
    username = extract_instagram_username(link)
    if not username:
        return None, "❌ Không lấy được username từ link Instagram"

    user_data = None

    # ── API 1: keyherlyswar (mới, ưu tiên cao nhất) ──
    try:
        r = requests.get(
            f"https://keyherlyswar.x10.mx/Apidocs/get_info/getinfoinsta.php?username={username}",
            timeout=FAST_API_TIMEOUT
        )
        if r.status_code == 200:
            j = r.json()
            d = j.get("data") or {}
            if d and (d.get("id") or d.get("username")):
                user_data = d
    except Exception:
        pass

    # ── API 2: i.instagram.com Android header ──
    if not user_data:
        try:
            r = requests.get(
                f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}",
                headers={
                    "User-Agent": "Instagram 219.0.0.12.117 Android",
                    "Accept": "application/json",
                    "X-IG-App-ID": "936619743392459",
                },
                timeout=FAST_API_TIMEOUT
            )
            if r.status_code == 200:
                j = r.json()
                u = j.get("data", {}).get("user") or j.get("user") or {}
                if u:
                    user_data = u
        except Exception:
            pass

    # ── API 3: instagram.com mobile browser ──
    if not user_data:
        try:
            r = requests.get(
                f"https://www.instagram.com/api/v1/users/web_profile_info/?username={username}",
                headers={
                    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15",
                    "Accept": "*/*",
                    "X-IG-App-ID": "936619743392459",
                    "X-Requested-With": "XMLHttpRequest",
                    "Referer": f"https://www.instagram.com/{username}/",
                },
                timeout=FAST_API_TIMEOUT
            )
            if r.status_code == 200:
                j = r.json()
                user_data = j.get("data", {}).get("user") or j.get("user") or {}
        except Exception:
            pass

    if not user_data:
        return None, f"❌ Không lấy được thông tin Instagram @{username}\n💡 Thử lại sau hoặc kiểm tra lại username."

    return _parse_ig_user_data(user_data, username), None

def get_tiktok_info_full(link):
    """Lấy thông tin TikTok qua api.zeidteam.xyz (tik.py)."""
    username = extract_tiktok_username(link)
    if not username:
        raw = str(link or "").strip().lstrip('@')
        if re.match(r'^[A-Za-z0-9._]{1,50}$', raw):
            username = raw
    if not username:
        return None, "❌ Không lấy được username từ link TikTok"

    try:
        res = requests.get(
            f"https://api.zeidteam.xyz/tiktok/user-info?username={urllib.parse.quote(username)}",
            timeout=FAST_API_TIMEOUT,
        )
        data = res.json()
    except Exception as e:
        return None, f"❌ Lỗi khi tra cứu: {str(e)}"

    if not data.get("status"):
        return None, "❌ Không tìm thấy tài khoản TikTok này!"

    user = (data.get("data") or {}).get("user") or {}
    stats = (data.get("data") or {}).get("stats") or {}

    def _tt_safe(val, default="Không có"):
        if val in (None, "", "null", "None"):
            return default
        return val

    create_time = "Không rõ"
    ct = user.get("createTime")
    if ct and str(ct).isdigit():
        create_time = datetime.fromtimestamp(int(ct)).strftime("%d/%m/%Y")

    uname = _tt_safe(user.get("uniqueId"), username)
    nick = _tt_safe(user.get("nickname"), "Không rõ")
    sig = user.get("signature")
    if sig in (None, "", "null", "None"):
        sig = "Không có"

    avatar_url = user.get("avatarLarger") or user.get("avatarMedium") or user.get("avatarThumb") or ""

    info = {
        "platform": "tiktok",
        "name": nick,
        "username": uname,
        "id": str(_tt_safe(user.get("id"), "Không rõ")),
        "avatar_url": avatar_url,
        "signature": sig,
        "follower_count": stats.get("followerCount") or 0,
        "following_count": stats.get("followingCount") or 0,
        "heart_count": stats.get("heartCount") or 0,
        "video_count": stats.get("videoCount") or 0,
        "verified": "Có" if user.get("verified") else "Không",
        "private_account": "Có" if user.get("privateAccount") else "Không",
        "created_time": create_time,
        "language": "Không rõ",
        "link": f"tiktok.com/@{uname}",
    }
    return info, None


def _load_avatar_image(avatar_url, size):
    """Tai avatar tu URL, tra ve PIL Image hoac None - co fallback"""
    if not avatar_url:
        return None
    from io import BytesIO as _BytesIO

    headers_av = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
    }

    urls_to_try = [avatar_url]
    # Neu la graph.facebook.com, redirect=1 de lay anh truc tiep
    if "graph.facebook.com" in avatar_url and "redirect=0" in avatar_url:
        urls_to_try.append(avatar_url.replace("redirect=0", "redirect=1"))
    elif "graph.facebook.com" in avatar_url and "redirect=false" in avatar_url:
        urls_to_try.append(avatar_url.replace("redirect=false", "redirect=true"))

    for url in urls_to_try:
        try:
            r = requests.get(url, headers=headers_av, timeout=12, allow_redirects=True)
            if r.status_code == 200 and len(r.content) > 500:
                ct = r.headers.get("content-type", "")
                if "image" in ct or "octet" in ct or len(r.content) > 1000:
                    img = Image.open(_BytesIO(r.content)).convert("RGBA")
                    img = img.resize((size, size), Image.Resampling.LANCZOS)
                    mask_av = Image.new("L", img.size, 0)
                    ImageDraw.Draw(mask_av).ellipse((0, 0, size, size), fill=255)
                    img.putalpha(mask_av)
                    return img
        except Exception:
            continue
    return None

def create_facebook_info_image_full(info):
    """Tạo ảnh thẻ thông tin Facebook"""
    try:
        from io import BytesIO as _BytesIO
        font_path = None
        for fp in ["arial.ttf", "Arial.ttf", "DejaVuSans.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]:
            if os.path.exists(fp):
                font_path = fp
                break
        if font_path:
            name_font = ImageFont.truetype(font_path, 50)
            title_font = ImageFont.truetype(font_path, 20)
            value_font = ImageFont.truetype(font_path, 20)
        else:
            name_font = title_font = value_font = ImageFont.load_default()

        canvas_size = (1280, 768)
        bg_color = (random.randint(30,80), random.randint(80,150), random.randint(150,220))
        background = Image.new("RGBA", canvas_size, bg_color + (255,))

        # Glass panel trái
        margin = 50
        gl = Image.new("RGBA", canvas_size, (0,0,0,0))
        gl_draw = ImageDraw.Draw(gl)
        gl_draw.rounded_rectangle([(margin, margin),(margin+400, canvas_size[1]-margin)], radius=25, fill=(255,255,255,50))
        background = Image.alpha_composite(background, gl)

        # Avatar
        avatar_size = 180
        avatar_x = margin + (400-avatar_size)//2
        avatar_y = margin + 30
        av = _load_avatar_image(info.get('avatar_url',''), avatar_size)
        if av:
            border = Image.new("RGBA", (avatar_size+10, avatar_size+10), (0,0,0,0))
            ImageDraw.Draw(border).ellipse((0,0,avatar_size+10,avatar_size+10), outline=(255,255,255,200), width=4)
            background.paste(border, (avatar_x-5, avatar_y-5), border)
            background.paste(av, (avatar_x, avatar_y), av)

        # Tên trên ảnh trái
        draw = ImageDraw.Draw(background)
        draw.text((margin+20, avatar_y+avatar_size+20), info['name'], fill=(255,255,255), font=name_font)

        # Info panel phải
        right_x = margin + 420
        rows = [
            ("🆔 UID", info.get('id','')),
            ("📝 Username", info.get('username','')),
            ("🚻 Giới tính", info.get('gender','')),
            ("💑 Quan hệ", info.get('relationship','')),
            ("📍 Sống tại", info.get('location','')),
            ("🏡 Quê quán", info.get('hometown','')),
            ("💼 Công việc", info.get('work','')),
            ("🎂 Sinh nhật", info.get('birthday','')),
            ("📅 Ngày tạo", info.get('created_time','')),
            ("👥 Follower", str(info.get('follower',''))),
            ("✅ Xác minh", info.get('verified','')),
            ("🌐 Ngôn ngữ", info.get('locale','')),
            ("🕐 Múi giờ", str(info.get('timezone',''))),
        ]
        y = margin + 20
        for label, val in rows:
            draw.text((right_x, y), f"{label}:", fill=(200,230,255), font=title_font)
            draw.text((right_x + 200, y), str(val)[:35], fill=(255,255,255), font=value_font)
            y += 42

        image_path = os.path.join(CACHE_DIR, f"info_fb_{random.randint(1000,9999)}.png")
        background.convert("RGB").save(image_path, "PNG")
        return image_path, None
    except Exception as e:
        return None, f"❌ Lỗi tạo ảnh: {str(e)}"

def create_instagram_info_image_full(info):
    """Tạo ảnh thẻ thông tin Instagram (gradient hồng)"""
    try:
        from io import BytesIO as _BytesIO
        font_path = None
        for fp in ["arial.ttf", "Arial.ttf", "DejaVuSans.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]:
            if os.path.exists(fp):
                font_path = fp
                break
        if font_path:
            name_font = ImageFont.truetype(font_path, 55)
            title_font = ImageFont.truetype(font_path, 20)
            value_font = ImageFont.truetype(font_path, 20)
        else:
            name_font = title_font = value_font = ImageFont.load_default()

        canvas_size = (1280, 768)
        background = Image.new("RGBA", canvas_size, (193, 53, 132, 255))
        overlay = Image.new("RGBA", canvas_size, (255,255,255,60))
        background = Image.alpha_composite(background, overlay)

        avatar_size = 190
        avatar_x = (canvas_size[0]-avatar_size)//2
        avatar_y = 60
        av = _load_avatar_image(info.get('avatar_url',''), avatar_size)
        if av:
            border = Image.new("RGBA", (avatar_size+10, avatar_size+10), (0,0,0,0))
            ImageDraw.Draw(border).ellipse((0,0,avatar_size+10,avatar_size+10), outline=(225,48,108,255), width=5)
            background.paste(border, (avatar_x-5, avatar_y-5), border)
            background.paste(av, (avatar_x, avatar_y), av)

        draw = ImageDraw.Draw(background)
        name_y = avatar_y + avatar_size + 20
        draw.text(((canvas_size[0]-len(info['name'])*28)//2, name_y), info['name'], fill=(255,255,255), font=name_font)
        draw.text(((canvas_size[0]-len(f"@{info['username']}")*12)//2, name_y+65), f"@{info['username']}", fill=(240,200,230), font=value_font)

        # Bio box
        bio_y = name_y + 105
        bio_box = Image.new("RGBA", (700,60), (0,0,0,0))
        ImageDraw.Draw(bio_box).rounded_rectangle([(0,0),(700,60)], radius=12, fill=(255,255,255,80))
        ImageDraw.Draw(bio_box).text((10,10), info.get('biography','')[:80], fill=(255,255,255), font=value_font)
        background.paste(bio_box, ((canvas_size[0]-700)//2, bio_y), bio_box)

        # Stats
        stats = [
            ("Bài viết", str(info.get('media_count',0))),
            ("Follower", str(info.get('follower_count',0))),
            ("Following", str(info.get('following_count',0))),
            ("Xác minh", info.get('is_verified','Không')),
        ]
        stats_y = bio_y + 80
        box_w, box_h = 190, 75
        total_w = len(stats)*box_w + (len(stats)-1)*15
        start_x = (canvas_size[0]-total_w)//2
        for i, (t, v) in enumerate(stats):
            sx = start_x + i*(box_w+15)
            sb = Image.new("RGBA", (box_w, box_h), (0,0,0,0))
            ImageDraw.Draw(sb).rounded_rectangle([(0,0),(box_w,box_h)], radius=12, fill=(225,48,108,200))
            ImageDraw.Draw(sb).text((10,8), t, fill=(255,255,255), font=title_font)
            ImageDraw.Draw(sb).text((10,36), v, fill=(255,255,255), font=value_font)
            background.paste(sb, (sx, stats_y), sb)

        image_path = os.path.join(CACHE_DIR, f"info_ig_{random.randint(1000,9999)}.png")
        background.convert("RGB").save(image_path, "PNG")
        return image_path, None
    except Exception as e:
        return None, f"❌ Lỗi tạo ảnh: {str(e)}"

def create_tiktok_info_image_full(info):
    """Tạo ảnh thẻ thông tin TikTok (nền đen)"""
    try:
        font_path = None
        for fp in ["arial.ttf", "Arial.ttf", "DejaVuSans.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]:
            if os.path.exists(fp):
                font_path = fp
                break
        if font_path:
            name_font = ImageFont.truetype(font_path, 55)
            title_font = ImageFont.truetype(font_path, 20)
            value_font = ImageFont.truetype(font_path, 20)
        else:
            name_font = title_font = value_font = ImageFont.load_default()

        canvas_size = (1280, 768)
        background = Image.new("RGBA", canvas_size, (20, 20, 20, 255))
        overlay = Image.new("RGBA", canvas_size, (255,255,255,25))
        background = Image.alpha_composite(background, overlay)

        avatar_size = 190
        avatar_x = (canvas_size[0]-avatar_size)//2
        avatar_y = 55
        av = _load_avatar_image(info.get('avatar_url',''), avatar_size)
        if av:
            border = Image.new("RGBA", (avatar_size+10, avatar_size+10), (0,0,0,0))
            ImageDraw.Draw(border).ellipse((0,0,avatar_size+10,avatar_size+10), outline=(254,44,85,255), width=5)
            background.paste(border, (avatar_x-5, avatar_y-5), border)
            background.paste(av, (avatar_x, avatar_y), av)

        draw = ImageDraw.Draw(background)
        name_y = avatar_y + avatar_size + 20
        draw.text(((canvas_size[0]-len(info['name'])*28)//2, name_y), info['name'], fill=(255,255,255), font=name_font)
        draw.text(((canvas_size[0]-len(f"@{info['username']}")*12)//2, name_y+65), f"@{info['username']}", fill=(180,180,180), font=value_font)

        # Bio
        bio_y = name_y + 105
        bio_box = Image.new("RGBA", (700,60), (0,0,0,0))
        ImageDraw.Draw(bio_box).rounded_rectangle([(0,0),(700,60)], radius=12, fill=(255,255,255,30))
        ImageDraw.Draw(bio_box).text((10,10), info.get('signature','')[:80], fill=(220,220,220), font=value_font)
        background.paste(bio_box, ((canvas_size[0]-700)//2, bio_y), bio_box)

        # Stats
        stats = [
            ("Follower", str(info.get('follower_count',0))),
            ("Following", str(info.get('following_count',0))),
            ("❤️ Likes", str(info.get('heart_count',0))),
            ("🎬 Video", str(info.get('video_count',0))),
        ]
        stats_y = bio_y + 80
        box_w, box_h = 185, 75
        total_w = len(stats)*box_w + (len(stats)-1)*15
        start_x = (canvas_size[0]-total_w)//2
        for i, (t, v) in enumerate(stats):
            sx = start_x + i*(box_w+15)
            sb = Image.new("RGBA", (box_w, box_h), (0,0,0,0))
            ImageDraw.Draw(sb).rounded_rectangle([(0,0),(box_w,box_h)], radius=12, fill=(254,44,85,200))
            ImageDraw.Draw(sb).text((10,8), t, fill=(255,255,255), font=title_font)
            ImageDraw.Draw(sb).text((10,36), v, fill=(255,255,255), font=value_font)
            background.paste(sb, (sx, stats_y), sb)

        image_path = os.path.join(CACHE_DIR, f"info_tt_{random.randint(1000,9999)}.png")
        background.convert("RGB").save(image_path, "PNG")
        return image_path, None
    except Exception as e:
        return None, f"❌ Lỗi tạo ảnh: {str(e)}"

def _download_avatar_bytes(avatar_url):
    """Tai avatar URL ve bytes, uu tien toc do va fallback an toan."""
    if not avatar_url:
        return None

    headers_list = [
        {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"},
        {},
    ]
    for h in headers_list:
        try:
            r = info_fast_session.get(avatar_url, headers=h, timeout=FAST_AVATAR_TIMEOUT, allow_redirects=True, stream=False)
            if r.status_code == 200 and len(r.content) > 500:
                ct = r.headers.get("content-type", "")
                if "image" in ct or "octet" in ct or len(r.content) > 1000:
                    return r.content
        except Exception:
            continue
    return None

def _md(text):
    """Escape ky tu dac biet Markdown Telegram de tranh loi parse"""
    if text is None:
        return "Không rõ"
    s = str(text)
    # Chi escape * _ ` [ trong plain Markdown mode
    for ch in ['\\', '*', '_', '`', '[']:
        s = s.replace(ch, '\\' + ch)
    return s

def handle_check_info_full(message, link, fb_mode="basic"):
    """Xử lý check info FB/IG/TikTok — fb_mode: basic | premium (chỉ Facebook)."""
    chat_id = message.chat.id
    user_id = message.from_user.id
    raw_link = str(link).strip()
    platform = detect_social_platform(raw_link)

    if not platform:
        if raw_link.isdigit():
            platform = 'facebook'
            link = _normalize_facebook_link(raw_link)
        elif _extract_facebook_vanity_slug(raw_link):
            platform = 'facebook'
            link = _normalize_facebook_link(raw_link)
        else:
            bot.reply_to(message,
                "❌ Không nhận diện được platform!\n\n"
                "✅ Hỗ trợ:\n"
                "• UID số: <code>100001234567890</code>\n"
                "• <code>https://facebook.com/username</code>\n"
                "• <code>username</code> (tên FB)\n"
                "• https://instagram.com/username\n"
                "• https://tiktok.com/@username",
                parse_mode="HTML")
            return
    elif platform == 'facebook':
        link = _normalize_facebook_link(raw_link)
    else:
        link = raw_link

    processing_msg = bot.reply_to(message, f"⏳ Đang lấy thông tin {platform.upper()}...")

    try:
        if platform == 'facebook':
            mode = "premium" if fb_mode == "premium" else "basic"
            if mode == "premium" and not _fb_can_use_premium(user_id):
                bot.edit_message_text(
                    "⚠️ Check Info FB Full (VIP) chỉ dành cho Admin và thành viên VIP.\n\n"
                    "Dùng mục 📋 Check Info FB (Cơ bản) hoặc nâng cấp VIP.",
                    processing_msg.chat.id, processing_msg.message_id)
                return
            info, error = get_facebook_info_full(link, mode=mode)
            if error:
                bot.edit_message_text(error, processing_msg.chat.id, processing_msg.message_id)
                return
            avatar_url = info.get('avatar_url', '')
            caption = (
                format_facebook_info_report(info)
                if mode == "premium"
                else format_facebook_info_basic(info)
            )

        elif platform == 'instagram':
            info, error = get_instagram_info_full(link)
            if error:
                bot.edit_message_text(error, processing_msg.chat.id, processing_msg.message_id)
                return
            avatar_url = info.get('avatar_url', '')
            caption = (
                f"📷 *THÔNG TIN INSTAGRAM*\n"
                f"━━━━━━━━━━━━━━\n"
                f"👤 Tên: *{_md(info['name'])}*\n"
                f"🆔 ID: `{info['id']}`\n"
                f"📝 Username: @{_md(info['username'])}\n\n"
                f"📖 Bio: {_md(info['biography'])}\n\n"
                f"👥 Follower: *{info['follower_count']}*\n"
                f"👤 Following: {info['following_count']}\n"
                f"📷 Bài viết: {info['media_count']}\n\n"
                f"✅ Xác minh: {_md(info['is_verified'])}\n"
                f"🔒 Riêng tư: {_md(info['is_private'])}\n"
                f"💼 Business: {_md(info['is_business'])}\n"
                f"📂 Danh mục: {_md(info['category'])}\n"
                f"🔗 External: {_md(info['external_url'])}\n\n"
                f"🔗 [Mở Profile](https://www.instagram.com/{info['username']})\n"
                f"⏰ {datetime.now().strftime('%H:%M:%S - %d/%m/%Y')}"
            )

        elif platform == 'tiktok':
            info, error = get_tiktok_info_full(link)
            if error:
                bot.edit_message_text(error, processing_msg.chat.id, processing_msg.message_id)
                return
            avatar_url = info.get('avatar_url', '')
            caption = (
                f"🎵 *THÔNG TIN TIKTOK*\n"
                f"━━━━━━━━━━━━━━\n"
                f"👤 Tên: *{_md(info['name'])}*\n"
                f"🆔 ID: `{info['id']}`\n"
                f"📝 Username: @{_md(info['username'])}\n\n"
                f"📖 Bio: {_md(info['signature'])}\n\n"
                f"👥 Follower: *{info['follower_count']}*\n"
                f"👤 Following: {info['following_count']}\n"
                f"❤️ Likes: {info['heart_count']}\n"
                f"🎬 Video: {info['video_count']}\n\n"
                f"✅ Xác minh: {_md(info['verified'])}\n"
                f"🔒 Riêng tư: {_md(info['private_account'])}\n"
                f"📅 Ngày tạo: {_md(info['created_time'])}\n"
                f"🌐 Khu vực: {_md(info['language'])}\n\n"
                f"🔗 [Mở Profile](https://www.tiktok.com/@{info['username']})\n"
                f"⏰ {datetime.now().strftime('%H:%M:%S - %d/%m/%Y')}"
            )
        else:
            return

        # ── Xoá tin nhắn chờ ──
        try:
            bot.delete_message(processing_msg.chat.id, processing_msg.message_id)
        except Exception:
            pass

        # ── Gửi ảnh avatar nhanh: ưu tiên Telegram tự lấy URL, fallback bytes rồi text ──
        sent = False
        photo_parse = "Markdown"
        if avatar_url:
            try:
                bot.send_photo(chat_id, avatar_url, caption=caption, parse_mode=photo_parse)
                sent = True
            except Exception:
                pass

        if not sent and avatar_url:
            avatar_bytes = _download_avatar_bytes(avatar_url)
            if avatar_bytes:
                try:
                    from io import BytesIO as _BytesIO
                    bot.send_photo(chat_id, _BytesIO(avatar_bytes), caption=caption, parse_mode=photo_parse)
                    sent = True
                except Exception:
                    sent = False

        if not sent:
            bot.send_message(chat_id, caption, parse_mode=photo_parse, disable_web_page_preview=True)

    except Exception as e:
        try:
            bot.edit_message_text(f"❌ Lỗi xử lý: {str(e)}", processing_msg.chat.id, processing_msg.message_id)
        except Exception:
            bot.reply_to(message, f"❌ Lỗi: {str(e)}")

# ==================== LỆNH /info ====================
@bot.message_handler(commands=['info'])
def info_command_handler(message):
    if not require_feature_access_message(message, "check_info", FEATURE_LABELS["check_info"]):
        return
    try:
        parts = message.text.split(None, 1)
        if len(parts) < 2:
            bot.reply_to(message,
                "❌ Sai cú pháp!\n\n"
                "📝 Cú pháp: /info <link>\n\n"
                "💡 Hỗ trợ:\n"
                "• /info https://facebook.com/username\n"
                "• /info https://instagram.com/username\n"
                "• /info https://tiktok.com/@username")
            return
        link = parts[1].strip()
        uid = message.from_user.id
        fb_mode = "premium" if _fb_can_use_premium(uid) else "basic"
        handle_check_info_full(message, link, fb_mode=fb_mode)
    except Exception as e:
        bot.reply_to(message, f"❌ Lỗi: {e}")

# ==================== KẾT THÚC CHECKINFO ====================


file_locks = {

    "users": threading.Lock(),

    "tracking": threading.Lock(),

    "tracking_tiktok": threading.Lock(),

    "history": threading.Lock(),

    "all_users": threading.Lock(),

    "revenue": threading.Lock(),

    "config": threading.Lock(),

    "codes": threading.Lock(),

    "uid_memory": threading.Lock()

} 



class FacebookProfileExtractor:

    def __init__(self):

        self.base_url = "https://www.facebook.com/profile.php"

        self.mobile_headers = {

            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36",

            'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",

            'Accept-Language': "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",

            'sec-ch-ua-mobile': '?1',

            'sec-ch-ua-platform': '"Android"'

        }

        self.crawler_headers = {

            'User-Agent': "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",

            'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",

            'Accept-Language': "en-US,en;q=0.9"

        }

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



    def extract_profile_info(self, html_content, vanity_url_name=None):

        if vanity_url_name and str(vanity_url_name).strip().isdigit():
            vanity_url_name = None

        title_match = re.search(r'<title>(.*?)</title>', html_content)

        name = title_match.group(1) if title_match else ""

        

        low_name = name.lower()

        bad_terms = ["error", "login", "đăng nhập", "facebook", "vui lòng", "chuyển hướng", "checkpoint"]

        if not name or any(x in low_name for x in bad_terms):

            og_title = re.search(r'property="og:title" content="(.*?)"', html_content)

            if og_title:

                name = og_title.group(1)

            elif vanity_url_name:

                name = vanity_url_name

        

        for suffix in [" | Facebook", " - Log In", " - Đăng nhập", " | Trang chủ", "Facebook - Log In"]:

            if suffix in name: name = name.replace(suffix, "")

        

        if any(x in name.lower() for x in ["login.php", "checkpoint", "đăng nhập", "chuyển hướng"]):

            name = vanity_url_name if vanity_url_name else "Facebook User"



        if not name or len(name) < 2 or any(x in name.lower() for x in ["facebook", "login", "error", "đăng nhập", "chuyển hướng", "checkpoint"]): 

            name = vanity_url_name if vanity_url_name else "Facebook User"



        og_name_match = re.search(r'property="og:title" content="(.*?)"', html_content)

        if og_name_match:

            cand = og_name_match.group(1).replace(" | Facebook", "").replace("Facebook - ", "")

            if len(cand) > 2 and not any(x in cand.lower() for x in ["login", "đăng nhập", "facebook", "error", "checkpoint"]):

                name = cand

        

        if any(x in name.lower() for x in ["login", "đăng nhập", "chuyển hướng", "checkpoint", "error"]):

            name = "Facebook User"



        profile_pic_match = re.search(r'property="og:image" content="([^"]+)"', html_content)

        profile_pic_url = profile_pic_match.group(1) if profile_pic_match else ""

        profile_pic_url = html_module.unescape(profile_pic_url.replace("&amp;", "&"))

        

        cover_match = re.search(r'id="cover_photo_resizer".*?src="([^"]+)"', html_content)
        if not cover_match:
            cover_match = re.search(r'class="cover".*?src="([^"]+)"', html_content)
        if not cover_match:
            cover_match = re.search(r'"coverPhoto".*?"uri":"([^"]+)"', html_content)
        if not cover_match:
            cover_match = re.search(r'"cover_photo".*?"url":"([^"]+)"', html_content)
        cover_url = cover_match.group(1).replace("&amp;", "&").replace("/", "/") if cover_match else ""

        

        followers = "0"

        friends = "0"

        

        json_fol = re.search(r'"follower_count":(\d+)', html_content)

        if json_fol: followers = json_fol.group(1)

        

        json_fri = re.search(r'"friend_count":(\d+)', html_content)

        if json_fri: friends = json_fri.group(1)



        if followers == "0" or friends == "0":

            og_desc_match = re.search(r'property="og:description" content="(.*?)"', html_content)

            if og_desc_match:

                desc = og_desc_match.group(1)

                if followers == "0":

                    fol_match = re.search(r'([\d.,Mk]+)\s*(?:người theo dõi|followers|người follow|subscribers|người đăng ký)', desc, re.I)

                    if fol_match: followers = fol_match.group(1)

                if friends == "0":

                    fri_match = re.search(r'([\d.,Mk]+)\s*(?:bạn bè|friends)', desc, re.I)

                    if fri_match: friends = fri_match.group(1)



        html_clean = re.sub(r'<[^>]*>', ' ', html_content)

        

        if followers == "0":

            for pattern in [

                r'([\d.,Mk]+)\s*(?:người theo dõi|followers|người follow|subscribers|người đăng ký)',

                r'(?:Followed by|Theo dõi bởi|Có)\s*([\d.,Mk]+)\s*(?:người|people|followers)',

                r'([\d.,Mk]+)\s*(?:người khác theo dõi|people follow this)'

            ]:

                m = re.search(pattern, html_clean, re.I)

                if m:

                    followers = m.group(1)

                    break

            

        if friends == "0":

            for pattern in [

                r'([\d.,Mk]+)\s*(?:bạn bè|friends)',

                r'(?:Bạn bè|Friends)\s*\(([\d.,Mk]+)\)',

                r'(\d+)\s*người bạn',

                r'([\d.,Mk]+)\s*(?:bạn bè chung|mutual friends)'

            ]:

                m = re.search(pattern, html_clean, re.I)

                if m:

                    friends = m.group(1)

                    break



        def clean_num(s):

            if not s: return "0"

            s = s.upper().replace(",", "").replace(" ", "")

            if "." in s and not any(x in s for x in ["K", "M"]):

                s = s.replace(".", "")

            

            multi = 1

            if "K" in s:

                multi = 1000

                s = s.replace("K", "")

            if "M" in s:

                multi = 1000000

                s = s.replace("M", "")

            

            try:

                return str(int(float(s) * multi))

            except:

                return "0"



        followers = clean_num(followers)

        friends = clean_num(friends)

        bio = ""
        bio_match = re.search(r'id="bio".*?>(.*?)</div>', html_content, re.DOTALL)
        if bio_match:
            bio = re.sub(r'<.*?>', '', bio_match.group(1)).strip()

        is_verified = False
        if 'alt="Verified"' in html_content or 'alt="Blue Verified Badge"' in html_content or '/e/1f535.png' in html_content:
            is_verified = True

        following = "0"
        json_following = re.search(r'"following_count":(\d+)', html_content)
        if json_following:
            following = json_following.group(1)

        category = ""
        og_desc_match = re.search(r'property="og:description" content="(.*?)"', html_content)
        if og_desc_match:
            desc_raw = html_module.unescape(og_desc_match.group(1))
            if followers == "0":
                fol_m = re.search(
                    r'([\d.,]+[KkMm]?)\s*(?:likes|lượt thích|followers|người theo dõi|subscribers|người đăng ký)',
                    desc_raw, re.I)
                if fol_m:
                    followers = fol_m.group(1)
            if following == "0":
                folw_m = re.search(
                    r'([\d.,]+[KkMm]?)\s*(?:following|đang theo dõi)',
                    desc_raw, re.I)
                if folw_m:
                    following = folw_m.group(1)
            parts = [p.strip() for p in desc_raw.split('.') if p.strip()]
            if len(parts) >= 2:
                last_part = parts[-1]
                if not re.search(r'^\d', last_part) and len(last_part) > 2:
                    category = last_part

        followers = clean_num(followers)
        following = clean_num(following)

        gender = "Không rõ"
        gm = re.search(r'"gender":"(MALE|FEMALE)"', html_content)
        if gm:
            gender = {'MALE': 'Nam', 'FEMALE': 'Nữ'}.get(gm.group(1), 'Không rõ')

        locale = "Không rõ"
        lm = re.search(r'"locale":"([^"]+)"', html_content)
        if lm:
            locale = lm.group(1).replace('_', '-')

        created_time = "Không rõ"
        for m in re.finditer(r'"created_time":(\d{9,11})', html_content):
            try:
                ts = int(m.group(1))
                dt = datetime.utcfromtimestamp(ts)
                if 2004 <= dt.year <= 2030:
                    created_time = dt.strftime('%d/%m/%Y')
                    break
            except Exception:
                pass

        birthday = "Không rõ"
        for m in re.finditer(r'\{"day":(\d{1,2}),"month":(\d{1,2}),"year":(\d{4})\}', html_content):
            try:
                d, mo, y = int(m.group(1)), int(m.group(2)), int(m.group(3))
                if 1 <= mo <= 12 and 1900 <= y <= 2015:
                    birthday = f"{d:02d}/{mo:02d}/{y}"
                    break
            except Exception:
                pass
        if birthday == "Không rõ":
            for m in re.finditer(r'"text":"((?:\\.|[^"\\])*)"', html_content):
                try:
                    t = html_module.unescape(m.group(1))
                    if re.search(r'\b(january|february|march|april|may|june|july|august|september|october|november|december)\b', t, re.I):
                        birthday = t
                        break
                    if re.search(r'sinh nhật|birthday', t, re.I) and re.search(r'\d', t):
                        birthday = t
                        break
                except Exception:
                    pass

        if category and (not bio or bio == og_desc_match.group(1) if og_desc_match else False):
            bio = category



        return {

            "name": html_module.unescape(name) if name else name,

            "avatar": profile_pic_url,

            "cover": cover_url,

            "followers": int(followers) if str(followers).isdigit() else 0,

            "following": int(following) if str(following).isdigit() else 0,

            "friends": int(friends) if str(friends).isdigit() else 0,

            "bio": html_module.unescape(bio) if bio else bio,

            "category": html_module.unescape(category) if category else category,

            "gender": gender,

            "locale": locale,

            "created_time": created_time,

            "birthday": birthday,

            "verified": is_verified,

            "status": "LIVE" if "Tài khoản của bạn đã bị khóa" not in html_content else "DIE"

        }

    

    def get_profile(self, user_id, fallback_name=None, source_link=None):

        try:

            uid = str(user_id).strip()
            norm_link = _normalize_facebook_link(source_link) if source_link else ""
            cookie_string = ""
            cookie_dict = {}
            try:
                cookie_string = _get_fb_cookie_string()
                cookie_dict = _cookie_string_to_dict(cookie_string)
            except Exception:
                pass

            html = None
            fetch_source = None
            urls_all = _facebook_profile_urls(norm_link or uid, include_mbasic=bool(cookie_dict))
            urls_public = _facebook_profile_urls(norm_link or uid, include_mbasic=False)

            if cookie_dict:
                cookie_urls = [u for u in urls_all if "mbasic.facebook.com" in u or "m.facebook.com" in u]
                cookie_urls += [u for u in urls_all if u not in cookie_urls]
                for url in cookie_urls:
                    try:
                        r = requests.get(
                            url,
                            headers=dict(self.mobile_headers),
                            cookies=cookie_dict,
                            timeout=20,
                            allow_redirects=True,
                        )
                        if r.status_code == 200 and r.text and _fb_is_valid_profile_html(r.text):
                            html = r.text
                            fetch_source = "cookie"
                            break
                    except Exception:
                        continue

            if not html:
                for url in urls_public:
                    try:
                        r = requests.get(
                            url,
                            headers=dict(self.crawler_headers),
                            timeout=20,
                            allow_redirects=True,
                        )
                        if r.status_code == 200 and r.text and _fb_is_valid_profile_html(r.text):
                            html = r.text
                            fetch_source = "public"
                            break
                    except Exception:
                        continue

            if html:
                vanity = _extract_facebook_vanity_slug(norm_link)
                if vanity and str(vanity).isdigit():
                    vanity = None
                if not vanity and not uid.isdigit():
                    vanity = uid
                info = self.extract_profile_info(html, vanity_url_name=fallback_name or vanity)
                if info.get('name') in ('Facebook User', '') and fallback_name:
                    info['name'] = fallback_name
                if not info.get('avatar'):
                    av_key = uid if uid.isdigit() else (vanity or uid)
                    info['avatar'] = get_facebook_avatar_url(av_key)
                return info

            api_name = fallback_name
            lookup_link = norm_link or (f"https://www.facebook.com/profile.php?id={uid}" if uid.isdigit()
                                        else f"https://www.facebook.com/{uid}")
            if not api_name:
                try:
                    api_headers = {
                        'accept': 'application/json, text/javascript, */*; q=0.01',
                        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                        'origin': 'https://id.traodoisub.com',
                        'referer': 'https://id.traodoisub.com/',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                    }
                    r_api = requests.post('https://id.traodoisub.com/api.php', headers=api_headers,
                                            data={'link': lookup_link}, timeout=10)
                    if r_api.status_code == 200:
                        js = r_api.json()
                        if js.get("success") == 200 or js.get("code") == 200:
                            api_name = js.get("name")
                except Exception:
                    pass

            final_name = api_name if api_name else "Facebook User"
            av_key = uid if uid.isdigit() else (_extract_facebook_vanity_slug(norm_link) or uid)
            avatar = get_facebook_avatar_url(av_key)

            return {
                "name": final_name,
                "avatar": avatar,
                "followers": 0,
                "following": 0,
                "friends": 0,
                "status": "LIVE",
                "cover": "",
                "bio": "",
                "category": "",
                "gender": "Không rõ",
                "locale": "Không rõ",
                "created_time": "Không rõ",
                "birthday": "Không rõ",
                "verified": False
            }

        except Exception as e:

            return {"error": str(e), "status": "ERROR"}



fb_extractor = FacebookProfileExtractor()



class TikTokProfileChecker:

    def __init__(self):

        self.base_url = "https://www.tiktok.com/@{}"

        self.headers = {

            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',

            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',

            'Accept-Language': 'en-US,en;q=0.5',

            'Connection': 'keep-alive',

            'Upgrade-Insecure-Requests': '1',

        }

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        self.session = create_session_with_retry()

    

    def check_user_exists(self, username):

        username = username.lstrip('@').strip()

        url = self.base_url.format(username)

        

        try:

            response = self.session.get(url, headers=self.headers, timeout=30, allow_redirects=True)

            

            if response.status_code == 404:

                return "NOT_FOUND"

            

            if 'tiktok.com/@' not in response.url or response.url.endswith('tiktok.com/'):

                return "ERROR"

            

            content = response.text

            

            if re.search(r'"(followerCount|followingCount|videoCount|uniqueId)"', content):

                return "EXISTS"

            

            if re.search(r'(couldn\'t find this account|user not found|page not available)', content, re.IGNORECASE):

                return "NOT_FOUND"

            

            return "EXISTS"

            

        except requests.exceptions.Timeout:

            return "ERROR"

        except requests.exceptions.ConnectionError:

            return "ERROR"

        except Exception:

            return "ERROR"

    

    def get_profile(self, username):

        username = username.lstrip('@').strip()

        url = self.base_url.format(username)

        

        try:

            response = self.session.get(url, headers=self.headers, timeout=30, allow_redirects=True)

            if response.status_code == 404:

                return {"error": "User not found", "status": "NOT_FOUND"}

            

            html_content = response.text

            patterns = {

                'user_id': r'"id":"(\d+)","(?:shortId|uniqueId)"',

                'unique_id': r'"uniqueId":"(.*?)"',

                'nickname': r'"nickname":"(.*?)"',

                'followers': r'"followerCount":(\d+)',

                'following': r'"followingCount":(\d+)',

                'likes': r'"heartCount":(\d+)',

                'videos': r'"videoCount":(\d+)',

                'signature': r'"signature":"(.*?)"',

                'verified': r'"verified":(true|false)',

                'secUid': r'"secUid":"(.*?)"',

                'privateAccount': r'"privateAccount":(true|false)',

                'region': r'"region":"([^"]*)"',

                'profile_pic': r'"avatarLarger":"(.*?)"',

                'friendCount': r'"friendCount":(\d+)',

                'diggCount': r'"diggCount":(\d+)'

            }

            

            fallback_patterns = {

                'followers': [r'"stats":{[^}]*"followerCount":(\d+)', r'(\d+) Followers'],

                'likes': [r'"stats":{[^}]*"heartCount":(\d+)', r'(\d+) Likes'],

                'user_id': [r'"userInfo":{"user":{"id":"(\d+)"'],

                'nickname': [r'"nickname":"(.*?)"']

            }

            

            info = {}

            for key, pattern in patterns.items():

                match = re.search(pattern, html_content)

                info[key] = match.group(1) if match else ""

            

            for key, p_list in fallback_patterns.items():

                if not info.get(key):

                    for p in p_list:

                        match = re.search(p, html_content)

                        if match:

                            info[key] = match.group(1)

                            break

            

            if info.get('profile_pic'):

                info['profile_pic'] = info['profile_pic'].replace('\\u002F', '/')

            

            social_links = []

            bio = info.get('signature', "").replace('\\n', '\n')

            

            ig_match = re.search(r'[iI][gG]:\s*@?([a-zA-Z0-9._]+)', bio)

            if ig_match: social_links.append(f"📸 Instagram: @{ig_match.group(1)}")

            

            tele_match = re.search(r'[tT]elegram:\s*@?([a-zA-Z0-9._]+)', bio)

            if tele_match: social_links.append(f"✈️ Telegram: @{tele_match.group(1)}")

            

            email_match = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', bio)

            if email_match: social_links.append(f"📧 Email: {email_match.group(0)}")

            

            bio_link_matches = re.findall(r'"bioLink":{"link":"([^"]+)","risk":\d+}', html_content)

            for link in bio_link_matches:

                clean_link = link.replace('\\u002F', '/')

                if clean_link not in social_links: social_links.append(f"🔗 Link: {clean_link}")



            return {

                "name": info.get('nickname', username),

                "username": info.get('unique_id', username),

                "avatar": info.get('profile_pic', ''),

                "followers": int(info['followers']) if info.get('followers') else 0,

                "videos_count": int(info['videos']) if info.get('videos') else 0,

                "likes": int(info['likes']) if info.get('likes') else 0,

                "verified": info.get('verified') == 'true',

                "private": info.get('privateAccount') == 'true',

                "region": info.get('region', ''),

                "bio": bio,

                "user_id": info.get('user_id', ''),

                "secUid": info.get('secUid', ''),

                "friends": int(info['friendCount']) if info.get('friendCount') else 0,

                "digg": int(info['diggCount']) if info.get('diggCount') else 0,

                "social_links": social_links,

                "status": "EXISTS"

            }

            

        except Exception as e:

            print(f"⚠️ TikTok profile error: {str(e)[:50]}")

            return {"error": str(e), "status": "ERROR"}



tiktok_checker = TikTokProfileChecker()





def load_admins():

    global ADMIN_IDS

    try:

        if os.path.exists(FILES["admins"]):

            with open(FILES["admins"], "r") as f:

                for line in f:

                    uid = line.strip()

                    if uid.isdigit(): ADMIN_IDS.add(int(uid))

    except: pass



def add_new_admin(uid):

    global ADMIN_IDS

    if uid not in ADMIN_IDS:

        ADMIN_IDS.add(uid)

        with open(FILES["admins"], "a") as f: f.write(f"\n{uid}")

        return True

    return False



def load_cookie():

    global FB_COOKIE

    try:

        if os.path.exists(FILES["cookie"]):

            with open(FILES["cookie"], "r", encoding="utf-8") as f:

                FB_COOKIE = f.read().strip()

    except: pass



load_admins()

load_cookie()



_fast_json_cache = {}

def load_json(filename):

    now = time.time()
    if filename in _fast_json_cache and now - _fast_json_cache[filename]["ts"] < 2.0:
        return _fast_json_cache[filename]["data"]

    lock_key = None

    for key, file_path in FILES.items():

        if file_path == filename and key in file_locks:

            lock_key = key

            break

    # Update cache after reading
    if lock_key:
        with file_locks[lock_key]:
            try:
                if os.path.exists(filename):
                    with open(filename, "r", encoding="utf-8") as f: 
                        _fast_json_cache[filename] = {"ts": time.time(), "data": json.load(f)}
                        return _fast_json_cache[filename]["data"]
            except: pass
    else:
        try:
            if os.path.exists(filename):
                with open(filename, "r", encoding="utf-8") as f: 
                    _fast_json_cache[filename] = {"ts": time.time(), "data": json.load(f)}
                    return _fast_json_cache[filename]["data"]
        except: pass

    # Default fallback
    res = [] if filename in [FILES["all_users"], FILES["revenue"], FILES["codes"]] else {}
    _fast_json_cache[filename] = {"ts": time.time(), "data": res}
    return res



def save_json(filename, data):
    _fast_json_cache[filename] = {"ts": time.time(), "data": data}

    lock_key = None

    for key, file_path in FILES.items():

        if file_path == filename and key in file_locks:

            lock_key = key

            break

    

    def _do_save():
        tmp = filename + ".tmp"
        try:
            with open(tmp, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            os.replace(tmp, filename)  # atomic trên Unix/Windows
        except Exception as e:
            try: os.remove(tmp)
            except: pass

    if lock_key:

        with file_locks[lock_key]:

            _do_save()

    else:

        _do_save()



def get_config():

    data = load_json(FILES["config"])

    if not data:

        data = {

            "vip_price_30d": 30000,

            "bank_info": "VietCombank: 1389278236 ( Nguyễn Tùng Anh)",

            "new_user_free_vip_days": 0,

            "required_groups": [],

            "free_features": {}

        }

        save_json(FILES["config"], data)

    if "free_features" not in data:

        data["free_features"] = {}

        save_json(FILES["config"], data)

    

    updated = False

    if "required_groups" not in data:

        old_user = data.get("required_group")

        old_link = data.get("join_group_link")

        if old_user and old_link:

            data["required_groups"] = [{"username": old_user, "link": old_link}]

        else:

            data["required_groups"] = []

        updated = True

    

    if updated:

        save_json(FILES["config"], data)

    return data



def update_config(key, value):

    data = get_config()

    data[key] = value

    save_json(FILES["config"], data)



def init_files():

    for f in FILES.values():

        if f == FILES["cookie"]: continue

        if not os.path.exists(f):

            if f in [FILES["all_users"], FILES["revenue"], FILES["codes"]]: save_json(f, [])

            elif f == FILES["history"]: save_json(f, {})

            elif f.endswith(".txt"):

                with open(f, "w", encoding="utf-8") as file: file.write("") 

            else: save_json(f, {})

    get_config() 



def sync_old_users():

    users_data = load_json(FILES["users"])

    all_users = load_json(FILES["all_users"])

    count = 0

    for uid in users_data:

        try:

            uid_int = int(uid)

            if uid_int not in all_users:

                all_users.append(uid_int)

                count += 1

        except: pass

    if count > 0: save_json(FILES["all_users"], all_users)



init_files()

sync_old_users()



def save_user_global(user_id):

    data = load_json(FILES["all_users"])

    if user_id not in data:

        data.append(user_id)

        save_json(FILES["all_users"], data)

        return True

    return False



def get_all_users_list():

    return load_json(FILES["all_users"])



def log_revenue(amount):

    if amount <= 0: return

    data = load_json(FILES["revenue"])

    data.append({"time": int(time.time()), "amount": amount})

    save_json(FILES["revenue"], data)



def get_admin_revenue_stats():

    data = load_json(FILES["revenue"])

    now = datetime.now()

    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0).timestamp()

    yesterday_start = today_start - 86400

    stats = {"today": 0, "yesterday": 0, "total": 0}

    for rec in data:

        t = rec["time"]; amt = rec["amount"]; stats["total"] += amt

        if t >= today_start: stats["today"] += amt

        if yesterday_start <= t < today_start: stats["yesterday"] += amt

    return stats



def log_user_history(user_id, action_type, amount, detail):

    data = load_json(FILES["history"])

    str_id = str(user_id)

    if str_id not in data: data[str_id] = []

    data[str_id].append({"time": int(time.time()), "type": action_type, "amount": amount, "detail": detail})

    save_json(FILES["history"], data)



def get_user_history(user_id):

    data = load_json(FILES["history"])

    return data.get(str(user_id), [])



def get_user_data(user_id):

    data = load_json(FILES["users"])

    str_id = str(user_id)

    if str_id not in data:

        data[str_id] = {

            "balance": 0, 

            "vip_expiry": 0, 

            "vip_active": False, 

            "level": 1, 

            "received_welcome_gift": False,

            "stats": {"done": 0, "cancel": 0, "tracking": 0, "money_generated": 0}, 

            "active_discount_code": None, 

            "active_bonus_days_code": None, 

            "active_discount_code_time": None, 

            "active_bonus_days_code_time": None, 

            "referral_code": None, 

            "referral_stats": {"total_referrals": 0, "total_earned": 0}, 

            "referral_vip_discount": 0

        }

        save_json(FILES["users"], data)

    

    updated = False

    if "received_welcome_gift" not in data[str_id]:

        data[str_id]["received_welcome_gift"] = False

        updated = True

    if "stats" not in data[str_id]:

        data[str_id]["stats"] = {"done": 0, "cancel": 0, "tracking": 0, "money_generated": 0}

        updated = True

    if "active_discount_code" not in data[str_id]:

        data[str_id]["active_discount_code"] = None

        data[str_id]["active_discount_code_time"] = None

        updated = True

    if "active_bonus_days_code" not in data[str_id]:

        data[str_id]["active_bonus_days_code"] = None

        data[str_id]["active_bonus_days_code_time"] = None

        updated = True

    if "referral_code" not in data[str_id]:

        data[str_id]["referral_code"] = None

        data[str_id]["referral_stats"] = {"total_referrals": 0, "total_earned": 0}

        data[str_id]["referral_vip_discount"] = 0

        updated = True

    

    if updated:

        save_json(FILES["users"], data)

        

    return data[str_id]



def update_user_stats(user_id, type_update, value=0):

    data = load_json(FILES["users"])

    str_id = str(user_id)

    if str_id not in data: return

    stats = data[str_id].get("stats", {"done": 0, "cancel": 0, "tracking": 0, "money_generated": 0})

    if type_update == "done":

        stats["done"] += 1; stats["money_generated"] += value

        if stats["tracking"] > 0: stats["tracking"] -= 1

    elif type_update == "cancel":

        stats["cancel"] += 1

        if stats["tracking"] > 0: stats["tracking"] -= 1

    elif type_update == "add": stats["tracking"] += 1

    data[str_id]["stats"] = stats

    save_json(FILES["users"], data)



def update_balance(user_id, amount):

    data = load_json(FILES["users"])

    str_id = str(user_id)

    if str_id not in data: get_user_data(user_id)

    current = int(data[str_id]["balance"])

    data[str_id]["balance"] = current + amount

    if data[str_id]["balance"] < 0: data[str_id]["balance"] = 0

    save_json(FILES["users"], data)

    if amount > 0: log_revenue(amount)

    return data[str_id]["balance"]



def set_vip(user_id, days):

    data = load_json(FILES["users"])

    str_id = str(user_id)

    now = int(time.time())

    if str_id not in data: 

        get_user_data(user_id)

        data = load_json(FILES["users"])

    current_expiry = data[str_id].get("vip_expiry", 0)

    

    if days == 0: 

        new_expiry = 0

        data[str_id]["vip_active"] = False

        data[str_id]["level"] = 1

    else: 

        if current_expiry > now:

            new_expiry = current_expiry + (days * 86400)

        else:

            new_expiry = now + (days * 86400)

        data[str_id]["vip_active"] = True

        data[str_id]["level"] = 2

        

    data[str_id]["vip_expiry"] = new_expiry

    save_json(FILES["users"], data)

    # Đồng bộ VIP sang Bot Con để user chỉ cần 1 trạng thái VIP dùng cho cả 2
    try:
        sync_vip_to_botcon(user_id, new_expiry)
    except Exception:
        pass

    return new_expiry



def check_vip(user_id):

    if user_id in ADMIN_IDS: return True, "Vĩnh viễn (Admin)"

    data = get_user_data(user_id)

    if not data["vip_active"]: return False, "Chưa kích hoạt"

    if data["vip_expiry"] > int(time.time()):

        dt = datetime.fromtimestamp(data["vip_expiry"])

        return True, dt.strftime('%d/%m/%Y %H:%M:%S')

    else:

        if data["vip_active"]:

            full = load_json(FILES["users"])

            full[str(user_id)]["vip_active"] = False

            full[str(user_id)]["level"] = 1

            save_json(FILES["users"], full)

        return False, "Đã hết hạn"



# ─── Danh sách tính năng có thể bật/tắt free ────────────────────────────────
FEATURE_LABELS = {
    "check_faq":      "🔄 Check FAQ/DIE",
    "them_uid_fb":    "➕ Thêm UID FB",
    "check_meta":     "🌟 Check Meta",
    "check_info":     "📋 Check Info FB (Cơ bản)",
    "check_info_vip": "👑 Check Info FB (Full VIP)",
    "them_tiktok":    "🎵 Thêm TikTok",
    "them_post_fb":   "📘 Thêm Post FB",
    "them_group_fb":  "👥 Thêm Group FB",
    "them_instagram": "📸 Thêm Instagram",
    "them_youtube":   "🎞️ Thêm Youtube",
    "bot_con":        "🤖 Bot Con",
    "get_avatar":     "🖼️ Avatar FB",
    "get_cover":      "🌉 Ảnh Bìa FB",
    "tim_nhac":       "🎵 Tìm Nhạc",
    "ma_2fa":         "🔐 Mã 2FA",
}

def check_access(user_id, feature_key):
    if user_id in ADMIN_IDS:
        return True
    cfg = get_config()
    if cfg.get("free_features", {}).get(feature_key, False):
        return True
    is_vip, _ = check_vip(user_id)
    return is_vip

def _vip_required_msg(chat_id, user_id, feature_label="tính năng này"):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("⭐ Nâng cấp ngay", callback_data="show_vip_info"),
        types.InlineKeyboardButton("🔙 Quay lại Menu", callback_data="back_to_menu")
    )
    bot.send_message(
        chat_id,
        f"⚠️ <b>Tính năng này chỉ dành cho gói VIP</b>\n\n"
        f"Vui lòng nâng cấp để sử dụng tính năng <b>{feature_label}</b>.",
        parse_mode="HTML",
        reply_markup=markup
    )

def require_feature_access_call(call, feature_key, feature_label):
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    if check_access(user_id, feature_key):
        return True
    try:
        bot.answer_callback_query(call.id, "⚠️ Tính năng này chỉ dành cho VIP!", show_alert=True)
    except Exception:
        pass
    _vip_required_msg(chat_id, user_id, feature_label)
    return False

def require_feature_access_message(message, feature_key, feature_label):
    user_id = message.from_user.id
    chat_id = message.chat.id
    if check_access(user_id, feature_key):
        return True
    _vip_required_msg(chat_id, user_id, feature_label)
    return False

def admin_feature_toggle_menu(chat_id, edit_msg_id=None):
    cfg = get_config()
    free = cfg.get("free_features", {})
    text = (
        "<b>⚙️ QUẢN LÝ TÍNH NĂNG FREE/VIP</b>\n\n"
        "🟢 = Miễn phí (ai cũng dùng)\n"
        "🔴 = Chỉ VIP mới dùng"
    )
    markup = types.InlineKeyboardMarkup(row_width=1)
    for key, label in FEATURE_LABELS.items():
        is_free = free.get(key, False)
        icon = "🟢 FREE" if is_free else "🔴 VIP"
        markup.add(types.InlineKeyboardButton(f"{icon}  {label}", callback_data=f"ftoggle_{key}"))
    markup.add(types.InlineKeyboardButton("🟢 Bật FREE tất cả", callback_data="ftoggle_all_free"))
    markup.add(types.InlineKeyboardButton("🔴 Bật VIP tất cả", callback_data="ftoggle_all_vip"))
    markup.add(types.InlineKeyboardButton("🔙 Quay lại Admin", callback_data="open_admin_panel"))
    if edit_msg_id:
        try:
            bot.edit_message_text(text, chat_id, edit_msg_id, parse_mode="HTML", reply_markup=markup)
            return
        except Exception:
            pass
    bot.send_message(chat_id, text, parse_mode="HTML", reply_markup=markup)

def read_prompt_file(prompt_file):

    try:

        with open(prompt_file, "r", encoding="utf-8") as f:

            return f.read()

    except:

        return ""



def get_fixed_menu(user_id=None):
    """Giữ tương thích với các chỗ cũ nhưng không hiện menu bàn phím dưới ô chat."""
    return types.ReplyKeyboardRemove()

def set_bot_commands():

    try:

        bot.set_my_commands([

            types.BotCommand("start", "Khởi động bot"),

            types.BotCommand("menu", "Mở menu chính"),

            types.BotCommand("checkfb", "Check Thông Tin Facebook Full"),

            types.BotCommand("cookie", "Nạp Cookie Admin"),
            types.BotCommand("addytb", "Thêm kênh YouTube theo dõi"),
            types.BotCommand("listytb", "Danh sách kênh YouTube"),
            types.BotCommand("delytb", "Xóa kênh YouTube"),
            types.BotCommand("addfb", "Thêm UID FB nhanh: /addfb uid|ghi chú|giá"),
            types.BotCommand("addpost", "Thêm Post FB theo dõi LIVE/DIE"),
            types.BotCommand("listpost", "Danh sách Post FB đang theo dõi"),
            types.BotCommand("removepost", "Xóa Post FB khỏi theo dõi"),
            types.BotCommand("statuspost", "Check ngay trạng thái Post FB"),

            types.BotCommand("free", "Tặng VIP (Admin)"),

            types.BotCommand("freeall", "Tặng VIP cho tất cả (Admin)"),

            types.BotCommand("panel", "Bảng quản trị (Admin)"),

        ])

    except: pass



def format_vnd(amount):

    try: 

        amount_decimal = Decimal(str(amount))

        amount_int = int(amount_decimal.quantize(Decimal('1'), rounding=ROUND_HALF_UP))

        return f"{amount_int:,}".replace(",", ".") + " VNĐ"

    except: return "0 VNĐ"



def escape_markdown_v2(text):

    """Escape special characters for Telegram MarkdownV2"""

    if not text:

        return ""

    special_chars = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']

    result = str(text)

    for char in special_chars:

        result = result.replace(char, f'\\{char}')

    return result


def html_escape(text):
    if not text:
        return ""
    s = str(text)
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _tg_error_benign(err):
    e = str(err).lower()
    return any(x in e for x in (
        "chat not found", "bot was blocked", "user is deactivated",
        "query is too old", "query id is invalid",
    ))


def _safe_callback_ack(call, text=None, show_alert=False):
    try:
        bot.answer_callback_query(call.id, text=text, show_alert=show_alert)
    except Exception:
        pass


def _user_tracking_stats(user_id):
    cid = str(user_id)
    tracking = get_tracking()
    uids = tracking.get(cid, {})
    active = {k: v for k, v in uids.items() if v.get("status") != "done"}
    live = sum(1 for v in active.values() if v.get("last_check") == "LIVE")
    die = sum(1 for v in active.values() if v.get("last_check") == "DIE")
    return {"total": len(active), "live": live, "die": die}


MENU_CATEGORIES = {
    "tracking": {
        "title": "📌 Theo dõi UID",
        "desc": "Thêm và quản lý UID Facebook đang check.",
        "buttons": [
            ("➕ Thêm UID FB", "add_uid"),
            ("📋 Danh sách UID", "list_uid"),
            ("📊 Thống kê", "stats"),
        ],
    },
    "facebook": {
        "title": "🔵 Công cụ Facebook",
        "desc": "Check meta, info, avatar, bìa, FAQ/DIE.",
        "buttons": [
            ("🌟 Check Meta", "add_meta"),
            ("📋 Check Info FB (Cơ bản)", "check_fb_basic"),
            ("👑 Check Info FB (Full VIP)", "check_fb_vip"),
            ("🖼️ Avatar Facebook", "get_avatar"),
            ("🌉 Ảnh bìa FB", "get_cover"),
            ("🔄 Check FAQ / DIE", "menu_check_faq"),
        ],
    },
    "social": {
        "title": "🎵 TikTok & YouTube",
        "desc": "Theo dõi TikTok và kênh YouTube.",
        "buttons": [
            ("🎵 Thêm TikTok", "add_tiktok"),
            ("🎞️ Thêm YouTube", "add_ytb"),
        ],
    },
    "groups": {
        "title": "👥 Group & Instagram",
        "desc": "Group FB, Instagram, Post FB.",
        "buttons": [
            ("👥 Thêm Group FB", "grig_add_group_inline"),
            ("📸 Thêm Instagram", "grig_add_ig_inline"),
            ("📘 Thêm Post Facebook", "fbpost_open_add"),
        ],
    },
    "account": {
        "title": "🤖 Bot con & Tài khoản",
        "desc": "VIP, bot riêng, mã giới thiệu.",
        "buttons": [
            ("🤖 Bot Con", "botcon_menu"),
            ("👤 Tài khoản", "info_account"),
            ("🎁 Mã giới thiệu", "show_referral"),
            ("💝 Donate", "show_donate"),
        ],
    },
    "tools": {
        "title": "🛠 Tiện ích",
        "desc": "Cookie, support, 2FA, nhạc.",
        "buttons": [
            ("🍪 Nạp Cookie", "help_cookie"),
            ("💬 Chat Support", "start_support"),
            ("🔐 Mã 2FA", "get_2fa"),
            ("🎵 Tìm nhạc", "search_music"),
        ],
    },
}


def admin_stop_all_sub_bots():
    data = botcon_load()
    stopped = 0
    for info in data.values():
        token = info.get("token", "")
        if token and token in _SUB_BOT_STOP_EVENTS:
            try:
                botcon_stop_polling(token)
                stopped += 1
            except Exception:
                pass
    return stopped


def admin_reset_all_tracking():
    save_json(FILES["tracking"], {})
    save_json(FILES["tracking_tiktok"], {})
    save_json(FILES["ytb_channels"], {})
    save_json(FILES["uid_memory"], {})
    if os.path.exists("grig_data.json"):
        save_json("grig_data.json", {})


def admin_reset_all_sub_bots():
    admin_stop_all_sub_bots()
    botcon_save({})


def admin_factory_reset():
    """Reset tracking + bot con + history (giữ user/VIP/số dư)."""
    admin_reset_all_tracking()
    admin_reset_all_sub_bots()
    save_json(FILES["history"], {})


def admin_wipe_all_data():
    """Reset toàn bộ như bot mới — xóa user, UID, bot con, doanh thu."""
    admin_factory_reset()
    save_json(FILES["users"], {})
    save_json(FILES["all_users"], [])
    save_json(FILES["revenue"], [])
    save_json(FILES["codes"], [])
    try:
        with open(FILES["cookie"], "w", encoding="utf-8") as f:
            f.write("")
    except Exception:
        pass
    for cache_dir in ("cache_images", "grig_avatar_cache", "grig_cache"):
        if os.path.isdir(cache_dir):
            for name in os.listdir(cache_dir):
                try:
                    os.remove(os.path.join(cache_dir, name))
                except Exception:
                    pass


def calculate_bonus_with_ai(base_amount, user_id):

    try:

        user_data = get_user_data(user_id)

        active_discount_code = user_data.get("active_discount_code", None)

        referral_vip_discount = user_data.get("referral_vip_discount", 0)

        referral_config = get_referral_config()

        deposit_bonus_percent = referral_config.get("deposit_bonus_percent_new_user", 0)

        today_date = datetime.now().strftime('%Y-%m-%d')

        

        total_bonus_percent = 0

        bonus_sources = []

        

        if active_discount_code:

            code = get_code(active_discount_code)

            if code and code.get("code_type") == "DISCOUNT":

                expiry_date = code.get("expiry_date", "")

                min_amount = code.get("min_amount", 0)

                if (not expiry_date or expiry_date >= today_date) and (min_amount == 0 or base_amount >= min_amount):

                    total_bonus_percent += code.get("value", 0)

                    bonus_sources.append(f"Mã {active_discount_code} ({code.get('value', 0)}%)")

        

        if deposit_bonus_percent > 0 and user_data.get("used_referral"):

            total_bonus_percent += deposit_bonus_percent

            bonus_sources.append(f"Referral bonus ({deposit_bonus_percent}%)")

        

        if total_bonus_percent == 0:

            return {

                "has_bonus": False,

                "base_amount": base_amount,

                "bonus_percent": 0,

                "bonus_amount": 0,

                "total_amount": base_amount,

                "code_name": None,

                "code_valid": False,

                "validation_message": None

            }

        

        code = get_code(active_discount_code)

        if not code or code.get("code_type") != "DISCOUNT":

            user_data["active_discount_code"] = None

            data = load_json(FILES["users"])

            data[str(user_id)] = user_data

            save_json(FILES["users"], data)

            return {

                "has_bonus": False,

                "base_amount": base_amount,

                "bonus_percent": 0,

                "bonus_amount": 0,

                "total_amount": base_amount,

                "code_name": None,

                "code_valid": False,

                "validation_message": "Mã không tồn tại hoặc không hợp lệ"

            }

        

        expiry_date = code.get("expiry_date", "")

        min_amount = code.get("min_amount", 0)

        code_valid = True

        validation_message = "Đạt"

        

        if expiry_date and expiry_date < today_date:

            code_valid = False

            validation_message = f"Không đạt - Mã đã hết hạn ({expiry_date})"

            user_data["active_discount_code"] = None

            data = load_json(FILES["users"])

            data[str(user_id)] = user_data

            save_json(FILES["users"], data)

        elif min_amount > 0 and base_amount < min_amount:

            code_valid = False

            validation_message = f"Không đạt - Số tiền {format_vnd(base_amount)} < Tối thiểu {format_vnd(min_amount)}"

        

        if not code_valid:

            return {

                "has_bonus": False,

                "base_amount": base_amount,

                "bonus_percent": 0,

                "bonus_amount": 0,

                "total_amount": base_amount,

                "code_name": active_discount_code,

                "code_valid": False,

                "validation_message": validation_message

            }

        

        bonus_percent = code.get("value", 0)

        base_decimal = Decimal(str(base_amount))

        bonus_decimal = base_decimal * Decimal(str(bonus_percent)) / Decimal("100")

        bonus_amount = int(bonus_decimal.quantize(Decimal('1'), rounding=ROUND_HALF_UP))

        total_amount = int((base_decimal + bonus_decimal).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

        

        return {

            "has_bonus": True,

            "base_amount": base_amount,

            "bonus_percent": bonus_percent,

            "bonus_amount": bonus_amount,

            "total_amount": total_amount,

            "code_name": active_discount_code,

            "code_valid": True,

            "validation_message": validation_message,

            "min_amount": min_amount,

            "expiry_date": expiry_date

        }

    except:

        return {

            "has_bonus": False,

            "base_amount": base_amount,

            "bonus_percent": 0,

            "bonus_amount": 0,

            "total_amount": base_amount,

            "code_name": None,

            "code_valid": False,

            "validation_message": "Lỗi kiểm tra mã"

        }



def get_user_active_codes(user_id):

    user_data = get_user_data(user_id)

    active_discount = user_data.get("active_discount_code", None)

    active_bonus_days = user_data.get("active_bonus_days_code", None)

    

    discount_code = None

    bonus_days_code = None

    

    if active_discount:

        discount_code = get_code(active_discount)

    

    if active_bonus_days:

        bonus_days_code = get_code(active_bonus_days)

    

    return {

        "discount": discount_code,

        "bonus_days": bonus_days_code

    }



def create_code(code_name, code_type, value, max_uses=100, expiry_days=30, expiry_date=None, min_amount=0):

    codes = load_json(FILES["codes"])

    

    if expiry_date:

        try:

            expiry_datetime = datetime.strptime(expiry_date, '%Y-%m-%d')

            expiry_timestamp = int(expiry_datetime.timestamp())

            expiry_date_str = expiry_date

        except:

            expiry_timestamp = int(time.time()) + (expiry_days * 86400)

            expiry_date_str = datetime.fromtimestamp(expiry_timestamp).strftime('%Y-%m-%d')

    else:

        expiry_timestamp = int(time.time()) + (expiry_days * 86400)

        expiry_date_str = datetime.fromtimestamp(expiry_timestamp).strftime('%Y-%m-%d')

    

    code_entry = {

        "code_name": code_name.upper(),

        "code_type": code_type,

        "value": value,

        "max_uses": max_uses,

        "used_count": 0,

        "used_by": [],

        "expiry": expiry_timestamp,

        "expiry_date": expiry_date_str,

        "min_amount": int(min_amount),

        "created_at": int(time.time()),

        "created_date": datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    }

    codes.append(code_entry)

    save_json(FILES["codes"], codes)

    return code_entry



def get_code(code_name):

    codes = load_json(FILES["codes"])

    code_name_upper = code_name.upper()

    for code in codes:

        if code.get("code_name") == code_name_upper:

            return code

    return None



def use_code(user_id, code_name, check_amount=0):

    codes = load_json(FILES["codes"])

    code_name_upper = code_name.upper()

    now = int(time.time())

    today_date = datetime.now().strftime('%Y-%m-%d')

    

    for code in codes:

        if code.get("code_name") == code_name_upper:

            expiry_date = code.get("expiry_date", "")

            if expiry_date and expiry_date < today_date:

                return {"success": False, "message": f"❌ Mã đã hết hạn. Hạn sử dụng: {expiry_date}"}

            

            if code.get("expiry", 0) < now:

                return {"success": False, "message": "❌ Mã đã hết hạn."}

            

            min_amount = code.get("min_amount", 0)

            if min_amount > 0 and check_amount > 0 and check_amount < min_amount:

                return {"success": False, "message": f"❌ Mã yêu cầu số tiền tối thiểu {format_vnd(min_amount)}. Số tiền của bạn: {format_vnd(check_amount)}"}

            

            if str(user_id) in code.get("used_by", []):

                return {"success": False, "message": "❌ Bạn đã sử dụng mã này rồi."}

            

            if code.get("used_count", 0) >= code.get("max_uses", 0):

                return {"success": False, "message": "❌ Mã đã hết lượt sử dụng."}

            

            code_type = code.get("code_type")

            value = code.get("value", 0)

            

            if code_type == "FREE_VIP":

                code["used_count"] = code.get("used_count", 0) + 1

                if "used_by" not in code:

                    code["used_by"] = []

                code["used_by"].append(str(user_id))

                save_json(FILES["codes"], codes)

                set_vip(user_id, value)

                return {"success": True, "message": f"✅ Đã nhận {value} ngày VIP miễn phí!", "type": "VIP", "value": value, "code_info": code}

            elif code_type == "DISCOUNT":

                user_data = get_user_data(user_id)

                old_code = user_data.get("active_discount_code", None)

                user_data["active_discount_code"] = code_name_upper

                user_data["active_discount_code_time"] = int(time.time())

                data = load_json(FILES["users"])

                data[str(user_id)] = user_data

                save_json(FILES["users"], data)

                old_msg = f"\n\n⚠️ Mã cũ `{old_code}` đã bị thay thế." if old_code and old_code != code_name_upper else ""

                return {"success": True, "message": f"✅ Mã giảm giá {value}% đã được kích hoạt! Mã sẽ tự động áp dụng khi bạn nạp tiền hoặc mua VIP.{old_msg}", "type": "DISCOUNT", "value": value, "code_info": code}

            elif code_type == "BONUS_DAYS":

                user_data = get_user_data(user_id)

                old_code = user_data.get("active_bonus_days_code", None)

                user_data["active_bonus_days_code"] = code_name_upper

                user_data["active_bonus_days_code_time"] = int(time.time())

                data = load_json(FILES["users"])

                data[str(user_id)] = user_data

                save_json(FILES["users"], data)

                old_msg = f"\n\n⚠️ Mã cũ `{old_code}` đã bị thay thế." if old_code and old_code != code_name_upper else ""

                return {"success": True, "message": f"✅ Mã tặng thêm {value} ngày VIP đã được kích hoạt! Mã sẽ tự động áp dụng khi bạn mua VIP.{old_msg}", "type": "BONUS_DAYS", "value": value, "code_info": code}

            elif code_type == "ADD_MONEY":

                code["used_count"] = code.get("used_count", 0) + 1

                if "used_by" not in code:

                    code["used_by"] = []

                code["used_by"].append(str(user_id))

                save_json(FILES["codes"], codes)

                update_balance(user_id, value)

                log_user_history(user_id, "code_reward", value, f"Mã {code_name_upper}")

                return {"success": True, "message": f"✅ Đã nhận {format_vnd(value)} từ mã khuyến mãi!", "type": "MONEY", "value": value, "code_info": code}

            

            return {"success": False, "message": "❌ Loại mã không hợp lệ."}

    

    return {"success": False, "message": "❌ Mã không tồn tại."}



def get_referral_config():

    data = load_json(FILES["config"])

    return data.get("referral_config", {

        "vip_days_referrer": 0,

        "vip_days_new_user": 0,

        "deposit_bonus_percent_referrer": 0,

        "deposit_bonus_percent_new_user": 0,

        "vip_discount_percent": 0

    })



def update_referral_config(config):

    data = load_json(FILES["config"])

    data["referral_config"] = config

    save_json(FILES["config"], data)



def create_user_referral_code(user_id, user_name=""):

    user_data = get_user_data(user_id)

    if not user_data.get("referral_code"):

        referral_code = f"REF{user_id}" if not user_name else f"REF{user_name.upper().replace(' ', '')[:10]}{user_id}"

        user_data["referral_code"] = referral_code

        user_data["referral_stats"] = {"total_referrals": 0, "total_earned": 0}

        data = load_json(FILES["users"])

        data[str(user_id)] = user_data

        save_json(FILES["users"], data)

    return user_data.get("referral_code", str(user_id))



def mass_create_referral_codes(vip_days_referrer=0, vip_days_new_user=0, deposit_bonus_referrer=0, deposit_bonus_new_user=0, vip_discount=0):

    all_users = get_all_users_list()

    config = {

        "vip_days_referrer": vip_days_referrer,

        "vip_days_new_user": vip_days_new_user,

        "deposit_bonus_percent_referrer": deposit_bonus_referrer,

        "deposit_bonus_percent_new_user": deposit_bonus_new_user,

        "vip_discount_percent": vip_discount

    }

    update_referral_config(config)

    

    created_count = 0

    users_data = load_json(FILES["users"])

    

    for user_id in all_users:

        try:

            user_data = users_data.get(str(user_id), {})

            if not user_data.get("referral_code"):

                try:

                    chat_member = bot.get_chat_member(user_id, user_id)

                    user_name = chat_member.user.first_name or ""

                except:

                    user_name = ""

                referral_code = create_user_referral_code(user_id, user_name)

                created_count += 1

        except: pass

    

    save_json(FILES["users"], users_data)

    return created_count, config



def use_referral_code(new_user_id, referral_code_or_uid):

    if str(new_user_id) == str(referral_code_or_uid):

        return {"success": False, "message": "❌ Bạn không thể sử dụng mã giới thiệu của chính mình."}

    

    try:

        referral_uid_int = None

        users_data = load_json(FILES["users"])

        

        if referral_code_or_uid.isdigit():

            referral_uid_int = int(referral_code_or_uid)

        else:

            for uid, user_data in users_data.items():

                if user_data.get("referral_code") == referral_code_or_uid.upper():

                    referral_uid_int = int(uid)

                    break

        

        if not referral_uid_int or referral_uid_int not in get_all_users_list():

            return {"success": False, "message": "❌ Mã giới thiệu không hợp lệ."}

        

        user_data = get_user_data(new_user_id)

        if user_data.get("used_referral"):

            return {"success": False, "message": "❌ Bạn đã sử dụng mã giới thiệu rồi."}

        

        referral_config = get_referral_config()

        

        referrer_data = get_user_data(referral_uid_int)

        referral_code = referrer_data.get("referral_code", str(referral_uid_int))

        

        benefits_msg = []

        total_referrer_benefit = 0

        total_new_user_benefit = 0

        

        if referral_config.get("vip_days_referrer", 0) > 0:

            days = referral_config["vip_days_referrer"]

            set_vip(referral_uid_int, days)

            benefits_msg.append(f"👑 +{days} ngày VIP")

        

        if referral_config.get("vip_days_new_user", 0) > 0:

            days = referral_config["vip_days_new_user"]

            set_vip(new_user_id, days)

            benefits_msg.append(f"👑 +{days} ngày VIP (bạn)")

        

        if referral_config.get("deposit_bonus_percent_referrer", 0) > 0:

            percent = referral_config["deposit_bonus_percent_referrer"]

            benefits_msg.append(f"💰 +{percent}% tiền nạp (người mời)")

        

        if referral_config.get("deposit_bonus_percent_new_user", 0) > 0:

            percent = referral_config["deposit_bonus_percent_new_user"]

            benefits_msg.append(f"💰 +{percent}% tiền nạp (bạn)")

        

        if referral_config.get("vip_discount_percent", 0) > 0:

            percent = referral_config["vip_discount_percent"]

            user_data["referral_vip_discount"] = percent

            benefits_msg.append(f"🎫 Giảm {percent}% khi mua VIP (bạn)")

        

        user_data["used_referral"] = True

        user_data["referral_by"] = referral_uid_int

        user_data["referral_code_used"] = referral_code

        

        if "referral_stats" not in referrer_data:

            referrer_data["referral_stats"] = {"total_referrals": 0, "total_earned": 0}

        referrer_data["referral_stats"]["total_referrals"] = referrer_data["referral_stats"].get("total_referrals", 0) + 1

        

        data = load_json(FILES["users"])

        data[str(new_user_id)] = user_data

        data[str(referral_uid_int)] = referrer_data

        save_json(FILES["users"], data)

        

        log_user_history(new_user_id, "referral_activated", 0, f"Mã giới thiệu: {referral_code}")

        log_user_history(referral_uid_int, "referral_reward", 0, f"Người được giới thiệu: {new_user_id}")

        

        try:

            referrer_msg = f"🎉 **THƯỞNG GIỚI THIỆU!**\n\n"

            referrer_msg += f"Bạn đã có người dùng mã giới thiệu `{referral_code}`!\n\n"

            referrer_msg += f"🎁 **Quyền lợi bạn nhận:**\n"

            if referral_config.get("vip_days_referrer", 0) > 0:

                referrer_msg += f"👑 +{referral_config['vip_days_referrer']} ngày VIP\n"

            if referral_config.get("deposit_bonus_percent_referrer", 0) > 0:

                referrer_msg += f"💰 +{referral_config['deposit_bonus_percent_referrer']}% tiền nạp\n"

            referrer_msg += f"\n📊 Tổng người giới thiệu: {referrer_data['referral_stats']['total_referrals']}"

            bot.send_message(referral_uid_int, referrer_msg, parse_mode="Markdown")

        except: pass

        

        new_user_msg = f"✅ **KÍCH HOẠT MÃ GIỚI THIỆU THÀNH CÔNG!**\n\n"

        new_user_msg += f"🎫 Mã: `{referral_code}`\n\n"

        new_user_msg += f"🎁 **Quyền lợi của bạn:**\n"

        for benefit in benefits_msg:

            if "(bạn)" in benefit or "Giảm" in benefit:

                new_user_msg += f"• {benefit}\n"

        if referral_config.get("vip_days_new_user", 0) > 0:

            new_user_msg += f"\n👑 Bạn đã nhận {referral_config['vip_days_new_user']} ngày VIP!"

        

        return {"success": True, "message": new_user_msg, "referral_code": referral_code, "benefits": benefits_msg}

    except Exception as e:

        return {"success": False, "message": f"❌ Lỗi: {str(e)}"}



def get_uid_from_link(link):

    if "facebook.com" not in link and "fb.com" not in link: return None, None

    try:

        api_headers = {

            'accept': 'application/json, text/javascript, */*; q=0.01',

            'accept-language': 'vi,en-US;q=0.9,en;q=0.8',

            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',

            'origin': 'https://id.traodoisub.com',

            'priority': 'u=1, i',

            'referer': 'https://id.traodoisub.com/',

            'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Microsoft Edge";v="144"',

            'sec-ch-ua-mobile': '?0',

            'sec-ch-ua-platform': '"Windows"',

            'sec-fetch-dest': 'empty',

            'sec-fetch-mode': 'cors',

            'sec-fetch-site': 'same-origin',

            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0',

            'x-requested-with': 'XMLHttpRequest',

        }

        api_data = {'link': link}

        

        r = requests.post('https://id.traodoisub.com/api.php', headers=api_headers, data=api_data, timeout=10)

        if r.status_code == 200:

            js = r.json()

            if js.get("success") == 200 or js.get("code") == 200:

                uid = js.get("id")

                name = js.get("name")

                if uid:

                    return str(uid), name if (name and "login" not in name.lower()) else None

    except: pass

    return None, None



def _normalize_fb_uid_input(uid):
    uid_clean = str(uid).strip()
    if 'profile.php?id=' in uid_clean:
        m = re.search(r'id=(\d+)', uid_clean)
        if m:
            uid_clean = m.group(1)
    elif 'facebook.com/' in uid_clean:
        uid_clean = uid_clean.split('facebook.com/')[-1].split('?')[0].split('/')[0]
    return uid_clean


def _extract_image_url_from_payload(payload, preferred_keys=None, strict_preferred=False):
    if preferred_keys is None:
        preferred_keys = []

    def _looks_like_image_url(s):
        s = (s or '').strip()
        return s.startswith('http') and any(token in s.lower() for token in [
            '.jpg', '.jpeg', '.png', '.webp', '.gif', '/picture', 'fbcdn', 'scontent'
        ])

    def _search_preferred_only(obj):
        if isinstance(obj, dict):
            for key in preferred_keys:
                if key in obj:
                    val = obj.get(key)
                    if isinstance(val, str) and _looks_like_image_url(val):
                        return val
                    found = _search_preferred_only(val)
                    if found:
                        return found
            for value in obj.values():
                found = _search_preferred_only(value)
                if found:
                    return found
        elif isinstance(obj, list):
            for item in obj:
                found = _search_preferred_only(item)
                if found:
                    return found
        elif isinstance(obj, str) and not preferred_keys:
            if _looks_like_image_url(obj):
                return obj
        return None

    def _walk_general(obj):
        ordered_keys = [
            'cover', 'cover_url', 'cover_photo',
            'avatar', 'avatar_url', 'profile_pic', 'profile_picture', 'picture',
            'image', 'image_url', 'img', 'thumb', 'thumbnail',
            'url', 'hd', 'src'
        ]

        if isinstance(obj, str):
            s = obj.strip()
            return s if _looks_like_image_url(s) else None

        if isinstance(obj, dict):
            for key in ordered_keys:
                if key in obj:
                    found = _walk_general(obj.get(key))
                    if found:
                        return found
            for value in obj.values():
                found = _walk_general(value)
                if found:
                    return found

        elif isinstance(obj, list):
            for item in obj:
                found = _walk_general(item)
                if found:
                    return found

        return None

    if strict_preferred and preferred_keys:
        return _search_preferred_only(payload)

    if preferred_keys:
        found = _search_preferred_only(payload)
        if found:
            return found

    return _walk_general(payload)


def _download_image_bytes(source_url, preferred_keys=None, timeout=FAST_API_TIMEOUT):
    headers_dl = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36",
        "Accept": "image/webp,image/apng,image/*,*/*;q=0.8,application/json;q=0.9,text/plain;q=0.8",
    }

    def _is_image_response(resp):
        ct = (resp.headers.get('content-type') or '').lower()
        body = resp.content or b''
        magic = body[:12]
        return (
            'image/' in ct or
            magic[:2] == b'\xff\xd8' or
            magic[:4] == b'\x89PNG' or
            magic[:4] == b'RIFF' or
            magic[:6] in (b'GIF87a', b'GIF89a')
        )

    try:
        r = requests.get(source_url, headers=headers_dl, timeout=timeout, allow_redirects=True)
        ct = (r.headers.get('content-type') or '').lower()
        print(f"[IMG] {source_url[:80]} -> status={r.status_code} ct={ct} size={len(r.content)}")
        if r.status_code != 200 or not r.content:
            return None, None

        if _is_image_response(r):
            return r.content, r.url

        payload = None
        try:
            payload = r.json()
        except Exception:
            try:
                payload = json.loads(r.text)
            except Exception:
                payload = None

        if payload is not None:
            next_url = _extract_image_url_from_payload(payload, preferred_keys=preferred_keys, strict_preferred=bool(preferred_keys and any(k.startswith('cover') or k == 'image' for k in preferred_keys)))
            if next_url and next_url != source_url:
                return _download_image_bytes(next_url, preferred_keys=preferred_keys, timeout=timeout)

    except Exception as e:
        print(f"⚠️ _download_image_bytes loi: {e}")

    return None, None


def get_facebook_avatar_url(uid):
    """Lay URL avatar Facebook qua Graph API, fallback venzfin."""
    try:
        uid_for_api = _normalize_fb_uid_input(uid)
        graph_url = f"https://graph.facebook.com/v3.3/{uid_for_api}/picture?type=large&redirect=0"
        r = requests.get(graph_url, timeout=FAST_AVATAR_TIMEOUT)
        if r.status_code == 200:
            j = r.json()
            pic = (j.get("data") or {}).get("url")
            if pic:
                return pic
        venz_api = f"https://venzfin.io.vn/apifbvenzdev/index.php?input={urllib.parse.quote(uid_for_api)}&key=Venzdev012026"
        _, resolved_url = _download_image_bytes(venz_api, preferred_keys=['avatar', 'avatar_url', 'profile_pic', 'picture'])
        if resolved_url:
            return resolved_url
    except Exception as e:
        print(f"get_facebook_avatar_url loi: {e}")
    return ""


def get_facebook_avatar_bytes(uid):
    """Tai avatar Facebook ve bytes — uu tien Graph API, fallback venzfin."""
    try:
        uid_clean = _normalize_fb_uid_input(uid)
        graph_url = f"https://graph.facebook.com/v3.3/{uid_clean}/picture?type=large"
        try:
            avatar_bytes, _ = _download_image_bytes(graph_url)
            if avatar_bytes:
                return avatar_bytes
        except Exception:
            pass
        venz_api = f"https://venzfin.io.vn/apifbvenzdev/index.php?input={urllib.parse.quote(uid_clean)}&key=Venzdev012026"
        avatar_bytes, _ = _download_image_bytes(venz_api, preferred_keys=['avatar', 'avatar_url', 'profile_pic', 'picture'])
        if avatar_bytes:
            return avatar_bytes
        print(f"Khong lay duoc avatar: {uid_clean}")
    except Exception as e:
        print(f"get_facebook_avatar_bytes loi: {e}")
    return None

def download_die_image():

    """Tải ảnh DIE - ưu tiên mark3.jpg > mark.jpg > link ANHDIE"""

    try:

        # Ưu tiên 1: mark3.jpg
        if os.path.exists(LOCAL_ANH3):

            print(f"✅ Dùng ảnh DIE local: {LOCAL_ANH3}")

            return LOCAL_ANH3

        # Ưu tiên 2: mark.jpg
        if os.path.exists(LOCAL_ANH):

            print(f"✅ Dùng ảnh DIE local fallback: {LOCAL_ANH}")

            return LOCAL_ANH

        # Fallback: tải từ link ANHDIE
        if ANHDIE and ANHDIE.startswith('http'):

            response = requests.get(ANHDIE, timeout=10)

            if response.status_code == 200 and response.headers.get('content-type', '').startswith('image'):

                temp_path = os.path.join(CACHE_DIR, f"die_image_{random.randint(1000,9999)}.jpg")

                with open(temp_path, "wb") as f:

                    f.write(response.content)

                print(f"✅ Đã tải ảnh DIE từ link: {temp_path}")

                return temp_path

        print(f"⚠️ Không tìm thấy ảnh DIE (mark3.jpg / mark.jpg / ANHDIE)")

        return None

    except Exception as e:

        print(f"❌ Lỗi tải ảnh DIE: {str(e)}")

        return None



def download_live_image():

    """Tải ảnh LIVE (Mark sống) - ưu tiên mark1.jpg, fallback ANHLIVE"""

    try:

        # Ưu tiên dùng file local mark1.jpg
        if os.path.exists(LOCAL_ANH1):

            print(f"✅ Dùng ảnh LIVE local: {LOCAL_ANH1}")

            return LOCAL_ANH1

        # Fallback: tải từ link ANHLIVE
        if ANHLIVE and ANHLIVE.startswith('http'):

            response = requests.get(ANHLIVE, timeout=10)

            if response.status_code == 200 and response.headers.get('content-type', '').startswith('image'):

                temp_path = os.path.join(CACHE_DIR, f"live_image_{random.randint(1000,9999)}.jpg")

                with open(temp_path, "wb") as f:

                    f.write(response.content)

                print(f"✅ Đã tải ảnh LIVE từ link: {temp_path}")

                return temp_path

        print(f"⚠️ Không tìm thấy ảnh LIVE (mark1.jpg / ANHLIVE)")

        return None

    except Exception as e:

        print(f"❌ Lỗi tải ảnh LIVE: {str(e)}")

        return None



def cleanup_old_cache_images():

    """Xóa các ảnh cache cũ hơn 1 giờ"""

    try:

        if not os.path.exists(CACHE_DIR):

            return

        

        current_time = time.time()

        deleted_count = 0

        

        for filename in os.listdir(CACHE_DIR):

            if filename.startswith("die_image_") and filename.endswith(".jpg"):

                filepath = os.path.join(CACHE_DIR, filename)

                try:

                    # Xóa file cũ hơn 1 giờ (3600 giây)

                    if os.path.isfile(filepath) and (current_time - os.path.getmtime(filepath)) > 3600:

                        os.remove(filepath)

                        deleted_count += 1

                except Exception as e:

                    print(f"⚠️ Không xóa được {filename}: {e}")

        

        if deleted_count > 0:

            print(f"🧹 Đã dọn dẹp {deleted_count} ảnh cache cũ")

    except Exception as e:

        print(f"⚠️ Lỗi cleanup cache: {str(e)}")



def safe_edit_message(chat_id, message_id, text, reply_markup=None):

    try:

        bot.edit_message_text(text, chat_id, message_id, reply_markup=reply_markup, parse_mode="Markdown")

    except Exception as e:

        error_str = str(e).lower()

        if "there is no text in the message to edit" in error_str:

            try:

                bot.edit_message_caption(text, chat_id, message_id, reply_markup=reply_markup, parse_mode="Markdown")

            except Exception as e2:

                if "can't parse" in str(e2).lower():

                    try: bot.edit_message_caption(text, chat_id, message_id, reply_markup=reply_markup)

                    except: pass

        elif "can't parse" in error_str:

            try:

                bot.edit_message_text(text, chat_id, message_id, reply_markup=reply_markup)

            except: pass

        elif "message is not modified" in error_str:

            pass

        else:

            print(f"⚠️ safe_edit_message error: {str(e)}")



def save_tracking_uid(chat_id, uid, name, note, price, track_type="normal", is_verified=False, initial_status="UNKNOWN", avatar=""):

    data = load_json(FILES["tracking"])

    str_chat_id = str(chat_id)

    if str_chat_id not in data: data[str_chat_id] = {}

    now_ts = int(time.time())
    entry = {
        "name": name, "note": note, "price": price,
        "status": "tracking", "last_check": initial_status,
        "last_notified_status": initial_status,
        "start_time": now_ts,
        "is_verified": is_verified, "track_type": track_type,
        "avatar": avatar
    }
    if initial_status == "DIE":
        entry["die_timestamp"] = now_ts

    data[str_chat_id][str(uid)] = entry

    save_json(FILES["tracking"], data)

    manage_uid_memory(uid, name, initial_status)



def get_tracking():

    return load_json(FILES["tracking"])



def remove_tracking_uid(chat_id, uid):

    data = load_json(FILES["tracking"])

    str_chat_id = str(chat_id)

    if str_chat_id in data and str(uid) in data[str_chat_id]:

        del data[str_chat_id][str(uid)]

        save_json(FILES["tracking"], data)

        return True

    return False



def mark_done_uid(chat_id, uid):

    data = load_json(FILES["tracking"])

    str_chat_id = str(chat_id)

    if str_chat_id in data and str(uid) in data[str_chat_id]:

        data[str_chat_id][str(uid)]["status"] = "done"

        save_json(FILES["tracking"], data)

        return True

    return False



def update_tracking_uid_fields(chat_id, uid, **fields):

    """Cập nhật atomically 1 UID đang theo dõi, tránh ghi đè mất UID mới thêm."""

    data = load_json(FILES["tracking"])

    str_chat_id = str(chat_id)

    str_uid = str(uid)

    if str_chat_id not in data or str_uid not in data[str_chat_id]:

        return None

    for k, v in fields.items():
        if k == "die_timestamp" and v is None:
            data[str_chat_id][str_uid].pop("die_timestamp", None)
        else:
            data[str_chat_id][str_uid][k] = v

    save_json(FILES["tracking"], data)

    return data[str_chat_id][str_uid]



def save_tracking_tiktok(chat_id, username, name, note, price, avatar="", followers=0, verified=False):

    data = load_json(FILES["tracking_tiktok"])

    str_chat_id = str(chat_id)

    if str_chat_id not in data:

        data[str_chat_id] = {}

    

    username = username.lstrip('@').strip()

    data[str_chat_id][username] = {

        "name": name,

        "note": note,

        "price": price,

        "status": "tracking",

        "last_check": "EXISTS",

        "start_time": int(time.time()),

        "avatar": avatar,

        "followers": followers,

        "verified": verified

    }

    save_json(FILES["tracking_tiktok"], data)



def get_tracking_tiktok():

    return load_json(FILES["tracking_tiktok"])



def remove_tracking_tiktok(chat_id, username):

    data = load_json(FILES["tracking_tiktok"])

    str_chat_id = str(chat_id)

    username = username.lstrip('@').strip()

    if str_chat_id in data and username in data[str_chat_id]:

        del data[str_chat_id][username]

        save_json(FILES["tracking_tiktok"], data)

        return True

    return False



def mark_done_tiktok(chat_id, username):

    data = load_json(FILES["tracking_tiktok"])

    str_chat_id = str(chat_id)

    username = username.lstrip('@').strip()

    if str_chat_id in data and username in data[str_chat_id]:

        data[str_chat_id][username]["status"] = "done"

        save_json(FILES["tracking_tiktok"], data)

        return True

    return False





def check_tick_xanh(uid):

    global FB_COOKIE

    try:

        headers_m = {

            "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36",

            "Accept-Language": "en-US,en;q=0.9"

        }

        r_m = requests.get(f"https://mbasic.facebook.com/{uid}", headers=headers_m, timeout=30)

        if 'alt="Verified"' in r_m.text or 'alt="Blue Verified Badge"' in r_m.text: return True

        if '/e/1f535.png' in r_m.text: return True

    except: pass

    return False



def manage_uid_memory(uid, name, status):

    try:

        data = load_json(FILES["uid_memory"])

        if not data: data = {}

        str_uid = str(uid)

        current_time = int(time.time())

        changed = False

        if str_uid not in data:

            data[str_uid] = {

                "name": name if name else f"UID {uid}",

                "last_status": status,

                "timestamp": current_time,

                "start_time": current_time,

                "last_status_change": current_time

            }

            changed = True

        else:

            old_status = data[str_uid].get("last_status")
            old_name = data[str_uid].get("name")

            if name and old_name != name:

                data[str_uid]["name"] = name
                changed = True

            

            if old_status != status:

                data[str_uid]["last_status"] = status

                data[str_uid]["last_status_change"] = current_time
                
                data[str_uid]["timestamp"] = current_time

                changed = True

            

        if changed:
            save_json(FILES["uid_memory"], data)

        return data.get(str_uid, {})

    except:

        return {}



def get_time_diff(timestamp):

    if not timestamp or timestamp == 0:

        return "vừa xong"

    try:

        start_time = datetime.fromtimestamp(timestamp)

        current_time = datetime.now()

        duration = current_time - start_time

        total_seconds = int(duration.total_seconds())

        

        if total_seconds < 60:

            return f"{total_seconds} giây"

            

        days = total_seconds // 86400

        hours = (total_seconds % 86400) // 3600

        minutes = (total_seconds % 3600) // 60

        seconds = total_seconds % 60

        

        parts = []

        if days > 0: parts.append(f"{days} ngày")

        if hours > 0: parts.append(f"{hours} giờ")

        if minutes > 0: parts.append(f"{minutes} phút")

        if seconds > 0 and days == 0 and hours == 0: parts.append(f"{seconds} giây")

        

        if not parts: return "vừa xong"

        return " ".join(parts)

    except:

        return "vừa xong"



def process_chat_request(user, chat_id):

    user_id = user.id

    user_name = user.first_name or "Quý khách"

    if user_id in support_queue: return bot.send_message(chat_id, "⏳ Quý khách đã có trong hàng chờ hỗ trợ. Hệ thống đang kết nối bạn với chuyên viên...")

    support_queue[user_id] = user_name

    bot.send_message(chat_id, "✅ Hệ thống đã nhận yêu cầu hỗ trợ của Quý khách. Chuyên viên sẽ phản hồi trong thời gian sớm nhất.")

    for admin_id in ADMIN_IDS:

        try:

            markup = types.InlineKeyboardMarkup()

            markup.add(types.InlineKeyboardButton(f"💬 Kết nối với Quý khách {user_id}", callback_data=f"connect_{user_id}"))

            bot.send_message(admin_id, f"📞 **YÊU CẦU HỖ TRỢ MỚI**\n👤 Tên: {user_name}\n🆔 ID: `{user_id}`\n\nHệ thống đang chờ chuyên viên kết nối.", reply_markup=markup, parse_mode="Markdown")

        except: pass



def call_feedback_ai(message):

    try:

        user_id = message.from_user.id

        chat_id = message.chat.id

        user_text = message.text

        

        if user_id not in temp_user_state or "history" not in temp_user_state[user_id]:

            temp_user_state[user_id] = {"mode": "feedback_chat", "history": []}

        

        history = temp_user_state[user_id]["history"]

        history.append({"role": "user", "content": user_text})

        

        system_prompt = read_prompt_file(FILES["prompt_feedback_agent"])

        

        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {DEEPSEEK_API_KEY}"}

        data = {

            "model": "deepseek-chat",

            "messages": [{"role": "system", "content": system_prompt}] + history,

            "stream": False

        }

        

        bot.send_chat_action(chat_id, 'typing')

        response = requests.post("https://api.deepseek.com/chat/completions", headers=headers, json=data, timeout=FAST_API_TIMEOUT)

        

        if response.status_code == 200:

            ai_content = response.json()['choices'][0]['message']['content'].strip()

            history.append({"role": "assistant", "content": ai_content})

            

            if ai_content.startswith("REPLY:"):

                reply_text = ai_content.replace("REPLY:", "").strip()

                bot.send_message(chat_id, reply_text)

                

            elif ai_content.startswith("SUMMARY:"):

                summary_text = ai_content.replace("SUMMARY:", "").strip()

                first_name = message.from_user.first_name

                last_name = message.from_user.last_name if message.from_user.last_name else ""

                full_name = f"{first_name} {last_name}".strip()

                username = f"@{message.from_user.username}" if message.from_user.username else "No User"

                

                admin_msg = (f"📩 **BÁO CÁO AI LỄ TÂN**\n"

                             f"👤 {full_name}\n🆔 `{user_id}` | 🔗 {username}\n"

                             f"📝 **Tóm tắt:**\n{summary_text}\n"

                             f"👇 Bấm dưới để trả lời:")

                markup = types.InlineKeyboardMarkup()

                markup.add(types.InlineKeyboardButton(f"💬 Trả lời {first_name}", callback_data=f"admin_reply_{user_id}"))

                bot.send_message(BOSS_ID, admin_msg, reply_markup=markup, parse_mode="Markdown")

                bot.send_message(chat_id, "✅ Cảm ơn bạn! Đã gửi Admin.")

                temp_user_state.pop(user_id, None)

            else:

                bot.send_message(chat_id, ai_content)

    except: bot.send_message(chat_id, "⚠️ Lỗi kết nối AI.")



def execute_ai_command(cmd_data, chat_id):

    try:

        cmd = cmd_data.get("cmd")

        reason = cmd_data.get("reason", "Thông báo hệ thống.")

        if cmd == "give_vip":

            uid = int(cmd_data.get("uid")); days = int(cmd_data.get("days"))

            exp = set_vip(uid, days)
            sync_vip_to_botcon(uid, exp)

            bot.send_message(chat_id, f"✅ Đã cộng {days} ngày VIP cho `{uid}` (bot mẹ + bot con).")

            try: bot.send_message(uid, f"🎁 **QUÀ TẶNG:** +{days} ngày VIP.\n📝 {reason}")

            except: pass

        elif cmd == "give_vip_all":

            days = int(cmd_data.get("days"))

            all_users = get_all_users_list()

            msg = bot.send_message(chat_id, f"⏳ Đang phát VIP...")

            for uid in all_users:

                try:

                    set_vip(uid, days)

                    bot.send_message(uid, f"🎉 **QUÀ TOÀN SERVER:** +{days} ngày VIP.\n📝 {reason}")

                    time.sleep(0.05)

                except: pass

            bot.edit_message_text("✅ Đã phát xong.", chat_id, msg.message_id)

        elif cmd == "remove_vip":

            uid = int(cmd_data.get("uid"))

            set_vip(uid, 0)
            sync_vip_to_botcon(uid, 0)

            bot.send_message(chat_id, f"⛔ Đã xóa VIP `{uid}` cho cả bot mẹ + bot con.")

            try: bot.send_message(uid, f"⚠️ VIP bị thu hồi.\n📝 {reason}")

            except: pass

        elif cmd == "add_money":

            uid = int(cmd_data.get("uid")); amt = int(cmd_data.get("amount"))

            update_balance(uid, amt)

            bot.send_message(chat_id, f"💰 Đã cộng {format_vnd(amt)} cho `{uid}`.")

        elif cmd == "set_price_vip":

            update_config("vip_price_30d", int(cmd_data.get("amount")))

            bot.send_message(chat_id, "✅ Đã đổi giá VIP.")

        elif cmd == "mass_create_referral":

            vip_days_referrer = int(cmd_data.get("vip_days_referrer", 0))

            vip_days_new_user = int(cmd_data.get("vip_days_new_user", 0))

            deposit_bonus_referrer = int(cmd_data.get("deposit_bonus_referrer", 0))

            deposit_bonus_new_user = int(cmd_data.get("deposit_bonus_new_user", 0))

            vip_discount = int(cmd_data.get("vip_discount", 0))

            

            bot.send_message(chat_id, "⏳ Đang tạo mã giới thiệu cho tất cả user...")

            

            def mass_create_async():

                try:

                    created_count, config = mass_create_referral_codes(

                        vip_days_referrer, vip_days_new_user,

                        deposit_bonus_referrer, deposit_bonus_new_user,

                        vip_discount

                    )

                    

                    all_users = get_all_users_list()

                    sent_count = 0

                    

                    benefits_text = []

                    if config["vip_days_referrer"] > 0:

                        benefits_text.append(f"👑 +{config['vip_days_referrer']} ngày VIP")

                    if config["vip_days_new_user"] > 0:

                        benefits_text.append(f"👑 +{config['vip_days_new_user']} ngày VIP (người mới)")

                    if config["deposit_bonus_percent_referrer"] > 0:

                        benefits_text.append(f"💰 +{config['deposit_bonus_percent_referrer']}% tiền nạp")

                    if config["deposit_bonus_percent_new_user"] > 0:

                        benefits_text.append(f"💰 +{config['deposit_bonus_percent_new_user']}% tiền nạp (người mới)")

                    if config["vip_discount_percent"] > 0:

                        benefits_text.append(f"🎫 Giảm {config['vip_discount_percent']}% khi mua VIP (người mới)")

                    

                    benefits_str = "\n".join(benefits_text) if benefits_text else "Quyền lợi đặc biệt"

                    

                    for user_id in all_users:

                        try:

                            user_data = get_user_data(user_id)

                            referral_code = user_data.get("referral_code", str(user_id))

                            referral_link = f"https://t.me/{bot.get_me().username}?start=ref_{referral_code}"

                            

                            try:

                                chat_member = bot.get_chat_member(user_id, user_id)

                                user_name = chat_member.user.first_name or "Bạn"

                            except:

                                user_name = "Bạn"

                            

                            personalized_msg = f"🎉 **CHÚC MỪNG {user_name}!**\n\n"

                            personalized_msg += f"Bạn đã được Admin cấp mã giới thiệu riêng!\n\n"

                            personalized_msg += f"🔑 **Mã của bạn:** `{referral_code}`\n\n"

                            personalized_msg += f"🔗 **Link giới thiệu:**\n`{referral_link}`\n\n"

                            personalized_msg += f"🎁 **Khi bạn bè dùng mã, bạn sẽ nhận:**\n{benefits_str}\n\n"

                            personalized_msg += f"💡 Hãy gửi link này cho bạn bè để nhận thưởng!"

                            

                            markup = types.InlineKeyboardMarkup()

                            markup.add(types.InlineKeyboardButton("📋 Sao chép Link", url=referral_link))

                            

                            bot.send_message(user_id, personalized_msg, reply_markup=markup, parse_mode="Markdown")

                            sent_count += 1

                            time.sleep(0.03)

                        except: pass

                    

                    admin_report = f"✅ **ĐÃ TẠO MÃ GIỚI THIỆU HÀNG LOẠT**\n\n"

                    admin_report += f"📊 Đã tạo: {created_count} mã mới\n"

                    admin_report += f"📤 Đã gửi thông báo: {sent_count} user\n\n"

                    admin_report += f"🎁 **Quyền lợi đã thiết lập:**\n"

                    admin_report += f"👑 Người mời: +{config['vip_days_referrer']} ngày VIP\n"

                    admin_report += f"👑 Người mới: +{config['vip_days_new_user']} ngày VIP\n"

                    admin_report += f"💰 Người mời: +{config['deposit_bonus_percent_referrer']}% tiền nạp\n"

                    admin_report += f"💰 Người mới: +{config['deposit_bonus_percent_new_user']}% tiền nạp\n"

                    admin_report += f"🎫 Người mới: Giảm {config['vip_discount_percent']}% khi mua VIP\n\n"

                    admin_report += f"📝 {reason}"

                    

                    bot.send_message(chat_id, admin_report, parse_mode="Markdown")

                except Exception as e:

                    bot.send_message(chat_id, f"❌ Lỗi: {str(e)}")

            

            threading.Thread(target=mass_create_async, daemon=True).start()

        elif cmd == "create_code":

            code_name = cmd_data.get("code_name", "").upper()

            code_type = cmd_data.get("code_type", "FREE_VIP")

            value = int(cmd_data.get("value", 0))

            max_uses = int(cmd_data.get("max_uses", 100))

            expiry_days = int(cmd_data.get("expiry_days", 30))

            expiry_date = cmd_data.get("expiry_date", None)

            min_amount = int(cmd_data.get("min_amount", 0))

            

            if not code_name:

                bot.send_message(chat_id, "❌ Tên mã không được để trống.")

                return

            

            code_entry = create_code(code_name, code_type, value, max_uses, expiry_days, expiry_date, min_amount)

            

            code_type_text = {

                "FREE_VIP": f"Tặng {value} ngày VIP",

                "DISCOUNT": f"Giảm {value}%",

                "BONUS_DAYS": f"Tặng thêm {value} ngày VIP",

                "ADD_MONEY": f"Tặng {format_vnd(value)}"

            }.get(code_type, code_type)

            

            expiry_date = datetime.fromtimestamp(code_entry["expiry"]).strftime('%d/%m/%Y')

            

            admin_msg = f"✅ **ĐÃ TẠO MÃ THÀNH CÔNG**\n\n"

            admin_msg += f"🎫 **Mã:** `{code_name}`\n"

            admin_msg += f"📦 **Loại:** {code_type_text}\n"

            admin_msg += f"📊 **Số lượt:** {max_uses}\n"

            admin_msg += f"📅 **Hạn dùng:** {expiry_date}\n"

            if code_entry.get("min_amount", 0) > 0:

                admin_msg += f"💰 **Tối thiểu:** {format_vnd(code_entry.get('min_amount', 0))}\n"

            admin_msg += f"\n📝 {reason}"

            

            bot.send_message(chat_id, admin_msg, parse_mode="Markdown")

            

            broadcast_msg = f"🎉 **MÃ KHUYẾN MÃI MỚI!**\n\n"

            broadcast_msg += f"🎫 **Mã:** `{code_name}`\n"

            broadcast_msg += f"🎁 **Quà tặng:** {code_type_text}\n"

            broadcast_msg += f"📊 **Số lượt:** {max_uses}\n"

            broadcast_msg += f"📅 **Hạn dùng:** {expiry_date}\n"

            if code_entry.get("min_amount", 0) > 0:

                broadcast_msg += f"💰 **Tối thiểu:** {format_vnd(code_entry.get('min_amount', 0))}\n"

            broadcast_msg += f"\n💡 Nhập mã ngay để nhận quà!\n\n"

            broadcast_msg += f"📝 {reason}"

            

            markup = types.InlineKeyboardMarkup()

            markup.add(types.InlineKeyboardButton("🎫 Nhập Mã Ngay", callback_data="enter_code"))

            

            all_users = get_all_users_list()

            sent_count = 0

            for uid in all_users:

                try:

                    bot.send_message(uid, broadcast_msg, reply_markup=markup, parse_mode="Markdown")

                    sent_count += 1

                    time.sleep(0.03)

                except: pass

            

            bot.send_message(chat_id, f"✅ Đã gửi thông báo mã mới cho {sent_count} người dùng.")

    except Exception as e: bot.send_message(chat_id, f"❌ Lỗi: {str(e)}")



def call_deepseek_ai(user_id, chat_id, user_text):

    try:

        if user_id in temp_user_state and temp_user_state[user_id].get("mode") == "feedback_chat":

            call_feedback_ai(bot.get_channel_post(chat_id) if False else types.Message(message_id=0, from_user=types.User(user_id, False, "User"), date=0, chat=types.Chat(chat_id, "private"), content_type="text", options={}, json_string="")) 

            return



        is_admin = user_id in ADMIN_IDS

        if is_admin:

            prompt_file = FILES["prompt_code_logic"] if any(keyword in user_text.lower() for keyword in ["tạo mã", "tạo code", "mã khuyến mãi", "voucher", "mã giới thiệu", "referral", "affiliate"]) else FILES["prompt_admin"]

        else:

            prompt_file = FILES["prompt_user_twoface"]

        

        system_prompt = read_prompt_file(prompt_file)

        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {DEEPSEEK_API_KEY}"}

        

        if is_admin and prompt_file == FILES["prompt_code_logic"]:

            system_prompt += "\n\nTrả về JSON với format:\n"

            system_prompt += "Tạo mã khuyến mãi: {\"cmd\": \"create_code\", \"code_name\": \"TENMA\", \"code_type\": \"FREE_VIP|DISCOUNT|BONUS_DAYS|ADD_MONEY\", \"value\": số, \"max_uses\": số, \"expiry_days\": số, \"expiry_date\": \"YYYY-MM-DD\" (tùy chọn), \"min_amount\": số (tùy chọn), \"reason\": \"Lý do\"}\n"

            system_prompt += "Tạo mã giới thiệu hàng loạt: {\"cmd\": \"mass_create_referral\", \"vip_days_referrer\": số, \"vip_days_new_user\": số, \"deposit_bonus_referrer\": số (%), \"deposit_bonus_new_user\": số (%), \"vip_discount\": số (%), \"reason\": \"Lý do\"}\n\n"

            system_prompt += "Chỉ trả về JSON, không thêm text khác."

        

        data = {"model": "deepseek-chat", "messages": [{"role": "system", "content": system_prompt}, {"role": "user", "content": user_text}], "stream": False}

        bot.send_chat_action(chat_id, 'typing')

        response = requests.post("https://api.deepseek.com/chat/completions", headers=headers, json=data, timeout=FAST_API_TIMEOUT)

        if response.status_code == 200:

            content = response.json()['choices'][0]['message']['content'].strip()

            if is_admin and content.startswith("{") and content.endswith("}"):

                try: 

                    cmd_data = json.loads(content)

                    execute_ai_command(cmd_data, chat_id)

                except: bot.send_message(chat_id, content)

            else:

                bot.send_message(chat_id, content)

    except: pass



def ai_create_broadcast(admin_id, topic):

    try:

        system_prompt = read_prompt_file(FILES["thongbao_prompt"])

        prompt_user = f"Viết thông báo về: {topic}. Ngắn gọn, thu hút."

        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {DEEPSEEK_API_KEY}"}

        data = {"model": "deepseek-chat", "messages": [{"role": "system", "content": system_prompt}, {"role": "user", "content": prompt_user}]}

        bot.send_message(admin_id, "✍️ AI đang viết...")

        response = requests.post("https://api.deepseek.com/chat/completions", headers=headers, json=data, timeout=20)

        if response.status_code == 200:

            content = response.json()['choices'][0]['message']['content']

            markup = types.InlineKeyboardMarkup()

            markup.add(types.InlineKeyboardButton("📢 Gửi Thường", callback_data="exec_notify_normal"))

            markup.add(types.InlineKeyboardButton("💌 Gửi & Nhận Feedback", callback_data="exec_notify_feedback"))

            temp_user_state[admin_id] = {"broadcast_content": content}

            bot.send_message(admin_id, f"🔔 **NỘI DUNG:**\n\n{content}\n\n👇 Chọn cách gửi:", reply_markup=markup, parse_mode="Markdown")

    except: pass



def execute_broadcast_final(admin_id, content, mode="normal", photo_id=None):

    raw_users = get_all_users_list()
    all_users = []
    seen = set()
    for uid in raw_users:
        try:
            uid_int = int(uid)
        except Exception:
            continue
        if uid_int in seen:
            continue
        seen.add(uid_int)
        all_users.append(uid_int)

    markup_user = None

    if mode == "feedback":

        markup_user = types.InlineKeyboardMarkup()

        markup_user.add(types.InlineKeyboardButton("💬 Phản hồi cho Admin", callback_data="feedback_reply"))

    total  = len(all_users)
    count  = 0
    failed = 0

    progress_msg = bot.send_message(admin_id, f"📤 Đang gửi... 0/{total}")

    last_edit = time.time()

    for idx, uid in enumerate(all_users, 1):

        try:

            if photo_id:

                caption = f"📢 **THÔNG BÁO:**\n\n{content}\n\n— Admin" if content else "📢 **THÔNG BÁO**\n\n— Admin"
                if len(caption) > 1024:
                    caption = caption[:1020] + "..."
                try:
                    bot.send_photo(uid, photo_id, caption=caption, reply_markup=markup_user, parse_mode="Markdown")
                except Exception:
                    try:
                        bot.send_photo(uid, photo_id, caption=caption, reply_markup=markup_user)
                    except Exception:
                        bot.send_message(uid, caption, reply_markup=markup_user)

            else:

                msg_text = f"📢 **THÔNG BÁO:**\n\n{content}\n\n— Admin"
                try:
                    bot.send_message(uid, msg_text, reply_markup=markup_user, parse_mode="Markdown")
                except Exception:
                    bot.send_message(uid, msg_text, reply_markup=markup_user)

            count += 1

        except Exception:

            failed += 1

        if time.time() - last_edit >= 2:

            try:

                pct = int(idx / total * 100) if total else 100

                bar = "█" * (pct // 10) + "░" * (10 - pct // 10)

                bot.edit_message_text(

                    f"📤 Đang gửi...\n\n[{bar}] {pct}%\n✅ Thành công: {count} | ❌ Lỗi: {failed}\n📊 {idx}/{total}",

                    admin_id, progress_msg.message_id

                )

            except: pass

            last_edit = time.time()

        time.sleep(0.05)

    try:

        bot.edit_message_text(

            f"✅ **GỬI XONG!**\n\n"

            f"📊 Tổng: {total} user\n"

            f"✅ Thành công: {count}\n"

            f"❌ Thất bại: {failed}\n"

            f"📸 Có ảnh: {'Có' if photo_id else 'Không'}\n"

            f"⏰ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}",

            admin_id, progress_msg.message_id, parse_mode="Markdown"

        )

    except:

        bot.send_message(admin_id, f"✅ Đã gửi {count}/{total} người.")


def show_broadcast_menu(chat_id, user_id, edit_msg_id=None):

    markup = types.InlineKeyboardMarkup(row_width=1)

    markup.add(

        types.InlineKeyboardButton("✏️ Gửi Văn Bản", callback_data="broadcast_text_only"),

        types.InlineKeyboardButton("🖼 Gửi Ảnh + Văn Bản", callback_data="broadcast_photo_text"),

        types.InlineKeyboardButton("📸 Gửi Ảnh Không Chú Thích", callback_data="broadcast_photo_only"),

        types.InlineKeyboardButton("🤖 AI Soạn Thông Báo", callback_data="admin_ai_broadcast"),

        types.InlineKeyboardButton("🔙 Quay lại Admin", callback_data="admin_back"),

    )

    txt = (

        "📢 **GỬI THÔNG BÁO TẤT CẢ**\n\n"

        f"👥 Tổng user: **{len(get_all_users_list())}**\n\n"

        "Chọn kiểu gửi:"

    )

    try:

        if edit_msg_id:

            bot.edit_message_text(txt, chat_id, edit_msg_id, reply_markup=markup, parse_mode="Markdown")

        else:

            bot.send_message(chat_id, txt, reply_markup=markup, parse_mode="Markdown")

    except:

        bot.send_message(chat_id, txt, reply_markup=markup, parse_mode="Markdown")



def check_uid_live_die(uid):

    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    ]

    headers = {
        "User-Agent": random.choice(user_agents),
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive"
    }

    # API 1: graph.facebook.com (nhanh nhất) - dùng URL chính, timeout ngắn
    urls = [

        f"https://graph.facebook.com/v3.3/{uid}/picture?redirect=0",

    ]

    for url in urls:

        try:

            r = fb_check_session.get(url, headers=headers, timeout=3, allow_redirects=False)

            if r.status_code in [200, 400]:

                response_text = r.text

                if '"error"' in response_text:
                    return "DIE"
                elif '.gif' in response_text:
                    # Nick bị ẩn/checkpoint trả về ảnh gif 1x1
                    return "DIE"
                elif '"height"' in response_text or '.jpg' in response_text or '.png' in response_text:
                    return "LIVE"
                elif '"is_silhouette"' in response_text or ('"data"' in response_text and '"url"' in response_text):
                    # Fallback cho is_silhouette thật
                    return "LIVE"

        except requests.exceptions.Timeout:

            continue

        except Exception:

            continue

    # API 2: Fallback traodoisub khi graph.facebook.com không trả kết quả rõ ràng

    try:

        _api_headers = {

            'accept': 'application/json, text/javascript, */*; q=0.01',

            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',

            'origin': 'https://id.traodoisub.com',

            'referer': 'https://id.traodoisub.com/',

            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',

        }

        # Dùng fb_check_session thay vì requests.post mặc định để có connection pool
        _r = fb_check_session.post(

            'https://id.traodoisub.com/api.php',

            headers=_api_headers,

            data={'link': f'https://www.facebook.com/{uid}'},

            timeout=5

        )
        if _r.status_code == 200:
            _js = _r.json()
            # traodoisub: success=200/code=200 + có id thực sự → LIVE
            # Có error rõ ràng → DIE
            # Còn lại (không có id, không có error) → UNKNOWN tránh báo DIE giả
            _code = _js.get("success") or _js.get("code")
            _fb_id = str(_js.get("id", "")).strip()
            if _code == 200 and _fb_id and _fb_id not in ("0", "", "None"):
                return "LIVE"
            elif _js.get("error"):  # Chỉ DIE khi có lỗi rõ ràng từ API
                return "DIE"
            # Ngược lại: không rõ → UNKNOWN (tránh false positive)
    except Exception as _e_ts:
        pass  # Không log để tránh spam

    return "UNKNOWN"  # Trả UNKNOWN khi cả 2 API đều lỗi mạng - tránh báo DIE giả




def check_single_uid(uid, info, cid):

    # Chỉ bỏ qua nếu status == "done" (người dùng bấm Done)
    # KHÔNG bỏ qua khi status == "tracking" hoặc bất kỳ giá trị nào khác
    if info.get("status") == "done":

        return None

    try:

        curr_status = check_uid_live_die(uid)

        last_status = info.get("last_check", "UNKNOWN")

        # last_notified_status: trạng thái đã thực sự báo lần cuối
        # Dùng riêng để phát hiện mọi chuyển đổi DIE↔LIVE dù liên tục
        last_notified = info.get("last_notified_status", last_status)
        if last_notified == "UNKNOWN":
            last_notified = last_status

        _mem_before = load_json(FILES["uid_memory"]).get(str(uid), {})
        die_timestamp_saved = _mem_before.get("die_timestamp", 0)
        if not die_timestamp_saved and _mem_before.get("last_status") == "DIE":
            die_timestamp_saved = _mem_before.get("last_status_change", 0)

        mem_info = manage_uid_memory(uid, info.get("name"), curr_status)

        last_status_change = mem_info.get("last_status_change", 0)

        # Remove early return for UNKNOWN so should_update handles it

        # Thông báo khi trạng thái THỰC SỰ thay đổi so với lần báo cuối
        # → Phát hiện mọi chuyển đổi DIE→LIVE hoặc LIVE→DIE liên tục
        should_notify = False
        if curr_status != last_notified and curr_status in ["LIVE", "DIE"]:
            if last_notified in ["LIVE", "DIE"]:
                should_notify = True
            elif last_notified == "UNKNOWN" and curr_status == "DIE":
                should_notify = True

        if should_notify:

            return {

                "uid": uid, "info": info, "cid": cid, 

                "curr": curr_status, "update": True, "notify": True,

                "duration_ts": die_timestamp_saved if die_timestamp_saved else last_status_change,

                "mem_name": mem_info.get("name"),
                "prev_notified": last_notified

            }

        should_update = (curr_status != last_status)

        return {"uid": uid, "info": info, "cid": cid, "curr": curr_status, "update": should_update, "notify": False}

    except Exception as e:

        print(f"⚠️ Lỗi check UID {uid}: {str(e)[:50]}")

        return None



# Cache tên Telegram: tránh gọi bot.get_chat() mỗi lần gửi notification
_tg_name_cache = {}  # {chat_id: (name, timestamp)}
_TG_NAME_CACHE_TTL = 3600  # 1 giờ

def _get_telegram_name(chat_id):
    """Lấy tên Telegram từ cache hoặc API, tránh gọi lặp."""
    now = time.time()
    cached = _tg_name_cache.get(chat_id)
    if cached and now - cached[1] < _TG_NAME_CACHE_TTL:
        return cached[0]
    try:
        chat_info = bot.get_chat(chat_id)
        name = chat_info.first_name or "Bạn"
    except Exception:
        name = "Bạn"
    _tg_name_cache[chat_id] = (name, now)
    return name


def _send_fb_notification(note, data):
    """Gửi thông báo DIE/LIVE lên Telegram ngay lập tức (chạy trong thread riêng)."""
    try:
        chat_id   = int(note["cid"])
        uid_str   = note["uid"]
        curr_status = note["curr"]
        duration_ts = note.get("duration_ts", 0)
        mem_name    = note.get("mem_name", note["info"].get("name", f"UID {uid_str}"))

        if curr_status == "DIE":
            print(f"💀 [CMD NOTIFY] Phát hiện UID DIE: {uid_str} - Gửi thông báo đến Tele: {chat_id}")
        elif curr_status == "LIVE":
            print(f"🎉 [CMD NOTIFY] Phát hiện UID SỐNG LẠI: {uid_str} - Gửi thông báo đến Tele: {chat_id}")

        telegram_name = _get_telegram_name(chat_id)

        # Lấy thời gian bắt đầu theo dõi
        start_time_uid = note["info"].get("start_time", 0)
        if not start_time_uid:
            uid_memory_data = load_json(FILES["uid_memory"])
            uid_info = uid_memory_data.get(str(uid_str), {})
            start_time_uid = uid_info.get("start_time", 0)

        now = int(time.time())

        def _fmt_secs(total_secs):
            if total_secs <= 0:
                return "vừa xong"
            if total_secs < 60:
                return f"{total_secs} giây"
            days    = total_secs // 86400
            hours   = (total_secs % 86400) // 3600
            minutes = (total_secs % 3600) // 60
            seconds = total_secs % 60
            parts = []
            if days > 0:    parts.append(f"{days} ngày")
            if hours > 0:   parts.append(f"{hours} giờ")
            if minutes > 0: parts.append(f"{minutes} phút")
            if seconds > 0 and days == 0 and hours == 0:
                parts.append(f"{seconds} giây")
            return " ".join(parts) if parts else "vừa xong"

        if curr_status == "DIE":
            time_str = _fmt_secs(now - start_time_uid) if start_time_uid else "vừa xong"
        else:
            time_str = _fmt_secs(now - duration_ts) if duration_ts > 0 else "vừa xong"

        name        = note["info"].get("name", "Facebook User")
        note_text   = note["info"].get("note", "")
        price       = note["info"].get("price", 0)
        last_status = note.get("prev_status") or note["info"].get("last_check", "UNKNOWN")

        # Xác định avatar
        avatar_to_send = None
        if curr_status == "DIE" and last_status == "LIVE":
            _die_path = download_die_image()
            if _die_path:
                try:
                    with open(_die_path, 'rb') as _f:
                        avatar_to_send = _f.read()
                    print(f"✅ Gửi ảnh DIE (LIVE→DIE): {_die_path}")
                except Exception as e:
                    print(f"❌ Lỗi đọc ảnh DIE (LIVE→DIE): {str(e)}")

        elif curr_status == "LIVE" and last_status == "DIE":
            _fb_avatar_fetched = None
            _stored_avatar = note["info"].get("avatar", "")
            try:
                _fb_avatar_fetched = get_facebook_avatar_bytes(uid_str)
                if _fb_avatar_fetched:
                    print(f"✅ Lấy avatar MỚI khi SỐNG LẠI: {uid_str}")
                    try:
                        _new_avt_url = f"https://keyherlyswar.x10.mx/Apidocs/tien_ich/avtfb.php?uid={uid_str}"
                        if str(chat_id) in data and uid_str in data[str(chat_id)]:
                            data[str(chat_id)][uid_str]["avatar"] = _new_avt_url
                    except Exception:
                        pass
            except Exception as _e_new_avt:
                print(f"⚠️ Lấy avatar mới lỗi: {_e_new_avt}")

            if not _fb_avatar_fetched and _stored_avatar and isinstance(_stored_avatar, str) and _stored_avatar.startswith("http"):
                try:
                    _av_resp = requests.get(_stored_avatar, timeout=5, allow_redirects=True,
                        headers={"User-Agent": "Mozilla/5.0", "Accept": "image/webp,image/apng,image/*,*/*;q=0.8"})
                    if _av_resp.status_code == 200 and len(_av_resp.content) > 500:
                        _magic = _av_resp.content[:4]
                        _ct = _av_resp.headers.get("content-type", "")
                        _is_img = (_magic[:2] == b'\xff\xd8' or _magic[:4] == b'\x89PNG' or
                                   b'image' in _ct.encode() or
                                   (len(_av_resp.content) > 5000 and b'<html' not in _av_resp.content[:100].lower()))
                        if _is_img:
                            _fb_avatar_fetched = _av_resp.content
                            print(f"✅ Dùng avatar đã lưu (URL fallback): {uid_str}")
                except Exception as _e_av:
                    print(f"⚠️ Tải avatar URL lỗi: {_e_av}")

            try:
                _api_headers = {
                    'accept': 'application/json, text/javascript, */*; q=0.01',
                    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'origin': 'https://id.traodoisub.com',
                    'referer': 'https://id.traodoisub.com/',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                }
                _r = fb_check_session.post('https://id.traodoisub.com/api.php',
                    headers=_api_headers,
                    data={'link': f'https://www.facebook.com/{uid_str}'},
                    timeout=5)
                if _r.status_code == 200:
                    _js = _r.json()
                    if _js.get("success") == 200 or _js.get("code") == 200:
                        _new_name = _js.get("name", "")
                        if _new_name:
                            name = _new_name
            except Exception as _e2:
                print(f"⚠️ traodoisub tên lỗi: {_e2}")

            if _fb_avatar_fetched:
                avatar_to_send = _fb_avatar_fetched
            else:
                _p = LOCAL_ANH1 if os.path.exists(LOCAL_ANH1) else None
                if _p:
                    try:
                        with open(_p, 'rb') as _f:
                            avatar_to_send = _f.read()
                        print(f"✅ Fallback mark1.jpg")
                    except Exception as _ef:
                        print(f"❌ Lỗi đọc mark1.jpg: {str(_ef)}")

            if name and name != "Facebook User":
                try:
                    update_tracking_uid_fields(chat_id, uid_str, name=name)
                except Exception:
                    pass

        else:
            if curr_status == "DIE":
                _die_path = download_die_image()
                if _die_path:
                    try:
                        with open(_die_path, 'rb') as _f:
                            avatar_to_send = _f.read()
                    except Exception:
                        pass
            else:
                avatar_url = note["info"].get("avatar", "")
                avatar_to_send = avatar_url

        # Escape & build HTML caption
        name_h    = html_escape(name)
        uid_h     = html_escape(uid_str)
        note_h    = html_escape(note_text)
        time_h    = html_escape(time_str)
        now_h     = html_escape(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        price_h   = html_escape(f"{price:,}".replace(",", ".") + " VNĐ")
        fb_link   = f"https://www.facebook.com/{uid_str}"

        if curr_status == "LIVE" and last_status == "DIE":
            msg = "🎉 <b>--- ACC SỐNG LẠI! ---</b> 🎉\n\n"
        else:
            msg = ""

        status_icon = "🔴" if curr_status == "DIE" else "🟢"
        status_text = "ĐÃ DIE ❌" if curr_status == "DIE" else "ĐÃ SỐNG LẠI ✅"

        msg += f"📘 {'FACEBOOK LIVE' if curr_status == 'LIVE' else 'FACEBOOK DIE'}\n"
        msg += f"👤 <b>Tên:</b> <tg-spoiler>{name_h}</tg-spoiler>\n"
        msg += f"🔎 <b>UID:</b> <tg-spoiler>{uid_h}</tg-spoiler> — <a href=\"{fb_link}\">Link</a>\n"
        msg += f"{status_icon} <b>Trạng thái:</b> {status_text}\n"
        msg += f"📝 <b>Ghi chú:</b> {note_h}\n"
        msg += f"💵 <b>Giá:</b> <tg-spoiler>{price_h}</tg-spoiler>\n"
        msg += f"⏰ <b>Thời gian:</b> {time_h}\n"
        msg += f"📅 <b>Cập nhật lúc:</b> {now_h}\n"
        msg += f"📊 <b>Tiến trình:</b> Đang Theo Dõi Liên Tục ♾️\n"
        msg += f"👤 <b>Hạn trả kèo:</b> Vĩnh Viễn"

        markup = types.InlineKeyboardMarkup()
        if curr_status == "DIE":
            markup.add(types.InlineKeyboardButton("👁 Theo Dõi Đến Khi Sống Lại 🔔", callback_data=f"keep_{uid_str}"))
            markup.add(
                types.InlineKeyboardButton("✅ Done kèo", callback_data=f"done_{uid_str}"),
                types.InlineKeyboardButton("❌ Hủy theo dõi", callback_data=f"del_{uid_str}")
            )
        else:
            markup.add(types.InlineKeyboardButton("♾️ Đang Theo Dõi Liên Tục ✅", callback_data=f"keep_{uid_str}"))
            markup.add(
                types.InlineKeyboardButton("✅ Done kèo", callback_data=f"done_{uid_str}"),
                types.InlineKeyboardButton("❌ Hủy theo dõi", callback_data=f"del_{uid_str}")
            )

        _use_spoiler = True
        _parse = "HTML"
        if avatar_to_send:
            try:
                if isinstance(avatar_to_send, bytes):
                    bot.send_photo(chat_id, avatar_to_send, caption=msg, reply_markup=markup,
                                   parse_mode=_parse, has_spoiler=_use_spoiler)
                else:
                    bot.send_photo(chat_id, avatar_to_send, caption=msg, reply_markup=markup,
                                   parse_mode=_parse, has_spoiler=_use_spoiler)
            except Exception as e:
                if not _tg_error_benign(e):
                    print(f"❌ Lỗi gửi ảnh: {str(e)}")
                try:
                    bot.send_message(chat_id, msg, reply_markup=markup, parse_mode=_parse)
                except Exception as e2:
                    if not _tg_error_benign(e2):
                        raise
        else:
            try:
                bot.send_message(chat_id, msg, reply_markup=markup, parse_mode=_parse)
            except Exception as e:
                if not _tg_error_benign(e):
                    raise

        # Gửi thông báo qua Bot Con (nếu user có đăng ký)
        try:
            bc_info = botcon_get_user(chat_id)
            if bc_info and bc_info.get("token"):
                bc_token = bc_info["token"]
                is_vip_bc2, _ = botcon_check_vip(chat_id)
                if is_vip_bc2:
                    if curr_status == "DIE":
                        bc_markup = {"inline_keyboard": [
                            [{"text": "👁 Theo Dõi Đến Khi Sống Lại 🔔", "callback_data": f"keep_{uid_str}"}],
                            [{"text": "✅ Done kèo", "callback_data": f"done_{uid_str}"},
                             {"text": "❌ Hủy theo dõi", "callback_data": f"cancel_{uid_str}"}]
                        ]}
                    else:
                        bc_markup = {"inline_keyboard": [
                            [{"text": "♾️ Đang Theo Dõi Liên Tục ✅", "callback_data": f"keep_{uid_str}"}],
                            [{"text": "✅ Done kèo", "callback_data": f"done_{uid_str}"},
                             {"text": "❌ Hủy theo dõi", "callback_data": f"cancel_{uid_str}"}]
                        ]}
                    bc_payload = {"chat_id": chat_id, "caption": msg, "parse_mode": "HTML",
                                  "reply_markup": json.dumps(bc_markup)}
                    bc_url_base = f"https://api.telegram.org/bot{bc_token}"
                    bc_sent = False
                    if avatar_to_send:
                        try:
                            if isinstance(avatar_to_send, bytes):
                                r_bc = requests.post(f"{bc_url_base}/sendPhoto",
                                    data=bc_payload,
                                    files={"photo": ("photo.jpg", avatar_to_send, "image/jpeg")},
                                    timeout=20)
                            else:
                                bc_payload["photo"] = avatar_to_send
                                r_bc = requests.post(f"{bc_url_base}/sendPhoto", json=bc_payload, timeout=20)
                            if r_bc.json().get("ok"):
                                bc_sent = True
                        except Exception as _e_bc:
                            if not _tg_error_benign(_e_bc):
                                print(f"[BotCon] gui anh loi: {_e_bc}")
                    if not bc_sent:
                        requests.post(f"{bc_url_base}/sendMessage", json={
                            "chat_id": chat_id, "text": msg, "parse_mode": "HTML",
                            "reply_markup": json.dumps(bc_markup)
                        }, timeout=FAST_API_TIMEOUT)
        except Exception as _e_bcn:
            if not _tg_error_benign(_e_bcn):
                print(f"[BotCon] notify loi: {_e_bcn}")

    except Exception as e:
        if not _tg_error_benign(e):
            print(f"⚠️ Lỗi gửi notification: {str(e)[:80]}")


def auto_check_thread():

    # 300 workers song song: mỗi task ~1-2s network → 69 UID ~1s, 2000 UID ~7s
    # timeout graph API: 1.5s; fallback traodoisub: 2.5s
    executor = ThreadPoolExecutor(max_workers=300)
    # Thread pool riêng để gửi notification NGAY khi phát hiện, không chặn check loop
    notify_executor = ThreadPoolExecutor(max_workers=20)

    

    check_count = 0

    start_time = time.time()

    last_cleanup_time = time.time()

    

    try:

        while True:

            try:

                # Dọn dẹp cache mỗi 30 phút

                if time.time() - last_cleanup_time > 1800:

                    cleanup_old_cache_images()

                    last_cleanup_time = time.time()

                

                cycle_start = time.time()

                data = load_json(FILES["tracking"])

                if not data:

                    time.sleep(5)

                    continue

                

                tasks = []

                for cid, uids in data.items():

                    for uid, info in uids.items():

                        tasks.append((uid, info.copy(), cid))

                

                if not tasks:

                    time.sleep(5)

                    continue

                

                check_count += len(tasks)

                if check_count % 100 == 0:

                    elapsed = time.time() - start_time

                    rate = check_count / elapsed if elapsed > 0 else 0

                    print(f"📊 Performance: {check_count} checks | {rate:.2f} checks/sec | {len(tasks)} UIDs tracking")

                

                random.shuffle(tasks)

                futures = {executor.submit(check_single_uid, uid, info, cid): (uid, cid) for uid, info, cid in tasks}

                # Timeout hợp lý: tối thiểu 30s, tối đa 300s
                dynamic_timeout = min(300, max(30, len(tasks) * 0.3))

                for future in as_completed(futures, timeout=dynamic_timeout):

                    try:

                        result = future.result(timeout=8)

                        if result:

                            uid = result["uid"]
                            cid = result["cid"]
                            curr = result["curr"]
                            update = result["update"]
                            notify = result["notify"]

                            latest_info = None
                            prev_status_before_update = result.get("prev_notified", "UNKNOWN")

                            if update:
                                fields_to_update = {"last_check": curr}
                                if curr == "DIE":
                                    fields_to_update["die_timestamp"] = int(time.time())
                                elif curr == "LIVE":
                                    fields_to_update["die_timestamp"] = None
                                if notify:
                                    fields_to_update["last_notified_status"] = curr
                                    fields_to_update["status"] = "tracking"
                                latest_info = update_tracking_uid_fields(cid, uid, **fields_to_update)

                            if notify:
                                if latest_info is None:
                                    latest_all = get_tracking()
                                    latest_info = latest_all.get(str(cid), {}).get(str(uid))

                                if latest_info:
                                    note_payload = {
                                        "uid": uid,
                                        "info": latest_info,
                                        "cid": cid,
                                        "curr": curr,
                                        "prev_status": prev_status_before_update,
                                        "duration_ts": result.get("duration_ts", 0),
                                        "mem_name": result.get("mem_name", latest_info.get("name", f"UID {uid}"))
                                    }
                                    # 🚀 GỬI NOTIFICATION NGAY LẬP TỨC - không đợi hết cycle
                                    _data_snapshot = dict(data)
                                    notify_executor.submit(_send_fb_notification, note_payload, _data_snapshot)

                    except Exception as e:

                        print(f"⚠️ Lỗi xử lý future: {str(e)[:50]}")
                        continue


                # [REMOVED] Notification loop đã chạy inline ở trên, không cần loop riêng nữa
                # for note in notifications: (đã xóa - notification được gửi ngay khi phát hiện)
                if False:  # placeholder để giữ indent

                    pass  # notification đã được gửi inline qua notify_executor

                

                cycle_time = time.time() - cycle_start

                print(f"⏱️ Check cycle completed in {cycle_time:.2f}s for {len(tasks)} UIDs")

                

            except Exception as e:

                print(f"⚠️ Lỗi trong check loop: {str(e)[:100]}")

                pass

            

            # Xử lý TikTok check (giữ nguyên)

            try:

                tiktok_data = load_json(FILES["tracking_tiktok"])

                if tiktok_data:

                    tiktok_updated = False

                    for cid, usernames in tiktok_data.items():

                        for username, info in list(usernames.items()):

                            if info.get("status") == "done":

                                continue

                            

                            try:

                                current_status = tiktok_checker.check_user_exists(username)

                                # ── LOGIC CHỐNG BÁO ẢO & LẶP ────────────────────────────
                                # last_check   : trạng thái raw mới nhất từ API
                                # notified_status : trạng thái đã THỰC SỰ BÁO cho user
                                # pending_count   : đếm số lần liên tiếp ra kết quả KHÁC notified_status
                                # Quy tắc:
                                #   - Chỉ báo khi pending_count >= CONFIRM_THRESHOLD
                                #   - Mỗi trạng thái chỉ báo ĐÚNG 1 LẦN (notified_status không đổi cho đến khi thực sự chuyển)
                                #   - Nếu kết quả API dao động về lại notified_status → reset pending_count ngay

                                CONFIRM_THRESHOLD = 3

                                notified = info.get("notified_status", "EXISTS")  # trạng thái đã báo lần cuối
                                pending  = info.get("pending_count", 0)

                                if current_status == notified:
                                    # Kết quả khớp trạng thái đã báo → ổn định, reset đếm nếu cần
                                    if pending != 0:
                                        tiktok_data[cid][username]["pending_count"] = 0
                                        tiktok_data[cid][username]["last_check"] = current_status
                                        tiktok_updated = True
                                    else:
                                        tiktok_data[cid][username]["last_check"] = current_status

                                else:
                                    # Kết quả KHÁC trạng thái đã báo → tăng bộ đếm
                                    pending += 1
                                    tiktok_data[cid][username]["pending_count"] = pending
                                    tiktok_data[cid][username]["last_check"] = current_status
                                    tiktok_updated = True

                                    if pending >= CONFIRM_THRESHOLD:
                                        # Xác nhận đủ lần → cập nhật notified_status, reset đếm, GỬI THÔNG BÁO
                                        tiktok_data[cid][username]["notified_status"] = current_status
                                        tiktok_data[cid][username]["pending_count"] = 0

                                        try:

                                            chat_id = int(cid)

                                            telegram_name = "Bạn"

                                            try:

                                                chat_info = bot.get_chat(chat_id)

                                                telegram_name = chat_info.first_name or "Bạn"

                                            except: pass

                                            tiktok_link = f"https://www.tiktok.com/@{username}"

                                            time_str = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

                                            note  = info.get("note", "")

                                            price = info.get("price", 0)

                                            # ── BÁO DIE ──
                                            if current_status == "NOT_FOUND":

                                                name   = info.get("name", username)

                                                avatar = info.get("avatar", "")

                                                msg  = f"🔴 **DIE RỒI SẾP ƠI {telegram_name}!**\n\n"

                                                msg += f"TikTok @{username} - 🔴 DIE\n"

                                                msg += f"🔗 Link: {tiktok_link}\n"

                                                if info.get("user_id"): msg += f"🆔 ID: `{info['user_id']}`\n"

                                                msg += f"\n👤 Tên: {name}\n"

                                                msg += f"📝 Ghi chú: {note}\n"

                                                msg += f"💵 Giá: {format_vnd(price)}\n"

                                                msg += f"⏰ Thời gian: {time_str}\n\n"

                                                msg += f"(TikTok đã bị xóa hoặc banned)"

                                                markup = types.InlineKeyboardMarkup()

                                                markup.add(

                                                    types.InlineKeyboardButton("✅ Done", callback_data=f"done_tiktok_{username[:50]}"),

                                                    types.InlineKeyboardButton("❌ Hủy", callback_data=f"del_tiktok_{username[:51]}")

                                                )

                                                markup.add(types.InlineKeyboardButton("🔄 Tiếp Tục Theo Dõi", callback_data=f"keep_tiktok_{username}"))

                                                if avatar and avatar.startswith("http"):

                                                    try:

                                                        bot.send_photo(chat_id, avatar, caption=msg, reply_markup=markup)

                                                    except:

                                                        bot.send_message(chat_id, msg, reply_markup=markup)

                                                else:

                                                    bot.send_message(chat_id, msg, reply_markup=markup)

                                            # ── BÁO SỐNG ──
                                            else:

                                                profile = tiktok_checker.get_profile(username)

                                                name   = profile.get("name", info.get("name", username))

                                                avatar = profile.get("avatar", info.get("avatar", ""))

                                                if avatar:

                                                    tiktok_data[cid][username]["avatar"] = avatar

                                                msg  = f"🟢 **SỐNG RỒI SẾP ƠI {telegram_name}!**\n\n"

                                                msg += f"TikTok @{username} - 🟢 LIVE\n"

                                                msg += f"🔗 Link: {tiktok_link}\n"

                                                if profile.get("user_id"): msg += f"🆔 ID: `{profile['user_id']}`\n"

                                                if profile.get("region"): msg += f"🌍 Khu vực: {profile['region']}\n"

                                                msg += f"\n👤 Tên: {name}\n"

                                                msg += f"📊 Follow: {profile.get('followers', 0)} | 🎬 Video: {profile.get('videos_count', 0)}\n"

                                                msg += f"📝 Ghi chú: {note}\n"

                                                msg += f"💵 Giá: {format_vnd(price)}\n"

                                                if profile.get("bio"):

                                                    msg += f"\n📖 **BIO:**\n_{profile['bio']}_\n"

                                                socials = profile.get("social_links", [])

                                                if socials:

                                                    msg += "\n🔗 **SOCIAL LINKS:**\n" + "\n".join(socials) + "\n"

                                                msg += f"\n⏰ Thời gian: {time_str}\n"

                                                if avatar and avatar.startswith("http"):

                                                    try:

                                                        bot.send_photo(chat_id, avatar, caption=msg)

                                                    except:

                                                        bot.send_message(chat_id, msg)

                                                else:

                                                    bot.send_message(chat_id, msg)

                                        except: pass

                                time.sleep(0.1)

                            except: pass

                    

                    if tiktok_updated:

                        save_json(FILES["tracking_tiktok"], tiktok_data)

            except: pass

            

            time.sleep(1)

    finally:

        print("🛑 Shutting down executor...")

        executor.shutdown(wait=False)



@bot.message_handler(commands=['start'])

def send_welcome(message):

    user_id = message.from_user.id

    user_name = message.from_user.first_name or "Bạn"

    chat_id = message.chat.id

    save_user_global(user_id)

    

    user_data = get_user_data(user_id)

    if not user_data.get("received_welcome_gift", False):

        config = get_config()

        required_groups = []

        missing_groups = []

        if required_groups:

            for group in required_groups:

                try:

                    chat_member = bot.get_chat_member(group['username'], user_id)

                    if chat_member.status not in ['member', 'administrator', 'creator']:

                        missing_groups.append(group)

                except:

                    missing_groups.append(group)

        

        if not missing_groups:
            # Đã tắt tự động tặng VIP free cho user mới
            data = load_json(FILES["users"])
            data[str(user_id)]["received_welcome_gift"] = True
            save_json(FILES["users"], data)

            

            gift_msg = f"""👋 **CHÀO MỪNG {user_name}!**

Chúc bạn sử dụng bot vui vẻ.

⚠️ Các chức năng VIP chỉ dùng được khi **Admin cấp VIP** cho bạn.

━━━━━━━━━━━━━━━━━━━━━━━━━━"""

            # Gửi ảnh kèm gift message

            try:

                with open('menu.jpg', 'rb') as photo:

                    bot.send_photo(message.chat.id, photo, caption=gift_msg, parse_mode="Markdown", reply_markup=get_fixed_menu(user_id))

            except FileNotFoundError:

                bot.send_message(message.chat.id, gift_msg, parse_mode="Markdown", reply_markup=get_fixed_menu(user_id))

        else:

            join_msg = f"""👋 **Chào mừng {user_name}!**

Vui lòng tham gia đầy đủ các nhóm sau để tiếp tục sử dụng bot.

"""

            for i, g in enumerate(missing_groups, 1):

                join_msg += f"{i}. 👤 `{g['username']}`\n"

            

            join_msg += "\n⚠️ **Lưu ý:** Chỉ sau khi tham gia **TẤT CẢ** các nhóm, bạn mới được kích hoạt quà tặng."

            

            markup = types.InlineKeyboardMarkup(row_width=1)

            for g in missing_groups:

                markup.add(types.InlineKeyboardButton(f"👥 Tham Gia {g['username']}", url=g['link']))

            

            markup.add(types.InlineKeyboardButton("✅ Tôi Đã Tham Gia Hết", callback_data="verify_join"))

            

            # Gửi ảnh kèm join message

            try:

                with open('menu.jpg', 'rb') as photo:

                    bot.send_photo(message.chat.id, photo, caption=join_msg, reply_markup=markup, parse_mode="Markdown")

            except FileNotFoundError:

                bot.send_message(message.chat.id, join_msg, reply_markup=markup, parse_mode="Markdown")

            return

    

    if message.text and len(message.text.split()) > 1:

        ref_payload = message.text.split()[1]

        if ref_payload.startswith("ref_"):

            ref_code = ref_payload.replace("ref_", "")

            result = use_referral_code(user_id, ref_code)

            if result.get('success'):

                bot.send_message(message.chat.id, result.get('message', '✅ Đã áp dụng mã giới thiệu thành công!'), parse_mode="Markdown")

                user_data = get_user_data(user_id)

                if user_data.get("referral_vip_discount", 0) > 0:

                    bot.send_message(message.chat.id, f"🎫 Bạn cũng được giảm {user_data['referral_vip_discount']}% khi mua VIP!", parse_mode="Markdown")

            else:

                bot.send_message(message.chat.id, result.get('message', '⚠️ Mã giới thiệu không hợp lệ.'))



    show_menu(message)

@bot.message_handler(commands=['checkfb'])

def command_checkfb(message):

    if not require_feature_access_message(message, "check_info", FEATURE_LABELS["check_info"]):
        return

    user_id = message.from_user.id

    chat_id = message.chat.id

    

    parts = message.text.split()

    if len(parts) < 2:

        return bot.reply_to(message, "📝 **Cách dùng:** `/checkfb <link hoặc UID>`", parse_mode="Markdown")

    

    input_data = parts[1].strip()

    uid = input_data

    name_from_link = None

    if not uid.isdigit():

        uid, name_from_link = get_uid_from_link(input_data)

        if not uid:

            return bot.reply_to(message, "❌ Link không hợp lệ hoặc không tìm thấy UID.")

    

    checking_msg = bot.reply_to(message, f"⏳ Đang lấy thông tin Full cho UID `{uid}`...")

    

    profile = fb_extractor.get_profile(uid, fallback_name=name_from_link)

    if profile.get("status") == "ERROR":

        return safe_edit_message(chat_id, checking_msg.message_id, f"❌ Lỗi: {profile.get('error')}")

    

    status_real = check_uid_live_die(uid)

    status_text = "🟢 LIVE" if status_real == "LIVE" else "🔴 DIE"

    verified_text = " (Tích xanh ☑️)" if profile.get("verified") else ""

    

    msg = f"👤 **THÔNG TIN FACEBOOK FULL**\n"

    msg += f"━━━━━━━━━━━━━━━━━━\n"

    msg += f"🆔 UID: `{uid}`\n"

    msg += f"👤 Tên: **{profile.get('name')}**{verified_text}\n"

    msg += f"📊 Follow: **{profile.get('followers', 0):,}**\n"

    msg += f"👥 Bạn bè: **{profile.get('friends', 0):,}**\n"

    msg += f"📈 Trạng thái: **{status_text}**\n"

    if profile.get("bio"):

        msg += f"\n📖 **Tiểu sử:**\n_{profile.get('bio')}_\n"

    

    msg += f"\n🔗 Link: [facebook.com/{uid}](https://www.facebook.com/{uid})\n"

    msg += f"━━━━━━━━━━━━━━━━━━"

    

    media = []

    if profile.get("cover"):

        media.append(types.InputMediaPhoto(profile["cover"], caption=msg if not profile.get("avatar") else None, parse_mode="Markdown"))

    

    if profile.get("avatar"):

        media.append(types.InputMediaPhoto(profile["avatar"], caption=msg, parse_mode="Markdown"))

    

    try:

        if media:

            if len(media) > 1:

                bot.send_media_group(chat_id, media)

            else:

                bot.send_photo(chat_id, media[0].media, caption=media[0].caption, parse_mode="Markdown")

            bot.delete_message(chat_id, checking_msg.message_id)

        else:

            safe_edit_message(chat_id, checking_msg.message_id, msg)

    except Exception as e:

        bot.send_message(chat_id, msg, parse_mode="Markdown")

        print(f"⚠️ CheckFB media error: {e}")





@bot.message_handler(commands=['menu'])

def show_menu(message, edit_msg_id=None):

    user_id = message.from_user.id
    chat_id = message.chat.id

    cfg = get_config()
    groups = cfg.get("required_groups", [])
    primary_link = groups[0].get("link") if groups else "https://t.me/thonbaochecklive_nin"

    msg = (
        "📋 𝗠𝗘𝗡𝗨 • 𝗕𝗢𝗧 𝗖𝗛𝗘𝗖𝗞 𝗟𝗜𝗩𝗘/𝗗𝗜𝗘\n\n"
        "🔵 𝗙𝗔𝗖𝗘𝗕𝗢𝗢𝗞\n"
        "┣ 🔍 Check UID LIVE/DIE\n"
        "┣ ✅ Check Meta Verified\n"
        "┣ 🖼️ Lấy Avatar\n"
        "┣ 🌄 Lấy Ảnh Bìa\n"
        "┣ ℹ️ Xem Thông Tin\n"
        "┗ 🚨 Check FAQ • 282 • 956\n\n"
        "📡 𝗧𝗥𝗔𝗖𝗞𝗜𝗡𝗚\n"
        "┣ 👤 Theo Dõi UID Facebook\n"
        "┣ 🎵 Theo Dõi UID TikTok\n"
        "┣ 👥 Theo Dõi Group Facebook\n"
        "┣ 📷 Theo Dõi Instagram\n"
        "┗ ⚡ Cập Nhật Realtime\n\n"
        "🤖 𝗕𝗢𝗧 𝗥𝗜Ê𝗡𝗚\n"
        "┣ 🔑 Thêm Token BotFather\n"
        "┣ 🔄 Đồng Bộ Dữ Liệu\n"
        "┣ 🔔 Nhận Thông Báo Riêng\n"
        "┗ 🚀 Hoạt Động 24/7\n\n"
        "━━━━━━━━━━━━━━\n"
        "⚙️ Nhanh • Ổn Định • Tự Động\n"
        "━━━━━━━━━━━━━━"
    )

    markup = types.InlineKeyboardMarkup(row_width=1)
    for key, cat in MENU_CATEGORIES.items():
        markup.add(types.InlineKeyboardButton(cat["title"], callback_data=f"menu_cat_{key}"))
    markup.add(types.InlineKeyboardButton("💬 Nhóm hỗ trợ", url=primary_link))
    if user_id in ADMIN_IDS and not _get_subbot_ctx():
        markup.add(types.InlineKeyboardButton("🛡️ Admin Panel", callback_data="open_admin_panel"))

    sent = False
    if edit_msg_id:
        try:
            bot.edit_message_text(msg, chat_id, edit_msg_id, parse_mode="HTML", reply_markup=markup)
            sent = True
        except Exception:
            pass

    if not sent:
        try:
            bot.send_message(chat_id, msg, parse_mode="HTML", reply_markup=markup)
        except Exception:
            bot.send_message(chat_id, msg, reply_markup=markup)


def show_menu_category(chat_id, user_id, category, edit_msg_id=None):
    cat = MENU_CATEGORIES.get(category)
    if not cat:
        return
    msg = f"<b>{html_escape(cat['title'])}</b>\n{html_escape(cat['desc'])}"
    markup = types.InlineKeyboardMarkup(row_width=1)
    for label, cb in cat["buttons"]:
        markup.add(types.InlineKeyboardButton(label, callback_data=cb))
    markup.add(types.InlineKeyboardButton("🔙 Về Menu", callback_data="back_to_menu"))
    if edit_msg_id:
        try:
            bot.edit_message_text(msg, chat_id, edit_msg_id, parse_mode="HTML", reply_markup=markup)
            return
        except Exception:
            pass
    bot.send_message(chat_id, msg, parse_mode="HTML", reply_markup=markup)


def show_admin_reset_menu(chat_id, edit_msg_id=None):
    tracking = load_json(FILES["tracking"])
    uid_count = sum(len(v) for v in tracking.values())
    bot_count = len(botcon_load())
    msg = (
        "<b>🗑 RESET HỆ THỐNG</b>\n\n"
        f"📌 UID đang check: <b>{uid_count}</b>\n"
        f"🤖 Bot con đăng ký: <b>{bot_count}</b>\n\n"
        "⚠️ Thao tác không thể hoàn tác. Chọn mục cần reset:"
    )
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton("🗑 Xóa TẤT CẢ UID đang check", callback_data="admin_reset_confirm_tracking"))
    markup.add(types.InlineKeyboardButton("🤖 Xóa TẤT CẢ Bot con", callback_data="admin_reset_confirm_botcon"))
    markup.add(types.InlineKeyboardButton("💣 Reset toàn bộ (UID + Bot con)", callback_data="admin_reset_confirm_full"))
    markup.add(types.InlineKeyboardButton("🧨 XÓA HẾT — Bot như mới", callback_data="admin_reset_confirm_wipe"))
    markup.add(types.InlineKeyboardButton("🔙 Quay lại Admin", callback_data="open_admin_panel"))
    if edit_msg_id:
        try:
            bot.edit_message_text(msg, chat_id, edit_msg_id, parse_mode="HTML", reply_markup=markup)
            return
        except Exception:
            pass
    bot.send_message(chat_id, msg, parse_mode="HTML", reply_markup=markup)

@bot.message_handler(commands=['admin'])

def admin_panel_command(message):

    if message.from_user.id not in ADMIN_IDS: return

    show_admin_panel(message.chat.id, message.from_user.id)



def show_admin_panel(chat_id, user_id, edit_msg_id=None):

    markup = types.InlineKeyboardMarkup(row_width=2)

    markup.add(

        types.InlineKeyboardButton(f"📋 DS Chờ ({len(support_queue)})", callback_data="admin_view_queue"),

        types.InlineKeyboardButton("📢 Gửi Thông Báo", callback_data="admin_broadcast_menu"),

        types.InlineKeyboardButton("👥 Quản lý User", callback_data="admin_manage_users"),

        types.InlineKeyboardButton("➕ Cộng tiền", callback_data="admin_add_guide"),

        types.InlineKeyboardButton("📊 Doanh Thu", callback_data="admin_stats_full"),

        types.InlineKeyboardButton("📢 Cài đặt Nhóm VIP", callback_data="admin_set_group_config"),

        types.InlineKeyboardButton("🤖 Quản lý Bot Con", callback_data="adminbot_menu"),

        types.InlineKeyboardButton("⚙️ Quản lý Tính Năng", callback_data="admin_features"),

        types.InlineKeyboardButton("🗑 Reset Hệ Thống", callback_data="admin_reset_menu"),

        types.InlineKeyboardButton("❌ Đóng", callback_data="close_panel")

    )

    txt = f"🛡️ <b>ADMIN PANEL</b>\n👑 Admin: <code>{user_id}</code>"

    try:

        if edit_msg_id:

            bot.edit_message_text(txt, chat_id, edit_msg_id, reply_markup=markup, parse_mode="HTML")

        else:

            bot.send_message(chat_id, txt, reply_markup=markup, parse_mode="HTML")

    except Exception:

        bot.send_message(chat_id, txt, reply_markup=markup, parse_mode="HTML")



@bot.message_handler(commands=['ai_thongbao'])

def command_ai_broadcast(message):

    if message.from_user.id not in ADMIN_IDS: return

    topic = message.text.replace("/ai_thongbao", "").strip()

    if not topic: return bot.reply_to(message, "⚠️ Nhập chủ đề.")

    threading.Thread(target=ai_create_broadcast, args=(message.from_user.id, topic), daemon=True).start()



@bot.message_handler(commands=['thongbao'])

def send_broadcast(message):

    if message.from_user.id not in ADMIN_IDS: return

    msg_text = message.text.replace("/thongbao", "").strip() if message.text else ""

    photo_id = None

    

    if message.reply_to_message and message.reply_to_message.photo:

        photo_id = message.reply_to_message.photo[-1].file_id

        if message.reply_to_message.caption:

            msg_text = message.reply_to_message.caption if not msg_text else msg_text

    elif message.photo:

        photo_id = message.photo[-1].file_id

        if message.caption:

            msg_text = message.caption if not msg_text else msg_text

    

    if not msg_text and not photo_id: return bot.reply_to(message, "⚠️ Nhập nội dung hoặc paste/gửi hình ảnh.")

    execute_broadcast_final(message.from_user.id, msg_text, mode="normal", photo_id=photo_id)



@bot.message_handler(commands=['addmoney'])

def admin_add_money(message):

    if message.from_user.id not in ADMIN_IDS: return 

    try:

        _, uid, amount = message.text.split()

        uid = int(uid); amount = int(amount)

        

        bonus_info = calculate_bonus_with_ai(amount, uid)

        

        user_data = get_user_data(uid)

        referral_config = get_referral_config()

        referral_bonus_percent = 0

        if user_data.get("used_referral") and referral_config.get("deposit_bonus_percent_new_user", 0) > 0:

            referral_bonus_percent = referral_config["deposit_bonus_percent_new_user"]

            if bonus_info.get("has_bonus"):

                bonus_info["bonus_percent"] = bonus_info.get("bonus_percent", 0) + referral_bonus_percent

                base_decimal = Decimal(str(amount))

                total_bonus_decimal = base_decimal * Decimal(str(bonus_info["bonus_percent"])) / Decimal("100")

                bonus_info["bonus_amount"] = int(total_bonus_decimal.quantize(Decimal('1'), rounding=ROUND_HALF_UP))

                bonus_info["total_amount"] = int((base_decimal + total_bonus_decimal).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

            else:

                bonus_info["has_bonus"] = True

                bonus_info["bonus_percent"] = referral_bonus_percent

                base_decimal = Decimal(str(amount))

                bonus_decimal = base_decimal * Decimal(str(referral_bonus_percent)) / Decimal("100")

                bonus_info["bonus_amount"] = int(bonus_decimal.quantize(Decimal('1'), rounding=ROUND_HALF_UP))

                bonus_info["total_amount"] = int((base_decimal + bonus_decimal).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

                bonus_info["code_name"] = "Referral Bonus"

                bonus_info["code_valid"] = True

                bonus_info["validation_message"] = "Đạt"

        

        if bonus_info.get("has_bonus") and bonus_info.get("code_valid"):

            admin_msg = f"💰 **YÊU CẦU NẠP TIỀN**\n\n"

            admin_msg += f"👤 User: `{uid}`\n"

            admin_msg += f"💵 Nạp gốc: {format_vnd(bonus_info['base_amount'])}\n"

            admin_msg += f"🎫 Mã áp dụng: `{bonus_info['code_name']}` ({bonus_info['bonus_percent']}%)\n"

            admin_msg += f"📋 Điều kiện đạt: ✅ {bonus_info.get('validation_message', 'Đạt')}\n"

            if bonus_info.get('min_amount', 0) > 0:

                admin_msg += f"   • Tối thiểu: {format_vnd(bonus_info['min_amount'])} | Đạt: ✅\n"

            if bonus_info.get('expiry_date'):

                admin_msg += f"   • Hạn dùng: {bonus_info['expiry_date']} | Đạt: ✅\n"

            admin_msg += f"🎁 Thưởng thêm: {format_vnd(bonus_info['bonus_amount'])}\n"

            admin_msg += f"✅ **Số tiền cuối: {format_vnd(bonus_info['total_amount'])}**\n\n"

            admin_msg += f"👇 Bấm để duyệt:"

            

            markup = types.InlineKeyboardMarkup()

            markup.add(types.InlineKeyboardButton("✅ Duyệt", callback_data=f"approve_deposit_{uid}_{bonus_info['base_amount']}_{bonus_info['total_amount']}"))

            markup.add(types.InlineKeyboardButton("❌ Hủy", callback_data=f"cancel_deposit_{uid}"))

            

            bot.reply_to(message, admin_msg, reply_markup=markup, parse_mode="Markdown")

        elif bonus_info.get("has_bonus") and not bonus_info.get("code_valid"):

            admin_msg = f"⚠️ **MÃ KHÔNG HỢP LỆ**\n\n"

            admin_msg += f"👤 User: `{uid}`\n"

            admin_msg += f"💵 Nạp gốc: {format_vnd(amount)}\n"

            admin_msg += f"🎫 Mã: `{bonus_info.get('code_name', 'N/A')}`\n"

            admin_msg += f"❌ **Điều kiện đạt: {bonus_info.get('validation_message', 'Không đạt')}**\n\n"

            admin_msg += f"💡 Mã đã bị xóa khỏi tài khoản. Nạp tiền bình thường:"

            

            markup = types.InlineKeyboardMarkup()

            markup.add(types.InlineKeyboardButton("✅ Nạp không mã", callback_data=f"approve_deposit_{uid}_{amount}_{amount}"))

            markup.add(types.InlineKeyboardButton("❌ Hủy", callback_data=f"cancel_deposit_{uid}"))

            

            bot.reply_to(message, admin_msg, reply_markup=markup, parse_mode="Markdown")

        else:

            new_bal = update_balance(uid, amount)

            log_user_history(uid, "deposit", amount, "Admin cộng")

            bot.reply_to(message, f"✅ Cộng {format_vnd(amount)} cho `{uid}`.\nDư: {format_vnd(new_bal)}", parse_mode="Markdown")

            try: bot.send_message(uid, f"✅ **CỘNG TIỀN THÀNH CÔNG!**\n💰 +{format_vnd(amount)}\n💵 Số dư: {format_vnd(new_bal)}", parse_mode="Markdown")

            except: pass

    except: bot.reply_to(message, "⚠️ `/addmoney <UID> <TIỀN>`", parse_mode="Markdown")



@bot.message_handler(commands=['setprice'])

def admin_set_price(message):

    if message.from_user.id not in ADMIN_IDS: return

    try:

        _, price = message.text.split()

        update_config("vip_price_30d", int(price))

        bot.reply_to(message, f"✅ Đã đổi giá VIP 1 tháng thành: {format_vnd(price)}")

    except: bot.reply_to(message, "⚠️ Lỗi. Dùng: `/setprice <số_tiền>`")



@bot.message_handler(commands=['setbank'])

def admin_set_bank(message):

    if message.from_user.id not in ADMIN_IDS: return

    try:

        info = message.text.replace("/setbank", "").strip()

        if not info: return bot.reply_to(message, "⚠️ Nhập thông tin bank.")

        update_config("bank_info", info)

        bot.reply_to(message, f"✅ Đã đổi thông tin Bank:\n{info}")

    except: pass



@bot.message_handler(commands=['tangvip'])

def admin_give_vip(message):

    if message.from_user.id not in ADMIN_IDS: return

    try:

        _, uid, days = message.text.split()

        exp = set_vip(int(uid), int(days))
        sync_vip_to_botcon(int(uid), exp)

        bot.reply_to(message, f"✅ Đã tặng VIP {days} ngày cho `{uid}` (bot mẹ + bot con).")

        try: bot.send_message(int(uid), f"🎁 **BẠN ĐƯỢC TẶNG VIP!**\nThời hạn: {days} ngày.")

        except: pass

    except: bot.reply_to(message, "⚠️ Dùng: `/tangvip <UID> <SỐ_NGÀY>`")


@bot.message_handler(commands=['kickvip'])
def admin_kick_vip(message):
    """Admin kích VIP bot mẹ: /kickvip <UID> <SỐ_NGÀY>"""
    if message.from_user.id not in ADMIN_IDS: return
    try:
        parts = message.text.split()
        if len(parts) < 3:
            bot.reply_to(message, "⚠️ Dùng: `/kickvip <UID> <SỐ_NGÀY>`\nVD: `/kickvip 123456 30` → kích 30 ngày VIP", parse_mode="Markdown")
            return
        uid = parts[1]
        days = int(parts[2])
        if days <= 0:
            bot.reply_to(message, "⚠️ Số ngày phải lớn hơn 0!", parse_mode="Markdown")
            return

        data = load_json(FILES["users"])
        str_id = str(uid)
        now = int(time.time())
        if str_id not in data:
            get_user_data(int(uid))
            data = load_json(FILES["users"])

        current_expiry = data[str_id].get("vip_expiry", 0)
        if current_expiry > now:
            new_expiry = current_expiry + (days * 86400)
        else:
            new_expiry = now + (days * 86400)

        data[str_id]["vip_active"] = True
        data[str_id]["level"] = 2
        data[str_id]["vip_expiry"] = new_expiry
        save_json(FILES["users"], data)

        exp_str = datetime.fromtimestamp(new_expiry).strftime('%d/%m/%Y %H:%M:%S')
        bot.reply_to(message,
            f"✅ Đã kích **{days} ngày** VIP cho UID `{uid}`\n"
            f"└ Hết hạn: `{exp_str}`", parse_mode="Markdown")

        try:
            bot.send_message(int(uid),
                f"🎁 **BẠN ĐƯỢC KÍCH VIP!**\nThời hạn: **{days} ngày**\nHết hạn: `{exp_str}`",
                parse_mode="Markdown")
        except: pass

    except ValueError:
        bot.reply_to(message, "⚠️ Số ngày phải là số nguyên!", parse_mode="Markdown")
    except Exception as e:
        bot.reply_to(message, f"❌ Lỗi: {e}")


@bot.message_handler(commands=['xoavip'])
def admin_xoa_vip(message):
    """Admin xóa toàn bộ VIP: /xoavip <UID>"""
    if message.from_user.id not in ADMIN_IDS: return
    try:
        parts = message.text.split()
        if len(parts) < 2:
            bot.reply_to(message, "⚠️ Dùng: `/xoavip <UID>`\nVD: `/xoavip 123456` → xóa toàn bộ VIP", parse_mode="Markdown")
            return
        uid = parts[1]

        data = load_json(FILES["users"])
        str_id = str(uid)
        if str_id not in data:
            bot.reply_to(message, f"❌ Không tìm thấy UID `{uid}` trong hệ thống.", parse_mode="Markdown")
            return

        old_active = data[str_id].get("vip_active", False)
        old_expiry = data[str_id].get("vip_expiry", 0)
        if old_active and old_expiry > 0:
            old_exp_str = datetime.fromtimestamp(old_expiry).strftime('%d/%m/%Y %H:%M:%S')
            vip_cu = f"✅ Hết hạn: {old_exp_str}"
        elif old_active:
            vip_cu = "✅ Đang hoạt động"
        else:
            vip_cu = "❌ Không hoạt động"

        set_vip(int(uid), 0)
        bot.reply_to(message,
            f"🚫 Đã **xóa toàn bộ VIP** của UID `{uid}`\n"
            f"├ VIP cũ: {vip_cu}\n"
            f"└ VIP mới: ❌ Đã xóa sạch (bot mẹ + bot con)", parse_mode="Markdown")

        try:
            bot.send_message(int(uid),
                "⚠️ **THÔNG BÁO VIP**\n\n🚫 VIP của bạn đã bị Admin thu hồi.\nLiên hệ Admin nếu cần hỗ trợ.",
                parse_mode="Markdown")
        except: pass

    except Exception as e:
        bot.reply_to(message, f"❌ Lỗi: {e}")


@bot.message_handler(commands=['free'])

def admin_free_vip(message):

    if message.from_user.id not in ADMIN_IDS: return

    try:

        _, uid, days = message.text.split()

        exp = set_vip(int(uid), int(days))
        sync_vip_to_botcon(int(uid), exp)

        try:

            chat_member = bot.get_chat_member(int(uid), int(uid))

            user_name = chat_member.user.first_name or "Bạn"

        except:

            user_name = "Bạn"

        

        bot.reply_to(message, f"✅ Đã tặng FREE {days} ngày VIP cho `{uid}` ({user_name}).", parse_mode="Markdown")

        

        try:

            user_msg = f"""🎉 **CHÚC MỪNG {user_name.upper()}!**



🎁 Bạn được tặng **{days} ngày VIP MIỄN PHÍ** từ Admin!



👑 **ƯU ĐÃI VIP:**

✅ Không giới hạn số lượng UID theo dõi

✅ Hỗ trợ ưu tiên 24/7

✅ Tính năng đặc biệt dành riêng cho VIP



⏰ **Thời hạn:** {days} ngày

📅 **Bắt đầu:** Ngay bây giờ



💬 Cảm ơn bạn đã sử dụng dịch vụ!

━━━━━━━━━━━━━━━━━━━━━━━━━━"""

            bot.send_message(int(uid), user_msg, parse_mode="Markdown")

        except:

            pass

        

        log_user_history(int(uid), "free_vip", 0, f"Admin tặng {days} ngày VIP miễn phí")

        

    except:

        bot.reply_to(message, "⚠️ **Cách dùng:** `/free <UID> <SỐ_NGÀY>`\n\n**Ví dụ:** `/free 123456789 30`", parse_mode="Markdown")



@bot.message_handler(commands=['freeall'])

def admin_free_vip_all(message):

    if message.from_user.id not in ADMIN_IDS: return

    try:

        parts = message.text.split()

        if len(parts) < 2:

            bot.reply_to(message, "⚠️ **Cách dùng:** `/freeall <SỐ_NGÀY>`\n\n**Ví dụ:** `/freeall 7` - Tặng 7 ngày VIP cho tất cả thành viên", parse_mode="Markdown")

            return

        

        days = int(parts[1])

        

        all_users = get_all_users_list()

        

        if not all_users:

            bot.reply_to(message, "❌ Không có user nào trong hệ thống.")

            return

        

        confirm_msg = f"⚠️ **XÁC NHẬN TẶNG VIP CHO TẤT CẢ**\n\n"

        confirm_msg += f"📊 Tổng số user: **{len(all_users)}**\n"

        confirm_msg += f"🎁 Số ngày VIP: **{days} ngày**\n\n"

        confirm_msg += f"Bạn có chắc chắn muốn tặng {days} ngày VIP cho tất cả {len(all_users)} thành viên?\n\n"

        confirm_msg += f"Gửi lại lệnh `/freeall {days} confirm` để xác nhận."

        

        if len(parts) < 3 or parts[2] != "confirm":

            bot.reply_to(message, confirm_msg, parse_mode="Markdown")

            return

        

        processing_msg = bot.reply_to(message, f"⏳ **BẮT ĐẦU TẶNG VIP...**\n\n📊 Đang xử lý {len(all_users)} user...", parse_mode="Markdown")

        

        success_count = 0

        fail_count = 0

        admin_count = 0

        

        for idx, uid in enumerate(all_users, 1):

            try:

                if uid in ADMIN_IDS:

                    admin_count += 1

                    continue

                

                set_vip(uid, days)

                

                try:

                    chat_member = bot.get_chat_member(uid, uid)

                    user_name = chat_member.user.first_name or "Bạn"

                except:

                    user_name = "Bạn"

                

                try:

                    user_msg = f"""🎉 **CHÚC MỪNG {user_name.upper()}!**



🎁 Bạn được tặng **{days} ngày VIP MIỄN PHÍ** từ Admin!



👑 **ƯU ĐÃI VIP:**

✅ Không giới hạn số lượng UID theo dõi

✅ Hỗ trợ ưu tiên 24/7

✅ Tính năng đặc biệt dành riêng cho VIP



⏰ **Thời hạn:** {days} ngày

📅 **Bắt đầu:** Ngay bây giờ



💬 Cảm ơn bạn đã sử dụng dịch vụ!

━━━━━━━━━━━━━━━━━━━━━━━━━━"""

                    bot.send_message(uid, user_msg, parse_mode="Markdown")

                    success_count += 1

                except:

                    success_count += 1

                    fail_count += 1

                

                log_user_history(uid, "free_vip_all", 0, f"Admin tặng {days} ngày VIP miễn phí (Mass gift)")

                

                if idx % 10 == 0:

                    try:

                        progress_text = f"⏳ **ĐANG XỬ LÝ...**\n\n"

                        progress_text += f"📊 Tiến độ: {idx}/{len(all_users)}\n"

                        progress_text += f"✅ Thành công: {success_count}\n"

                        progress_text += f"⏭️ Bỏ qua Admin: {admin_count}"

                        bot.edit_message_text(progress_text, message.chat.id, processing_msg.message_id, parse_mode="Markdown")

                    except:

                        pass

                

                time.sleep(0.05)

                

            except Exception as e:

                fail_count += 1

                continue

        

        summary_msg = f"""✅ **HOÀN THÀNH TẶNG VIP!**



📊 **THỐNG KÊ:**

━━━━━━━━━━━━━━━━━━━━━━━━━━

👥 Tổng user: {len(all_users)}

✅ Đã tặng VIP: {success_count}

⏭️ Bỏ qua Admin: {admin_count}

❌ Thất bại: {fail_count}



🎁 **Số ngày VIP:** {days} ngày

⏰ **Thời gian:** {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}



💬 Tất cả thành viên đã nhận được VIP miễn phí!

━━━━━━━━━━━━━━━━━━━━━━━━━━"""

        

        bot.edit_message_text(summary_msg, message.chat.id, processing_msg.message_id, parse_mode="Markdown")

        

    except ValueError:

        bot.reply_to(message, "❌ Số ngày phải là một số nguyên.\n\n**Ví dụ:** `/freeall 7`", parse_mode="Markdown")

    except Exception as e:

        bot.reply_to(message, f"❌ Lỗi: {str(e)[:100]}", parse_mode="Markdown")



@bot.message_handler(commands=['addytb'])
def cmd_addytb(message):
    if not require_feature_access_message(message, "them_youtube", FEATURE_LABELS["them_youtube"]):
        return
    user_id = message.from_user.id
    chat_id = message.chat.id
    if message.text and len(message.text.split()) > 1:
        url = message.text.split(None, 1)[1].strip()
        if "youtube.com" not in url and "youtu.be" not in url:
            return bot.reply_to(message, "❌ Link không hợp lệ! Ví dụ: /addytb https://youtube.com/@channelname")
        identifier = ytb_extract_identifier(url)
        if not identifier:
            return bot.reply_to(message, "❌ Không thể trích xuất thông tin kênh!\nVí dụ: /addytb https://youtube.com/@channelname")
        wait_msg = bot.send_message(chat_id, "⏳ Đang lấy thông tin kênh YouTube...")
        channel_info = ytb_get_channel_info(identifier)
        try: bot.delete_message(chat_id, wait_msg.message_id)
        except: pass
        if not channel_info:
            return bot.reply_to(message, "❌ Không tìm thấy kênh YouTube này!")
        data = load_ytb_data(); cid_str = str(chat_id)
        if cid_str not in data: data[cid_str] = {}
        if url in data[cid_str]:
            return bot.reply_to(message, "⚠️ Kênh này đã có trong danh sách!")
        now_str = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        data[cid_str][url] = {"channel_id": channel_info["channel_id"], "title": channel_info["title"],
                               "avatar": channel_info["avatar"], "added_time": now_str,
                               "last_check": now_str, "status": "live", "fail_count": 0}
        save_ytb_data(data)
        bot.reply_to(message, f"✅ Đã thêm kênh <b>{channel_info['title']}</b> vào danh sách theo dõi!", parse_mode="HTML")
    else:
        temp_user_state[user_id] = {"mode": "add_ytb", "step": "wait_url"}
        bot.reply_to(message, "🎞️ Vui lòng dán link kênh YouTube:\nVí dụ: https://youtube.com/@channelname")

@bot.message_handler(commands=['listytb'])
def cmd_listytb(message):
    chat_id = message.chat.id
    data = load_ytb_data()
    channels = data.get(str(chat_id), {})
    if not channels:
        return bot.reply_to(message, "📋 Bạn chưa theo dõi kênh YouTube nào!\n\nDùng /addytb hoặc bấm 📺 Thêm YTB để thêm kênh.")
    msg = "📋 <b>DANH SÁCH KÊNH YOUTUBE ĐANG THEO DÕI:</b>\n\n"
    markup = types.InlineKeyboardMarkup(row_width=1)
    for idx, (url, ch) in enumerate(channels.items(), 1):
        s_icon = "🟢" if ch.get("status") == "live" else "🔴"
        s_text = "ĐANG HOẠT ĐỘNG" if ch.get("status") == "live" else "ĐÃ DIE ❌"
        msg += f"{idx}. {s_icon} <b>{ch['title']}</b>\n   🔗 {url}\n   📊 {s_text}\n   🕐 {ch.get('last_check','N/A')}\n\n"
        markup.add(types.InlineKeyboardButton(f"🗑 Xóa: {ch['title'][:30]}", callback_data=f"ytb_remove_{ch['channel_id']}"))
    msg += f"📊 Tổng: {len(channels)} kênh | Kiểm tra mỗi {YTB_CHECK_INTERVAL}s"
    bot.send_message(chat_id, msg, parse_mode="HTML", reply_markup=markup)

@bot.message_handler(commands=['delytb'])
def cmd_delytb(message):
    chat_id = message.chat.id
    if not message.text or len(message.text.split()) < 2:
        return bot.reply_to(message, "⚠️ Vui lòng cung cấp link YTB cần xóa!\nVí dụ: /delytb https://youtube.com/@channelname")
    url = message.text.split(None, 1)[1].strip()
    data = load_ytb_data(); cid_str = str(chat_id)
    if cid_str not in data or url not in data[cid_str]:
        return bot.reply_to(message, "❌ Không tìm thấy kênh này trong danh sách!")
    title = data[cid_str][url].get("title", url)
    del data[cid_str][url]
    if not data[cid_str]: del data[cid_str]
    save_ytb_data(data)
    bot.reply_to(message, f"🗑 <b>Đã xóa kênh {title} khỏi danh sách!</b>", parse_mode="HTML")

@bot.message_handler(commands=['cookie'])

def command_cookie(message):

    global FB_COOKIE

    user_id = message.from_user.id

    if user_id not in ADMIN_IDS:

        return bot.reply_to(message, "❌ Lệnh này chỉ dành cho Admin.")

    

    parts = message.text.split(maxsplit=1)

    if len(parts) < 2:

        return bot.reply_to(message, "📝 Cách dùng: `/cookie <nội dung cookie>`", parse_mode="Markdown")

    

    new_cookie = parts[1].strip()

    FB_COOKIE = new_cookie

    

    try:

        with open(FILES["cookie"], "w", encoding="utf-8") as f:

            f.write(new_cookie)

        bot.reply_to(message, "✅ **Đã cập nhật Cookie Admin thành công!**\n\nToàn bộ hệ thống sẽ dùng Cookie này để cào dữ liệu Facebook.", parse_mode="Markdown")

        print(f"Update Cookie by {user_id}")

    except Exception as e:

        bot.reply_to(message, f"❌ Lỗi lưu file: {str(e)}")



@bot.message_handler(commands=['addadmin'])

def admin_add_new_admin(message):

    if message.from_user.id != BOSS_ID: return 

    try:

        _, uid = message.text.split()

        if add_new_admin(int(uid)): bot.reply_to(message, f"✅ Đã thêm Admin `{uid}`", parse_mode="Markdown")

    except: pass



@bot.message_handler(commands=['setanhdie'])

def set_anh_die_command(message):

    """Lệnh để admin cập nhật link ảnh DIE"""

    global ANHDIE  # Khai báo global trước

    

    user_id = message.from_user.id

    if user_id not in ADMIN_IDS and user_id != BOSS_ID:

        return bot.reply_to(message, "❌ Bạn không có quyền sử dụng lệnh này!")

    

    try:

        parts = message.text.split(maxsplit=1)

        if len(parts) < 2:

            return bot.reply_to(message, 

                f"📌 **Hướng dẫn sử dụng:**\n\n"

                f"`/setanhdie [LINK_ảnh]`\n\n"

                f"**Link hiện tại:** {ANHDIE}", 

                parse_mode="Markdown")

        

        new_link = parts[1].strip()

        

        # Kiểm tra link có hợp lệ không

        if not new_link.startswith(('http://', 'https://')):

            return bot.reply_to(message, "❌ Link không hợp lệ! Phải bắt đầu bằng http:// hoặc https://")

        

        # Cập nhật biến global

        ANHDIE = new_link

        

        # Lưu vào file config để persistent

        try:

            config = load_json(FILES["config"]) or {}

            config["ANHDIE"] = new_link

            save_json(FILES["config"], config)

        except Exception as e:

            print(f"⚠️ Không lưu được config: {str(e)}")

        

        bot.reply_to(message, 

            f"✅ **Đã cập nhật link ảnh DIE thành công!**\n\n"

            f"**Link mới:** {new_link}\n\n"

            f"Ảnh này sẽ được gửi khi UID chuyển từ LIVE → DIE", 

            parse_mode="Markdown")

        

        print(f"🔄 Admin {user_id} đã cập nhật ANHDIE: {new_link}")

        

    except Exception as e:

        bot.reply_to(message, f"❌ Lỗi: {str(e)}")





@bot.message_handler(commands=['setanhlive'])

def set_anh_live_command(message):

    """Lệnh để admin cập nhật link ảnh LIVE (Mark sống)"""

    global ANHLIVE

    user_id = message.from_user.id

    if user_id not in ADMIN_IDS and user_id != BOSS_ID:

        return bot.reply_to(message, "❌ Bạn không có quyền sử dụng lệnh này!")

    try:

        parts = message.text.split(maxsplit=1)

        if len(parts) < 2:

            return bot.reply_to(message,
                f"📌 **Hướng dẫn sử dụng:**\n\n"
                f"`/setanhlive [LINK_ảnh]`\n\n"
                f"**Link hiện tại:** {ANHLIVE}\n\n"
                f"Ảnh này sẽ được gửi khi UID chuyển từ DIE → LIVE (sống lại)",
                parse_mode="Markdown")

        new_link = parts[1].strip()

        if not new_link.startswith(('http://', 'https://')):

            return bot.reply_to(message, "❌ Link không hợp lệ! Phải bắt đầu bằng http:// hoặc https://")

        ANHLIVE = new_link

        try:

            config = load_json(FILES["config"]) or {}

            config["ANHLIVE"] = new_link

            save_json(FILES["config"], config)

        except Exception as e:

            print(f"⚠️ Không lưu được config ANHLIVE: {str(e)}")

        bot.reply_to(message,
            f"✅ **Đã cập nhật link ảnh LIVE thành công!**\n\n"
            f"**Link mới:** {new_link}\n\n"
            f"Ảnh này sẽ được gửi khi UID chuyển từ DIE → LIVE (sống lại)",
            parse_mode="Markdown")

        print(f"🔄 Admin {user_id} đã cập nhật ANHLIVE: {new_link}")

    except Exception as e:

        bot.reply_to(message, f"❌ Lỗi: {str(e)}")


@bot.message_handler(commands=['endchat'])

def end_chat_command(message):

    user_id = message.from_user.id

    if user_id in active_chats:

        partner_id = active_chats[user_id]

        del active_chats[user_id]

        if partner_id in active_chats:

            del active_chats[partner_id]

        if user_id in ADMIN_IDS:

            bot.reply_to(message, "✅ Đã kết thúc hội thoại hỗ trợ với Quý khách.")

            try: bot.send_message(partner_id, "👋 Chuyên viên đã kết thúc hội thoại hỗ trợ. Cảm ơn Quý khách đã sử dụng dịch vụ!")

            except: pass

        else:

            bot.reply_to(message, "✅ Đã kết thúc hội thoại hỗ trợ. Cảm ơn Quý khách đã sử dụng dịch vụ!")

            try: bot.send_message(partner_id, "👋 Quý khách đã kết thúc hội thoại hỗ trợ.")

            except: pass

    else:

        bot.reply_to(message, "❌ Quý khách không đang trong hội thoại hỗ trợ nào.")



@bot.message_handler(commands=['naptien'], content_types=['text', 'photo'])
def cmd_naptien(message):
    chat_id = message.chat.id
    mk = types.InlineKeyboardMarkup()
    mk.add(types.InlineKeyboardButton("💝 Ủng hộ / Donate", callback_data="show_donate"))
    bot.send_message(chat_id, "💝 Bấm nút bên dưới để xem thông tin donate:", reply_markup=mk)



@bot.callback_query_handler(func=lambda call: call.data.startswith("donate_") or call.data == "show_donate")
def donate_callback(call):
    if call.data == "donate_copy_stk":
        bot.answer_callback_query(call.id, "✅ STK: 0862197064 — MB Bank\nChủ TK: NGUYỄN MAI NIN", show_alert=True)
    elif call.data == "show_donate":
        bot.answer_callback_query(call.id)
        user_id = call.from_user.id
        chat_id = call.message.chat.id
        qr_url = f"https://img.vietqr.io/image/MB-0862197064-compact2.png?amount=0&addInfo=DH%20Donate%20{user_id}&accountName=NGUYEN%20MAI%20NIN"
        caption = (
            "💝 *ỦNG HỘ DUY TRÌ SERVER*\n"
            "───────────────\n"
            "🏦 NH: Mb Bank\n"
            "💳 STK: `0862197064`\n"
            "👤 CTK: NGUYỄN MAI NIN\n"
            f"📝 ND: `DH Donate {user_id}`\n"
            "───────────────\n"
            "💖 Cảm ơn bạn đã ủng hộ bot!\n"
            "ℹ️ _Donate không tự động check_"
        )
        mk = types.InlineKeyboardMarkup()
        mk.add(types.InlineKeyboardButton("💳 Sao chép STK: 0862197064", callback_data="donate_copy_stk"))
        try:
            bot.send_photo(chat_id, qr_url, caption=caption, parse_mode="Markdown", reply_markup=mk)
        except:
            bot.send_message(chat_id, caption, parse_mode="Markdown", reply_markup=mk)

@bot.callback_query_handler(func=lambda call: call.data.startswith("ulist_"))
def unified_list_callback(call):
    chat_id = call.message.chat.id
    user_id = call.from_user.id
    data = call.data
    mid = call.message.message_id
    bot.answer_callback_query(call.id)

    # Tab chuyển
    if data == "ulist_tab_overview":
        show_unified_list(chat_id, user_id, "overview", mid); return
    if data == "ulist_tab_fb":
        show_unified_list(chat_id, user_id, "fb", mid); return
    if data == "ulist_tab_gr":
        show_unified_list(chat_id, user_id, "gr", mid); return
    if data == "ulist_tab_ig":
        show_unified_list(chat_id, user_id, "ig", mid); return
    if data == "ulist_tab_tt":
        show_unified_list(chat_id, user_id, "tt", mid); return
    if data == "ulist_tab_post":
        show_unified_list(chat_id, user_id, "post", mid); return

    # Xóa từng item
    if data.startswith("ulist_del_fb_"):
        uid = data.replace("ulist_del_fb_", "")
        remove_tracking_uid(chat_id, uid)
        update_user_stats(user_id, "cancel")
        show_unified_list(chat_id, user_id, "fb", mid); return

    if data.startswith("ulist_del_gr_"):
        uid = data.replace("ulist_del_gr_", "")
        grig_dm.remove_account(user_id, uid)
        show_unified_list(chat_id, user_id, "gr", mid); return

    if data.startswith("ulist_del_ig_"):
        uid = data.replace("ulist_del_ig_", "")
        grig_dm.remove_account(user_id, uid)
        show_unified_list(chat_id, user_id, "ig", mid); return

    if data.startswith("ulist_del_tt_"):
        username = data.replace("ulist_del_tt_", "")
        remove_tracking_tiktok(chat_id, username)
        update_user_stats(user_id, "cancel")
        show_unified_list(chat_id, user_id, "tt", mid); return

    if data.startswith("ulist_del_post_"):
        short_key = data.replace("ulist_del_post_", "")
        url = _get_fp_url_cache().get(short_key)
        if url and url in _get_fp_watching():
            try: _get_fp_watching()[url]["task"].cancel()
            except: pass
            del _get_fp_watching()[url]
        show_unified_list(chat_id, user_id, "post", mid); return

    # Xóa tất cả từng loại
    if data == "ulist_delall_fb":
        d = get_tracking()
        if str(chat_id) in d: d[str(chat_id)] = {}; save_json(FILES["tracking"], d)
        show_unified_list(chat_id, user_id, "fb", mid); return

    if data == "ulist_delall_gr":
        accs = grig_dm.get_accounts(user_id)
        for uid, v in list(accs.items()):
            if v.get('platform') == 'facebook_group':
                grig_dm.remove_account(user_id, uid)
        show_unified_list(chat_id, user_id, "gr", mid); return

    if data == "ulist_delall_ig":
        accs = grig_dm.get_accounts(user_id)
        for uid, v in list(accs.items()):
            if v.get('platform') == 'instagram':
                grig_dm.remove_account(user_id, uid)
        show_unified_list(chat_id, user_id, "ig", mid); return

    if data == "ulist_delall_tt":
        d = get_tracking_tiktok()
        if str(chat_id) in d: d[str(chat_id)] = {}; save_json(FILES["tracking_tiktok"], d)
        show_unified_list(chat_id, user_id, "tt", mid); return

    if data == "ulist_delall_post":
        for info in _get_fp_watching().values():
            try: info["task"].cancel()
            except: pass
        _get_fp_watching().clear()
        show_unified_list(chat_id, user_id, "post", mid); return

    if data == "ulist_tab_ytb":
        show_unified_list(chat_id, user_id, "ytb", mid); return

    if data.startswith("ulist_del_ytb_"):
        channel_id = data.replace("ulist_del_ytb_", "")
        ytb_d = load_ytb_data()
        cid_str = str(chat_id)
        if cid_str in ytb_d:
            to_del = [url for url, ch in ytb_d[cid_str].items() if ch.get("channel_id","") == channel_id]
            for url in to_del:
                del ytb_d[cid_str][url]
            if not ytb_d[cid_str]:
                del ytb_d[cid_str]
            save_ytb_data(ytb_d)
        show_unified_list(chat_id, user_id, "ytb", mid); return

    if data == "ulist_delall_ytb":
        ytb_d = load_ytb_data()
        if str(chat_id) in ytb_d:
            del ytb_d[str(chat_id)]
            save_ytb_data(ytb_d)
        show_unified_list(chat_id, user_id, "ytb", mid); return

    # Xóa tất cả mọi thứ
    if data == "ulist_del_all":
        d = get_tracking()
        if str(chat_id) in d: d[str(chat_id)] = {}; save_json(FILES["tracking"], d)
        d2 = get_tracking_tiktok()
        if str(chat_id) in d2: d2[str(chat_id)] = {}; save_json(FILES["tracking_tiktok"], d2)
        accs = grig_dm.get_accounts(user_id)
        for uid in list(accs.keys()):
            grig_dm.remove_account(user_id, uid)
        for info in _get_fp_watching().values():
            try: info["task"].cancel()
            except: pass
        _get_fp_watching().clear()
        ytb_d = load_ytb_data()
        if str(chat_id) in ytb_d:
            del ytb_d[str(chat_id)]
            save_ytb_data(ytb_d)
        bot.answer_callback_query(call.id, "✅ Đã xóa tất cả!", show_alert=True)
        show_unified_list(chat_id, user_id, "overview", mid); return

# ========== END MENU DANH SÁCH TỔNG HỢP ==========

@bot.callback_query_handler(func=lambda call: True)

def handle_callback(call):

    try:

        user_id = call.from_user.id

        chat_id = call.message.chat.id

        _safe_callback_ack(call)

        # ===== MENU ĐIỀU HƯỚNG =====
        if call.data == "back_to_menu":
            class _FakeMenuMsg:
                def __init__(self, cid, user):
                    self.chat = type("C", (), {"id": cid})()
                    self.from_user = user
            show_menu(_FakeMenuMsg(chat_id, call.from_user), edit_msg_id=call.message.message_id)
            return

        if call.data.startswith("menu_cat_"):
            show_menu_category(chat_id, user_id, call.data.replace("menu_cat_", ""), call.message.message_id)
            return

        # ===== ADMIN RESET =====
        if call.data.startswith("admin_reset"):
            if user_id not in ADMIN_IDS and user_id != BOSS_ID:
                return
            if _get_subbot_ctx():
                return
            if call.data == "admin_reset_menu":
                show_admin_reset_menu(chat_id, call.message.message_id)
                return
            if call.data == "admin_reset_confirm_tracking":
                mk = types.InlineKeyboardMarkup()
                mk.add(
                    types.InlineKeyboardButton("✅ Xác nhận xóa UID", callback_data="admin_reset_do_tracking"),
                    types.InlineKeyboardButton("❌ Hủy", callback_data="admin_reset_menu"),
                )
                bot.edit_message_text(
                    "⚠️ <b>Xóa TẤT CẢ UID đang check?</b>\n"
                    "Bao gồm FB, TikTok, YouTube, Group/IG, uid_memory.",
                    chat_id, call.message.message_id, parse_mode="HTML", reply_markup=mk)
                return
            if call.data == "admin_reset_confirm_botcon":
                mk = types.InlineKeyboardMarkup()
                mk.add(
                    types.InlineKeyboardButton("✅ Xác nhận xóa Bot con", callback_data="admin_reset_do_botcon"),
                    types.InlineKeyboardButton("❌ Hủy", callback_data="admin_reset_menu"),
                )
                bot.edit_message_text(
                    "⚠️ <b>Xóa TẤT CẢ Bot con?</b>\nDừng polling và xóa token đã lưu.",
                    chat_id, call.message.message_id, parse_mode="HTML", reply_markup=mk)
                return
            if call.data == "admin_reset_confirm_full":
                mk = types.InlineKeyboardMarkup()
                mk.add(
                    types.InlineKeyboardButton("💣 XÁC NHẬN RESET", callback_data="admin_reset_do_full"),
                    types.InlineKeyboardButton("❌ Hủy", callback_data="admin_reset_menu"),
                )
                bot.edit_message_text(
                    "⚠️ <b>RESET TOÀN BỘ?</b>\n"
                    "Xóa mọi UID + Bot con + lịch sử check.\n"
                    "<i>Giữ user/VIP/số dư.</i>",
                    chat_id, call.message.message_id, parse_mode="HTML", reply_markup=mk)
                return
            if call.data == "admin_reset_confirm_wipe":
                mk = types.InlineKeyboardMarkup()
                mk.add(
                    types.InlineKeyboardButton("🧨 XÓA HẾT DỮ LIỆU", callback_data="admin_reset_do_wipe"),
                    types.InlineKeyboardButton("❌ Hủy", callback_data="admin_reset_menu"),
                )
                bot.edit_message_text(
                    "⚠️ <b>XÓA HẾT — BOT NHƯ MỚI?</b>\n\n"
                    "Sẽ xóa:\n"
                    "• Tất cả user & VIP & số dư\n"
                    "• Tất cả UID đang check\n"
                    "• Tất cả Bot con\n"
                    "• Doanh thu, mã, cookie, cache\n\n"
                    "<b>Không thể hoàn tác!</b>",
                    chat_id, call.message.message_id, parse_mode="HTML", reply_markup=mk)
                return
            if call.data == "admin_reset_do_tracking":
                admin_reset_all_tracking()
                bot.edit_message_text("✅ Đã xóa tất cả UID đang check.", chat_id, call.message.message_id)
                return
            if call.data == "admin_reset_do_botcon":
                n = admin_stop_all_sub_bots()
                admin_reset_all_sub_bots()
                bot.edit_message_text(f"✅ Đã xóa tất cả Bot con ({n} bot đã dừng).", chat_id, call.message.message_id)
                return
            if call.data == "admin_reset_do_full":
                admin_factory_reset()
                bot.edit_message_text("✅ Reset toàn bộ hoàn tất (UID + Bot con + history).", chat_id, call.message.message_id)
                return
            if call.data == "admin_reset_do_wipe":
                admin_wipe_all_data()
                bot.edit_message_text(
                    "✅ <b>Đã xóa toàn bộ dữ liệu.</b>\nBot như mới — chưa có user.\n"
                    "Giữ nguyên: cấu hình (<code>data_config.json</code>) & admin.",
                    chat_id, call.message.message_id, parse_mode="HTML")
                return

        # ===== FEATURE TOGGLE CALLBACKS (Admin) =====
        if call.data.startswith("ftoggle_") or call.data == "admin_features":
            bot.answer_callback_query(call.id)
            if user_id not in ADMIN_IDS and user_id != BOSS_ID:
                bot.answer_callback_query(call.id, "❌ Chỉ Admin!", show_alert=True)
                return
            if call.data == "admin_features":
                admin_feature_toggle_menu(chat_id, call.message.message_id)
                return
            cfg = get_config()
            free = cfg.get("free_features", {})
            if call.data == "ftoggle_all_free":
                for k in FEATURE_LABELS:
                    free[k] = True
                cfg["free_features"] = free
                save_json(FILES["config"], cfg)
                bot.answer_callback_query(call.id, "✅ Đã bật FREE tất cả!", show_alert=True)
                admin_feature_toggle_menu(chat_id, call.message.message_id)
                return
            if call.data == "ftoggle_all_vip":
                for k in FEATURE_LABELS:
                    free[k] = False
                cfg["free_features"] = free
                save_json(FILES["config"], cfg)
                bot.answer_callback_query(call.id, "✅ Đã bật VIP tất cả!", show_alert=True)
                admin_feature_toggle_menu(chat_id, call.message.message_id)
                return
            fkey = call.data.replace("ftoggle_", "")
            if fkey in FEATURE_LABELS:
                cur = free.get(fkey, False)
                free[fkey] = not cur
                cfg["free_features"] = free
                save_json(FILES["config"], cfg)
                label = FEATURE_LABELS[fkey]
                status = "🟢 FREE" if not cur else "🔴 VIP"
                bot.answer_callback_query(call.id, f"{status} — {label}", show_alert=True)
                admin_feature_toggle_menu(chat_id, call.message.message_id)
            return

        # ===== ADMINBOT CALLBACKS - CHỈ BOT CHÍNH =====
        if call.data.startswith("adminbot_") or call.data == "adminbot_menu":
            if _get_subbot_ctx():
                # Bot con: bỏ qua hoàn toàn, không làm gì
                bot.answer_callback_query(call.id)
                return
            if user_id not in ADMIN_IDS and user_id != BOSS_ID:
                bot.answer_callback_query(call.id, "❌ Chỉ Admin mới dùng được!", show_alert=True)
                return
            bot.answer_callback_query(call.id)
            if call.data == "adminbot_menu":
                adminbot_show_menu(chat_id)
            elif call.data == "adminbot_list":
                adminbot_list_all(chat_id, call.message.message_id)
            elif call.data == "adminbot_check_vip":
                adminbot_check_vip_all(chat_id, call.message.message_id)
            elif call.data == "adminbot_delete_ask":
                msg = "<b>🗑 XÓA BOT CON CỦA USER</b>\n\nNhập UID của user cần xóa bot con:\n<i>(Bot con bị xóa và dừng polling)</i>"
                mk = types.InlineKeyboardMarkup()
                mk.add(types.InlineKeyboardButton("❌ Hủy", callback_data="adminbot_menu"))
                try:
                    bot.edit_message_text(msg, chat_id, call.message.message_id, parse_mode="HTML", reply_markup=mk)
                except Exception:
                    bot.send_message(chat_id, msg, parse_mode="HTML", reply_markup=mk)
                temp_user_state[user_id] = {"mode": "adminbot_delete"}
            elif call.data == "adminbot_addvip_ask":
                msg = "<b>⭐ CẤP/GIA HẠN VIP BOT CON</b>\n\nNhập theo định dạng:\n<code>UID so_thang</code>\n\nVí dụ: <code>123456789 3</code>\n<i>(Cộng thêm vào hạn hiện tại)</i>"
                mk = types.InlineKeyboardMarkup()
                mk.add(types.InlineKeyboardButton("❌ Hủy", callback_data="adminbot_menu"))
                try:
                    bot.edit_message_text(msg, chat_id, call.message.message_id, parse_mode="HTML", reply_markup=mk)
                except Exception:
                    bot.send_message(chat_id, msg, parse_mode="HTML", reply_markup=mk)
                temp_user_state[user_id] = {"mode": "adminbot_addvip"}
            elif call.data == "adminbot_stop_ask":
                msg = "<b>🔴 DỪNG BOT CON CỦA USER</b>\n\nNhập UID của user cần dừng bot con:"
                mk = types.InlineKeyboardMarkup()
                mk.add(types.InlineKeyboardButton("❌ Hủy", callback_data="adminbot_menu"))
                try:
                    bot.edit_message_text(msg, chat_id, call.message.message_id, parse_mode="HTML", reply_markup=mk)
                except Exception:
                    bot.send_message(chat_id, msg, parse_mode="HTML", reply_markup=mk)
                temp_user_state[user_id] = {"mode": "adminbot_stop"}
            elif call.data == "adminbot_start_ask":
                msg = "<b>🟢 KHỞI ĐỘNG LẠI BOT CON</b>\n\nNhập UID của user cần khởi động lại bot con:"
                mk = types.InlineKeyboardMarkup()
                mk.add(types.InlineKeyboardButton("❌ Hủy", callback_data="adminbot_menu"))
                try:
                    bot.edit_message_text(msg, chat_id, call.message.message_id, parse_mode="HTML", reply_markup=mk)
                except Exception:
                    bot.send_message(chat_id, msg, parse_mode="HTML", reply_markup=mk)
                temp_user_state[user_id] = {"mode": "adminbot_start"}
            return


        if call.data.startswith('grig_done_'):
            uid = call.data.replace('grig_done_', '')
            bot.answer_callback_query(call.id, "✅ Đã Done kèo!")
            try:
                new_cap = (call.message.caption or call.message.text or '') + "\n\n✅ DONE KÈO!"
                if call.message.caption:
                    bot.edit_message_caption(new_cap, call.message.chat.id, call.message.message_id, reply_markup=None)
                else:
                    bot.edit_message_text(new_cap, call.message.chat.id, call.message.message_id, reply_markup=None)
            except:
                try: bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
                except: pass
            return

        elif call.data.startswith('grig_cancel_'):
            uid = call.data.replace('grig_cancel_', '')
            bot.answer_callback_query(call.id, "❌ Đã hủy kèo!")
            try:
                new_cap = (call.message.caption or call.message.text or '') + "\n\n❌ HỦY KÈO!"
                if call.message.caption:
                    bot.edit_message_caption(new_cap, call.message.chat.id, call.message.message_id, reply_markup=None)
                else:
                    bot.edit_message_text(new_cap, call.message.chat.id, call.message.message_id, reply_markup=None)
            except:
                try: bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
                except: pass
            return

        elif call.data.startswith('grig_unfollow_'):
            uid = call.data.replace('grig_unfollow_', '')
            if grig_dm.remove_account(call.from_user.id, uid):
                grig_reset_die(call.from_user.id, uid)
                bot.answer_callback_query(call.id, "🚫 Đã hủy theo dõi!")
                try: bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
                except: pass
            else:
                bot.answer_callback_query(call.id, "⚠️ Không tìm thấy!", show_alert=True)
            return

        elif call.data == 'grig_list':
            accounts = grig_dm.get_accounts(call.from_user.id)
            if not accounts:
                bot.answer_callback_query(call.id, "⚠️ Chưa có tài khoản nào!", show_alert=True)
                return
            live_c = sum(1 for d in accounts.values() if d['status'] == 'live')
            die_c = len(accounts) - live_c
            text = "📋 DANH SÁCH THEO DÕI (Group/IG)\n\n"
            markup_ds = types.InlineKeyboardMarkup(row_width=1)
            for i, (uid, d) in enumerate(list(accounts.items())[:20], 1):
                icon = "✅" if d['status'] == 'live' else "❌"
                plt = '📷' if d.get('platform') == 'instagram' else '👥'
                name = d.get('name', uid)
                note = d.get('note', '')
                text += f"{i}. {icon}{plt} {name}\n   🆔 {uid}\n   📝 {note}\n\n"
                markup_ds.add(types.InlineKeyboardButton(f"🗑 Xóa: {name[:25]}", callback_data=f"grig_unfollow_{uid}"))
            if len(accounts) > 20:
                text += f"... và {len(accounts)-20} tài khoản khác\n"
            text += f"━━━━━━━━━━━━━━\n✅ LIVE: {live_c}  ❌ DIE: {die_c}"
            bot.answer_callback_query(call.id)
            bot.send_message(call.message.chat.id, text, reply_markup=markup_ds)
            return
        # ===== END GRIG CALLBACKS =====

        # Xử lý callback music
        if call.data.startswith('music_'):
            try:
                if call.data == "music_cancel":
                    if user_id in music_cache:
                        del music_cache[user_id]
                    bot.edit_message_caption("❌ Đã hủy", call.message.chat.id, call.message.message_id)
                    bot.send_message(call.message.chat.id, "Bấm nút để tìm lại:", reply_markup=get_fixed_menu(user_id))
                    bot.answer_callback_query(call.id)
                    return
                
                if call.data == "music_stop":
                    bot.answer_callback_query(call.id, "🛑 Đã tắt nhạc!")
                    if user_id in music_cache and 'current' in music_cache[user_id]:
                        del music_cache[user_id]['current']
                    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
                    return
                
                if call.data == "music_replay":
                    bot.answer_callback_query(call.id, "🔄 Đang phát lại...")
                    if user_id in music_cache and 'current' in music_cache[user_id]:
                        gui_nhac(call.message.chat.id, music_cache[user_id]['current'], user_id)
                    return
                
                if call.data == "music_loop":
                    if user_id not in music_cache:
                        music_cache[user_id] = {}
                    music_cache[user_id]['loop'] = not music_cache[user_id].get('loop', False)
                    trang_thai = "BẬT" if music_cache[user_id]['loop'] else "TẮT"
                    bot.answer_callback_query(call.id, f"🔁 Đã {trang_thai} chế độ lặp!")
                    return
                
                chi_so = int(call.data.replace('music_', '')) - 1
                
                if user_id not in music_cache:
                    bot.answer_callback_query(call.id, "⚠️ Hết hạn!", show_alert=True)
                    return
                
                danh_sach = music_cache[user_id]['songs']
                if chi_so < 0 or chi_so >= len(danh_sach):
                    bot.answer_callback_query(call.id, "❌ Không hợp lệ!", show_alert=True)
                    return
                
                bai_hat = danh_sach[chi_so]
                music_cache[user_id]['current'] = bai_hat
                
                bot.answer_callback_query(call.id, "⏳ Đang tải...")
                bot.delete_message(call.message.chat.id, call.message.message_id)
                gui_nhac(call.message.chat.id, bai_hat, user_id)
                
                # Hiển thị lại menu sau khi gửi nhạc
                bot.send_message(call.message.chat.id, "Bấm nút để tìm bài khác:", reply_markup=get_fixed_menu(user_id))
                
            except Exception as e:
                bot.answer_callback_query(call.id, f"❌ Lỗi: {e}", show_alert=True)
            return
        
        if call.data == "start_support":

            process_chat_request(call.from_user, chat_id)

            bot.answer_callback_query(call.id)

            

        elif call.data == "help_cookie":

            bot.send_message(chat_id, "🍪 **HƯỚNG DẪN NẠP COOKIE:**\n\n👉 Mua Clone/Via về, lấy Cookie.\n👉 Gõ: `/cookie <dán_cookie>`\n\n(Người dùng tự trang bị cookie, Admin không cung cấp).", parse_mode="Markdown")

            bot.answer_callback_query(call.id)

        elif call.data == "menu_check_faq":
            if not require_feature_access_call(call, "check_faq", FEATURE_LABELS["check_faq"]):
                return

            bot.answer_callback_query(call.id)

            bot.send_message(
                chat_id,
                "🔄 <b>CHECK FAQ / DIE (dạng 282/956)</b>\n\n"
                "Gửi UID hoặc link Facebook để kiểm tra.\n"
                "Hỗ trợ nhiều UID — mỗi dòng 1 cái.\n\n"
                "📝 <b>Ví dụ:</b>\n"
                "<code>100001234567890</code>\n"
                "<code>https://www.facebook.com/profile.php?id=100001234567890</code>\n\n"
                "👉 Hoặc dùng lệnh: <code>/checkfaq UID</code>",
                parse_mode="HTML"
            )

            temp_user_state[user_id] = {"mode": "check_faq", "step": "wait_input"}

        elif call.data == "botcon_menu":
            if not require_feature_access_call(call, "bot_con", FEATURE_LABELS["bot_con"]):
                return

            bot.answer_callback_query(call.id)
            botcon_show_menu(chat_id, user_id)

        elif call.data == "botcon_vip_upgrade":
            bot.answer_callback_query(call.id)
            botcon_show_vip_upgrade(chat_id, user_id)

        elif call.data.startswith("botcon_vip_buy_"):
            plan_key = call.data.replace("botcon_vip_buy_", "")
            bot.answer_callback_query(call.id)
            botcon_vip_buy_request(chat_id, user_id, plan_key)

        elif call.data == "botcon_copy_stk":
            bot.answer_callback_query(call.id,
                "✅ STK: 0862197064 — MB Bank\nChủ TK: NGUYỄN MAI NIN",
                show_alert=True)

        elif call.data.startswith("botcon_vip_bill_"):
            plan_key = call.data.replace("botcon_vip_bill_", "")
            plan = BOTCON_VIP_PLANS.get(plan_key, {})
            bot.answer_callback_query(call.id)
            bot.send_message(chat_id,
                f"📸 <b>Gửi ảnh bill chuyển khoản</b>\n\n"
                f"Gói: <b>{plan.get('label','?')}</b> — {format_vnd(plan.get('price',0))}\n"
                f"📝 Nội dung CK: <code>BOTCON {user_id} {plan_key}T</code>\n\n"
                "Gửi ảnh bill/screenshot ngay bên dưới để Admin duyệt.",
                parse_mode="HTML")
            temp_user_state[user_id] = {"mode": "botcon_vip_bill", "plan": plan_key}

        elif call.data.startswith("botcon_vip_approve_"):
            if user_id not in ADMIN_IDS:
                bot.answer_callback_query(call.id, "❌ Chỉ Admin!", show_alert=True)
                return
            parts_cb = call.data.replace("botcon_vip_approve_", "").split("_")
            if len(parts_cb) >= 2:
                target_uid = int(parts_cb[0])
                plan_key   = parts_cb[1]
                plan = BOTCON_VIP_PLANS.get(plan_key, {})
                months = plan.get("months", 1)
                new_exp = botcon_add_vip(target_uid, months)
                exp_str = datetime.fromtimestamp(new_exp).strftime("%d/%m/%Y")
                bot.answer_callback_query(call.id, f"✅ Đã cấp VIP {plan.get('label','?')}")
                bot.edit_message_reply_markup(chat_id, call.message.message_id, reply_markup=None)
                bot.send_message(chat_id, f"✅ Đã kích hoạt VIP Bot Con gói <b>{plan.get('label','?')}</b> cho UID <code>{target_uid}</code>\nHạn đến: <b>{exp_str}</b>", parse_mode="HTML")
                try:
                    _botcon_orig['send_message'](target_uid,
                        f"🎉 <b>VIP Bot Con đã được kích hoạt!</b>\n\n"
                        f"⭐ Gói: <b>{plan.get('label','?')}</b>\n"
                        f"📅 Hạn đến: <b>{exp_str}</b>\n\n"
                        "✅ Bot con của bạn đã sẵn sàng hoạt động!",
                        parse_mode="HTML")
                except Exception:
                    pass
                bc_data = botcon_load()
                bc_info = bc_data.get(str(target_uid), {})
                if bc_info.get("token"):
                    botcon_start_polling(bc_info["token"], target_uid)

        elif call.data.startswith("botcon_vip_reject_"):
            if user_id not in ADMIN_IDS:
                bot.answer_callback_query(call.id, "❌ Chỉ Admin!", show_alert=True)
                return
            target_uid = int(call.data.replace("botcon_vip_reject_", ""))
            bot.answer_callback_query(call.id, "Đã từ chối")
            bot.edit_message_reply_markup(chat_id, call.message.message_id, reply_markup=None)
            bot.send_message(chat_id, f"❌ Đã từ chối VIP Bot Con UID <code>{target_uid}</code>", parse_mode="HTML")
            try:
                _botcon_orig['send_message'](target_uid,
                    "❌ <b>Yêu cầu VIP Bot Con bị từ chối.</b>\n"
                    "Vui lòng kiểm tra lại bill và liên hệ Admin.",
                    parse_mode="HTML")
            except Exception:
                pass

        elif call.data == "botcon_add_token":

            bot.answer_callback_query(call.id)
            botcon_show_add_token(chat_id, user_id)

        elif call.data == "botcon_delete":

            bot.answer_callback_query(call.id)
            botcon_delete_token(chat_id, user_id)

        elif call.data == "botcon_change_token":
            bot.answer_callback_query(call.id)
            # Xoa token cu nhung giu VIP
            data_bc = botcon_load()
            uid_str_bc = str(user_id)
            old_token = data_bc.get(uid_str_bc, {}).get("token", "")
            if old_token:
                botcon_stop_polling(old_token)
            # Giu VIP, xoa thong tin bot
            vip_expiry_save = data_bc.get(uid_str_bc, {}).get("vip_expiry", 0)
            data_bc[uid_str_bc] = {"vip_expiry": vip_expiry_save}
            botcon_save(data_bc)
            _botcon_orig['send_message'](chat_id,
                "🔄 <b>Thay Token Bot Con</b>\n\n"
                "⚠️ Token cũ đã được gỡ, VIP của bạn vẫn được giữ nguyên.\n\n"
                "📟 <b>Nhập token mới:</b>\n"
                "Lấy từ @BotFather → /mybots → chọn bot → /token\n\n"
                "💡 Token có dạng:\n"
                "<code>123456789:ABCdefGHIjklMNOpqrsTUVwxyz</code>\n\n"
                "⬇️ <b>Gửi token mới ngay bên dưới:</b>",
                parse_mode="HTML")
            temp_user_state[user_id] = {"mode": "botcon_add", "step": "wait_token"}

        elif call.data == "botcon_back_menu":

            bot.answer_callback_query(call.id)
            botcon_show_menu(chat_id, user_id, edit_msg_id=call.message.message_id)

        

        elif call.data == "add_uid":
            if not require_feature_access_call(call, "them_uid_fb", FEATURE_LABELS["them_uid_fb"]):
                return

            temp_user_state[user_id] = {"step": "wait_uid", "mode": "normal"}

            bot.send_message(chat_id, "🔗 Vui lòng dán LINK cá nhân hoặc nhập UID Facebook:")

            bot.answer_callback_query(call.id)

    

        elif call.data == "check_fb_basic":
            if not require_feature_access_call(call, "check_info", FEATURE_LABELS["check_info"]):
                return

            temp_user_state[user_id] = {"step": "wait_checkfb", "fb_mode": "basic"}

            bot.send_message(chat_id,
                "📋 *CHECK INFO FB (CƠ BẢN)*\n\n"
                "Dùng API Facebook công khai — không cookie.\n\n"
                "👤 Facebook: UID / link / username\n"
                "📷 Instagram: instagram.com/username\n"
                "🎵 TikTok: tiktok.com/@username\n\n"
                "⬇️ Gửi link hoặc UID để check:",
                parse_mode="Markdown")

            bot.answer_callback_query(call.id)

        elif call.data == "check_fb_vip":
            if not require_feature_access_call(call, "check_info_vip", FEATURE_LABELS["check_info_vip"]):
                return

            temp_user_state[user_id] = {"step": "wait_checkfb", "fb_mode": "premium"}

            bot.send_message(chat_id,
                "👑 *CHECK INFO FB (FULL VIP)*\n\n"
                "Tra cứu qua cookie clone — đầy đủ thông tin.\n\n"
                "👤 Gửi UID / link / username Facebook:\n"
                "• <code>100001234567890</code>\n"
                "• <code>facebook.com/username</code>\n\n"
                "⬇️ Gửi ngay bên dưới:",
                parse_mode="HTML")

            bot.answer_callback_query(call.id)

        elif call.data == "check_fb_full":
            if not require_feature_access_call(call, "check_info", FEATURE_LABELS["check_info"]):
                return

            temp_user_state[user_id] = {"step": "wait_checkfb", "fb_mode": "basic"}

            bot.send_message(chat_id, "🔍 *CHECK INFO FULL*\n\nDán link hoặc nhập vào:\n\n👤 *Facebook:* facebook.com/username hoặc UID số\n📷 *Instagram:* instagram.com/username\n🎵 *TikTok:* tiktok.com/@username\n\n⬇️ Gửi link để check:", parse_mode="Markdown")

            bot.answer_callback_query(call.id)

        

        elif call.data == "admin_broadcast_menu":

            bot.answer_callback_query(call.id)

            if user_id in ADMIN_IDS:

                show_broadcast_menu(chat_id, user_id, call.message.message_id)

        elif call.data == "admin_back":

            bot.answer_callback_query(call.id)

            if user_id in ADMIN_IDS:

                show_admin_panel(chat_id, user_id, call.message.message_id)

        elif call.data == "broadcast_text_only":

            bot.answer_callback_query(call.id)

            if user_id in ADMIN_IDS:

                bot.send_message(chat_id, "✏️ **GỬI VĂN BẢN**\n\nNhập nội dung thông báo:", parse_mode="Markdown")

                temp_user_state[user_id] = {"mode": "broadcast", "step": "wait_text", "photo_id": None}

        elif call.data == "broadcast_photo_text":

            bot.answer_callback_query(call.id)

            if user_id in ADMIN_IDS:

                bot.send_message(chat_id, "🖼 **GỬI ẢNH + VĂN BẢN**\n\nGửi ảnh kèm chú thích (caption).\nHoặc gửi ảnh trước, rồi nhập văn bản sau.", parse_mode="Markdown")

                temp_user_state[user_id] = {"mode": "broadcast", "step": "wait_photo_text", "photo_id": None}

        elif call.data == "broadcast_photo_only":

            bot.answer_callback_query(call.id)

            if user_id in ADMIN_IDS:

                bot.send_message(chat_id, "📸 **GỬI ẢNH**\n\nGửi ảnh lên (không cần chú thích):", parse_mode="Markdown")

                temp_user_state[user_id] = {"mode": "broadcast", "step": "wait_photo_only", "photo_id": None}

        elif call.data == "broadcast_confirm_send":

            bot.answer_callback_query(call.id, "📢 Đang thông báo...")

            if user_id in ADMIN_IDS:

                state = temp_user_state.pop(user_id, None)
                if not state:
                    return

                try:
                    bot.edit_message_reply_markup(chat_id, call.message.message_id, reply_markup=None)
                except:
                    pass

                content  = state.get("broadcast_content", "")

                photo_id = state.get("broadcast_photo_id", None)

                threading.Thread(target=execute_broadcast_final, args=(user_id, content, "normal", photo_id), daemon=True).start()

        elif call.data == "broadcast_confirm_feedback":

            bot.answer_callback_query(call.id, "📢 Đang thông báo...")

            if user_id in ADMIN_IDS:

                state = temp_user_state.pop(user_id, None)
                if not state:
                    return

                try:
                    bot.edit_message_reply_markup(chat_id, call.message.message_id, reply_markup=None)
                except:
                    pass

                content  = state.get("broadcast_content", "")

                photo_id = state.get("broadcast_photo_id", None)

                threading.Thread(target=execute_broadcast_final, args=(user_id, content, "feedback", photo_id), daemon=True).start()

        elif call.data == "broadcast_cancel":

            bot.answer_callback_query(call.id)

            temp_user_state.pop(user_id, None)

            show_broadcast_menu(chat_id, user_id, call.message.message_id)

        elif call.data == "admin_ai_broadcast":

            if user_id in ADMIN_IDS:

                bot.send_message(chat_id, "🤖 Nhập chủ đề thông báo:")

                temp_user_state[user_id] = {"mode": "ai", "step": "wait_ai_topic"}

            bot.answer_callback_query(call.id)

        

        elif call.data == "exec_notify_normal":

            bot.answer_callback_query(call.id)

            if user_id in ADMIN_IDS and "broadcast_content" in temp_user_state.get(user_id, {}):

                content = temp_user_state[user_id]["broadcast_content"]

                temp_user_state.pop(user_id, None)

                threading.Thread(target=execute_broadcast_final, args=(user_id, content, "normal"), daemon=True).start()



        elif call.data == "exec_notify_feedback":

            bot.answer_callback_query(call.id)

            if user_id in ADMIN_IDS and "broadcast_content" in temp_user_state.get(user_id, {}):

                content = temp_user_state[user_id]["broadcast_content"]

                temp_user_state.pop(user_id, None)

                threading.Thread(target=execute_broadcast_final, args=(user_id, content, "feedback"), daemon=True).start()



        elif call.data == "verify_join":

            user_data = get_user_data(user_id)

            if user_data.get("received_welcome_gift", False):

                return bot.answer_callback_query(call.id, "✅ Bạn đã nhận quà rồi!")

                

            config = get_config()

            required_groups = []

            missing_groups = []

            if required_groups:

                for group in required_groups:

                    try:

                        chat_member = bot.get_chat_member(group['username'], user_id)

                        if chat_member.status not in ['member', 'administrator', 'creator']:

                            missing_groups.append(group)

                    except:

                        missing_groups.append(group)

                        

            if not missing_groups:
                # Đã tắt tự động tặng VIP free khi nhận quà chào mừng
                data = load_json(FILES["users"])
                data[str(user_id)]["received_welcome_gift"] = True
                save_json(FILES["users"], data)

                

                bot.delete_message(chat_id, call.message.message_id)

                gift_msg = f"""✅ **XÁC NHẬN THÀNH CÔNG!**

Bạn đã hoàn tất bước xác nhận.

⚠️ Các chức năng VIP chỉ dùng được khi **Admin cấp VIP** cho bạn.

━━━━━━━━━━━━━━━━━━━━━━━━━━"""

                bot.send_message(chat_id, gift_msg, parse_mode="Markdown", reply_markup=get_fixed_menu(user_id))

                bot.answer_callback_query(call.id, "✅ Xác nhận thành công!")

            else:

                bot.answer_callback_query(call.id, "❌ Bạn vẫn chưa tham gia đầy đủ nhóm. Vui lòng kiểm tra lại!", show_alert=True)

        

        elif call.data == "show_referral":

            user_data = get_user_data(user_id)

            referral_code = user_data.get("referral_code")

            if not referral_code:

                referral_code = create_user_referral_code(user_id, call.from_user.first_name or "")

                user_data = get_user_data(user_id)

            

            referral_link = f"https://t.me/{bot.get_me().username}?start=ref_{referral_code}"

            used_referral = user_data.get("used_referral", False)

            referral_stats = user_data.get("referral_stats", {"total_referrals": 0, "total_earned": 0})

            referral_config = get_referral_config()

            

            msg = f"🎁 **MÃ GIỚI THIỆU CỦA BẠN**\n\n"

            msg += f"🔑 **Mã:** `{referral_code}`\n\n"

            msg += f"🔗 **Link giới thiệu:**\n`{referral_link}`\n\n"

            msg += f"💰 **Phần thưởng khi có người dùng mã:**\n"

            

            if referral_config.get("vip_days_referrer", 0) > 0:

                msg += f"👑 +{referral_config['vip_days_referrer']} ngày VIP\n"

            if referral_config.get("deposit_bonus_percent_referrer", 0) > 0:

                msg += f"💰 +{referral_config['deposit_bonus_percent_referrer']}% tiền nạp\n"

            

            if not referral_config.get("vip_days_referrer", 0) and not referral_config.get("deposit_bonus_percent_referrer", 0):

                msg += f"• Đang chờ Admin cấu hình quyền lợi\n"

            

            msg += f"\n📊 **Thống kê:**\n"

            msg += f"👥 Tổng người giới thiệu: {referral_stats.get('total_referrals', 0)}\n\n"

            

            if used_referral:

                referral_by = user_data.get("referral_by", "")

                referral_code_used = user_data.get("referral_code_used", "")

                msg += f"✅ Bạn đã sử dụng mã: `{referral_code_used}`\n"

                msg += f"👤 Từ user: `{referral_by}`\n\n"

            else:

                msg += f"💡 **Chưa sử dụng mã giới thiệu?**\n"

                msg += f"Nhập mã giới thiệu để nhận quyền lợi đặc biệt!\n\n"

            

            msg += f"📤 Chia sẻ link này để nhận thưởng!"

            

            markup = types.InlineKeyboardMarkup()

            markup.add(types.InlineKeyboardButton("📋 Sao chép Link", url=referral_link))

            if not used_referral:

                markup.add(types.InlineKeyboardButton("🎫 Nhập Mã Giới Thiệu", callback_data="enter_referral"))

            

            bot.send_message(chat_id, msg, reply_markup=markup, parse_mode="Markdown")

            bot.answer_callback_query(call.id)

        

        elif call.data == "enter_code":

            bot.send_message(chat_id, "🎫 **NHẬP MÃ KHUYẾN MÃI**\n\nVui lòng nhập mã khuyến mãi:", parse_mode="Markdown")

            temp_user_state[user_id] = {"mode": "enter_code", "step": "wait_code"}

            bot.answer_callback_query(call.id)

        

        elif call.data == "enter_referral":

            bot.send_message(chat_id, "🎁 **NHẬP MÃ GIỚI THIỆU**\n\nVui lòng nhập mã giới thiệu (Mã hoặc UID):", parse_mode="Markdown")

            temp_user_state[user_id] = {"mode": "enter_referral", "step": "wait_referral"}

            bot.answer_callback_query(call.id)

        

        elif call.data == "start_feedback_ai" or call.data == "feedback_reply":

            msg_intro = "🤖 **AI LỄ TÂN:**\nChào bạn! Bạn cần hỗ trợ vấn đề gì về hệ thống? Hãy mô tả chi tiết nhé!"

            if call.data == "feedback_reply":

                msg_intro = "🤖 **AI LỄ TÂN:**\nChào bạn! Bạn muốn phản hồi gì về thông báo này? Mình sẽ ghi nhận và gửi Admin."

            bot.send_message(chat_id, msg_intro)

            temp_user_state[user_id] = {"mode": "feedback_chat", "history": []}

            bot.answer_callback_query(call.id)



        elif call.data.startswith("admin_reply_"):

            t_uid = int(call.data.split("_")[2])

            bot.send_message(chat_id, f"✍️ Nhập nội dung trả lời cho UID `{t_uid}`:")

            temp_user_state[user_id] = {"mode": "admin_replying", "target_uid": t_uid}

            bot.answer_callback_query(call.id)



        elif call.data == "open_admin_panel":

            if _get_subbot_ctx():
                return

            if user_id in ADMIN_IDS:

                show_admin_panel(chat_id, user_id, call.message.message_id)



        elif call.data == "admin_set_group_config":

            if user_id not in ADMIN_IDS: return

            cfg = get_config()

            groups = cfg.get("required_groups", [])

            

            msg = "📢 **DANH SÁCH NHÓM VIP BẮT BUỘC**\n\n"

            if not groups:

                msg += "❌ Hiện chưa có nhóm nào.\n"

            else:

                for i, g in enumerate(groups, 1):

                    msg += f"{i}. 👤 `{g['username']}`\n   🔗 {g['link']}\n\n"

            

            msg += "💡 Người dùng phải tham gia **TẤT CẢ** các nhóm trên để nhận quà VIP."

            

            markup = types.InlineKeyboardMarkup(row_width=1)

            markup.add(types.InlineKeyboardButton("➕ Thêm Nhóm Mới", callback_data="admin_add_group_prompt"))

            for i, g in enumerate(groups):

                markup.add(types.InlineKeyboardButton(f"❌ Xóa Nhóm {i+1}", callback_data=f"admin_del_group_{i}"))

            

            markup.add(types.InlineKeyboardButton("🔙 Quay lại", callback_data="open_admin_panel"))

            bot.edit_message_text(msg, chat_id, call.message.message_id, reply_markup=markup, parse_mode="Markdown")

            bot.answer_callback_query(call.id)



        elif call.data == "admin_add_group_prompt":

            if user_id not in ADMIN_IDS: return

            bot.send_message(chat_id, "✍️ Nhập thông tin nhóm mới theo định dạng:\n`@username | link` (Phải có dấu gạch đứng ở giữa)\n\nVí dụ: `@nhom_cua_ban | https://t.me/nhom_cua_ban`")

            temp_user_state[user_id] = {"mode": "admin_add_group"}

            bot.answer_callback_query(call.id)



        elif call.data.startswith("admin_del_group_"):

            if user_id not in ADMIN_IDS: return

            idx = int(call.data.replace("admin_del_group_", ""))

            cfg = load_json(FILES["config"])

            groups = cfg.get("required_groups", [])

            if 0 <= idx < len(groups):

                removed = groups.pop(idx)

                cfg["required_groups"] = groups

                save_json(FILES["config"], cfg)

                bot.answer_callback_query(call.id, f"✅ Đã xóa {removed['username']}")

                call.data = "admin_set_group_config"

                return handle_callback(call)

            bot.answer_callback_query(call.id, "❌ Lỗi: Không tìm thấy nhóm")



        elif call.data == "admin_edit_group_user":

            if user_id not in ADMIN_IDS: return

            bot.send_message(chat_id, "✍️ Nhập Username nhóm mới (Bắt đầu bằng @):\nVí dụ: `@nhom_cua_ban`")

            temp_user_state[user_id] = {"mode": "admin_edit_group_user"}

            bot.answer_callback_query(call.id)



        elif call.data == "admin_edit_group_link":

            if user_id not in ADMIN_IDS: return

            bot.send_message(chat_id, "✍️ Nhập Link tham gia nhóm mới:\nVí dụ: `https://t.me/joinchat/...` hoặc `https://t.me/nhom_cua_ban`")

            temp_user_state[user_id] = {"mode": "admin_edit_group_link"}

            bot.answer_callback_query(call.id)



        elif call.data == "show_vip_info":

            cfg = get_config()
            bank_txt = cfg.get("bank_info", "Liên hệ Admin")
            base_price = cfg.get("vip_price_30d", 30000)
            u = get_user_data(user_id)
            balance = u.get("balance", 0)

            msg = (
                f"⭐ **NÂNG CẤP VIP**\n\n"
                f"💵 Giá VIP 30 ngày: **{format_vnd(base_price)}**\n"
                f"💰 Số dư hiện tại: **{format_vnd(balance)}**\n\n"
                f"━━━━━━━━━━━━━━\n"
                f"🏦 **THÔNG TIN NẠP TIỀN:**\n"
                f"{bank_txt}\n"
                f"📝 Nội dung CK: `Buy {user_id}`\n"
                f"━━━━━━━━━━━━━━\n\n"
                f"📌 Sau khi chuyển khoản gõ:\n"
                f"`/naptien <số tiền>`\n"
                f"Ví dụ: `/naptien {base_price}`\n\n"
                f"✅ Admin duyệt xong bạn có thể bấm **Mua VIP** để kích hoạt."
            )
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(types.InlineKeyboardButton("💳 Mua VIP bằng số dư", callback_data="buy_vip"))
            markup.add(types.InlineKeyboardButton("🔙 Quay lại Menu", callback_data="back_to_menu"))

            bot.send_message(chat_id, msg, parse_mode="Markdown", reply_markup=markup)
            bot.answer_callback_query(call.id)



        elif call.data == "buy_vip":


            u = get_user_data(user_id)

            cfg = get_config()

            base_price = cfg.get("vip_price_30d", 30000)

            base_days = 30

            today_date = datetime.now().strftime('%Y-%m-%d')

            

            active_codes = get_user_active_codes(user_id)

            discount_code = active_codes.get("discount")

            bonus_days_code = active_codes.get("bonus_days")

            user_data = get_user_data(user_id)

            referral_vip_discount = user_data.get("referral_vip_discount", 0)

            

            final_price = base_price

            final_days = base_days

            discount_valid = False

            bonus_days_valid = False

            total_discount_percent = 0

            

            price_msg = f"💰 **THANH TOÁN VIP**\n\n"

            

            if discount_code:

                expiry_date = discount_code.get("expiry_date", "")

                min_amount = discount_code.get("min_amount", 0)

                

                if expiry_date and expiry_date < today_date:

                    user_data = get_user_data(user_id)

                    user_data["active_discount_code"] = None

                    data = load_json(FILES["users"])

                    data[str(user_id)] = user_data

                    save_json(FILES["users"], data)

                    discount_code = None

                elif min_amount > 0 and base_price < min_amount:

                    discount_valid = False

                else:

                    discount_valid = True

                    total_discount_percent += discount_code.get("value", 0)

            

            if referral_vip_discount > 0:

                total_discount_percent += referral_vip_discount

            

            if total_discount_percent > 0:

                base_decimal = Decimal(str(base_price))

                discount_decimal = base_decimal * Decimal(str(total_discount_percent)) / Decimal("100")

                final_price = int((base_decimal - discount_decimal).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

                price_msg += f"💵 Giá gốc: {format_vnd(base_price)}\n"

                if discount_code and discount_valid:

                    price_msg += f"🎫 Mã giảm giá: `{discount_code.get('code_name')}` ({discount_code.get('value', 0)}%)\n"

                if referral_vip_discount > 0:

                    price_msg += f"🎁 Referral giảm: {referral_vip_discount}%\n"

                price_msg += f"✅ **Giá ưu đãi: {format_vnd(final_price)}**\n\n"

            else:

                price_msg += f"💵 Giá: {format_vnd(base_price)}\n\n"

            

            if bonus_days_code:

                expiry_date = bonus_days_code.get("expiry_date", "")

                if expiry_date and expiry_date < today_date:

                    user_data = get_user_data(user_id)

                    user_data["active_bonus_days_code"] = None

                    data = load_json(FILES["users"])

                    data[str(user_id)] = user_data

                    save_json(FILES["users"], data)

                    bonus_days_code = None

                else:

                    bonus_days_valid = True

                    bonus_days = bonus_days_code.get("value", 0)

                    final_days = base_days + bonus_days

                    price_msg += f"📅 Mua {base_days} ngày tặng thêm {bonus_days} ngày\n"

                    price_msg += f"✅ **Tổng: {final_days} ngày VIP**\n\n"

            

            if not bonus_days_code or not bonus_days_valid:

                price_msg += f"📅 Thời hạn: {base_days} ngày\n\n"

            

            price_msg += f"💳 Số dư hiện tại: {format_vnd(u['balance'])}\n"

            

            if u['balance'] >= final_price:

                markup = types.InlineKeyboardMarkup()

                markup.add(types.InlineKeyboardButton("✅ Xác nhận mua", callback_data=f"confirm_buy_vip_{final_price}_{final_days}"))

                markup.add(types.InlineKeyboardButton("❌ Hủy", callback_data="cancel_buy_vip"))

                bot.send_message(chat_id, price_msg, reply_markup=markup, parse_mode="Markdown")

            else:

                price_msg += f"❌ **Thiếu tiền. Cần thêm: {format_vnd(final_price - u['balance'])}**"

                bot.send_message(chat_id, price_msg, parse_mode="Markdown")

            bot.answer_callback_query(call.id)

        

        elif call.data.startswith("confirm_buy_vip_"):

            parts = call.data.split("_")

            final_price = int(parts[3])

            final_days = int(parts[4])

            

            u = get_user_data(user_id)

            if u['balance'] >= final_price:

                new_b = update_balance(user_id, -final_price)

                exp = set_vip(user_id, final_days)
                sync_vip_to_botcon(user_id, exp)

                user_data = get_user_data(user_id)

                if user_data.get("active_discount_code"):

                    user_data["active_discount_code"] = None

                if user_data.get("active_bonus_days_code"):

                    user_data["active_bonus_days_code"] = None

                data = load_json(FILES["users"])

                data[str(user_id)] = user_data

                save_json(FILES["users"], data)

                

                bot.send_message(chat_id, f"🎉 **LÊN VIP THÀNH CÔNG!**\n\n📅 Hạn: {datetime.fromtimestamp(exp).strftime('%d/%m/%Y')}\n💵 Số dư còn lại: {format_vnd(new_b)}", parse_mode="Markdown")

            else:

                bot.send_message(chat_id, "❌ Số dư không đủ. Vui lòng nạp thêm tiền.")

            bot.answer_callback_query(call.id)

        

        elif call.data.startswith("approve_deposit_"):

            parts = call.data.split("_")

            uid = int(parts[2])

            base_amount = int(parts[3])

            total_amount = int(parts[4])

            bonus_amount = total_amount - base_amount

            

            user_data = get_user_data(uid)

            active_code_name = user_data.get("active_discount_code", None)

            code_info = None

            if active_code_name:

                code_info = get_code(active_code_name)

            

            new_bal = update_balance(uid, total_amount)

            log_user_history(uid, "deposit", total_amount, f"Admin cộng (Gốc: {base_amount}, Bonus: {bonus_amount})")

            

            admin_report = f"✅ **ĐÃ DUYỆT NẠP TIỀN**\n\n"

            admin_report += f"👤 User: `{uid}`\n"

            admin_report += f"💵 Nạp gốc: {format_vnd(base_amount)}\n"

            

            bonus_sources = []

            if active_code_name and code_info:

                bonus_sources.append(f"Mã {active_code_name}")

            

            user_data_check = get_user_data(uid)

            referral_config_check = get_referral_config()

            if user_data_check.get("used_referral") and referral_config_check.get("deposit_bonus_percent_new_user", 0) > 0:

                bonus_sources.append(f"Referral ({referral_config_check['deposit_bonus_percent_new_user']}%)")

            

            if bonus_sources:

                admin_report += f"🎫 Mã áp dụng: {', '.join(bonus_sources)}\n"

                validation_status = "✅ Đạt" if bonus_amount > 0 else "❌ Không đạt"

                admin_report += f"📋 Điều kiện đạt: {validation_status}\n"

                if active_code_name and code_info:

                    if code_info.get("min_amount", 0) > 0:

                        min_check = "✅" if base_amount >= code_info.get("min_amount", 0) else "❌"

                        admin_report += f"   • Tối thiểu {format_vnd(code_info.get('min_amount', 0))}: {min_check}\n"

                    if code_info.get("expiry_date"):

                        expiry_check = "✅" if code_info.get("expiry_date", "") >= datetime.now().strftime('%Y-%m-%d') else "❌"

                        admin_report += f"   • Hạn dùng {code_info.get('expiry_date', '')}: {expiry_check}\n"

                admin_report += f"🎁 Thưởng thêm: {format_vnd(bonus_amount)}\n"

            else:

                admin_report += f"🎫 Mã áp dụng: Không có\n"

                admin_report += f"📋 Điều kiện đạt: N/A\n"

            

            admin_report += f"✅ **Số tiền cuối: {format_vnd(total_amount)}**\n"

            admin_report += f"💵 Số dư: {format_vnd(new_bal)}"

            

            if user_data.get("active_discount_code"):

                user_data["active_discount_code"] = None

                data = load_json(FILES["users"])

                data[str(uid)] = user_data

                save_json(FILES["users"], data)

            

            bot.send_message(chat_id, admin_report, parse_mode="Markdown")

            try: 

                bot.send_message(uid, f"✅ **NẠP TIỀN THÀNH CÔNG!**\n\n💰 Nạp gốc: {format_vnd(base_amount)}\n🎁 Thưởng thêm: {format_vnd(bonus_amount)}\n💵 **Tổng nhận: {format_vnd(total_amount)}**\n\n💳 Số dư: {format_vnd(new_bal)}", parse_mode="Markdown")

            except: pass

            bot.answer_callback_query(call.id)

        

        elif call.data.startswith("cancel_deposit_"):

            parts = call.data.split("_")

            uid = int(parts[2])

            bot.send_message(chat_id, f"❌ Đã hủy yêu cầu nạp tiền cho `{uid}`.", parse_mode="Markdown")

            bot.answer_callback_query(call.id)

        

        elif call.data == "cancel_buy_vip":

            bot.send_message(chat_id, "❌ Đã hủy giao dịch mua VIP.")

            bot.answer_callback_query(call.id)

            

        elif call.data == "info_account":

            u = get_user_data(user_id)

            is_vip, vip_info = check_vip(user_id)

            stats = u.get("stats", {"done": 0, "cancel": 0, "tracking": 0, "money_generated": 0})

            level = u.get("level", 1)

            level_text = "👑 VIP" if level == 2 else "👤 Thường"

            

            vip_status = f"✅ {vip_info}" if is_vip else f"❌ {vip_info}"

            if is_vip and u.get("vip_expiry", 0) > 0:

                expiry_dt = datetime.fromtimestamp(u["vip_expiry"])

                vip_status = f"✅ {vip_info}\n📅 Hết hạn: {expiry_dt.strftime('%d/%m/%Y %H:%M:%S')}"

            

            history = get_user_history(user_id)

            recent_history = history[-5:] if len(history) > 5 else history

            history_text = ""

            if recent_history:

                history_text = "\n\n📜 **LỊCH SỬ GẦN ĐÂY:**\n"

                for h in reversed(recent_history):

                    h_time = datetime.fromtimestamp(h["time"]).strftime('%d/%m/%Y %H:%M')

                    h_type = h["type"]

                    h_amount = format_vnd(h["amount"]) if h["amount"] > 0 else ""

                    h_detail = h.get("detail", "")

                    history_text += f"• {h_time} - {h_type} {h_amount} {h_detail}\n"

            

            msg = f"""👤 **THÔNG TIN TÀI KHOẢN**



🆔 **UID:** `{user_id}`

💰 **Số dư:** {format_vnd(u['balance'])}

{level_text}



👑 **VIP:**

{vip_status}



📊 **THỐNG KÊ:**

✅ Done: {stats['done']}

❌ Cancel: {stats['cancel']}

👀 Đang theo dõi: {stats['tracking']}

💵 Tổng tiền: {format_vnd(stats['money_generated'])}

{history_text}"""

            bot.send_message(chat_id, msg, parse_mode="Markdown")

            bot.answer_callback_query(call.id)



        elif call.data == "stats":

            u = get_user_data(user_id)

            # Facebook Profile
            fb_data   = get_tracking().get(str(chat_id), {})
            fb_active = {k: v for k, v in fb_data.items() if v.get('status') != 'done'}
            fb_live   = sum(1 for v in fb_active.values() if v.get('last_check') == 'LIVE')
            fb_die    = len(fb_active) - fb_live
            fb_val    = sum(v.get('price', 0) for v in fb_active.values() if v.get('last_check') == 'LIVE')

            # TikTok
            tt_data   = get_tracking_tiktok().get(str(chat_id), {})
            tt_active = {k: v for k, v in tt_data.items() if v.get('status') != 'done'}
            tt_live   = sum(1 for v in tt_active.values() if v.get('last_check') in ['EXISTS', 'live'])
            tt_die    = len(tt_active) - tt_live
            tt_val    = sum(v.get('price', 0) for v in tt_active.values() if v.get('last_check') in ['EXISTS', 'live'])

            # Group FB & Instagram
            grig_accounts = grig_dm.get_accounts(user_id)
            gr_active = {k: v for k, v in grig_accounts.items() if v.get('platform') == 'facebook_group'}
            gr_live   = sum(1 for v in gr_active.values() if v.get('status') == 'live')
            gr_die    = len(gr_active) - gr_live
            ig_active = {k: v for k, v in grig_accounts.items() if v.get('platform') == 'instagram'}
            ig_live   = sum(1 for v in ig_active.values() if v.get('status') == 'live')
            ig_die    = len(ig_active) - ig_live

            # Post FB
            post_list = list(_get_fp_watching().items())
            post_live = sum(1 for _, i in post_list if i.get('last_status') == 'live')
            post_die  = len(post_list) - post_live

            # YouTube
            ytb_data  = load_ytb_data().get(str(chat_id), {})
            ytb_live  = sum(1 for ch in ytb_data.values() if ch.get('status') == 'live')
            ytb_die   = len(ytb_data) - ytb_live

            total_uid = len(fb_active) + len(tt_active) + len(gr_active) + len(ig_active) + len(post_list) + len(ytb_data)
            total_val = fb_val + tt_val

            now_str = datetime.now().strftime("%H:%M  %d/%m/%Y")

            msg  = "📊 **THỐNG KÊ**\n\n"
            msg += f"📅 _{now_str}_\n"
            msg += "━━━━━━━━━━━━━━━━━\n\n"

            msg += "📘 **Facebook:**\n"
            msg += f"├ Tổng số: {len(fb_active)}\n"
            msg += f"├ ✅ Live: {fb_live} ({format_vnd(fb_val)})\n"
            msg += f"├ ❌ Die: {fb_die} (0 đ)\n"
            msg += f"└ 💰 Tổng giá trị: {format_vnd(fb_val)}\n\n"

            msg += "🎵 **TikTok:**\n"
            msg += f"├ Tổng số: {len(tt_active)}\n"
            msg += f"├ ✅ Live: {tt_live} ({format_vnd(tt_val)})\n"
            msg += f"├ ❌ Die: {tt_die} (0 đ)\n"
            msg += f"└ 💰 Tổng giá trị: {format_vnd(tt_val)}\n\n"

            msg += "👥 **Group Facebook:**\n"
            msg += f"├ Tổng số: {len(gr_active)}\n"
            msg += f"├ ✅ Live: {gr_live}\n"
            msg += f"└ ❌ Die: {gr_die}\n\n"

            msg += "📷 **Instagram:**\n"
            msg += f"├ Tổng số: {len(ig_active)}\n"
            msg += f"├ ✅ Live: {ig_live}\n"
            msg += f"└ ❌ Die: {ig_die}\n\n"

            msg += "📌 **Post Facebook:**\n"
            msg += f"├ Tổng số: {len(post_list)}\n"
            msg += f"├ ✅ Live: {post_live}\n"
            msg += f"└ ❌ Die: {post_die}\n\n"

            msg += "🎞️ **YouTube:**\n"
            msg += f"├ Tổng số: {len(ytb_data)}\n"
            msg += f"├ ✅ Live: {ytb_live}\n"
            msg += f"└ ❌ Die: {ytb_die}\n\n"

            msg += "━━━━━━━━━━━━━━━━━\n"
            msg += f"📊 **Tổng cộng: {total_uid} UID | {format_vnd(total_val)}**"

            bot.send_message(chat_id, msg, parse_mode="Markdown")
            bot.answer_callback_query(call.id)



        elif call.data == "admin_view_queue":

            if user_id not in ADMIN_IDS: return

            if not support_queue: return bot.answer_callback_query(call.id, "📭 Không có yêu cầu hỗ trợ nào trong hàng chờ.")

            msg = "📋 **DANH SÁCH HÀNG CHỜ HỖ TRỢ:**\n\n"

            markup = types.InlineKeyboardMarkup()

            for w_uid, w_name in support_queue.items():

                msg += f"👤 **{w_name}**\n🆔 ID: `{w_uid}`\n\n"

                markup.add(types.InlineKeyboardButton(f"💬 Kết nối với {w_name}", callback_data=f"connect_{w_uid}"))

            bot.send_message(chat_id, msg, reply_markup=markup, parse_mode="Markdown")

            bot.answer_callback_query(call.id)



        elif call.data.startswith("connect_"):

            if user_id not in ADMIN_IDS: return

            t_uid = int(call.data.split("_")[1])

            if user_id in active_chats: return bot.send_message(chat_id, "❌ Chuyên viên đang trong một hội thoại hỗ trợ khác. Vui lòng kết thúc hội thoại hiện tại trước.")

            if t_uid in support_queue:

                del support_queue[t_uid]

                active_chats[user_id] = t_uid; active_chats[t_uid] = user_id

                markup_end = types.InlineKeyboardMarkup()

                markup_end.add(types.InlineKeyboardButton("🔚 Kết thúc hội thoại hỗ trợ", callback_data="end_chat"))

                bot.send_message(chat_id, f"✅ Đã kết nối với Quý khách (ID: {t_uid}). Hội thoại hỗ trợ đã được thiết lập.", reply_markup=markup_end)

                try: 

                    bot.send_message(t_uid, "👨‍💼 **Chuyên viên đã tham gia hội thoại hỗ trợ**\n\nXin chào Quý khách! Chuyên viên sẵn sàng hỗ trợ bạn. Vui lòng mô tả vấn đề bạn đang gặp phải.", reply_markup=markup_end)

                except: pass

                bot.delete_message(chat_id, call.message.message_id)

            else: bot.answer_callback_query(call.id, "Quý khách đã rời khỏi hàng chờ.")



        elif call.data == "admin_stats_full":

            if user_id not in ADMIN_IDS: return

            s = get_admin_revenue_stats()

            bot.send_message(chat_id, f"📊 **DOANH THU**\n💵 Hôm nay: {format_vnd(s['today'])}\n💰 Tổng: {format_vnd(s['total'])}", parse_mode="Markdown")

            bot.answer_callback_query(call.id)



        elif call.data == "admin_add_guide":

            bot.send_message(chat_id, "ℹ️ **LỆNH ADMIN:**\n`/addmoney <UID> <TIỀN>` - Cộng tiền\n`/setprice <TIỀN>` - Đặt giá VIP\n`/setbank <INFO>` - Cập nhật bank\n`/tangvip <UID> <NGÀY>` - Tặng VIP\n`/free <UID> <NGÀY>` - Tặng VIP miễn phí\n`/freeall <NGÀY>` - Tặng VIP cho tất cả", parse_mode="Markdown")

            bot.answer_callback_query(call.id)



        elif call.data == "admin_manage_users":

            if user_id not in ADMIN_IDS: return

            all_users = get_all_users_list()

            if not all_users:

                bot.send_message(chat_id, "📭 Chưa có user nào.")

                bot.answer_callback_query(call.id)

                return

            msg = f"👥 **DANH SÁCH USER**\n\nTổng: {len(all_users)} user\n\n"

            users_data = load_json(FILES["users"])

            for idx, uid in enumerate(all_users[:20], 1):

                try:

                    u = users_data.get(str(uid), {})

                    balance = u.get("balance", 0)

                    is_vip = u.get("vip_active", False)

                    vip_icon = "👑" if is_vip else "👤"

                    try:

                        chat_member = bot.get_chat_member(uid, uid)

                        user_info = chat_member.user

                        first_name = user_info.first_name or ""

                        last_name = user_info.last_name or ""

                        username = f"@{user_info.username}" if user_info.username else "No Username"

                        full_name = f"{first_name} {last_name}".strip() or "Unknown"

                    except:

                        full_name = "Unknown"

                        username = "No Username"

                    msg += f"{idx}. {vip_icon} **{full_name}**\n"

                    msg += f"   🆔 `{uid}` | 🔗 {username}\n"

                    msg += f"   💰 {format_vnd(balance)}\n\n"

                except: pass

            if len(all_users) > 20:

                msg += f"... và {len(all_users) - 20} user khác\n\n"

            msg += "👇 Chọn user để quản lý:"

            markup = types.InlineKeyboardMarkup(row_width=2)

            for uid in all_users[:20]:

                try:

                    u = users_data.get(str(uid), {})

                    is_vip = u.get("vip_active", False)

                    vip_icon = "👑" if is_vip else "👤"

                    try:

                        chat_member = bot.get_chat_member(uid, uid)

                        user_info = chat_member.user

                        first_name = user_info.first_name or "User"

                    except:

                        first_name = "User"

                    markup.add(types.InlineKeyboardButton(f"{vip_icon} {first_name}", callback_data=f"admin_view_user_{uid}"))

                except: pass

            if len(all_users) > 20:

                markup.add(types.InlineKeyboardButton("📄 Xem thêm...", callback_data="admin_users_page_2"))

            bot.send_message(chat_id, msg, reply_markup=markup, parse_mode="Markdown")

            bot.answer_callback_query(call.id)



        elif call.data.startswith("admin_view_user_"):

            if user_id not in ADMIN_IDS: return

            target_uid = int(call.data.split("_")[3])

            try:

                chat_member = bot.get_chat_member(target_uid, target_uid)

                user_info = chat_member.user

                first_name = user_info.first_name or "Unknown"

                last_name = user_info.last_name or ""

                username = f"@{user_info.username}" if user_info.username else "No Username"

                full_name = f"{first_name} {last_name}".strip() or "Unknown"

                is_bot = user_info.is_bot

                bot_text = "🤖 Bot" if is_bot else "👤 User"

            except:

                full_name = "Unknown"

                username = "No Username"

                bot_text = "👤 User"

            

            u = get_user_data(target_uid)

            is_vip, vip_info = check_vip(target_uid)

            stats = u.get("stats", {"done": 0, "cancel": 0, "tracking": 0, "money_generated": 0})

            level = u.get("level", 1)

            level_text = "👑 VIP" if level == 2 else "👤 Thường"

            

            vip_status = f"✅ {vip_info}" if is_vip else f"❌ {vip_info}"

            if is_vip and u.get("vip_expiry", 0) > 0:

                expiry_dt = datetime.fromtimestamp(u["vip_expiry"])

                vip_status = f"✅ {vip_info}\n📅 Hết hạn: {expiry_dt.strftime('%d/%m/%Y %H:%M:%S')}"

            

            msg = f"""👤 **THÔNG TIN USER ĐẦY ĐỦ**



👤 **Tên:** {full_name}

🆔 **UID:** `{target_uid}`

🔗 **Username:** {username}

{bot_text}



💰 **Số dư:** {format_vnd(u['balance'])}

{level_text}



👑 **VIP:**

{vip_status}



📊 **THỐNG KÊ:**

✅ Done: {stats['done']}

❌ Cancel: {stats['cancel']}

👀 Đang theo dõi: {stats['tracking']}

💵 Tổng tiền: {format_vnd(stats['money_generated'])}"""

            markup = types.InlineKeyboardMarkup(row_width=2)

            markup.add(

                types.InlineKeyboardButton("💰 Cộng tiền", callback_data=f"admin_add_money_{target_uid}"),

                types.InlineKeyboardButton("👑 Tặng VIP", callback_data=f"admin_give_vip_{target_uid}"),

                types.InlineKeyboardButton("⛔ Xóa VIP", callback_data=f"admin_remove_vip_{target_uid}"),

                types.InlineKeyboardButton("🔙 Quay lại", callback_data="admin_manage_users")

            )

            bot.send_message(chat_id, msg, reply_markup=markup, parse_mode="Markdown")

            bot.answer_callback_query(call.id)



        elif call.data.startswith("admin_add_money_"):

            if user_id not in ADMIN_IDS: return

            target_uid = int(call.data.split("_")[3])

            bot.send_message(chat_id, f"💰 Nhập số tiền cộng cho `{target_uid}`:\n\nDùng: `/addmoney {target_uid} <SỐ_TIỀN>`", parse_mode="Markdown")

            bot.answer_callback_query(call.id)



        elif call.data.startswith("admin_give_vip_"):

            if user_id not in ADMIN_IDS: return

            target_uid = int(call.data.split("_")[3])

            bot.send_message(chat_id, f"👑 Nhập số ngày VIP cho `{target_uid}`:\n\nDùng: `/tangvip {target_uid} <SỐ_NGÀY>`", parse_mode="Markdown")

            bot.answer_callback_query(call.id)



        elif call.data.startswith("admin_remove_vip_"):

            if user_id not in ADMIN_IDS: return

            target_uid = int(call.data.split("_")[3])

            set_vip(target_uid, 0)
            sync_vip_to_botcon(target_uid, 0)

            bot.send_message(chat_id, f"⛔ Đã xóa VIP cho `{target_uid}` (bot mẹ + bot con).", parse_mode="Markdown")

            try: bot.send_message(target_uid, "⚠️ VIP bị thu hồi bởi Admin.")

            except: pass

            bot.answer_callback_query(call.id)



        elif call.data == "close_panel":

            bot.delete_message(chat_id, call.message.message_id)



        elif call.data == "deposit":

            cfg = get_config()

            bank_txt = cfg.get("bank_info", "Liên hệ Admin")

            msg = f"💰 **NẠP TIỀN**\n🏦 {bank_txt}\n📝 ND: `Buy {user_id}`\n\n📸 Gõ `/naptien <SỐ TIỀN>` để báo Admin."

            bot.send_message(chat_id, msg, parse_mode="Markdown")

            bot.answer_callback_query(call.id)



        elif call.data == "add_uid":
            if not require_feature_access_call(call, "them_uid_fb", FEATURE_LABELS["them_uid_fb"]):
                return

            bot.send_message(chat_id, "📝 **THÊM UID THƯỜNG**\nNhập UID hoặc Link FB:", parse_mode="Markdown")

            temp_user_state[user_id] = {"mode": "normal", "step": "wait_uid"}

            bot.answer_callback_query(call.id)



        elif call.data == "add_meta":
            if not require_feature_access_call(call, "check_meta", FEATURE_LABELS["check_meta"]):
                return

            bot.send_message(chat_id, "🌟 **CHECK META VERIFIED**\nNhập UID cần Acc Tick xanh hoặc acc chuẩn bị lên Tích Xanh:", parse_mode="Markdown")

            temp_user_state[user_id] = {"mode": "meta", "step": "wait_uid"}

            bot.answer_callback_query(call.id)

        elif call.data == "get_avatar":
            if not require_feature_access_call(call, "get_avatar", FEATURE_LABELS["get_avatar"]):
                return

            bot.answer_callback_query(call.id)

            bot.send_message(

                chat_id, 

                "🖼️ **LẤY AVATAR FACEBOOK**\n\n"

                "Vui lòng gửi link Facebook hoặc UID.\n\n"

                "📝 **Cách sử dụng:**\n"

                "1. Gửi link profile Facebook\n"

                "2. Gửi UID Facebook\n\n",


                parse_mode="Markdown"

            )

            temp_user_state[user_id] = {"mode": "get_avatar", "step": "wait_link"}

        

        elif call.data == "get_cover":
            if not require_feature_access_call(call, "get_cover", FEATURE_LABELS["get_cover"]):
                return

            bot.answer_callback_query(call.id)

            bot.send_message(

                chat_id, 

                "🌉 **LẤY ẢNH BÌA FACEBOOK**\n\n"

                "Vui lòng gửi link Facebook hoặc UID.\n\n"

                "📝 **Cách sử dụng:**\n"

                "1. Gửi link profile Facebook\n"

                "2. Gửi UID Facebook\n\n",

                parse_mode="Markdown"

            )

            temp_user_state[user_id] = {"mode": "get_cover", "step": "wait_link"}

        

        elif call.data == "search_music":
            if not require_feature_access_call(call, "tim_nhac", FEATURE_LABELS["tim_nhac"]):
                return

            bot.answer_callback_query(call.id)
            user_input_state[user_id] = "waiting_for_song_name"
            bot.send_message(
                chat_id, 
                "🎵 **TÌM NHẠC SOUNDCLOUD**\n\n"
                "Nhập tên bài hát hoặc nghệ sĩ bạn muốn tìm:\n\n"
                "💡 Ví dụ: Dừng Thương, See You Again, ...",
                parse_mode="Markdown"
            )
        
        

        elif call.data == "get_2fa":
            if not require_feature_access_call(call, "ma_2fa", FEATURE_LABELS["ma_2fa"]):
                return

            bot.answer_callback_query(call.id)

            bot.send_message(

                chat_id, 

                "🔐 **LẤY MÃ OTP 2FA**\n\n"

                "Vui lòng nhập mã secret 2FA.\n\n"

                "📝 **Cách sử dụng:**\n"

                "1. Nhập mã secret 2FA (dài 32 ký tự)\n"

                "2. Bot sẽ trả về mã OTP 6 số\n\n"


                "⚠️ **Lưu ý:** Mã OTP chỉ có hiệu lực trong 30 giây!",

                parse_mode="Markdown"

            )

            temp_user_state[user_id] = {"mode": "get_2fa", "step": "wait_secret"}

        

        elif call.data == "send_notification_all":

            ctx = _get_subbot_ctx()
            if ctx:
                bot.answer_callback_query(call.id, "⚠️ Chức năng này chỉ dùng được trong bot chính!", show_alert=True)
                return

            if user_id not in ADMIN_IDS:
                bot.answer_callback_query(call.id, "❌ Chỉ Admin mới dùng được chức năng này!", show_alert=True)
                return

            bot.answer_callback_query(call.id)

            total_users = len(get_all_users_list())
            markup_sn = types.InlineKeyboardMarkup(row_width=1)
            markup_sn.add(
                types.InlineKeyboardButton("✏️ Chỉ Gửi Văn Bản", callback_data="sna_text_only"),
                types.InlineKeyboardButton("🖼 Gửi Ảnh + Văn Bản", callback_data="sna_photo_text"),
                types.InlineKeyboardButton("📸 Gửi Ảnh Không Caption", callback_data="sna_photo_only"),
                types.InlineKeyboardButton("❌ Hủy", callback_data="sna_cancel"),
            )
            bot.send_message(
                chat_id,
                f"📢 **GỬI THÔNG BÁO CHO TẤT CẢ USER**\n\n"
                f"👥 Tổng user: **{total_users}**\n\n"
                "Chọn kiểu gửi:",
                parse_mode="Markdown",
                reply_markup=markup_sn
            )

        elif call.data == "sna_text_only":
            if user_id not in ADMIN_IDS: return
            bot.answer_callback_query(call.id)
            bot.send_message(chat_id, "✏️ Nhập nội dung văn bản cần gửi:", parse_mode="Markdown")
            temp_user_state[user_id] = {"mode": "send_notification_all", "step": "wait_text"}

        elif call.data == "sna_photo_text":
            if user_id not in ADMIN_IDS: return
            bot.answer_callback_query(call.id)
            bot.send_message(chat_id, "🖼 Gửi ảnh kèm caption.\nHoặc gửi ảnh trước rồi nhập text sau:", parse_mode="Markdown")
            temp_user_state[user_id] = {"mode": "send_notification_all", "step": "wait_photo_text", "photo_id": None}

        elif call.data == "sna_photo_only":
            if user_id not in ADMIN_IDS: return
            bot.answer_callback_query(call.id)
            bot.send_message(chat_id, "📸 Gửi ảnh lên (không cần caption):", parse_mode="Markdown")
            temp_user_state[user_id] = {"mode": "send_notification_all", "step": "wait_photo_only", "photo_id": None}

        elif call.data == "sna_cancel":
            bot.answer_callback_query(call.id)
            temp_user_state.pop(user_id, None)
            try:
                bot.edit_message_text("❌ Đã hủy gửi thông báo.", chat_id, call.message.message_id)
            except Exception:
                bot.send_message(chat_id, "❌ Đã hủy.")

        elif call.data == "sna_confirm_send":
            if user_id not in ADMIN_IDS: return
            bot.answer_callback_query(call.id, "📢 Đang thông báo...")
            state = temp_user_state.pop(user_id, None)
            if not state:
                return
            try:
                bot.edit_message_reply_markup(chat_id, call.message.message_id, reply_markup=None)
            except:
                pass
            content_val  = state.get("broadcast_content", "")
            photo_id_val = state.get("broadcast_photo_id")
            threading.Thread(
                target=guitn_helper,
                args=(call.message, content_val, photo_id_val),
            daemon=True
            ).start()

        elif call.data == "list_uid":
            bot.answer_callback_query(call.id)
            show_unified_list(chat_id, user_id)



        

        elif call.data == "add_tiktok":
            if not require_feature_access_call(call, "them_tiktok", FEATURE_LABELS["them_tiktok"]):
                return

            bot.send_message(chat_id, "🎵 **THÊM TIKTOK USERNAME**\nNhập TikTok username (có hoặc không có @):\n\nVí dụ: @khaby.lame hoặc khaby.lame", parse_mode="Markdown")

            temp_user_state[user_id] = {"mode": "tiktok", "step": "wait_username"}

            bot.answer_callback_query(call.id)



        elif call.data == "list_tiktok":
            try:
                d = get_tracking_tiktok(); u = d.get(str(chat_id), {})
                active = {k: v for k, v in u.items() if v.get('status') != 'done'}
                if not active:
                    bot.send_message(chat_id, "📋 *DANH SÁCH TIKTOK*\n\nChưa có TikTok nào đang theo dõi.", parse_mode="Markdown")
                else:
                    msg = f"📋 *DANH SÁCH TIKTOK* ({len(active)} tài khoản)\n\n"
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    for username, v in active.items():
                        lc = v.get('last_check', 'DIE')
                        si = "🟢" if lc in ['EXISTS', 'live'] else "🔴"
                        vi = " ☑️" if v.get("verified") else ""
                        su = username.replace("_", r"\_").replace("*", r"\*")
                        sn = str(v.get('name', username))[:25].replace("_", r"\_").replace("*", r"\*")
                        sno = str(v.get('note', ''))[:20].replace("_", r"\_").replace("*", r"\*")
                        msg += f"{si} @{su}{vi}\n   👤 {sn} | 📝 {sno}\n   💵 {format_vnd(v.get('price', 0))}\n\n"
                        markup.add(types.InlineKeyboardButton(f"🗑 Xóa: @{username[:30]}", callback_data=f"del_tiktok_{username[:51]}"))
                    markup.add(types.InlineKeyboardButton("🗑 XÓA TẤT CẢ TIKTOK", callback_data="del_tiktok_all"))
                    bot.send_message(chat_id, msg, parse_mode="Markdown", reply_markup=markup)
                bot.answer_callback_query(call.id)
            except Exception as e:
                print(f"❌ Lỗi list_tiktok: {str(e)}")
                bot.answer_callback_query(call.id, "❌ Lỗi xử lý danh sách.")



        elif call.data.startswith("done_tiktok_"):

            username = call.data.replace("done_tiktok_", "")

            bot.answer_callback_query(call.id)

            if mark_done_tiktok(chat_id, username):

                d = get_tracking_tiktok()

                p = d.get(str(chat_id), {}).get(username, {}).get('price', 0)

                update_user_stats(user_id, "done", p)

                safe_username = username.replace("_", "\\_").replace("*", "\\*")

                safe_edit_message(chat_id, call.message.message_id, f"✅ **LỤM LÚA!**\nTikTok @{safe_username} done.")



        elif call.data.startswith("del_tiktok_"):
            username = call.data.replace("del_tiktok_", "")
            if username == "all":
                d = get_tracking_tiktok()
                if str(chat_id) in d: d[str(chat_id)] = {}; save_json(FILES["tracking_tiktok"], d)
                try: bot.delete_message(chat_id, call.message.message_id)
                except: pass
                bot.answer_callback_query(call.id, "✅ Đã xóa toàn bộ TikTok!")
                bot.send_message(chat_id, "🗑 Đã xóa toàn bộ danh sách TikTok.")
            else:
                if remove_tracking_tiktok(chat_id, username):
                    update_user_stats(user_id, "cancel")
                    bot.answer_callback_query(call.id, f"✅ Đã xóa @{username}!")
                    d2 = get_tracking_tiktok()
                    ac2 = {k: v for k, v in d2.get(str(chat_id), {}).items() if v.get('status') != 'done'}
                    if not ac2:
                        try: bot.delete_message(chat_id, call.message.message_id)
                        except: pass
                        bot.send_message(chat_id, "📋 *DANH SÁCH TIKTOK*\n\nĐã xóa hết.", parse_mode="Markdown")
                    else:
                        m2 = f"📋 *DANH SÁCH TIKTOK* ({len(ac2)} tài khoản)\n\n"
                        mk2 = types.InlineKeyboardMarkup(row_width=1)
                        for un2, vv2 in ac2.items():
                            si2 = "🟢" if vv2.get('last_check') in ['EXISTS','live'] else "🔴"
                            su2 = un2.replace("_", r"\_").replace("*", r"\*")
                            sn2 = str(vv2.get('name', un2))[:25].replace("_", r"\_").replace("*", r"\*")
                            m2 += f"{si2} @{su2} | 👤 {sn2}\n   💵 {format_vnd(vv2.get('price',0))}\n\n"
                            mk2.add(types.InlineKeyboardButton(f"🗑 Xóa: @{un2[:30]}", callback_data=f"del_tiktok_{un2[:51]}"))
                        mk2.add(types.InlineKeyboardButton("🗑 XÓA TẤT CẢ TIKTOK", callback_data="del_tiktok_all"))
                        try: bot.edit_message_text(m2, chat_id, call.message.message_id, parse_mode="Markdown", reply_markup=mk2)
                        except: bot.send_message(chat_id, m2, parse_mode="Markdown", reply_markup=mk2)
                else:
                    bot.answer_callback_query(call.id, "⚠️ Không tìm thấy!")

        elif call.data.startswith("del_uid_"):
            uid = call.data.replace("del_uid_", "")
            if uid == "all":
                d = get_tracking()
                if str(chat_id) in d: d[str(chat_id)] = {}; save_json(FILES["tracking"], d)
                try: bot.delete_message(chat_id, call.message.message_id)
                except: pass
                bot.answer_callback_query(call.id, "✅ Đã xóa toàn bộ UID!")
                bot.send_message(chat_id, "🗑 Đã xóa toàn bộ danh sách UID FB.")
            else:
                if remove_tracking_uid(chat_id, uid):
                    update_user_stats(user_id, "cancel")
                    bot.answer_callback_query(call.id, f"✅ Đã xóa UID {uid}!")
                    d3 = get_tracking()
                    ac3 = {k: v for k, v in d3.get(str(chat_id), {}).items() if v.get('status') != 'done'}
                    if not ac3:
                        try: bot.delete_message(chat_id, call.message.message_id)
                        except: pass
                        bot.send_message(chat_id, "📋 *DANH SÁCH UID FB*\n\nĐã xóa hết.", parse_mode="Markdown")
                    else:
                        m3 = f"📋 *DANH SÁCH UID FB* ({len(ac3)} UID)\n\n"
                        mk3 = types.InlineKeyboardMarkup(row_width=1)
                        for k3, v3 in ac3.items():
                            si3 = "💎" if v3.get("track_type")=="meta" else ("🟢" if v3.get('last_check')=='LIVE' else "🔴")
                            ti3 = " ☑️" if v3.get("is_verified") else ""
                            sn3 = str(v3.get('name', k3))[:30].replace("_", r"\_").replace("*", r"\*")
                            m3 += f"{si3} `{k3}`{ti3} — {sn3}\n"
                            mk3.add(types.InlineKeyboardButton(f"🗑 Xóa: {str(v3.get('name',k3))[:25]}", callback_data=f"del_uid_{k3}"))
                        mk3.add(types.InlineKeyboardButton("🗑 XÓA TẤT CẢ", callback_data="del_uid_all"))
                        try: bot.edit_message_text(m3, chat_id, call.message.message_id, parse_mode="Markdown", reply_markup=mk3)
                        except: bot.send_message(chat_id, m3, parse_mode="Markdown", reply_markup=mk3)
                else:
                    bot.answer_callback_query(call.id, "⚠️ Không tìm thấy UID!")





        elif call.data.startswith("done_"):

            uid = call.data.split("_")[1]

            bot.answer_callback_query(call.id)

            if mark_done_uid(chat_id, uid):

                d = get_tracking(); p = d.get(str(chat_id), {}).get(uid, {}).get('price', 0)

                update_user_stats(user_id, "done", p)

                safe_edit_message(chat_id, call.message.message_id, f"✅ **LỤM LÚA!**\nUID `{uid}` done.")



        elif call.data.startswith("del_"):

            uid = call.data.split("_")[1]

            if remove_tracking_uid(chat_id, uid):

                update_user_stats(user_id, "cancel")

                bot.delete_message(chat_id, call.message.message_id)

                bot.answer_callback_query(call.id, "✅ Đã xóa!")



        elif call.data.startswith("cancel_"):

            # Handler cho nút "Hủy kèo" - giống del_

            uid = call.data.split("_")[1]

            if remove_tracking_uid(chat_id, uid):

                update_user_stats(user_id, "cancel")

                bot.delete_message(chat_id, call.message.message_id)

                bot.answer_callback_query(call.id, "✅ Đã hủy kèo!")



        elif call.data.startswith("update_"):

            # Handler cho nút "Cập nhật"

            uid = call.data.split("_")[1]

            bot.answer_callback_query(call.id, "🔄 Đang cập nhật...")

            try:

                # Kiểm tra lại trạng thái UID

                stat = check_uid_live_die(uid)

                current_status = "live" if stat == "LIVE" else "die"

                

                # Lấy thông tin từ tracking

                d = get_tracking()

                account_info = d.get(str(chat_id), {}).get(uid, {})

                

                if account_info:

                    # Cập nhật trạng thái mới

                    account_info['last_check'] = current_status.upper()

                    save_json(FILES["tracking"], d)

                    

                    # Tạo message cập nhật

                    ten_tai_khoan = account_info.get('name', 'Facebook User')

                    ghi_chu = account_info.get('note', 'Không có ghi chú')

                    

                    if current_status == "live":

                        icon_trang_thai2 = "🟢"

                        chu_trang_thai = "ĐANG HOẠT ĐỘNG"

                    else:

                        icon_trang_thai2 = "🔴"

                        chu_trang_thai = "ĐÃ BỊ KHÓA❌"

                    

                    # Escape cho MarkdownV2

                    ten_tai_khoan_escaped = escape_markdown_v2(ten_tai_khoan)

                    uid_escaped = escape_markdown_v2(uid)

                    ghi_chu_escaped = escape_markdown_v2(ghi_chu)

                    link_tai_khoan = f"https://facebook\\.com/{uid_escaped}"

                    thoi_gian_escaped = escape_markdown_v2(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))

                    

                    ket_qua = (

                        f"📘 FACEBOOK PROFILE\n"

                        f"👤 *Tên:* ||{ten_tai_khoan_escaped}||\n"

                        f"🔎 *UID:* ||{uid_escaped}|| \\- [Link]({link_tai_khoan})\n"

                        f"{icon_trang_thai2} *Trạng thái:* {chu_trang_thai}\n"

                        f"📝 *Ghi chú:* {ghi_chu_escaped}\n"


                        f"📊 *Tiến trình:* Đang theo dõi chờ {'DIE ❌' if current_status == 'live' else 'LIVE ✅'}\n"

                        f"👤 *Hạn trả kèo:* Vĩnh viễn"

                    )

                    

                    keyboard = types.InlineKeyboardMarkup(row_width=2)

                    keyboard.row(

                        types.InlineKeyboardButton("🔔 Cập nhật", callback_data=f"update_{uid}"),

                        types.InlineKeyboardButton("📋 Danh Sách UID", callback_data=f"list_uid")

                    )

                    keyboard.row(

                        types.InlineKeyboardButton("❌ Hủy kèo", callback_data=f"cancel_{uid}"),

                        types.InlineKeyboardButton("✅ Done kèo", callback_data=f"done_{uid}")

                    )

                    

                    # Cập nhật message
                    try:
                        bot.edit_message_caption(
                            chat_id=chat_id,
                            message_id=call.message.message_id,
                            caption=ket_qua,
                            parse_mode='MarkdownV2',
                            reply_markup=keyboard
                        )
                        bot.answer_callback_query(call.id, "✅ Cập nhật thành công!")
                    except Exception as e_cap:
                        if "message is not modified" in str(e_cap).lower():
                            bot.answer_callback_query(call.id, "ℹ️ Trạng thái không thay đổi!")
                        else:
                            try:
                                bot.edit_message_text(
                                    chat_id=chat_id,
                                    message_id=call.message.message_id,
                                    text=ket_qua,
                                    parse_mode='MarkdownV2',
                                    reply_markup=keyboard
                                )
                                bot.answer_callback_query(call.id, "✅ Cập nhật thành công!")
                            except Exception as e_text:
                                if "message is not modified" in str(e_text).lower():
                                    bot.answer_callback_query(call.id, "ℹ️ Trạng thái không thay đổi!")
                                else:
                                    print(f"Lỗi edit_message_text: {e_text}")
                                    bot.answer_callback_query(call.id, "❌ Lỗi khi cập nhật!", show_alert=True)

                else:
                    bot.answer_callback_query(call.id, "❌ Không tìm thấy UID này!", show_alert=True)

            except Exception as e:
                print(f"Lỗi update handler: {e}")
                bot.answer_callback_query(call.id, "❌ Lỗi hệ thống khi cập nhật!", show_alert=True)



        elif call.data == "add_ytb":
            if not require_feature_access_call(call, "them_youtube", FEATURE_LABELS["them_youtube"]):
                return

            temp_user_state[user_id] = {"mode": "add_ytb", "step": "wait_url"}
            bot.send_message(chat_id, "📺 <b>THÊM KÊNH YOUTUBE</b>\n\nVui lòng dán link kênh YouTube:\nVí dụ: https://youtube.com/@channelname", parse_mode="HTML")
            bot.answer_callback_query(call.id)

        elif call.data == "list_ytb":
            data = load_ytb_data()
            channels = data.get(str(chat_id), {})
            if not channels:
                bot.send_message(chat_id, "📋 Bạn chưa theo dõi kênh YouTube nào!\n\nBấm <b>📺 Thêm YTB</b> để thêm kênh.", parse_mode="HTML")
            else:
                msg = "📋 <b>DANH SÁCH KÊNH YOUTUBE ĐANG THEO DÕI:</b>\n\n"
                markup = types.InlineKeyboardMarkup(row_width=1)
                for idx, (url, ch_data) in enumerate(channels.items(), 1):
                    status_icon = "🟢" if ch_data.get("status") == "live" else "🔴"
                    status_text = "ĐANG HOẠT ĐỘNG" if ch_data.get("status") == "live" else "ĐÃ DIE ❌"
                    msg += f"{idx}. {status_icon} <b>{ch_data['title']}</b>\n"
                    msg += f"   🔗 {url}\n"
                    msg += f"   📊 {status_text}\n"
                    msg += f"   🕐 Kiểm tra: {ch_data.get('last_check', 'N/A')}\n\n"
                    markup.add(types.InlineKeyboardButton(
                        f"🗑 Xóa: {ch_data['title'][:30]}",
                        callback_data=f"ytb_remove_{ch_data['channel_id']}"
                    ))
                msg += f"📊 Tổng: {len(channels)} kênh | Kiểm tra mỗi {YTB_CHECK_INTERVAL}s"
                bot.send_message(chat_id, msg, parse_mode="HTML", reply_markup=markup)
            bot.answer_callback_query(call.id)

        elif call.data == "grig_add_group_inline":
            if not require_feature_access_call(call, "them_group_fb", FEATURE_LABELS["them_group_fb"]):
                return

            bot.answer_callback_query(call.id)
            bot.send_message(chat_id,
                "👥 *THÊM FACEBOOK GROUP THEO DÕI*\n\n"
                "Dùng lệnh:\n"
                "`/addpgr <link> | <ghi chú>`\n\n"
                "Ví dụ:\n"
                "`/addpgr https://facebook.com/groups/123456 | Nhóm ABC`",
                parse_mode='Markdown')

        elif call.data == "grig_add_ig_inline":
            if not require_feature_access_call(call, "them_instagram", FEATURE_LABELS["them_instagram"]):
                return

            bot.answer_callback_query(call.id)
            bot.send_message(chat_id,
                "📷 *THÊM INSTAGRAM THEO DÕI*\n\n"
                "Dùng lệnh:\n"
                "`/add <link> | <ghi chú>`\n\n"
                "Ví dụ:\n"
                "`/add https://instagram.com/username | Check kèo`",
                parse_mode='Markdown')

        elif call.data.startswith("fpadd|"):
            if not require_feature_access_call(call, "them_post_fb", FEATURE_LABELS["them_post_fb"]):
                return
            try:
                parts = call.data.split("|")
                short_key = parts[1]
                interval = int(parts[2])
                url = _get_fp_url_cache().get(short_key)
                if not url:
                    bot.answer_callback_query(call.id, "⚠️ Link hết hạn, dán lại nhé!", show_alert=True)
                    return
                if url in _get_fp_watching():
                    bot.answer_callback_query(call.id, "⚠️ URL này đã theo dõi rồi!")
                    return
                fbpost_start_monitor(url, interval, chat_id, "")
                interval_text = f"{interval}s" if interval < 60 else f"{interval // 60} phút"
                bot.answer_callback_query(call.id, "✅ Đang check lần đầu...")
                bot.edit_message_text(
                    f"✅ *Đã thêm theo dõi Post FB!*\n🔗 {url}\n⏱ Check mỗi: {interval_text}\n\n⏳ Đang check trạng thái lần đầu (~10s)...\n🔔 Sẽ tự động báo kết quả",
                    call.message.chat.id, call.message.message_id, parse_mode="Markdown"
                )
                _get_fp_url_cache().pop(short_key, None)
            except Exception as e:
                bot.answer_callback_query(call.id, f"❌ Lỗi: {e}", show_alert=True)

        elif call.data == "fbpost_open_add":
            if not require_feature_access_call(call, "them_post_fb", FEATURE_LABELS["them_post_fb"]):
                return

            bot.answer_callback_query(call.id)
            bot.send_message(chat_id,
                "📘 *THÊM POST FB THEO DÕI*\n\n"
                "Dán link bài post FB vào chat → bot tự hỏi interval.\n\n"
                "Hoặc dùng lệnh:\n"
                "`/addpost <url> [giây] [nhãn kèo]`\n\n"
                "Ví dụ:\n"
                "`/addpost https://facebook.com/share/p/abc 60 Kèo sáng`",
                parse_mode="Markdown")

        elif call.data == "fbpost_open_list":
            bot.answer_callback_query(call.id)
            if not _get_fp_watching():
                bot.send_message(chat_id, "📭 Chưa có Post FB nào đang theo dõi.\nDán link FB vào chat hoặc dùng /addpost")
            else:
                markup_fp = types.InlineKeyboardMarkup(row_width=1)
                lines_fp = [f"📋 *Đang theo dõi {len(_get_fp_watching())} Post FB:*\n"]
                for i, (fp_url, fp_info) in enumerate(list(_get_fp_watching().items())[:20], 1):
                    fp_label = fp_info.get("label", "")
                    fp_lbl = f" [{fp_label}]" if fp_label else ""
                    lines_fp.append(f"{i}. {fp_url[:60]}{fp_lbl}\n   ⏱ {fp_info['interval']}s | 📊 {fp_info.get('last_status','?')}")
                    fp_uid_key = fp_url.replace("|", "_")[:50]
                    markup_fp.add(types.InlineKeyboardButton(f"🗑 Xóa #{i}", callback_data=f"fbpost_del_{fp_uid_key}"))
                markup_fp.add(types.InlineKeyboardButton("🗑 Xóa TẤT CẢ", callback_data="fbpost_removeall"))
                bot.send_message(chat_id, "\n".join(lines_fp), parse_mode="Markdown", reply_markup=markup_fp)

        elif call.data == "fbpost_removeall":
            for fp_info in _get_fp_watching().values():
                try:
                    fp_info["task"].cancel()
                except Exception:
                    pass
            _get_fp_watching().clear()
            bot.answer_callback_query(call.id, "✅ Đã xóa tất cả!")
            try:
                bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
            except Exception:
                pass

        elif call.data.startswith("fbpost_done_"):
            bot.answer_callback_query(call.id, "✅ Done kèo!")
            try:
                new_cap = (call.message.caption or call.message.text or "") + "\n\n✅ DONE KÈO!"
                if call.message.caption:
                    bot.edit_message_caption(new_cap, call.message.chat.id, call.message.message_id, parse_mode="Markdown", reply_markup=None)
                else:
                    bot.edit_message_text(new_cap, call.message.chat.id, call.message.message_id, parse_mode="Markdown", reply_markup=None)
            except Exception:
                try:
                    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
                except Exception:
                    pass

        elif call.data.startswith("fbpost_cancel_"):
            bot.answer_callback_query(call.id, "❌ Hủy kèo!")
            try:
                new_cap = (call.message.caption or call.message.text or "") + "\n\n❌ HỦY KÈO!"
                if call.message.caption:
                    bot.edit_message_caption(new_cap, call.message.chat.id, call.message.message_id, parse_mode="Markdown", reply_markup=None)
                else:
                    bot.edit_message_text(new_cap, call.message.chat.id, call.message.message_id, parse_mode="Markdown", reply_markup=None)
            except Exception:
                try:
                    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
                except Exception:
                    pass

        elif call.data.startswith("fbpost_del_"):
            uid_key = call.data.replace("fbpost_del_", "")
            found_url = None
            for fp_u in list(_get_fp_watching().keys()):
                if fp_u.replace("|", "_")[:50] == uid_key:
                    found_url = fp_u
                    break
            if found_url:
                try:
                    _get_fp_watching()[found_url]["task"].cancel()
                except Exception:
                    pass
                del _get_fp_watching()[found_url]
                bot.answer_callback_query(call.id, "🗑 Đã xóa URL!")
                try:
                    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
                except Exception:
                    pass
            else:
                bot.answer_callback_query(call.id, "⚠️ Không tìm thấy!", show_alert=True)

        elif call.data.startswith("ytb_done_"):
            channel_id = call.data.replace("ytb_done_", "")
            data = load_ytb_data()
            channels = data.get(str(chat_id), {})
            removed = False
            for url in list(channels.keys()):
                if channels[url].get("channel_id") == channel_id:
                    del channels[url]
                    removed = True
                    break
            if removed:
                data[str(chat_id)] = channels
                if not channels:
                    del data[str(chat_id)]
                save_ytb_data(data)
                try:
                    bot.edit_message_caption(
                        caption=(call.message.caption or "") + "\n\n✅ <b>DONE - Đã dừng theo dõi kênh này!</b>",
                        chat_id=chat_id, message_id=call.message.message_id, parse_mode="HTML"
                    )
                except:
                    bot.send_message(chat_id, "✅ Đã DONE kênh YouTube!")
            bot.answer_callback_query(call.id, "✅ Done!")

        elif call.data.startswith("ytb_del_") or call.data.startswith("ytb_remove_"):
            if call.data.startswith("ytb_del_"):
                channel_id = call.data.replace("ytb_del_", "")
            else:
                channel_id = call.data.replace("ytb_remove_", "")
            data = load_ytb_data()
            channels = data.get(str(chat_id), {})
            removed = False
            for url in list(channels.keys()):
                if channels[url].get("channel_id") == channel_id:
                    del channels[url]
                    removed = True
                    break
            if removed:
                data[str(chat_id)] = channels
                if not channels:
                    del data[str(chat_id)]
                save_ytb_data(data)
                try:
                    bot.delete_message(chat_id, call.message.message_id)
                except: pass
                bot.answer_callback_query(call.id, "✅ Đã xóa kênh!")
            else:
                bot.answer_callback_query(call.id, "❌ Không tìm thấy!")

        elif call.data.startswith("ytb_keep_"):
            try:
                bot.edit_message_caption(
                    caption=(call.message.caption or "") + "\n\n🔔 <b>Tiếp tục theo dõi!</b>",
                    chat_id=chat_id, message_id=call.message.message_id, parse_mode="HTML"
                )
            except: pass
            bot.answer_callback_query(call.id, "🔔 Tiếp tục theo dõi!")

        elif call.data.startswith("keep_"):
            uid = call.data[len("keep_"):]
            bot.answer_callback_query(call.id, "✅ Đang tiếp tục theo dõi đến khi sống lại!")
            try:
                _d = load_json(FILES["tracking"])
                _cid_str = str(chat_id)
                if _cid_str in _d and uid in _d[_cid_str]:
                    _changed = False
                    # Reset status về tracking
                    if _d[_cid_str][uid].get("status") in ("done", "waiting"):
                        _d[_cid_str][uid]["status"] = "tracking"
                        _changed = True
                    # Đảm bảo last_notified_status = last_check (trạng thái hiện tại đã biết)
                    # Để lần check tiếp khi trạng thái đổi sẽ báo ngay
                    _curr_known = _d[_cid_str][uid].get("last_check", "UNKNOWN")
                    if _curr_known in ("DIE", "LIVE"):
                        _d[_cid_str][uid]["last_notified_status"] = _curr_known
                        _changed = True
                    if _changed:
                        save_json(FILES["tracking"], _d)
                    bot.send_message(chat_id,
                        f"👁 Đang theo dõi UID `{uid}` đến khi *sống lại*\\.\n"
                        f"Bạn sẽ được thông báo ngay khi acc mở trở lại\\! 🔔",
                        parse_mode="MarkdownV2")
            except Exception as _e:
                print(f"[keep_] Lỗi: {_e}")

        elif call.data == "end_chat":

            if user_id in active_chats:

                partner_id = active_chats[user_id]

                del active_chats[user_id]

                if partner_id in active_chats:

                    del active_chats[partner_id]

                if user_id in ADMIN_IDS:

                    bot.send_message(chat_id, "✅ Đã kết thúc hội thoại hỗ trợ với Quý khách.")

                    try: bot.send_message(partner_id, "👋 Chuyên viên đã kết thúc hội thoại hỗ trợ. Cảm ơn Quý khách đã sử dụng dịch vụ!")

                    except: pass

                else:

                    bot.send_message(chat_id, "✅ Đã kết thúc hội thoại hỗ trợ. Cảm ơn Quý khách đã sử dụng dịch vụ!")

                    try: bot.send_message(partner_id, "👋 Quý khách đã kết thúc hội thoại hỗ trợ.")

                    except: pass

            else:

                bot.answer_callback_query(call.id, "❌ Không đang trong hội thoại hỗ trợ.")

        elif call.data == "help": bot.send_message(chat_id, "ℹ️ Nạp -> Mua VIP -> Thêm UID."); bot.answer_callback_query(call.id)

    except Exception as e:

        err = str(e)
        if _tg_error_benign(err):
            return
        print(f"❌ Lỗi callback handler [{getattr(call, 'data', '?')}]: {err}")
        _safe_callback_ack(call, "❌ Lỗi hệ thống.", show_alert=True)



# ===== HELPER FUNCTIONS - Không dùng command nữa, chỉ qua nút =====



def getavt_helper(message, link_or_uid):

    """Lấy avatar Facebook - không dùng command"""

    try:

        processing_msg = bot.reply_to(message, f"⏳ Đang lấy avatar từ: {link_or_uid}")

        

        uid = get_id(link_or_uid)

        if not uid:

            bot.edit_message_text(

                f"❌ Không lấy được UID từ link: {link_or_uid}",

                processing_msg.chat.id,

                processing_msg.message_id

            )

            return

        

        # Dùng get_facebook_avatar_bytes để lấy bytes trực tiếp (có đầy đủ fallback API)
        avatar_bytes = get_facebook_avatar_bytes(uid)

        if not avatar_bytes:

            bot.edit_message_text(

                f"❌ Không lấy được avatar cho UID: {uid}\n"
                f"💡 Tài khoản có thể đã khóa ảnh đại diện hoặc UID không tồn tại.",

                processing_msg.chat.id,

                processing_msg.message_id

            )

            return

        

        from io import BytesIO as _AVBIO
        bot.send_photo(

            message.chat.id,

            _AVBIO(avatar_bytes),

            caption=f"✅ Avatar Facebook\n🆔 UID: {uid}"

        )

        

        bot.delete_message(processing_msg.chat.id, processing_msg.message_id)

        

    except Exception as e:

        bot.reply_to(message, f"❌ Lỗi khi xử lý: {str(e)[:100]}")

        print(f"❌ Lỗi getavt_helper: {str(e)}")



def getbia_helper(message, link_or_uid):

    """Lấy ảnh bìa Facebook - không dùng command"""

    try:

        processing_msg = bot.reply_to(message, f"⏳ Đang lấy ảnh bìa từ: {link_or_uid}")

        

        uid = get_id(link_or_uid)

        if not uid:

            bot.edit_message_text(

                f"❌ Không lấy được UID từ link: {link_or_uid}",

                processing_msg.chat.id,

                processing_msg.message_id

            )

            return

        

        temp_image_path = get_facebook_cover(uid)

        if not temp_image_path:

            bot.edit_message_text(

                f"❌ Không lấy được ảnh bìa cho UID: {uid}",

                processing_msg.chat.id,

                processing_msg.message_id

            )

            return

        

        with open(temp_image_path, 'rb') as photo:

            bot.send_photo(

                message.chat.id,

                photo,

                caption=f"✅ Ảnh bìa Facebook (UID: {uid})"

            )

        

        bot.delete_message(processing_msg.chat.id, processing_msg.message_id)

        

        if os.path.exists(temp_image_path):

            os.remove(temp_image_path)

        

    except Exception as e:

        bot.reply_to(message, f"❌ Lỗi khi xử lý: {str(e)[:100]}")

        print(f"❌ Lỗi getbia_helper: {str(e)}")



def get2fa_helper(message, secret):
    """Lấy mã 2FA dùng pyotp - tính trực tiếp, không cần API ngoài"""
    try:
        import pyotp, time as _t, re as _re
        # Làm sạch secret: bỏ khoảng trắng, dấu gạch ngang, chuyển hoa
        secret_clean = _re.sub(r'[^A-Z2-7=]', '', secret.upper().replace(' ', '').replace('-', ''))
        if len(secret_clean) < 8:
            bot.reply_to(message, "❌ <b>Secret không hợp lệ!</b>\nSecret phải là chuỗi Base32 (chứa chữ A-Z và số 2-7).\nVí dụ: <code>JBSWY3DPEHPK3PXP</code>", parse_mode="HTML")
            return
        totp = pyotp.TOTP(secret_clean)
        otp_code = totp.now()
        # Tính thời gian còn lại của mã
        remaining = 30 - (int(_t.time()) % 30)
        bot.reply_to(
            message,
            f"✅ <b>Mã OTP (2FA) của bạn:</b>\n\n"
            f"🔐 <code>{otp_code}</code>\n\n"
            f"⏱ Còn hiệu lực: <b>{remaining} giây</b>\n"
            f"📝 Secret: <code>{secret_clean[:10]}...</code>",
            parse_mode="HTML"
        )
    except Exception as e:
        bot.reply_to(message, f"❌ Lỗi không xác định: {str(e)[:100]}")
        print(f"❌ Lỗi get2fa_helper: {str(e)}")



def guitn_helper(message, content, photo_id=None):
    """Gửi thông báo cho tất cả user — ổn định hơn, có retry và progress."""
    try:
        raw_users = get_all_users_list()
        cleaned_users = []
        seen = set()
        for uid in raw_users:
            try:
                uid_int = int(uid)
            except Exception:
                continue
            if uid_int > 0 and uid_int not in seen:
                seen.add(uid_int)
                cleaned_users.append(uid_int)

        if not cleaned_users:
            bot.reply_to(message, "⚠️ Chưa có user nào trong danh sách!")
            return

        content = (content or "").strip()
        time_str = datetime.now().strftime('%H:%M:%S - %d/%m/%Y')
        notification = (
            f"📢 THÔNG BÁO\n{'='*26}\n\n{content}\n\n{'='*26}\n⏰ {time_str}"
            if content else
            f"📢 THÔNG BÁO\n⏰ {time_str}"
        )

        total = len(cleaned_users)
        success = 0
        fail = 0
        progress_msg = bot.reply_to(message, f"📤 Đang gửi... 0/{total}")
        last_edit = 0

        def _send_one(target_id):
            if photo_id:
                try:
                    bot.send_photo(target_id, photo_id, caption=notification[:1024])
                    return True
                except Exception:
                    if content:
                        bot.send_message(target_id, notification, disable_web_page_preview=True)
                        return True
                    raise
            bot.send_message(target_id, notification, disable_web_page_preview=True)
            return True

        for idx, uid in enumerate(cleaned_users, 1):
            ok = False
            for _ in range(2):
                try:
                    _send_one(uid)
                    ok = True
                    break
                except Exception:
                    time.sleep(0.2)
            if ok:
                success += 1
            else:
                fail += 1

            if (idx == total) or (time.time() - last_edit >= 1.5):
                try:
                    pct = int(idx / total * 100)
                    bar = "█" * (pct // 10) + "░" * (10 - pct // 10)
                    bot.edit_message_text(
                        f"📤 Đang gửi...\n\n[{bar}] {pct}%\n✅ {success} | ❌ {fail}\n📊 {idx}/{total}",
                        message.chat.id, progress_msg.message_id
                    )
                except Exception:
                    pass
                last_edit = time.time()
            time.sleep(0.05)

        try:
            bot.edit_message_text(
                f"✅ **GỬI XONG!**\n\n"
                f"📊 Tổng: {total}\n✅ Thành công: {success}\n❌ Thất bại: {fail}\n"
                f"📸 Có ảnh: {'Có' if photo_id else 'Không'}",
                message.chat.id, progress_msg.message_id, parse_mode="Markdown"
            )
        except Exception:
            bot.reply_to(message, f"✅ Đã gửi {success}/{total} người.")

    except Exception as e:
        print(f"Lỗi guitn_helper: {e}")
        bot.reply_to(message, f"❌ Lỗi: {str(e)[:100]}")


@bot.message_handler(commands=['donate'])
def cmd_donate(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    qr_url = f"https://img.vietqr.io/image/MB-0862197064-compact2.png?amount=0&addInfo=DH%20Donate%20{user_id}&accountName=NGUYEN%20MAI%20NIN"
    caption = (
        "💝 *ỦNG HỘ DUY TRÌ SERVER*\n"
        "─────────────────\n"
        "🏦 NH: MB Bank\n"
        "💳 STK: `0862197064`\n"
        "👤 CTK: NGUYỄN MAI NIN\n"
        f"📝 ND: `DH Donate {user_id}`\n"
        "─────────────────\n"
        "💖 Cảm ơn bạn đã ủng hộ bot!\n"
        "ℹ️ _Donate không tự động check_"
    )
    mk_donate = types.InlineKeyboardMarkup()
    mk_donate.add(types.InlineKeyboardButton("💳 Sao chép STK: 0862197064", callback_data="donate_copy_stk"))
    try:
        bot.send_photo(chat_id, qr_url, caption=caption, parse_mode="Markdown", reply_markup=mk_donate)
    except:
        bot.send_message(chat_id, caption, parse_mode="Markdown", reply_markup=mk_donate)

@bot.message_handler(commands=['resetmenu'])
def cmd_resetmenu(message):
    """Ẩn bàn phím dưới và gửi lại menu inline kiểu cũ."""
    chat_id = message.chat.id
    bot.send_message(chat_id, "✅ *Đã reset menu về kiểu cũ.*", parse_mode="Markdown", reply_markup=types.ReplyKeyboardRemove())
    show_menu(message)

@bot.message_handler(content_types=['text', 'photo'])

def handle_text(message):

    if message.from_user.is_bot: return

    user_id = message.from_user.id

    chat_id = message.chat.id

    

    # Xử lý nút Group/IG trước
    if message.text in ("👥 Thêm Group FB", "📸 Thêm Instagram", "📋 Danh Sách Group & Ins"):
        grig_handle_keyboard_button(message)
        return

    # Xử lý nút FB Post Monitor
    if message.text == "📘 Thêm Post Facebook":
        bot.send_message(chat_id,
            "📘 *THÊM POST FB THEO DÕI*\n\n"
            "Dán link bài post FB vào chat → bot tự hỏi interval.\n\n"
            "Hoặc dùng lệnh:\n"
            "`/addpost <url> [giây] [nhãn kèo]`\n\n"
            "Ví dụ:\n"
            "`/addpost https://facebook.com/share/p/abc 60 Kèo sáng`",
            parse_mode="Markdown")
        return

    if message.text == "📋 DS Post FB":
        show_unified_list(chat_id, user_id)
        return

    # Kiểm tra user có đang trong state nhập link/UID không
    _current_st_main = temp_user_state.get(user_id)
    _in_fb_input_state = isinstance(_current_st_main, dict) and (
        _current_st_main.get("step") in ("wait_uid", "wait_checkfb", "wait_link") or
        _current_st_main.get("mode") in ("meta", "get_avatar", "get_cover", "normal")
    )
    if message.text and ("facebook.com" in message.text or "fb.com" in message.text) and not _in_fb_input_state:
        if fbpost_handle_fb_link(message):
            return

    # Xử lý các nút chức năng từ bàn phím

    if message.text == "➕ Thêm UID":

        is_vip, _ = check_vip(user_id)

        if not is_vip: 

            return bot.send_message(chat_id, "🔒 Tính năng này chỉ dành cho thành viên VIP.", reply_markup=get_fixed_menu(user_id))

        bot.send_message(chat_id, "📝 **THÊM UID THƯỜNG**\nNhập UID hoặc Link FB:", parse_mode="Markdown", reply_markup=get_fixed_menu(user_id))

        temp_user_state[user_id] = {"mode": "normal", "step": "wait_uid"}

        return

    elif message.text in ("📋 DS UID", "📋 Danh sách", "📋 DS TikTok", "📋 Danh Sách Group & Ins", "📋 DS Post FB"):
        show_unified_list(chat_id, user_id)
        return

    elif message.text == "📊 Thống kê":
        u = get_user_data(user_id)

        # Facebook Profile
        fb_data   = get_tracking().get(str(chat_id), {})
        fb_active = {k: v for k, v in fb_data.items() if v.get('status') != 'done'}
        fb_live   = sum(1 for v in fb_active.values() if v.get('last_check') == 'LIVE')
        fb_die    = len(fb_active) - fb_live
        fb_val    = sum(v.get('price', 0) for v in fb_active.values() if v.get('last_check') == 'LIVE')

        # TikTok
        tt_data   = get_tracking_tiktok().get(str(chat_id), {})
        tt_active = {k: v for k, v in tt_data.items() if v.get('status') != 'done'}
        tt_live   = sum(1 for v in tt_active.values() if v.get('last_check') in ['EXISTS', 'live'])
        tt_die    = len(tt_active) - tt_live
        tt_val    = sum(v.get('price', 0) for v in tt_active.values() if v.get('last_check') in ['EXISTS', 'live'])

        # Group FB & Instagram
        grig_accounts = grig_dm.get_accounts(user_id)
        gr_active = {k: v for k, v in grig_accounts.items() if v.get('platform') == 'facebook_group'}
        gr_live   = sum(1 for v in gr_active.values() if v.get('status') == 'live')
        gr_die    = len(gr_active) - gr_live
        ig_active = {k: v for k, v in grig_accounts.items() if v.get('platform') == 'instagram'}
        ig_live   = sum(1 for v in ig_active.values() if v.get('status') == 'live')
        ig_die    = len(ig_active) - ig_live

        # Post FB
        post_list = list(_get_fp_watching().items())
        post_live = sum(1 for _, i in post_list if i.get('last_status') == 'live')
        post_die  = len(post_list) - post_live

        # YouTube
        ytb_data  = load_ytb_data().get(str(chat_id), {})
        ytb_live  = sum(1 for ch in ytb_data.values() if ch.get('status') == 'live')
        ytb_die   = len(ytb_data) - ytb_live

        total_uid = len(fb_active) + len(tt_active) + len(gr_active) + len(ig_active) + len(post_list) + len(ytb_data)
        total_val = fb_val + tt_val

        now_str = datetime.now().strftime("%H:%M  %d/%m/%Y")

        msg  = "📊 **THỐNG KÊ**\n\n"
        msg += f"📅 _{now_str}_\n"
        msg += "━━━━━━━━━━━━━━━━━\n\n"

        msg += "📘 **Facebook:**\n"
        msg += f"├ Tổng số: {len(fb_active)}\n"
        msg += f"├ ✅ Live: {fb_live} ({format_vnd(fb_val)})\n"
        msg += f"├ ❌ Die: {fb_die} (0 đ)\n"
        msg += f"└ 💰 Tổng giá trị: {format_vnd(fb_val)}\n\n"

        msg += "🎵 **TikTok:**\n"
        msg += f"├ Tổng số: {len(tt_active)}\n"
        msg += f"├ ✅ Live: {tt_live} ({format_vnd(tt_val)})\n"
        msg += f"├ ❌ Die: {tt_die} (0 đ)\n"
        msg += f"└ 💰 Tổng giá trị: {format_vnd(tt_val)}\n\n"

        msg += "👥 **Group Facebook:**\n"
        msg += f"├ Tổng số: {len(gr_active)}\n"
        msg += f"├ ✅ Live: {gr_live}\n"
        msg += f"└ ❌ Die: {gr_die}\n\n"

        msg += "📷 **Instagram:**\n"
        msg += f"├ Tổng số: {len(ig_active)}\n"
        msg += f"├ ✅ Live: {ig_live}\n"
        msg += f"└ ❌ Die: {ig_die}\n\n"

        msg += "📌 **Post Facebook:**\n"
        msg += f"├ Tổng số: {len(post_list)}\n"
        msg += f"├ ✅ Live: {post_live}\n"
        msg += f"└ ❌ Die: {post_die}\n\n"

        msg += "🎞️ **YouTube:**\n"
        msg += f"├ Tổng số: {len(ytb_data)}\n"
        msg += f"├ ✅ Live: {ytb_live}\n"
        msg += f"└ ❌ Die: {ytb_die}\n\n"

        msg += "━━━━━━━━━━━━━━━━━\n"
        msg += f"📊 **Tổng cộng: {total_uid} UID | {format_vnd(total_val)}**"

        bot.send_message(chat_id, msg, parse_mode="Markdown")
        return

    elif message.text == "🎵 DS TikTok":

        try:

            d = get_tracking_tiktok(); u = d.get(str(chat_id), {})

            if not u:

                return bot.send_message(chat_id, "📋 **DANH SÁCH TIKTOK**\n\nTrống.", parse_mode="Markdown", reply_markup=get_fixed_menu(user_id))

            msg = "📋 **DANH SÁCH TIKTOK**\n\n"

            active_count = 0

            for username, v in u.items():

                if v.get('status') != 'done':

                    active_count += 1

                    last_check = v.get('last_check', 'DIE')

                    status_icon = "🟢 Live" if last_check in ['EXISTS', 'live'] else "🔴 Die"

                    verified_icon = " ☑️ VERIFIED" if v.get("verified") else ""

                    msg += f"{status_icon} @{username}{verified_icon} | {v.get('name', username)}\n"

            if active_count == 0: msg += "Trống."

            bot.send_message(chat_id, msg, parse_mode="Markdown", reply_markup=get_fixed_menu(user_id))

        except: pass

        return

    elif message.text == "🎵 Tìm nhạc":
        user_input_state[user_id] = "waiting_for_song_name"
        bot.send_message(
            message.chat.id,
            "🎵 Nhập tên bài hát bạn muốn tìm:\n\n💡 Ví dụ: Dừng Thương, See You Again, ..."
        )
        return
    elif message.text == "👤 Tài khoản":

        u = get_user_data(user_id)

        is_vip, vip_text = check_vip(user_id)

        stats = u.get("stats", {"done": 0, "cancel": 0, "tracking": 0, "money_generated": 0})

        level_text = "👑 VIP" if u.get("level") == 2 else "👤 Thường"

        msg = f"""👤 **THÔNG TIN TÀI KHOẢN**



🆔 UID: `{user_id}`

💰 Số dư: **{format_vnd(u['balance'])}**

🏅 Cấp độ: {level_text}

👑 Trạng thái VIP: {vip_text}



📊 **THỐNG KÊ:**

✅ Đã xong: {stats['done']}

❌ Đã hủy: {stats['cancel']}

👀 Đang theo dõi: {stats['tracking']}"""

        bot.send_message(chat_id, msg, parse_mode="Markdown", reply_markup=get_fixed_menu(user_id))

        return

    elif message.text == "🎁 Mã quà tặng":

        markup = types.InlineKeyboardMarkup()

        markup.add(

            types.InlineKeyboardButton("🎁 Mã Giới Thiệu", callback_data="show_referral"),

            types.InlineKeyboardButton("🎫 Nhập Mã Quà Tặng", callback_data="enter_code")

        )

        bot.send_message(chat_id, "🎁 **QUÀ TẶNG & GIỚI THIỆU**\n\nChọn một tùy chọn bên dưới:", reply_markup=markup, parse_mode="Markdown")

        return

    elif message.text == "💝 Donate":
        qr_url = f"https://img.vietqr.io/image/MB-0862197064-compact2.png?amount=0&addInfo=DH%20Donate%20{user_id}&accountName=NGUYEN%20MAI%20NIN"
        caption = (
            "💝 *ỦNG HỘ DUY TRÌ SERVER*\n"
            "─────────────────\n"
            "🏦 NH: MB Bank\n"
            "💳 STK: `0862197064`\n"
            "👤 CTK: NGUYỄN MAI NIN\n"
            f"📝 ND: `DH Donate {user_id}`\n"
            "─────────────────\n"
            "💖 Cảm ơn bạn đã ủng hộ bot!\n"
            "ℹ️ _Donate không tự động check_"
        )
        mk_donate = types.InlineKeyboardMarkup()
        mk_donate.add(types.InlineKeyboardButton("💳 Sao chép STK: 0862197064", callback_data="donate_copy_stk"))
        try:
            bot.send_photo(chat_id, qr_url, caption=caption, parse_mode="Markdown", reply_markup=mk_donate)
        except:
            bot.send_message(chat_id, caption, parse_mode="Markdown", reply_markup=mk_donate)
        return

    elif message.text == "🏠 Menu chính":

        show_menu(message)

        return

    elif message.text == "🛡️ Admin Panel":

        if user_id in ADMIN_IDS: show_admin_panel(chat_id, user_id)

        return



    # Xử lý chat hỗ trợ

    if user_id in active_chats:

        pid = active_chats[user_id]

        try:

            markup_end = types.InlineKeyboardMarkup()

            markup_end.add(types.InlineKeyboardButton("🔚 Kết thúc hội thoại hỗ trợ", callback_data="end_chat"))

            if message.content_type == 'text': 

                if user_id in ADMIN_IDS:

                    bot.send_message(pid, f"💬 **Chuyên viên:** {message.text}", reply_markup=markup_end)

                else:

                    bot.send_message(pid, f"💬 **Quý khách:** {message.text}", reply_markup=markup_end)

            elif message.content_type == 'photo': 

                caption_prefix = "**Chuyên viên:** " if user_id in ADMIN_IDS else "**Quý khách:** "

                bot.send_photo(pid, message.photo[-1].file_id, caption=(caption_prefix + (message.caption or "")), reply_markup=markup_end)

        except: bot.reply_to(message, "❌ Hệ thống gặp lỗi khi gửi tin nhắn. Vui lòng thử lại.")

        return



    # Xử lý khi user đang chờ nhập tên nhạc
    if user_id in user_input_state and user_input_state[user_id] == "waiting_for_song_name":

        if not message.text: return
        noi_dung = message.text.strip()
        
        if not noi_dung:
            bot.reply_to(message, "❌ Vui lòng nhập tên bài hát!")
            return
        
        # Xóa trạng thái chờ
        del user_input_state[user_id]
        
        try:
            tin_nhan_xu_ly = bot.reply_to(message, f"🔍 Đang tìm: {noi_dung}...")
            danh_sach_bai_hat = tim_nhac(noi_dung)
            
            if not danh_sach_bai_hat:
                bot.edit_message_text(
                    f"❌ Không tìm thấy: {noi_dung}",
                    tin_nhan_xu_ly.chat.id,
                    tin_nhan_xu_ly.message_id
                )
                bot.send_message(message.chat.id, "Nhấn nút bên dưới để tìm lại:", reply_markup=get_fixed_menu(user_id))
                return
            
            music_cache[user_id] = {'songs': danh_sach_bai_hat, 'query': noi_dung}
            
            duong_dan_anh = tao_anh_danh_sach(danh_sach_bai_hat)
            
            ban_phim = types.InlineKeyboardMarkup(row_width=1)
            for i, bai_hat in enumerate(danh_sach_bai_hat[:10], 1):
                link, ten, anh_bia, luot_nghe, luot_thich, binh_luan, nghe_si = bai_hat
                chu_nut = f"🎵 {i}. {ten[:35]}... - 👤 {nghe_si}"
                ban_phim.add(types.InlineKeyboardButton(chu_nut, callback_data=f"music_{i}"))
            ban_phim.add(types.InlineKeyboardButton("❌ Hủy", callback_data="music_cancel"))
            
            if duong_dan_anh:
                with open(duong_dan_anh, 'rb') as anh:
                    bot.send_photo(
                        message.chat.id,
                        anh,
                        caption=f"🎵 Tìm thấy {len(danh_sach_bai_hat)} bài hát: {noi_dung}\n\n📋 Chọn bài hát:",
                        reply_markup=ban_phim
                    )
                os.remove(duong_dan_anh)
                bot.delete_message(tin_nhan_xu_ly.chat.id, tin_nhan_xu_ly.message_id)
                bot.send_message(message.chat.id, "Bấm nút để tìm bài khác:", reply_markup=get_fixed_menu(user_id))
            else:
                bot.edit_message_text(
                    f"🎵 Tìm thấy {len(danh_sach_bai_hat)} bài hát: {noi_dung}\n\n📋 Chọn bài hát:",
                    tin_nhan_xu_ly.chat.id,
                    tin_nhan_xu_ly.message_id,
                    reply_markup=ban_phim
                )
                bot.send_message(message.chat.id, "Bấm nút để tìm bài khác:", reply_markup=get_fixed_menu(user_id))
                
        except Exception as e:
            bot.reply_to(message, f"❌ Lỗi: {e}")
            bot.send_message(message.chat.id, "Thử lại:", reply_markup=get_fixed_menu(user_id))
        return

    st = temp_user_state.get(user_id)

    

    # Xử lý admin đang trả lời hỗ trợ

    if user_id in ADMIN_IDS and isinstance(st, dict) and st.get("mode") == "admin_replying":

        target = st["target_uid"]

        try:

            bot.send_message(target, f"💌 **PHẢN HỒI TỪ ADMIN:**\n\n{message.text}")

            bot.reply_to(message, f"✅ Đã gửi cho UID `{target}`.")

        except: bot.reply_to(message, "❌ Không gửi được (Khách chặn bot?).")

        temp_user_state.pop(user_id, None)

        return



    # Xử lý admin thêm nhóm mới

    if user_id in ADMIN_IDS and isinstance(st, dict):

        if st.get("mode") == "admin_add_group":

            try:


                if not message.text: return
                parts = message.text.split("|")

                if len(parts) != 2:

                    return bot.reply_to(message, "❌ Định dạng sai! Vui lòng nhập: `@username | link`")

                

                uname = parts[0].strip()

                link = parts[1].strip()

                

                if not uname.startswith("@") or not link.startswith("http"):

                    return bot.reply_to(message, "❌ Dữ liệu không hợp lệ! Username phải có @, Link phải có http.")

                

                cfg = load_json(FILES["config"])

                groups = cfg.get("required_groups", [])

                groups.append({"username": uname, "link": link})

                cfg["required_groups"] = groups

                save_json(FILES["config"], cfg)

                

                bot.reply_to(message, f"✅ Đã thêm nhóm `{uname}` vào danh sách bắt buộc.", parse_mode="Markdown")

                temp_user_state.pop(user_id, None)

                show_admin_panel(chat_id, user_id)

            except Exception as e:

                bot.reply_to(message, f"❌ Lỗi: {str(e)}")

            return



    # Xử lý nhập mã khuyến mãi

    if isinstance(st, dict) and st.get("mode") == "enter_code":

        if st.get("step") == "wait_code":


            if not message.text: return
            code_name = message.text.strip().upper()

            result = use_code(user_id, code_name, check_amount=0)

            

            if result.get("success"):

                code_info = result.get("code_info", {})

                expiry_date = code_info.get("expiry_date", "")

                min_amount = code_info.get("min_amount", 0)

                

                msg = result.get("message", "")

                if expiry_date:

                    msg += f"\n📅 Hạn dùng: {expiry_date}"

                if min_amount > 0:

                    msg += f"\n💰 Tối thiểu: {format_vnd(min_amount)}"

                

                bot.reply_to(message, msg, parse_mode="Markdown")

                

                if result.get("type") == "VIP":

                    bot.send_message(chat_id, f"🎉 Chúc mừng! Bạn đã nhận {result.get('value', 0)} ngày VIP miễn phí!", parse_mode="Markdown")

                elif result.get("type") == "MONEY":

                    new_balance = get_user_data(user_id)["balance"]

                    bot.send_message(chat_id, f"💰 Số dư hiện tại: {format_vnd(new_balance)}", parse_mode="Markdown")

            else:

                bot.reply_to(message, result.get('message', '❌ Mã không hợp lệ.'))

            

            temp_user_state.pop(user_id, None)

            return

    

    # Xử lý nhập mã giới thiệu

    if isinstance(st, dict) and st.get("mode") == "enter_referral":

        if st.get("step") == "wait_referral":


            if not message.text: return
            referral_input = message.text.strip()

            result = use_referral_code(user_id, referral_input)

            

            if result.get("success"):

                bot.reply_to(message, result.get("message", ""), parse_mode="Markdown")

                user_data = get_user_data(user_id)

                if user_data.get("referral_vip_discount", 0) > 0:

                    bot.send_message(chat_id, f"🎫 Bạn cũng được giảm {user_data['referral_vip_discount']}% khi mua VIP!", parse_mode="Markdown")

            else:

                bot.reply_to(message, result.get('message', '❌ Mã giới thiệu không hợp lệ.'))

            

            temp_user_state.pop(user_id, None)

            return

    

    # Xử lý nạp tiền

    if isinstance(st, dict) and st.get("mode") == "deposit":

        if st.get("step") == "wait_amount":

            if not message.text: return

            try:

                amt_text = message.text.strip().replace(".", "").replace(",", "").replace(" ", "")

                if not amt_text.isdigit(): return bot.reply_to(message, "❌ Số tiền không hợp lệ.")

                amt = int(amt_text)

                if amt <= 0: return bot.reply_to(message, "❌ Số tiền phải > 0.")

                

                qr_url = f"https://qr.sepay.vn/img?acc=0862197064&bank=ICB&amount={amt}&des={user_id}&template=compact&download=false"

                form_msg = f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n🔥 HỆ THỐNG NẠP TIỀN NHANH 🔥\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n\n🏦 NGÂN HÀNG: MBBANK\n💳 STK: 0862197064\n👤 CHỦ TK: NGUYEN MAI NIN\n💰 SỐ TIỀN: {format_vnd(amt)} VNĐ\n\n📌 NỘI DUNG CK: 👉 {user_id} 👈\n\n👉 QUÉT MÃ QR HOẶC CK THEO THÔNG TIN TRÊN\n📝 Gửi bill tại đây để Admin duyệt.\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬"

                bot.send_photo(chat_id, qr_url, caption=form_msg)

                st["step"] = "wait_bill"

                st["amount"] = amt

            except: bot.reply_to(message, "❌ Số tiền lỗi.")

        elif st.get("step") == "wait_bill":

            if message.photo:

                amt = st.get("amount", 0)

                bonus_info = calculate_bonus_with_ai(amt, user_id)

                base_amount = bonus_info.get("base_amount", amt)

                total_amount = bonus_info.get("total_amount", amt)

                bonus_amount = bonus_info.get("bonus_amount", 0)

                

                markup = types.InlineKeyboardMarkup()

                if bonus_info.get("has_bonus"):

                    bonus_sources = bonus_info.get("bonus_sources", [])

                    bonus_text = "\n".join([f"🎁 {s}" for s in bonus_sources])

                    admin_msg = f"💰 **YÊU CẦU NẠP TIỀN**\n\n"

                    admin_msg += f"🆔 UID: `{user_id}`\n"

                    admin_msg += f"💰 Số tiền gốc: {format_vnd(base_amount)}\n"

                    admin_msg += f"{bonus_text}\n"

                    admin_msg += f"💵 **Tổng nhận: {format_vnd(total_amount)}**"

                    markup.add(types.InlineKeyboardButton("✅ Duyệt", callback_data=f"approve_deposit_{user_id}_{base_amount}_{total_amount}"))

                    markup.add(types.InlineKeyboardButton("❌ Hủy", callback_data=f"cancel_deposit_{user_id}"))

                else:

                    admin_msg = f"💰 **YÊU CẦU NẠP TIỀN**\n\n"

                    admin_msg += f"🆔 UID: `{user_id}`\n"

                    admin_msg += f"💰 Số tiền: {format_vnd(amt)}\n"

                    admin_msg += f"💡 Mã đã bị xóa khỏi tài khoản. Nạp tiền bình thường:"

                    markup.add(types.InlineKeyboardButton("✅ Nạp không mã", callback_data=f"approve_deposit_{user_id}_{amt}_{amt}"))

                    markup.add(types.InlineKeyboardButton("❌ Hủy", callback_data=f"cancel_deposit_{user_id}"))

                

                for admin in ADMIN_IDS:

                    try: bot.send_photo(admin, message.photo[-1].file_id, caption=admin_msg, reply_markup=markup, parse_mode="Markdown")

                    except: pass

                bot.reply_to(message, "✅ Đã gửi bill. Chờ Admin duyệt.")

                temp_user_state.pop(user_id, None)

            else:

                bot.reply_to(message, "❌ Vui lòng gửi ảnh bill.")

        return



    # Xử lý feedback chat với AI

    if isinstance(st, dict) and st.get("mode") == "feedback_chat":

        call_feedback_ai(message) 

        return



    # Xử lý AI tạo thông báo

    if isinstance(st, dict) and st.get("step") == "wait_ai_topic":

        if user_id not in ADMIN_IDS: return

        topic = message.text

        threading.Thread(target=ai_create_broadcast, args=(user_id, topic), daemon=True).start()

        temp_user_state.pop(user_id, None); return

    # ── Xử lý broadcast menu (gửi thông báo tất cả user) ──
    if isinstance(st, dict) and st.get("mode") == "broadcast":

        if user_id not in ADMIN_IDS: return

        step = st.get("step", "")

        def _send_broadcast_preview(admin_id, content, photo_id):
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(
                types.InlineKeyboardButton("📢 Gửi Thường", callback_data="broadcast_confirm_send"),
                types.InlineKeyboardButton("💬 Gửi + Nhận Feedback", callback_data="broadcast_confirm_feedback"),
                types.InlineKeyboardButton("❌ Hủy", callback_data="broadcast_cancel"),
            )
            total = len(get_all_users_list())
            preview_header = f"👁 **XEM TRƯỚC** (sẽ gửi tới {total} user)\n" + "─"*30 + "\n"
            temp_user_state[admin_id]["broadcast_content"] = content or ""
            temp_user_state[admin_id]["broadcast_photo_id"] = photo_id
            if photo_id:
                caption = preview_header + (content or "")
                try:
                    bot.send_photo(admin_id, photo_id, caption=caption[:1024], reply_markup=markup, parse_mode="Markdown")
                except:
                    bot.send_photo(admin_id, photo_id, caption=caption[:1024], reply_markup=markup)
            else:
                try:
                    bot.send_message(admin_id, preview_header + (content or "(Không có văn bản)"), reply_markup=markup, parse_mode="Markdown")
                except:
                    bot.send_message(admin_id, preview_header + (content or "(Không có văn bản)"), reply_markup=markup)

        if step == "wait_text":
            if message.text:
                content = message.text.strip()
                temp_user_state[user_id]["step"] = "wait_confirm"
                _send_broadcast_preview(user_id, content, None)
            else:
                bot.reply_to(message, "⚠️ Vui lòng nhập văn bản.")
            return

        if step == "wait_photo_text":
            if message.photo:
                photo_id = message.photo[-1].file_id
                content  = message.caption.strip() if message.caption else ""
                if content:
                    temp_user_state[user_id]["step"] = "wait_confirm"
                    _send_broadcast_preview(user_id, content, photo_id)
                else:
                    temp_user_state[user_id]["photo_id"] = photo_id
                    temp_user_state[user_id]["step"] = "wait_photo_caption"
                    bot.reply_to(message, "✅ Đã nhận ảnh!\n\nBây giờ nhập nội dung văn bản (hoặc gửi /skip để bỏ qua):")
            elif message.text and st.get("photo_id"):
                content  = message.text.strip() if message.text != "/skip" else ""
                photo_id = st["photo_id"]
                temp_user_state[user_id]["step"] = "wait_confirm"
                _send_broadcast_preview(user_id, content, photo_id)
            else:
                bot.reply_to(message, "⚠️ Vui lòng gửi ảnh lên.")
            return

        if step == "wait_photo_caption":
            content  = message.text.strip() if (message.text and message.text != "/skip") else ""
            photo_id = st.get("photo_id")
            temp_user_state[user_id]["step"] = "wait_confirm"
            _send_broadcast_preview(user_id, content, photo_id)
            return

        if step == "wait_photo_only":
            if message.photo:
                photo_id = message.photo[-1].file_id
                temp_user_state[user_id]["step"] = "wait_confirm"
                _send_broadcast_preview(user_id, "", photo_id)
            else:
                bot.reply_to(message, "⚠️ Vui lòng gửi ảnh lên.")
            return

        return

    st = temp_user_state.get(user_id)

    





    # Xử lý 5 lệnh mới từ menu

    if isinstance(st, dict):

        mode = st.get("mode")

        step = st.get("step")

        

        # 1. Lấy Avatar Facebook

        if mode == "get_avatar" and step == "wait_link":


            if not message.text: return
            link = message.text.strip()

            if not link:

                bot.reply_to(message, "❌ Vui lòng nhập link Facebook hoặc UID.")

                return

            

            # Gọi helper function (không dùng command nữa)

            getavt_helper(message, link)

            temp_user_state.pop(user_id, None)

            return

        

        # 2. Lấy Ảnh bìa Facebook

        elif mode == "get_cover" and step == "wait_link":


            if not message.text: return
            link = message.text.strip()

            if not link:

                bot.reply_to(message, "❌ Vui lòng nhập link Facebook hoặc UID.")

                return

            

            # Gọi helper function (không dùng command nữa)

            getbia_helper(message, link)

            temp_user_state.pop(user_id, None)

            return

        

        

        # 4. Lấy mã 2FA

        elif mode == "get_2fa" and step == "wait_secret":


            if not message.text: return
            secret = message.text.strip()

            if not secret:

                bot.reply_to(message, "❌ Vui lòng nhập mã secret 2FA.")

                return

            

            # Gọi helper function (không dùng command nữa)

            get2fa_helper(message, secret)

            temp_user_state.pop(user_id, None)

            return

        

        # 5. Gửi thông báo cho tất cả user (Admin)

        elif mode == "send_notification_all":

            ctx = _get_subbot_ctx()
            if ctx:
                bot.reply_to(message, "⚠️ Chức năng gửi thông báo chỉ dùng được trong bot chính!")
                temp_user_state.pop(user_id, None)
                return

            if user_id not in ADMIN_IDS:
                bot.reply_to(message, "❌ Bạn không có quyền sử dụng chức năng này!")
                temp_user_state.pop(user_id, None)
                return

            def _sna_preview(admin_id, content_p, photo_id_p):
                """Gửi preview + nút xác nhận cho admin trước khi broadcast."""
                total = len(get_all_users_list())
                markup_p = types.InlineKeyboardMarkup(row_width=1)
                markup_p.add(
                    types.InlineKeyboardButton("📢 XÁC NHẬN GỬI", callback_data="sna_confirm_send"),
                    types.InlineKeyboardButton("❌ Hủy", callback_data="sna_cancel"),
                )
                preview_text = (
                    f"👁 **XEM TRƯỚC** — sẽ gửi tới {total} user\n"
                    f"{'─'*30}\n"
                    f"{content_p or '(Không có văn bản)'}\n"
                    f"{'─'*30}"
                )
                temp_user_state[admin_id]["broadcast_content"]  = content_p or ""
                temp_user_state[admin_id]["broadcast_photo_id"] = photo_id_p
                temp_user_state[admin_id]["step"] = "wait_confirm"
                if photo_id_p:
                    try:
                        bot.send_photo(admin_id, photo_id_p, caption=preview_text[:1024], reply_markup=markup_p, parse_mode="Markdown")
                    except Exception:
                        bot.send_photo(admin_id, photo_id_p, caption=preview_text[:1024], reply_markup=markup_p)
                else:
                    try:
                        bot.send_message(admin_id, preview_text, reply_markup=markup_p, parse_mode="Markdown")
                    except Exception:
                        bot.send_message(admin_id, preview_text, reply_markup=markup_p)

            # ── Chờ văn bản thuần ──
            if step == "wait_text":
                if message.text:
                    _sna_preview(user_id, message.text.strip(), None)
                else:
                    bot.reply_to(message, "⚠️ Vui lòng nhập văn bản.")
                return

            # ── Chờ ảnh + văn bản ──
            if step == "wait_photo_text":
                if message.photo:
                    pid = message.photo[-1].file_id
                    cap = message.caption.strip() if message.caption else ""
                    if cap:
                        _sna_preview(user_id, cap, pid)
                    else:
                        temp_user_state[user_id]["photo_id"] = pid
                        temp_user_state[user_id]["step"] = "wait_photo_caption"
                        bot.reply_to(message, "✅ Đã nhận ảnh!\n\nNhập nội dung văn bản (hoặc /skip để bỏ qua):")
                elif message.text and st.get("photo_id"):
                    cap = "" if message.text == "/skip" else message.text.strip()
                    _sna_preview(user_id, cap, st["photo_id"])
                else:
                    bot.reply_to(message, "⚠️ Vui lòng gửi ảnh lên.")
                return

            # ── Đợi caption sau khi nhận ảnh ──
            if step == "wait_photo_caption":
                cap = "" if (not message.text or message.text == "/skip") else message.text.strip()
                _sna_preview(user_id, cap, st.get("photo_id"))
                return

            # ── Chờ ảnh không caption ──
            if step == "wait_photo_only":
                if message.photo:
                    _sna_preview(user_id, "", message.photo[-1].file_id)
                else:
                    bot.reply_to(message, "⚠️ Vui lòng gửi ảnh lên.")
                return

            return  # wait_confirm — bỏ qua tin nhắn khác


    # Xu ly them kenh YouTube
    if isinstance(st, dict) and st.get("mode") == "add_ytb":
        step = st.get("step")
        if step == "wait_url":

            if not message.text: return
            url = message.text.strip()
            if not url:
                bot.reply_to(message, "❌ Vui long nhap link YouTube!")
                return
            if "youtube.com" not in url and "youtu.be" not in url:
                bot.reply_to(message, "❌ Link khong hop le! Vi du: https://youtube.com/@channelname")
                return
            identifier = ytb_extract_identifier(url)
            if not identifier:
                bot.reply_to(message, "❌ Khong the trich xuat thong tin kenh!\nHay dung: https://youtube.com/@channelname")
                temp_user_state.pop(user_id, None)
                return
            wait_msg = bot.send_message(chat_id, "⏳ Đang lấy thông tin kênh YouTube...")
            channel_info = ytb_get_channel_info(identifier)
            try: bot.delete_message(chat_id, wait_msg.message_id)
            except: pass
            if not channel_info:
                bot.reply_to(message, "❌ Không tìm thấy kênh YouTube này!\nKiểm tra lại link hoặc YouTube API key.")
                temp_user_state.pop(user_id, None)
                return
            data = load_ytb_data()
            cid_str = str(chat_id)
            if cid_str not in data: data[cid_str] = {}
            if url in data[cid_str]:
                bot.reply_to(message, "⚠️ Kênh này đã có trong danh sách theo dõi!")
                temp_user_state.pop(user_id, None)
                return
            now_str = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            data[cid_str][url] = {
                "channel_id": channel_info["channel_id"],
                "title": channel_info["title"],
                "avatar": channel_info["avatar"],
                "added_time": now_str,
                "last_check": now_str,
                "status": "live",
                "fail_count": 0
            }
            save_ytb_data(data)
            msg = (
                f"✅ <b>THÊM KÊNH THÀNH CÔNG!</b>\n\n"
                f"📺 Tên: {channel_info['title']}\n"
                f"🔗 Link: {url}\n"
                f"🆔 Channel ID: {channel_info['channel_id']}\n"
                f"👥 Subscribers: {channel_info['subscriber_count']}\n"
                f"🎬 Videos: {channel_info['video_count']}\n"
                f"🟢 Trạng thái: ĐANG HOẠT ĐỘNG\n"
                f"⏰ Thêm lúc: {now_str}"
            )
            markup = types.InlineKeyboardMarkup(row_width=2)
            markup.row(
                types.InlineKeyboardButton("✅ Done", callback_data=f"ytb_done_{channel_info['channel_id']}"),
                types.InlineKeyboardButton("❌ Xóa", callback_data=f"ytb_del_{channel_info['channel_id']}")
            )
            markup.add(types.InlineKeyboardButton("🔔 Tiếp Tục Theo Dõi", callback_data=f"ytb_keep_{channel_info['channel_id']}"))
            avatar = channel_info.get("avatar")
            if avatar:
                bot.send_photo(chat_id, avatar, caption=msg, parse_mode="HTML", reply_markup=markup)
            else:
                bot.send_message(chat_id, msg, parse_mode="HTML", reply_markup=markup)
            temp_user_state.pop(user_id, None)
            return

    # Xử lý TikTok

    if isinstance(st, dict) and st.get("mode") == "tiktok":

        step = st.get("step")

        

        if step == "wait_username":


            if not message.text: return
            raw_input = message.text.strip()

            if 'tiktok.com' in raw_input:
                username = extract_tiktok_username(raw_input)
                if not username:
                    return bot.reply_to(message, "❌ Không đọc được username từ link.\nGửi username trực tiếp, ví dụ: @khaby.lame")
            else:
                username = raw_input.lstrip('@').strip()

            if not username:

                return bot.reply_to(message, "❌ Username không hợp lệ.")

            

            data = get_tracking_tiktok()

            if str(chat_id) in data and username in data[str(chat_id)]:

                return bot.reply_to(message, f"❌ TikTok @{_md(username)} *đã có trong danh sách theo dõi*.\n\nVui lòng xóa khỏi danh sách cũ trước khi thêm mới.", parse_mode="Markdown")



            checking_msg = bot.reply_to(message, "⏳ Đang kiểm tra TikTok username...")

            

            info, error = get_tiktok_info_full(f"https://www.tiktok.com/@{username}")
            if error or not info:
                status = tiktok_checker.check_user_exists(username)
                if status == "ERROR":
                    safe_edit_message(chat_id, checking_msg.message_id, "❌ Lỗi khi kiểm tra TikTok. Vui lòng thử lại sau.")
                    temp_user_state.pop(user_id, None)
                    return
                status_live = "LIVE" if status == "EXISTS" else "DIE"
                st["username"] = username; st["name"] = username
                st["avatar"] = ""; st["followers"] = 0; st["likes"] = 0; st["verified"] = False
            else:
                status_live = "LIVE"
                st["username"] = username
                st["name"] = info.get("name", username)
                st["avatar"] = info.get("avatar_url", "")
                st["followers"] = info.get("follower_count", 0)
                st["likes"] = info.get("heart_count", 0)
                st["verified"] = info.get("verified") == "Có"
            st["step"] = "wait_note"; st["initial_status"] = status_live
            profile_info = ""; avatar_url = st.get("avatar", "")
            if status_live == "LIVE":
                followers = st.get("followers", 0); likes = st.get("likes", 0)
                verified = " (Tích xanh ☑️)" if st.get("verified") else ""
                try:
                    profile_info = f"🔍 *THÔNG TIN PROFILE:*\n\n👤 Tên: {_md(st['name'])}{verified}\n📊 Followers: {int(followers):,} | Likes: {int(likes):,}\n"
                except:
                    profile_info = f"🔍 *THÔNG TIN PROFILE:*\n\n👤 Tên: {_md(st['name'])}{verified}\n📊 Followers: {followers} | Likes: {likes}\n"
            msg_text = f"✅ TikTok @{_md(username)} - {status_live}\n\n{profile_info}\n📝 Vui lòng nhập Ghi chú:"
            if avatar_url:
                try:
                    avatar_bytes = _download_avatar_bytes(avatar_url)
                    if avatar_bytes:
                        from io import BytesIO as _BIO
                        bot.send_photo(chat_id, _BIO(avatar_bytes), caption=msg_text, parse_mode="Markdown")
                    else:
                        bot.send_photo(chat_id, avatar_url, caption=msg_text, parse_mode="Markdown")
                    bot.delete_message(chat_id, checking_msg.message_id)
                except:
                    safe_edit_message(chat_id, checking_msg.message_id, msg_text)
            else:
                safe_edit_message(chat_id, checking_msg.message_id, msg_text)

        

        elif step == "wait_note":

            st["note"] = message.text

            st["step"] = "wait_price"

            bot.reply_to(message, "💰 Nhập GIÁ (Số):")

        

        elif step == "wait_price":

            try:

                price = int(message.text.replace(".", ""))

            except:

                return bot.reply_to(message, "❌ Phải là số.")

            

            username = st["username"]

            name = st.get("name", username)[:100]

            note = st["note"][:200]

            initial_status = st.get("initial_status", "EXISTS")

            

            def escape_markdown(text):

                special_chars = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']

                for char in special_chars:

                    text = text.replace(char, '\\' + char)

                return text

            

            username_escaped = escape_markdown(username)

            name_escaped = escape_markdown(name)

            note_escaped = escape_markdown(note)

            

            avatar = st.get("avatar", "")

            followers = st.get("followers", 0)

            likes = st.get("likes", 0)

            verified = st.get("verified", False)

            save_tracking_tiktok(chat_id, username, name, note, price, avatar, followers, verified)

            update_user_stats(user_id, "add")

            

            status_icon = "🟢 LIVE" if initial_status == "LIVE" else "🔴 DIE"

            verified_icon = " ☑️ VERIFIED" if st.get("verified") else ""

            

            time_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            

            stats_text = ""

            if initial_status == "LIVE":

                stats_text = f"📊 **Follow:** {st.get('followers', 0):,} | **Like:** {st.get('likes', 0):,}\n"



            msg = f"✅ **ĐÃ LƯU TIKTOK THÀNH CÔNG!**\n\n"

            msg += f"@{username_escaped} - {status_icon}{verified_icon}\n\n"

            msg += f"👤 **Tên:** {name_escaped}\n"

            msg += stats_text

            msg += f"📝 **Ghi chú:** {note_escaped}\n"

            msg += f"💵 **Giá:** {format_vnd(price)}\n"

            msg += f"🔄 **Tiến trình:** Đang theo dõi báo Sống/Die\n"

            msg += f"⏰ **Thời gian:** {time_str}\n\n"

            msg += f"(Bot sẽ báo ngay khi TikTok bị DIE)"

            

            markup = types.InlineKeyboardMarkup()

            markup.add(

                types.InlineKeyboardButton("✅ Done", callback_data=f"done_tiktok_{username[:50]}"),

                types.InlineKeyboardButton("❌ Hủy", callback_data=f"del_tiktok_{username[:51]}")

            )

            

            if avatar:

                try:

                    bot.send_photo(chat_id, avatar, caption=msg, reply_markup=markup, parse_mode="Markdown")

                except:

                    bot.send_message(chat_id, msg, reply_markup=markup, parse_mode="Markdown")

            else:

                bot.send_message(chat_id, msg, reply_markup=markup, parse_mode="Markdown")

            

            temp_user_state.pop(user_id, None)

        return



    # Xử lý check FB Full (nâng cấp: hỗ trợ FB / Instagram / TikTok)

    if isinstance(st, dict) and st.get("step") == "wait_checkfb":


        if not message.text: return
        input_data = message.text.strip()
        fb_mode = st.get("fb_mode", "basic")

        temp_user_state.pop(user_id, None)

        platform = detect_social_platform(input_data)

        if platform in ('instagram', 'tiktok', 'facebook'):
            handle_check_info_full(message, input_data, fb_mode=fb_mode)
        elif input_data.isdigit() or _extract_facebook_vanity_slug(input_data):
            handle_check_info_full(message, input_data, fb_mode=fb_mode)
        else:
            norm = _normalize_facebook_link(input_data)
            uid, _ = get_uid_from_link(norm) if norm else (None, None)
            if not uid:
                uid, _ = get_uid_from_link(input_data)
            if uid:
                handle_check_info_full(
                    message, f"https://www.facebook.com/profile.php?id={uid}", fb_mode=fb_mode)
            else:
                bot.reply_to(message,
                    "❌ Không nhận diện được link!\n\n"
                    "✅ Hỗ trợ:\n"
                    "• Link/UID Facebook\n"
                    "• Link Instagram\n"
                    "• Link TikTok")

        return



    # Xử lý check FAQ/DIE từ menu

    if isinstance(st, dict) and st.get("mode") == "check_faq" and st.get("step") == "wait_input":

        temp_user_state.pop(user_id, None)


        if not message.text: return
        raw = message.text.strip()

        uid_list, invalid_lines = faq_extract_uid_list(raw)

        if not uid_list:

            bot.reply_to(message, "❌ Không tìm thấy UID hợp lệ.\nNhập số UID hoặc link facebook.com/profile.php?id=...", parse_mode="HTML")

            return

        if invalid_lines:

            warn = "⚠️ Các dòng không nhận dạng được (bỏ qua):\n"

            for line in invalid_lines[:5]:

                warn += f"  • <code>{faq_esc(line[:80])}</code>\n"

            bot.send_message(message.chat.id, warn, parse_mode="HTML")

        threading.Thread(target=faq_run_check,

                         args=(message.chat.id, message.message_id, uid_list,
                               getattr(_subbot_tl, 'ctx', None)),

                         daemon=True).start()

        return

    # Xử lý gửi bill VIP Bot Con
    if isinstance(st, dict) and st.get("mode") == "botcon_vip_bill":
        plan_key = st.get("plan", "1")
        plan = BOTCON_VIP_PLANS.get(plan_key, {})
        temp_user_state.pop(user_id, None)
        admin_msg = (
            f"💳 <b>YÊU CẦU VIP BOT CON</b>\n\n"
            f"👤 UID: <code>{user_id}</code>\n"
            f"📦 Gói: <b>{plan.get('label','?')}</b> — {format_vnd(plan.get('price',0))}\n\n"
            "📸 Bill đính kèm bên dưới:"
        )
        mk_admin = types.InlineKeyboardMarkup(row_width=2)
        mk_admin.add(
            types.InlineKeyboardButton(f"✅ Duyệt {plan.get('label','?')}", callback_data=f"botcon_vip_approve_{user_id}_{plan_key}"),
            types.InlineKeyboardButton("❌ Từ chối", callback_data=f"botcon_vip_reject_{user_id}"),
        )
        for admin_id in ADMIN_IDS:
            try:
                bot.send_message(admin_id, admin_msg, parse_mode="HTML")
                if message.photo:
                    bot.send_photo(admin_id, message.photo[-1].file_id, reply_markup=mk_admin)
                elif message.document:
                    bot.send_document(admin_id, message.document.file_id, reply_markup=mk_admin)
                else:
                    bot.send_message(admin_id, message.text or "(không có nội dung)", reply_markup=mk_admin)
            except Exception:
                pass
        bot.reply_to(message,
            "✅ <b>Đã gửi bill đến Admin!</b>\n\n"
            f"⏳ Gói: <b>{plan.get('label','?')}</b>\n"
            "Admin sẽ duyệt trong <b>5-15 phút</b>.\n"
            "Bạn sẽ nhận thông báo khi được kích hoạt.",
            parse_mode="HTML")
        return

    # Xử lý thêm Bot Con token

    elif isinstance(st, dict) and st.get("mode") == "botcon_add" and st.get("step") == "wait_token":

        temp_user_state.pop(user_id, None)

        botcon_process_token(message, message.text)

        return

    # Xử lý input admin quản lý bot con
    if isinstance(st, dict) and st.get("mode", "").startswith("adminbot_"):
        if handle_adminbot_input(message):
            return

    if isinstance(st, dict) and st.get("step") == "wait_uid":


        if not message.text: return
        txt = message.text.strip(); uid = txt; name_from_link = None

        if not uid.isdigit():

            bot.reply_to(message, "🔍 Check link...")

            uid, name_from_link = get_uid_from_link(txt)

            if not uid: return bot.reply_to(message, "❌ Link lỗi.")

        

        if st.get("mode") == "meta":

            is_verified = check_tick_xanh(uid)

            name_to_save = name_from_link if name_from_link else "Săn Meta Verified"

            avatar_url = get_facebook_avatar_url(uid)

            save_tracking_uid(chat_id, uid, name_to_save, "Auto Meta Check", 0, track_type="meta", is_verified=is_verified, avatar=avatar_url)

            update_user_stats(user_id, "add")

            status_text = "☑️ Đã có Meta Verified" if is_verified else "❌ Chưa có"

            msg = f"✅ **ĐÃ LƯU UID!**\nUID: `{uid}`\nTrạng thái: {status_text}\n\n(Bot đang treo theo dõi...)"

            markup = types.InlineKeyboardMarkup()

            markup.add(types.InlineKeyboardButton("❌ Hủy Theo Dõi", callback_data=f"del_{uid}"))

            

            # Tai avatar ve bytes de gui chinh xac
            _avt_bytes_meta = get_facebook_avatar_bytes(uid)
            if _avt_bytes_meta:
                try:
                    from io import BytesIO as _BIO
                    bot.send_photo(chat_id, _BIO(_avt_bytes_meta), caption=msg, reply_markup=markup, parse_mode="Markdown")
                except:
                    bot.send_message(chat_id, msg, reply_markup=markup, parse_mode="Markdown")
            elif avatar_url:
                try:
                    bot.send_photo(chat_id, avatar_url, caption=msg, reply_markup=markup, parse_mode="Markdown")
                except:
                    bot.send_message(chat_id, msg, reply_markup=markup, parse_mode="Markdown")
            else:
                bot.send_message(chat_id, msg, reply_markup=markup, parse_mode="Markdown")

            temp_user_state.pop(user_id, None); return

        else:

            st["uid"] = uid

            

            checking_msg = bot.reply_to(message, "⏳ Đang lấy thông tin profile...")

            profile = fb_extractor.get_profile(uid, fallback_name=name_from_link)

            

            if profile.get("status") == "ERROR":

                bot.send_message(chat_id, "⚠️ Không thể lấy thông tin chi tiết, nhưng vẫn sẽ tiếp tục thêm UID.")

            else:

                st["name"] = profile.get("name", st.get("name", f"UID {uid}"))

                st["avatar"] = profile.get("avatar", "")

                st["followers"] = profile.get("followers", 0)

                st["friends"] = profile.get("friends", 0)

                st["verified"] = profile.get("verified", False)

                st["bio"] = profile.get("bio", "")

            

            verified_text = " (Tích xanh ☑️)" if profile.get("verified") else ""

            info_msg = f"🔍 **THÔNG TIN PROFILE:**\n\n"

            info_msg += f"👤 **Tên:** {profile.get('name', 'Facebook User')}{verified_text}\n"

            if profile.get("bio"): info_msg += f"📖 **Bio:** _{profile['bio']}_\n"

            info_msg += f"\n📝 Vui lòng nhập **Ghi chú**:"

            

            st["step"] = "note"

            

            # Tai avatar ve bytes de gui qua Telegram chinh xac hon
            _avt_bytes = get_facebook_avatar_bytes(uid)
            if _avt_bytes:
                # Luu bytes vao state de dung lai o buoc price (tranh URL het han)
                st["avatar_bytes"] = _avt_bytes
                st["avatar"] = ""  # khong dung URL nua, dung bytes
                try:
                    from io import BytesIO as _BIO
                    bot.send_photo(chat_id, _BIO(_avt_bytes), caption=info_msg, parse_mode="Markdown")
                    bot.delete_message(chat_id, checking_msg.message_id)
                except:
                    bot.send_message(chat_id, info_msg, parse_mode="Markdown")
            elif profile.get("avatar"):
                st["avatar"] = profile["avatar"]
                try:
                    bot.send_photo(chat_id, profile["avatar"], caption=info_msg, parse_mode="Markdown")
                    bot.delete_message(chat_id, checking_msg.message_id)
                except:
                    bot.send_message(chat_id, info_msg, parse_mode="Markdown")
            else:
                bot.send_message(chat_id, info_msg, parse_mode="Markdown")

            return



    # Xử lý ghi chú và giá cho UID

    elif isinstance(st, dict):

        step = st.get("step")

        if step == "note":

            st["note"] = message.text; st["step"] = "price"

            bot.reply_to(message, "💰 Nhập GIÁ (Số):")

        elif step == "price":

            try: p = int(message.text.replace(".", ""))

            except: return bot.reply_to(message, "❌ Phải là số.")

            

            checking_msg = bot.reply_to(message, "⏳ Đang kiểm tra trạng thái UID...")

            

            stat = check_uid_live_die(st["uid"])

            initial_status = stat  # Giữ nguyên format LIVE/DIE chữ hoa

            

            save_tracking_uid(

                chat_id, 

                st["uid"], 

                st.get("name", f"UID {st['uid']}"), 

                st.get("note", "No note"), 

                p, 

                track_type="normal", 

                is_verified=st.get("verified", False), 

                initial_status=initial_status, 

                avatar=st.get("avatar", "")

            )

            update_user_stats(user_id, "add")

            

            try: bot.delete_message(chat_id, checking_msg.message_id)

            except: pass

            

            thoi_gian_hien_tai = datetime.now()

            

            # Lấy thông tin tài khoản

            ten_tai_khoan = st.get('name', 'Facebook User')

            uid_ket_qua = st['uid']

            ghi_chu = st.get('note', 'Không có ghi chú')

            

            # Xác định trạng thái và icon (initial_status giờ là LIVE/DIE chữ hoa)

            if initial_status == "LIVE":

                icon_trang_thai = "👉"

                icon_trang_thai2 = "🟢"

                icon_trang_thai3 = "🔎"

                chu_trang_thai = "ĐANG HOẠT ĐỘNG"

            else:

                icon_trang_thai = "👉"

                icon_trang_thai2 = "🔴"

                icon_trang_thai3 = "🔎"

                chu_trang_thai = "ĐÃ BỊ KHÓA❌"

            

            # Escape các giá trị cho MarkdownV2

            ten_tai_khoan_escaped = escape_markdown_v2(ten_tai_khoan)

            uid_escaped = escape_markdown_v2(uid_ket_qua)

            ghi_chu_escaped = escape_markdown_v2(ghi_chu)


            

            # Tạo link với UID đã escape

            link_tai_khoan = f"https://facebook\\.com/{uid_escaped}"

            

            thoi_gian_escaped = escape_markdown_v2(thoi_gian_hien_tai.strftime('%d/%m/%Y %H:%M:%S'))

            

            # Tạo message với format hiển thị thông tin

            ket_qua = (

                f"📘 FACEBOOK PROFILE\n"

                f"👤 *Tên:* ||{ten_tai_khoan_escaped}||\n"

                f"{icon_trang_thai3} *UID:* ||{uid_escaped}|| \\- [Link]({link_tai_khoan})\n"

                f"{icon_trang_thai2} *Trạng thái:* {chu_trang_thai}\n"

                f"📝 *Ghi chú:* {ghi_chu_escaped}\n"

                f"💵 *Giá:* ||{escape_markdown_v2(f'{p:,}' + ' VNĐ')}||\n"
                f"⏰ *Thời gian xử lý:* Vừa xong\n"
                f"📅 *Thời gian tạo:* {thoi_gian_escaped}\n"
                f"📊 *Tiến trình:* Đang theo dõi chờ {'DIE ❌' if initial_status == 'LIVE' else 'LIVE ✅'}\n"

                f"👤 *Hạn trả kèo:* Vĩnh viễn"

            )

            

            # Tạo keyboard với 4 nút giống mã gợi ý

            keyboard = types.InlineKeyboardMarkup(row_width=2)

            keyboard.row(

                types.InlineKeyboardButton("🔔 Cập nhật", callback_data=f"update_{uid_ket_qua}"),

                types.InlineKeyboardButton("📋 Danh Sách UID", callback_data=f"list_uid")

            )

            keyboard.row(

                types.InlineKeyboardButton("❌ Hủy kèo", callback_data=f"cancel_{uid_ket_qua}"),

                types.InlineKeyboardButton("✅ Done kèo", callback_data=f"done_{uid_ket_qua}")

            )

            

            # Gửi message với avatar nếu có
            if initial_status == "DIE":
                # UID die: gửi ảnh mark1.jpg (Mark cười - ĐÃ BỊ KHÓA), fallback mark3
                _die_photo = LOCAL_ANH1 if os.path.exists(LOCAL_ANH1) else LOCAL_ANH3
                try:
                    with open(_die_photo, "rb") as f:
                        bot.send_photo(chat_id, f, caption=ket_qua, parse_mode='MarkdownV2', reply_markup=keyboard, has_spoiler=True)
                except Exception as e:
                    print(f"❌ Lỗi gửi ảnh die: {e} - bot1.py:4127")
                    bot.send_message(chat_id, ket_qua, parse_mode='MarkdownV2', reply_markup=keyboard)
            else:
                # UID live: uu tien dung bytes (da download truoc), sau moi fallback URL
                avatar_bytes_st = st.get("avatar_bytes")
                avatar_url = st.get("avatar", "")
                if avatar_bytes_st:
                    try:
                        from io import BytesIO as _BIO2
                        bot.send_photo(chat_id, _BIO2(avatar_bytes_st), caption=ket_qua, parse_mode='MarkdownV2', reply_markup=keyboard, has_spoiler=True)
                    except Exception as e:
                        print(f"❌ Lỗi gửi avatar bytes: {e}")
                        bot.send_message(chat_id, ket_qua, parse_mode='MarkdownV2', reply_markup=keyboard)
                elif avatar_url:
                    try:
                        bot.send_photo(chat_id, avatar_url, caption=ket_qua, parse_mode='MarkdownV2', reply_markup=keyboard, has_spoiler=True)
                    except Exception as e:
                        print(f"❌ Lỗi gửi avatar URL: {e}")
                        bot.send_message(chat_id, ket_qua, parse_mode='MarkdownV2', reply_markup=keyboard)
                else:
                    bot.send_message(chat_id, ket_qua, parse_mode='MarkdownV2', reply_markup=keyboard)


            temp_user_state.pop(user_id, None)
            return



    # Nếu user gửi link Instagram hoặc Facebook Group → tự động xử lý
    if message.text:
        txt = message.text.strip()
        grig_plt = grig_detect_platform(txt)
        if grig_plt == 'facebook_group':
            # Giả lập lệnh /addpgr
            message.text = f"/addpgr {txt}"
            grig_cmd_addpgr(message)
            return
        elif grig_plt == 'instagram':
            message.text = f"/add {txt}"
            grig_cmd_add(message)
            return

    # Xử lý khi người dùng gửi UID trực tiếp (không qua menu)

    if message.text:

        uid_check, _ = get_uid_from_link(message.text) if not message.text.isdigit() else (None, None)

        if message.text.isdigit() or uid_check:

            bot.reply_to(message, "⚠️ Vui lòng chọn 'Thêm UID' trong menu để thêm vào danh sách theo dõi.")

            return



    # Gọi AI nếu không có xử lý nào khác

    call_deepseek_ai(user_id, message.chat.id, message.text)





def signal_handler(signum, frame):

    sys.exit(0)



def _get_fb_cookie_string():
    try:
        cookie_file = FILES.get("cookie", "cookie.txt")
        if os.path.exists(cookie_file):
            raw = open(cookie_file, "r", encoding="utf-8").read().strip()
            if raw:
                return raw
    except Exception:
        pass
    try:
        if FB_COOKIE and str(FB_COOKIE).strip():
            return str(FB_COOKIE).strip()
    except Exception:
        pass
    return ""


def _cookie_string_to_dict(cookie_string):
    cookies = {}
    for part in (cookie_string or "").split(";"):
        if "=" not in part:
            continue
        k, v = part.split("=", 1)
        k = k.strip()
        v = v.strip()
        if k:
            cookies[k] = urllib.parse.unquote(v) if "%" in v else v
    return cookies


def _cookie_string_to_playwright_cookies(cookie_string):
    cookie_dict = _cookie_string_to_dict(cookie_string)
    cookies = []
    for name, value in cookie_dict.items():
        cookies.append({
            "name": name,
            "value": value,
            "domain": ".facebook.com",
            "path": "/",
            "httpOnly": False,
            "secure": True,
            "sameSite": "Lax",
        })
    return cookies


def _decode_fb_url(s):
    if not s:
        return ""
    try:
        return str(s).replace("\\u0026", "&").replace("\\/", "/").replace("&amp;", "&").strip()
    except Exception:
        return str(s).strip()


def _extract_cover_candidates_from_html(html):
    html = html or ""
    patterns = [
        r'"coverPhoto".*?"uri":"([^"]+)"',
        r'"cover_photo".*?"url":"([^"]+)"',
        r'"cover_photo".*?"uri":"([^"]+)"',
        r'"comet_ufi_photo".*?"uri":"([^"]+fbcdn[^"]+)"',
        r'"image":\{"uri":"([^"]+fbcdn[^"]+)"[^}]*"width":(\d+),"height":(\d+)\}',
        r'"uri":"(https:\\/\\/[^"]+fbcdn[^"]+)"[^}]{0,120}"width":(\d{3,4})[^}]{0,80}"height":(\d{2,4})',
    ]
    out = []
    for pat in patterns:
        for m in re.finditer(pat, html):
            groups = m.groups()
            url = _decode_fb_url(groups[0])
            if not url.startswith("http"):
                continue
            if "fbcdn" not in url and "scontent" not in url:
                continue
            if url not in out:
                out.append(url)
    return out


def _download_fb_image_to_temp(image_url, uid_clean, cookie_string=""):
    if not image_url:
        return None
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/122 Safari/537.36",
            "Referer": f"https://www.facebook.com/{uid_clean}",
            "Accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8",
        }
        req_kwargs = {
            "headers": headers,
            "timeout": 25,
            "allow_redirects": True,
        }
        cookie_dict = _cookie_string_to_dict(cookie_string)
        if cookie_dict:
            req_kwargs["cookies"] = cookie_dict
        r = requests.get(image_url, **req_kwargs)
        ct = (r.headers.get("content-type") or "").lower()
        if r.status_code == 200 and r.content and ("image/" in ct or len(r.content) > 5000):
            temp_path = os.path.join(CACHE_DIR, f"cover_{random.randint(1000,9999)}.jpg")
            with open(temp_path, "wb") as f:
                f.write(r.content)
            return temp_path
    except Exception as e:
        print(f"⚠️ Tải ảnh cover trực tiếp lỗi: {e}")
    return None


def _get_facebook_cover_playwright(uid_clean):
    cookie_string = _get_fb_cookie_string()
    if not cookie_string:
        print("⚠️ Playwright cover fallback bỏ qua vì chưa có cookie Facebook")
        return None

    try:
        from playwright.sync_api import sync_playwright
    except Exception as e:
        print(f"⚠️ Chưa import được Playwright sync API: {e}")
        return None

    urls = [
        f"https://www.facebook.com/{uid_clean}",
        f"https://m.facebook.com/{uid_clean}",
        f"https://www.facebook.com/profile.php?id={uid_clean}",
        f"https://m.facebook.com/profile.php?id={uid_clean}",
    ]

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/122 Safari/537.36",
                viewport={"width": 1440, "height": 2200},
                ignore_https_errors=True,
            )
            pw_cookies = _cookie_string_to_playwright_cookies(cookie_string)
            if pw_cookies:
                context.add_cookies(pw_cookies)

            page = context.new_page()

            for url in urls:
                try:
                    page.goto(url, wait_until="domcontentloaded", timeout=60000)
                    page.wait_for_timeout(5000)

                    try:
                        page.evaluate("window.scrollTo(0, 500)")
                        page.wait_for_timeout(1500)
                    except Exception:
                        pass

                    html = page.content()
                    lower_html = html.lower()
                    if "log in to facebook" in lower_html or "login" in lower_html[:5000]:
                        continue

                    candidates = _extract_cover_candidates_from_html(html)

                    try:
                        dom_imgs = page.evaluate(
                            """() => Array.from(document.images).map(img => ({
                                src: img.currentSrc || img.src || "",
                                w: img.naturalWidth || img.width || 0,
                                h: img.naturalHeight || img.height || 0,
                                alt: img.alt || ""
                            }))"""
                        )
                    except Exception:
                        dom_imgs = []

                    scored = []
                    for item in dom_imgs or []:
                        src = _decode_fb_url((item or {}).get("src", ""))
                        w = int((item or {}).get("w") or 0)
                        h = int((item or {}).get("h") or 0)
                        if not src.startswith("http"):
                            continue
                        if "fbcdn" not in src and "scontent" not in src:
                            continue
                        if w < 400 or h < 120:
                            continue
                        if h > 0 and w > h * 1.2:
                            scored.append((w * h, src))
                    scored.sort(reverse=True)
                    for _, src in scored:
                        if src not in candidates:
                            candidates.append(src)

                    avatar_url = ""
                    try:
                        info = fb_extractor.extract_profile_info(html, vanity_url_name=uid_clean)
                        avatar_url = _decode_fb_url((info or {}).get("avatar", ""))
                    except Exception:
                        pass

                    for cover_url in candidates:
                        cover_url = _decode_fb_url(cover_url)
                        if not cover_url or cover_url == avatar_url:
                            continue
                        if "/p50x50/" in cover_url or "/s50x50/" in cover_url or "/p64x64/" in cover_url:
                            continue
                        saved = _download_fb_image_to_temp(cover_url, uid_clean, cookie_string=cookie_string)
                        if saved:
                            print(f"✅ Ảnh bìa OK từ PLAYWRIGHT: {cover_url}")
                            browser.close()
                            return saved
                except Exception as e:
                    print(f"⚠️ Playwright cover fallback lỗi ở {url}: {e}")
                    continue

            browser.close()
    except Exception as e:
        print(f"⚠️ Playwright cover fallback không chạy được: {e}")

    return None


def get_facebook_cover(uid):
    """Tai anh bia Facebook. Uu tien API, roi HTML+cookie, cuoi cung la Playwright."""
    try:
        uid_clean = _normalize_fb_uid_input(uid)
        apis_to_try = [
            (
                f"https://venzfin.io.vn/apifbvenzdev/index.php?input={urllib.parse.quote(uid_clean)}&key=Venzdev012026",
                ['cover', 'cover_url', 'cover_photo']
            ),
            (
                f"https://keyherlyswar.x10.mx/Apidocs/tien_ich/biafb.php?uid={urllib.parse.quote(uid_clean)}",
                ['cover', 'cover_url', 'cover_photo']
            ),
            (
                f"https://keyherlyswar.x10.mx/Apidocs/biafb.php?uid={urllib.parse.quote(uid_clean)}",
                ['cover', 'cover_url', 'cover_photo']
            ),
        ]

        for api_url, preferred_keys in apis_to_try:
            try:
                cover_bytes, resolved_url = _download_image_bytes(
                    api_url,
                    preferred_keys=preferred_keys,
                    timeout=12
                )
                if cover_bytes:
                    temp_path = os.path.join(CACHE_DIR, f"cover_{random.randint(1000,9999)}.jpg")
                    with open(temp_path, "wb") as f_out:
                        f_out.write(cover_bytes)
                    print(f"✅ Ảnh bìa OK từ API: {resolved_url or api_url}")
                    return temp_path
            except Exception as e:
                print(f"⚠️ Cover API lỗi: {e}")

        cookie_string = _get_fb_cookie_string()
        cookie_dict = _cookie_string_to_dict(cookie_string)
        has_cookie = bool(cookie_dict)
        base_headers = getattr(fb_extractor, "mobile_headers", {}) or {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 Chrome/119 Mobile Safari/537.36",
            "Accept-Language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
        }

        html_urls = [
            f"https://mbasic.facebook.com/{uid_clean}",
            f"https://m.facebook.com/{uid_clean}",
            f"https://www.facebook.com/{uid_clean}",
            f"https://www.facebook.com/profile.php?id={uid_clean}",
            f"https://m.facebook.com/profile.php?id={uid_clean}",
        ]
        for html_url in html_urls:
            try:
                req_kwargs = {"headers": dict(base_headers), "timeout": 20, "allow_redirects": True}
                if has_cookie:
                    req_kwargs["cookies"] = cookie_dict
                r = requests.get(html_url, **req_kwargs)
                if r.status_code != 200 or not r.text:
                    continue

                html = r.text
                lower_html = html.lower()
                if ("log in or sign up to view" in lower_html or "login" in lower_html) and not has_cookie:
                    continue

                info = fb_extractor.extract_profile_info(html, vanity_url_name=uid_clean)
                avatar_url = _decode_fb_url((info or {}).get("avatar", "").strip())
                candidate_urls = []

                direct_cover = _decode_fb_url((info or {}).get("cover", "").strip())
                if direct_cover:
                    candidate_urls.append(direct_cover)

                for extra_cover in _extract_cover_candidates_from_html(html):
                    if extra_cover and extra_cover not in candidate_urls:
                        candidate_urls.append(extra_cover)

                for cover_url in candidate_urls:
                    if not cover_url or cover_url == avatar_url:
                        continue
                    if not (cover_url.startswith("http") and ("fbcdn" in cover_url or "scontent" in cover_url or "xx.fbcdn.net" in cover_url)):
                        continue
                    saved = _download_fb_image_to_temp(cover_url, uid_clean, cookie_string=cookie_string)
                    if saved:
                        src = "HTML+COOKIE" if has_cookie else "HTML"
                        print(f"✅ Ảnh bìa OK từ {src}: {cover_url}")
                        return saved
            except Exception as e:
                print(f"⚠️ HTML cover fallback lỗi: {e}")

        pw_saved = _get_facebook_cover_playwright(uid_clean)
        if pw_saved:
            return pw_saved

        if not has_cookie:
            print(f"⚠️ Không tìm thấy ảnh bìa thật cho UID: {uid_clean} (chưa có cookie Facebook hoặc profile chặn public)")
        else:
            print(f"⚠️ Không tìm thấy ảnh bìa thật cho UID: {uid_clean} dù đã dùng cookie và Playwright")
        return None
    except Exception as e:
        print(f"❌ get_facebook_cover lỗi: {str(e)}")
        return None


def get_id(link):

    """Trích xuất UID từ link Facebook"""

    uid, _ = get_uid_from_link(link)

    return uid



# Thêm hàm get_facebook_cover và get_facebook_avatar sau hàm get_facebook_avatar_url

# (get_facebook_cover đã được định nghĩa ở trên với đầy đủ API)



def get_facebook_avatar(uid):

    """Tải avatar Facebook và trả về đường dẫn file tạm - dùng get_facebook_avatar_bytes có đầy đủ fallback"""

    try:
        avatar_data = get_facebook_avatar_bytes(uid)
        if avatar_data:
            temp_path = os.path.join(CACHE_DIR, f"avatar_{random.randint(1000,9999)}.jpg")
            with open(temp_path, "wb") as f:
                f.write(avatar_data)
            return temp_path
        return None

    except Exception as e:

        print(f"❌ Lỗi khi lấy avatar: {str(e)}")

        return None



# ===== PHẦN SOUNDCLOUD =====


def random_contrast_color(base_color):

    """Tạo màu tương phản với màu nền"""

    r, g, b, _ = base_color

    luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255

    if luminance > 0.5:

        r, g, b = random.randint(0, 50), random.randint(0, 50), random.randint(0, 50)

    else:

        r, g, b = random.randint(200, 255), random.randint(200, 255), random.randint(200, 255)

    h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)

    s = min(1.0, s + 0.9)

    v = min(1.0, v + 0.7)

    r, g, b = colorsys.hsv_to_rgb(h, s, v)

    return (int(r * 255), int(g * 255), int(b * 255), 255)



def tai_anh(url, ten_file):

    """Tải ảnh từ URL"""

    try:

        response = requests.get(url, timeout=5)

        if response.status_code == 200:

            duong_dan = os.path.join(SCL_PA, ten_file)

            with open(duong_dan, "wb") as f:

                f.write(response.content)

            return duong_dan

    except Exception as e:

        print(f"Lỗi tải ảnh: {e}")

        return None



def tao_nen(rong, cao):

    """Tạo nền từ ảnh random hoặc màu mặc định"""

    anh_list = [f for f in os.listdir(SCL_PATH) if f.endswith(('.jpg', '.png', '.jpeg'))]

    if not anh_list:

        return Image.new("RGBA", (rong, cao), (20, 20, 20, 255))

    duong_dan = os.path.join(SCL_PATH, random.choice(anh_list))

    bg = Image.open(duong_dan).convert("RGBA").resize((rong, cao), Image.Resampling.LANCZOS)

    return bg.filter(ImageFilter.GaussianBlur(radius=7))



def lay_headers():

    return {

        "User-Agent": "Mozilla/5.0",

        "Accept-Language": "en-US,en;q=0.9",

        "Referer": "https://soundcloud.com/",

        "Upgrade-Insecure-Requests": "1"

    }



def lay_client_id():

    global client_id_cache

    if client_id_cache:

        return client_id_cache

    try:

        res = requests.get('https://soundcloud.com/', headers=lay_headers(), timeout=15)

        soup = BeautifulSoup(res.text, 'html.parser')

        script_tags = soup.find_all('script', {'crossorigin': True})

        urls = [tag.get('src') for tag in script_tags if tag.get('src') and tag.get('src').startswith('https')]

        res = requests.get(urls[-1], headers=lay_headers(), timeout=15)

        client_id_cache = re.search(r'client_id:"(.*?)"', res.text).group(1)

        return client_id_cache

    except:

        return None



def cho_client_id():

    client_id = lay_client_id()

    while not client_id:

        time.sleep(2)

        client_id = lay_client_id()

    return client_id



def lay_thong_tin_bai_hat(link):

    try:

        client_id = cho_client_id()

        api_url = f'https://api-v2.soundcloud.com/resolve?url={link}&client_id={client_id}'

        response = requests.get(api_url, headers=lay_headers(), timeout=15)

        data = response.json()

        return {

            'play_count': data.get('playback_count', 0),

            'like_count': data.get('likes_count', 0),

            'comment_count': data.get('comment_count', 0),

            'username': data.get('user', {}).get('username', 'Unknown')

        }

    except:

        return {'play_count': 0, 'like_count': 0, 'comment_count': 0, 'username': 'Unknown'}



def tim_nhac(tu_khoa):

    try:

        base_url = 'https://soundcloud.com'

        search_url = f'https://m.soundcloud.com/search?q={urllib.parse.quote(tu_khoa)}'

        response = requests.get(search_url, headers=lay_headers(), timeout=15)

        soup = BeautifulSoup(response.text, 'html.parser')

        bai_hat_list = []

        url_pattern = re.compile(r'^/[^/]+/[^/]+$')

        

        for element in soup.select('li > div'):

            a_tag = element.select_one('a')

            if a_tag and a_tag.has_attr('href'):

                relative_url = a_tag['href']

                if url_pattern.match(relative_url):

                    ten = a_tag.get('aria-label', '').strip()

                    link = base_url + relative_url

                    img_tag = element.select_one('img')

                    anh_bia = img_tag['src'] if img_tag and img_tag.has_attr('src') else ""

                    metadata = lay_thong_tin_bai_hat(link)

                    bai_hat_list.append((

                        link, ten, anh_bia,

                        metadata['play_count'],

                        metadata['like_count'],

                        metadata['comment_count'],

                        metadata['username']

                    ))

            if len(bai_hat_list) >= 10:

                break

        return bai_hat_list

    except:

        return []



def tao_anh_danh_sach(danh_sach_bai_hat):

    """TẠO ẢNH DANH SÁCH"""

    try:

        scale = 2

        

        font_path = None

        emoji_font_path = None

        

        possible_fonts = [

            "arial unicode ms.otf",

            "Arial.ttf",

            "DejaVuSans.ttf",

            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",

            "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"

        ]

        

        for font_file in possible_fonts:

            if os.path.exists(font_file):

                font_path = font_file

                break

        

        possible_emoji_fonts = [

            "emoji.ttf",

            "NotoColorEmoji.ttf",

            "AppleColorEmoji.ttf",

            "/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf"

        ]

        

        for emoji_file in possible_emoji_fonts:

            if os.path.exists(emoji_file):

                emoji_font_path = emoji_file

                break

        

        if not font_path:

            print("[WARN] Không tìm thấy font chính, dùng font mặc định")

            font = ImageFont.load_default()

            emoji_font = font

            artist_font = font

            number_font = font

            info_font = font

        else:

            font = ImageFont.truetype(font_path, 28 * scale)

            emoji_font = ImageFont.truetype(emoji_font_path if emoji_font_path else font_path, 28 * scale)

            artist_font = ImageFont.truetype(font_path, 20 * scale)

            number_font = ImageFont.truetype(font_path, 40 * scale)

            info_font = ImageFont.truetype(font_path, 14 * scale)



        card_height = 105 * scale

        card_width = 583 * scale

        thumb_size = 90 * scale

        padding = 20 * scale

        spacing_y = 10 * scale

        card_padding = 8 * scale



        img_width = card_width + 2 * padding

        img_height = padding * 2 + len(danh_sach_bai_hat) * card_height + (len(danh_sach_bai_hat) - 1) * spacing_y



        background = tao_nen(img_width, img_height)

        image = Image.new("RGBA", (img_width, img_height), (0, 0, 0, 0))

        image.paste(background, (0, 0))

        draw = ImageDraw.Draw(image)



        box_colors = [

            (255, 20, 147, 110), (128, 0, 128, 110), (0, 100, 0, 110),

            (0, 0, 139, 110), (184, 134, 11, 110), (138, 3, 3, 110), (0, 0, 0, 80)

        ]

        box_color = random.choice(box_colors)

        title_color = random_contrast_color(box_color)

        number_color = random_contrast_color(box_color)

        artist_color = (255, 255, 255, 255)

        info_color = (255, 255, 255, 255)



        icon_colors = {

            "🎧": (0, 255, 0, 255),

            "🖤": (255, 0, 0, 255),

            "💬": (255, 215, 0, 255)

        }



        def dinh_dang_so(so):

            return f"{so:,}".replace(",", ".")



        def lay_do_rong_chu(chu, font_su_dung):

            try:

                bbox = draw.textbbox((0, 0), chu, font=font_su_dung)

                return bbox[2] - bbox[0]

            except:

                return len(chu) * 10



        def cat_ngan_chu(chu, do_rong_toi_da, font_chu, font_emoji):

            ket_qua = ''

            tong_rong = 0

            for ky_tu in chu:

                font_dung = font_emoji if emoji.is_emoji(ky_tu) else font_chu

                rong_ky_tu = lay_do_rong_chu(ky_tu, font_dung)

                if tong_rong + rong_ky_tu > do_rong_toi_da:

                    ket_qua += '...'

                    break

                ket_qua += ky_tu

                tong_rong += rong_ky_tu

            return ket_qua



        def ve_chu_co_bong(draw, vi_tri, chu, font_dung, mau_chu, mau_bong=(0, 0, 0, 150)):

            x, y = vi_tri

            draw.text((x + 2, y + 2), chu, font=font_dung, fill=mau_bong)

            draw.text((x, y), chu, font=font_dung, fill=mau_chu)



        for i, bai_hat in enumerate(danh_sach_bai_hat[:10]):

            link, ten, anh_bia, luot_nghe, luot_thich, binh_luan, nghe_si = bai_hat

            trai = padding

            tren = padding + i * (card_height + spacing_y)



            card_img = Image.new("RGBA", (card_width, card_height), (0, 0, 0, 0))

            card_draw = ImageDraw.Draw(card_img)

            card_draw.rounded_rectangle([0, 0, card_width, card_height], radius=20 * scale, fill=box_color)

            image.paste(card_img, (trai, tren), card_img.split()[3])



            if anh_bia:

                cover_path = tai_anh(anh_bia, f"cover_{i}.jpg")

                if cover_path:

                    cover = Image.open(cover_path).convert("RGB")

                    cover = ImageOps.fit(cover, (thumb_size, thumb_size), centering=(0.5, 0.5))

                    mask = Image.new("L", (thumb_size, thumb_size), 0)

                    draw_mask = ImageDraw.Draw(mask)

                    draw_mask.ellipse((0, 0, thumb_size, thumb_size), fill=255)

                    cover.putalpha(mask)

                    image.paste(cover, (trai + card_padding, tren + card_padding), cover)

                    os.remove(cover_path)



            x_chu = trai + card_padding + thumb_size + 20 * scale

            y_chu = tren + card_padding

            do_rong_chu_toi_da = card_width - thumb_size - 3 * card_padding - 20 * scale

            tieu_de_cat = cat_ngan_chu(ten, do_rong_chu_toi_da, font, emoji_font)



            for ky_tu in tieu_de_cat:

                font_dung = emoji_font if emoji.is_emoji(ky_tu) else font

                ve_chu_co_bong(draw, (x_chu, y_chu), ky_tu, font_dung, title_color)

                x_chu += lay_do_rong_chu(ky_tu, font_dung)



            x_nghe_si = trai + card_padding + thumb_size + 20 * scale

            y_nghe_si = y_chu + int(35 * scale)

            nghe_si_cat = cat_ngan_chu(nghe_si, do_rong_chu_toi_da, artist_font, emoji_font)

            for ky_tu in nghe_si_cat:

                font_dung = emoji_font if emoji.is_emoji(ky_tu) else artist_font

                ve_chu_co_bong(draw, (x_nghe_si, y_nghe_si), ky_tu, font_dung, artist_color)

                x_nghe_si += lay_do_rong_chu(ky_tu, font_dung)



            chu_thong_tin = f"🎧 {dinh_dang_so(luot_nghe)}  🖤 {dinh_dang_so(luot_thich)}  💬 {dinh_dang_so(binh_luan)}"

            x_thong_tin = trai + card_padding + thumb_size + 20 * scale

            y_thong_tin = tren + card_height - card_padding - info_font.size

            for ky_tu in chu_thong_tin:

                font_dung = emoji_font if emoji.is_emoji(ky_tu) else info_font

                mau_icon = icon_colors.get(ky_tu, info_color)

                ve_chu_co_bong(draw, (x_thong_tin, y_thong_tin), ky_tu, font_dung, mau_icon)

                x_thong_tin += lay_do_rong_chu(ky_tu, font_dung)



            chu_so = str(i + 1)

            rong_so = lay_do_rong_chu(chu_so, number_font)

            x_so = trai + card_width - rong_so - card_padding

            y_so = tren + (card_height - number_font.size) // 2

            ve_chu_co_bong(draw, (x_so, y_so), chu_so, number_font, number_color)



        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:

            image.convert("RGB").save(tmp.name, "PNG", quality=95)

            return tmp.name

    except Exception as e:

        print(f"Lỗi tạo ảnh danh sách: {e}")

        import traceback

        traceback.print_exc()

        return None



def tao_anh_bai_hat(bai_hat):

    """TẠO ẢNH BÀI HÁT ĐƠN"""

    try:

        scale = 2

        

        font_path = None

        emoji_font_path = None

        

        possible_fonts = [

            "arial unicode ms.otf",

            "Arial.ttf",

            "DejaVuSans.ttf",

            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

        ]

        

        for font_file in possible_fonts:

            if os.path.exists(font_file):

                font_path = font_file

                break

        

        possible_emoji_fonts = [

            "emoji.ttf",

            "NotoColorEmoji.ttf",

            "/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf"

        ]

        

        for emoji_file in possible_emoji_fonts:

            if os.path.exists(emoji_file):

                emoji_font_path = emoji_file

                break

        

        if not font_path:

            font = ImageFont.load_default()

            emoji_font = font

            title_font = font

            emoji_title_font = font

        else:

            font = ImageFont.truetype(font_path, 32 * scale)

            emoji_font = ImageFont.truetype(emoji_font_path if emoji_font_path else font_path, 32 * scale)

            title_font = ImageFont.truetype(font_path, 48 * scale)

            emoji_title_font = ImageFont.truetype(emoji_font_path if emoji_font_path else font_path, 48 * scale)



        padding = 80 * scale

        thumb_size = 300 * scale

        img_width = 1200 * scale

        img_height = 420 * scale



        image = Image.new("RGB", (img_width, img_height), (25, 25, 25))

        draw = ImageDraw.Draw(image)



        link, ten, anh_bia, luot_nghe, luot_thich, binh_luan, nghe_si = bai_hat

        background = tao_nen(img_width, img_height)

        image.paste(background, (0, 0))



        overlay = Image.new("RGBA", (img_width, img_height), (0, 0, 0, 128))

        image.paste(overlay, (0, 0), overlay)



        thumb = Image.new("RGB", (thumb_size, thumb_size), (50, 50, 50))

        if anh_bia:

            cover_path = tai_anh(anh_bia, "selected_cover.jpg")

            if cover_path:

                thumb = Image.open(cover_path).convert("RGB")

                thumb = ImageOps.fit(thumb, (thumb_size, thumb_size), centering=(0.5, 0.5))

                mask = Image.new("L", (thumb_size, thumb_size), 0)

                draw_mask = ImageDraw.Draw(mask)

                draw_mask.ellipse((0, 0, thumb_size, thumb_size), fill=255)

                thumb.putalpha(mask)

                os.remove(cover_path)



        image.paste(thumb, (padding, (img_height - thumb.height) // 2), thumb)



        base_colors = [(102, 204, 255), (255, 255, 180), (102, 255, 204)]

        colors = random.sample(base_colors, 3)



        def lay_mau_gradient(x, tong_rong):

            ti_le = x / tong_rong if tong_rong > 0 else 0

            if ti_le < 0.5:

                c1, c2 = colors[0], colors[1]

                ti_le *= 2

            else:

                c1, c2 = colors[1], colors[2]

                ti_le = (ti_le - 0.5) * 2

            return (int(c1[0] + (c2[0] - c1[0]) * ti_le),

                    int(c1[1] + (c2[1] - c1[1]) * ti_le),

                    int(c1[2] + (c2[2] - c1[2]) * ti_le))



        text_x = padding + thumb.width + 50 * scale

        max_text_width = img_width - text_x - padding



        def rut_gon_chu(chu, f1, f2):

            rong_hien_tai = 0

            ket_qua = ""

            for ky_tu in chu:

                f = f2 if emoji.is_emoji(ky_tu) else f1

                try:

                    rong_ky_tu = f.getlength(ky_tu)

                except:

                    rong_ky_tu = 10

                if rong_hien_tai + rong_ky_tu > max_text_width:

                    ket_qua += "..."

                    break

                ket_qua += ky_tu

                rong_hien_tai += rong_ky_tu

            return ket_qua



        def ve_chu_gradient(draw, chu, x, y, f1, f2):

            chu_rut_gon = rut_gon_chu(chu, f1, f2)

            try:

                tong_rong = sum((f2 if emoji.is_emoji(c) else f1).getlength(c) for c in chu_rut_gon)

            except:

                tong_rong = len(chu_rut_gon) * 10

            vi_tri_x = x

            for ky_tu in chu_rut_gon:

                f = f2 if emoji.is_emoji(ky_tu) else f1

                try:

                    rong_ky_tu = f.getlength(ky_tu)

                except:

                    rong_ky_tu = 10

                mau = lay_mau_gradient(vi_tri_x - x, tong_rong)

                draw.text((vi_tri_x + 2, y + 2), ky_tu, font=f, fill=(0, 0, 0, 120))

                draw.text((vi_tri_x, y), ky_tu, font=f, fill=mau)

                vi_tri_x += rong_ky_tu

            return y + int(f1.size * 1.6)



        text_y = padding

        text_y = ve_chu_gradient(draw, f"🎧 {ten}", text_x, text_y, title_font, emoji_title_font)

        text_y = ve_chu_gradient(draw, f"👤 {nghe_si}", text_x, text_y, font, emoji_font)

        text_y = ve_chu_gradient(draw, "🎯 Nền tảng: SoundCloud ☁️", text_x, text_y, font, emoji_font)

        ve_chu_gradient(draw, f"🎶 {luot_nghe:,} ❤️ {luot_thich:,} 💬 {binh_luan:,}", text_x, text_y, font, emoji_font)



        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:

            image.save(tmp.name, "PNG", quality=95)

            return tmp.name

    except Exception as e:

        print(f"Lỗi tạo ảnh bài hát: {e}")

        import traceback

        traceback.print_exc()

        return None



def tai_hls_bang_ffmpeg(hls_url):

    try:

        output_path = os.path.join(SCL_PA, f"soundcloud_{int(time.time())}.mp3")

        cmd = [

            'ffmpeg', '-y', '-i', hls_url, '-vn',

            '-acodec', 'libmp3lame', '-b:a', '192k',

            '-ar', '44100', output_path

        ]

        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=180)

        if result.returncode != 0:

            return None

        if os.path.exists(output_path) and os.path.getsize(output_path) > 0:

            return output_path

        return None

    except:

        return None



def tai_nhac_soundcloud(link_bai_hat):

    try:

        client_id = cho_client_id()

        api_url = f'https://api-v2.soundcloud.com/resolve?url={link_bai_hat}&client_id={client_id}'

        response = requests.get(api_url, headers=lay_headers(), timeout=15)

        data = response.json()

        transcodings = data.get('media', {}).get('transcodings', [])

        if not transcodings:

            return None

        

        stream_url = None

        for t in transcodings:

            if 'progressive' in t.get('format', {}).get('protocol', '').lower():

                stream_url = t.get('url')

                break

        if not stream_url:

            stream_url = transcodings[0].get('url')

        

        stream_response = requests.get(f"{stream_url}?client_id={client_id}", headers=lay_headers(), timeout=30)

        audio_url = stream_response.json().get('url')

        

        if '.m3u8' in audio_url or 'hls' in audio_url.lower():

            return tai_hls_bang_ffmpeg(audio_url)

        

        audio_response = requests.get(audio_url, headers=lay_headers(), stream=True, timeout=60)

        audio_path = os.path.join(SCL_PA, f"soundcloud_{int(time.time())}.mp3")

        with open(audio_path, 'wb') as f:

            for chunk in audio_response.iter_content(chunk_size=8192):

                if chunk:

                    f.write(chunk)

        return audio_path if os.path.exists(audio_path) else None

    except:

        return None



def gui_nhac(chat_id, bai_hat, user_id):
    try:
        link, ten, anh_bia, luot_nghe, luot_thich, binh_luan, nghe_si = bai_hat
        tin_trang_thai = bot.send_message(chat_id, "⏳ Đang tải nhạc...")
        
        duong_dan_nhac = tai_nhac_soundcloud(link)
        if not duong_dan_nhac:
            bot.edit_message_text("❌ Không thể tải nhạc!", tin_trang_thai.chat.id, tin_trang_thai.message_id)
            return
        
        duong_dan_anh = tao_anh_bai_hat(bai_hat)
        if duong_dan_anh:
            with open(duong_dan_anh, 'rb') as anh:
                bot.send_photo(chat_id, anh, caption=f"🎵 {ten}\n👤 {nghe_si}")
            os.remove(duong_dan_anh)
        
        chu_thich = (
            f"🎵 {ten}\n"
            f"👤 {nghe_si}\n"
            f"🎧 {luot_nghe:,} • ❤️ {luot_thich:,} • 💬 {binh_luan:,}\n"
            f"━━━━━━━━━━━━━━━━━━━\n"
            f"🔊 Nhấn nút để điều khiển"
        )
        
        ban_phim = types.InlineKeyboardMarkup(row_width=3)
        ban_phim.row(
            types.InlineKeyboardButton("🛑 Tắt", callback_data="music_stop"),
            types.InlineKeyboardButton("🔄 Nghe lại", callback_data="music_replay"),
            types.InlineKeyboardButton("🔁 Lặp", callback_data="music_loop")
        )
        
        if music_cache.get(user_id, {}).get('loop', False):
            chu_thich += "\n\n🔁 Chế độ lặp: BẬT"
        
        with open(duong_dan_nhac, 'rb') as nhac:
            bot.send_voice(chat_id, nhac, caption=chu_thich, reply_markup=ban_phim)
        
        bot.delete_message(tin_trang_thai.chat.id, tin_trang_thai.message_id)
        os.remove(duong_dan_nhac)
        
    except Exception as e:
        bot.send_message(chat_id, f"❌ Lỗi: {e}")

    except Exception as e:

        print(f"Lỗi guitn: {e}")

        bot.reply_to(message, f"❌ Lỗi: {str(e)[:100]}")



def init_config():

    config = get_config()

    if "ANHDIE" in config:

        global ANHDIE

        ANHDIE = config["ANHDIE"]

    if "ANHLIVE" in config:

        global ANHLIVE

        ANHLIVE = config["ANHLIVE"]

        


# ============================================================
# TÍCH HỢP BOTGR - THEO DÕI FACEBOOK GROUP & INSTAGRAM
# Copy nguyên xi từ botgr.py
# ============================================================
import colorsys
from io import BytesIO

GRIG_DATA_FILE = "grig_data.json"
GRIG_CACHE_DIR = "grig_cache/"
GRIG_AVATAR_CACHE = "grig_avatar_cache/"
GRIG_AVT_DIE = "avt.jpg"
GRIG_DIE_CONFIRM_NEEDED = 2

os.makedirs(GRIG_CACHE_DIR, exist_ok=True)
os.makedirs(GRIG_AVATAR_CACHE, exist_ok=True)

grig_die_tracker = {}   # { "user_id:uid": count }
grig_checking_processes = {}  # { "user_id": thread }

def _grig_die_key(user_id, uid):
    return f"{user_id}:{uid}"

def grig_reset_die(user_id, uid):
    grig_die_tracker.pop(_grig_die_key(user_id, uid), None)

def grig_increment_die(user_id, uid):
    key = _grig_die_key(user_id, uid)
    grig_die_tracker[key] = grig_die_tracker.get(key, 0) + 1
    return grig_die_tracker[key]

# ---- DATA MANAGER ----
class GrigDataManager:
    def __init__(self):
        self.data = self._load()

    def _load(self):
        if os.path.exists(GRIG_DATA_FILE):
            try:
                with open(GRIG_DATA_FILE, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                pass
        return {}

    def save(self):
        with open(GRIG_DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

    def _ensure(self, user_id):
        uid = str(user_id)
        if uid not in self.data:
            self.data[uid] = {'accounts': {}}

    def add_account(self, user_id, uid, name, link, note, status, platform, avatar_path=None):
        self._ensure(user_id)
        self.data[str(user_id)]['accounts'][uid] = {
            'link': link, 'note': note, 'name': name, 'status': status,
            'last_check': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            'die_count': 0, 'avatar_path': avatar_path, 'platform': platform
        }
        self.save()

    def update_status(self, user_id, uid, status):
        uid_str = str(uid); user_str = str(user_id)
        if user_str not in self.data or uid_str not in self.data[user_str]['accounts']:
            return False
        old = self.data[user_str]['accounts'][uid_str].get('status', 'unknown')
        self.data[user_str]['accounts'][uid_str]['last_check'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.data[user_str]['accounts'][uid_str]['status'] = status
        changed = (old != status)
        if changed and status == 'die' and old == 'live':
            cur = self.data[user_str]['accounts'][uid_str].get('die_count', 0)
            self.data[user_str]['accounts'][uid_str]['die_count'] = cur + 1
        if changed:
            self.save()
        return changed

    def remove_account(self, user_id, uid):
        user_str = str(user_id)
        if user_str in self.data and uid in self.data[user_str]['accounts']:
            ap = self.data[user_str]['accounts'][uid].get('avatar_path')
            if ap and os.path.exists(ap):
                try: os.remove(ap)
                except: pass
            del self.data[user_str]['accounts'][uid]
            self.save()
            return True
        return False

    def get_accounts(self, user_id, platform='all'):
        accs = self.data.get(str(user_id), {}).get('accounts', {})
        if platform == 'all':
            return accs
        return {uid: d for uid, d in accs.items() if d.get('platform') == platform}

    def get_live(self, user_id, platform='all'):
        return {uid: d for uid, d in self.get_accounts(user_id, platform).items() if d['status'] == 'live'}

    def get_die(self, user_id, platform='all'):
        return {uid: d for uid, d in self.get_accounts(user_id, platform).items() if d['status'] == 'die'}

grig_dm = GrigDataManager()

# ---- CHECK INSTAGRAM ----
def grig_extract_ig_username(link):
    patterns = [r'instagram\.com/([^/?#\s]+)', r'instagr\.am/([^/?#\s]+)']
    for p in patterns:
        m = re.search(p, link)
        if m:
            uname = m.group(1).strip('/')
            if uname and uname not in ['p', 'reel', 'stories', 'tv', 'explore']:
                return uname
    return None

def grig_check_instagram(username):
    """
    Check Instagram sống/die:
    - Còn tồn tại + PUBLIC  → live
    - Khóa wall (private)   → die  (user muốn treat private = die)
    - Bị xóa / ban          → die
    - Lỗi mạng              → unknown (không báo die ảo)
    """
    username = username.strip().lstrip('@')

    # ── API 1: keyherlyswar mới (nhanh, check được is_private) ──
    try:
        r1 = requests.get(
            f"https://keyherlyswar.x10.mx/Apidocs/get_info/getinfoinsta.php?username={username}",
            timeout=12
        )
        if r1.status_code == 200:
            d1 = r1.json()
            ud = d1.get('data') or {}
            if ud and (ud.get('id') or ud.get('username')):
                # Tài khoản tồn tại — check private
                if ud.get('is_private', False):
                    return 'die'   # Khóa wall = die
                return 'live'
            err = str(d1.get('message', '') or d1.get('error', '') or d1.get('status', '')).lower()
            if any(x in err for x in ['not found', 'user not found', 'does not exist', 'no user', 'invalid']):
                pass  # Cần double-check scrape
            else:
                return 'unknown'
        elif r1.status_code == 404:
            pass  # Tiếp tục double-check
        else:
            return 'unknown'
    except Exception:
        return 'unknown'

    # ── Double-check scrape instagram.com ──
    try:
        headers2 = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
            'Accept-Language': 'vi-VN,vi;q=0.9',
        }
        r2 = requests.get(
            f"https://www.instagram.com/{username}/",
            headers=headers2, timeout=12, allow_redirects=True
        )
        if r2.status_code == 404:
            return 'die'
        if r2.status_code == 200:
            html = r2.text
            # Khóa wall
            if '"is_private":true' in html or '"isPrivate":true' in html:
                return 'die'
            # Bị xóa / ban
            html_lower = html.lower()
            if 'page not found' in html_lower or 'sorry, this page' in html_lower:
                return 'die'
            # Còn tồn tại public
            if f'"username":"{username.lower()}"' in html.lower():
                return 'live'
            if f'@{username.lower()}' in html.lower()[:8000]:
                return 'live'
        return 'unknown'
    except Exception:
        return 'unknown'


# ---- CHECK FACEBOOK GROUP ----
def grig_check_fb_group(group_id):
    try:
        url = f"https://www.facebook.com/groups/{group_id}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8',
            'Referer': 'https://www.facebook.com/'
        }
        resp = requests.get(url, headers=headers, timeout=12, allow_redirects=True)
        if resp.status_code == 404:
            return 'die'
        if resp.status_code != 200:
            return 'unknown'
        content = resp.text.lower()
        hard_die = ['content not found', "this content isn't available", "this group isn't available",
                    'group not found', 'violated our community standards', 'violated our terms']
        for sign in hard_die:
            if sign in content:
                return 'die'
        live_signs = ['groupid', 'group_id', 'join group', 'members', 'about this group',
                      'group rules', 'public group', 'private group', '/groups/', 'facebook.com/groups']
        for sign in live_signs:
            if sign in content:
                return 'live'
        title_m = re.search(r'<title>(.*?)</title>', resp.text, re.IGNORECASE)
        if title_m:
            title = title_m.group(1).strip().lower()
            bad = ['facebook', 'log in', 'sign up', 'đăng nhập', 'đăng ký']
            if title and not any(b in title for b in bad) and len(title) > 3:
                return 'live'
        return 'unknown'
    except requests.exceptions.Timeout:
        return 'unknown'
    except:
        return 'unknown'

# ---- GET INSTAGRAM INFO ----
def grig_get_ig_info(link):
    """Lấy thông tin Instagram cho tracking — dùng chung _parse_ig_user_data."""
    try:
        username = grig_extract_ig_username(link)
        if not username:
            return None, "❌ Không lấy được username từ link Instagram"

        user_data = None

        # API 1: keyherlyswar (ưu tiên)
        try:
            r = requests.get(
                f"https://keyherlyswar.x10.mx/Apidocs/get_info/getinfoinsta.php?username={username}",
                timeout=FAST_API_TIMEOUT
            )
            if r.status_code == 200:
                d = r.json().get("data") or {}
                if d and (d.get("id") or d.get("username")):
                    user_data = d
        except Exception:
            pass

        # API 2: i.instagram.com fallback
        if not user_data:
            try:
                r2 = requests.get(
                    f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}",
                    headers={
                        "User-Agent": "Instagram 219.0.0.12.117 Android",
                        "Accept": "application/json",
                        "X-IG-App-ID": "936619743392459",
                    },
                    timeout=FAST_API_TIMEOUT
                )
                if r2.status_code == 200:
                    j = r2.json()
                    u = j.get("data", {}).get("user") or j.get("user") or {}
                    if u:
                        user_data = u
            except Exception:
                pass

        if not user_data:
            return None, "❌ Không thể lấy thông tin Instagram"

        return _parse_ig_user_data(user_data, username), None
    except Exception as e:
        return None, f"❌ Lỗi: {str(e)}"

# ---- GET INSTAGRAM AVATAR ----
def grig_get_ig_avatar(username):
    """Lấy avatar Instagram - thử nhiều API, không download URL trực tiếp của IG (bị block)"""
    save_path = os.path.join(GRIG_CACHE_DIR, f"ig_avatar_{random.randint(1000,9999)}.jpg")

    # Method 1: unavatar.io - proxy public, không bị block
    try:
        url = f"https://unavatar.io/instagram/{username}"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        r = requests.get(url, headers=headers, timeout=FAST_API_TIMEOUT, allow_redirects=True)
        if r.status_code == 200 and len(r.content) > 2000 and r.headers.get('content-type','').startswith('image'):
            with open(save_path, 'wb') as f:
                f.write(r.content)
            return save_path
    except:
        pass

    # Method 2: API lấy URL rồi dùng headers giả Instagram để download
    try:
        api_url = f"https://keyherlyswar.x10.mx/Apidocs/get_info/getinfoinsta.php?username={username}"
        resp = requests.get(api_url, timeout=FAST_API_TIMEOUT)
        if resp.status_code == 200:
            data = resp.json()
            user_data = data.get('data', {})
            avatar_url = user_data.get('profile_pic_url_hd') or user_data.get('profile_pic_url')
            if avatar_url:
                # Dùng headers giống browser thật
                img_headers = {
                    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15',
                    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
                    'Accept-Language': 'vi-VN,vi;q=0.9',
                    'Referer': 'https://www.instagram.com/',
                    'sec-fetch-dest': 'image',
                    'sec-fetch-mode': 'no-cors',
                    'sec-fetch-site': 'cross-site',
                }
                ir = requests.get(avatar_url, headers=img_headers, timeout=FAST_API_TIMEOUT)
                if ir.status_code == 200 and len(ir.content) > 2000:
                    with open(save_path, 'wb') as f:
                        f.write(ir.content)
                    return save_path
    except:
        pass

    # Method 3: i.instagram.com API
    try:
        url3 = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}"
        h3 = {
            'User-Agent': 'Instagram 219.0.0.12.117 Android',
            'Accept': '*/*',
        }
        r3 = requests.get(url3, headers=h3, timeout=FAST_API_TIMEOUT)
        if r3.status_code == 200:
            d3 = r3.json()
            pic = d3.get('data', {}).get('user', {}).get('profile_pic_url_hd') or                   d3.get('data', {}).get('user', {}).get('profile_pic_url')
            if pic:
                ir3 = requests.get(pic, headers=h3, timeout=FAST_API_TIMEOUT)
                if ir3.status_code == 200 and len(ir3.content) > 2000:
                    with open(save_path, 'wb') as f:
                        f.write(ir3.content)
                    return save_path
    except:
        pass

    # Method 4: Session + cookies để bypass Instagram block
    try:
        session = requests.Session()
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'vi-VN,vi;q=0.9',
        })
        session.get('https://www.instagram.com/', timeout=10)
        api_url = f"https://keyherlyswar.x10.mx/Apidocs/get_info/getinfoinsta.php?username={username}"
        resp = session.get(api_url, timeout=FAST_API_TIMEOUT)
        if resp.status_code == 200:
            ud = resp.json().get('data', {})
            pic_url = ud.get('profile_pic_url_hd') or ud.get('profile_pic_url')
            if pic_url:
                ir = session.get(pic_url, timeout=FAST_API_TIMEOUT)
                if ir.status_code == 200 and len(ir.content) > 2000:
                    with open(save_path, 'wb') as f:
                        f.write(ir.content)
                    return save_path
    except:
        pass

    return None

# ---- GET FACEBOOK GROUP AVATAR ----
def grig_get_gr_avatar(group_id):
    try:
        url = f"https://graph.facebook.com/{group_id}/picture?type=large"
        resp = requests.get(url, timeout=10, allow_redirects=True)
        if resp.status_code == 200 and resp.headers.get('content-type', '').startswith('image') and len(resp.content) > 5000:
            path = os.path.join(GRIG_CACHE_DIR, f"grp_avt_{random.randint(1000,9999)}.jpg")
            with open(path, 'wb') as f:
                f.write(resp.content)
            return path
    except:
        pass
    try:
        group_url = f"https://m.facebook.com/groups/{group_id}"
        headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15'}
        resp = requests.get(group_url, headers=headers, timeout=10)
        if resp.status_code == 200:
            all_images = re.findall(r'(https://[^"\'>\s]+\.(?:jpg|jpeg|png)[^"\'>\s]*)', resp.text, re.IGNORECASE)
            for img_url in all_images[:8]:
                try:
                    img_url = img_url.replace('\\/', '/').replace('\\u0026', '&').replace('&amp;', '&')
                    if any(x in img_url.lower() for x in ['rsrc.php', 'static', 'emoji', 'icon']):
                        continue
                    img_resp = requests.get(img_url, timeout=8, headers=headers)
                    if img_resp.status_code == 200 and 10000 < len(img_resp.content) < 500000:
                        path = os.path.join(GRIG_CACHE_DIR, f"grp_avt_{random.randint(1000,9999)}.jpg")
                        with open(path, 'wb') as f:
                            f.write(img_resp.content)
                        return path
                except:
                    continue
    except:
        pass
    return None

# ---- GET FACEBOOK GROUP ID & NAME ----
def grig_get_group_id_name(link):
    try:
        url = "https://id.traodoisub.com/api.php"
        headers = {
            "accept": "application/json, text/javascript, */*; q=0.01",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "origin": "https://id.traodoisub.com",
            "referer": "https://id.traodoisub.com/",
            "user-agent": "Mozilla/5.0",
            "x-requested-with": "XMLHttpRequest"
        }
        resp = requests.post(url, headers=headers, data={"link": link}, timeout=10)
        if resp.status_code == 200:
            result = resp.json()
            group_id = result.get("id")
            group_name = result.get("name", "")
            if group_id:
                if not group_name or group_name.lower() in ['facebook', 'không rõ', '']:
                    try:
                        group_url = f'https://m.facebook.com/groups/{group_id}'
                        h = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15'}
                        r = requests.get(group_url, headers=h, timeout=10)
                        if r.status_code == 200:
                            tm = re.search(r'<title>(.*?)</title>', r.text, re.IGNORECASE)
                            if tm:
                                title = re.sub(r'\s*\|\s*Facebook$', '', tm.group(1).strip(), flags=re.IGNORECASE).strip()
                                bad = ['facebook', 'log in', 'đăng nhập']
                                if title and title.lower() not in bad:
                                    group_name = title
                    except:
                        pass
                if not group_name:
                    group_name = f"Group {group_id}"
                return group_id, group_name, 'live'
        return None, None, 'die'
    except Exception as e:
        return None, None, 'unknown'

# ---- DETECT PLATFORM ----
def grig_detect_platform(link):
    ll = link.lower()
    if '/groups/' in ll and 'facebook.com' in ll:
        return 'facebook_group'
    if 'instagram.com' in ll or 'instagr.am' in ll:
        return 'instagram'
    return None

# ---- ESCAPE MARKDOWN V2 ----
def grig_esc(text):
    if not text:
        return ""
    escape_chars = r'_*[]()~`>#+-=|{}.!'
    result = ""
    for char in str(text):
        if char in escape_chars:
            result += '\\' + char
        else:
            result += char
    return result

# ---- AUTO CHECK LOOP ----
def grig_auto_check_loop(user_id):
    import logging
    logger_g = logging.getLogger(f"grig_{user_id}")
    logger_g.info(f"🚀 Khởi động luồng GRIG check cho User {user_id}")
    time.sleep(random.uniform(0.5, 2.0))
    check_count = 0

    while str(user_id) in grig_checking_processes:
        try:
            accounts = grig_dm.get_accounts(user_id)
            if not accounts:
                time.sleep(10)
                continue

            for uid, account_data in list(accounts.items()):
                try:
                    time.sleep(random.uniform(3.0, 6.0))  # Delay giữa các acc
                    platform = account_data.get('platform', '')
                    link = account_data.get('link', '')

                    if platform == 'instagram':
                        username = grig_extract_ig_username(link) or uid
                        raw_status = grig_check_instagram(username)
                    elif platform == 'facebook_group':
                        raw_status = grig_check_fb_group(uid)
                    else:
                        continue

                    if raw_status == 'live':
                        grig_reset_die(user_id, uid)
                        status = 'live'
                    elif raw_status == 'die':
                        count = grig_increment_die(user_id, uid)
                        if count >= GRIG_DIE_CONFIRM_NEEDED:
                            status = 'die'
                        else:
                            continue
                    else:
                        continue  # unknown → bỏ qua, tránh die ảo

                    old_status = account_data.get('status', 'unknown')
                    changed = grig_dm.update_status(user_id, uid, status)

                    if changed:
                        grig_reset_die(user_id, uid)
                        current = grig_dm.get_accounts(user_id).get(uid, {})
                        name = current.get('name', 'Không rõ')
                        note = current.get('note', 'Không có')
                        die_count = current.get('die_count', 0)
                        avatar_path = current.get('avatar_path')

                        if platform == 'instagram':
                            plt_emoji = '📷'
                            id_label = 'Username'
                        else:
                            plt_emoji = '👥'
                            id_label = 'Group ID'

                        time_str = datetime.now().strftime('%H:%M:%S')
                        date_str = datetime.now().strftime('%d/%m/%Y')

                        keyboard = types.InlineKeyboardMarkup(row_width=2)
                        keyboard.row(
                            types.InlineKeyboardButton("✅ Done kèo", callback_data=f"grig_done_{uid}"),
                            types.InlineKeyboardButton("❌ Hủy kèo", callback_data=f"grig_cancel_{uid}")
                        )
                        keyboard.row(
                            types.InlineKeyboardButton("📋 Danh sách", callback_data="grig_list"),
                            types.InlineKeyboardButton("🚫 Hủy theo dõi", callback_data=f"grig_unfollow_{uid}")
                        )

                        if status == 'die' and old_status == 'live':
                            msg = (
                                f"⚠️ THÔNG BÁO THAY ĐỔI TRẠNG THÁI\n"
                                f"━━━━━━━━━━━━━━━━━━━\n"
                                f"{plt_emoji} Platform: {grig_esc(platform.upper().replace('_', ' '))}\n"
                                f"👤 Tên: {grig_esc(name)}\n"
                                f"🆔 {id_label}: `{grig_esc(uid)}`\n"
                                f"📝 Ghi chú: {grig_esc(note)}\n"
                                f"🔄 Trạng thái: LIVE → *DIE*\n"
                                f"🕐 Giờ: {grig_esc(time_str)}\n"
                                f"📅 Ngày: {grig_esc(date_str)}\n"
                                f"🔢 Số lần DIE: {die_count}\n"
                                f"━━━━━━━━━━━━━━━━━━━"
                            )
                            try:
                                if os.path.exists(GRIG_AVT_DIE):
                                    with open(GRIG_AVT_DIE, 'rb') as f:
                                        bot.send_photo(user_id, f, caption=msg, parse_mode='MarkdownV2', reply_markup=keyboard)
                                else:
                                    bot.send_message(user_id, msg, parse_mode='MarkdownV2', reply_markup=keyboard)
                            except Exception as e:
                                print(f"Gửi DIE GRIG lỗi: {e}")

                        elif status == 'live' and old_status in ['die', 'unknown']:
                            msg = (
                                f"🎉 THÔNG BÁO SỐNG LẠI\n"
                                f"━━━━━━━━━━━━━━━━━━━\n"
                                f"{plt_emoji} Platform: {grig_esc(platform.upper().replace('_', ' '))}\n"
                                f"👤 Tên: {grig_esc(name)}\n"
                                f"🆔 {id_label}: `{grig_esc(uid)}`\n"
                                f"📝 Ghi chú: {grig_esc(note)}\n"
                                f"🔄 Trạng thái: DIE → *LIVE*\n"
                                f"🕐 Giờ: {grig_esc(time_str)}\n"
                                f"📅 Ngày: {grig_esc(date_str)}\n"
                                f"━━━━━━━━━━━━━━━━━━━"
                            )
                            try:
                                if avatar_path and os.path.exists(avatar_path):
                                    with open(avatar_path, 'rb') as f:
                                        bot.send_photo(user_id, f, caption=msg, parse_mode='MarkdownV2', reply_markup=keyboard)
                                else:
                                    bot.send_message(user_id, msg, parse_mode='MarkdownV2', reply_markup=keyboard)
                            except Exception as e:
                                print(f"Gửi LIVE GRIG lỗi: {e}")

                    check_count += 1

                except Exception as e:
                    print(f"Lỗi check GRIG {uid} user {user_id}: {e}")
                    continue

            time.sleep(random.uniform(5.0, 10.0))

        except Exception as e:
            print(f"Vòng lặp GRIG lỗi user {user_id}: {e}")
            time.sleep(15)

def grig_start_check(user_id):
    key = str(user_id)
    if key in grig_checking_processes and grig_checking_processes[key].is_alive():
        return False
    t = threading.Thread(
        target=grig_auto_check_loop,
        args=(user_id,),
        daemon=True,
        name=f"GRIG-{user_id}"
    )
    t.start()
    grig_checking_processes[key] = t
    return True

def grig_stop_check(user_id):
    key = str(user_id)
    if key in grig_checking_processes:
        del grig_checking_processes[key]
        return True
    return False

def grig_restart_threads():
    for user_id_str in grig_dm.data.keys():
        accounts = grig_dm.get_accounts(user_id_str)
        if accounts:
            grig_start_check(user_id_str)

# ---- /add - THÊM INSTAGRAM ----
@bot.message_handler(commands=['add'])
def grig_cmd_add(message):
    if not require_feature_access_message(message, "them_instagram", FEATURE_LABELS["them_instagram"]):
        return
    user_id = message.from_user.id
    try:
        content = message.text.replace('/add', '').strip()
        if not content:
            bot.reply_to(message, "❌ Cú pháp: /add <link> | <ghi chú>\n\nVí dụ:\n/add https://instagram.com/user123 | Check kèo")
            return

        parts = [p.strip() for p in content.split('|')]
        link = parts[0]
        note = parts[1] if len(parts) > 1 else "Không có ghi chú"

        platform = grig_detect_platform(link)
        if platform != 'instagram':
            bot.reply_to(message, "❌ Lệnh /add chỉ dùng cho Instagram!\n\n💡 Dùng /addpgr cho Facebook Group")
            return

        username = grig_extract_ig_username(link)
        if not username:
            bot.reply_to(message, "❌ Không lấy được username từ link!")
            return

        proc_msg = bot.reply_to(message, f"⏳ Đang lấy thông tin @{username}...")

        # Luôn mặc định live khi thêm - tránh die ảo lúc thêm mới
        status = 'live'

        info, _ = grig_get_ig_info(link)
        name = info['name'] if info else username

        avatar_path = None
        try:
            temp_avt = grig_get_ig_avatar(username)
            if temp_avt and os.path.exists(temp_avt):
                avatar_path = os.path.join(GRIG_AVATAR_CACHE, f"ig_{username}.jpg")
                if os.path.exists(avatar_path):
                    os.remove(avatar_path)
                os.rename(temp_avt, avatar_path)
        except:
            pass

        grig_dm.add_account(user_id=user_id, uid=username, name=name, link=link,
                             note=note, status=status, platform='instagram', avatar_path=avatar_path)

        try:
            bot.delete_message(proc_msg.chat.id, proc_msg.message_id)
        except:
            pass

        status_text = "ĐANG HOẠT ĐỘNG ✅" if status == 'live' else "ĐÃ DIE ❌"
        status_icon = "🟢" if status == 'live' else "🔴"
        name_esc = grig_esc(name)
        uid_esc = grig_esc(username)
        note_esc = grig_esc(note)
        link_esc = f"https://instagram\\.com/{uid_esc}"
        time_esc = grig_esc(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))

        caption = (
            f"📷 *Platform:* INSTAGRAM\n"
            f"👤 *Tên:* {name_esc}\n"
            f"🔎 *Username:* `{uid_esc}` \\- [Link]({link_esc})\n"
            f"🟢 *Trạng thái:* {grig_esc(status_text)}\n"
            f"📝 *Ghi chú:* {note_esc}\n"
            f"📅 *Thêm lúc:* {time_esc}\n"
            f"📊 *Tiến Trình:* Đang Theo Dõi♻️\n"
            f"👤 *Hạn Trả Kèo:* Vĩnh Viễn\n"
        )
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.row(
            types.InlineKeyboardButton("✅ Done kèo", callback_data=f"grig_done_{username}"),
            types.InlineKeyboardButton("❌ Hủy kèo", callback_data=f"grig_cancel_{username}")
        )
        keyboard.row(
            types.InlineKeyboardButton("📋 Danh sách", callback_data="grig_list"),
            types.InlineKeyboardButton("🚫 Hủy theo dõi", callback_data=f"grig_unfollow_{username}")
        )

        if avatar_path and os.path.exists(avatar_path):
            with open(avatar_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=caption, parse_mode='MarkdownV2', reply_markup=keyboard)
        else:
            bot.send_message(message.chat.id, caption, parse_mode='MarkdownV2', reply_markup=keyboard)

        grig_start_check(user_id)

    except Exception as e:
        bot.reply_to(message, f"❌ Lỗi: {e}")

# ---- /addfb - THÊM UID FACEBOOK NHANH (1 DÒNG LỆNH) ----
@bot.message_handler(commands=['addfb'])
def cmd_addfb(message):
    if not require_feature_access_message(message, "them_uid_fb", FEATURE_LABELS["them_uid_fb"]):
        return
    user_id = message.from_user.id
    chat_id = message.chat.id
    try:
        content = message.text.strip()
        # Bỏ lệnh prefix (/addfb hoặc /addfb@botname)
        content = re.sub(r'^/addfb(?:@\S+)?\s*', '', content).strip()

        if not content:
            bot.reply_to(message,
                "❌ Cú pháp: /addfb <uid hoặc link>|<ghi chú>|<giá>\n\n"
                "Ví dụ:\n"
                "/addfb 100012345678|Check kèo A|500000\n"
                "/addfb facebook.com/user123|Check kèo B|1000000")
            return

        parts = [p.strip() for p in content.split('|')]
        raw_uid = parts[0]
        note    = parts[1] if len(parts) > 1 else "Không có ghi chú"
        price_str = parts[2] if len(parts) > 2 else "0"

        # Parse giá
        try:
            price = int(price_str.replace(".", "").replace(",", ""))
        except:
            bot.reply_to(message, "❌ Giá phải là số nguyên. Ví dụ: 500000")
            return

        # Xác định UID
        proc_msg = bot.reply_to(message, "⏳ Đang lấy thông tin UID...")
        uid = None
        name_from_link = None
        if raw_uid.isdigit():
            uid = raw_uid
        else:
            uid, name_from_link = get_uid_from_link(raw_uid)
        if not uid:
            try: bot.edit_message_text("❌ Không lấy được UID từ link!", proc_msg.chat.id, proc_msg.message_id)
            except: pass
            return

        # Lấy profile
        profile = {}
        try:
            profile = fb_extractor.get_profile(uid, fallback_name=name_from_link) or {}
        except:
            pass

        name = profile.get("name") or name_from_link or f"UID {uid}"
        avatar_url = profile.get("avatar", "")
        is_verified = profile.get("verified", False)

        # Tải avatar bytes
        avatar_bytes = None
        try:
            avatar_bytes = get_facebook_avatar_bytes(uid)
        except:
            pass

        # Xóa proc_msg
        try: bot.delete_message(proc_msg.chat.id, proc_msg.message_id)
        except: pass

        # Check live/die
        proc2 = bot.send_message(chat_id, "⏳ Đang kiểm tra trạng thái UID...")
        initial_status = check_uid_live_die(uid)
        try: bot.delete_message(chat_id, proc2.message_id)
        except: pass

        # Lưu tracking
        save_tracking_uid(
            chat_id, uid, name, note, price,
            track_type="normal",
            is_verified=is_verified,
            initial_status=initial_status,
            avatar=avatar_url
        )
        update_user_stats(user_id, "add")

        # Tạo nội dung message
        thoi_gian = datetime.now()
        ten_esc   = escape_markdown_v2(name)
        uid_esc   = escape_markdown_v2(uid)
        note_esc  = escape_markdown_v2(note)
        gia_esc   = escape_markdown_v2(f"{price:,} VNĐ")
        tg_esc    = escape_markdown_v2(thoi_gian.strftime('%d/%m/%Y %H:%M:%S'))
        link_esc  = f"https://facebook\\.com/{uid_esc}"

        if initial_status == "LIVE":
            icon2, chu_tt, tien_trinh = "🟢", "ĐANG HOẠT ĐỘNG", "Đang theo dõi chờ DIE ❌"
        else:
            icon2, chu_tt, tien_trinh = "🔴", "ĐÃ BỊ KHÓA❌", "Đang theo dõi chờ LIVE ✅"

        verified_str = escape_markdown_v2(" ☑️" if is_verified else "")
        ket_qua = (
            f"📘 FACEBOOK PROFILE\n"
            f"👤 *Tên:* ||{ten_esc}||{verified_str}\n"
            f"🔎 *UID:* ||{uid_esc}|| \\- [Link]({link_esc})\n"
            f"{icon2} *Trạng thái:* {chu_tt}\n"
            f"📝 *Ghi chú:* {note_esc}\n"
            f"💵 *Giá:* ||{gia_esc}||\n"
            f"⏰ *Thời gian xử lý:* Vừa xong\n"
            f"📅 *Thời gian tạo:* {tg_esc}\n"
            f"📊 *Tiến trình:* {tien_trinh}\n"
            f"👤 *Hạn trả kèo:* Vĩnh viễn"
        )
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.row(
            types.InlineKeyboardButton("🔔 Cập nhật", callback_data=f"update_{uid}"),
            types.InlineKeyboardButton("📋 Danh Sách UID", callback_data="list_uid")
        )
        keyboard.row(
            types.InlineKeyboardButton("❌ Hủy kèo", callback_data=f"cancel_{uid}"),
            types.InlineKeyboardButton("✅ Done kèo", callback_data=f"done_{uid}")
        )

        # Gửi kết quả
        if initial_status == "DIE":
            _die_photo = LOCAL_ANH1 if os.path.exists(LOCAL_ANH1) else LOCAL_ANH3
            try:
                with open(_die_photo, "rb") as f:
                    bot.send_photo(chat_id, f, caption=ket_qua, parse_mode='MarkdownV2', reply_markup=keyboard, has_spoiler=True)
            except:
                bot.send_message(chat_id, ket_qua, parse_mode='MarkdownV2', reply_markup=keyboard)
        else:
            if avatar_bytes:
                try:
                    from io import BytesIO as _BIO
                    bot.send_photo(chat_id, _BIO(avatar_bytes), caption=ket_qua, parse_mode='MarkdownV2', reply_markup=keyboard, has_spoiler=True)
                except:
                    bot.send_message(chat_id, ket_qua, parse_mode='MarkdownV2', reply_markup=keyboard)
            elif avatar_url:
                try:
                    bot.send_photo(chat_id, avatar_url, caption=ket_qua, parse_mode='MarkdownV2', reply_markup=keyboard, has_spoiler=True)
                except:
                    bot.send_message(chat_id, ket_qua, parse_mode='MarkdownV2', reply_markup=keyboard)
            else:
                bot.send_message(chat_id, ket_qua, parse_mode='MarkdownV2', reply_markup=keyboard)

    except Exception as e:
        bot.reply_to(message, f"❌ Lỗi: {e}")

# ---- /addpgr - THÊM FACEBOOK GROUP ----
@bot.message_handler(commands=['addpgr'])
def grig_cmd_addpgr(message):
    if not require_feature_access_message(message, "them_group_fb", FEATURE_LABELS["them_group_fb"]):
        return
    user_id = message.from_user.id
    try:
        content = message.text.replace('/addpgr', '').strip()
        if not content:
            bot.reply_to(message, "❌ Cú pháp: /addpgr <link> | <ghi chú>\n\nVí dụ:\n/addpgr https://facebook.com/groups/123456 | Group ABC")
            return

        parts = [p.strip() for p in content.split('|')]
        link = parts[0]
        note = parts[1] if len(parts) > 1 else "Không có ghi chú"

        platform = grig_detect_platform(link)
        if platform != 'facebook_group':
            bot.reply_to(message, "❌ Lệnh /addpgr chỉ dùng cho Facebook Group!\n\n💡 Dùng /add cho Instagram")
            return

        proc_msg = bot.reply_to(message, "⏳ Đang lấy thông tin Group...")

        group_id, group_name, _ = grig_get_group_id_name(link)
        if not group_id:
            try:
                bot.edit_message_text("❌ Không lấy được Group ID! (Group có thể bị xóa hoặc riêng tư)", proc_msg.chat.id, proc_msg.message_id)
            except:
                pass
            return

        avatar_path = None
        try:
            bot.edit_message_text(f"⏳ Đang lấy avatar Group {group_id}...", proc_msg.chat.id, proc_msg.message_id)
            temp_avt = grig_get_gr_avatar(group_id)
            if temp_avt and os.path.exists(temp_avt):
                avatar_path = os.path.join(GRIG_AVATAR_CACHE, f"group_{group_id}.jpg")
                if os.path.exists(avatar_path):
                    os.remove(avatar_path)
                os.rename(temp_avt, avatar_path)
        except:
            pass

        grig_dm.add_account(user_id=user_id, uid=group_id, name=group_name, link=link,
                             note=note, status='live', platform='facebook_group', avatar_path=avatar_path)

        try:
            bot.delete_message(proc_msg.chat.id, proc_msg.message_id)
        except:
            pass

        name_esc = grig_esc(group_name)
        id_esc = grig_esc(group_id)
        note_esc = grig_esc(note)
        link_esc = f"https://facebook\\.com/groups/{id_esc}"
        time_esc = grig_esc(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))

        caption = (
            f"📘 *Platform:* FACEBOOK GROUP\n"
            f"👤 *Tên:* {name_esc}\n"
            f"🔎 *UID:* `{id_esc}` \\- [Link]({link_esc})\n"
            f"🟢 *Trạng thái:* ĐANG HOẠT ĐỘNG\n"
            f"📝 *Ghi chú:* {note_esc}\n"
            f"📅 *Thêm lúc:* {time_esc}\n"
            f"📊 *Tiến Trình:* Đang Theo Dõi♻️\n"
            f"👤 *Hạn Trả Kèo:* Vĩnh Viễn\n"
        )
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.row(
            types.InlineKeyboardButton("✅ Done kèo", callback_data=f"grig_done_{group_id}"),
            types.InlineKeyboardButton("❌ Hủy kèo", callback_data=f"grig_cancel_{group_id}")
        )
        keyboard.row(
            types.InlineKeyboardButton("📋 Danh sách", callback_data="grig_list"),
            types.InlineKeyboardButton("🚫 Hủy theo dõi", callback_data=f"grig_unfollow_{group_id}")
        )

        if avatar_path and os.path.exists(avatar_path):
            with open(avatar_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=caption, parse_mode='MarkdownV2', reply_markup=keyboard)
        else:
            bot.send_message(message.chat.id, caption, parse_mode='MarkdownV2', reply_markup=keyboard)

        grig_start_check(user_id)

    except Exception as e:
        bot.reply_to(message, f"❌ Lỗi: {e}")

# ---- /view /tablive /tabdie - XEM DANH SÁCH ----
def grig_show_accounts(message, filter_status=None):
    user_id = message.from_user.id
    if filter_status == 'live':
        accounts = grig_dm.get_live(user_id)
        title = "✅ DANH SÁCH LIVE"
    elif filter_status == 'die':
        accounts = grig_dm.get_die(user_id)
        title = "❌ DANH SÁCH DIE"
    else:
        accounts = grig_dm.get_accounts(user_id)
        title = "📋 TẤT CẢ"

    if not accounts:
        bot.reply_to(message, f"⚠️ Không có dữ liệu!\n\nDùng /add để thêm Instagram\nDùng /addpgr để thêm FB Group")
        return

    live_c = sum(1 for d in accounts.values() if d['status'] == 'live')
    die_c = len(accounts) - live_c
    text = f"{title} ({len(accounts)} tài khoản)\n━━━━━━━━━━━━━━\n"
    for i, (uid, d) in enumerate(list(accounts.items())[:30], 1):
        icon = "✅" if d['status'] == 'live' else "❌"
        plt_icon = '📷' if d.get('platform') == 'instagram' else '👥'
        text += f"{i}. {icon}{plt_icon} {uid} – {d.get('note', '')}\n"
    if len(accounts) > 30:
        text += f"... và {len(accounts)-30} tài khoản khác\n"
    text += f"\n━━━━━━━━━━━━━━\n✅ LIVE: {live_c}  ❌ DIE: {die_c}"
    bot.reply_to(message, text)

@bot.message_handler(commands=['view'])
def grig_cmd_view(message):
    grig_show_accounts(message)

@bot.message_handler(commands=['tablive'])
def grig_cmd_tablive(message):
    grig_show_accounts(message, filter_status='live')

@bot.message_handler(commands=['tabdie'])
def grig_cmd_tabdie(message):
    grig_show_accounts(message, filter_status='die')

# ---- /delete - XÓA TÀI KHOẢN ----
@bot.message_handler(commands=['delete'])
def grig_cmd_delete(message):
    parts = message.text.split()
    if len(parts) < 2:
        bot.reply_to(message, "❌ Cú pháp: /delete <uid/username/group_id>")
        return
    uid = parts[1].strip()
    if grig_dm.remove_account(message.from_user.id, uid):
        grig_reset_die(message.from_user.id, uid)
        bot.reply_to(message, f"✅ Đã xóa: {uid}")
    else:
        bot.reply_to(message, f"⚠️ Không tìm thấy: {uid}")

# ---- CALLBACKS CHO GRIG ----
@bot.callback_query_handler(func=lambda call: (
    call.data.startswith('grig_done_') or
    call.data.startswith('grig_cancel_') or
    call.data.startswith('grig_unfollow_') or
    call.data == 'grig_list'
))
def grig_handle_callbacks(call):
    try:
        if call.data.startswith('grig_done_'):
            uid = call.data.replace('grig_done_', '')
            bot.answer_callback_query(call.id, "✅ Đã Done kèo!")
            try:
                new_cap = (call.message.caption or call.message.text or '') + "\n\n✅ DONE KÈO!"
                if call.message.caption:
                    bot.edit_message_caption(new_cap, call.message.chat.id, call.message.message_id, reply_markup=None)
                else:
                    bot.edit_message_text(new_cap, call.message.chat.id, call.message.message_id, reply_markup=None)
            except:
                try:
                    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
                except:
                    pass

        elif call.data.startswith('grig_unfollow_'):
            uid = call.data.replace('grig_unfollow_', '')
            if grig_dm.remove_account(call.from_user.id, uid):
                grig_reset_die(call.from_user.id, uid)
                bot.answer_callback_query(call.id, "🚫 Đã hủy theo dõi!")
                try:
                    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
                except:
                    pass
            else:
                bot.answer_callback_query(call.id, "⚠️ Không tìm thấy tài khoản!", show_alert=True)

        elif call.data.startswith('grig_cancel_'):
            uid = call.data.replace('grig_cancel_', '')
            bot.answer_callback_query(call.id, "❌ Đã hủy kèo!")
            try:
                new_cap = (call.message.caption or call.message.text or '') + "\n\n❌ HỦY KÈO!"
                if call.message.caption:
                    bot.edit_message_caption(new_cap, call.message.chat.id, call.message.message_id, reply_markup=None)
                else:
                    bot.edit_message_text(new_cap, call.message.chat.id, call.message.message_id, reply_markup=None)
            except:
                try:
                    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
                except:
                    pass

        elif call.data == 'grig_list':
            user_id = call.from_user.id
            accounts = grig_dm.get_accounts(user_id)
            if not accounts:
                bot.answer_callback_query(call.id, "⚠️ Chưa có tài khoản nào!", show_alert=True)
                return
            text = "📋 DANH SÁCH THEO DÕI (Group/IG)\n\n"
            for i, (uid, d) in enumerate(list(accounts.items())[:20], 1):
                icon = "✅" if d['status'] == 'live' else "❌"
                plt = '📷' if d.get('platform') == 'instagram' else '👥'
                text += f"{i}. {icon}{plt} {uid} – {d.get('note','')}\n"
            if len(accounts) > 20:
                text += f"\n... và {len(accounts)-20} tài khoản khác"
            bot.answer_callback_query(call.id)
            bot.send_message(call.message.chat.id, text)

    except Exception as e:
        try:
            bot.answer_callback_query(call.id, f"❌ Lỗi: {e}", show_alert=True)
        except:
            pass

# ---- XỬ LÝ NÚT BÀN PHÍM CHO GROUP/IG ----
def grig_handle_keyboard_button(message):
    """Xử lý nút bàn phím 👥 Thêm Group FB, 📸 Thêm Instagram, 📋 Danh Sách Group & Ins"""
    text = message.text
    chat_id = message.chat.id

    if text == "👥 Thêm Group FB":
        bot.send_message(chat_id,
            "👥 *THÊM FACEBOOK GROUP THEO DÕI*\n\n"
            "Sử dụng lệnh:\n"
            "`/addpgr <link> | <ghi chú>`\n\n"
            "Ví dụ:\n"
            "`/addpgr https://facebook.com/groups/123456 | Nhóm ABC`\n\n"
            "Hoặc chỉ gửi link:\n"
            "`/addpgr https://facebook.com/groups/123456`",
            parse_mode='Markdown')
        return True

    elif text == "📷 Thêm Instagram":
        bot.send_message(chat_id,
            "📷 *THÊM INSTAGRAM THEO DÕI*\n\n"
            "Sử dụng lệnh:\n"
            "`/add <link> | <ghi chú>`\n\n"
            "Ví dụ:\n"
            "`/add https://instagram.com/username | Check kèo`\n\n"
            "Hoặc chỉ gửi link:\n"
            "`/add https://instagram.com/username`",
            parse_mode='Markdown')
        return True

    elif text == "📋 Danh Sách Group & Ins":
        show_unified_list(chat_id, message.from_user.id)
        return True

    return False



# ============================================================
# ===== MODULE: THEO DÕI FB POST LIVE/DIE (tích hợp từ livediepost.py) =====
# ============================================================

try:
    from playwright.async_api import async_playwright as _async_playwright
    _PLAYWRIGHT_OK = True
except ImportError:
    _PLAYWRIGHT_OK = False

FB_POST_AVT_API = "https://keyherlyswar.x10.mx/Apidocs/tien_ich/avtfb.php?uid={uid}"
FB_POST_DEFAULT_INTERVAL = 60

fb_post_watching = {}   # bot mẹ: {url: {interval, added_at, chat_id, label, status, task}}
fb_post_loop = None
fb_post_thread = None
fb_post_url_cache = {}  # bot mẹ: {short_key: url}

# Per-subbot dicts: {token: {url: ...}}
_subbot_fp_watching = {}   # {subbot_token: {url: {...}}}
_subbot_fp_url_cache = {}  # {subbot_token: {short_key: url}}

def _get_fp_watching():
    """Trả về fb_post_watching đúng theo context (bot mẹ hoặc bot con)."""
    ctx = getattr(_subbot_tl, 'ctx', None)
    if ctx:
        token = ctx.get('token')
        if token:
            if token not in _subbot_fp_watching:
                _subbot_fp_watching[token] = {}
            return _subbot_fp_watching[token]
    return fb_post_watching

def _get_fp_url_cache():
    """Trả về fb_post_url_cache đúng theo context."""
    ctx = getattr(_subbot_tl, 'ctx', None)
    if ctx:
        token = ctx.get('token')
        if token:
            if token not in _subbot_fp_url_cache:
                _subbot_fp_url_cache[token] = {}
            return _subbot_fp_url_cache[token]
    return fb_post_url_cache


def fbpost_get_cookie():
    """Lấy cookie FB từ file cookie.txt hoặc FB_COOKIE global"""
    try:
        with open("cookie.txt", "r", encoding="utf-8") as f:
            c = f.read().strip()
            if c:
                return c
    except Exception:
        pass
    return FB_COOKIE


def fbpost_parse_cookies(cookie_str):
    cookies = []
    for part in cookie_str.split(";"):
        part = part.strip()
        if "=" in part:
            name, value = part.split("=", 1)
            cookies.append({"name": name.strip(), "value": value.strip(), "domain": ".facebook.com", "path": "/"})
    return cookies


def fbpost_decode_unicode(s):
    try:
        return s.encode('utf-8').decode('unicode_escape').encode('latin1').decode('utf-8')
    except Exception:
        try:
            return s.encode().decode('unicode_escape')
        except Exception:
            return s


async def fbpost_get_info(html, author_uid_cookie):
    info = {"author_name": "", "author_uid": "", "author_avatar": "", "post_image": "", "likes": "0", "comments": "0", "post_text": ""}
    try:
        for m in re.finditer(r'"actor":\{"__typename":"(?:User|Page)","id":"(\d+)","name":"([^"]+)"', html):
            uid = m.group(1)
            name = fbpost_decode_unicode(m.group(2))
            if uid != author_uid_cookie:
                info["author_uid"] = uid
                info["author_name"] = name
                break
        if not info["author_name"]:
            for pattern in [r'"ownerName":"([^"]+)"', r'"node":\{"__typename":"(?:User|Page)","id":"(\d+)?","name":"([^"]+)"']:
                m = re.search(pattern, html)
                if m:
                    groups = m.groups()
                    name = fbpost_decode_unicode(groups[-1])
                    if name and name != "Facebook":
                        info["author_name"] = name
                        if len(groups) > 1 and groups[0] and groups[0] != author_uid_cookie:
                            info["author_uid"] = groups[0]
                    break
        if info["author_uid"]:
            info["author_avatar"] = FB_POST_AVT_API.format(uid=info["author_uid"])
        m = re.search(r'"reaction_count":\{"count":(\d+)\}', html)
        if m:
            info["likes"] = f"{int(m.group(1)):,}"
        m = re.search(r'"comment_count":\{"total_count":(\d+)\}', html)
        if m:
            info["comments"] = f"{int(m.group(1)):,}"
        m = re.search(r'"message":\{"text":"([^"]{1,500}?)"\}', html)
        if m:
            info["post_text"] = fbpost_decode_unicode(m.group(1))[:300]
        for pat in [
            r'"full_picture":"([^"]+fbcdn[^"]+)"',
            r'"uri":"(https://[^"]+fbcdn\.net/v/[^"]+)"',
            r'"image":\{"height":\d+,"uri":"([^"]+fbcdn[^"]+)","width":\d+\}',
        ]:
            m = re.search(pat, html)
            if m:
                img = m.group(1).replace("\\u0026", "&").replace("\\/", "/")
                if "profile" not in img and "/p/" not in img:
                    info["post_image"] = img
                    break
    except Exception:
        pass
    return info


async def fbpost_check_playwright(post_url):
    if not _PLAYWRIGHT_OK:
        return {"url": post_url, "status": "ERROR", "reason": "Playwright chưa được cài. Chạy: playwright install chromium", "info": {}}
    url = post_url.strip()
    if not url.startswith("http"):
        url = "https://" + url
    die_signals = [
        "nội dung không có sẵn", "content not available", "this content isn't available",
        "sorry, this content isn't available", "the link you followed may be broken",
        "đường liên kết bạn theo dõi có thể bị hỏng", "this page isn't available",
        "trang này không khả dụng", "page not found", "trang không tìm thấy",
        "bạn hiện không xem được nội dung này", "you can't see this content",
        "nội dung này không có sẵn", "bài viết này không còn",
    ]
    cookie_str = fbpost_get_cookie()
    cookie_uid = ""
    m = re.search(r'c_user=(\d+)', cookie_str)
    if m:
        cookie_uid = m.group(1)
    try:
        async with _async_playwright() as p:
            browser = await p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-setuid-sandbox", "--disable-blink-features=AutomationControlled"])
            context = await browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                viewport={"width": 1280, "height": 800}, locale="vi-VN",
            )
            if cookie_str:
                await context.add_cookies(fbpost_parse_cookies(cookie_str))
            page = await context.new_page()
            await page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")
            try:
                await page.goto(url, wait_until="domcontentloaded", timeout=25000)
                await page.wait_for_timeout(4000)
                if "facebook.com/login" in page.url:
                    await browser.close()
                    return {"url": post_url, "status": "UNKNOWN", "reason": "⚠️ Cookie hết hạn hoặc chưa nạp!", "info": {}}
                content_html = await page.content()
                page_text = await page.evaluate("() => document.body.innerText")
                text_lower = page_text.lower()
                html_lower = content_html.lower()
                for signal in die_signals:
                    if signal in text_lower or signal in html_lower:
                        await browser.close()
                        return {"url": post_url, "status": "DIE", "reason": f"Phát hiện: '{signal}'", "info": {}}
                live_signals = ["feedback_id", "top_level_post_id", "story_fbid", "tl_objid", '"__typename":"story"']
                is_live = any(s in html_lower for s in live_signals)
                if is_live:
                    info = await fbpost_get_info(content_html, cookie_uid)
                    await browser.close()
                    return {"url": post_url, "status": "LIVE", "reason": "Post vẫn còn tồn tại", "info": info}
                await browser.close()
                return {"url": post_url, "status": "UNKNOWN", "reason": "Không xác định được trạng thái", "info": {}}
            except Exception as e:
                await browser.close()
                return {"url": post_url, "status": "ERROR", "reason": str(e), "info": {}}
    except Exception as e:
        return {"url": post_url, "status": "ERROR", "reason": str(e), "info": {}}


def fbpost_build_caption(url, result, is_die=False, label=""):
    info = result.get("info", {})
    now = datetime.now().strftime("%H:%M:%S %d/%m/%Y")
    header = "🔴 *POST ĐÃ DIE!*" if is_die else "🟢 *POST ĐANG LIVE*"
    lines = [header, ""]
    if label:
        lines.append(f"🏷 Kèo: *{label}*")
    lines.append(f"🔗 [Link bài post]({url})")
    if info.get("author_name"):
        lines.append(f"👤 Tác giả: *{info['author_name']}*")
    lines.append(f"👍 Like: *{info.get('likes', '0')}*")
    lines.append(f"💬 Comment: *{info.get('comments', '0')}*")
    if info.get("post_text"):
        lines.append(f"📝 _{info['post_text'][:200]}_")
    lines.append(f"\n🕐 {now}")
    if is_die:
        lines.append(f"📋 Lý do: {result.get('reason', '')}")
    return "\n".join(lines)


def fbpost_send_notify(chat_id, url, result, is_die=False, label="", token=None):
    """Gửi thông báo post. token=None → bot mẹ, token=str → bot con."""
    caption = fbpost_build_caption(url, result, is_die=is_die, label=label)
    info = result.get("info", {})
    post_image = info.get("post_image", "")
    avatar = info.get("author_avatar", "")
    uid_key = url.replace("|", "_")[:50]

    markup = None
    if not is_die:
        markup = types.InlineKeyboardMarkup(row_width=3)
        markup.add(
            types.InlineKeyboardButton("✅ Done kèo", callback_data=f"fbpost_done_{uid_key}"),
            types.InlineKeyboardButton("❌ Hủy kèo", callback_data=f"fbpost_cancel_{uid_key}"),
            types.InlineKeyboardButton("🗑 Xóa URL", callback_data=f"fbpost_del_{uid_key}"),
        )
    else:
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(
            types.InlineKeyboardButton("✅ Done kèo", callback_data=f"fbpost_done_{uid_key}"),
            types.InlineKeyboardButton("❌ Hủy kèo", callback_data=f"fbpost_cancel_{uid_key}"),
        )

    if token:
        # Bot con: gửi trực tiếp qua API, không qua wrapper
        rm_json = markup.to_json() if markup else None
        try:
            sent = False
            if post_image or avatar:
                img = post_image or avatar
                payload = {"chat_id": chat_id, "caption": caption, "parse_mode": "Markdown"}
                if rm_json: payload["reply_markup"] = rm_json
                try:
                    r = requests.post(f"https://api.telegram.org/bot{token}/sendPhoto",
                                      json={**payload, "photo": img}, timeout=20)
                    if r.json().get("ok"):
                        sent = True
                except Exception:
                    pass
            if not sent:
                payload = {"chat_id": chat_id, "text": caption, "parse_mode": "Markdown"}
                if rm_json: payload["reply_markup"] = rm_json
                r = requests.post(f"https://api.telegram.org/bot{token}/sendMessage",
                                  json=payload, timeout=20)
                if not r.json().get("ok"):
                    # Markdown lỗi → thử plain text
                    payload.pop("parse_mode", None)
                    requests.post(f"https://api.telegram.org/bot{token}/sendMessage",
                                  json=payload, timeout=20)
        except Exception as e:
            print(f"[BotCon] fbpost_send_notify subbot lỗi: {e}")
        return

    # Bot mẹ: dùng original methods (tránh wrapper proxy)
    _sm = _botcon_orig.get('send_message') or bot.send_message
    _sp = _botcon_orig.get('send_photo') or bot.send_photo
    try:
        if post_image:
            _sp(chat_id, post_image, caption=caption, parse_mode="Markdown", reply_markup=markup)
        elif avatar:
            _sp(chat_id, avatar, caption=caption, parse_mode="Markdown", reply_markup=markup)
        else:
            _sm(chat_id, caption, parse_mode="Markdown", reply_markup=markup)
    except Exception:
        try:
            _sm(chat_id, caption, parse_mode="Markdown", reply_markup=markup)
        except Exception:
            pass


async def fbpost_monitor_loop(url, interval, chat_id, label="", token=None):
    """
    token=None → bot mẹ (dùng _botcon_orig).
    token=str  → bot con (gửi trực tiếp qua Telegram API).
    """
    unknown_count = 0
    MAX_UNKNOWN = 3
    first_check = True

    # Chọn dict đúng — dùng closure trên token (không check ctx vì async thread)
    def _watching():
        if token:
            # Luôn trả về dict của bot con này, tạo nếu chưa có
            if token not in _subbot_fp_watching:
                _subbot_fp_watching[token] = {}
            return _subbot_fp_watching[token]
        return fb_post_watching

    def _send_msg(text):
        if token:
            try:
                requests.post(
                    f"https://api.telegram.org/bot{token}/sendMessage",
                    json={"chat_id": chat_id, "text": text, "parse_mode": "Markdown"},
                    timeout=FAST_API_TIMEOUT
                )
            except Exception as e:
                print(f"[BotCon] fbpost _send_msg lỗi: {e}")
        else:
            try:
                _sm = _botcon_orig.get('send_message') or bot.send_message
                _sm(chat_id, text, parse_mode="Markdown")
            except Exception:
                pass

    while True:
        try:
            w = _watching()
            if url not in w:
                return
            result = await fbpost_check_playwright(url)
            status = result["status"]
            now = datetime.now().strftime("%H:%M:%S %d/%m/%Y")
            w = _watching()
            if url in w:
                w[url]["last_status"] = status
                w[url]["last_check"] = now

            if first_check:
                first_check = False
                print(f"[FBPost] first_check url={url[:40]} status={status} token={'BOT_CON' if token else 'BOT_ME'} chat_id={chat_id}")
                if status == "LIVE":
                    fbpost_send_notify(chat_id, url, result, is_die=False, label=label, token=token)
                elif status == "DIE":
                    fbpost_send_notify(chat_id, url, result, is_die=True, label=label, token=token)
                    w = _watching()
                    if url in w: del w[url]
                    return
                elif status == "UNKNOWN":
                    lbl_text = f"\n🏷 Kèo: *{label}*" if label else ""
                    _send_msg(f"⚠️ *Không xác định được trạng thái*{lbl_text}\n🔗 {url}\n📋 {result.get('reason','')}\n🕐 {now}\n\n🔄 Tiếp tục theo dõi...")
                elif status == "ERROR":
                    lbl_text = f"\n🏷 Kèo: *{label}*" if label else ""
                    _send_msg(f"❌ *Lỗi khi check*{lbl_text}\n🔗 {url}\n📋 {result.get('reason','')}\n🕐 {now}\n\n🔄 Tiếp tục theo dõi...")
            else:
                if status == "DIE":
                    fbpost_send_notify(chat_id, url, result, is_die=True, label=label, token=token)
                    w = _watching()
                    if url in w: del w[url]
                    return
                elif status == "UNKNOWN":
                    unknown_count += 1
                    if unknown_count >= MAX_UNKNOWN:
                        lbl_text = f"\n🏷 Kèo: *{label}*" if label else ""
                        _send_msg(f"⚠️ *POST CÓ THỂ ĐÃ DIE!*{lbl_text}\n\n🔗 {url}\n📋 Không xác định {MAX_UNKNOWN} lần liên tiếp\n🕐 {now}")
                        w = _watching()
                        if url in w: del w[url]
                        return
                elif status in ("LIVE", "ERROR"):
                    unknown_count = 0

            await asyncio.sleep(interval)
        except asyncio.CancelledError:
            return
        except Exception:
            await asyncio.sleep(interval)


def fbpost_ensure_loop():
    global fb_post_loop, fb_post_thread
    if fb_post_loop is not None and fb_post_loop.is_running():
        return
    def run_loop(loop):
        asyncio.set_event_loop(loop)
        loop.run_forever()
    fb_post_loop = asyncio.new_event_loop()
    fb_post_thread = threading.Thread(target=run_loop, args=(fb_post_loop,), daemon=True)
    fb_post_thread.start()


def fbpost_start_monitor(url, interval, chat_id, label=""):
    global fb_post_loop
    fbpost_ensure_loop()
    # Lấy token nếu đang trong context bot con
    ctx = getattr(_subbot_tl, 'ctx', None)
    token = ctx.get('token') if ctx else None

    entry = {
        "interval": interval,
        "added_at": datetime.now().strftime("%H:%M:%S %d/%m/%Y"),
        "chat_id": chat_id,
        "label": label,
        "last_status": "checking",
        "last_check": "",
        "task": None,  # sẽ gán sau
    }
    # Lưu vào đúng dict TRƯỚC khi start coroutine (tránh race condition)
    _get_fp_watching()[url] = entry

    task = asyncio.run_coroutine_threadsafe(
        fbpost_monitor_loop(url, interval, chat_id, label, token=token),
        fb_post_loop
    )
    entry["task"] = task


# ---- COMMANDS /addpost /listpost /removepost /statuspost ----

@bot.message_handler(commands=['addpost'])
def fbpost_cmd_add(message):
    if not require_feature_access_message(message, "them_post_fb", FEATURE_LABELS["them_post_fb"]):
        return
    args = message.text.split(maxsplit=3)
    if len(args) < 2:
        bot.reply_to(message, "❌ Dùng: /addpost <url> [giây] [nhãn kèo]")
        return
    url = args[1].strip()
    if not url.startswith("http"):
        url = "https://" + url
    interval = FB_POST_DEFAULT_INTERVAL
    label = ""
    if len(args) >= 3:
        if args[2].isdigit():
            interval = int(args[2])
            label = args[3].strip() if len(args) >= 4 else ""
        else:
            label = " ".join(args[2:]).strip()
    if url in _get_fp_watching():
        bot.reply_to(message, "⚠️ URL này đã được theo dõi rồi!")
        return
    try:
        fbpost_start_monitor(url, interval, message.chat.id, label)
        interval_text = f"{interval}s" if interval < 60 else f"{interval // 60} phút"
        lbl_text = f"\n🏷 Kèo: *{label}*" if label else ""
        bot.reply_to(message, f"✅ *Đã thêm theo dõi Post FB!*\n🔗 {url}{lbl_text}\n⏱ Check mỗi: {interval_text}\n🔔 Tự động báo khi DIE", parse_mode="Markdown")
    except Exception as e:
        bot.reply_to(message, f"❌ Lỗi khi thêm post: {str(e)}")


@bot.message_handler(commands=['listpost'])
def fbpost_cmd_list(message):
    if not _get_fp_watching():
        bot.reply_to(message, "📭 Chưa có Post FB nào đang theo dõi.\nDán link FB vào chat hoặc dùng /addpost")
        return
    markup = types.InlineKeyboardMarkup(row_width=1)
    lines = [f"📋 *Đang theo dõi {len(_get_fp_watching())} Post FB:*\n"]
    for i, (url, info) in enumerate(list(_get_fp_watching().items())[:20], 1):
        label = info.get("label", "")
        lbl_text = f" [{label}]" if label else ""
        lines.append(f"{i}. {url[:60]}{lbl_text}\n   ⏱ {info['interval']}s | 📊 {info.get('last_status','?')} | {info['added_at']}")
        uid_key = url.replace("|", "_")[:50]
        markup.add(types.InlineKeyboardButton(f"🗑 Xóa #{i}", callback_data=f"fbpost_del_{uid_key}"))
    markup.add(types.InlineKeyboardButton("🗑 Xóa TẤT CẢ", callback_data="fbpost_removeall"))
    bot.reply_to(message, "\n".join(lines), parse_mode="Markdown", reply_markup=markup)


@bot.message_handler(commands=['removepost'])
def fbpost_cmd_remove(message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        bot.reply_to(message, "❌ Dùng: /removepost <url>")
        return
    url = args[1].strip()
    if url in _get_fp_watching():
        try:
            _get_fp_watching()[url]["task"].cancel()
        except Exception:
            pass
        del _get_fp_watching()[url]
        bot.reply_to(message, "✅ Đã xóa!")
    else:
        bot.reply_to(message, "⚠️ Không tìm thấy URL này.")


@bot.message_handler(commands=['statuspost'])
def fbpost_cmd_status(message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        bot.reply_to(message, "❌ Dùng: /statuspost <url>")
        return
    url = args[1].strip()
    msg = bot.reply_to(message, "🔄 Đang check (~10 giây)...")
    fbpost_ensure_loop()
    future = asyncio.run_coroutine_threadsafe(fbpost_check_playwright(url), fb_post_loop)
    try:
        result = future.result(timeout=40)
        status = result["status"]
        label = _get_fp_watching().get(url, {}).get("label", "")
        try:
            bot.delete_message(message.chat.id, msg.message_id)
        except Exception:
            pass
        if status in ("LIVE", "DIE"):
            fbpost_send_notify(message.chat.id, url, result, is_die=(status == "DIE"), label=label)
        else:
            bot.send_message(message.chat.id,
                f"⚠️ *Kết quả:*\n\n🔗 {url}\n📊 Trạng thái: *{status}*\n📋 {result['reason']}",
                parse_mode="Markdown")
    except Exception as e:
        bot.edit_message_text(f"❌ Lỗi check: {e}", message.chat.id, msg.message_id)


# ---- Callback buttons FB Post ----
# (Được xử lý trong handle_callback chính bên dưới)

# ---- Auto detect link FB Post từ chat ----

# ========== MENU DANH SÁCH TỔNG HỢP ==========
def show_unified_list(chat_id, user_id, tab="overview", message_id=None):
    """Hiển thị danh sách gộp tất cả loại theo dõi"""
    import hashlib

    def _bar(live, total):
        die = total - live
        if total == 0: return "—"
        return f"✦{live}  ✧{die}"

    def make_overview():
        fb_data = get_tracking().get(str(chat_id), {})
        fb_active = {k: v for k, v in fb_data.items() if v.get('status') != 'done'}
        fb_live = sum(1 for v in fb_active.values() if v.get('last_check') == 'LIVE')

        tt_data = get_tracking_tiktok().get(str(chat_id), {})
        tt_active = {k: v for k, v in tt_data.items() if v.get('status') != 'done'}
        tt_live = sum(1 for v in tt_active.values() if v.get('last_check') in ['EXISTS','live'])

        grig_accounts = grig_dm.get_accounts(user_id)
        gr_active = {k: v for k, v in grig_accounts.items() if v.get('platform') == 'facebook_group'}
        gr_live = sum(1 for v in gr_active.values() if v.get('status') == 'live')
        ig_active = {k: v for k, v in grig_accounts.items() if v.get('platform') == 'instagram'}
        ig_live = sum(1 for v in ig_active.values() if v.get('status') == 'live')

        post_list = list(_get_fp_watching().items())
        post_live = sum(1 for _, i in post_list if i.get('last_status') == 'live')

        ytb_data = load_ytb_data().get(str(chat_id), {})
        ytb_live = sum(1 for ch in ytb_data.values() if ch.get('status') == 'live')

        total = len(fb_active)+len(tt_active)+len(gr_active)+len(ig_active)+len(post_list)+len(ytb_data)
        total_live = fb_live+gr_live+ig_live+tt_live+post_live+ytb_live

        msg  = "📊 *DANH SÁCH THEO DÕI TỔNG HỢP*\n"
        msg += "───────────────────\n"
        msg += f"👤 Profile FB: *{len(fb_active)}* mục\n"
        msg += f"👥 Group FB: *{len(gr_active)}* mục\n"
        msg += f"📷 Instagram: *{len(ig_active)}* mục\n"
        msg += f"🎵 TikTok: *{len(tt_active)}* mục\n"
        msg += f"📘 Post FB: *{len(post_list)}* mục\n"
        msg += f"🎞️ YouTube: *{len(ytb_data)}* kênh\n"
        msg += "───────────────────\n"
        msg += f"📦 Tổng cộng: *{total}* mục đang theo dõi"

        mk = types.InlineKeyboardMarkup(row_width=2)
        mk.add(
            types.InlineKeyboardButton(f"👤 Profile FB ({len(fb_active)})", callback_data="ulist_tab_fb"),
            types.InlineKeyboardButton(f"👥 Group FB ({len(gr_active)})",   callback_data="ulist_tab_gr"),
        )
        mk.add(
            types.InlineKeyboardButton(f"📷 Instagram ({len(ig_active)})",  callback_data="ulist_tab_ig"),
            types.InlineKeyboardButton(f"🎵 TikTok ({len(tt_active)})",     callback_data="ulist_tab_tt"),
        )
        mk.add(
            types.InlineKeyboardButton(f"📘 Post FB ({len(post_list)})",    callback_data="ulist_tab_post"),
            types.InlineKeyboardButton(f"🎞️ YouTube ({len(ytb_data)})",     callback_data="ulist_tab_ytb"),
        )
        if total > 0:
            mk.add(types.InlineKeyboardButton("🗑 XÓA TẤT CẢ MỌI THỨ", callback_data="ulist_del_all"))
        return msg, mk

    def make_tab_fb():
        fb_data = get_tracking().get(str(chat_id), {})
        active = {k: v for k, v in fb_data.items() if v.get('status') != 'done'}
        if not active:
            msg = "👤 *Profile FB*\n\n_Chưa có UID nào đang theo dõi._"
        else:
            live_c = sum(1 for v in active.values() if v.get('last_check') == 'LIVE')
            msg  = f"👤 *PROFILE FB — {len(active)} UID*\n"
            msg += f"🟢 Live: {live_c}  │  🔴 Die: {len(active)-live_c}\n"
            msg += "━━━━━━━━━━━━━━━━━━━━\n"
            for i, (k, v) in enumerate(list(active.items())[:20], 1):
                if v.get("track_type") == "meta": si = "💎"
                else: si = "🟢" if v.get('last_check') == 'LIVE' else "🔴"
                verified = " ☑️" if v.get("is_verified") else ""
                sn = str(v.get('name', k))[:20].replace("_", r"\_").replace("*", r"\*")
                msg += f"{i}. {si} *{sn}*{verified}\n   🆔 `{k}`\n"
        mk = types.InlineKeyboardMarkup(row_width=1)
        for k, v in list(active.items())[:20]:
            si = "🟢" if v.get('last_check') == 'LIVE' else "🔴"
            sn = str(v.get('name', k))[:20]
            mk.add(types.InlineKeyboardButton(f"{si} 🗑 {sn}", callback_data=f"ulist_del_fb_{k}"))
        if active:
            mk.add(types.InlineKeyboardButton("🗑 Xóa tất cả Profile FB", callback_data="ulist_delall_fb"))
        mk.add(types.InlineKeyboardButton("« Quay lại tổng hợp", callback_data="ulist_tab_overview"))
        return msg, mk

    def make_tab_gr():
        grig_accounts = grig_dm.get_accounts(user_id)
        active = {k: v for k, v in grig_accounts.items() if v.get('platform') == 'facebook_group'}
        if not active:
            msg = "👥 *Group FB*\n\n_Chưa có Group nào đang theo dõi._"
        else:
            live_c = sum(1 for v in active.values() if v.get('status') == 'live')
            msg  = f"👥 *GROUP FB — {len(active)} group*\n"
            msg += f"🟢 Live: {live_c}  │  🔴 Die: {len(active)-live_c}\n"
            msg += "━━━━━━━━━━━━━━━━━━━━\n"
            for i, (uid, d) in enumerate(list(active.items())[:20], 1):
                si = "🟢" if d['status'] == 'live' else "🔴"
                nm = d.get('name', uid)[:20].replace("_", r"\_").replace("*", r"\*")
                nt = d.get('note', '')[:15]
                msg += f"{i}. {si} *{nm}*\n   🆔 `{uid}`\n"
                if nt: msg += f"   📝 {nt}\n"
        mk = types.InlineKeyboardMarkup(row_width=1)
        for uid, d in list(active.items())[:20]:
            si = "🟢" if d['status'] == 'live' else "🔴"
            nm = d.get('name', uid)[:20]
            mk.add(types.InlineKeyboardButton(f"{si} 🗑 {nm}", callback_data=f"ulist_del_gr_{uid}"))
        if active:
            mk.add(types.InlineKeyboardButton("🗑 Xóa tất cả Group FB", callback_data="ulist_delall_gr"))
        mk.add(types.InlineKeyboardButton("« Quay lại tổng hợp", callback_data="ulist_tab_overview"))
        return msg, mk

    def make_tab_ig():
        grig_accounts = grig_dm.get_accounts(user_id)
        active = {k: v for k, v in grig_accounts.items() if v.get('platform') == 'instagram'}
        if not active:
            msg = "📷 *Instagram*\n\n_Chưa có tài khoản nào đang theo dõi._"
        else:
            live_c = sum(1 for v in active.values() if v.get('status') == 'live')
            msg  = f"📷 *INSTAGRAM — {len(active)} tài khoản*\n"
            msg += f"🟢 Live: {live_c}  │  🔴 Die: {len(active)-live_c}\n"
            msg += "━━━━━━━━━━━━━━━━━━━━\n"
            for i, (uid, d) in enumerate(list(active.items())[:20], 1):
                si = "🟢" if d['status'] == 'live' else "🔴"
                nm = d.get('name', uid)[:20].replace("_", r"\_").replace("*", r"\*")
                nt = d.get('note', '')[:15]
                msg += f"{i}. {si} *{nm}*\n   🔗 @`{uid}`\n"
                if nt: msg += f"   📝 {nt}\n"
        mk = types.InlineKeyboardMarkup(row_width=1)
        for uid, d in list(active.items())[:20]:
            si = "🟢" if d.get('status') == 'live' else "🔴"
            nm = d.get('name', uid)[:20]
            mk.add(types.InlineKeyboardButton(f"{si} 🗑 {nm}", callback_data=f"ulist_del_ig_{uid}"))
        if active:
            mk.add(types.InlineKeyboardButton("🗑 Xóa tất cả Instagram", callback_data="ulist_delall_ig"))
        mk.add(types.InlineKeyboardButton("« Quay lại tổng hợp", callback_data="ulist_tab_overview"))
        return msg, mk

    def make_tab_tt():
        tt_data = get_tracking_tiktok().get(str(chat_id), {})
        active = {k: v for k, v in tt_data.items() if v.get('status') != 'done'}
        if not active:
            msg = "🎵 *TikTok*\n\n_Chưa có tài khoản nào đang theo dõi._"
        else:
            live_c = sum(1 for v in active.values() if v.get('last_check') in ['EXISTS','live'])
            msg  = f"🎵 *TIKTOK — {len(active)} tài khoản*\n"
            msg += f"🟢 Live: {live_c}  │  🔴 Die: {len(active)-live_c}\n"
            msg += "━━━━━━━━━━━━━━━━━━━━\n"
            for i, (un, v) in enumerate(list(active.items())[:20], 1):
                si = "🟢" if v.get('last_check') in ['EXISTS','live'] else "🔴"
                verified = " ☑️" if v.get("verified") else ""
                nm = v.get('name', un)[:18].replace("_", r"\_")
                su = un.replace("_", r"\_")
                msg += f"{i}. {si} *{nm}*{verified}\n   🔗 @`{su}`\n"
        mk = types.InlineKeyboardMarkup(row_width=1)
        for un, v in list(active.items())[:20]:
            si = "🟢" if v.get('last_check') in ['EXISTS','live'] else "🔴"
            mk.add(types.InlineKeyboardButton(f"{si} 🗑 @{un[:22]}", callback_data=f"ulist_del_tt_{un[:45]}"))
        if active:
            mk.add(types.InlineKeyboardButton("🗑 Xóa tất cả TikTok", callback_data="ulist_delall_tt"))
        mk.add(types.InlineKeyboardButton("« Quay lại tổng hợp", callback_data="ulist_tab_overview"))
        return msg, mk

    def make_tab_post():
        if not _get_fp_watching():
            msg = "📌 *Post FB*\n\n_Chưa có Post nào đang theo dõi._"
        else:
            live_c = sum(1 for i in _get_fp_watching().values() if i.get('last_status') == 'live')
            msg  = f"📌 *POST FB — {len(_get_fp_watching())} post*\n"
            msg += f"🟢 Live: {live_c}  │  🔴 Die: {len(_get_fp_watching())-live_c}\n"
            msg += "━━━━━━━━━━━━━━━━━━━━\n"
            for i, (url, info) in enumerate(list(_get_fp_watching().items())[:20], 1):
                si  = "🟢" if info.get('last_status') == 'live' else "🔴"
                lb  = info.get('label', '')[:25] or url[-30:]
                ivl = info.get('interval', 0)
                msg += f"{i}. {si} *{lb}*\n   ⏱ Check mỗi {ivl}s\n"
        mk = types.InlineKeyboardMarkup(row_width=1)
        for url, info in list(_get_fp_watching().items())[:20]:
            si = "🟢" if info.get('last_status') == 'live' else "🔴"
            lb = info.get('label', '')[:20] or url[-20:]
            short_key = hashlib.md5(url.encode()).hexdigest()[:12]
            _get_fp_url_cache()[short_key] = url
            mk.add(types.InlineKeyboardButton(f"{si} 🗑 {lb}", callback_data=f"ulist_del_post_{short_key}"))
        if _get_fp_watching():
            mk.add(types.InlineKeyboardButton("🗑 Xóa tất cả Post FB", callback_data="ulist_delall_post"))
        mk.add(types.InlineKeyboardButton("« Quay lại tổng hợp", callback_data="ulist_tab_overview"))
        return msg, mk

    def make_tab_ytb():
        ytb_data = load_ytb_data().get(str(chat_id), {})
        if not ytb_data:
            msg = "🎞️ *YouTube*\n\n_Chưa có kênh nào đang theo dõi._"
        else:
            live_c = sum(1 for ch in ytb_data.values() if ch.get('status') == 'live')
            msg  = f"🎞️ *YOUTUBE — {len(ytb_data)} kênh*\n"
            msg += f"🟢 Hoạt động: {live_c}  │  🔴 Die: {len(ytb_data)-live_c}\n"
            msg += "━━━━━━━━━━━━━━━━━━━━\n"
            for i, (url, ch) in enumerate(list(ytb_data.items())[:20], 1):
                si = "🟢" if ch.get('status') == 'live' else "🔴"
                title = ch.get('title', url)[:22].replace("_", r"\_").replace("*", r"\*")
                subs = ch.get('subscriber_count', ch.get('subscribers', 0))
                try: subs_fmt = f"{int(subs):,}"
                except: subs_fmt = str(subs)
                msg += f"{i}. {si} *{title}*\n   👥 {subs_fmt} subs\n"
        mk = types.InlineKeyboardMarkup(row_width=1)
        for url, ch in list(ytb_data.items())[:20]:
            si    = "🟢" if ch.get('status') == 'live' else "🔴"
            title = ch.get('title', url)[:22]
            cid   = ch.get('channel_id', '')
            mk.add(types.InlineKeyboardButton(f"{si} 🗑 {title}", callback_data=f"ulist_del_ytb_{cid[:45]}"))
        if ytb_data:
            mk.add(types.InlineKeyboardButton("🗑 Xóa tất cả YouTube", callback_data="ulist_delall_ytb"))
        mk.add(types.InlineKeyboardButton("« Quay lại tổng hợp", callback_data="ulist_tab_overview"))
        return msg, mk

    # Dispatch: gọi đúng hàm theo tab
    tab_map = {
        "overview": make_overview,
        "fb":       make_tab_fb,
        "gr":       make_tab_gr,
        "ig":       make_tab_ig,
        "tt":       make_tab_tt,
        "post":     make_tab_post,
        "ytb":      make_tab_ytb,
    }
    make_fn = tab_map.get(tab, make_overview)
    try:
        msg, mk = make_fn()
    except Exception as e:
        msg = f"❌ Lỗi tải danh sách: {e}"
        mk = types.InlineKeyboardMarkup()

    try:
        if message_id:
            bot.edit_message_text(msg, chat_id, message_id, parse_mode="Markdown", reply_markup=mk)
        else:
            bot.send_message(chat_id, msg, parse_mode="Markdown", reply_markup=mk)
    except Exception as e:
        try:
            bot.send_message(chat_id, msg, parse_mode="Markdown", reply_markup=mk)
        except Exception:
            pass


def fbpost_handle_fb_link(message):
    raw_text = message.text.strip()
    chat_id = message.chat.id
    user_id = message.from_user.id
    # Extract URL Facebook từ text
    url_match = re.search(r'https?://(?:www\.)?(?:facebook\.com|fb\.com)/\S+', raw_text)
    if not url_match:
        return False
    url = url_match.group(0).rstrip('.,;)')
    if not ("/posts/" in url or "/share/" in url or "story_fbid" in url or "fbid=" in url or "/p/" in url):
        return False
    if url in _get_fp_watching():
        bot.reply_to(message, "⚠️ URL này đã theo dõi rồi!")
        return True

    # Tạo key ngắn (tránh callback_data > 64 bytes)
    import hashlib
    short_key = hashlib.md5(url.encode()).hexdigest()[:12]
    _get_fp_url_cache()[short_key] = url

    markup = types.InlineKeyboardMarkup(row_width=3)
    markup.add(
        types.InlineKeyboardButton("30s",     callback_data=f"fpadd|{short_key}|30"),
        types.InlineKeyboardButton("1 phút",  callback_data=f"fpadd|{short_key}|60"),
        types.InlineKeyboardButton("5 phút",  callback_data=f"fpadd|{short_key}|300"),
    )
    markup.add(
        types.InlineKeyboardButton("10 phút", callback_data=f"fpadd|{short_key}|600"),
        types.InlineKeyboardButton("30 phút", callback_data=f"fpadd|{short_key}|1800"),
    )
    bot.reply_to(message, f"📌 *Phát hiện link FB Post!*\n`{url[:80]}`\nChọn interval check ưu tiên chọn 30s sẽ check 1 lần:", parse_mode="Markdown", reply_markup=markup)
    return True


# fpadd| được xử lý trong handle_callback chính (dòng 8699) - đảm bảo cùng giao diện bot mẹ/con
# ============================================================
# ===== KẾT THÚC MODULE FB POST ==============================
# ============================================================


# ============================================================
# ===== MODULE CHECK FAQ / DIE (PLAYWRIGHT) ==================
# ============================================================

from urllib.parse import urlparse, parse_qs as faq_parse_qs

FAQ_CHECK_LOCK = threading.Lock()

FAQ_DIE_SHORT_CODES = {
    "217", "282", "956", "368", "505", "457",
}

def faq_esc(text):
    return str(text).replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

def faq_parse_uid(text):
    """Trả về (uid, error). Hỗ trợ UID số hoặc link Facebook."""
    text = text.strip()
    if text.isdigit():
        return text, None
    fb_domains = ["facebook.com", "fb.com"]
    if any(d in text for d in fb_domains):
        try:
            parsed = urlparse(text if text.startswith("http") else "https://" + text)
            params = faq_parse_qs(parsed.query)
            if "id" in params:
                uid = params["id"][0]
                if uid.isdigit():
                    return uid, None
            path = parsed.path.strip("/")
            for part in path.split("/"):
                if part.isdigit() and len(part) >= 9:
                    return part, None
        except Exception as e:
            return None, f"❌ Lỗi parse URL: {e}"
    return None, None

def faq_extract_uid_list(text):
    """Nhận nhiều dòng, trả về (uid_list, invalid_lines)."""
    uid_list, invalid_lines, seen = [], [], set()
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        uid, err = faq_parse_uid(line)
        if uid:
            if uid not in seen:
                seen.add(uid)
                uid_list.append(uid)
        else:
            invalid_lines.append(line)
    return uid_list, invalid_lines

def faq_check_uid(uid):
    """Dùng Playwright kiểm tra trạng thái UID Facebook qua recover/password."""
    from playwright.sync_api import sync_playwright
    url = f"https://www.facebook.com/recover/password/?u={uid}&n=999999"
    result = {
        "status": "UNKNOWN",
        "help_id": None,
        "help_id_short": None,
        "help_url": None,
        "message": "Không xác định được trạng thái.",
    }
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(
                headless=True,
                args=["--no-sandbox","--disable-setuid-sandbox",
                      "--disable-blink-features=AutomationControlled","--lang=vi-VN"],
            )
            context = browser.new_context(
                user_agent=("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                            "AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/122.0.0.0 Safari/537.36"),
                locale="vi-VN", viewport={"width": 1280, "height": 800},
            )
            page = context.new_page()
            page.goto(url, timeout=30000)
            page.wait_for_load_state("networkidle", timeout=30000)

            help_element = page.query_selector("a[href*='/help/']")
            if help_element:
                try:
                    with page.expect_navigation(timeout=30000):
                        help_element.click()
                except Exception:
                    pass
                page.wait_for_load_state("networkidle", timeout=30000)
                current_url = page.url
                match = re.search(r"/help/(\d+)", current_url)
                if not match:
                    href = help_element.get_attribute("href") or ""
                    match = re.search(r"/help/(\d+)", href)
                if match:
                    help_id = match.group(1)
                    help_id_short = help_id[-3:]
                    help_url = f"https://www.facebook.com/help/{help_id}"
                    if help_id_short in FAQ_DIE_SHORT_CODES:
                        result.update({"status": "DIE_FAQ", "help_id": help_id,
                                       "help_id_short": help_id_short, "help_url": help_url,
                                       "message": "DIE dạng 282 hoặc 956"})
                    else:
                        result.update({"status": "FAQ", "help_id": help_id,
                                       "help_id_short": help_id_short, "help_url": help_url,
                                       "message": "Cần xác minh hoặc khôi phục"})
            else:
                page_content = page.content()
                die_keywords = [
                    "Liên kết không hợp lệ","Lien ket khong hop le",
                    "Tài khoản này đã bị vô hiệu hóa","Tài khoản của bạn đã bị vô hiệu hóa",
                    "account has been disabled","link you used is invalid",
                ]
                if any(kw.lower() in page_content.lower() for kw in die_keywords):
                    result.update({"status": "DIE", "message": "DIE 282/956"})
                else:
                    result.update({"status": "LIVE", "message": "Tài khoản đang hoạt động bình thường."})
            page.close(); context.close(); browser.close()
    except Exception as e:
        result.update({"status": "ERROR", "message": str(e)})
    time.sleep(2)
    return result

def faq_format_result(uid, result):
    now = datetime.now().strftime("%H:%M:%S %d/%m/%Y")
    SEP = "─" * 20
    if result["status"] == "LIVE":
        return (
            "🟢 <b>TÀI KHOẢN ĐANG HOẠT ĐỘNG (LIVE)</b>\n"
            f"<code>{SEP}</code>\n\n"
            f"👤 <b>UID:</b> <code>{faq_esc(uid)}</code>\n"
            f"📡 <b>Trạng thái:</b> ✅ Đang sống\n"
            f"📌 <b>Chi tiết:</b> {faq_esc(result['message'])}\n"
            f"🕐 <b>Thời gian:</b> {faq_esc(now)}\n\n"
            f"<code>{SEP}</code>\n💚 <i>Account đang hoạt động bình thường!</i>"
        )
    elif result["status"] == "FAQ":
        return (
            "⚠️ <b>TÀI KHOẢN BỊ VÔ HIỆU HÓA (FAQ)</b>\n"
            f"<code>{SEP}</code>\n\n"
            f"👤 <b>UID:</b> <code>{faq_esc(uid)}</code>\n"
            f"🔑 <b>Mã trạng thái:</b> <code>{faq_esc(result['help_id_short'])}</code>\n"
            f"📌 <b>Chi tiết:</b> {faq_esc(result['message'])}\n"
            f"🔗 <b>Link help:</b> <a href=\"{faq_esc(result['help_url'])}\">{faq_esc(result['help_url'])}</a>\n"
            f"🕐 <b>Thời gian:</b> {faq_esc(now)}\n\n"
            f"<code>{SEP}</code>"
        )
    elif result["status"] == "DIE_FAQ":
        return (
            "🔴 <b>TÀI KHOẢN KHÔNG HOẠT ĐỘNG (DIE)</b>\n"
            f"<code>{SEP}</code>\n\n"
            f"👤 <b>UID:</b> <code>{faq_esc(uid)}</code>\n"
            f"🔑 <b>Mã trạng thái:</b> <code>{faq_esc(result['help_id_short'])}</code>\n"
            f"📌 <b>Chi tiết:</b> {faq_esc(result['message'])}\n"
            f"🔗 <b>Link help:</b> <a href=\"{faq_esc(result['help_url'])}\">{faq_esc(result['help_url'])}</a>\n"
            f"🕐 <b>Thời gian:</b> {faq_esc(now)}\n\n"
            f"<code>{SEP}</code>\n💀 <i>Tài khoản đã bị khóa / DIE!</i>"
        )
    elif result["status"] == "DIE":
        return (
            "💀 <b>DIE 282/956</b>\n"
            f"<code>{SEP}</code>\n\n"
            f"👤 <b>UID:</b> <code>{faq_esc(uid)}</code>\n"
            f"📌 <b>Chi tiết:</b> Tài khoản không hợp lệ hoặc đã bị vô hiệu hóa\n"
            f"🕐 <b>Thời gian:</b> {faq_esc(now)}\n\n"
            f"<code>{SEP}</code>"
        )
    elif result["status"] == "ERROR":
        return (
            f"❌ <b>Lỗi kiểm tra UID:</b> <code>{faq_esc(uid)}</code>\n\n"
            f"📌 {faq_esc(result['message'])}\n"
            f"🕐 <b>Thời gian:</b> {faq_esc(now)}"
        )
    else:
        return (
            f"❓ <b>Không xác định trạng thái</b>\n\n"
            f"👤 <b>UID:</b> <code>{faq_esc(uid)}</code>\n"
            f"📌 {faq_esc(result['message'])}\n"
            f"🕐 <b>Thời gian:</b> {faq_esc(now)}"
        )

def faq_run_check(chat_id, message_id, uid_list, _subbot_ctx=None):
    """Chạy check toàn bộ danh sách UID, gửi kết quả từng cái."""
    # Khôi phục context bot con nếu chạy từ thread relay
    if _subbot_ctx is not None:
        _subbot_tl.ctx = _subbot_ctx
    if not FAQ_CHECK_LOCK.acquire(blocking=False):
        bot.send_message(chat_id, "⏳ <b>Bot đang bận check. Thử lại sau vài giây.</b>", parse_mode="HTML")
        return
    total = len(uid_list)
    try:
        proc_msg = bot.send_message(
            chat_id,
            f"🔍 <b>Đang kiểm tra {total} UID...</b> Vui lòng chờ.",
            parse_mode="HTML", reply_to_message_id=message_id
        )
        for idx, uid in enumerate(uid_list, 1):
            if total > 1:
                try:
                    bot.edit_message_text(
                        f"🔍 <b>Đang kiểm tra [{idx}/{total}]:</b> <code>{faq_esc(uid)}</code>",
                        chat_id, proc_msg.message_id, parse_mode="HTML"
                    )
                except Exception:
                    pass
            result = faq_check_uid(uid)
            reply_text = faq_format_result(uid, result)
            bot.send_message(chat_id, reply_text, parse_mode="HTML",
                             reply_to_message_id=message_id)
        try:
            bot.delete_message(chat_id, proc_msg.message_id)
        except Exception:
            pass
        if total > 1:
            bot.send_message(chat_id, f"✅ <b>Kiểm tra xong {total} UID!</b>", parse_mode="HTML")
    except Exception as e:
        bot.send_message(chat_id, f"❌ <b>Lỗi hệ thống:</b> <code>{faq_esc(str(e))}</code>", parse_mode="HTML")
    finally:
        FAQ_CHECK_LOCK.release()
        if _subbot_ctx is not None:
            _subbot_tl.ctx = None

@bot.message_handler(commands=["checkfaq"])
def cmd_checkfaq(message):
    if not require_feature_access_message(message, "check_faq", FEATURE_LABELS["check_faq"]):
        return
    parts = message.text.strip().split(None, 1)
    if len(parts) < 2:
        bot.reply_to(message,
            "❌ Cần nhập UID hoặc link.\n\n"
            "Ví dụ:\n<code>/checkfaq 100001234567890</code>\n"
            "<code>/checkfaq https://facebook.com/profile.php?id=100001234567890</code>",
            parse_mode="HTML")
        return
    uid_list, invalid_lines = faq_extract_uid_list(parts[1])
    if not uid_list:
        bot.reply_to(message,
            "❌ Không tìm thấy UID hợp lệ.\nNhập số UID hoặc link facebook.com/profile.php?id=...",
            parse_mode="HTML")
        return
    if invalid_lines:
        warn = "⚠️ Các dòng không nhận dạng được (bỏ qua):\n"
        for line in invalid_lines[:5]:
            warn += f"  • <code>{faq_esc(line[:80])}</code>\n"
        bot.send_message(message.chat.id, warn, parse_mode="HTML")
    threading.Thread(target=faq_run_check,
                     args=(message.chat.id, message.message_id, uid_list,
                           getattr(_subbot_tl, 'ctx', None)),
                     daemon=True).start()

# ===== KẾT THÚC MODULE CHECK FAQ / DIE =======================

# ============================================================
# ===== MODULE BOT CON (SUB-BOT) - RELAY PROXY ===============
# ============================================================
# Bot con là proxy trong suốt của bot mẹ.
# Mọi message/callback từ user → bot con → xử lý bởi handlers
# của bot mẹ → reply về bot con.
# Tự động đồng bộ 100% khi bot mẹ update, không cần sửa gì.
# Dữ liệu: data_sub_bots.json
# Schema: { "user_id": { "token": "...", "bot_name": "...", ... } }
# ============================================================

SUB_BOT_VIDEO_TUTORIAL = "https://www.facebook.com/share/v/19Qb6JHwzC/"

# Dict lưu stop events và offsets cho polling threads
_SUB_BOT_STOP_EVENTS = {}   # {token: threading.Event}
_SUB_BOT_OFFSETS     = {}   # {token: int}

# ── Thread-local context cho relay proxy ─────────────────────
_subbot_tl = threading.local()

def _get_subbot_ctx():
    """Trả về context relay hiện tại của thread, hoặc None."""
    return getattr(_subbot_tl, 'ctx', None)

# ── SmartStateDict: cô lập state bot mẹ và bot con ───────────
class _SmartStateDict(dict):
    """
    Thay thế các dict state (temp_user_state, user_input_state, v.v.)
    Khi relay từ bot con, ctx['state_key'] = real_chat_id.
    Mọi thao tác đọc/ghi tự động dùng real_chat_id đó làm key
    → state bot con và bot mẹ hoàn toàn độc lập.
    """
    def _k(self, key):
        try:
            ctx = getattr(_subbot_tl, 'ctx', None)
            if ctx and 'state_key' in ctx:
                return ctx['state_key']
        except Exception:
            pass
        return key

    def __getitem__(self, k):    return super().__getitem__(self._k(k))
    def __setitem__(self, k, v): super().__setitem__(self._k(k), v)
    def __delitem__(self, k):    super().__delitem__(self._k(k))
    def __contains__(self, k):   return super().__contains__(self._k(k))
    def get(self, k, d=None):    return super().get(self._k(k), d)
    def pop(self, k, *a):        return super().pop(self._k(k), *a)

# Gán lại tất cả state dict thành SmartStateDict
temp_user_state  = _SmartStateDict()
user_input_state = _SmartStateDict()
active_chats     = _SmartStateDict()

# ── Data helpers ─────────────────────────────────────────────

# ── VIP Bot Con helpers ──────────────────────────────────────

def botcon_check_vip(user_id):
    """Kiểm tra user có VIP bot con còn hạn không. Admin luôn True."""
    if user_id in ADMIN_IDS:
        return True, "Vĩnh viễn (Admin)"
    data = botcon_load()
    info = data.get(str(user_id), {})
    expiry = info.get("vip_expiry", 0)
    now = int(time.time())
    if expiry > now:
        dt = datetime.fromtimestamp(expiry)
        return True, dt.strftime("%d/%m/%Y %H:%M")
    # Hết hạn → dừng polling nếu đang chạy
    if expiry > 0 and expiry <= now:
        token = info.get("token", "")
        if token and token in _SUB_BOT_STOP_EVENTS:
            try:
                botcon_stop_polling(token)
            except Exception:
                pass
    return False, "Chưa kích hoạt" if expiry == 0 else "Đã hết hạn"

def botcon_add_vip(user_id, months):
    """Cộng thêm VIP bot con cho user."""
    data = botcon_load()
    uid_str = str(user_id)
    if uid_str not in data:
        data[uid_str] = {}
    now = int(time.time())
    current = data[uid_str].get("vip_expiry", 0)
    base = current if current > now else now
    new_expiry = base + months * 30 * 86400
    data[uid_str]["vip_expiry"] = new_expiry
    botcon_save(data)
    return new_expiry

def botcon_show_vip_upgrade(chat_id, user_id, edit_msg_id=None):
    """Hiển thị bảng giá VIP bot con - giao diện đẹp, chưa có QR."""
    is_vip, vip_info = botcon_check_vip(user_id)
    if is_vip:
        status_line = f"✅ <b>VIP đến:</b> {vip_info}"
    else:
        status_line = "❌ <b>Chưa kích hoạt</b>"

    msg = (
        "⭐ <b>NÂNG CẤP VIP BOT CON</b>\n"
        f"📊 Trạng thái: {status_line}\n\n"
        "🌟 <b>BẢNG GIÁ GÓI VIP</b>\n"
        "├ <b>1 tháng</b>  —  50.000đ\n"
        "├ <b>3 tháng</b>  —  126.000đ <i>(-10%)</i>\n"
        "├ <b>6 tháng</b>  —  221.000đ <i>(-15%)</i>\n"
        "└ <b>12 tháng</b> —  400.000đ <i>(-20%)</i>\n\n"
        "🔥 <b>Quyền lợi:</b>\n"
        "├ 🤖 Bot Telegram riêng của bạn\n"
        "├ 📡 100% chức năng giống bot chính\n"
        "├ 🔔 Nhận thông báo tracking riêng\n"
        "└ 🔄 Tự động cập nhật liên tục\n\n"
        "👇 Chọn gói để xem QR thanh toán:"
    )
    mk = types.InlineKeyboardMarkup(row_width=2)
    mk.add(
        types.InlineKeyboardButton("1️⃣  1 tháng — 50.000đ",     callback_data="botcon_vip_buy_1"),
        types.InlineKeyboardButton("3️⃣  3 tháng — 126.000đ",    callback_data="botcon_vip_buy_3"),
    )
    mk.add(
        types.InlineKeyboardButton("6️⃣  6 tháng — 221.000đ",    callback_data="botcon_vip_buy_6"),
        types.InlineKeyboardButton("🔟 12 tháng — 400.000đ",    callback_data="botcon_vip_buy_12"),
    )
    mk.add(types.InlineKeyboardButton("🔙 Quay lại Bot Con", callback_data="botcon_menu"))
    try:
        if edit_msg_id:
            _botcon_orig['edit_message_text'](msg, chat_id, edit_msg_id, parse_mode="HTML", reply_markup=mk)
        else:
            _botcon_orig['send_message'](chat_id, msg, parse_mode="HTML", reply_markup=mk)
    except Exception:
        _botcon_orig['send_message'](chat_id, msg, parse_mode="HTML", reply_markup=mk)

def botcon_vip_buy_request(chat_id, user_id, plan_key):
    """Giao diện thanh toán đẹp: QR VietQR + copy STK."""
    plan = BOTCON_VIP_PLANS.get(plan_key)
    if not plan:
        return
    disc_text = f"  🏷 Tiết kiệm {plan['discount']}%" if plan["discount"] else ""
    noi_dung  = f"BOTCON {user_id} {plan_key}T"
    amount    = plan["price"]
    qr_url    = (f"https://img.vietqr.io/image/MB-0862197064-compact2.png"
                 f"?amount={amount}"
                 f"&addInfo={noi_dung.replace(' ', '%20')}"
                 f"&accountName=NGUYEN%20MAI%20NIN")
    caption = (
        f"💳 <b>THANH TOÁN VIP BOT CON</b>\n\n"
        f"📦 Gói: <b>{plan['label']}</b>{disc_text}\n"
        f"💰 Số tiền: <b>{format_vnd(amount)}</b>\n\n"
        f"🏦 NH: <b>MB Bank</b>\n"
        f"💳 STK: <code>0862197064</code>\n"
        f"👤 CTK: <b>NGUYỄN MAI NIN</b>\n\n"
        f"📝 Nội dung CK: <code>{noi_dung}</code>\n"
        f"⚠️ <i>Nhập đúng nội dung để Admin duyệt nhanh!</i>\n\n"
        f"📲 Quét QR hoặc CK theo thông tin trên\n"
        f"📸 CK xong → nhấn <b>Gửi bill</b> để Admin duyệt"
    )
    mk = types.InlineKeyboardMarkup(row_width=1)
    mk.add(types.InlineKeyboardButton(
        "📋 Sao chép STK: 0862197064", callback_data="botcon_copy_stk"))
    mk.add(types.InlineKeyboardButton(
        f"📸 Gửi bill xác nhận", callback_data=f"botcon_vip_bill_{plan_key}"))
    mk.add(types.InlineKeyboardButton(
        "🔙 Quay lại bảng giá", callback_data="botcon_vip_upgrade"))
    try:
        _botcon_orig['send_photo'](chat_id, qr_url, caption=caption,
                                   parse_mode="HTML", reply_markup=mk)
    except Exception:
        _botcon_orig['send_message'](chat_id, caption,
                                     parse_mode="HTML", reply_markup=mk)


def botcon_load():
    d = load_json(FILES["sub_bots"])
    return d if isinstance(d, dict) else {}

def botcon_save(data):
    save_json(FILES["sub_bots"], data)

def sync_vip_to_botcon(user_id, main_expiry=None):
    """Đồng bộ hạn VIP bot mẹ sang bot con."""
    if main_expiry is None:
        u = get_user_data(user_id)
        main_expiry = u.get("vip_expiry", 0) if u.get("vip_active") else 0

    data = botcon_load()
    uid_str = str(user_id)
    if uid_str not in data:
        data[uid_str] = {}

    data[uid_str]["vip_expiry"] = int(main_expiry or 0)
    botcon_save(data)

    token = data[uid_str].get("token", "")
    now = int(time.time())

    if not main_expiry or int(main_expiry) <= now:
        if token and token in _SUB_BOT_STOP_EVENTS:
            try:
                botcon_stop_polling(token)
            except Exception:
                pass
    else:
        if token:
            try:
                botcon_start_polling(token, int(user_id))
            except Exception:
                pass

    return int(main_expiry or 0)

def botcon_get_user(user_id):
    return botcon_load().get(str(user_id))

def botcon_api(token, method, payload=None, timeout=10):
    """Gọi Telegram Bot API cho sub-bot, trả về dict."""
    try:
        url = f"https://api.telegram.org/bot{token}/{method}"
        if payload:
            r = requests.post(url, json=payload, timeout=timeout)
        else:
            r = requests.get(url, timeout=timeout)
        return r.json()
    except Exception as e:
        return {"ok": False, "description": str(e)}

def botcon_send(token, chat_id, text, parse_mode="HTML", reply_markup=None):
    """Gửi tin nhắn văn bản qua Bot Con (không qua proxy)."""
    payload = {"chat_id": chat_id, "text": text, "parse_mode": parse_mode}
    if reply_markup:
        payload["reply_markup"] = (reply_markup.to_json()
                                   if hasattr(reply_markup, 'to_json')
                                   else json.dumps(reply_markup))
    res = botcon_api(token, "sendMessage", payload)
    if res.get("ok"):
        ctx = _get_subbot_ctx()
        if ctx:
            ctx.setdefault('last_msg_ids', []).append(res["result"]["message_id"])
    return res.get("ok", False)

def botcon_validate_token(token):
    """Kiểm tra token hợp lệ. Trả về (True, info) hoặc (False, error)."""
    data = botcon_api(token, "getMe")
    if data.get("ok"):
        info = data["result"]
        return True, {
            "bot_name":     info.get("first_name", "Bot"),
            "bot_username": info.get("username", ""),
            "bot_id":       info.get("id", 0),
        }
    return False, data.get("description", "Token không hợp lệ")

def botcon_notify(user_id, text):
    """Forward thông báo tracking qua Bot Con (chạy thread riêng)."""
    info = botcon_get_user(user_id)
    if not info:
        return
    token = info.get("token")
    if not token:
        return
    threading.Thread(
        target=botcon_send, args=(token, user_id, text), daemon=True
    ).start()

def botcon_find_owner(token):
    """Tìm owner_id theo token."""
    for uid_str, info in botcon_load().items():
        if info.get("token") == token:
            return int(uid_str)
    return None

# ── Relay Proxy: monkey-patch bot methods ─────────────────────
#
# Khi một thread đang xử lý update từ bot con (_subbot_tl.ctx != None),
# mọi lời gọi bot.send_message / bot.send_photo / ... sẽ tự động
# được redirect về bot con thay vì bot mẹ.
# Thread-local đảm bảo an toàn với đa luồng.

_botcon_orig = {}   # lưu các method gốc trước khi wrap

def _botcon_install_proxy():
    """
    Wrap các method của bot để relay về bot con khi có context.
    Gọi 1 lần duy nhất khi khởi động.
    """
    global _botcon_orig

    _botcon_orig['send_message']              = bot.send_message
    _botcon_orig['send_photo']                = bot.send_photo
    _botcon_orig['send_voice']                = bot.send_voice
    _botcon_orig['edit_message_text']         = bot.edit_message_text
    _botcon_orig['edit_message_caption']      = bot.edit_message_caption
    _botcon_orig['edit_message_reply_markup'] = bot.edit_message_reply_markup
    _botcon_orig['answer_callback_query']     = bot.answer_callback_query
    _botcon_orig['reply_to']                  = bot.reply_to
    _botcon_orig['delete_message']            = bot.delete_message
    _botcon_orig['send_document']             = bot.send_document
    _botcon_orig['send_chat_action']          = bot.send_chat_action

    def _rm(rm):
        if rm is None: return None
        if hasattr(rm, 'to_json'): return rm.to_json()
        return json.dumps(rm)

    # Counter âm để tạo fake message_id (không trùng với Telegram ID thật)
    _ctr = [-1000000000]

    def _track_mid(ctx, res):
        """Lưu message_id thật và trả FakeMsg với ID riêng để mapping delete/edit."""
        if res and res.get("ok"):
            real_mid = res["result"]["message_id"]
            ctx.setdefault('last_msg_ids', []).append(real_mid)
            # Tạo fake_id để code bot mẹ giữ và dùng sau cho delete/edit
            _ctr[0] -= 1
            fake_id = _ctr[0]
            ctx.setdefault('mid_map', {})[fake_id] = real_mid
            # Cũng map real→real để xử lý khi code dùng message_id thật từ call.message.message_id
            ctx['mid_map'][real_mid] = real_mid
            class _FakeMsg:
                message_id = fake_id
                chat = type('C', (), {'id': ctx['real_chat_id']})()
            return _FakeMsg()
        return None

    def _resolve_mid(ctx, message_id):
        """Tìm real message_id từ fake hoặc real ID."""
        mid_map = ctx.get('mid_map', {})
        if message_id in mid_map:
            return mid_map[message_id]
        # Fallback: last sent
        last = ctx.get('last_msg_ids', [])
        return last[-1] if last else message_id

    # ── send_message ─────────────────────────────────────────
    def _wrap_send_message(chat_id, text, **kw):
        ctx = _get_subbot_ctx()
        if ctx:
            payload = {"chat_id": ctx['real_chat_id'], "text": text}
            if kw.get('parse_mode'): payload['parse_mode'] = kw['parse_mode']
            rm = _rm(kw.get('reply_markup'))
            if rm: payload['reply_markup'] = rm
            res = botcon_api(ctx['token'], "sendMessage", payload)
            return _track_mid(ctx, res)
        return _botcon_orig['send_message'](chat_id, text, **kw)

    # ── send_photo ───────────────────────────────────────────
    def _wrap_send_photo(chat_id, photo, **kw):
        ctx = _get_subbot_ctx()
        if ctx:
            token = ctx['token']
            rcid  = ctx['real_chat_id']
            url   = f"https://api.telegram.org/bot{token}/sendPhoto"
            data  = {"chat_id": rcid}
            if kw.get('caption'):     data['caption']     = kw['caption']
            if kw.get('parse_mode'):  data['parse_mode']  = kw['parse_mode']
            if kw.get('has_spoiler'): data['has_spoiler'] = kw['has_spoiler']
            rm = _rm(kw.get('reply_markup'))
            if rm: data['reply_markup'] = rm
            try:
                # Chuẩn hóa photo → bytes
                if isinstance(photo, str) and os.path.isfile(photo):
                    with open(photo, 'rb') as f:
                        photo_bytes = f.read()
                elif isinstance(photo, bytes):
                    photo_bytes = photo
                elif hasattr(photo, 'read'):
                    # BytesIO: seek về đầu trước khi đọc tránh đọc rỗng
                    if hasattr(photo, 'seek'):
                        photo.seek(0)
                    photo_bytes = photo.read()
                elif isinstance(photo, str):
                    # URL: download về bytes để upload lên bot con
                    _hd = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                           "Accept": "image/*,*/*;q=0.8"}
                    _r = requests.get(photo, headers=_hd, timeout=FAST_API_TIMEOUT, allow_redirects=True)
                    if _r.status_code == 200 and len(_r.content) > 500:
                        photo_bytes = _r.content
                    else:
                        # fallback gửi URL trực tiếp
                        data['photo'] = photo
                        r = requests.post(url, json=data, timeout=30)
                        res = r.json()
                        if res.get("ok"):
                            return _track_mid(ctx, res)
                        raise Exception(res.get("description", "sendPhoto URL failed"))
                else:
                    data['photo'] = photo
                    r = requests.post(url, json=data, timeout=30)
                    res = r.json()
                    if res.get("ok"):
                        return _track_mid(ctx, res)
                    raise Exception(res.get("description", "sendPhoto direct failed"))

                if not photo_bytes:
                    raise Exception("photo_bytes rỗng")
                r = requests.post(url, data=data,
                                  files={'photo': ('photo.jpg', photo_bytes, 'image/jpeg')},
                                  timeout=30)
                res = r.json()
                if res.get("ok"):
                    return _track_mid(ctx, res)
                raise Exception(res.get("description", "sendPhoto upload failed"))
            except Exception as e:
                print(f"[BotCon] send_photo lỗi: {e}")
                cap = kw.get('caption', '')
                if cap:
                    return _wrap_send_message(rcid, cap,
                                              parse_mode=kw.get('parse_mode', 'HTML'),
                                              reply_markup=kw.get('reply_markup'))
            return None
        return _botcon_orig['send_photo'](chat_id, photo, **kw)

    # ── send_voice ───────────────────────────────────────────
    def _wrap_send_voice(chat_id, voice, **kw):
        ctx = _get_subbot_ctx()
        if ctx:
            token = ctx['token']
            rcid  = ctx['real_chat_id']
            url   = f"https://api.telegram.org/bot{token}/sendVoice"
            data  = {"chat_id": rcid}
            if kw.get('caption'):    data['caption']    = kw['caption']
            if kw.get('parse_mode'): data['parse_mode'] = kw['parse_mode']
            rm = _rm(kw.get('reply_markup'))
            if rm: data['reply_markup'] = rm
            try:
                if hasattr(voice, 'read'):
                    voice_bytes = voice.read()
                    r = requests.post(url, data=data,
                                      files={'voice': ('audio.ogg', voice_bytes, 'audio/ogg')}, timeout=60)
                elif isinstance(voice, bytes):
                    r = requests.post(url, data=data,
                                      files={'voice': ('audio.ogg', voice, 'audio/ogg')}, timeout=60)
                else:
                    data['voice'] = voice
                    r = requests.post(url, json=data, timeout=60)
                res = r.json()
                if res.get("ok"):
                    return _track_mid(ctx, res)
                raise Exception(res.get("description", "sendVoice failed"))
            except Exception as e:
                print(f"[BotCon] send_voice lỗi: {e}")
                cap = kw.get('caption', '')
                if cap:
                    _wrap_send_message(rcid, f"🎵 {cap}", parse_mode=kw.get('parse_mode'))
            return None
        return _botcon_orig['send_voice'](chat_id, voice, **kw)

    # ── edit_message_text ────────────────────────────────────
    def _wrap_edit_message_text(text, chat_id, message_id, **kw):
        ctx = _get_subbot_ctx()
        if ctx:
            real_mid = _resolve_mid(ctx, message_id)
            if real_mid:
                payload = {"chat_id": ctx['real_chat_id'], "message_id": real_mid, "text": text}
                if kw.get('parse_mode'): payload['parse_mode'] = kw['parse_mode']
                rm = _rm(kw.get('reply_markup'))
                if rm: payload['reply_markup'] = rm
                res = botcon_api(ctx['token'], "editMessageText", payload)
                if not res.get("ok"):
                    _wrap_send_message(ctx['real_chat_id'], text, **kw)
            else:
                _wrap_send_message(ctx['real_chat_id'], text, **kw)
            return
        return _botcon_orig['edit_message_text'](text, chat_id, message_id, **kw)

    # ── edit_message_caption ─────────────────────────────────
    def _wrap_edit_message_caption(caption, chat_id, message_id, **kw):
        ctx = _get_subbot_ctx()
        if ctx:
            real_mid = _resolve_mid(ctx, message_id)
            if real_mid:
                payload = {"chat_id": ctx['real_chat_id'], "message_id": real_mid, "caption": caption}
                if kw.get('parse_mode'): payload['parse_mode'] = kw['parse_mode']
                rm = _rm(kw.get('reply_markup'))
                if rm: payload['reply_markup'] = rm
                res = botcon_api(ctx['token'], "editMessageCaption", payload)
                if not res.get("ok"):
                    _wrap_send_message(ctx['real_chat_id'], caption, **kw)
            else:
                _wrap_send_message(ctx['real_chat_id'], caption, **kw)
            return
        return _botcon_orig['edit_message_caption'](caption, chat_id, message_id, **kw)

    # ── edit_message_reply_markup ─────────────────────────────
    def _wrap_edit_message_reply_markup(chat_id, message_id, **kw):
        ctx = _get_subbot_ctx()
        if ctx:
            real_mid = _resolve_mid(ctx, message_id)
            if real_mid:
                payload = {"chat_id": ctx['real_chat_id'], "message_id": real_mid}
                rm = _rm(kw.get('reply_markup'))
                payload['reply_markup'] = rm if rm else "{}"
                botcon_api(ctx['token'], "editMessageReplyMarkup", payload)
            return
        return _botcon_orig['edit_message_reply_markup'](chat_id, message_id, **kw)

    # ── answer_callback_query ────────────────────────────────
    def _wrap_answer_callback_query(callback_query_id, text=None, show_alert=False, **kw):
        ctx = _get_subbot_ctx()
        if ctx:
            cbq_id = ctx.get('cbq_id', callback_query_id)
            payload = {"callback_query_id": cbq_id}
            if text: payload['text'] = text
            if show_alert: payload['show_alert'] = True
            botcon_api(ctx['token'], "answerCallbackQuery", payload)
            return
        return _botcon_orig['answer_callback_query'](callback_query_id, text=text,
                                                     show_alert=show_alert, **kw)

    # ── reply_to ─────────────────────────────────────────────
    def _wrap_reply_to(message, text, **kw):
        ctx = _get_subbot_ctx()
        if ctx:
            return _wrap_send_message(ctx['real_chat_id'], text, **kw)
        return _botcon_orig['reply_to'](message, text, **kw)

    # ── delete_message ───────────────────────────────────────
    def _wrap_delete_message(chat_id, message_id):
        ctx = _get_subbot_ctx()
        if ctx:
            real_mid = _resolve_mid(ctx, message_id)
            botcon_api(ctx['token'], "deleteMessage",
                       {"chat_id": ctx['real_chat_id'], "message_id": real_mid})
            return
        return _botcon_orig['delete_message'](chat_id, message_id)

    # ── send_document ────────────────────────────────────────
    def _wrap_send_document(chat_id, document, **kw):
        ctx = _get_subbot_ctx()
        if ctx:
            cap = kw.get('caption', '')
            if cap:
                _wrap_send_message(ctx['real_chat_id'], f"📄 {cap}",
                                   parse_mode=kw.get('parse_mode'))
            return
        return _botcon_orig['send_document'](chat_id, document, **kw)

    # ── send_chat_action ─────────────────────────────────────
    def _wrap_send_chat_action(chat_id, action):
        ctx = _get_subbot_ctx()
        if ctx:
            botcon_api(ctx['token'], "sendChatAction",
                       {"chat_id": ctx['real_chat_id'], "action": action})
            return
        return _botcon_orig['send_chat_action'](chat_id, action)

    # Gán các wrapper vào bot object
    bot.send_message              = _wrap_send_message
    bot.send_photo                = _wrap_send_photo
    bot.send_voice                = _wrap_send_voice
    bot.edit_message_text         = _wrap_edit_message_text
    bot.edit_message_caption      = _wrap_edit_message_caption
    bot.edit_message_reply_markup = _wrap_edit_message_reply_markup
    bot.answer_callback_query     = _wrap_answer_callback_query
    bot.reply_to                  = _wrap_reply_to
    bot.delete_message            = _wrap_delete_message
    bot.send_document             = _wrap_send_document
    bot.send_chat_action          = _wrap_send_chat_action

    print("[BotCon] ✅ Relay proxy đã được cài đặt.")

# ── Fake objects cho relay ────────────────────────────────────

def _make_fake_user(user_id, first_name="User", username="user"):
    u = type('FU', (), {})()
    u.id          = user_id
    u.first_name  = first_name
    u.username    = username
    u.is_bot      = False
    return u

def _make_fake_message(raw_msg, owner_id):
    """
    Tạo fake telebot Message từ raw dict Telegram.
    - from_user.id = owner_id  (để handlers check quyền đúng)
    - chat.id = real_chat_id từ raw_msg (để state/tracking theo đúng chat bot con)
    """
    m              = type('FM', (), {})()
    from_info      = raw_msg.get("from", {})
    real_cid       = raw_msg["chat"]["id"]
    m.chat         = type('FC', (), {
        'id': real_cid, 'type': 'private'
    })()
    m.message_id   = raw_msg.get("message_id", 0)
    m.from_user    = _make_fake_user(
        owner_id,
        first_name = from_info.get("first_name", "User"),
        username   = from_info.get("username", "user"),
    )
    m.text         = raw_msg.get("text", "")
    m.caption      = raw_msg.get("caption")
    m.photo        = raw_msg.get("photo")
    m.document     = raw_msg.get("document")
    m.content_type = ("text"  if m.text
                      else "photo" if m.photo
                      else "document" if m.document
                      else "text")
    return m

def _make_fake_callback(raw_cbq, owner_id):
    """Tạo fake telebot CallbackQuery từ raw dict Telegram."""
    c          = type('FC', (), {})()
    from_info  = raw_cbq.get("from", {})
    c.id       = raw_cbq.get("id", "")
    c.from_user= _make_fake_user(
        owner_id,
        first_name = from_info.get("first_name", "User"),
        username   = from_info.get("username", "user"),
    )
    c.data     = raw_cbq.get("data", "")

    raw_msg       = raw_cbq.get("message", {})
    real_cid      = raw_msg.get("chat", {}).get("id", owner_id)
    cm            = type('FCM', (), {})()
    cm.chat       = type('C', (), {'id': real_cid})()
    cm.message_id = raw_msg.get("message_id", 0)
    cm.text       = raw_msg.get("text", "")
    cm.caption    = raw_msg.get("caption")
    c.message     = cm
    return c

# ── Dispatch callback về đúng handler ────────────────────────

def _subbot_dispatch_callback(fake_call):
    """
    Route callback từ bot con về đúng handler đã đăng ký bằng decorator.
    Telebot xử lý theo thứ tự đăng ký; bot con relay phải làm tương tự.
    """
    data = fake_call.data

    # donate_* / show_donate
    if data.startswith("donate_") or data == "show_donate":
        try: donate_callback(fake_call)
        except Exception as e: print(f"[BotCon] dispatch donate lỗi: {e}")
        return

    # ulist_* (danh sách tổng hợp)
    if data.startswith("ulist_"):
        try: unified_list_callback(fake_call)
        except Exception as e: print(f"[BotCon] dispatch ulist lỗi: {e}")
        return

    # grig_* (group/instagram callbacks)
    if (data.startswith("grig_done_") or data.startswith("grig_cancel_") or
            data.startswith("grig_unfollow_") or data == "grig_list"):
        try: grig_handle_callbacks(fake_call)
        except Exception as e: print(f"[BotCon] dispatch grig lỗi: {e}")
        return

    # Tất cả còn lại (bao gồm fpadd|, fbpost_*, music_*, ...) → handle_callback chính
    handle_callback(fake_call)


# ── Xử lý update từ bot con ──────────────────────────────────

def _subbot_handle_update(token, update, owner_id):
    """
    Relay một update nhận từ bot con sang handlers của bot mẹ.
    - state_key = real_chat_id: đảm bảo temp_user_state không xung đột với bot mẹ
    - Mọi lỗi được gửi về user trong bot con
    """
    try:
        msg = update.get("message") or update.get("edited_message")
        cbq = update.get("callback_query")

        # ── Xử lý Message ────────────────────────────────────
        if msg:
            chat_id = msg["chat"]["id"]
            text    = msg.get("text", "")
            cmd     = (text.split()[0].split("@")[0].lower()
                       if text and text.startswith("/") else "")

            # Chỉ cho phép owner (người đăng ký bot con) sử dụng
            real_sender_id = msg.get("from", {}).get("id")
            if real_sender_id and real_sender_id != owner_id:
                botcon_send(token, chat_id,
                    "🚫 <b>Bot này chỉ dành riêng cho chủ sở hữu.</b>\n"
                    "Bạn không có quyền sử dụng bot này.",
                    parse_mode="HTML")
                return

            if cmd == "/mybot":
                botcon_send(token, chat_id,
                    "⚠️ Lệnh này chỉ dùng được trong <b>bot chính</b>.\n"
                    "👉 Mở bot chính để quản lý Bot Con.",
                    parse_mode="HTML")
                return

            # Kiểm tra VIP bot con
            is_vip_bc, _ = botcon_check_vip(owner_id)
            if not is_vip_bc:
                if cmd in ("/start", "/menu"):
                    # Hiển thị thông báo cần VIP kèm bảng giá (qua bot mẹ)
                    botcon_send(token, chat_id,
                        "⚠️ <b>Gói VIP đã hết hạn</b>\n\n"
                        "Tính năng này yêu cầu VIP.\n"
                        "Vui lòng gia hạn trên bot chính để tiếp tục sử dụng.",
                        parse_mode="HTML")
                return

            _subbot_tl.ctx = {
                'token':        token,
                'real_chat_id': chat_id,
                'last_msg_ids': [],
                'mid_map':      {},
                'state_key':    chat_id,   # ← key riêng, tránh xung đột bot mẹ
            }
            try:
                fake_msg = _make_fake_message(msg, owner_id)
                if cmd in ("/start", "/menu"):
                    show_menu(fake_msg)
                else:
                    handle_text(fake_msg)
            except Exception as e:
                import traceback
                err_detail = traceback.format_exc()
                print(f"[BotCon] Lỗi xử lý message owner={owner_id}: {e}\n{err_detail}")
                try:
                    botcon_send(token, chat_id,
                        f"⚠️ <b>Lỗi xử lý:</b> <code>{str(e)[:200]}</code>",
                        parse_mode="HTML")
                except Exception:
                    pass
            finally:
                _subbot_tl.ctx = None

        # ── Xử lý Callback Query ─────────────────────────────
        if cbq:
            cid    = cbq["message"]["chat"]["id"]
            cbq_id = cbq.get("id", "")
            data   = cbq.get("data", "")

            # Chỉ cho phép owner sử dụng
            real_sender_id = cbq.get("from", {}).get("id")
            if real_sender_id and real_sender_id != owner_id:
                botcon_api(token, "answerCallbackQuery",
                           {"callback_query_id": cbq_id,
                            "text": "🚫 Bot này chỉ dành riêng cho chủ sở hữu!", "show_alert": True})
                return

            if data.startswith("botcon_") or data == "send_notification_all":
                botcon_api(token, "answerCallbackQuery",
                           {"callback_query_id": cbq_id,
                            "text": "⚠️ Chức năng này chỉ dùng được trong bot chính!", "show_alert": True})
                if data.startswith("botcon_"):
                    botcon_send(token, cid,
                        "⚙️ Chức năng <b>quản lý Bot Con</b> chỉ có trong bot chính.\n"
                        "👉 Mở bot chính để cài đặt.",
                        parse_mode="HTML")
                return

            _subbot_tl.ctx = {
                'token':        token,
                'real_chat_id': cid,
                'last_msg_ids': [],
                'mid_map':      {},
                'cbq_id':       cbq_id,
                'state_key':    cid,       # ← key riêng
            }
            try:
                fake_call = _make_fake_callback(cbq, owner_id)
                # Map message_id thật của tin nhắn bot con vào mid_map
                real_msg_id = cbq.get("message", {}).get("message_id", 0)
                if real_msg_id:
                    _subbot_tl.ctx['mid_map'][real_msg_id] = real_msg_id
                # Dispatch đến đúng handler theo data prefix
                _subbot_dispatch_callback(fake_call)
            except Exception as e:
                import traceback
                err_detail = traceback.format_exc()
                print(f"[BotCon] Lỗi xử lý callback owner={owner_id} data={data}: {e}\n{err_detail}")
                try:
                    botcon_api(token, "answerCallbackQuery",
                               {"callback_query_id": cbq_id,
                                "text": f"⚠️ Lỗi: {str(e)[:100]}", "show_alert": True})
                except Exception:
                    pass
            finally:
                _subbot_tl.ctx = None

    except Exception as e:
        print(f"[BotCon] Lỗi handle_update owner={owner_id}: {e}")

# ── Polling loop ──────────────────────────────────────────────

def _subbot_polling_loop(token, owner_id, stop_event):
    print(f"[BotCon] Bắt đầu polling cho owner={owner_id}")
    offset = _SUB_BOT_OFFSETS.get(token, 0)
    botcon_api(token, "deleteWebhook", {"drop_pending_updates": False})
    while not stop_event.is_set():
        try:
            resp = botcon_api(
                token, "getUpdates",
                {"offset": offset, "timeout": 20, "limit": 10},
                timeout=30
            )
            if resp.get("ok"):
                for upd in resp.get("result", []):
                    offset = upd["update_id"] + 1
                    _SUB_BOT_OFFSETS[token] = offset
                    threading.Thread(
                        target=_subbot_handle_update,
                        args=(token, upd, owner_id),
                        daemon=True
                    ).start()
        except Exception as e:
            if not stop_event.is_set():
                print(f"[BotCon] Lỗi polling owner={owner_id}: {e}")
                time.sleep(3)
    print(f"[BotCon] Dừng polling cho owner={owner_id}")

def botcon_start_polling(token, owner_id):
    """Khởi động polling thread cho 1 sub-bot token."""
    botcon_stop_polling(token)
    ev = threading.Event()
    _SUB_BOT_STOP_EVENTS[token] = ev
    threading.Thread(
        target=_subbot_polling_loop,
        args=(token, owner_id, ev),
        daemon=True
    ).start()

def botcon_stop_polling(token):
    """Dừng polling thread của 1 token."""
    if token in _SUB_BOT_STOP_EVENTS:
        _SUB_BOT_STOP_EVENTS[token].set()
        del _SUB_BOT_STOP_EVENTS[token]

def botcon_start_all_polling():
    """Khởi động polling cho tất cả sub-bot đã đăng ký (gọi khi main bot start)."""
    data = botcon_load()
    now  = int(time.time())
    for uid_str, info in data.items():
        token  = info.get("token")
        expiry = info.get("vip_expiry", 0)
        uid_int = int(uid_str)
        # Chỉ start nếu còn VIP hoặc là admin
        if not token:
            continue
        if uid_int not in ADMIN_IDS and expiry > 0 and expiry <= now:
            print(f"[BotCon] Bỏ qua polling uid={uid_str} (VIP hết hạn)")
            continue
        try:
            botcon_start_polling(token, uid_int)
        except Exception as e:
            print(f"[BotCon] Lỗi start polling uid={uid_str}: {e}")

# ── UI quản lý Bot Con (trong bot mẹ) ────────────────────────

def botcon_show_menu(chat_id, user_id, edit_msg_id=None):
    info = botcon_get_user(user_id)
    is_vip, vip_info = botcon_check_vip(user_id)
    vip_line = f"✅ VIP đến: <b>{vip_info}</b>" if is_vip else "❌ <b>Chưa có VIP</b> — Cần nâng cấp để dùng!"
    if info:
        bot_name     = info.get("bot_name", "Bot")
        bot_username = info.get("bot_username", "bot")
        added_at     = info.get("added_at", "N/A")
        is_polling   = info.get("token", "") in _SUB_BOT_STOP_EVENTS
        status_icon  = "🟢 Đang chạy" if is_polling else "🔴 Chưa kết nối"
        msg = (
            "🤖 <b>BOT CON CỦA BẠN</b>\n\n"
            f"📛 <b>Tên:</b> {bot_name}\n"
            f"🔗 <b>Username:</b> @{bot_username}\n"
            f"📡 <b>Trạng thái:</b> {status_icon}\n"
            f"📅 <b>Thêm lúc:</b> {added_at}\n"
            f"⭐ <b>VIP:</b> {vip_line}\n\n"
            "✨ Bot con có <b>100% chức năng</b> giống bot chính, tự động cập nhật."
        )
        mk = types.InlineKeyboardMarkup(row_width=1)
        mk.add(
            types.InlineKeyboardButton(f"💬 Mở @{bot_username}",
                                       url=f"https://t.me/{bot_username}"),
        )
        if is_vip:
            mk.add(types.InlineKeyboardButton("⭐ Gia hạn VIP Bot Con", callback_data="botcon_vip_upgrade"))
        else:
            mk.add(types.InlineKeyboardButton("⭐ NÂNG CẤP VIP BOT CON", callback_data="botcon_vip_upgrade"))
        mk.add(types.InlineKeyboardButton("🔄 Thay Token Bot Con", callback_data="botcon_change_token"))
        mk.add(
            types.InlineKeyboardButton("🗑 Xóa Bot Con",
                                       callback_data="botcon_delete"),
            types.InlineKeyboardButton("🔙 Quay lại Menu",
                                       callback_data="botcon_back_to_main"),
        )
    else:
        msg = (
            "🤖 <b>BOT CON CỦA BẠN</b>\n\n"
            "📭 Bạn chưa có bot con.\n\n"
            "🤔 <b>Bot con là gì?</b>\n"
            "├ Bot Telegram riêng của bạn\n"
            "├ 100% chức năng giống bot chính\n"
            "├ Tự động update khi bot chính thay đổi\n"
            "└ Nhận thông báo tracking riêng\n\n"
            "🔑 <b>Cách lấy token:</b>\n"
            "└ @BotFather → /newbot hoặc /mybots → /token"
        )
        mk = types.InlineKeyboardMarkup(row_width=1)
        mk.add(
            types.InlineKeyboardButton("➕ Thêm Bot Token",
                                       callback_data="botcon_add_token"),
            types.InlineKeyboardButton("🔙 Quay lại Menu",
                                       callback_data="botcon_back_to_main"),
        )
    try:
        if edit_msg_id:
            _botcon_orig['edit_message_text'](
                msg, chat_id, edit_msg_id, parse_mode="HTML", reply_markup=mk)
        else:
            _botcon_orig['send_message'](
                chat_id, msg, parse_mode="HTML", reply_markup=mk)
    except Exception:
        _botcon_orig['send_message'](
            chat_id, msg, parse_mode="HTML", reply_markup=mk)

def botcon_show_add_token(chat_id, user_id):
    msg = (
        "🔑 <b>Thêm Bot Token</b>\n\n"
        "📟 <b>Lấy token từ bot cũ:</b>\n"
        "@BotFather → /mybots → chọn bot → /token\n\n"
        "📟 <b>Tạo bot mới:</b>\n"
        "@BotFather → /newbot → đặt tên → copy token\n\n"
        "💡 Token có dạng:\n"
        "<code>123456789:ABCdefGHIjklMNOpqrsTUVwxyz</code>\n\n"
        "⬇️ <b>Gửi token ngay bên dưới:</b>"
    )
    mk = types.InlineKeyboardMarkup(row_width=1)
    mk.add(
        types.InlineKeyboardButton("📹 Xem video hướng dẫn",
                                   url=SUB_BOT_VIDEO_TUTORIAL),
        types.InlineKeyboardButton("🔙 Quay lại Bot Con",
                                   callback_data="botcon_back_menu"),
    )
    _botcon_orig['send_message'](chat_id, msg, parse_mode="HTML",
                                  reply_markup=mk,
                                  disable_web_page_preview=False)
    temp_user_state[user_id] = {"mode": "botcon_add", "step": "wait_token"}

def botcon_delete_token(chat_id, user_id):
    data    = botcon_load()
    uid_str = str(user_id)
    if uid_str in data:
        token    = data[uid_str].get("token", "")
        bot_name = data[uid_str].get("bot_name", "Bot")
        botcon_stop_polling(token)
        del data[uid_str]
        botcon_save(data)
        msg = (
            f"🗑 <b>Đã xóa Bot Con!</b>\n\n"
            f"Bot <b>{bot_name}</b> đã được gỡ.\n"
            "Bạn có thể thêm bot mới bất kỳ lúc nào."
        )
    else:
        msg = "⚠️ Bạn chưa có bot con nào để xóa."
    mk = types.InlineKeyboardMarkup(row_width=1)
    mk.add(
        types.InlineKeyboardButton("➕ Thêm Bot Token mới",
                                   callback_data="botcon_add_token"),
        types.InlineKeyboardButton("🔙 Quay lại Menu",
                                   callback_data="botcon_back_to_main"),
    )
    _botcon_orig['send_message'](chat_id, msg, parse_mode="HTML", reply_markup=mk)

def botcon_process_token(message, token):
    """Validate token, lưu và khởi động polling."""
    chat_id = message.chat.id
    user_id = message.from_user.id
    token   = token.strip()

    if not re.match(r'^\d+:[A-Za-z0-9_-]{35,}$', token):
        _botcon_orig['reply_to'](message,
            "❌ <b>Token không đúng định dạng!</b>\n\n"
            "Token hợp lệ có dạng:\n"
            "<code>123456789:ABCdefGHIjklMNOpqrsTUVwxyz</code>\n\n"
            "Vui lòng kiểm tra lại.",
            parse_mode="HTML")
        temp_user_state[user_id] = {"mode": "botcon_add", "step": "wait_token"}
        return

    if token == TOKEN:
        _botcon_orig['reply_to'](message,
            "❌ <b>Không thể dùng token của bot chính!</b>\n"
            "Vui lòng tạo bot riêng từ @BotFather.",
            parse_mode="HTML")
        temp_user_state[user_id] = {"mode": "botcon_add", "step": "wait_token"}
        return

    wait_msg = _botcon_orig['reply_to'](message,
                                         "⏳ Đang kiểm tra token...",
                                         parse_mode="HTML")
    valid, result = botcon_validate_token(token)
    try:
        _botcon_orig['delete_message'](chat_id, wait_msg.message_id)
    except Exception:
        pass

    if not valid:
        _botcon_orig['reply_to'](message,
            f"❌ <b>Token không hợp lệ!</b>\n\n📌 Lỗi: {result}\n\n"
            "Vui lòng kiểm tra lại token.",
            parse_mode="HTML")
        temp_user_state[user_id] = {"mode": "botcon_add", "step": "wait_token"}
        return

    # Lưu
    data = botcon_load()
    data[str(user_id)] = {
        "token":        token,
        "bot_name":     result["bot_name"],
        "bot_username": result["bot_username"],
        "bot_id":       result["bot_id"],
        "added_at":     datetime.now().strftime("%H:%M %d/%m/%Y"),
    }
    botcon_save(data)
    temp_user_state.pop(user_id, None)

    # Khởi động polling ngay
    botcon_start_polling(token, user_id)

    is_vip, vip_info = botcon_check_vip(user_id)

    if is_vip:
        # Admin hoặc đã có VIP → dùng được luôn
        mk = types.InlineKeyboardMarkup(row_width=1)
        mk.add(
            types.InlineKeyboardButton(f"💬 Mở @{result['bot_username']}",
                                        url=f"https://t.me/{result['bot_username']}"),
            types.InlineKeyboardButton("🤖 Xem Bot Con của tôi",
                                       callback_data="botcon_menu"),
            types.InlineKeyboardButton("🔙 Quay lại Menu",
                                       callback_data="botcon_back_to_main"),
        )
        _botcon_orig['reply_to'](
            message,
            f"✅ <b>Đã kết nối Bot Con thành công!</b>\n\n"
            f"📛 <b>Tên bot:</b> {result['bot_name']}\n"
            f"🔗 <b>Username:</b> @{result['bot_username']}\n"
            f"⭐ <b>VIP:</b> {vip_info}\n\n"
            f"🟢 Nhấn /start tại @{result['bot_username']} để dùng!",
            parse_mode="HTML",
            reply_markup=mk
        )
    else:
        # Chưa có VIP → thông báo và hiện bảng giá
        _botcon_orig['reply_to'](
            message,
            f"✅ <b>Đã thêm Bot Con thành công!</b>\n\n"
            f"📛 <b>Tên bot:</b> {result['bot_name']}\n"
            f"🔗 <b>Username:</b> @{result['bot_username']}\n\n"
            f"⚠️ <b>Cần nâng cấp VIP để kích hoạt bot con!</b>\n"
            f"Vui lòng chọn gói VIP bên dưới để sử dụng.",
            parse_mode="HTML"
        )
        botcon_show_vip_upgrade(chat_id, user_id)

@bot.message_handler(commands=["addbotconvip"])
def cmd_addbotconvip(message):
    """Admin cấp VIP Bot Con thủ công: /addbotconvip <uid> <tháng>"""
    if message.from_user.id not in ADMIN_IDS:
        return
    parts = message.text.strip().split()
    if len(parts) < 3:
        bot.reply_to(message, "Dùng: <code>/addbotconvip &lt;uid&gt; &lt;tháng&gt;</code>\nVí dụ: <code>/addbotconvip 123456789 3</code>", parse_mode="HTML")
        return
    try:
        target_uid = int(parts[1])
        months     = int(parts[2])
    except ValueError:
        bot.reply_to(message, "❌ UID và số tháng phải là số nguyên.")
        return
    new_exp = botcon_add_vip(target_uid, months)
    exp_str = datetime.fromtimestamp(new_exp).strftime("%d/%m/%Y")
    bot.reply_to(message, f"✅ Đã cấp <b>{months} tháng</b> VIP Bot Con cho UID <code>{target_uid}</code>\nHạn đến: <b>{exp_str}</b>", parse_mode="HTML")
    try:
        _botcon_orig['send_message'](target_uid,
            f"🎉 <b>VIP Bot Con đã được kích hoạt!</b>\n\n"
            f"⭐ Thời hạn: <b>{months} tháng</b>\n"
            f"📅 Hạn đến: <b>{exp_str}</b>\n\n"
            "✅ Bot con của bạn đã sẵn sàng!",
            parse_mode="HTML")
    except Exception:
        pass
    # Khởi động polling nếu có token
    bc_data = botcon_load()
    bc_info = bc_data.get(str(target_uid), {})
    if bc_info.get("token"):
        botcon_start_polling(bc_info["token"], target_uid)



# ═══════════════════════════════════════════════════════
# MODULE ADMIN QUẢN LÝ BOT CON
# ═══════════════════════════════════════════════════════

def adminbot_show_menu(chat_id, edit_msg_id=None):
    data = botcon_load()
    total = len(data)
    active = sum(1 for v in data.values() if v.get("token", "") in _SUB_BOT_STOP_EVENTS)
    now = int(time.time())
    vip_ok = sum(1 for v in data.values() if v.get("vip_expiry", 0) > now or v.get("vip_expiry", 0) == 0)
    msg = (
        "<b>🛠 ADMIN - QUẢN LÝ BOT CON</b>\n\n"
        + f"📊 <b>Tổng bot con:</b> {total}\n"
        + f"🟢 <b>Đang chạy:</b> {active}\n"
        + f"⭐ <b>Còn VIP:</b> {vip_ok}\n\n"
        + "Chọn chức năng:"
    )
    mk = types.InlineKeyboardMarkup(row_width=1)
    mk.add(
        types.InlineKeyboardButton("📋 Danh sách tất cả Bot Con", callback_data="adminbot_list"),
        types.InlineKeyboardButton("🔍 Kiểm tra hạn VIP Bot Con", callback_data="adminbot_check_vip"),
        types.InlineKeyboardButton("🗑 Xóa Bot Con của user", callback_data="adminbot_delete_ask"),
        types.InlineKeyboardButton("⭐ Cấp/Gia hạn VIP Bot Con", callback_data="adminbot_addvip_ask"),
        types.InlineKeyboardButton("🔴 Dừng Bot Con của user", callback_data="adminbot_stop_ask"),
        types.InlineKeyboardButton("🟢 Khởi động lại Bot Con", callback_data="adminbot_start_ask"),
        types.InlineKeyboardButton("🔙 Quay lại Admin Panel", callback_data="open_admin_panel"),
    )
    try:
        if edit_msg_id:
            bot.edit_message_text(msg, chat_id, edit_msg_id, parse_mode="HTML", reply_markup=mk)
        else:
            bot.send_message(chat_id, msg, parse_mode="HTML", reply_markup=mk)
    except Exception:
        bot.send_message(chat_id, msg, parse_mode="HTML", reply_markup=mk)


def adminbot_list_all(chat_id, edit_msg_id=None):
    data = botcon_load()
    now = int(time.time())
    if not data:
        msg = "<b>📭 Chưa có bot con nào được đăng ký.</b>"
    else:
        parts = ["<b>📋 DANH SÁCH TẤT CẢ BOT CON</b>\n"]
        for idx, (uid_str, info) in enumerate(data.items(), 1):
            token = info.get("token", "")
            bot_name = info.get("bot_name", "N/A")
            bot_username = info.get("bot_username", "N/A")
            added_at = info.get("added_at", "N/A")
            is_running = token in _SUB_BOT_STOP_EVENTS
            expiry = info.get("vip_expiry", 0)
            if expiry == 0:
                vip_str = "⭐ Vĩnh viễn (Admin)"
            elif expiry > now:
                days_left = int((expiry - now) / 86400)
                exp_date = datetime.fromtimestamp(expiry).strftime("%d/%m/%Y")
                vip_str = "✅ Còn " + str(days_left) + " ngày (hết " + exp_date + ")"
            else:
                vip_str = "❌ Đã hết hạn"
            status_str = "🟢 Đang chạy" if is_running else "🔴 Dừng"
            parts.append(
                "<b>" + str(idx) + ". " + bot_name + "</b> (@" + bot_username + ")\n"
                + "   👤 UID: <code>" + uid_str + "</code>\n"
                + "   📡 " + status_str + " | " + vip_str + "\n"
                + "   📅 Thêm lúc: " + added_at
            )
        msg = "\n\n".join(parts)
    mk = types.InlineKeyboardMarkup(row_width=1)
    mk.add(types.InlineKeyboardButton("🔙 Quay lại", callback_data="adminbot_menu"))
    try:
        if edit_msg_id:
            bot.edit_message_text(msg[:4096], chat_id, edit_msg_id, parse_mode="HTML", reply_markup=mk)
        else:
            bot.send_message(chat_id, msg[:4096], parse_mode="HTML", reply_markup=mk)
    except Exception:
        bot.send_message(chat_id, msg[:4096], parse_mode="HTML", reply_markup=mk)


def adminbot_check_vip_all(chat_id, edit_msg_id=None):
    data = botcon_load()
    now = int(time.time())
    if not data:
        msg = "<b>📭 Chưa có bot con nào.</b>"
    else:
        parts = ["<b>🔍 KIỂM TRA HẠN VIP BOT CON</b>\n"]
        sorted_data = sorted(
            data.items(),
            key=lambda x: x[1].get("vip_expiry", 0) if x[1].get("vip_expiry", 0) != 0 else float('inf')
        )
        for uid_str, info in sorted_data:
            bot_username = info.get("bot_username", "N/A")
            bot_name = info.get("bot_name", "N/A")
            expiry = info.get("vip_expiry", 0)
            if expiry == 0:
                vip_line = "⭐ Vĩnh viễn (Admin)"
            elif expiry > now:
                days_left = int((expiry - now) / 86400)
                hrs_left = int(((expiry - now) % 86400) / 3600)
                exp_date = datetime.fromtimestamp(expiry).strftime("%d/%m/%Y %H:%M")
                if days_left == 0:
                    vip_line = "⚠️ Còn " + str(hrs_left) + " giờ (hết " + exp_date + ")"
                else:
                    vip_line = "✅ Còn " + str(days_left) + " ngày " + str(hrs_left) + "h (hết " + exp_date + ")"
            else:
                expired_ago = int((now - expiry) / 86400)
                vip_line = "❌ Đã hết hạn " + str(expired_ago) + " ngày trước"
            parts.append(
                "• <b>" + bot_name + "</b> (@" + bot_username + ")\n"
                + "  UID: <code>" + uid_str + "</code>\n"
                + "  " + vip_line
            )
        msg = "\n\n".join(parts)
    mk = types.InlineKeyboardMarkup(row_width=1)
    mk.add(types.InlineKeyboardButton("🔙 Quay lại", callback_data="adminbot_menu"))
    try:
        if edit_msg_id:
            bot.edit_message_text(msg[:4096], chat_id, edit_msg_id, parse_mode="HTML", reply_markup=mk)
        else:
            bot.send_message(chat_id, msg[:4096], parse_mode="HTML", reply_markup=mk)
    except Exception:
        bot.send_message(chat_id, msg[:4096], parse_mode="HTML", reply_markup=mk)


def handle_adminbot_input(message):
    user_id = message.from_user.id
    state = temp_user_state.get(user_id, {})
    mode = state.get("mode", "")
    chat_id = message.chat.id
    text = message.text.strip() if message.text else ""

    if mode == "adminbot_delete":
        temp_user_state.pop(user_id, None)
        try:
            target_uid = int(text)
        except ValueError:
            bot.reply_to(message, "❌ UID không hợp lệ! Phải là số nguyên.")
            return True
        data = botcon_load()
        uid_str = str(target_uid)
        if uid_str not in data:
            bot.reply_to(message, "❌ Không tìm thấy bot con của UID <code>" + str(target_uid) + "</code>.", parse_mode="HTML")
            return True
        info = data[uid_str]
        token = info.get("token", "")
        bot_name = info.get("bot_name", "N/A")
        bot_username = info.get("bot_username", "N/A")
        if token and token in _SUB_BOT_STOP_EVENTS:
            try:
                botcon_stop_polling(token)
            except Exception:
                pass
        del data[uid_str]
        botcon_save(data)
        bot.reply_to(message,
            "✅ <b>Đã xóa bot con thành công!</b>\n\n"
            + "📛 Bot: " + bot_name + " (@" + bot_username + ")\n"
            + "👤 UID: <code>" + str(target_uid) + "</code>",
            parse_mode="HTML")
        try:
            bot.send_message(target_uid,
                "⚠️ <b>Bot con của bạn đã bị Admin xóa.</b>\n"
                "Liên hệ Admin nếu cần hỗ trợ.",
                parse_mode="HTML")
        except Exception:
            pass
        return True

    elif mode == "adminbot_addvip":
        temp_user_state.pop(user_id, None)
        parts = text.split()
        if len(parts) < 2:
            bot.reply_to(message, "❌ Sai định dạng! Nhập: <code>UID số_tháng</code>", parse_mode="HTML")
            return True
        try:
            target_uid = int(parts[0])
            months = int(parts[1])
        except ValueError:
            bot.reply_to(message, "❌ UID và số tháng phải là số nguyên.")
            return True
        new_exp = botcon_add_vip(target_uid, months)
        exp_str = datetime.fromtimestamp(new_exp).strftime("%d/%m/%Y %H:%M")
        days_left = int((new_exp - int(time.time())) / 86400)
        bot.reply_to(message,
            "✅ <b>Đã cấp VIP Bot Con!</b>\n\n"
            + "👤 UID: <code>" + str(target_uid) + "</code>\n"
            + "⭐ Cộng thêm: <b>" + str(months) + " tháng</b>\n"
            + "📅 Hạn đến: <b>" + exp_str + "</b>\n"
            + "⏳ Còn lại: <b>" + str(days_left) + " ngày</b>",
            parse_mode="HTML")
        try:
            bot.send_message(target_uid,
                "🎉 <b>VIP Bot Con đã được cấp!</b>\n\n"
                + "⭐ Thêm: <b>" + str(months) + " tháng</b>\n"
                + "📅 Hạn đến: <b>" + exp_str + "</b>\n"
                + "⏳ Còn lại: <b>" + str(days_left) + " ngày</b>",
                parse_mode="HTML")
        except Exception:
            pass
        bc_data = botcon_load()
        bc_info = bc_data.get(str(target_uid), {})
        if bc_info.get("token"):
            botcon_start_polling(bc_info["token"], target_uid)
        return True

    elif mode == "adminbot_stop":
        temp_user_state.pop(user_id, None)
        try:
            target_uid = int(text)
        except ValueError:
            bot.reply_to(message, "❌ UID không hợp lệ!")
            return True
        data = botcon_load()
        info = data.get(str(target_uid), {})
        token = info.get("token", "")
        bot_username = info.get("bot_username", "N/A")
        if not token:
            bot.reply_to(message, "❌ UID <code>" + str(target_uid) + "</code> không có bot con.", parse_mode="HTML")
            return True
        if token in _SUB_BOT_STOP_EVENTS:
            botcon_stop_polling(token)
            bot.reply_to(message,
                "🔴 <b>Đã dừng bot con @" + bot_username + "</b>\n"
                + "👤 UID: <code>" + str(target_uid) + "</code>",
                parse_mode="HTML")
        else:
            bot.reply_to(message, "⚠️ Bot con @" + bot_username + " chưa chạy.")
        return True

    elif mode == "adminbot_start":
        temp_user_state.pop(user_id, None)
        try:
            target_uid = int(text)
        except ValueError:
            bot.reply_to(message, "❌ UID không hợp lệ!")
            return True
        data = botcon_load()
        info = data.get(str(target_uid), {})
        token = info.get("token", "")
        bot_username = info.get("bot_username", "N/A")
        if not token:
            bot.reply_to(message, "❌ UID <code>" + str(target_uid) + "</code> không có bot con.", parse_mode="HTML")
            return True
        botcon_start_polling(token, target_uid)
        bot.reply_to(message,
            "🟢 <b>Đã khởi động bot con @" + bot_username + "</b>\n"
            + "👤 UID: <code>" + str(target_uid) + "</code>",
            parse_mode="HTML")
        return True

    return False


@bot.message_handler(commands=["adminbot"])
def cmd_adminbot(message):
    if message.from_user.id not in ADMIN_IDS and message.from_user.id != BOSS_ID:
        return
    adminbot_show_menu(message.chat.id)


@bot.callback_query_handler(func=lambda call: call.data == "adminbot_menu")
def cb_adminbot_menu(call):
    bot.answer_callback_query(call.id)
    if call.from_user.id not in ADMIN_IDS and call.from_user.id != BOSS_ID:
        return
    # Luôn gửi tin mới vì Admin Panel dùng Markdown, adminbot dùng HTML
    adminbot_show_menu(call.message.chat.id)


@bot.callback_query_handler(func=lambda call: call.data == "adminbot_list")
def cb_adminbot_list(call):
    bot.answer_callback_query(call.id)
    if call.from_user.id not in ADMIN_IDS and call.from_user.id != BOSS_ID:
        return
    adminbot_list_all(call.message.chat.id, call.message.message_id)


@bot.callback_query_handler(func=lambda call: call.data == "adminbot_check_vip")
def cb_adminbot_check_vip(call):
    bot.answer_callback_query(call.id)
    if call.from_user.id not in ADMIN_IDS and call.from_user.id != BOSS_ID:
        return
    adminbot_check_vip_all(call.message.chat.id, call.message.message_id)


@bot.callback_query_handler(func=lambda call: call.data == "adminbot_delete_ask")
def cb_adminbot_delete_ask(call):
    bot.answer_callback_query(call.id)
    if call.from_user.id not in ADMIN_IDS and call.from_user.id != BOSS_ID:
        return
    msg = (
        "<b>🗑 XÓA BOT CON CỦA USER</b>\n\n"
        "Nhập UID của user cần xóa bot con:\n"
        "<i>(Bot con bị xóa và dừng polling)</i>"
    )
    mk = types.InlineKeyboardMarkup()
    mk.add(types.InlineKeyboardButton("❌ Hủy", callback_data="adminbot_menu"))
    try:
        bot.edit_message_text(msg, call.message.chat.id, call.message.message_id, parse_mode="HTML", reply_markup=mk)
    except Exception:
        bot.send_message(call.message.chat.id, msg, parse_mode="HTML", reply_markup=mk)
    temp_user_state[call.from_user.id] = {"mode": "adminbot_delete"}


@bot.callback_query_handler(func=lambda call: call.data == "adminbot_addvip_ask")
def cb_adminbot_addvip_ask(call):
    bot.answer_callback_query(call.id)
    if call.from_user.id not in ADMIN_IDS and call.from_user.id != BOSS_ID:
        return
    msg = (
        "<b>⭐ CẤP/GIA HẠN VIP BOT CON</b>\n\n"
        "Nhập theo định dạng:\n"
        "<code>UID so_thang</code>\n\n"
        "Ví dụ: <code>123456789 3</code>\n"
        "<i>(Cộng thêm vào hạn hiện tại)</i>"
    )
    mk = types.InlineKeyboardMarkup()
    mk.add(types.InlineKeyboardButton("❌ Hủy", callback_data="adminbot_menu"))
    try:
        bot.edit_message_text(msg, call.message.chat.id, call.message.message_id, parse_mode="HTML", reply_markup=mk)
    except Exception:
        bot.send_message(call.message.chat.id, msg, parse_mode="HTML", reply_markup=mk)
    temp_user_state[call.from_user.id] = {"mode": "adminbot_addvip"}


@bot.callback_query_handler(func=lambda call: call.data == "adminbot_stop_ask")
def cb_adminbot_stop_ask(call):
    bot.answer_callback_query(call.id)
    if call.from_user.id not in ADMIN_IDS and call.from_user.id != BOSS_ID:
        return
    msg = (
        "<b>🔴 DỪNG BOT CON CỦA USER</b>\n\n"
        "Nhập UID của user cần dừng bot con:"
    )
    mk = types.InlineKeyboardMarkup()
    mk.add(types.InlineKeyboardButton("❌ Hủy", callback_data="adminbot_menu"))
    try:
        bot.edit_message_text(msg, call.message.chat.id, call.message.message_id, parse_mode="HTML", reply_markup=mk)
    except Exception:
        bot.send_message(call.message.chat.id, msg, parse_mode="HTML", reply_markup=mk)
    temp_user_state[call.from_user.id] = {"mode": "adminbot_stop"}


@bot.callback_query_handler(func=lambda call: call.data == "adminbot_start_ask")
def cb_adminbot_start_ask(call):
    bot.answer_callback_query(call.id)
    if call.from_user.id not in ADMIN_IDS and call.from_user.id != BOSS_ID:
        return
    msg = (
        "<b>🟢 KHỞI ĐỘNG LẠI BOT CON</b>\n\n"
        "Nhập UID của user cần khởi động lại bot con:"
    )
    mk = types.InlineKeyboardMarkup()
    mk.add(types.InlineKeyboardButton("❌ Hủy", callback_data="adminbot_menu"))
    try:
        bot.edit_message_text(msg, call.message.chat.id, call.message.message_id, parse_mode="HTML", reply_markup=mk)
    except Exception:
        bot.send_message(call.message.chat.id, msg, parse_mode="HTML", reply_markup=mk)
    temp_user_state[call.from_user.id] = {"mode": "adminbot_start"}

# ═══════════════════════════════════════════════════════
# KẾT THÚC MODULE ADMIN QUẢN LÝ BOT CON
# ═══════════════════════════════════════════════════════
@bot.message_handler(commands=["mybot"])
def cmd_mybot(message):
    if not require_feature_access_message(message, "bot_con", FEATURE_LABELS["bot_con"]):
        return
    parts   = message.text.strip().split(None, 1)
    user_id = message.from_user.id
    chat_id = message.chat.id
    if len(parts) < 2:
        botcon_show_menu(chat_id, user_id)
    else:
        botcon_process_token(message, parts[1])

@bot.callback_query_handler(func=lambda call: call.data == "botcon_back_to_main")
def botcon_cb_back_to_main(call):
    _safe_callback_ack(call)
    class FakeMsg:
        def __init__(self, cid, user):
            self.chat      = type("C", (), {"id": cid})()
            self.from_user = user
    show_menu(FakeMsg(call.message.chat.id, call.from_user), edit_msg_id=call.message.message_id)

# ── Thread kiểm tra VIP hết hạn tự động ────────────────────
def _botcon_vip_watchdog():
    """Chạy mỗi 60s, dừng polling của bot con hết hạn VIP."""
    while True:
        try:
            now = int(time.time())
            data = botcon_load()
            for uid_str, info in data.items():
                expiry = info.get("vip_expiry", 0)
                token  = info.get("token", "")
                if expiry == 0:
                    continue  # admin hoặc chưa set
                if expiry <= now and token and token in _SUB_BOT_STOP_EVENTS:
                    print(f"[BotCon] VIP hết hạn uid={uid_str}, dừng polling.")
                    try:
                        botcon_stop_polling(token)
                    except Exception:
                        pass
                    # Gửi thông báo 1 lần khi vừa hết hạn (trong vòng 2 phút)
                    if now - expiry < 120:
                        try:
                            uid_int = int(uid_str)
                            _botcon_orig['send_message'](uid_int,
                                "⚠️ <b>VIP Bot Con đã hết hạn!</b>\n\n"
                                "Bot con của bạn đã bị tạm dừng.\n"
                                "Vui lòng gia hạn tại 🤖 Bot Con → ⭐ Gia hạn VIP.",
                                parse_mode="HTML")
                        except Exception:
                            pass
        except Exception as e:
            print(f"[BotCon] vip_watchdog lỗi: {e}")
        time.sleep(60)

threading.Thread(target=_botcon_vip_watchdog, daemon=True).start()

# Cài relay proxy ngay khi module load (sau khi bot object đã sẵn sàng)
_botcon_install_proxy()

# ===== KẾT THÚC MODULE BOT CON ================================

if __name__ == "__main__":

    # Load config

    init_config()

    

    signal.signal(signal.SIGINT, signal_handler)

    signal.signal(signal.SIGTERM, signal_handler)

    # ── Migrate data cũ: chuyển status "waiting" → "tracking", khởi tạo last_notified_status ──
    try:
        _mig_data = load_json(FILES["tracking"])
        _mig_changed = False
        for _cid, _uids in _mig_data.items():
            for _uid, _info in _uids.items():
                if _info.get("status") == "waiting":
                    _mig_data[_cid][_uid]["status"] = "tracking"
                    _mig_changed = True
                if "last_notified_status" not in _info:
                    _mig_data[_cid][_uid]["last_notified_status"] = _info.get("last_check", "UNKNOWN")
                    _mig_changed = True
        if _mig_changed:
            save_json(FILES["tracking"], _mig_data)
            print(f"✅ Migration tracking data: đã cập nhật {sum(len(v) for v in _mig_data.values())} UIDs sang chế độ theo dõi liên tục")
    except Exception as _mig_e:
        print(f"⚠️ Migration lỗi (không ảnh hưởng bot): {_mig_e}")

    t = threading.Thread(target=auto_check_thread); t.daemon = True; t.start()
    t_ytb = threading.Thread(target=ytb_monitoring_thread); t_ytb.daemon = True; t_ytb.start()
    grig_restart_threads()  # Khởi động lại thread check Group/IG
    fbpost_ensure_loop()    # Khởi động asyncio loop cho FB Post Monitor
    botcon_start_all_polling()  # Khởi động polling cho tất cả Bot Con đã đăng ký

    set_bot_commands()

    print("Bot đang chạy...")

    time.sleep(2)

    

    retry_count = 0

    max_retries = 999999

    

    while retry_count < max_retries:

        try:

            print("🔄 Đang kết nối với Telegram...")

            bot.infinity_polling(timeout=30, long_polling_timeout=30, skip_pending=True)

            break

        except KeyboardInterrupt:

            print("\n⚠️ Đã nhận tín hiệu dừng bot...")

            break

        except requests.exceptions.ConnectionError as e:

            retry_count += 1

            wait_time = min(retry_count * 5, 30)

            print(f"\n❌ Lỗi kết nối mạng! (Lần thử: {retry_count})")

            print(f"⏳ Đang thử kết nối lại sau {wait_time} giây...")

            print(f"💡 Kiểm tra: Internet, VPN, hoặc Telegram có bị chặn không?\n")

            time.sleep(wait_time)

        except Exception as e:

            retry_count += 1

            wait_time = min(retry_count * 5, 30)

            print(f"\n❌ Lỗi không xác định: {str(e)[:100]}")

            print(f"⏳ Thử lại sau {wait_time} giây... (Lần {retry_count})\n")

            time.sleep(wait_time)

    

    if retry_count >= max_retries:

        print("❌ Đã vượt quá số lần thử kết nối. Bot dừng hoạt động.")