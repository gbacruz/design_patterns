from .element import Element, HTMLITEM
from .simple import Simple


class Complex(Element):
    def add_element(self, html_item: HTMLITEM) -> None:
        self._elements.append(html_item)