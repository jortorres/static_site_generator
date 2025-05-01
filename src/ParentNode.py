'''
Our new ParentNode class will handle the nesting of HTML
nodes inside of one another. Any HTML node that's not "leaf" node
(i.e. it has children) is a "parent" node.
'''

from htmlnode import *

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Requires HTML tag for ParentNode")
        if not self.children:
            raise ValueError("Requires a children node ")

        props_str = self.props_to_html()
        opening_tag = f'<{self.tag}{props_str}>'
        
        new_string = ""
        for child in self.children:
            new_string += child.to_html()
        
        return opening_tag + new_string + f'</{self.tag}>'
        
        
        
