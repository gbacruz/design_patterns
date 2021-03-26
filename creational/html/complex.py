from .element import Element, HTMLITEM


class Complex(Element):
    def add_element(self, html_item: HTMLITEM) -> None:
        self._elements.append(html_item)