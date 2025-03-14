import random

def randomList(size, limit=1000):
    """
    Generates a list of random integers.

    :param size: Number of elements in the list.
    :param limit: Upper bound for the random values (default is 1000).
    :return: List containing randomly generated integers within the specified range.
    """
    return [random.randint(0, limit) for _ in range(size)]