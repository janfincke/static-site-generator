from enum import Enum

class TextType(Enum):
    TEXT = 1
    BOLD = 2
    ITALIC = 3
    UNDERLINE = 4
    STRIKETHROUGH = 5
    CODE = 6
    LINK = 7

class TextNode:
    def __init__(self, text: str, TextType: TextType, url: str = None):
        self.text = text
        self.text_type = TextType
        self.url = url
    
    def __eq__(self, value):
        return self.text == value.text and self.text_type.value == value.text_type.value and self.url == value.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"