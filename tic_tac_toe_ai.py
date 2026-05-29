board = [" " for _ in range(9)]

def winner(b):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a, c, d in wins:
        if b[a] == b[c] == b[d] and b[a] != " ":
            return b[a]
    if " " not in b:
        return "Draw"
    return None

def minimax(b, is_ai):
    win = winner(b)
    if win == "O":
        return 1
    if win == "X":
        return -1
    if win == "Draw":
        return 0

    if is_ai:
        best = -999
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                best = max(best, minimax(b, False))
                b[i] = " "
        return best
    else:
        best = 999
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                best = min(best, minimax(b, True))
                b[i] = " "
        return best

def best_move():
    best_score = -999
    move = 0

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move

board[0] = "X"
board[4] = "X"

ai_move = best_move()
board[ai_move] = "O"

print(board[0:3])
print(board[3:6])
print(board[6:9])
