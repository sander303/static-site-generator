from textnode import TextNode, TextType

def main():
    testnode = TextNode("test text", TextType.LINK, "https://www.boot.dev")
    print(testnode)

main()