import abc
from typing import Dict, Optional, TypeVar, Union

HTMLITEM = TypeVar("HTMLITEM", bound=Union["Element", str])


class Element(metaclass=abc.ABCMeta):
    __slots__ = (
        "_props",
        "_elements",
        "_tag",
    )

    def __init__(self, tag):
        self._props = []
        self._elements = []
        self._tag = tag

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "html")
            and callable(subclass.html)
            and hasattr(subclass, "add_class")
            and callable(subclass.add_class)
            and hasattr(subclass, "add_props")
            and callable(subclass.add_props)
            and hasattr(subclass, "add_element")
            and callable(subclass.add_element)
            and hasattr(subclass, "add_element")
            and callable(subclass.add_element)
            or NotImplemented
        )

    def _get_props(self) -> str:
        if not self._props:
            return ""
        return " ".join(c for c in self._props)

    def _build_init_tag(self) -> str:
        return f"<{self._tag} {self._get_props()}>"

    @abc.abstractmethod
    def add_element(self, html_item: HTMLITEM) -> None:
        raise NotImplementedError

    def add_prop(self, key: str, value: str) -> None:
        self._props.append(f"{key}='{value}'")

    def add_props(self, html_props: Optional[Dict[str, str]] = None) -> None:
        if html_props is not None:
            for k, v in html_props.items():
                self.add_prop(k, v)

    def html(self, child=1) -> str:
        tab = "\t"
        data = [self._build_init_tag()]
        if not self._elements:
            return f"{data[0][:-1]} />"
        for element in self._elements:
            data.append(f"\n{tab * child}{get_element(element, child)}")
        data.append(f"\n{tab * (child - 1)}</{self._tag}>")
        return "".join(data)


def get_element(element: HTMLITEM, child: int) -> str:
    if isinstance(element, Element):
        return element.html(child + 1)
    return element
