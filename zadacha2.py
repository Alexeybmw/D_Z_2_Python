# Напишитете программу, которая принемает на вход число N и выдает набор произведений чисел от 1 до N.

def main():
      n_number = int(input('Введите число:' ))
      factorial = 1
      factorial_list = []
      for i in range(1, n_number + 1):
            factorial *= i

            factorial_list.append(factorial)
      print("Факториал: ", n_number,'равен', factorial_list)

main()