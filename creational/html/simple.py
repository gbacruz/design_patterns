from .element import Element, HTMLITEM


class Simple(Element):
    def add_element(self, html_item: HTMLITEM) -> None:
        self._elements.append(html_item)