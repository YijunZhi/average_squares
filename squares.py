"""Computation of weighted average of squares."""
import argparse

def average_of_squares(list_of_numbers, list_of_weights=None):
    """ Return the weighted average of a list of values.
    
    By default, all values are equally weighted, but this can be changed
    by the list_of_weights argument.
    
    Example:
    --------
    >>> average_of_squares([1, 2, 4])
    7.0
    >>> average_of_squares([2, 4], [1, 0.5])
    6.0
    >>> average_of_squares([1, 2, 4], [1, 0.5])
    Traceback (most recent call last):
    AssertionError: weights and numbers must have same length

    """
    if list_of_weights is not None:
        assert len(list_of_weights) == len(list_of_numbers), \
            "weights and numbers must have same length"
        effective_weights = list_of_weights
    else:
        effective_weights = [1] * len(list_of_numbers)
    squares = [
        weight * number * number
        for number, weight
        in zip(list_of_numbers, effective_weights)
    ]
    return sum(squares) / len(list_of_numbers)


def convert_numbers(list_of_strings):
    """Convert a list of strings into numbers, ignoring whitespace.
    
    Example:
    --------
    >>> convert_numbers(["4", " 8 ", "15 16", " 23    42 "])
    [4, 8, 15, 16, 23, 42]

    """
    all_numbers = []
    for s in list_of_strings:
        # Take each string in the list, split it into substrings separated by
        # whitespace, and collect them into a single list...
        all_numbers.extend([token.strip() for token in s.split()])
    # ...then convert each substring into a number
    result = []
    for number_string in all_numbers:
        try:
            result.append(int(number_string))   # 能整型就整型
        except ValueError:
            result.append(float(number_string)) # 否则再用 float
    return result

def read_numbers_from_file(filename):
    """Read numbers from a text file and return a list of numbers.

    The file can contain numbers separated by whitespace (spaces or newlines).
    """
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()       # 每一行是一个字符串

    # 利用你已有的 convert_numbers，把这些字符串变成数字列表
    return convert_numbers(lines)


def parse_args():

    parser = argparse.ArgumentParser(
        description="Compute the (weighted) average of squares from files."
    )

    # 位置参数：numbers 文件名
    parser.add_argument(
        "numbers_file",
        help="Text file containing the numbers (one per line or separated by spaces).",
    )

    # 可选参数：weights 文件名（还是叫 --weights，按题目要求）
    parser.add_argument(
        "--weights",
        dest="weights_file",
        help="Optional text file containing the weights.",
    )

    return parser.parse_args()



if __name__ == "__main__":
    
    args = parse_args()

    # 1. 从 numbers 文件读数字
    list_of_numbers = read_numbers_from_file(args.numbers_file)

    # 2. 如果给了 weights 文件，也读出来；否则用 None（等权重）
    if args.weights_file is None:
        list_of_weights = None
    else:
        list_of_weights = read_numbers_from_file(args.weights_file)

    # 3. 调用平均平方函数
    result = average_of_squares(list_of_numbers, list_of_weights)

    # 4. 打印结果
    print(result)

