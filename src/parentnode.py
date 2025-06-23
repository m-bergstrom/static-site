from typing import Any, Dict, List
from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag: str | None, children: List[HTMLNode] | None, props: Dict[str, Any] | None = None, pretty_print: bool=False) -> None:
        super().__init__(tag, None, children, props)
        #TODO self.pretty_print = pretty_print

    def to_html(self) -> str:
        if not self.tag:
            raise ValueError("tag is empty")
        if not self.children:
            raise ValueError("no children")
        return f'<{self.tag}{self.props_to_html()}>{"".join(map(lambda c: c.to_html(),self.children))}</{self.tag}>'