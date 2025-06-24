import unittest

from leafnode import LeafNode
from md_to_blocks import block_to_code_node, block_to_heading_node, block_to_ordered_list_node, block_to_paragraph_node, block_to_quote_node, block_to_unordered_list_node, markdown_to_blocks, markdown_to_html_node
from parentnode import ParentNode


class TestMdToBlocks(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.maxDiff=None

    def test_markdown_to_html_node_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph\ntext in a p\ntag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_markdown_to_html_node_code(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff</code></pre></div>",
        )

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line


- This is a list
- with items

"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_paragraph_node(self):
        block = """This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line"""
        self.assertEqual(block_to_paragraph_node(block), ParentNode("p", [
            LeafNode(None, "This is another paragraph with "),
            LeafNode("i", "italic"),
            LeafNode(None, " text and "),
            LeafNode("code", "code"),
            LeafNode(None, """ here
This is the same paragraph on a new line""")
            ]))

    def test_block_to_heading_node(self):
        block = "### Simulations"
        self.assertEqual(block_to_heading_node(block), ParentNode("h3", [LeafNode(None,"Simulations")]))

    def test_block_to_code_node(self):
        block="""```py
def fact(i):
    if i == 0:
        return 1
    return i * fact(i - 1)
def sqr(i)
    return i**2 #** exponentiates
```"""
        self.assertEqual(block_to_code_node(block),
                         ParentNode("pre", [LeafNode("code", """def fact(i):
    if i == 0:
        return 1
    return i * fact(i - 1)
def sqr(i)
    return i**2 #** exponentiates""")]))
        
    def test_block_to_unordered_list_node(self):
        block="""- first
- second -- deu
- third"""
        node = block_to_unordered_list_node(block)
        standard = ParentNode("ul", [
                             ParentNode("li", [LeafNode(None, "first")]),
                             ParentNode("li", [LeafNode(None, "second -- deu")]),
                             ParentNode("li", [LeafNode(None, "third")])
                             ])
        
        self.assertEqual(node, standard)

    def test_block_to_ordered_list_node(self):
        block="""1. first
2. second. deu
3. third"""
        node = block_to_ordered_list_node(block)
        standard = ParentNode("ol", [
                             ParentNode("li", [LeafNode(None, "first")]),
                             ParentNode("li", [LeafNode(None, "second. deu")]),
                             ParentNode("li", [LeafNode(None, "third")])
                             ])
        
        self.assertEqual(node, standard)
    
    def test_block_to_quote_node(self):
        block="""> half a league,
> half a league,
> half a league onward"""
        self.assertEqual(block_to_quote_node(block),
                         ParentNode("blockquote", [LeafNode(None, """half a league,
half a league,
half a league onward""")]))

if __name__ == "__main__":
    unittest.main()