import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_prop_text(self):
        text = "This is some text."
        node = TextNode(text, TextType.TEXT)
        self.assertEqual(text, node.text)

    def test_prop_text_type(self):
        text_type = TextType.CODE
        node = TextNode("text_type = TextType.CODE", text_type)
        self.assertEqual(text_type, node.text_type)

    def test_prop_url(self):
        url = "http://rinkworks.com/stupid"
        node = TextNode("Computer Stupidities!", TextType.LINK, url)
        self.assertEqual(url, node.url)

    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq_url(self):
        text = "This is a link"
        text_type = TextType.LINK
        node = TextNode(text, text_type, "http://rinkworks.com/stupid")
        node2 = TextNode(text, text_type)
        self.assertNotEqual(node, node2)

    def test_not_eq_text_type(self):
        text = "This is some text"
        node = TextNode(text, TextType.BOLD)
        node2 = TextNode(text, TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_text_node_to_html_node_PLAIN(self):
        value = "This is a(n) PLAIN node."
        text = TextNode(value, text_type=TextType.TEXT)
        html_node = text_node_to_html_node(text)
        self.assertEqual(html_node.value, value)
        self.assertEqual(html_node.tag, None)

    def test_text_node_to_html_node_BOLD(self):
        value = "This is a(n) BOLD node."
        text = TextNode(value, text_type=TextType.BOLD)
        html_node = text_node_to_html_node(text)
        self.assertEqual(html_node.value, value)
        self.assertEqual(html_node.tag, "b")

    def test_text_node_to_html_node_ITALIC(self):
        value = "This is a(n) ITALIC node."
        text = TextNode(value, text_type=TextType.ITALIC)
        html_node = text_node_to_html_node(text)
        self.assertEqual(html_node.value, value)
        self.assertEqual(html_node.tag, "i")

    def test_text_node_to_html_node_CODE(self):
        value = "This is a(n) CODE node."
        text = TextNode(value, text_type=TextType.CODE)
        html_node = text_node_to_html_node(text)
        self.assertEqual(html_node.value, value)
        self.assertEqual(html_node.tag, "code")

    def test_text_node_to_html_node_LINK(self):
        value = "This is a(n) LINK node."
        url="http://rinkworks.com/stupid"
        text = TextNode(value, text_type=TextType.LINK, url=url)
        html_node = text_node_to_html_node(text)
        self.assertEqual(html_node.value, value)
        self.assertEqual(html_node.tag, "a")
        self.assertIn("href", html_node.props)
        self.assertEqual(html_node.props["href"], url)

    def test_text_node_to_html_node_IMAGE(self):
        value = "This is a(n) IMAGE node."
        url="http://rinkworks.com/stupid/im/compbnnr.gif"
        text = TextNode(value, text_type=TextType.IMAGE, url=url)
        html_node = text_node_to_html_node(text)
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.tag, "img")
        self.assertIn("src", html_node.props)
        self.assertEqual(html_node.props["src"], url)
        self.assertIn("alt", html_node.props)
        self.assertEqual(html_node.props["alt"], value)

if __name__ == "__main__":
    unittest.main()