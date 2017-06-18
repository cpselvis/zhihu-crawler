#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
zhihu_crawler.worker
~~~~~~~~~~~~~~~~

Use rq module to support distributed crawler task assigment,
deploy this file to a machine cluster.

"""

import os

import redis
from rq import Worker, Queue, Connection

listen = ['high', 'default', 'low']

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')

conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()
