# Депозит
start_sum = float(input('Введите начальную сумму: '))
period = float(input('Введите период (лет): '))
rate = float(input('Введите процент (%): '))

final_sum = start_sum * (pow((1 + (rate / 100) / 12), period * 12))
print('Итоговая сумма в конце срока: ' + str(round(final_sum, 2)) + ' BYN')
