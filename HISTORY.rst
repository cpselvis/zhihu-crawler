.. :changelog:

Release History
---------------

0.7.0 (2017-6-18)
+++++++++++++++++++

- Use redis queue to support distributed crawler.

0.6.0 (2017-6-12)
+++++++++++++++++++

- Print exception when error.
- Use proxy ip to avoid crawler against replies.

0.5.0 (2017-6-11)
+++++++++++++++++++

- Seperate html parser part to a single file.

0.4.0 (2017-1-5)
+++++++++++++++++++

- Implements bloom filter to judge wether an element exists in a collection.

0.3.0 (2016-12-7)
+++++++++++++++++++

- Design database and table scheme.
- Use mysql as persistent layer, store user data.
- Encapsulate python mysql operate library.

0.2.0 (2016-12-6)
+++++++++++++++++++

- Memory queue to support BFS crawler.
- Hash set to to story visited urls, avoid duplicate visits.

0.1.0 (2016-12-6)
+++++++++++++++++++

- Crawler can fetch username, personal brief info, current industry, education university, major subject and social activities such as answer count, article count, ask question count, collection count, follower count, follow live count, follow topic count, follow column count, follow question count, follow collection count.
- Print information in console with a format pattern.
- Support utf-8 encoding
