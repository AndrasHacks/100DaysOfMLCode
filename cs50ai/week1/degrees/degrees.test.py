import unittest
degrees = __import__('degrees')


class DegreesTests(unittest.TestCase):
    # If the frontier cannot be populated more, and becomes empty
    # then the search returns None.
    def test_frontier_empty_returns_None(self):
        test_person_id = 0
        degrees.people[test_person_id] = {"movies": []}
        result = degrees.shortest_path(test_person_id, 1)
        self.assertIsNone(result)

    # If target is not laoded, then the search should return None.
    def test_target_is_not_loaded_retruns_None(self):
        degrees.movies[0] = {"stars": [0, 1]}
        degrees.people[0] = {"movies": [0]}
        degrees.people[1] = {"movies": [0]}
        result = degrees.shortest_path(0, 2)
        self.assertIsNone(result)

    # Tests whether the algorithm fins the path or not.
    def test_tagret_is_found_returns_path(self):
        degrees.movies[0] = {"stars": [0, 1]}
        degrees.movies[1] = {"stars": [1, 2]}
        degrees.people[0] = {"movies": [0]}
        degrees.people[1] = {"movies": [0, 1]}
        degrees.people[2] = {"movies": [1]}
        result = degrees.shortest_path(0, 2)
        result = [(None, 0)] + result
        self.assertEqual([(None, 0), (0, 1), (1, 2)], result)

    # Tests whether the algorithm find the shortest path or not.
    def test_shortest_path_found_from_two_paths(self):
        degrees.movies[0] = {"stars": [1, 0]}
        degrees.movies[1] = {"stars": [2, 1]}
        degrees.movies[2] = {"stars": [3, 1]}
        degrees.movies[3] = {"stars": [3, 2]}
        degrees.people[0] = {"movies": [0]}
        degrees.people[1] = {"movies": [2, 1, 0]}
        degrees.people[2] = {"movies": [3, 1]}
        degrees.people[3] = {"movies": [3, 2]}
        result = degrees.shortest_path(0, 2)
        result = [(None, 0)] + result
        self.assertEqual([(None, 0), (0, 1), (1, 2)], result)


if __name__ == '__main__':
    unittest.main()
