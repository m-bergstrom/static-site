from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block: str) -> BlockType:
    if re.match(r"#{1,6} (\w|\d)", block):
        return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    block_lines = block.split("\n")
    if all(map(lambda l: l.startswith('>'), block_lines)):
        return BlockType.QUOTE
    if all(map(lambda l: l.startswith("- "), block_lines)): # or l.startswith("* "), block_lines)):
        return BlockType.UNORDERED_LIST
    if all(map(lambda e: e[1].startswith(f"{e[0] + 1}. "), enumerate(block_lines))):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH