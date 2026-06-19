import requests, re, os, urllib.parse

cookie_raw = open(r"c:\Users\tranh\Desktop\checklivenin\cookie.txt", encoding="utf-8").read().strip()
cookies = {}
for part in cookie_raw.split(";"):
    if "=" not in part:
        continue
    k, v = part.split("=", 1)
    k, v = k.strip(), v.strip()
    if k:
        cookies[k] = v

uid = "61577256312713"
headers_mobile = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 Chrome/119 Mobile Safari/537.36",
    "Accept-Language": "vi-VN,vi;q=0.9",
}
url = f"https://www.facebook.com/profile.php?id={uid}"
r = requests.get(url, headers=headers_mobile, cookies=cookies, timeout=25)
print("status", r.status_code, "len", len(r.text))
print("login" in r.text.lower()[:5000])
m = re.search(r'property="og:title" content="(.*?)"', r.text)
print("og:title", m.group(1) if m else None)
m2 = re.search(r'property="og:description" content="(.*?)"', r.text)
print("og:desc", (m2.group(1)[:120] if m2 else None))
print("c_user in cookie", cookies.get("c_user"))
