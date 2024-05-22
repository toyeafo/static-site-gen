import re
from textnode import (TextNode, text_type_bold, text_type_code, text_type_image, text_type_italic, text_type_link, text_type_text)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    node_list = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            node_list.append(node)
            continue
        node_split = node.text.split(delimiter)
        if len(node_split) % 2 == 0:
            raise ValueError(f"Invalid markdown syntax")
        for val in range(len(node_split)):
            if node_split[val] == "":
                continue
            if val % 2 == 0:
                node_list.append(TextNode(node_split[val], text_type_text))
            else:
                node_list.append(TextNode(node_split[val], text_type))
            
    return node_list

def extract_markdown_images(text):
    image_match = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return image_match

def extract_markdown_links(text):
    link_match = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return link_match

def split_nodes_image(old_nodes):
    node_list = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            node_list.append(node)
            continue
        node_text = node.text

        image_link_search = extract_markdown_images(node.text)
        
        if len(image_link_search) == 0:
            node_list.append(node)
            continue

        for link in image_link_search:
            split_node_using_link = node_text.split(f"![{link[0]}]({link[1]})", maxsplit=1)
            if len(split_node_using_link) != 2:
                raise ValueError("Invalid Markdown, image section not closed")
            if split_node_using_link[0] != "":
                node_list.append(TextNode(split_node_using_link[0], text_type_text))
            node_list.append(TextNode(link[0], text_type_image, link[1]))
            node_text = split_node_using_link[1]
        if node_text != "":
            node_list.append(TextNode(node_text, text_type_text))
    return node_list

def split_nodes_link(old_nodes):
    node_list = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            node_list.append(node)
            continue
        node_text = node.text

        image_link_search = extract_markdown_links(node.text)
        
        if len(image_link_search) == 0:
            node_list.append(node)
            continue

        for link in image_link_search:
            split_node_using_link = node_text.split(f"[{link[0]}]({link[1]})", maxsplit=1)
            if len(split_node_using_link) != 2:
                raise ValueError("Invalid Markdown, link section not closed")
            if split_node_using_link[0] != "":
                node_list.append(TextNode(split_node_using_link[0], text_type_text))
            node_list.append(TextNode(link[0], text_type_link, link[1]))
            node_text = split_node_using_link[1]
        if node_text != "":
            node_list.append(TextNode(node_text, text_type_text))
    return node_list

def text_to_textnodes(text):
    node = [TextNode(text, text_type_text)]
    node = split_nodes_delimiter(node, "**", text_type_bold)
    node = split_nodes_delimiter(node, "*", text_type_italic)
    node = split_nodes_delimiter(node, "`", text_type_code)
    node = split_nodes_image(node)
    node = split_nodes_link(node)
    return node