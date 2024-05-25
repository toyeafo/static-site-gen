from textnode import TextNode
from static_copy import copy_contents

def main():
    text_node = TextNode('This is a text node', 'italic', 'https://sometext')
    print(text_node)
    result = copy_contents('static', 'public')
    print(result)

main()
