def find_largest_word(file_path):
    try:
        large_word = ""
        for line in open(file_path, "r"):
            split_line = line.split()
            for word in split_line:
                word = word.replace(",", "").replace(".", "")
                if len(word.rstrip()) > len(large_word.rstrip()):
                    large_word = word
        return large_word, large_word[::-1]
    except IOError as e:
        print(f"\nI/O error({e.errno}): {e.strerror}")
        return e.strerror, e.__doc__
    except Exception as e:
        print(f"\nUnexpected error({e}): {e.__cause__}")
        return str(e), e.__doc__


largest_word, largest_word_reversed = find_largest_word('files/words_file1.txt')
print(f"\n LARGEST WORD: {largest_word}\nREVERSED WORD: {largest_word_reversed}")
