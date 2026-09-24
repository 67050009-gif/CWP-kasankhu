def checkmate(board):
    try:
        # 1. แปลง String กระดานให้เป็น List 2 มิติ (Array)
        rows = board.split('\n')
        
        # ตัดบรรทัดว่างสุดท้ายที่เกิดจากการพิมพ์ \n ปิดท้ายทิ้งไป
        if rows and not rows[-1]:
            rows = rows[:-1]

        n = len(rows)
        # ตรวจสอบว่ามีข้อมูลหรือไม่
        if n == 0:
            print("Error")
            return

        # 2. ตรวจสอบความถูกต้องของกระดาน (ต้องเป็น NxN และมี K ตัวเดียว)
        king_pos = None
        king_count = 0
        for r in range(n):
            # ตรวจสอบว่าความยาวของแต่ละแถวเท่ากับจำนวนแถวทั้งหมด (NxN)
            if len(rows[r]) != n:
                print("Error")
                return
            for c in range(n):
                piece = rows[r][c]
                if piece == 'K':
                    king_pos = (r, c)
                    king_count += 1
                # ถ้าเจอตัวอักษรที่ไม่ใช่ตัวหมากรุกที่กำหนดหรือจุดไข่ปลา
                elif piece not in ['.', 'P', 'B', 'R', 'Q']:
                    print("Error")
                    return

        # ต้องมี King แค่ 1 ตัวเท่านั้น
        if king_count != 1:
            print("Error")
            return

        # 3. เริ่มกระบวนการตรวจสอบการถูกรุก (Check)
        kr, kc = king_pos

        # ==========================================
        # เช็กแนวทแยง 4 มุม (สำหรับ Bishop, Queen และ Pawn)
        # ==========================================
        diagonals = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in diagonals:
            r, c = kr + dr, kc + dc
            dist = 1
            while 0 <= r < n and 0 <= c < n:
                piece = rows[r][c]
                if piece != '.':
                    # ถ้าเจอ Bishop หรือ Queen ในแนวทแยง ถือว่าถูกรุก
                    if piece in ['B', 'Q']:
                        print("Success")
                        return
                    # ถ้าเจอ Pawn ในแนวทแยงและอยู่ติดกัน (ระยะ 1 ช่อง) ถือว่าถูกรุก
                    if piece == 'P' and dist == 1:
                        print("Success")
                        return
                    # ถ้าเจอตัวอื่นๆ บังอยู่ ลำแสงจะถูกบล็อก ให้หยุดหาในทิศทางนี้
                    break
                r += dr
                c += dc
                dist += 1

        # ==========================================
        # เช็กแนวตรง 4 ทิศ บน ล่าง ซ้าย ขวา (สำหรับ Rook และ Queen)
        # ==========================================
        straights = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in straights:
            r, c = kr + dr, kc + dc
            while 0 <= r < n and 0 <= c < n:
                piece = rows[r][c]
                if piece != '.':
                    # ถ้าเจอ Rook หรือ Queen ในแนวตรง ถือว่าถูกรุก
                    if piece in ['R', 'Q']:
                        print("Success")
                        return
                    # ถ้าเจอตัวอื่นๆ บังอยู่ ลำแสงจะถูกบล็อก ให้หยุดหาในทิศทางนี้
                    break
                r += dr
                c += dc

        # หากรอดจากทุกทิศทาง แปลว่าไม่ถูกรุก
        print("Fail")

    except Exception:
        # ดักจับ Error ที่ไม่คาดคิด (Undefined behavior) เพื่อไม่ให้โปรแกรม Crash
        print("Error")