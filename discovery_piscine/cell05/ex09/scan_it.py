import sys
import re
# เช็กว่ามีพารามิเตอร์ 2 ตัวถ้วนหรือไม่ (ความยาวรวมชื่อไฟล์ต้องเป็น 3)
if len(sys.argv) == 3:
    keyword = sys.argv[1]
    text = sys.argv[2]
    
    # ใช้ re.findall() เพื่อหา keyword ใน text
    # ผลลัพธ์จะได้เป็น list ของคำที่หาเจอ
    matches = re.findall(keyword, text)
    
    # นับจำนวนครั้งที่หาเจอ
    match_count = len(matches)
    
    # ถ้าหาเจออย่างน้อย 1 ครั้ง ให้พิมพ์จำนวนครั้ง
    if match_count > 0:
        print(match_count)
    else:
        # ถ้าหาไม่เจอเลย ให้พิมพ์ none
        print("none")
else:
    # ถ้าจำนวนพารามิเตอร์ผิด ให้พิมพ์ none
    print("none")