import unittest

from md_to_html_functions import extract_markdown_images, extract_markdown_links, split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes
from textnode import TextNode, TextType

class TestMdToHTMLFunctions(unittest.TestCase):
    def test_split_nodes_delimiter_uneven(self):
        text = r"This is a **bold statement."
        start_node = TextNode(text, text_type=TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([start_node], "**", TextType.BOLD)

    def test_split_nodes_delimiter_single(self):
        text = r"This is a **bold** statement."
        start_node = TextNode(text, text_type=TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([start_node], "**", TextType.BOLD),
                         [TextNode("This is a ", TextType.TEXT),
                          TextNode("bold", TextType.BOLD),
                          TextNode(" statement.", TextType.TEXT)])

    def test_split_nodes_delimiter_multiple_end(self):
        text = r"This is one **bold** statement after **another.**"
        start_node = TextNode(text, text_type=TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([start_node], "**", TextType.BOLD),
                         [TextNode("This is one ", TextType.TEXT),
                          TextNode("bold", TextType.BOLD),
                          TextNode(" statement after ", TextType.TEXT),
                          TextNode("another.", TextType.BOLD)])

    def test_split_nodes_delimiter_code(self):
        text = r"`This is a code block`"
        start_node = TextNode(text, text_type=TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([start_node], "`", TextType.CODE),
                         [TextNode("This is a code block", TextType.CODE)])
        
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link to [Computer Stupidities!](http://rinkworks.com/stupid)"
        )
        self.assertListEqual([("Computer Stupidities!", "http://rinkworks.com/stupid")], matches)
        
    def test_extract_markdown_images_and_links(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a link to [Computer Stupidities!](http://rinkworks.com/stupid)"
        image_matches = extract_markdown_images(text)
        link_matches = extract_markdown_links(text)
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], image_matches)
        self.assertListEqual([("Computer Stupidities!", "http://rinkworks.com/stupid")], link_matches)

    def test_split_nodes_image(self):
        node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT)
        self.assertListEqual(split_nodes_image([node]),
                             [
                                 TextNode("This is text with an ", TextType.TEXT),
                                 TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")
                             ])
    
    def test_split_nodes_link(self):
        node = TextNode("This is text with a link to [Computer Stupidities!](http://rinkworks.com/stupid)", TextType.TEXT)
        self.assertListEqual(split_nodes_link([node]),
                             [
                                 TextNode("This is text with a link to ", TextType.TEXT),
                                 TextNode("Computer Stupidities!", TextType.LINK, "http://rinkworks.com/stupid")
                             ])

    def test_split_nodes_images(self):
        node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)!", TextType.TEXT)
        self.assertListEqual(split_nodes_image([node]),
                             [
                                 TextNode("This is text with an ", TextType.TEXT),
                                 TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                                 TextNode(" and another ", TextType.TEXT),
                                 TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                                 TextNode("!", TextType.TEXT)
                             ])
    
    def test_split_nodes_links(self):
        node = TextNode("This is text with a link to [Computer Stupidities!](http://rinkworks.com/stupid) and [to boot dev](https://www.boot.dev)!", TextType.TEXT)
        self.assertListEqual(split_nodes_link([node]),
                             [
                                 TextNode("This is text with a link to ", TextType.TEXT),
                                 TextNode("Computer Stupidities!", TextType.LINK, "http://rinkworks.com/stupid"),
                                 TextNode(" and ", TextType.TEXT),
                                 TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                                 TextNode("!", TextType.TEXT)
                             ])
        
    def test_split_nodes_image_and_link(self):
        node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a link to [Computer Stupidities!](http://rinkworks.com/stupid)", TextType.TEXT)
        self.assertListEqual(split_nodes_image(split_nodes_link([node])),split_nodes_link(split_nodes_image([node])))
        self.assertListEqual(split_nodes_image(split_nodes_link([node])),
                             [
                                 TextNode("This is text with an ", TextType.TEXT),
                                 TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                                 TextNode(" and a link to ", TextType.TEXT),
                                 TextNode("Computer Stupidities!", TextType.LINK, "http://rinkworks.com/stupid")
                             ])
        
    def test_split_nodes_images_and_links(self):
        node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a link to [Computer Stupidities!](http://rinkworks.com/stupid) and another ![second image](https://i.imgur.com/3elNhQu.png) and a second link [to boot dev](https://www.boot.dev)", TextType.TEXT)
        self.assertListEqual(split_nodes_image(split_nodes_link([node])),split_nodes_link(split_nodes_image([node])))
        self.assertListEqual(split_nodes_image(split_nodes_link([node])),
                             [
                                 TextNode("This is text with an ", TextType.TEXT),
                                 TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                                 TextNode(" and a link to ", TextType.TEXT),
                                 TextNode("Computer Stupidities!", TextType.LINK, "http://rinkworks.com/stupid"),
                                 TextNode(" and another ", TextType.TEXT), 
                                 TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                                 TextNode(" and a second link ", TextType.TEXT), 
                                 TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                             ])
    
    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.assertListEqual(text_to_textnodes(text),
                             [
                                 TextNode("This is ", TextType.TEXT),
                                 TextNode("text", TextType.BOLD),
                                 TextNode(" with an ", TextType.TEXT),
                                 TextNode("italic", TextType.ITALIC),
                                 TextNode(" word and a ", TextType.TEXT),
                                 TextNode("code block", TextType.CODE),
                                 TextNode(" and an ", TextType.TEXT),
                                 TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                                 TextNode(" and a ", TextType.TEXT),
                                 TextNode("link", TextType.LINK, "https://boot.dev"),
                             ])

if __name__ == "__main__":
    unittest.main()