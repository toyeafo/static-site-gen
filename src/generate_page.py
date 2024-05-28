import os
from block_level import markdown_to_html


def extract_title(markdown):
    for lines in markdown.split('\n'):
        if lines.startswith('# '):
            return lines.strip('# ')
    raise Exception('Not valid markdown. Header not present.')

def generate_page(from_path, template_path, dest_path):
    print(f"Generate page from {from_path} to {dest_path} using {template_path}")

    file_from_path = open(from_path, 'r')
    file_template_path = open(template_path, 'r')

    md_file = file_from_path.read()
    html_file = markdown_to_html(md_file).to_html()
    title = extract_title(md_file)

    template_file = file_template_path.read()
    template_file = template_file.replace('{{ Title }}', title).replace('{{ Content }}', html_file)

    parent_dest_dir = os.path.dirname(dest_path)

    if not os.path.exists(parent_dest_dir):
        os.makedirs(parent_dest_dir)

    with open(dest_path, 'w') as f:
        f.write(template_file)

    file_from_path.close()
    file_template_path.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dir_path_content):
        raise ValueError('Invalid Content Directory Path')

    for dir in os.listdir(dir_path_content):
        new_source_path = os.path.join(dir_path_content, dir)
        new_dest_path = os.path.join(dest_dir_path, dir).replace('.md', '.html')
        if os.path.isfile(new_source_path):
            generate_page(new_source_path, template_path, new_dest_path)
        else:
            generate_pages_recursive(new_source_path, template_path, new_dest_path)
