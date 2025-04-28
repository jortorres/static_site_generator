from textnode import *

def main():
    print("Hello World")
    
    new_text_node = TextNode("This is some anchor text",TextType.LINKS, "https://www.boot.dev")
    print(new_text_node)


main()
