"""
Perform the special algorithm on the data set.
"""

import statistics

def get_average(data):
    """ Get the median of the data
    """
    return statistics.median(data)


def do_algorithm(data):
    """ Perform the special algorithm on the data.
    """
    return get_average(data)


def main():
    data = [1, 1, 2, 3, 5, 8, 13, 21]

    result = do_algorithm(data)

    print(f"The result is: {result}")


if __name__ == "__main__":
    main()
