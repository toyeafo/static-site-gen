import re

from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode
from inline_markdown import text_to_textnodes

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


def markdown_to_blocks(markdown):
    block_list = [val.strip('\n ') for val in markdown.split('\n\n') if val != '']
    return block_list

def block_to_block_type(markdown_block):
    lines = markdown_block.split('\n')

    if re.match(r'#+ \w+', markdown_block[:6]):
        return block_type_heading
    if len(lines) > 1 and markdown_block.startswith('```') and markdown_block.endswith('```'):
        return block_type_code
    if re.match(r'^\>.+', markdown_block):
        for line in lines:
            if not line.startswith('>'):
                return block_type_paragraph
        return block_type_quote
    if re.match(r'^\d+\. .+', markdown_block):
        for line in lines:
            if not re.match(r'^\d+\. .+', line):
                return block_type_paragraph
        return block_type_ordered_list
    if re.match(r'^\* .+|^\- .+', markdown_block):
        for line in lines:
            if not re.match(r'^\* .+|^\- .+', line):
                return block_type_paragraph
        return block_type_unordered_list
    return block_type_paragraph

def heading_block_type_to_html_node(markdown_block):
    count = 0
    md_split = [val for val in re.split(r'(#+ )', markdown_block) if val != '']
    for header_char in md_split[0]:
        if header_char == '#':
            count += 1
    text_node_list = text_to_textnodes(md_split[1])
    heading_value = ""
    for val in text_node_list:
        heading_value += val.text_node_to_html_node().to_html()
    return LeafNode(f"h{count}", f"{heading_value}")

def quote_block_type_to_html_node(markdown_block):
    lines = markdown_block.split('\n')
    quote_list = []
    for line in lines:
        md_split = [val.strip() for val in re.split(r'^\> ', line) if val != '']
        quote_list.extend(md_split)
    quote = " ".join(quote_list)
    text_node_list = [val.text_node_to_html_node() for val in text_to_textnodes(quote)]
    return ParentNode("blockquote", text_node_list)

def ordered_list_to_html_node(markdown_block):
    lines = markdown_block.split('\n')
    node_list = []
    for line in lines:
        md_split = [val for val in re.split(r'(^\d+\. )', line) if val != '']
        text_node_list = [val.text_node_to_html_node() for val in text_to_textnodes(md_split[1])]
        node_list.append(ParentNode("li", text_node_list))
    return ParentNode("ol", node_list)

def unordered_list_to_html_node(markdown_block):
    lines = markdown_block.split('\n')
    node_list = []
    for line in lines:
        md_split = [val for val in re.split(r'(^\* |^\- )', line) if val != '']
        text_node_list = [val.text_node_to_html_node() for val in text_to_textnodes(md_split[1])]
        node_list.append(ParentNode("li", text_node_list))
    return ParentNode("ul", node_list)

def code_to_html_node(markdown_block):
    split_md = [val.strip() for val in markdown_block.split('```') if val != '']
    node_list = []
    for line in range(len(split_md)):
        lines = "\n".join(split_md[line].split('\n'))
        if lines != '':
            text_node_list = [val.text_node_to_html_node() for val in text_to_textnodes(lines)]
            node_list.append(ParentNode("code", text_node_list))
    return ParentNode('pre', node_list)

def paragraph_to_html_node(markdown_block):
    md_split = [val for val in markdown_block.split('\n') if val != '']
    paragraph = " ".join(md_split)
    text_node_list = [val.text_node_to_html_node() for val in text_to_textnodes(paragraph)]
    return ParentNode("p", text_node_list)

def markdown_to_html(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    parent_block_list = []

    for block in markdown_blocks:
        if block_to_block_type(block) == block_type_heading:
            parent_block_list.append(heading_block_type_to_html_node(block))
        elif block_to_block_type(block) == block_type_quote:
            parent_block_list.append(quote_block_type_to_html_node(block))
        elif block_to_block_type(block) == block_type_code:
            parent_block_list.append(code_to_html_node(block))
        elif block_to_block_type(block) == block_type_ordered_list:
            parent_block_list.append(ordered_list_to_html_node(block))
        elif block_to_block_type(block) == block_type_unordered_list:
            parent_block_list.append(unordered_list_to_html_node(block))
        elif block_to_block_type(block) == block_type_paragraph:
            parent_block_list.append(paragraph_to_html_node(block))
        else:
            raise ValueError("Invalid Markdown block")

    return ParentNode("div", parent_block_list)