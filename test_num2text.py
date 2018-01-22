import unittest
import num2text

class TestNum2Text(unittest.TestCase):
    """Class to test that the num2text module converts number to its string representation
    ex: 120,050 is one hundred twenty thousand fifty"""

    def test_convert(self):        
        self.assertEqual('Four', num2text.convert(4))



if __name__ == '__main__':
    unittest.main()
