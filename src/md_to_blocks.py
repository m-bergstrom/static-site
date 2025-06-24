from typing import List
from blocktype import BlockType, block_to_block_type
from htmlnode import HTMLNode
from leafnode import LeafNode
from md_to_inline import text_to_textnodes
from parentnode import ParentNode
from textnode import TextNode, TextType, text_node_to_html_node


def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    return ParentNode("div", list(map(block_to_node, blocks)))

def block_to_node(block: str) -> HTMLNode:
    block_type = block_to_block_type(block)
    match block_type:
        case BlockType.PARAGRAPH:
            return block_to_paragraph_node(block)
        case BlockType.HEADING:
            return block_to_heading_node(block)
        case BlockType.CODE:
            return block_to_code_node(block)
        case BlockType.UNORDERED_LIST:
            return block_to_unordered_list_node(block)
        case BlockType.ORDERED_LIST:
            return block_to_ordered_list_node(block)
        case BlockType.QUOTE:
            return block_to_quote_node(block)

def block_to_paragraph_node(block: str) -> HTMLNode:
    return ParentNode("p", text_to_children(block))

def block_to_heading_node(block: str) -> HTMLNode:
    splits = block.split("# ")
    hash_length = len(splits[0]) + 1
    title = splits[1]
    return ParentNode(f"h{hash_length}", text_to_children(title))

def block_to_code_node(block: str) -> HTMLNode:
    return ParentNode("pre", [text_node_to_html_node(TextNode("\n".join(block.split("\n")[1:-1]), TextType.CODE))])

def block_to_unordered_list_node(block: str) -> HTMLNode:
    return ParentNode("ul", list(map(lambda l: ParentNode("li", list(map(text_node_to_html_node, text_to_textnodes(l.split("- ", 1)[1])))), block.split("\n"))))

def block_to_ordered_list_node(block: str) -> HTMLNode:
    return ParentNode("ol", list(map(lambda l: ParentNode("li", list(map(text_node_to_html_node, text_to_textnodes(l.split(". ", 1)[1])))), block.split("\n"))))

def block_to_quote_node(block: str) -> HTMLNode:
    return ParentNode("blockquote", list(map(text_node_to_html_node, text_to_textnodes("\n".join(map(lambda l: l.split('>', 1)[1].strip(), block.split("\n")))))))

def markdown_to_blocks(markdown: str) -> List[str]:
    return list(filter(lambda b: b, map(lambda b: b.strip(), markdown.split("\n\n"))))

def text_to_children(block: str) -> List[HTMLNode]:
    return list(map(text_node_to_html_node, text_to_textnodes(block)))
