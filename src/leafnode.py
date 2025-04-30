"""
LeafNode is a type of HTMLNode that 
represents a single HTML tag with no children, We call it a "leaf" node because
it's a "leaf" in the tree of HTML nodes. It's a node with no children.
"""

from htmlnode import *

class LeafNode(HTMLNode):
    def __init__(self, tag = None, value = None , props=None):
        super().__init__(tag, value, None, props)


    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value")
        if not self.tag:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
