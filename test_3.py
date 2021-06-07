import unittest
import re
import module1

class Test_test_3(unittest.TestCase):
    def test_A(self):
        for i in module1.list_mail_cor:
            self.assertTrue(module1.author_email_correct(i) is not None)


if __name__ == '__main__':
    unittest.main()
