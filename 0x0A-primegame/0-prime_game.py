#!/usr/bin/python3
"""
Return: name of the player that won the most rounds
"""


def isPrime(x):
    """Determine if x is prime or not"""
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def primeGame(n):
    """PrimeGame"""
    numbers = list(range(2, n + 1))
    player1 = True
    player2 = False

    while True:
        if player1:
            for num in numbers:
                if isPrime(num):
                    numbers = [x for x in numbers if x % num != 0]
                    break
            else:
                return "Ben"
        else:
            for num in numbers:
                if isPrime(num):
                    numbers = [x for x in numbers if x % num != 0]
                    break
            else:
                return "Maria"

        player1 = not player1
        player2 = not player2


def isWinner(x, nums):
    """Returns winner in the primeGame"""
    if x <= 0 or type(nums[0] != int):
        return None

    maria_score = 0
    ben_score = 0

    for n in nums:
        result = primeGame(n)
        if result == "Maria":
            maria_score += 1
        elif result == "Ben":
            ben_score += 1

    if maria_score > ben_score:
        return "Maria"
    elif ben_score > maria_score:
        return "Ben"
    else:
        return None
