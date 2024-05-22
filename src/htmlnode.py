class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ""
        dict_string = " "
        for key, val in self.props.items():
            dict_string += f'{key}="{val}" '
        return dict_string.rstrip()

    def __repr__(self):
        return f"HTMLNode(Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Props: {self.props})"