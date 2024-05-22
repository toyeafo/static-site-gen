import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_props_html(self):
        node = LeafNode('p', 'This is a leaf node.')
        self.assertEqual('<p>This is a leaf node.</p>', node.to_html())

    def test_tag_html(self):
        node = LeafNode(None, 'This is a leaf node.')
        self.assertEqual('This is a leaf node.', node.to_html())

    def test_props_html_false(self):
        node = LeafNode('a', 'Click my node!', {"href": "https://www.google.com"})
        self.assertEqual('<a href="https://www.google.com">Click my node!</a>', node.to_html())