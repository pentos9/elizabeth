#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : hash_ring.py
# @Author: lucas
# @Date  : 3/26/19
# @Desc  :


import hashlib

from pprint import pprint


class HashRing(object):
    def __init__(self, nodes=None, replicas=5):
        self.ring = dict()
        self.replicas = replicas
        self._sorted_keys = []

        if nodes:
            for node in nodes:
                self.add_node(node)

    def add_node(self, node):
        for i in range(0, self.replicas):
            key = self.gen_key("%s:%s" % (node, i))
            self.ring[key] = node
            self._sorted_keys.append(key)

        self._sorted_keys.sort()

    def remove(self, node):
        for i in range(0, self.replicas):
            key = self.gen_key("%s:%s" % (node, i))
            del self.ring[key]
            self._sorted_keys.remove(key)

    def get_node(self, string_key):
        return self.get_node_position(string_key)[0]

    def get_node_position(self, string_key):

        if not self.ring:
            return None, None

        key = self.gen_key(string_key)
        nodes = self._sorted_keys

        for i in range(0, len(nodes)):
            node = nodes[i]
            if key <= node:
                return self.ring[node], i

        return self.ring[nodes[0]], 0

    def get_nodes(self, string_key):

        if not self.ring:
            return None, None

        node, pos = self.get_node_position(string_key)
        for key in self._sorted_keys[pos:]:
            yield self.ring[key]

        while True:
            for key in self._sorted_keys:
                yield self.ring[key]

    def gen_key(self, key):
        m = hashlib.md5()
        m.update(key.encode('utf-8'))
        return int(m.hexdigest(), 16)


def run():
    hash_ring = HashRing()

    ip_pattern = '127.0.0.%s'
    for i in range(1, 21):
        ip = ip_pattern % i
        hash_ring.add_node(ip)

    for node in hash_ring.get_nodes('12123'):
        pprint(node)


if __name__ == '__main__':
    run()
