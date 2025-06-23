from textnode import TextNode, TextType

def main():
    node = TextNode("dummy", TextType.LINK, "http://rinkworks.com/stupid")
    print(node)

if __name__ == "__main__":
    main()