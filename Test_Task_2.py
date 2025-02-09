

def calculate_sum(n):
    summ = 0
    for i in range (n+1):
        summ += i
    return summ

def test_zero():
    assert calculate_sum(0) == 0, "Должно быть  0"

def test_one():
    assert calculate_sum(1) == 1, "Должно быть  1"

def test_minus():
    assert calculate_sum(-5) == 0, "Должно быть  0"


def count_words(line):
    lst = line.split(" ")
    n = len(lst)
    for i in lst:
        if i == '':
            n-=1
    return n

print(count_words(""))

def test_norm():
    assert count_words("www www www www") == 4, "Результат долженб быть 4"

def test_spaces():
    assert count_words("      ") == 0, "Результат долженб быть 0"

def test_one_word():
    assert count_words("word") == 1, "Результат долженб быть 1"

def test_one_space_word():
    assert count_words(" word") == 1, "Результат долженб быть 1"

def test_one_word_space():
    assert count_words("word ") == 1, "Результат долженб быть 1"

def test_word_space_word():
    assert count_words("word word") == 2, "Результат должен быть 2"

def test_space_word_space():
    assert count_words(" word ") == 1, "Результат должен быть 1"

def test_empty():
    assert count_words("") == 0, "Результат должен быть 0"
test_norm()
test_spaces()
test_one_word()
test_one_space_word()
test_one_word_space()
test_word_space_word()
test_space_word_space()
test_empty()