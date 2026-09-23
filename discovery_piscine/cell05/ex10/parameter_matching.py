#!/usr/bin/env python3
import sys

# เช็กว่ามีพารามิเตอร์ 1 ตัวถ้วนหรือไม่ (len เป็น 2)
if len(sys.argv) == 2:
    target_word = sys.argv[1]
    
    # ถามผู้ใช้ให้พิมพ์คำ
    user_input = input("What was the parameter? ")
    
    # เช็กว่าคำที่พิมพ์ตรงกับพารามิเตอร์หรือไม่
    if user_input == target_word:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    # ถ้าจำนวนพารามิเตอร์ผิด ให้พิมพ์ none
    print("none")