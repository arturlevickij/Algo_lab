from unittest import TestCase, main
from career import max_experience, build_organization_graph

class TestCareerGraph(TestCase):
    def test_career_graph_1(self):
        levels = [
            [4],
            [3, 1],
            [2, 1, 5],
            [1, 3, 2, 1]
        ]
        organization_graph = build_organization_graph(levels)
        result = max_experience(organization_graph)
        self.assertEqual(result, 12)

    def test_max_experience_with_negative_values(self):
        levels = [
            [0],
            [1, 1],
            [0, 0, 0],
            [1, 1, 1, 1],
            [0, 1, 0, 1, 0]
        ]
        organization_graph = build_organization_graph(levels)
        result = max_experience(organization_graph)
        self.assertEqual(result, 3)

    def test_max_experience_with_empty_graph(self):
        levels = []
        organization_graph = build_organization_graph(levels)
        result = max_experience(organization_graph)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    main()