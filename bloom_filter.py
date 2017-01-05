#!/usr/bin/python
# -*- coding: utf-8 -*-

import mmh3
from bitarray import bitarray

"""
zhihu_crawler.bloom_filter

Implement a simple bloom filter with murmurhash algorithm.
Bloom filter is used to check wether an element exists in a collection, and it has a good performance in big data situation.
It may has positive rate depend on hash functions and elements count.

~~~~~~~~~~~~~~~~
"""


BIT_SIZE = 5000000

class BloomFilter:
    
    def __init__(self, cfg):
        # Initialize bloom filter, set size and all bits to 0
        bit_array = bitarray(BIT_SIZE)
        bit_array.setall(0)

        this.bit_array = bit_array
        
    def add(url):
        # Add a url, and set points in bitarray to 1 (Points count is equal to hash funcs count.)
        # Here use 7 hash functions.
        point_list = this.get_postions(url)

        for b in point_list:
            this.bit_array[b] = 1

    def contains(url):
        # Check if a url is in a collection
        point_list = this.get_postions(url)

        result = True
        for b in point_list:
            result = result and this.bit_array[b]
    
        return result

    def get_postions(url):
        # Get points positions in bit vector.
        point1 = mmh3.hash(url, 41) % BIT_SIZE
        point2 = mmh3.hash(url, 42) % BIT_SIZE
        point3 = mmh3.hash(url, 43) % BIT_SIZE
        point4 = mmh3.hash(url, 44) % BIT_SIZE
        point5 = mmh3.hash(url, 45) % BIT_SIZE
        point6 = mmh3.hash(url, 46) % BIT_SIZE
        point7 = mmh3.hash(url, 47) % BIT_SIZE


        return [point1, point2, point3, point4, point5, point6, point7]
        
