#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from pathlib import Path

TARGET_FILE = Path("data_sub_bots.json")


def main():
    TARGET_FILE.write_text("{}", encoding="utf-8")
    print(f" reset danh sach bot con vip thanh cong: {TARGET_FILE.resolve()}")


if __name__ == "__main__":
    main()
