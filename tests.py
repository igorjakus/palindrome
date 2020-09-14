from palindrome import is_palindrome
import unittest

class TestPalindrome(unittest.TestCase):

    def test_text_palindrome_1(self):
        self.assertTrue(is_palindrome('level'))

    def test_text_palindrome_2(self):
        self.assertTrue(is_palindrome('asflaksl5748w55w8475lskalfsa'))

    def test_text_not_palindrome(self):
        self.assertFalse(is_palindrome('qwerty'))

    def test_number_palindrome_1(self):
        self.assertTrue(is_palindrome(12321))

    def test_number_palindrome_2(self):
        self.assertTrue(is_palindrome(5185095686006865905815))

    def test_number_not_palindrome(self):
        self.assertFalse(is_palindrome(12345))

    def test_wrong_type_1(self):
        self.assertRaises(TypeError, is_palindrome, 5.0)

    def test_wrong_type_2(self):
        self.assertRaises(TypeError, is_palindrome, True)
    
    def test_wrong_type_3(self):
        self.assertRaises(TypeError, is_palindrome, None)
    

if __name__ == '__main__':
    unittest.main()
