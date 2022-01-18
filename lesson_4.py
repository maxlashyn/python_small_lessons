"""
1. работа с файлами
открыть файл мы можем
-на чтение r r+
-на запись w w+
-на добавление a a+

2. with as

3. yield
"""

# file = open('calc.py', 'r')
# row = file.readline() # one row
# print(row)
# char = file.read(1)
# print(char)
# file.close()

# with open('words.txt', 'w') as file:
#     file.writelines([
#         'first\n',
#         'second'
#     ])
# with open('words.txt', 'a') as file:
#     file.writelines([
#         '1first\n',
#         '1second'
#     ])

def next_step_of_fact(a):
    b = 1
    for i in range(1, a+1):
        b *= i
        yield b
    return b

def read_line(file_name):
    with open(file_name, 'r') as file:
        for row in file.readlines():
            yield row
            print('awake')
            yield row

file = open('words.txt', 'r')
for line in file.readlines():
    print(line)
file.writelines([

])

for number in next_step_of_fact(5):
    print(number)