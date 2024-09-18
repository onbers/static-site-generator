from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, children, tag=None, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("missing tag")
        if not self.children:
            raise ValueError("missing children")
        
        return f"\n<{self.tag}>\n{self.traverse_children(self.children)}\n</{self.tag}>"

    def traverse_children(self, children):
        if not children:
            return ""

        return children[0].to_html() + self.traverse_children(children[1:])
        

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.value}, {self.children}, {self.props})"
