#!/usr/bin/env python3
from checkmate import checkmate

def main():
    # กระดานทดสอบตัวอย่าง (King จะถูกรุกโดย Pawn ที่มุมขวาล่าง หรือ Rook ซ้ายบน)
    board = """\
R...
.K..
P.P.
....
"""
    checkmate(board)

if __name__ == "__main__":
    main()