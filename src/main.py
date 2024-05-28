from static_copy import copy_contents
from generate_page import generate_pages_recursive

def main():
    result = copy_contents('static', 'public')
    print(result)
    webpage = generate_pages_recursive('content', 'template.html', 'public')
    print(webpage)

main()
