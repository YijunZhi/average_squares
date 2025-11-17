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

def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Compute the (weighted) average of squares."
    )
    # 位置参数：一串 numbers
    parser.add_argument(
        "numbers",
        nargs="+",      # 至少 1 个，可以很多个
        help="Numbers whose squares will be averaged.",
    )
    parser.add_argument(
        "--weights",
        nargs="+",   # 0.1 2 0.1 这样的多值
        help="Optional weights for each number.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    # 1. 解析命令行拿到字符串形式的 numbers
    args = parse_args()

    # 2. 用你写好的 convert_numbers 把字符串变成数字列表
    list_of_numbers = convert_numbers(args.numbers)

    # 3. 处理可选的 weights
    if args.weights is None:
        list_of_weights = None          # 不给就走默认等权重
    else:
        list_of_weights = convert_numbers(args.weights)

    # 4. 调用 average_of_squares，weights 不传，默认为 None（等权重）
    result = average_of_squares(list_of_numbers)

    # 5. print the outcome
    print(result)
