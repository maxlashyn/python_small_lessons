"""
списки
"""

l = [1, 2, 3]
l2 = list()
a  = l[1:]
print (l)
print (l2)
print (a)
l[0] = 23
print(l)

"""
кортеж
после создания не изменяются
"""
l = (1,2, 3)
l2 = tuple()
a = l[0]
print(l)
print(l2)
print(a)


"""
множества
"""
l = {1, 2, 3}
l2 = set()
a = l.pop()
print(l)
print(l2)
print(a)
l = {1, 1, 2, 2, 3, 4, 4}
print(l)
l.add(5)
print(l)

"""
словари
"""
l = {'name':'igor', 'last name': 'lashyn'}
l2 = dict()
a = l['name']
print(l)
print(l2)
print(a)
l['name'] = 'maxim'
print(l)

a = 1
print(a.to_bytes(5, 'big'))
name = 'Igor'
print(name.upper())

dir(int)

def func(a, b, c = 'default'):
    print(b)
    print(c)
    
func(1,2, 3)

func(b = 2, a=1, c =3)

func(1, 2)

def add(a, b, c = '+'):
    if c is '+':
        print(a + b)
    else:
        print(a - b)
        
add(4, 5)
add(5, 4, '-')

"""
стек
b <- 1 <- 2 <- 3
b -> 3
b -> 2
b -> 1

стековый калькулятор
это когда сначала в стек укладываются данные
а потом с элементами на вершине стека выполняются операции
b <- 1 <- 2 <- 3
b +
    b -> 3
    b -> 2
    +
    b <- 5
b (1, 5)
b /
    b ->5
    b -> 1
    /
    b <- 5
b (5)
"""

stack = list()
if len(stack) > 0:
    print('not empty')
    stack.pop()
else:
    print('empty')

stack.append(1)
stack.append(2)
stack.append(5)
stack.append(3)
print(stack.count(5))
print(stack)
a = stack.pop()
print(a)
print(stack)
b = stack.pop()
stack.append(a + b)
print(stack)

"""
форматирование строк
cout << 1 << "text" << 2 << endl;
"""
print('text')
print("text")
print("'text'")
print('"text"')
print('text\'')
print('lashy\n igor')
print('firt line')
print('second line')
print('first lint\nsecond line')
print('firs\tsecond')

print("show %d number %s" % (4, 'name'))

print(f"1 + 2 = {1+2}")
name = 'test'
print(f"show {name}")
print(f"1+2={add(1,2,'-')}")

print("{1} = {0}".format('first', 'second'))
print("{first} = {second}".format(first = 1, second =3))

name = "igor lashyn"
print(name[:2])


"""
разбиение строки на массив по разделителю
"""
print(name.split(' '))
"""
объединение массива в строку с использованием разделителя
"""
print('barashek'.join(['maxim', 'lashyn']))