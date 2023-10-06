# from _pytest.monkeypatch import monkeypatch
from sum_pairs import sum_pairs

def test_pad_array():
    assert sum_pairs([1,2,3,4,5], 9) == [[4,5]]
    assert sum_pairs([1,2,3,4,5], 7) == [[2,5], [3,4]]
    assert sum_pairs([7, 0, 1, 6], 7) == [[7,0], [1, 6]]
    assert sum_pairs([3, 1, 5, 8, 2], 27) == 'unable to find pairs'


# def userInput():
#     temp = input("")
#     return temp

# def test_say_hello(monkeypatch):
#     monkeypatch.setattr('builtins.input', lambda _: "Pavol")
#     assert userInput() == "Pavol"

