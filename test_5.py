import unittest
import re
import module1

class Test_test_5(unittest.TestCase):
    def test_A(self):
        for i in module1.list_phone_сor:
            self.assertTrue((module1.author_phone(i) is not None))


if __name__ == '__main__':
    unittest.main()
