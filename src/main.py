from textnode import *
from split_nodes_delim import *
from extract_markdown_img import *

def main():
    print("Hello World")
    
    new_text_node = TextNode("This is text with a `code block` word", TextType.TEXT)
    print(new_text_node)

    #new_nodes = split_nodes_delimiter([new_text_node], "`", TextType.CODE)
    #print(f"Main file: {new_nodes}")

    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_images(text))
    # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

    text1 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    print(extract_markdown_links(text1))
    # [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]




main()
