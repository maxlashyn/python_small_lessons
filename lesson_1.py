a = int(input("Input number"))

if a > 10:
    print(1)
elif a > 5:
    print(5)
else:
    print(2)

"""
for (i = 0; i< 10;i += 2) {
cout <<i << endl;
}
"""
for i in range(0, 10, 2):
    print(i)

"""
while(true) {
}
"""
while True:
    print('false')
else:
    print('else')


"""
int factorial(int a) {
    return a;
}
"""


def factorial(a):
    return a + a

b = factorial(10)

print(b)

"""
калькулятор обычный
вводим раздельно первый операнд, операцию, второй операнд
возвращаем результат
"""