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
найти и выделить в функции осмысленные участки кода
использвать эти функции
"""


class Life:
    def __init__(self, life=3):
        self.life = life

    def is_dead(self):
        return self.life == 0

    def do_damage(self):
        self.life -= 1

    def show(self):
        print('life count ', self.life)

class Word:
    def __init__(self, word):
        self.chars = list(word)
        count_of_chars = len(self.chars)
        self.guess_chars = ['_' for i in range(count_of_chars)]

    def show_guess_chars(self):
        print(' '.join(self.guess_chars))

    def fill_chars(self, char_of_word):
        for i, c in enumerate(self.chars):
            if c == char_of_word:
                self.guess_chars[i] = char_of_word

    def is_complete(self):
        return '_' not in self.guess_chars

    def in_word(self, char):
        return char in self.chars

class Game:
    def __init__(self, word:Word, life:Life):
        self.word = word
        self.life = life

    def main_loop(self):
        while True:
            self.word.show_guess_chars()
            self.life.show()
            char_of_word = input_chars()
            if self.word.in_word(char_of_word):
                self.word.fill_chars(char_of_word)
            else:
                self.life.do_damage()
            if self.word.is_complete():
                print('You win')  # п3
                break
            if self.life.is_dead():
                print('You lose')  # п3
                break

def input_words():
    with open('words.txt', 'r') as word_file:
        return word_file.readline().lower().rstrip('\n')

    # return input('Загадайте слово:').lower()

def input_chars():
    cout = input('Enter char:').lower()
    print('Input char', cout)
    return cout

if __name__ == '__main__':
    word = Word(input_words())
    life = Life(3)
    Game(word, life).main_loop()
