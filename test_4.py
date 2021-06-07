import unittest
import re
import module1

class Test_test_4(unittest.TestCase):
    def test_A(self):
        for j in module1.list_mail_uncor:
            self.assertFalse((module1.author_email_correct(j)))

if __name__ == '__main__':
    unittest.main()
