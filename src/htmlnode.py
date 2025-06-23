from __future__ import annotations
from typing import List, Dict, Optional, Any

class HTMLNode:
    def __init__(self, tag: Optional[str]=None, value: Optional[str]=None,
                  children: Optional[List[HTMLNode]]=None, props: Optional[Dict[str, Any]]=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        raise NotImplementedError
    
    def props_to_html(self) -> str:
        if not self.props:
            return ""
        return "".join(map(lambda p: f' {p[0]}="{p[1]}"', self.props.items()))
    
    def __repr__(self) -> str:
        return f'tag: {self.tag}\nvalue: {self.value}\nchildren:\nprops:\n{"\n".join(map(lambda p: f'  "{p[0]}": "{p[1]}"', self.props.items())) if self.props else ""}'