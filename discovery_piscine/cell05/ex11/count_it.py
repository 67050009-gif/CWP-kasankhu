import sys
# จำนวนพารามิเตอร์ทั้งหมด (ลบ 1 เพราะไม่นับชื่อไฟล์)
num_params = len(sys.argv) - 1

# ถ้าไม่มีพารามิเตอร์ ให้พิมพ์ none
if num_params == 0:
    print("none")
else:
    # พิมพ์จำนวนพารามิเตอร์ทั้งหมดก่อน
    print(f"parameters: {num_params}")
    
    # ใช้ for loop (ตามคำสั่งกรอบแดง) วนอ่านพารามิเตอร์ทีละตัว
    # เริ่มดึงข้อมูลจาก index 1 เป็นต้นไป เพื่อข้ามชื่อไฟล์
    for param in sys.argv[1:]:
        # พิมพ์ คำ นั้นๆ ตามด้วย : และความยาวของคำ
        print(f"{param}: {len(param)}")