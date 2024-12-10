# This was used to reduce the wordlist I have from 194,390 words to just 91,059 (valid between and including 4-8 length)
from timeit import default_timer as timer
start = timer()
new_word_list = []
with open("ref/english", "r") as file:
    words = file.read()
    word_list = list(map(str, words.splitlines()))

for word in word_list:
    if 4 <= len(word) <= 8:
        new_word_list.append(word)

with open("ref/test_english", "w") as new_file:
    for new_word in new_word_list:
        new_file.write(f"{new_word}\n")
print(f"{len(word_list):,} words to {len(new_word_list):,} words -- {timer() - start}")
