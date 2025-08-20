import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    """
    Recursively traverses a content directory and generates corresponding HTML files.
    
    - If the current item is a file, it converts it to HTML using a template.
    - If the item is a directory, it recurses into it and processes its contents.
    
    Args:
        dir_path_content (str): Source directory containing markdown files and subdirectories.
        template_path (str): Path to the HTML template file.
        dest_dir_path (str): Destination directory for generated HTML files.
        basepath (str): Base path for generated links (e.g., "/" or a subpath).
    """
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)   # Current source path
        dest_path = os.path.join(dest_dir_path, filename)      # Corresponding destination path

        if os.path.isfile(from_path):
            # Convert markdown file into an HTML file with ".html" extension
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path, basepath)
        else:
            # Recursively process subdirectories
            generate_pages_recursive(from_path, template_path, dest_path, basepath)


def generate_page(from_path, template_path, dest_path, basepath):
    """
    Converts a single markdown file into an HTML file using a template.
    
    - Reads markdown content from `from_path`.
    - Converts it to HTML using `markdown_to_html_node`.
    - Replaces placeholders in the template (Title, Content, href, src).
    - Writes the final HTML to `dest_path`.
    
    Args:
        from_path (str): Path to the source markdown file.
        template_path (str): Path to the HTML template file.
        dest_path (str): Destination path for the generated HTML file.
        basepath (str): Base path for adjusting relative URLs.
    """
    print(f" * {from_path} {template_path} -> {dest_path}")

    # Read markdown content
    with open(from_path, "r") as from_file:
        markdown_content = from_file.read()

    # Read HTML template
    with open(template_path, "r") as template_file:
        template = template_file.read()

    # Convert markdown content to an HTML node
    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    # Extract the page title from markdown (first-level heading)
    title = extract_title(markdown_content)

    # Replace template placeholders with actual values
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    template = template.replace('href="/', 'href="' + basepath)  # Adjust links
    template = template.replace('src="/', 'src="' + basepath)    # Adjust assets

    # Ensure destination directory exists
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    # Write the final HTML to the destination file
    with open(dest_path, "w") as to_file:
        to_file.write(template)


def extract_title(md):
    """
    Extracts the title from markdown content.
    
    The title is expected to be the first line starting with "# ".
    
    Args:
        md (str): Markdown content as a string.
    
    Returns:
        str: Title text without the markdown heading marker.
    
    Raises:
        ValueError: If no title is found in the markdown content.
    """
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]  # Strip "# " to get the title text
    raise ValueError("no title found")

