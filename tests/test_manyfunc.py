from src.manyfunc import *

def test_factorial():
    assert factorial(0) == 1
    assert factorial(4) == 24

def test_word_occurence_in_string():
    assert count_word_occurence_in_string("three", "one") == 0
    assert count_word_occurence_in_string("one two one", "one") == 2
