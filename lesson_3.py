"""
1. модули
2. декораторы
3. классы
4. исключения
"""




def decor(func):
    def wrapper(*argc, **kwargs):
        print('init')
        result = func(*argc, **kwargs)
        print(result)
        return result

    return wrapper

@decor
def test(a, b):
    return a + b


try:
    print('1')
    if(2/2 == 1):
        raise MyException('2/2 = 1')
    a = 1/0
    print(3)
except ZeroDivisionError as e:
    print(e)
except MyException as e:
    print(e)
print('2')