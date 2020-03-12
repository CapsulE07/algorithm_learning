
from typing import List

def prim(matrix:List[List[int]]):
    visited:List[int]=[0]
    parents:List[int]=[-1]*len(matrix)
    from_index =0
    to_index = 0
    while len(visited)< len(matrix):
        min_weight = 1 << 10
        count = 0
        for idx in visited:
            for i in range(len(matrix)):
                if i not in visited:
                    if matrix[idx][i] < min_weight and matrix[idx][i]:
                        min_weight = matrix[idx][i]
                        from_index = idx
                        to_index = i
       
        parents[to_index] = from_index
        visited.append(to_index)
        print("visited:", visited)
    return parents


import unittest
class TestMain(unittest.TestCase):

    def test_prim(self):
        _ = 1 << 10
        graph = [
        [0, 6, 3, _, _, _],
        [6, 0, 2, 5, _, _],
        [3, 2, 0, 3, 4, _],
        [_, 5, 3, 0, 2, 3],
        [_, _, 4, 2, 0, 5],
        [_, _, _, 3, 5, 0],
    ]
        res = prim(graph)
        print(res)

if __name__ == '__main__':
    unittest.main()
    # test_prim()