from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError
        if self.children == None:
            raise ValueError('Provide child tags for this tree')
        return f"<{self.tag}>{self.recurse_to_html()}</{self.tag}>"
        
    def recurse_to_html(self):
        html_string = ""
        if len(self.children) == 0:
            return html_string
        html_string = self.children[0].to_html()
        self.children = self.children[1:]
        tmp_node = html_string + self.recurse_to_html()
        return tmp_node
        
