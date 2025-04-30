"""
LeafNode is a type of HTMLNode that 
represents a single HTML tag with no children, We call it a "leaf" node because
it's a "leaf" in the tree of HTML nodes. It's a node with no children.
THIS IS THE UNITTEST FOR LEAFNODE.PY
"""

import unittest
from leafnode import *

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p","Hello, world!")
        self.assertEqual(node.to_html(),"<p>Hello, world!</p>")

    def test_lead_link(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(),'<a href="https://www.google.com">Click me!</a>')
    
    def test_empty_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_tag_none(self):
        node = LeafNode(None, "Hello world")
        self.assertEqual(node.to_html(),"Hello world")

    def test_multiple_attributes(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = LeafNode("a", "Click me!", props)
        html = node.to_html() 
        self.assertIn('href="https://www.google.com"', html)
        self.assertIn('target="_blank"', html)

    def test_different_tag_types(self):
        tags = ["h1", "div", "span", "li"]  #list of tags
        for tag in tags:  # loop to check tags if they are equal
            node = LeafNode(tag, "Content")
            self.assertEqual(node.to_html(), f"<{tag}>Content</{tag}>")

    
     
if __name__ == "__main__":
    unittest.main()