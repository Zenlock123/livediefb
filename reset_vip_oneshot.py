
import json, os, time

FILES_USERS = "data_users.json"

if not os.path.exists(FILES_USERS):
    print("Không tìm thấy data_users.json")
else:
    with open(FILES_USERS, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    BOSS_ID = 7203678858  # từ code gốc
    count = 0
    for uid_str, udata in data.items():
        try:
            uid_int = int(uid_str)
        except:
            uid_int = 0
        if uid_int == BOSS_ID:
            continue
        if udata.get("vip_active") or udata.get("vip_expiry", 0) > 0:
            data[uid_str]["vip_active"] = False
            data[uid_str]["vip_expiry"] = 0
            data[uid_str]["level"] = 1
            count += 1
    
    with open(FILES_USERS, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Đã xóa VIP của {count} user.")
