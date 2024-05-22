import unittest

from parentnode import ParentNode
from leafnode import LeafNode
from htmlnode import HTMLNode

from block_level import (
    markdown_to_blocks, 
    markdown_to_html,
    block_to_block_type,
    block_type_paragraph,
    block_type_code,
    block_type_heading,
    block_type_ordered_list,
    block_type_unordered_list,
    block_type_quote,
    heading_block_type_to_html_node,
    quote_block_type_to_html_node,
    code_to_html_node,
    ordered_list_to_html_node,
    unordered_list_to_html_node,
    paragraph_to_html_node
)

class TestBlockLevel(unittest.TestCase):
    
    def test_markdown_to_blocks(self):
        md = """This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        result = [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ]
        self.assertEqual(result, markdown_to_blocks(md))

    def test_markdown_to_blocks_newline(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        result = [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ]
        self.assertEqual(result, markdown_to_blocks(md))

    def test_block_to_block_type_unordered(self):
        block = "* This is a list\n* with items"
        self.assertEqual(block_type_unordered_list, block_to_block_type(block))

    def test_block_to_block_type_ordered(self):
        block = "1. This is a list\n24. with items"
        self.assertEqual(block_type_ordered_list, block_to_block_type(block))

    def test_block_to_block_type_heading(self):
        block = "# This is a heading"
        self.assertEqual(block_type_heading, block_to_block_type(block))

    def test_block_to_block_type_quote(self):
        block = "> quote\n> more quote"
        self.assertEqual(block_type_quote, block_to_block_type(block))

    def test_block_to_block_type_code(self):
        block = "``` This is a list\ncode\n```"
        self.assertEqual(block_type_code, block_to_block_type(block))

    def test_block_to_block_type_paragraph(self):
        block = "This is a paragraph of text. It has some **bold** and *italic* words inside of it."
        self.assertEqual(block_type_paragraph, block_to_block_type(block))

    def test_block_to_html_node_heading(self):
        text = "## Table of Contents"
        self.assertEqual("<h2>Table of Contents</h2>", heading_block_type_to_html_node(text).to_html())

    def test_block_to_html_node_quote(self):
        text = "> This is the first line of a quote.\n> This is the second line of the same quote."
        self.assertEqual("<blockquote>This is the first line of a quote. This is the second line of the same quote.</blockquote>", quote_block_type_to_html_node(text).to_html())

    def test_block_to_html_node_ordered_list(self):
        text = "1. This is an `ordered` list\n2. with items\n3. and more items"
        self.assertEqual("<ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol>", ordered_list_to_html_node(text).to_html())

    def test_block_to_html_node_unordered_list(self):
        text = "- This is an `ordered` list\n- with items\n- and *more* items"
        self.assertEqual("<ul><li>This is an <code>ordered</code> list</li><li>with items</li><li>and <i>more</i> items</li></ul>", unordered_list_to_html_node(text).to_html())

    def test_block_to_html_node_code(self):
        text = "```This is text with a `code block` word```"
        self.assertEqual("<pre><code>This is text with a <code>code block</code> word</code></pre>", code_to_html_node(text).to_html())

    def test_block_to_html_node_paragraph(self):
        pass

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )