"""
https://leetcode.com/contest/weekly-contest-87/problems/shortest-path-visiting-all-nodes/
"""

"""
An undirected, connected graph of N nodes (labeled 0, 1, 2, ..., N-1) is given as graph.

graph.length = N, and j != i is in the list graph[i] exactly once, if and only if nodes i and j are connected.

Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.

 

Example 1:

Input: [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]

Example 2:

Input: [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output: 4
Explanation: One possible path is [0,1,4,2,3]

 

Note:

    1 <= graph.length <= 12
    0 <= graph[i].length < graph.length
"""

class Solution:
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        def traverse(queue):
            while queue:
                current_node, visited, current_length = queue.pop(0)
                if len(visited) == len(graph):
                    return current_length
                for neighbor in graph[current_node]:
                    queue.append((neighbor, visited | set([neighbor]), current_length + 1))
        num_edges = float('inf') 
        endpoints = []
        for node_id in range(len(graph)):
            node_edges = graph[node_id]
            if len(node_edges) < num_edges:
                endpoints = [node_id]
                num_edges = len(node_edges)
            elif len(node_edges) == num_edges:
                endpoints.append(node_id)
        queue = []
        print(endpoints)
        for node_id in endpoints[1:2]:
            queue.append((node_id, set([node_id]), 0))
        return traverse([x for x in queue]) 
        

if __name__ == '__main__':
    test_cases = [
        #([[1,2,3],[0],[0],[0]], 4),
        #([[1],[0,2,4],[1,3,4],[2],[1,2]], 4),
        #([[1],[0,2],[1,3],[2],[1,5],[4]], 6),
        #([[1],[0,2,6],[1,3],[2],[5],[4,6],[1,5,7],[6]], 9),
        ([[1,4,6,8,9],[0,6],[9],[5],[0],[7,3],[0,1],[9,5],[0],[0,2,7]], 10),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().shortestPathLength(test_case[0])
        print('output:', output)
        assert output == test_case[1]
