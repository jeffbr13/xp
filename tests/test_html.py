import unittest
from io import StringIO
from lxml import etree
from lxml.builder import E

from xp.__main__ import main, wrap_in_results

SAMPLE_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Page Title</title>
    <meta charset="utf-8">
    <link rel="alternate" type="application/rss+xml" href="/rss/" />
    <link rel="shortcut icon" href="/favicon.ico" />
</head>
<body>
    <header>
        <h1>Heading 1</h1>
    </header>
    <main>
        <p>Paragraph 1 with a <a href="/url/1">link</a>.</p>
        <h1>Heading 2</h1>
        <p>Paragraph 2.</p>
    </main>
    <hr>
    <footer>
        <p><a href="/url/2">🛠</a></p>
    </footer>
</body>
</html>
"""


class TestHtmlXpathExpressions(unittest.TestCase):
    def setUp(self):
        self.test_input = StringIO(SAMPLE_HTML)

    def tearDown(self):
        self.test_input.close()

    def test_extract_elements(self):
        expected_output = etree.tounicode(
            E.results(
                E.result(
                    E.p('Paragraph 1 with a ', E.a('link', href='/url/1'), '.')
                ),
                E.result(
                    E.p('Paragraph 2.')
                ),
            ),
            pretty_print=True
        )
        # expected_output = etree.tounicode(wrap_in_results([
        #         E.p('Paragraph 1 with a ', E.a('link', href='/url/1'), '.'),
        #         E.p('Paragraph 2.')
        #     ]),
        #     pretty_print=True
        # )
        output = main(self.test_input, '//p', colorize=False)
        print(expected_output)
        print(output)
        self.assertEqual(expected_output, output)

    def test_extract_attributes(self):
        expected_output = etree.tounicode(
            E.results(
                E.result('/url/1'),
                E.result('/url/2'),
            ),
            pretty_print=True
        )
        self.assertEqual(expected_output, main(self.test_input, '//a/@href', colorize=False))

    def test_extract_text(self):
        expected_output = etree.tounicode(
            E.results(
                E.result('Heading 1'),
                E.result('Heading 2'),
            ),
            pretty_print=True
        )
        self.assertEqual(expected_output, main(self.test_input, '//h1/text()', colorize=False))
