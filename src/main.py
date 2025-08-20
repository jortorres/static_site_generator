import os
import shutil
import sys

from copystatic import copy_files_recursive
from gencontent import generate_page
from gencontent import generate_pages_recursive

# Directory paths used for static files, generated content, and templates
dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"

# Default base path used for generated links (can be overridden by CLI argument)
default_basepath = "/"


def main():
    """
    Main entry point of the script.
    - Cleans the public output directory
    - Copies static assets into it
    - Generates HTML pages from content using a template
    """

    # Use the default base path unless one is provided as a command-line argument
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    # Step 1: Remove the existing public directory to ensure a clean build
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    # Step 2: Copy static assets (CSS, JS, images, etc.) into the public directory
    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    # Step 3: Generate HTML pages from markdown/content files using the template
    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)


# Script execution begins here
# Ensures main() runs only when script is executed directly
main()
