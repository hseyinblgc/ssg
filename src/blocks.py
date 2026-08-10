def markdown_to_blocks(markdown: str) -> list[str]:
    blocks: list[str] = markdown.split("\n\n")
    return [block.strip() for block in blocks if len(block) > 0]
