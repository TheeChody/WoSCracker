# This was used to reduce the wordlist I have from 194,390 words to just 91,059 (valid between and including 4-8 length)
import os
import sys
import time
import random
from pathlib import Path
from timeit import default_timer as timer

if getattr(sys, 'frozen', False):
    application_path = f"{os.path.dirname(sys.executable)}\\"
else:
    application_path = f"{os.path.dirname(__file__)}\\"

data_path = f"{application_path}Data\\"
Path(data_path).mkdir(parents=True, exist_ok=True)

illegal_chars = ("#", "%", "&", "{", "}", "\\", "<", ">", "*", "?", "/", "$", "!", "'", '"', ":", "@", "+", "`", "|", "=")

while True:
    try:
        flagged_letter = None
        new_word_str = ""

        word_file = input("Enter the word list filename (with extension if any)\n")

        start = timer()
        for letter in word_file:
            if letter in illegal_chars:
                flagged_letter = letter
                break

        if word_file == "" or flagged_letter is not None:
            print(f"Please enter a valid filename -- {flagged_letter if word_file != '' else 'NULL'} is not valid")
        else:
            with open(f"{data_path}{word_file}", "r") as file:
                words = file.read()

            for word in words.splitlines():
                if 4 <= len(word) <= 8:
                    if new_word_str == "":
                        new_word_str += word
                    else:
                        new_word_str += f"\n{word}"

            with open(f"{data_path}{word_file}_new", "w") as new_file:
                new_file.write(new_word_str)

            word_list_length = len(new_word_str.splitlines())
            new_filename = f"{word_file}_{word_list_length:,}"

            if os.path.exists(f"{data_path}{new_filename}"):
                new_filename += f"---{random.randint(0, 5)}{random.randint(0, 1000)}"

            os.rename(f"{data_path}{word_file}_new", f"{data_path}{new_filename}")
            print(f"{len(words.splitlines()):,} words to {word_list_length:,} words -- {timer() - start}")
    except KeyboardInterrupt:
        print(f"Exiting program...")
        break
    except FileNotFoundError:
        print(f"Please enter a valid filename/make sure your source wordlist is in the 'Data' folder"), time.sleep(2)
        pass
    except FileExistsError:
        print(f"File still Exists somehow, random logic failed me... Should still exist as 'filename'_new")
        pass
    except Exception as e:
        print(f"Error occurred -- {e}")
        break
