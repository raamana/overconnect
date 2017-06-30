from numpy import ones


def over_connect(number_of_nodes=42):
    """
    Returns an over-connected graph for an arbitrary size.
    Default size is 42, which is the answer to everything.
    The R/C order doesn't matter due to over-connectivity.
    """

    return ones([number_of_nodes, number_of_nodes])


if __name__ == '__main__':
    over_connect()