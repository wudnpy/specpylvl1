#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import weakref
from collections import UserDict

from profiling import timing

from .read_nodes import read_nodes
from .read_links import read_links

__all__ = ('read_all', )

class CorruptedData(Exception): pass


@timing
def read_all(path, nodes='nodes.csv', links='links.csv'):

    nodes_path = os.path.join(path, nodes)
    links_path = os.path.join(path, links)

    Graph = {}
    Names = {}

    for number, name in read_nodes(nodes_path):
        Node = UserDict({
            'number': number,
            'name': name,
            'neighbours': dict(),
            'prohibited': set()
        })
        Graph[number] = Node
        if name in Names:
            raise CorruptedData('{0} already exists {1}'.format(name, number))# собственное исключение + операция форматирования строки
        Names[name] = Node

    for n1, n2, penalty in read_links(links_path):
        Node1 = Graph[n1]
        Node2 = Graph[n2]
        Node1['neighbours'][n2] = (penalty, weakref.ref(Node2))
        Node2['neighbours'][n1] = (penalty, weakref.ref(Node1))

    return Graph, Names