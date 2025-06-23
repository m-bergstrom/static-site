import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Computer Stupidities!", {"href": "http://rinkworks.com/stupid"})
        self.assertEqual('<a href="http://rinkworks.com/stupid">Computer Stupidities!</a>', node.to_html())
    def test_leaf_to_html_no_value(self):
        node = LeafNode(tag="p", value=None)
        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()