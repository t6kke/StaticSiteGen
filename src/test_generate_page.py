import unittest
from generate_page import extract_title

class TestExtractTitle(unittest.TestCase):
    # boot.dev tests
    def test_eq(self):
        actual = extract_title("# This is a title")
        self.assertEqual(actual, "This is a title")


    # my tests
    def test_title_eq(self):
        self.assertEqual(extract_title("# Title\n\nsome more text\n\nending"), "Title")

    def test_title_exeption(self):
        self.assertRaises(Exception, extract_title, " bad title \n\nsome more text\n\nending")



if __name__ == "__main__":
    unittest.main()