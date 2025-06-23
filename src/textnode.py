from __future__ import annotations
from enum import Enum
from typing import Optional

from htmlnode import HTMLNode
from leafnode import LeafNode

class TextType(Enum):
    PLAIN = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text: str, text_type: TextType, url:Optional[str]=None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self, value: object) -> bool:
        return (
            type(value) is TextNode 
            and value.text == self.text
            and value.text_type == self.text_type
            and value.url == self.url
            )
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

    def to_html_node(self) -> HTMLNode:
        match self.text_type:
            case TextType.PLAIN:
                return LeafNode(tag=None, value=self.text)
            case TextType.BOLD:
                return LeafNode("b", self.text)
            case TextType.ITALIC:
                return LeafNode("i", self.text)
            case TextType.CODE:
                return LeafNode("code", self.text)
            case TextType.LINK:
                return LeafNode("a", self.text, {"href": self.url})
            case TextType.IMAGE:
                return LeafNode("img", "", {"src": self.url, "alt": self.text})
            case _:
                raise ValueError(f"unknown text type {self.text_type}")

def text_node_to_html_node(text_node: TextNode) -> HTMLNode:
    return text_node.to_html_node()