from creational.web_page import Head, Body, WebPage, Simple

head = Head("My page")
head.add_link("<link href='example.com/test.css' />")
script = Simple("script")
script.add_props({"href": "example.com/test.js"})
head.add_script(script)

body = Body()
body.add_element("<h1>Some Title</h1>")

web_page = WebPage()
web_page.add_head(head)
web_page.add_body(body)
a = web_page.html()
print(a)

"""
<html >
        <head >
        <title >
                My page
        </title>
        <link href='example.com/test.css' />
        <script href='example.com/test.js' />
</head>
        <body >
                <h1>Some Title</h1>
        </body>
</html>
"""