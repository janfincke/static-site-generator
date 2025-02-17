class HTMLNode:
    def __init__(self, tag, value, props=None, children=None):
        self.tag = tag
        self.value = value
        self.props = props or {}
        self.children = children or []
        

    def __str__(self):
        return f"<{self.tag} {self.props}>{''.join(map(str, self.children))}</{self.tag}>"

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.props}, {self.children})"

    def add_child(self, child):
        self.children.append(child)

    def add_prop(self, key, value):
        self.props[key] = value

    def remove_prop(self, key):
        del self.props[key]

    def remove_child(self, child):
        self.children.remove(child)

    def get_prop(self, key):
        return self.props.get(key, None)

    def get_children(self):
        return self.children

    def get_tag(self):
        return self.tag

    def set_tag(self, tag):
        self.tag = tag

    def set_props(self, props):
        self.props = props

    def set_children(self, children):
        self.children = children

    def set_prop(self, key, value):
        self.props[key] = value

    def get_prop(self, key):
        return self.props.get(key, None)
    
    def to_html(self):
        return f"<{self.tag} {self.props}>{''.join(map(str, self.children))}</{self.tag}>"
    
    def props_to_html(self):
        return ' '.join([f'{key}="{value}"' for key, value in self.props.items()])