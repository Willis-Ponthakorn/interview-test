import unittest

def intToRoman(num: int):
    try:
        val = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syb = [ 'M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        roman = ''
        i = 0
        while num > 0:
            for x in range(num // val[i]):
                roman += syb[i]
                num -= val[i]
            i +=1
        return roman
    except:
        return 'Value Invaild'

class TestIntegerToRoman(unittest.TestCase):
    #test case from problem
    def test_integer_to_roman_success1(self):
        actual = intToRoman(3)
        expected = "III"
        self.assertEqual(actual,expected)

    #test case from problem
    def test_integer_to_roman_success2(self):
        actual = intToRoman(58)
        expected = "LVIII"
        self.assertEqual(actual,expected)

    #test case from problem
    def test_integer_to_roman_success3(self):
        actual = intToRoman(1994)
        expected = "MCMXCIV"
        self.assertEqual(actual,expected)

    def test_integer_to_roman_fail_by_input_not_integer(self):
        actual = intToRoman('A')
        expected = 'Value Invaild'
        self.assertEqual(actual,expected)

unittest.main()