
file_name = "DATA/words.txt"
search_word = "sword"

with open(file_name) as words_in:
    for raw_line in words_in:
        if search_word in raw_line:
            line = raw_line.rstrip()
            print(line)
print('-' * 60)

count = 0
letter = 's'
with open(file_name) as words_in:  # open file and get file object
    for raw_line in words_in:    # iterate over lines (including \n)
        word = raw_line.rstrip()   # remove \n
        # if word[-1] == letter:
        if word.endswith(letter):  # our test
            count += 1             # increment count
print(f"{count} words end with  {letter}")
