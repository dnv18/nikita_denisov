test_list = [1, 2, 'a', [2, 4, [[7, 8], 4, 6]]]


def sum_values(inp_list, sum_val=0):
    for i in inp_list:
        if type(i) == int:
            sum_val += i
        elif type(i) == list:
            sum_val += sum_values(i)
    return sum_val


print(sum_values(test_list))
