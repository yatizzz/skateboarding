import unittest
import re
import module1

class Test_test_2(unittest.TestCase):
    def test_A(self):
        for i in module1.list_data_uncor:
            self.assertFalse(module1.written_date_correct(i))


if __name__ == '__main__':
    unittest.main()
