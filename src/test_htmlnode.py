import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_no_props(self):
        node = HTMLNode("p", "Testing")
        self.assertEqual(node.props_to_html(), "")

    def test_single_prop(self):
        node = HTMLNode("a", "Google", props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_multiple_props(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode("a", "Google", props=props)
        # Since dictionary order isn't guaranteed, we need to check that both props are present
        html = node.props_to_html()
        self.assertIn(' href="https://www.google.com"', html)
        self.assertIn(' target="_blank"', html)
        # Verify the total length is correct (accounting for spaces)
        self.assertEqual(len(html), len(' href="https://www.google.com" target="_blank"'))
        

if __name__ == "__main__":
    unittest.main()