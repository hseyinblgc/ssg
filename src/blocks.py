from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(text: str) -> BlockType:
    lines = text.split("\n")
    prefix: dict[str, tuple[str, ...]] = {
        "heading": ("# ", "## ", "### ", "#### ", "##### ", "###### "),
        "code": ("```", "```\n", "\n```"),
        "quote": (">", " >"),
        "unordered": ("- ",),
    }

    if text.startswith(prefix["heading"]):
        return BlockType.HEADING

    if text.startswith(prefix["code"]) and text.endswith(prefix["code"]):
        return BlockType.CODE

    if text.startswith(prefix["quote"]):
        return BlockType.QUOTE

    if all(line.startswith(prefix["unordered"]) for line in lines):
        return BlockType.UNORDERED_LIST

    is_ordered = True
    for i, line in enumerate(lines):
        expected_prefix = f"{i + 1}. "
        if not line.startswith(expected_prefix):
            is_ordered = False
            break
    if is_ordered:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH


def markdown_to_blocks(markdown: str) -> list[str]:
    blocks: list[str] = markdown.split("\n\n")
    return [block.strip() for block in blocks if len(block) > 0]
