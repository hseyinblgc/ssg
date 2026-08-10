import unittest

from blocks import BlockType, block_to_block_type, markdown_to_blocks


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


class TestBlockToBlockType(unittest.TestCase):
    def test_ordered_list(self):
        md = "1. first item\n2. second item\n3. third item"
        self.assertEqual(block_to_block_type(md), BlockType.ORDERED_LIST)

    def test_ordered_list_not_starting_at_one(self):
        md = "2. first item\n3. second item"
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

    def test_heading(self):
        md = "### This is a heading"
        self.assertEqual(block_to_block_type(md), BlockType.HEADING)

    def test_quote(self):
        md = ">this is a quote\n>still a quote"
        self.assertEqual(block_to_block_type(md), BlockType.QUOTE)

    def test_paragraph(self):
        md = "This is just a normal paragraph of text."
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()
