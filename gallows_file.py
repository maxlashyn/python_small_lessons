"""
1. ввод слов из файла words.txt readline
2. ввод символов из файла chars.txt read(1)
3. весь вывод (вместо print) пишем в файл log.txt writelines
"""

with open('words.txt', 'r') as word_file:
    with open('chars.txt', 'r') as char_file:
        with open('log.txt', 'w') as log_file:
            for print_word in word_file.readlines():
                print_word = print_word.lower().rstrip('\n') #п1
                chars = list(print_word)
                count_of_chars = len(chars)
                life = 3
                guess_chars = ['_' for i in range(count_of_chars)]

                while True:
                    char_of_word = char_file.read(1)

                    if len(char_of_word) == 0:
                        out = ['закончились буквы\n']
                        break

                    out = [
                        'life count %s\n' % life,
                        ' '.join(guess_chars),
                        '\n'
                    ]
                    char_of_word = char_of_word.lower() #п2
                    out.append('Input char %s\n' % char_of_word) #п3
                    if char_of_word in chars:
                        for i, c in enumerate(chars):
                            if c == char_of_word:
                                guess_chars[i] = char_of_word
                    else:
                        life -= 1
                    if '_' not in guess_chars:
                        out.append('You win\n') #п3
                        break
                    elif life == 0:
                        out.append('You lose\n') #п3
                        break
                    log_file.writelines(out)
                log_file.writelines(out)

