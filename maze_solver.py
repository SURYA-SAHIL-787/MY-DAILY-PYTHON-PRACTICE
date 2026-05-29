maze = [
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 1, 0],
    [0, 0, 0, 0]
]

start = (0, 0)
end = (3, 3)

def solve(r, c, path):
    if r < 0 or c < 0 or r >= 4 or c >= 4:
        return False
    if maze[r][c] == 1 or (r, c) in path:
        return False

    path.append((r, c))

    if (r, c) == end:
        print("Path:", path)
        return True

    if solve(r+1, c, path) or solve(r, c+1, path) or solve(r-1, c, path) or solve(r, c-1, path):
        return True

    path.pop()
    return False

solve(start[0], start[1], [])
