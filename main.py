import os
import sys
import time
from timeit import default_timer as timer

if getattr(sys, 'frozen', False):
    application_path = f"{os.path.dirname(sys.executable)}\\_internal\\"
else:
    application_path = f"{os.path.dirname(__file__)}\\"

letter_values = {'a': 1,
                 'b': 3,
                 'c': 3,
                 'd': 2,
                 'e': 1,
                 'f': 4,
                 'g': 2,
                 'h': 4,
                 'i': 1,
                 'j': 8,
                 'k': 5,
                 'l': 1,
                 'm': 3,
                 'n': 1,
                 'o': 1,
                 'p': 3,
                 'q': 10,
                 'r': 1,
                 's': 1,
                 't': 1,
                 'u': 1,
                 'v': 4,
                 'w': 4,
                 'x': 8,
                 'y': 4,
                 'z': 10}

data_path = f"{application_path}Data\\"


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def word_check(letter_split: list, hidden: bool):
    cls()
    start = timer()
    valid_words = {}
    possible_words = {}

    for word in words_list:
        correct_letter = 0
        word_temp = list(word)
        for letter in letter_split:
            if len(word_temp) <= 0:
                break
            elif letter in word_temp:
                word_temp.remove(letter)
                correct_letter += 1
        if len(word) == correct_letter:
            word_value = 0
            for letter in word:
                word_value += letter_values.get(letter)
            valid_words[word] = word_value
        elif hidden and len(word) == correct_letter + 1:
            word_value = 0
            for letter in word:
                word_value += letter_values.get(letter)
            possible_words[word] = word_value
    sorted_valid_words = sorted(valid_words.items(), key=lambda word: word[1], reverse=False)
    if hidden:
        sorted_possible_words = sorted(possible_words.items(), key=lambda word: word[1], reverse=False)
        for word in sorted_possible_words:
            print(f"{word[1]}/{len(word[0])} - {word[0]} --")
    for word in sorted_valid_words:
        print(f"{word[1]}/{len(word[0])} - {word[0]}")
    print(f"{len(words_list)}{f' vs {len(possible_words)}' if hidden else ''} vs {len(valid_words)} -- {timer() - start}")


def run():
    while True:
        try:
            fake = input("Fake Letter; Y/N\n").lower()
            cls()
            if fake in ("y", "yes"):
                fake = True
            else:
                fake = False

            hidden = input("Hidden Letter; Y/N\n").lower()
            cls()
            if hidden in ("y", "yes"):
                hidden = True
            else:
                hidden = False

            letters = input("Enter letters\n").lower()
            letter_split = list(letters)
            word_check(letter_split, hidden)
            if fake:
                letter_remove = input("Input Fake Letter\n").lower()
                try:
                    letter_split.remove(letter_remove)
                except Exception as f:
                    print(f)
                    break
                word_check(letter_split, hidden)
                while True:
                    right_fake = input("Right Fake Letter? Y/N\n").lower()
                    if right_fake in ("n", "no"):
                        next_fake = input("Input Fake Letter\n")
                        try:
                            letter_split.append(letter_remove)
                            letter_split.remove(next_fake)
                        except Exception as f:
                            print(f)
                            break
                        letter_remove = next_fake
                        word_check(letter_split, hidden)
                    else:
                        break
            if hidden:
                letter_add = input("Input Hidden Letter\n").lower()
                try:
                    letter_split.append(letter_add)
                except Exception as f:
                    print(f)
                    break
                word_check(letter_split, False)
                while True:
                    right_hidden = input("Right Hidden Letter? Y/N\n").lower()
                    if right_hidden in ("n", "no"):
                        next_hidden = input("Input Hidden Letter\n").lower()
                        try:
                            letter_split.remove(letter_add)
                            letter_split.append(next_hidden)
                        except Exception as f:
                            print(f)
                            break
                        letter_add = next_hidden
                        word_check(letter_split, False)
                    else:
                        break
            input("Press Enter For Next Round"), cls()
        except KeyboardInterrupt:
            print("Exiting program")
            break
        except Exception as e:
            print(e)
            print(letter_values)
            time.sleep(120)
            break


if __name__ == "__main__":
    try:
        with open(f"{data_path}english_91k", "r") as file:
            words = file.read()
            words_list = list(map(str, words.splitlines()))
    except FileNotFoundError:
        print(f"Word List Not Found!\nApp Path; {application_path}\nData Path; {data_path}\nFile Name; english_91k\nAll Together; {data_path}english_91k\nProgram Will Close In 90 Sec, Or Manually Close"), time.sleep(90)
        os._exit(1)
    run()
