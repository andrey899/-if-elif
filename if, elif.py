first = input('первое число, ')
second = input('второе число, ')
third = input('третье число, ')
if first == second == third:  #if first == second and second == third and third == first: if first == second == third:
    print("Все равны, 3 числа")
elif first == second or second == third or third == first:
    print("равны, 2 числа")
else:
    print("нету равных чисел")




#number = input('Введите три числа через пробел >>>').split()
#if number[0] == number[1] == number[2]:
   # print(3)
#elif (number[0] == number[1] or
      #number[0] == number[2] or
      #number[1] == number[2]):
   # print(2)
#else:
   # print(0)