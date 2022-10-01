# Задайте список из n последовательности (1 + 1/n)^n и выведите на экран их сумму.

user_number = int(input('Введите число N: '))
result_seq = {}
sum_seq = 0

for key in range(1, user_number + 1):
      result_seq[key] = round((1 + 1 / key)**key, 2)
      sum_seq += result_seq[key]

print(f'N = {user_number}: {result_seq} \ n сумма = {round(sum_seq, 3)}')