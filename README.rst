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
    
    # Run serveral workers and listen task queue.
    python worker.py
    
    # Begin task
    python scheduler.py

Documentation
-------------

Fantastic documentation is available at `WIKI <http://www.cnblogs.com/cpselvis/p/7001137.html>`_.


How to Contribute
-----------------

#. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug.
#. Fork `the repository`_ on GitHub to start making your changes to the **master** branch (or branch off of it).
#. Write a test which shows that the bug was fixed or that the feature works as expected.
#. Send a pull request and bug the maintainer until it gets merged and published. :) Make sure to add yourself to AUTHORS_.
