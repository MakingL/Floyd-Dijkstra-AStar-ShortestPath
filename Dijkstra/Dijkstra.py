# -*- coding: utf-8 -*-
# @Time    : 2019/3/26 9:47
# @Author  : MLee
# @File    : Dijkstra.py
import heapq
from collections import deque


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

    def clear(self):
        return self.elements.clear()

    def size(self):
        return len(self.elements)


class Dijkstra(object):
    """docstring for Dijkstra"""

    def __init__(self, graph):
        super(Dijkstra, self).__init__()
        self.graph = graph

    def get_neighbors(self, current):
        return self.graph.get_neighbors(current)

    def dijkstra_search(self, start, goal):
        frontier = PriorityQueue()
        frontier.clear()
        frontier.put(start, 0)
        came_from = {}
        cost_so_far = dict()
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            current = frontier.get()

            if current == goal:
                break

            for edge_id, edge in self.get_neighbors(current).items():
                next_node_id = edge.end_id
                new_cost = cost_so_far[current] + self.cost(edge)
                if next_node_id not in cost_so_far or new_cost < cost_so_far[next_node_id]:
                    cost_so_far[next_node_id] = new_cost
                    priority = new_cost
                    frontier.put(next_node_id, priority)
                    came_from[next_node_id] = current

        return self.reconstruct_path(came_from, goal), cost_so_far[goal]

    def cost(self, edge):
        return edge.weight

    def reconstruct_path(self, came_from, goal):
        """
            重新建立路径完整信息
            :param came_from: 节点的父节点集合
            :param goal: 目标节点
            :return: 包含源节点 ID 到目标节点 ID 的路径
        """
        path = deque()
        path.clear()
        node = goal
        path.appendleft(node)
        while node in came_from:
            node = came_from[node]
            if node is None:
                continue
            path.appendleft(node)
        return path

