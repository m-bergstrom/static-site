import unittest

from main import extract_title

class TestMain(unittest.TestCase):
    def test_extract_title_succeeds(self):
        md = """This is a markdown document

# This is the top-level heading

Here's some _slanty text_.

## This is a subheading

## Chapter 2:!

# This is another top-level heading (oops!)

Does **this** part of the document _even exist?_"""
        self.assertEqual(extract_title(md), "This is the top-level heading")

        
    def test_extract_title_no_title_fails(self):
        md = """This is a markdown document

## This is the top-level heading

Here's some _slanty text_.

### This is a subheading

### Chapter 2:!

## This is another top-level heading (oops!)

Does **this** part of the document _even exist?_"""
        with self.assertRaises(Exception) as cm:
            extract_title(md)
        return
    
if __name__ == "__main__":
    unittest.main()