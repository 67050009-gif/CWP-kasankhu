#!/usr/bin/env python3
import sys

# เช็กว่าไม่มีพารามิเตอร์เลย (มีความยาวแค่ 1 คือชื่อไฟล์)
if len(sys.argv) == 1:
    print("none")
else:
    # วนลูปอ่านพารามิเตอร์ทีละตัว (ข้ามชื่อไฟล์ที่ index 0)
    for param in sys.argv[1:]:
        # เช็กว่าคำนั้น "ไม่ได้" ลงท้ายด้วย ism
        if not param.endswith("ism"):
            # พิมพ์คำนั้นพร้อมเติม ism ต่อท้าย
            print(f"{param}ism")