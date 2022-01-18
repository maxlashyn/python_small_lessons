from my_lib.test import Stack

class MyException (Exception):
    def __init__(self, text):
        self.txt = text

calc_operation = ('+', '-', '*', '/', '=')
stack = Stack()



while True:
    try:
        stack.show()
        c = input('цифра или операция: ')

        if c in calc_operation:

            if c == '=':
                if not stack.is_empty():
                    result = stack.pop()
                    stack.push(result)
                    print(result)
                    continue
                else:
                    print('Стек пуст')
                    continue
            if stack.size() > 1:
                a = stack.pop()
                b = stack.pop()
                result = ''
                if c == '+':
                    result = a + b
                if c == '-':
                    result = a - b
                if c == '*':
                    result = a * b
                if c == '/':
                    result = a / b
                print(result)
                stack.push(result)
            else:
                print('Стек пуст')
        else:
            if c.isnumeric():
                stack.push(int(c))
            else:
                raise MyException('c not integer')
    except MyException as e:
        print(e)
    else:
        print('with no exception')
    finally:
        print('finally')