"""

1. игрок №1 загадывает слово
2. Программа выводит это слово при этом неизвестные буквы заменяются на _, а угаданные выводятся
3. игрок №2 вводит по одной букве
4. если буква в слове нет, то игроку №2 начисляется штрафное очко
5. если штрафных очков набралось болше 10 - игрок №2 проиграл
6. игрок №2 выиграл если угадал все буквы в слове

если в слове есть одинаковые буквы, то при угадывании открываются все имеющиеся экземпляры


print(list())
print("".index('a'))
"""

"""
1. ввод слов из файла words.txt readline
2. ввод символов из файла chars.txt read(1)
3. весь вывод (вместо print) пишем в файл log.txt writelines
"""

print_word = input('Загадайте слово:').lower() #п1
chars = list(print_word)
count_of_chars = len(chars)
life = 3
guess_chars = ['_' for i in range(count_of_chars)]

while True:
    print('life count ', life) #п3
    print(' '.join(guess_chars)) #п3
    char_of_word = input('Enter char:').lower() #п2
    print('Input char', char_of_word) #п3
    if char_of_word in chars:
        for i, c in enumerate(chars):
            if c == char_of_word:
                guess_chars[i] = char_of_word
    else:
        life -= 1
    if '_' not in guess_chars:
        print('You win') #п3
        break
    elif life == 0:
        print('You lose') #п3
        break

