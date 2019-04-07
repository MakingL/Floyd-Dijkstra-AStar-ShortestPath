# -*- coding: utf-8 -*-
# @Time    : 2019/4/5 19:33
# @Author  : MLee
# @File    : test.py
import time

from AStar.AStar import AStar
from Dijkstra.Dijkstra import Dijkstra
from Floyd.Floyd import Floyd
from Graph.GraphConf import Road, Graph


def load_data_and_build_graph(road_path, graph):
    """
    导入输入数据并构建图
    :return:
    """

    # 读取边的信息，建图
    road_count = 0
    with open(road_path, 'r') as road_file:
        for line in road_file:
            line = line.strip(" \n()")
            if line.startswith("#"):
                continue
            data = line.replace(" ", "").replace("\t", "")
            road_id, road_len, speed_limit, chanel, start_id, end_id, bilateral = data.split(",")
            road_len, speed_limit, chanel = int(road_len), int(speed_limit), int(chanel)
            road_conf = road_id, road_len, speed_limit, chanel, start_id, end_id

            new_road = Road(road_conf)
            # 正向边添加到图中
            graph.add_edge(start_id, road_id, new_road)
            road_count += 1

            if bilateral == "1":
                # 反向边的 id 为 “正向边 id_b”
                back_road_id = "{}_b".format(road_id)
                road_conf = back_road_id, road_len, speed_limit, chanel, end_id, start_id

                new_road = Road(road_conf)
                # 反向边添加到图中
                graph.add_edge(end_id, back_road_id, new_road)


if __name__ == '__main__':
    road_data_path = "./data/road.txt"
    graphObj = Graph()
    load_data_and_build_graph(road_data_path, graphObj)
    print("max edge weight: {}".format(graphObj.max_weight))
    print("mini edge weight: {}".format(graphObj.min_weight))
    print("average edge weight: {}".format(graphObj.get_average_weight()))
    print()

    floyd = Floyd(graphObj)
    dijkstra = Dijkstra(graphObj)
    a_star = AStar(graphObj, floyd, gama=0.4)

    sourceNode = "7"
    dstNode = "1957"
    shortest_path, floydCost = floyd.get_shortest_path(sourceNode, dstNode)
    print("Floyd path: {} Floyd cost: {}".format(shortest_path, floydCost))

    last_cost = 0

    dijkstraPath = []
    dijkstraCost = 0
    start_time = time.clock()
    for i in range(100):
        dijkstraPath, dijkstraCost = dijkstra.dijkstra_search(sourceNode, dstNode)
    end_time = time.clock()
    dijkstra_time_cost = end_time - start_time

    aStarPath = []
    aStarCost = 0
    start_time = time.clock()
    for i in range(100):
        aStarPath, aStarCost = a_star.aStar(sourceNode, dstNode)
    end_time = time.clock()
    a_star_time_cost = end_time - start_time

    if dijkstraCost != aStarCost:
        print("Dijkstra cost is not equal a star cost\n")

    print("Dijkstra path: {} dijkstra cost: {}, spent time: {}".format(dijkstraPath, dijkstraCost, dijkstra_time_cost))
    print("AStar path: {} AStar cost: {}, spent time: {}".format(aStarPath, aStarCost, a_star_time_cost))

    print()
    print("Dijkstra cost time is slower than AStar: {}".format(dijkstra_time_cost - a_star_time_cost))
