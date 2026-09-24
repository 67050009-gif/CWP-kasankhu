def checkmate(board):
    if not isinstance(board, str):
        return

    rows = board.splitlines()

    if not rows:
        return

    size = len(rows)

    for row in rows:
        if len(row) != size:
            return

    kings = []

    for row in range(size):
        for col in range(size):
            if rows[row][col] == "K":
                kings.append((row, col))

    if len(kings) != 1:
        return

    king_row, king_col = kings[0]

    # Pawn
    pawn_row = king_row + 1

    if pawn_row < size:
        if king_col - 1 >= 0:
            if rows[pawn_row][king_col - 1] == "P":
                print("Success")
                return

        if king_col + 1 < size:
            if rows[pawn_row][king_col + 1] == "P":
                print("Success")
                return

    # Rook and Queen
    straight = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
    ]

    for dr, dc in straight:
        row = king_row + dr
        col = king_col + dc

        while 0 <= row < size and 0 <= col < size:
            piece = rows[row][col]

            if piece in "PBRQK":
                if piece == "R" or piece == "Q":
                    print("Success")
                    return
                break

            row += dr
            col += dc

    # Bishop and Queen
    diagonal = [
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1),
    ]

    for dr, dc in diagonal:
        row = king_row + dr
        col = king_col + dc

        while 0 <= row < size and 0 <= col < size:
            piece = rows[row][col]

            if piece in "PBRQK":
                if piece == "B" or piece == "Q":
                    print("Success")
                    return
                break

            row += dr
            col += dc

    print("Fail")
    