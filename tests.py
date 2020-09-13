from palindrome import is_text_palindrome, is_number_palindrome
import unittest

class TestPalindrome(unittest.TestCase):

    def test_text_palindrome(self):
        
        self.assertTrue(is_text_palindrome("atok am ala ala ma kota"))
        self.assertTrue(is_text_palindrome("Kobyła ma mały bok"))
        self.assertTrue(is_text_palindrome("a b c cb a"))
        self.assertTrue(is_text_palindrome("aDa"))
        self.assertTrue(is_text_palindrome(" _"))
        
        self.assertFalse(is_text_palindrome("loret ipsum 000 _"))
        self.assertFalse(is_text_palindrome("dfejfwehg5ujgrs"))
        self.assertFalse(is_text_palindrome("Ala ma kota"))
        self.assertFalse(is_text_palindrome("45t45"))

    def test_number_palindrome(self):
        self.assertTrue(is_number_palindrome(18518509568600686590581581))
        self.assertTrue(is_number_palindrome(5812351532185))
        self.assertTrue(is_number_palindrome(1234554321))
        self.assertTrue(is_number_palindrome(2222222))
        self.assertTrue(is_number_palindrome(1537351))

        self.assertFalse(is_number_palindrome(11111111111115111111))
        self.assertFalse(is_number_palindrome(1243456788765321))
        self.assertFalse(is_number_palindrome(541414155168411))
        self.assertFalse(is_number_palindrome(54411))
        

if __name__ == '__main__':
    unittest.main()
