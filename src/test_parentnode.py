import unittest

from ParentNode import *
from leafnode import *


class testParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
    )
    def test_to_html_with_none(self):
        child_node = LeafNode(None,None)
        parent_node = ParentNode("div", [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    def test_to_html_with_none_tag(self):
        child_node = LeafNode(None,None)
        parent_node = ParentNode(None,[child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    def test_to_html_props(self):  # Add self parameter
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], props)
        expected = '<div href="https://www.google.com" target="_blank"><span>child</span></div>'
        self.assertEqual(parent_node.to_html(), expected)

    def test_empty_children_list(self):
        child_node = LeafNode()




if __name__ == "__main__":
    unittest.main()