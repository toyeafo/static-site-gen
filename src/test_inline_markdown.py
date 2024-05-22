from inline_markdown import (
    split_nodes_delimiter, 
    extract_markdown_images, 
    extract_markdown_links, 
    split_nodes_image, 
    split_nodes_link,
    text_to_textnodes)

import unittest
from textnode import (
    TextNode, 
    text_type_text, 
    text_type_bold, 
    text_type_italic, 
    text_type_code, 
    text_type_link, 
    text_type_image, 
    text_type_link,)

class TestNodeExtraction(unittest.TestCase):

    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", "text")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        self.assertListEqual(new_nodes, [
    TextNode("This is text with a ", "text"),
    TextNode("code block", "code"),
    TextNode(" word", "text"),
])

    def test_split_nodes_delimiter_bold(self):
        node = TextNode("This is text with a **code block** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(new_nodes, [
    TextNode("This is text with a ", text_type_text),
    TextNode("code block", text_type_bold),
    TextNode(" word", text_type_text),
])

    def test_split_nodes_delimiter_italic(self):
        node = TextNode("This is text with a *code block* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(new_nodes, [
    TextNode("This is text with a ", text_type_text),
    TextNode("code block", text_type_italic),
    TextNode(" word", text_type_text),
])

    def test_split_nodes_delimiter_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_extract_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        result_list = [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]
        self.assertListEqual(result_list, extract_markdown_images(text))

    def test_extract_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        result_list = [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
        self.assertListEqual(result_list, extract_markdown_links(text))

    def test_extract_images_none(self):
        text = "This is text with nothing."
        result_list = []
        self.assertListEqual(result_list, extract_markdown_images(text))

    def test_split_nodes_link(self):
        node = TextNode(
    "This is text with an [link](https://www.example.com) and [another](https://www.example.com/another)",
    text_type_text,)
        result_list = [
    TextNode("This is text with an ", text_type_text),
    TextNode("link", text_type_link, "https://www.example.com"),
    TextNode(" and ", text_type_text),
    TextNode(
        "another", text_type_link, "https://www.example.com/another"
    ),]
        self.assertListEqual(result_list, split_nodes_link([node]))

    def test_split_nodes_image(self):
        node = TextNode(
    "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
    text_type_text,)
        result_list = [
    TextNode("This is text with an ", text_type_text),
    TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
    TextNode(" and another ", text_type_text),
    TextNode(
        "second image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
    ),]
        self.assertListEqual(result_list, split_nodes_image([node]))

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.com/image.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", text_type_image, "https://www.example.com/image.png"),
            ],
            new_nodes,
        )

    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        result_list = [
    TextNode("This is ", text_type_text),
    TextNode("text", text_type_bold),
    TextNode(" with an ", text_type_text),
    TextNode("italic", text_type_italic),
    TextNode(" word and a ", text_type_text),
    TextNode("code block", text_type_code),
    TextNode(" and an ", text_type_text),
    TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
    TextNode(" and a ", text_type_text),
    TextNode("link", text_type_link, "https://boot.dev"),]
        self.assertListEqual(result_list, text_to_textnodes(text))

    
