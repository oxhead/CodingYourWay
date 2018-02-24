import sys

def coin_change(coins, amount):
    # initialize the tables for dynamic programming
    sols = [sys.maxsize-1] * (amount+1)
    sols[0] = 0

    # start from the small amount
    # fill out the table from 0 to the amount
    for total in range(amount+1):
        for coin in coins:
            # calculate the solution for the subproblem 
            if (total + coin <= amount):
                sols[total + coin] = min(sols[total + coin], sols[total] + 1)
                
    # if no solution found, return -1
    return -1 if sols[amount] == sys.maxsize-1 else sols[amount]



if __name__ == '__main__':
    test_cases = [
        ([25, 20, 5, 1], 127, 7),
        ([25, 20, 4, 1], 121, 6),
        ([50, 45, 10, 2], 3, -1),
        ([50, 45, 10, 2], 92, 3)
    ]

    for test_case in test_cases:
        coins, amount, expected = test_case
        result = coin_change(coins, amount)
        print(coins, amount, expected, result)
        assert result == expected

    
        
