n = 8
board = [-1] * n

def safe(row, col):
    for r in range(row):
        if board[r] == col or abs(board[r] - col) == abs(r - row):
            return False
    return True

def solve(row=0):
    if row == n:
        for r in range(n):
            print(" ".join("Q" if board[r] == c else "." for c in range(n)))
        return True

    for col in range(n):
        if safe(row, col):
            board[row] = col
            if solve(row + 1):
                return True
    return False

solve()
