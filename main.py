# Задача: Написать программу, которая из имеющегося массива строк сформирует массив из строк,
# длина которых меньше либо равна 3 символа. Первоначальный массив можно ввести с клавиатуры,
# либо задать на старте выполнения алгоритма. При решении не рекомендуется пользоваться коллекциями,
# лучше обойтись исключительно массивами.


str_in = input("Введите строку, либо STOP, чтобы закончить: ").lower()
string_array = []

while str_in != "stop":
    string_array.append(str_in)
    str_in = input("Введите строку, либо STOP, чтобы закончить: ").lower()

print(string_array)
