import unittest

from main import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title_valid_header(self):
        """Test that a valid markdown header returns the stripped title."""
        markdown_input = "# Hello World"
        result = extract_title(markdown_input)
        self.assertEqual(result.strip(), "Hello World")

    def test_extract_title_invalid_format_raises_value_error(self):
        """Test that an invalid markdown string raises ValueError with the correct message."""
        invalid_input = "Hello World"
        with self.assertRaises(ValueError) as context:
            extract_title(invalid_input)

        self.assertEqual(str(context.exception), f"Invalid format: {invalid_input}")

    def test_extract_title_multiple_hashes(self):
        """Test that headers with multiple hashes raises ValueError"""
        markdown_input = "### Subtitle Heading"
        with self.assertRaises(ValueError) as context:
            extract_title(markdown_input)
        self.assertEqual(str(context.exception), f"Invalid format: {markdown_input}")


if __name__ == "__main__":
    unittest.main()
