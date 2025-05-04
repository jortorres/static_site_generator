from textnode import *
from split_nodes_delim import *

def main():
    print("Hello World")
    
    new_text_node = TextNode("This is text with a `code block` word", TextType.TEXT)
    print(new_text_node)

    new_nodes = split_nodes_delimiter([new_text_node], "`", TextType.CODE)
    print(f"Main file: {new_nodes}")


main()
