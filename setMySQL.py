"""
@ encoding:utf-8
@ author:nxc
@ GitHub:
@ 建立语料库
"""

import pandas as pd
from py2neo import Graph, Node, Relationship


class SearchGraph:
    def __init__(self):
        self.data_path = r'searchData.csv'
        self.graph = Graph(r"http://localhost:7474", username="SearchGraph", password="1234")

    def read_csv(self):
        search_data = pd.read_csv(self.data_path, encoding='utf-8', header=None)


def main():
    search_graph = SearchGraph()
    search_graph.read_csv()
    print('success')
    pass


if __name__ == '__main__':
    main()
