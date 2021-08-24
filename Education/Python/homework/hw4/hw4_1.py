def get_ranges():
    col = sorted(set(map(int, input('Enter numbers sep by space: \n').split())))
    result = ''
    q = 0
    end = col[q]
    while q in range(len(col) - 1):
        st = col[q]
        count = 0
        while q < len(col) - 1 and col[q + 1] == col[q] + 1:
            end = col[q + 1]
            q += 1
            count += 1
        if count == 0:
            result += f'{end}, '
        else:
            result += f'{st}-{end}, '
        q += 1
    if col[-1] != end:
        result += col[-1]
    else:
        result = result[:-2]
    return result


print(get_ranges())
