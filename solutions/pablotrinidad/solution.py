"""Solution by pablotrinidad."""


class Solution:
    """Solution to the Fibonacci problem."""

    def __init__(self):
        self.mem = [0, 1]

    def fib(self, n: int) -> int: # pylint: disable=C0103
        """Returns the n-th fibonacci number."""
        if n == 0:
            return 0
        if n == 1:
            return 1

        a, b = 1, 1 # pylint: disable=C0103
        for _ in range(2, n):
            a, b = b, a + b # pylint: disable=C0103
        return b
