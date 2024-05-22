import unittest

from textnode import TextNode, text_type_text, text_type_bold, text_type_italic, text_type_code, text_type_link
from leafnode import LeafNode

class TextNodeTest(unittest.TestCase):
    def test_eq(self):
        node = TextNode('This is a text node', 'bold')
        node2 = TextNode('This is a text node', 'bold')
        self.assertEqual(node, node2)

    def test_noeq(self):
        node = TextNode('This is a text node', 'italic')
        node2 = TextNode('This is a text node', 'bold')
        self.assertNotEqual(node, node2)
    
    def test_noeq_false(self):
        node = TextNode('This is a text node', 'italic')
        node2 = TextNode('This is a text node 2', 'italic')
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode('This is a text node', 'bold', 'https://boot.dev')
        node2 = TextNode('This is a text node', 'bold', 'https://boot.dev')
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode('This is a text node', 'bold', 'https://boot.dev')
        self.assertEqual('TextNode(This is a text node, bold, https://boot.dev)', repr(node))

    def test_to_html_node(self):
        node = TextNode('Click my node!', 'link', 'https://www.google.com')
        self.assertEqual('<a href="https://www.google.com">Click my node!</a>', node.text_node_to_html_node().to_html())


if __name__=="__main__":
    unittest.main()