from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for old_node in old_nodes:
        # Skip non-TEXT nodes
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
            
        text = old_node.text
        
        # If no delimiter is found, just add the original node
        if delimiter not in text:
            new_nodes.append(old_node)
            continue
        
        # Process the text by looking for delimiters
        segments = text.split(delimiter)
        
        # Process each segment
        for i in range(len(segments)):
            segment = segments[i]
            
            # First segment is always TEXT
            if i == 0:
                new_nodes.append(TextNode(segment, TextType.TEXT))
                continue
                
            # Odd-indexed segments are delimited content (CODE)
            if i % 2 == 1:
                new_nodes.append(TextNode(segment, text_type))
            # Even-indexed segments (except the first) are regular TEXT
            else:
                new_nodes.append(TextNode(segment, TextType.TEXT))
    
    return new_nodes