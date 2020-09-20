import pytest

from python.test_part1.find_largest_word import find_largest_word


# if you use the IDE to run the test, please set the working directory to the root path of the repo (test_secureworks)
# to make it to work in your IDE and in the terminal with the same code

@pytest.mark.positive
def test_read_valid_existing_file_one_word_per_line():
    largest_word, largest_word_reversed = find_largest_word(file_path="python/test_part1/files/words_file1.txt")
    print(f"\n LARGEST WORD: {largest_word}\nREVERSED WORD: {largest_word_reversed}")
    assert largest_word == 'abcde', "The largest word is not the expected!!"
    assert largest_word_reversed == 'edcba', "The largest word is not the expected!!"


@pytest.mark.positive
def test_read_valid_existing_file_multiple_words_one_line():
    largest_word, largest_word_reversed = find_largest_word(file_path="python/test_part1/files/words_file2.txt")
    print(f"\n LARGEST WORD: {largest_word}\nREVERSED WORD: {largest_word_reversed}")
    assert largest_word == 'secure_works', "The largest word is not the expected!!"
    assert largest_word_reversed == 'skrow_eruces', "The largest word is not the expected!!"


@pytest.mark.positive
def test_read_valid_existing_file_multiple_words_multiple_lines():
    largest_word, largest_word_reversed = find_largest_word(file_path="python/test_part1/files/words_file3.txt")
    print(f"\n LARGEST WORD: {largest_word}\nREVERSED WORD: {largest_word_reversed}")
    assert largest_word == 'aeiou_aeiou_aeiou', "The largest word is not the expected!!"
    assert largest_word_reversed == 'uoiea_uoiea_uoiea', "The largest word is not the expected!!"


@pytest.mark.positive
def test_read_valid_existing_file_multiple_numbers_multiple_lines():
    largest_word, largest_word_reversed = find_largest_word(file_path="python/test_part1/files/words_file4.txt")
    print(f"\n LARGEST WORD: {largest_word}\nREVERSED WORD: {largest_word_reversed}")
    assert largest_word == '12345678901234567890', "The largest word is not the expected!!"
    assert largest_word_reversed == '09876543210987654321', "The largest word is not the expected!!"


@pytest.mark.negative
def test_read_non_existing_file():
    strerror, error_doc = find_largest_word(file_path="invalid_path")
    print(f"\nError handled: {strerror}\nError handled: {error_doc}")
    assert strerror == 'No such file or directory', "The expected 'strerror' message is not the expected"
    assert error_doc == 'File not found.', "The expected 'error_doc' message is not the expected"


@pytest.mark.negative
def test_read_invalid_file_format():
    strerror, error_doc = find_largest_word(file_path="python/test_part1/files/pytest.png")
    print(f"\nError handled: {strerror}\nError handled: {error_doc}")
    assert strerror == '\'utf-8\' codec can\'t decode byte 0x89 in position 0: invalid start byte', \
        "The expected 'strerror' message is not the expected"
    assert error_doc == 'Unicode decoding error.', "The expected 'error_doc' message is not the expected"


@pytest.mark.negative
def test_read_corrupted_file():
    strerror, error_doc = find_largest_word(file_path="python/test_part1/files/words_file1_corrupted.txt")
    print(f"\nError handled: {strerror}\nError handled: {error_doc}")
    assert error_doc == 'Unicode decoding error.', "The expected 'error_doc' message is not the expected"


@pytest.mark.negative
def test_read_empty_file():
    largest_word, largest_word_reversed = find_largest_word(file_path="python/test_part1/files/words_file5.txt")
    print(f"\n LARGEST WORD: {largest_word}\nREVERSED WORD: {largest_word_reversed}")
    assert largest_word == '', "The largest word is not the expected!! It should be empty."
    assert largest_word_reversed == '', "The largest word reversed is not the expected!! It should be empty."
    assert len(largest_word) == 0, "The largest word length should be 0!!"
    assert len(largest_word_reversed) == 0, "The largest word reversed length should be 0!!"
