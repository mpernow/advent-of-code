import pathlib
import re

INPUT_PATH = pathlib.Path(__file__).parent.parent.parent / "input"


def get_wordsearch():
    return open(INPUT_PATH / "04").read()


def get_number_horizontal(wordsearch, row_length):
    # Use regex lookahead assertion to get overlapping
    matches = re.finditer(r"(?=(XMAS|SAMX))", wordsearch)
    # Only count those that are wholly inside the array
    return sum(match.start() % row_length < row_length - 3 for match in matches)


def get_number_vertical(wordsearch, col_length):
    # Use regex lookahead assertion to get overlapping
    num_between = col_length - 1
    matches = re.finditer(
        rf"(?=(X.{{{num_between}}}M.{{{num_between}}}A.{{{num_between}}}S|S.{{{num_between}}}A.{{{num_between}}}M.{{{num_between}}}X))",
        wordsearch,
    )
    return sum(match.start() // col_length < col_length - 3 for match in matches)


def get_number_right_diagonal(wordsearch, row_length):
    # Use regex lookahead assertion to get overlapping
    num_betwen = row_length
    matches = re.finditer(
        rf"(?=(X.{{{num_betwen}}}M.{{{num_betwen}}}A.{{{num_betwen}}}S|S.{{{num_betwen}}}A.{{{num_betwen}}}M.{{{num_betwen}}}X))",
        wordsearch,
    )
    return sum(
        (match.start() // row_length < row_length - 3)
        and (match.start() % row_length < row_length - 3)
        for match in matches
    )


def get_number_left_diagonal(wordsearch, row_length):
    # Use regex lookahead assertion to get overlapping
    num_between = row_length - 2
    matches = re.finditer(
        rf"(?=(X.{{{num_between}}}M.{{{num_between}}}A.{{{num_between}}}S|S.{{{num_between}}}A.{{{num_between}}}M.{{{num_between}}}X))",
        wordsearch,
    )
    return sum(
        (match.start() // row_length < row_length - 3)
        and (match.start() % row_length > 2)
        for match in matches
    )


def get_number_crosses(wordsearch, side_length):
    num_between = side_length - 2
    matches = re.finditer(
        rf"(?=(M.S.{{{num_between}}}A.{{{num_between}}}M.S))|"
        + rf"(?=(S.S.{{{num_between}}}A.{{{num_between}}}M.M))|"
        + rf"(?=(M.M.{{{num_between}}}A.{{{num_between}}}S.S))|"
        + rf"(?=(S.M.{{{num_between}}}A.{{{num_between}}}S.M))",
        wordsearch,
    )
    return sum(
        (match.start() // side_length < side_length - 2)
        and (match.start() % side_length < side_length - 2)
        for match in matches
    )


def part1():
    wordsearch = get_wordsearch()
    side_length = wordsearch.find("\n")  # input is square
    wordsearch = wordsearch.replace("\n", "")
    print(
        get_number_horizontal(wordsearch, side_length)
        + get_number_vertical(wordsearch, side_length)
        + get_number_left_diagonal(wordsearch, side_length)
        + get_number_right_diagonal(wordsearch, side_length)
    )


def part2():
    wordsearch = get_wordsearch()
    side_length = wordsearch.find("\n")  # input is square
    wordsearch = wordsearch.replace("\n", "")
    print(get_number_crosses(wordsearch, side_length))


if __name__ == "__main__":
    part1()
    part2()
