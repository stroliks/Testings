

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

print(count_words("www www ttt uuu "))

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


# №3

def is_number(string):
    try:
        int(string)
    except ValueError:
        return False
    return True

print(is_number('0x9'))
print(is_number('568'))

def test_num():
    assert is_number('568') == True, "Результат должен быть True"

def test_string():
    assert is_number('abc') == False, "Результат должен быть False"

def test_string_num():
    assert is_number('0x9g5') == False, "Результат должен быть False"

def test_empty():
    assert is_number('') == False, "Результат должен быть False"

def test_space():
    assert is_number(' ') == False, "Результат должен быть False"

test_num()
test_string()
test_string_num()
test_empty()
test_space()

# №4

def unique(lst):
    new_lst = []
    for i in range(len(lst)):
        if lst[i] not in new_lst:
            new_lst.append(lst[i])
    return new_lst

print(unique([1,2,3,3,2,1,5,9,8,8,9,6,6,1,4,8,7]))

def test_empty():
    assert unique([]) == [], "Результат должен быть []"

def test_many_1():
    assert unique([1,1,1,1]) == [1], "Результат должен быть [1]"

def test_simple():
    assert unique([1,2,3,3,2,1,5,9,8,8,9,6,6,1,4,8,7]) == [1, 2, 3, 5, 9, 8, 6, 4, 7], "Результат должен быть [1, 2, 3, 5, 9, 8, 6, 4, 7]"

def test_one_value():
    assert unique([3]) == [3], "Результат должен быть [3]"

test_empty()
test_many_1()
