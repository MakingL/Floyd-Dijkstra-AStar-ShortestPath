# -*- coding: utf-8 -*-
# @Time    : 2019/3/27 9:48
# @Author  : MLee
# @File    : Floyd.py
# import logging


class Floyd(object):
    """docstring for Floyd"""

    def __init__(self, graph):
        super(Floyd, self).__init__()
        self.graph = graph
        # self.INF = float("inf")
        self.INF = 0x3f3f3f3f
        # self.INF = 100
        self.dist = dict(dict())

        # 构建邻接矩阵
        for start_id in self.graph.vertex_set:
            if start_id not in self.dist:
                self.dist[start_id] = dict()

            for end_id in self.graph.vertex_set:
                if start_id == end_id:
                    self.dist[start_id][end_id] = 0

                if start_id in self.graph.graph_adjacent_dict and \
                        end_id in self.graph.graph_adjacent_dict[start_id]:
                    self.dist[start_id][end_id] = 1
                else:
                    self.dist[start_id][end_id] = self.INF
        # 利用 Floyd 算法求出任意两点间最短路长
        self.floyd_search()
        # self.print_dist_info()

    def floyd_search(self):
        # print(self.graph.vertex_set)

        vertex_list = self.graph.get_vertex_list()
        vertex_list.sort()
        # print(vertex_list)

        for start in vertex_list:
            for end in vertex_list:
                for mid in vertex_list:
                    self.dist[start][end] = min(self.dist[start][end], self.dist[start][mid] + self.dist[mid][end])

    # def print_dist_info(self):
    #     for start_id in self.graph.vertex_set:
    #         for end_id in self.graph.vertex_set:
    #             logging.info("dist[{}][{}]: {}".format(start_id, end_id, self.dist[start_id][end_id]))

    def get_dist(self, start_id, end_id):
        return self.dist[start_id][end_id]
