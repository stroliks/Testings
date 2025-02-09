from operator import invert


def test_1():
    sum = 0
    for i in range (1, 11):
        sum += i
    assert sum == 55, "Cумма должна быть равна 55!!"

test_1()

def test_2(value):
    assert abs(-value) == -value, "Имено по заданию модкль должен быть равен -5"

test_2(-5)

def test_3(value):
    assert bin(value) == "0b101", "Бинарное выражение 5 должен быть равен 0b101"

test_3(5)

def test_4(value_1, value_2):
    assert min(value_1, value_2) == 5, "Минимум должен быть равен 10"

test_4(10,5)


def reverse(word):
    word_1 = ""
    for i in range(len(word)):
        word_1 += word[-i - 1]
    return word_1

def test_reverse(word):
    assert (word == reverse(word)), "Слово должно быть паллиндроммом"

test_reverse("abba")