import pathlib
import re

INPUT_PATH = pathlib.Path(__file__).parent.parent.parent / "input"


def get_wordsearch():
    return open(INPUT_PATH / "04").read()


def get_number_horizontal(wordsearch, row_length):
    # Use regex lookahead assertion to get overlapping
    matches = re.finditer(r"(?=(XMAS|SAMX))", wordsearch)
    num = 0
    for match in matches:
        # Remove those that wrap around
        if match.start() % row_length < row_length - 3:
            num += 1
    return num


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
    num = 0
    for match in matches:
        # Remove those that wrap around
        if match.start() // col_length < col_length - 3:
            num += 1
    return num


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
    num = 0
    for match in matches:
        # Remove those that wrap around
        if (match.start() // row_length < row_length - 3) and (
            match.start() % row_length < row_length - 3
        ):
            num += 1
    return num


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
    num = 0
    for match in matches:
        # Remove those that wrap around
        if (match.start() // row_length < row_length - 3) and (
            match.start() % row_length > 2
        ):
            num += 1
    return num


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
    num = 0
    for match in matches:
        if (match.start() // side_length < side_length - 2) and (
            match.start() % side_length < side_length - 2
        ):
            num += 1
    return num


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
