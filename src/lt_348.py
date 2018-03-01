"""
https://leetcode.com/problems/design-tic-tac-toe

Related:

Complexity:
  - Time: O()
  - Space: O()
"""

"""
Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

    A move is guaranteed to be valid and is placed on an empty block.
    Once a winning condition is reached, no more moves is allowed.
    A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.

Example:

Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

TicTacToe toe = new TicTacToe(3);

toe.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

toe.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

toe.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

toe.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

toe.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

toe.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|

Follow up:
Could you do better than O(n2) per move() operation? 
"""

class TicTacToe:

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        # extra two for the diagonal lines
        self.track = [set() for _ in range(2*n+2)]
        self.records = [[0] * n for _ in range(n)]
        self.count = 0

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        if row >= self.n or col >= self.n or row < 0 or col < 0: raise Exception("Illegal movement due to out of space")
        if self.records[row][col]: raise Exception("Illegal movement due to repitition")

        self.records[row][col] = player
        self.track[row].add(player)
        self.track[self.n + col].add(player)
        if row == col:
            self.track[-2].add(player)
        if row + col == self.n - 1:
            self.track[-1].add(player)

        if len(self.track[row]) == 1 and all(map(lambda n: n == player, self.records[row])):
            return player
        elif len(self.track[self.n + col]) == 1 and all(map(lambda n: n == player, [row[col] for row in self.records])):
            return player
        elif len(self.track[-2]) == 1 and all(map(lambda n: n == player, [self.records[n][n] for n in range(self.n)])):
            return player
        elif len(self.track[-1]) == 1 and all(map(lambda n: n == player, [self.records[n][self.n - n - 1]for n in range(self.n)])):
            return player
        else:
            return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

if __name__ == '__main__':
    test_cases = [
        ((3, [(0, 1, 2), [2, 1, 2], [1, 1, 2]]), 2),
        ((3, [(0, 0, 1), (0, 2, 2), (2, 2, 1), (1, 1, 2), (2, 0, 1), (1, 0, 2), (2, 1, 1)]), 1),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        n, steps = test_case[0]
        obj = TicTacToe(n)
        for step in steps[:-1]:
            result = obj.move(*step)
            if result != 0:
                assert False
        output = obj.move(*steps[-1])
        print('output:', output)
        assert output == test_case[1]

