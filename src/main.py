from textnode import TextNode, TextType
from split_markdown_blocks import markdown_to_blocks


def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)


main()