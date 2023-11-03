from unittest import TestCase, main
from graph import directed_graph

class TestDirectedGraph(TestCase):
    def test_directed_graph_1(self):
        graph = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F'],
            'D': ['G'],
            'E': [],
            'F': [],
            'G': []
        }
        self.assertEqual(directed_graph(graph), 'A')

    def test_directed_graph_2(self):
        graph = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F'],
            'D': ['G'],
            'E': ['A'],  # A cycle is introduced here
            'F': [],
            'G': []
        }
        self.assertEqual(directed_graph(graph), -1)

    def test_directed_graph_3(self):
        graph = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F'],
            'D': ['G'],
            'E': ['F'],
            'F': [],
            'G': []
        }
        self.assertEqual(directed_graph(graph), 'A')

    def test_directed_graph_4(self):
        graph = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F'],
            'D': ['G'],
            'E': ['F'],
            'F': ['A'],  # A cycle is introduced here
            'G': []
        }
        self.assertEqual(directed_graph(graph), -1)

    def test_directed_graph_5(self):
        graph = {
            'A': ['B'],
            'B': ['C'],
            'C': ['D'],
            'D': ['E'],
            'E': ['F'],
            'F': ['G'],
            'G': ['H'],
            'H': []
        }
        self.assertEqual(directed_graph(graph), 'A')

    def test_directed_graph_6(self):
        graph = {
            'A': ['E'],
            'B': ['A', 'C'],
            'C': ['D', 'B'],
            'D': ['B', 'C'],
            'E': ['D']
        }
        self.assertEqual(directed_graph(graph), 'A')

if __name__ == '__main__':
    main()
