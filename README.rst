xq
==

Apply XPath expressions to XML, like ``jq`` does for JSONPath and JSON.


Installation
------------

Install with ``pip``::

    pip install xq

Or download the repo and install via ``setuptools``::

    python setup.py install


Usage
-----

Extract download URLs from an RSS feed::

    http get 'http://br-rss.jeffbr13.net/rss/channels/1/' | xq '//item/enclosure/@url'


Extract all links from an HTML page footer::

    http get 'http://br-rss.jeffbr13.net/ | xq '//footer//a/@href'


Test
----

Run ``unittest`` in the root directory to autodetect and run tests::

    python -m unittest


Build
-----

Increment ``xq.VERSION`` and run the following two commands
to create a `source distribution <https://packaging.python.org/tutorials/distributing-packages/#source-distributions>`_,
create a `universal wheel <https://packaging.python.org/tutorials/distributing-packages/#universal-wheels>`_,
and `upload to PyPI <https://packaging.python.org/tutorials/distributing-packages/#upload-your-distributions>`_ ::

    python setup.py sdist
    python setup.py bdist_wheel --universal
    twine upload dist/*


See Also
--------

- `jq <https://github.com/stedolan/jq>`_
- `hq <https://github.com/rbwinslow/hq>`_
