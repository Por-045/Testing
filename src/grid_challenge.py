def grid_challenge(grid):
    tmp = []

    for i in grid:
        tmp.append(''.join(sorted(i)))
    for i in range(len(tmp[0])):
        for j in range(1, len(tmp)):
            if ord(tmp[j][i])<ord(tmp[j-1][i]):
                return 'NO'
    return 'YES'