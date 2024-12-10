import os
import sys
import time
from timeit import default_timer as timer

if getattr(sys, 'frozen', False):
    application_path = f"{os.path.dirname(sys.executable)}\\_internal"
else:
    application_path = os.path.dirname(__file__)

letter_values = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 0, 'k': 5, 'l': 1, 'm': 3,
                 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}


def word_check(letter_split: list, hidden: bool):
    start = timer()
    valid_words = {}
    possible_words = {}

    with open(f"{application_path}\\ref\\english_91k", "r") as file:
        words = file.read()
        words_list = list(map(str, words.splitlines()))

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
            fake = input("Fake Letter; Y/N\n")
            if fake.lower() in ("y", "yes"):
                fake = True
            else:
                fake = False

            hidden = input("Hidden Letter; Y/N\n")
            if hidden.lower() in ("y", "yes"):
                hidden = True
            else:
                hidden = False

            letters = input("Enter letters\n")
            letter_split = list(letters)
            word_check(letter_split, hidden)
            if fake:
                letter_remove = input("Input Fake Letter\n")
                try:
                    letter_split.remove(letter_remove)
                except Exception as f:
                    print(f)
                    break
                word_check(letter_split, hidden)
            if hidden:
                letter_add = input("Input Hidden Letter\n")
                try:
                    letter_split.append(letter_add)
                except Exception as f:
                    print(f)
                    break
                word_check(letter_split, False)
        except KeyboardInterrupt:
            print("Exiting program")
            break
        except Exception as e:
            print(e)
            print(letter_values)
            time.sleep(120)
            break


if __name__ == "__main__":
    run()
