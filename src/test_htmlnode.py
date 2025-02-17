import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_htmlnode(self):
        # Create a new HtmlNode object
        node = HTMLNode("div")
        # Add a child node
        node.add_child(HTMLNode("span"))
        # Add a child node with text
        node.add_child(HTMLNode("p", "Hello, World!"))
        # Add a child node with attributes
        node.add_child(HTMLNode("a", "Click me!", {"href": "http://example.com"}))
        # Check the HTML representation
        self.assertEqual(str(node), '<div><span></span><p>Hello, World!</p><a href="http://example.com">Click me!</a></div>')