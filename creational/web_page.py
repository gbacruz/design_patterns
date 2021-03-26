from .html import Complex, Simple, HTMLITEM


class Head:
    def __init__(self, title):
        self._item = Complex("head")
        title_ = Simple("title")
        title_.add_element(title)
        self._item.add_element(title_)

    def add_link(self, link: HTMLITEM) -> None:
        self._item.add_element(link)

    def add_script(self, script: HTMLITEM) -> None:
        self._item.add_element(script)

    def html(self):
        return self._item.html(1)


class Body(Complex):
    def __init__(self):
        super().__init__("body")


class WebPage:
    def __init__(self):
        self._document = Complex("html")

    def add_head(self, head: Head):
        self._document.add_element(head.html())

    def add_body(self, body: Body):
        self._document.add_element(body)

    def html(self):
        return self._document.html()
