import unittest

from blocktype import block_to_block_type, BlockType

class TestBlocktype(unittest.TestCase):
    def test_blocktype_heading(self):
        block = """# Indigo

"""
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

        block = """## Indigo

"""
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

        block = """# 3. Indigo

"""
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)


    def test_blocktype_non_heading(self):
        block = """####### Indigo"""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        block = """Indigo
##### Blue
"""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_blocktype_code_block(self):
        block = """```
<>!*''#
```"""
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_blocktype_non_code_block(self):
        block = """<>!*''#
```"""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        block = """```
<>!*''#"""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_blocktype_quote_block(self):
        block = """> Half a league,
> half a league,
> half a league onward"""
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_blocktype_non_quote_block(self):
        block = """> Half a league,
 half a league,
> half a league onward"""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_blocktype_unordered_list(self):
        block = """- green
- pink
- yellow"""
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_blocktype_non_unordered_list(self):
        block = """- green
 pink
- yellow"""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_blocktype_ordered_list(self):
        block = """1. Step 1
2. Step 2
3. Step 3
4. Profit!"""
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_blocktype_non_ordered_list(self):
        block = """1. Step 1
 Step 2
3. Step 3
4. Profit!"""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        block = """1. Step 1
1. Step 2
3. Step 3
4. Profit!"""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()