import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_html(self):
        node = HTMLNode('p', 'This is an html node', None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(' href="https://www.google.com" target="_blank"', node.props_to_html())

    def test_props_html_false(self):
        node = HTMLNode('p', 'This is an html node', None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertNotEqual('href="https://www.google.com" target="_blank"', node.props_to_html())

    def test_props_html_false_second(self):
        node = HTMLNode('p', 'This is an html node', None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertNotEqual(' href="https://www.google.com"target="_blank"', node.props_to_html())

    def test_repr(self):
        node = HTMLNode('p', 'This is an html node', None, '{"href": "https://www.google.com", "target": "_blank"}')
        self.assertEqual('HTMLNode(Tag: p, Value: This is an html node, Children: None, Props: {"href": "https://www.google.com", "target": "_blank"})', repr(node))