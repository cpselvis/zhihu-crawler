zhihu-crawler:
=========================
A zhihu user information crawler, which will collect some useful message including username, education, profession, follower and folling count.

Technicial stack
------------
- `requests <https://github.com/kennethreitz/requests>`_.
- `Bloom Filter <https://en.wikipedia.org/wiki/Bloom_filter>`_.
- `XPath <https://en.wikipedia.org/wiki/XPath>`_.
- `rq <https://github.com/nvie/rq>`_.
- MySQL
- `Anti crawler strategy`

Setup
-------------


::

    git clone https://github.com/cpselvis/zhihu-crawler.git
    cd zhihu-crawler
    pip install -r requirements.txt
    python crawler.py

Documentation
-------------

Fantastic documentation is available at `WIKI <https://github.com/cpselvis/zhihu-crawler/wiki/%E4%B8%80%E6%AD%A5%E4%B8%80%E6%AD%A5%E5%AE%9E%E7%8E%B0%E9%AB%98%E6%80%A7%E8%83%BD%E7%88%AC%E8%99%AB/>`_.


How to Contribute
-----------------

#. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug.
#. Fork `the repository`_ on GitHub to start making your changes to the **master** branch (or branch off of it).
#. Write a test which shows that the bug was fixed or that the feature works as expected.
#. Send a pull request and bug the maintainer until it gets merged and published. :) Make sure to add yourself to AUTHORS_.
