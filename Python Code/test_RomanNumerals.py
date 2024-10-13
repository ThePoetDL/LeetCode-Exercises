from  RomanNumerals import solution

s = solution()

def test_romanToInt():
    assert s.romanToInt('III') == 3
    assert s.romanToInt('IV') == 4
    assert s.romanToInt('V') == 5
    assert s.romanToInt('VI') == 6
    assert s.romanToInt('XV') == 15
    assert s.romanToInt('LVIII') == 58
    assert s.romanToInt('MCMXCIV') == 1994
