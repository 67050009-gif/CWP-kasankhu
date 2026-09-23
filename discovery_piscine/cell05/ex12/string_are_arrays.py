#!/usr/bin/env python3
import sys
# เช็กว่ามีพารามิเตอร์ 1 ตัวถ้วนหรือไม่ (ความยาวรวมชื่อไฟล์ต้องเป็น 2)
if len(sys.argv) == 2:
    text = sys.argv[1]
    # นับจำนวนตัวอักษร 'z' ในข้อความ
    z_count = text.count('z')
    if z_count > 0:
        # ถ้าเจอ พิมพ์ 'z' ซ้ำตามจำนวนที่เจอ
        print('z' * z_count)
    else:
        # ถ้าไม่เจอเลย ให้พิมพ์ none
        print("none")
else:
    # ถ้าจำนวนพารามิเตอร์ผิด ให้พิมพ์ none
    print("none")