from words2num import w2n

w_str = input('Введите строку (прим. five, six, seven): ')
# w_str = 'one hundred million five hundred seventy-six thousand eight hundred fifty-five,\n' \
#             'five, six, seven, nineteen, thirteen, one, two, five'
w_num = []
odd_sum = 0

for x in w_str.split(','):
    x = w2n(x)
    if x not in w_num:
        w_num.append(x)
        if x % 2 != 0:
            odd_sum += x
    w_num = sorted(w_num)
print(f'Строка: {" ".join(map(str, w_num))}')

for x in range(len(w_num) - 1):
    if x % 2 == 0:
        print(f'Сумма чисел с индексом {x} и {x+1}: {w_num[x] + w_num[x+1]}')
    else:
        print(f'Произведение чисел с индексом {x} и {x+1}: {w_num[x] * w_num[x+1]}')
print(f'Полная сумма всех нечётных чисел: {odd_sum}')
