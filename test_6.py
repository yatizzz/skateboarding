import unittest
import re
import module1

class Test_test_6(unittest.TestCase):
    def test_A(self):
        for i in module1.list_phone_uncor:
            self.assertFalse(module1.author_phone(i))

if __name__ == '__main__':
    unittest.main()
