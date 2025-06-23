import re
from typing import List, Tuple
from textnode import TextNode, TextType

def text_to_textnodes(text: str) -> List[TextNode]:
    return split_nodes_link(
        split_nodes_image(
            split_nodes_delimiter(
                split_nodes_delimiter(
                    split_nodes_delimiter(
                        split_nodes_delimiter(
                            split_nodes_delimiter([TextNode(text, TextType.TEXT)], '`', TextType.CODE)
                            , '**', TextType.BOLD)
                        , '__', TextType.BOLD)
                    , '*', TextType.ITALIC)
                , '_', TextType.ITALIC)
            )
        )

def split_nodes_image(old_nodes: List[TextNode]) -> List[TextNode]:
    new_nodes: List[TextNode] = []

    for old_node in old_nodes:
        images = extract_markdown_images(old_node.text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        for i in range(0, len(images)):
            alt_text, url = images[i]
            splits = original_text.split(f"![{alt_text}]({url})", 1)
            if splits[0]:
                new_nodes.append(TextNode(splits[0], TextType.TEXT))
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            if i + 1 == len(images) and splits[1]:
                new_nodes.append(TextNode(splits[1], TextType.TEXT))
            else:
                original_text = splits[1]
    return new_nodes

def split_nodes_link(old_nodes: List[TextNode]) -> List[TextNode]:
    new_nodes: List[TextNode] = []

    for old_node in old_nodes:
        links = extract_markdown_links(old_node.text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        for i in range(0, len(links)):
            link_text, url = links[i]
            splits = original_text.split(f"[{link_text}]({url})", 1)
            if splits[0]:
                new_nodes.append(TextNode(splits[0], TextType.TEXT))
            new_nodes.append(TextNode(link_text, TextType.LINK, url))
            if i + 1 == len(links) and splits[1]:
                new_nodes.append(TextNode(splits[1], TextType.TEXT))
            else:
                original_text = splits[1]

    return new_nodes

def split_nodes_delimiter(old_nodes: List[TextNode], delimiter: str, text_type: TextType) -> List[TextNode]:
    new_nodes: List[TextNode] = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        splits = old_node.text.split(delimiter)
        if len(splits) % 2 == 0:
            raise Exception(f'"{old_node.text}" contains an unbalanced \'{delimiter}\'')
        new_nodes.extend(
            filter(lambda n: len(n.text) > 0,
                   map(lambda e: 
                       TextNode(text=e[1], 
                                text_type=old_node.text_type if e[0] % 2 == 0 else text_type),
                        enumerate(splits)
                    )
                )
            )
    return new_nodes
    
def extract_markdown_images(text: str) -> List[Tuple[str, str]]:
    return re.findall(r"!\[([^\]]+)\]\(([^)]+)\)", text)
    
def extract_markdown_links(text: str) -> List[Tuple[str, str]]:
    return re.findall(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)", text)