import unittest

from extract_markdown_img import *

class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_multiple_images(self):
        matches = extract_markdown_images(
            "First ![cat](https://example.com/cat.jpg) and then ![dog](https://example.com/dog.jpg)"
        )
        self.assertListEqual(
            [
                ("cat", "https://example.com/cat.jpg"),
                ("dog", "https://example.com/dog.jpg")
            ],
            matches
        )

    def test_empty_alt_text(self):
        matches = extract_markdown_images(
            "Image with no alt text ![](/local/path/image.png)"
        )
        self.assertListEqual([("", "/local/path/image.png")], matches)

    def test_no_images(self):
        matches = extract_markdown_images(
            "Just plain text with no images."
        )
        self.assertListEqual([], matches)

    def test_alt_text_with_spaces(self):
        matches = extract_markdown_images(
            "An image with ![spaces in alt text](http://example.com/img.jpg)"
        )
        self.assertListEqual([("spaces in alt text", "http://example.com/img.jpg")], matches)

    def test_minimal_image_syntax(self):
        matches = extract_markdown_images("![a](b)")
        self.assertListEqual([("a", "b")], matches)

class TestExtractMarkdownLinks(unittest.TestCase):
    def test_single_link(self):
        matches = extract_markdown_links(
            "This is a [link](https://example.com) in text."
        )
        self.assertListEqual([("link", "https://example.com")], matches)

    def test_multiple_links_with_image(self):
        matches = extract_markdown_links(
            "A [first link](https://example.com/first) and [second link](https://example.com/second) with an ![image](https://example.com/image.jpg)."
        )
        self.assertListEqual(
            [
                ("first link", "https://example.com/first"),
                ("second link", "https://example.com/second")
            ],
            matches
        )

    def test_no_links(self):
        matches = extract_markdown_links(
            "Text with no links but an ![image](https://example.com/image.jpg)."
        )
        self.assertListEqual([], matches)
    

if __name__ == "__main__":
    unittest.main()