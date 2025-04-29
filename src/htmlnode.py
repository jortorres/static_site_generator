class HTMLNode:  
    def __init__(self,tag=None,value=None,children=None,props=None): #string, string, list, dictinary
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("Subclass must for to html")
    
    def props_to_html(self):
        if not self.props:
            return ""
        new_string = ""
        for key, value in self.props.items():
            new_string += f' {key}="{value}"'
        return new_string
    
    def __repr__(self):
        return f"Tag: {self.tag} Value: {self.value} Child: {self.children} Props: {self.props}"