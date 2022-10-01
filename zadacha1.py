#Напишите програьму,которая принемает на вход вещественное число и показывает сумму его цифр. 

float_num = float(input(f'Введите число: '))
sum = 0
if float_num < 0:
      float_num *= -1
float_str = str(float_num)
for i in float_str:
      if i !='.':
            sum += int(i)
print(sum)