# Static Site Generator

## Overview

The **Static Site Generator** is a Python-based tool designed to convert Markdown content into static HTML pages. It provides a simple, customizable way to build and deploy static websites from Markdown files. The generator uses a predefined HTML template and applies custom CSS for styling.

## Features

- **Markdown to HTML Conversion**: Converts Markdown files into fully styled HTML pages.
- **Template-Based Rendering**: Utilizes an HTML template for consistent page layout across the site.
- **Static Asset Management**: Automatically copies CSS, images, and other static files to the output directory.
- **Local Development Server**: Includes a Python-based server for testing the generated site locally.

## Requirements

- Python 3.x
- Bash (for running shell scripts)

## Installation

1. Clone the repository or download the ZIP file and extract it.

    ```bash
    git clone https://github.com/yourusername/static-site-gen.git
    ```

2. Navigate to the project directory.

    ```bash
    cd static-site-gen
    ```

3. Ensure you have Python installed and ready to use.

## Usage

### Generate the Site

To generate the static site, run the `main.sh` script:

```bash
./main.sh
```

This script will process the Markdown files in the `content/` directory, convert them into HTML using the template, and place the output in the `output/` directory.

## Serve the Site Locally

You can serve the generated site locally using the `server.py` script:

```bash
python server.py
```

This will start a local development server, allowing you to preview the site in your browser.

## Customization

- **HTML Template**: Customize the `template.html` file to change the structure and layout of the generated pages.
- **CSS Styling**: Modify `static/index.css` to change the styling of the site.
- **Content**: Add or edit Markdown files in the `content/` directory to change the site content.

## Project Structure

- **`main.sh`**: Shell script for running the site generation.
- **`server.py`**: Python script to serve the generated site locally.
- **`template.html`**: The HTML template used for generating pages.
- **`test.sh`**: Shell script for running tests.
- **`content/`**: Directory containing Markdown files to be converted into HTML.
  - **`index.md`**: Main content for the homepage.
  - **`majesty/index.md`**: Additional content for a subpage.
- **`src/`**: Directory containing the Python source code for the site generator.
  - **`block_level.py`**: Handles block-level elements in Markdown.
  - **`generate_page.py`**: Generates HTML pages from Markdown files.
  - **`htmlnode.py`**: Defines structures for HTML elements.
  - **`inline_markdown.py`**: Handles inline Markdown elements.
  - **`leafnode.py`**: Deals with leaf nodes in HTML.
  - **`main.py`**: Main script for site generation.
  - **`parentnode.py`**: Manages parent nodes in HTML.
  - **`static_copy.py`**: Copies static assets like CSS and images.
  - **`textnode.py`**: Handles text nodes in HTML.
  - **`test_*.py`**: Test cases for various modules in the `src/` directory.
- **`static/`**: Directory containing static assets like CSS and images.
  - **`index.css`**: CSS file for styling the generated site.
  - **`images/`**: Directory for images used in the site.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.
