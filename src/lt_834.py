"""
https://leetcode.com/contest/weekly-contest-84/problems/sum-of-distances-in-tree/
"""

"""
An undirected, connected tree with N nodes labelled 0...N-1 and N-1 edges are given.

The ith edge connects nodes edges[i][0] and edges[i][1] together.

Return a list ans, where ans[i] is the sum of the distances between node i and all other nodes.

Example 1:

Input: N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation: 
Here is a diagram of the given tree:
  0
 / \
1   2
   /|\
  3 4 5
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.  Hence, answer[0] = 8, and so on.

Note: 1 <= N <= 10000
"""

import collections

class Solution:
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # Time: O(n)
        # Space: O(n)
        # https://leetcode.com/problems/sum-of-distances-in-tree/discuss/130583/Pre-order-and-Post-order-DFS-O(N)
        # Hints:
        # 1) Use 0 as the root
        # 2) Calculate the shifts when selecting different roots
        # 3) Let A be a root, and B be a subtree of A
        # 4) count_nodes(n) = the number of nodes when n is the root
        # 5) count_distances(n) = the sum of distances when n is the root
        # 6) count_distances(B) = count_distances(A) - count_nodes(B) + (N - count_nodes(B))
        #                       = count_distances(A) + N - 2 * count_distances(B)
        tree = collections.defaultdict(set)
        output = [0] * N  # sum of distance in subtree
        counts = [0] * N  # the number of nodes
        for i, j in edges:
            tree[i].add(j)
            tree[j].add(i)

        def count_nodes(root, visited=set()):
            visited.add(root)
            for node in [n for n in tree[root] if n not in visited]:
                count_nodes(node, visited)
                counts[root] += counts[node]
                # count the distances from the root of a subtree
                # =the number of nodes in a subtree
                output[root] += output[node] + counts[node]
            counts[root] += 1

        def count_distances(root, visited=set()):
            visited.add(root)
            for node in [n for n in tree[root] if n not in visited]:
                output[node] = output[root] + N - 2 * counts[node]
                count_distances(node, visited)
        count_nodes(0)
        count_distances(0)
        return output

    def sumOfDistancesInTree_TLE(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        class TreeNode:
            def __init__(self, val):
                self.val = val
                self.links = []
        def search(node):
            visited = set([node])
            queue = [node]
            distance = 1
            total = 0
            while queue:
                tmp = []
                for current in queue:
                    links = [x for x in current.links if x not in visited]
                    total += len(links) * distance
                    visited.update(links)
                    tmp += links
                queue = tmp
                distance += 1
            return total
        if not any(edges): return [0] * N
        records = {}
        for e_in, e_out in edges:
            if e_in not in records: records[e_in] = TreeNode(e_in)
            if e_out not in records: records[e_out] = TreeNode(e_out)
            n1 = records[e_in]
            n2 = records[e_out]
            n1.links.append(n2)
            n2.links.append(n1)
        return [search(records[n]) for n in range(N)]
         
        
        
if __name__ == '__main__':
    test_cases = [
        ((1, []), [0]),
        ((6, [[0,1],[0,2],[2,3],[2,4],[2,5]]), [8,12,6,10,10,10]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().sumOfDistancesInTree(*test_case[0])
        print('output:', output)
        assert output == test_case[1]
