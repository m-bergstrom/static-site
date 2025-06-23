import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.maxDiff=None

    def test_prop_tag(self):
        tag = "h2"
        node = HTMLNode(tag=tag)
        self.assertEqual(tag, node.tag)
    def test_prop_value(self):
        value = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus non lectus eu felis suscipit fringilla eget ac diam. Pellentesque non nisl gravida lacus scelerisque mollis. Vestibulum faucibus metus sed elit laoreet, at pretium lacus lobortis. Aliquam sit amet pretium metus, quis porta sem. Fusce ut ligula eleifend est dapibus fringilla. Aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc porttitor ipsum et eros malesuada hendrerit. Pellentesque condimentum venenatis commodo. Phasellus mollis sit amet nisl a mattis. Quisque vestibulum gravida lorem id ornare. Vivamus eu risus ante."
        node = HTMLNode(value=value)
        self.assertEqual(value, node.value)
    def test_prop_props(self):
        props={"href": "http://rinkworks.com/stupid",
               "title": "Computer Stupidities!"}
        node = HTMLNode(props=props)
        self.assertEqual(props, node.props)
    def test_props_to_html(self):
        props={"href": "http://rinkworks.com/stupid",
               "title": "Computer Stupidities!"}
        node = HTMLNode(props=props)
        self.assertEqual(' href="http://rinkworks.com/stupid" title="Computer Stupidities!"', node.props_to_html())
    def test_repr(self):
        node = HTMLNode("p", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec quis faucibus lectus. Donec lorem ante, sodales eu magna ultrices, fermentum cursus lacus. Vestibulum viverra erat mauris, sed commodo tortor interdum nec. Vestibulum posuere tincidunt mi, sit amet semper massa vehicula vel. Nunc vel justo suscipit, pharetra orci ullamcorper, tempus odio. Pellentesque vestibulum accumsan est, quis laoreet felis pretium ac. Quisque volutpat ex eu dui egestas, vel pretium mi facilisis. Vestibulum non magna lectus.", props={"class": "even", "style": 'display: block; font-family: "Open Sans", Arial, sans-serif; font-size: 14px; height: 80px; line-height: 20px; margin-block-end: 15px; margin-block-start: 0px; margin-bottom: 15px; margin-inline-end: 0px; margin-inline-start: 0px; margin-left: 0px; margin-right: 0px; margin-top: 0px; padding-bottom: 0px; padding-left: 0px; padding-right: 0px; padding-top: 0px; text-align: justify; text-size-adjust: 100%; unicode-bidi: isolate'})
        self.assertEqual('tag: p\nvalue: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec quis faucibus lectus. Donec lorem ante, sodales eu magna ultrices, fermentum cursus lacus. Vestibulum viverra erat mauris, sed commodo tortor interdum nec. Vestibulum posuere tincidunt mi, sit amet semper massa vehicula vel. Nunc vel justo suscipit, pharetra orci ullamcorper, tempus odio. Pellentesque vestibulum accumsan est, quis laoreet felis pretium ac. Quisque volutpat ex eu dui egestas, vel pretium mi facilisis. Vestibulum non magna lectus.\nchildren:\nprops:\n  "class": "even"\n  "style": "display: block; font-family: "Open Sans", Arial, sans-serif; font-size: 14px; height: 80px; line-height: 20px; margin-block-end: 15px; margin-block-start: 0px; margin-bottom: 15px; margin-inline-end: 0px; margin-inline-start: 0px; margin-left: 0px; margin-right: 0px; margin-top: 0px; padding-bottom: 0px; padding-left: 0px; padding-right: 0px; padding-top: 0px; text-align: justify; text-size-adjust: 100%; unicode-bidi: isolate"', str(node))

if __name__ == "__main__":
    unittest.main()