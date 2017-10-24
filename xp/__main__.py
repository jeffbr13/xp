import sys
from typing import Union

from lxml import etree
from lxml.builder import E
from pygments import highlight
from pygments.formatters.terminal import TerminalFormatter
from pygments.lexers.html import XmlLexer


def wrap_in_results(elements: [Union[etree.Element, etree._ElementUnicodeResult]]) -> str:
    results = E.results()
    for el in elements:
        results.append(E.result(el))
    return results


# See <http://lxml.de/FAQ.html#why-doesn-t-the-pretty-print-option-reformat-my-xml-output>
parser = etree.XMLParser(remove_blank_text=True)
input = etree.parse(sys.stdin, parser)

query = sys.argv[1] if len(sys.argv) > 1 else None
if query:
    matches = input.xpath(query)
    results = wrap_in_results(matches)
    output = etree.tostring(results, pretty_print=True)
else:
    output = etree.tostring(input, pretty_print=True)


sys.stdout.write(highlight(output, XmlLexer(), TerminalFormatter()))
