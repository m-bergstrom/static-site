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
    
    def __eq__(self, value: object) -> bool:
        return (
            isinstance(value, HTMLNode)
            and self.tag == value.tag
            and self.value == value.value
            and self.props == value.props
            and self.children == value.children
            )
    
    def __repr__(self) -> str:
        return self._get_string()

    def _get_string(self, levels:int=0) -> str:
        leading_white = " " * levels * 4
        return "\n".join([
            f'{leading_white}tag: {self.tag}',
            f'{leading_white}value: {self.value}',
            f'{leading_white}props:\n{"\n".join(map(lambda p: f'{leading_white}  "{p[0]}": "{p[1]}"', self.props.items())) if self.props else ""}',
            f'{leading_white}children:{("\n" if self.children else "") + "\n".join(map(lambda c: c._get_string(levels + 1), self.children if self.children and len(self.children) > 0 else []))}',
        ])
    #f'{leading_white}tag: {self.tag}\n{leading_white}value: {self.value}\n{leading_white}children:{("\n" if self.children else "") + "\n".join(map(lambda c: c._get_string(levels + 1), self.children if self.children and len(self.children) > 0 else []))}\n{leading_white}props:\n{"\n".join(map(lambda p: f'{leading_white}  "{p[0]}": "{p[1]}"', self.props.items())) if self.props else ""}'