# import unittest

# class TestStringMethods(unittest.TestCase):

#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')

#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())

#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split('.')

# if __name__ == '__main__':
#     unittest.main()

import unittest



def to_upper(value): 
    if not value:
        raise ValueError('Value cannot be empty') 
    return value.upper()

class TestToUpper(unittest.TestCase):

    def test_to_upper(self):
        with self.assertRaises(ValueError):
            to_upper('')

if __name__ =='__main__':
    unittest.main()