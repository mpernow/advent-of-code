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
    matches = re.finditer(
        r"(?=(X.{"
        + str(col_length - 1)
        + r"}M.{"
        + str(col_length - 1)
        + r"}A.{"
        + str(col_length - 1)
        + r"}S|S.{"
        + str(col_length - 1)
        + r"}A.{"
        + str(col_length - 1)
        + r"}M.{"
        + str(col_length - 1)
        + r"}X))",
        wordsearch,
    )
    return sum(match.start() // col_length < col_length - 3 for match in matches)


def get_number_right_diagonal(wordsearch, row_length):
    # Use regex lookahead assertion to get overlapping
    matches = re.finditer(
        r"(?=(X.{"
        + str(row_length)
        + r"}M.{"
        + str(row_length)
        + r"}A.{"
        + str(row_length)
        + r"}S|S.{"
        + str(row_length)
        + r"}A.{"
        + str(row_length)
        + r"}M.{"
        + str(row_length)
        + r"}X))",
        wordsearch,
    )
    return sum(
        (match.start() // row_length < row_length - 3)
        and (match.start() % row_length < row_length - 3)
        for match in matches
    )


def get_number_left_diagonal(wordsearch, row_length):
    # Use regex lookahead assertion to get overlapping
    matches = re.finditer(
        r"(?=(X.{"
        + str(row_length - 2)
        + r"}M.{"
        + str(row_length - 2)
        + r"}A.{"
        + str(row_length - 2)
        + r"}S|S.{"
        + str(row_length - 2)
        + r"}A.{"
        + str(row_length - 2)
        + r"}M.{"
        + str(row_length - 2)
        + r"}X))",
        wordsearch,
    )
    return sum(
        (match.start() // row_length < row_length - 3)
        and (match.start() % row_length > 2)
        for match in matches
    )


def get_number_crosses(wordsearch, side_length):
    matches = re.finditer(
        r"(?=(M.S.{"
        + str(side_length - 2)
        + r"}A.{"
        + str(side_length - 2)
        + r"}M.S))|"
        + r"(?=(S.S.{"
        + str(side_length - 2)
        + r"}A.{"
        + str(side_length - 2)
        + r"}M.M))|"
        + r"(?=(M.M.{"
        + str(side_length - 2)
        + r"}A.{"
        + str(side_length - 2)
        + r"}S.S))|"
        + r"(?=(S.M.{"
        + str(side_length - 2)
        + r"}A.{"
        + str(side_length - 2)
        + r"}S.M))",
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
