import unittest

class TestString(unittest.TestCase):
     def setUp(self):
         pass

     def test_string_length(self):
         self.assertEqual(len('Hello World'), 11)

if __name__ == '__main__':
    unittest.main()
