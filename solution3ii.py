# By Pooja Singh

from itertools import product


def a_condition(candidate, condition):
    common_elements = [digit for digit in candidate if digit in condition]
    return (len(common_elements) == 1) and (
        candidate.index(common_elements[0]) != condition.index(common_elements[0])
    )


def b_condition(candidate):
    condition = (6, 8, 2)
    common_elements = [digit for digit in candidate if digit in condition]
    return (len(common_elements) == 1) and (
        candidate.index(common_elements[0]) == condition.index(common_elements[0])
    )


def c_condition(candidate):
    condition = (2, 0, 6)
    common_elements = [digit for digit in candidate if digit in condition]
    if len(common_elements) != 2:
        return False
    for digit in common_elements:
        if candidate.index(digit) == condition.index(digit):
            return False
    return True

def d_condition(candidate):
    condition = (7, 3, 8)
    common_elements = [digit for digit in candidate if digit in condition]
    return len(common_elements) == 0


def find_code():
    # for completeness test all possible permutations with repetition of digits for length 3.
    # We can further optimize by eliminating 0,5,2,3 from the possible candidate calculation.
    for candidate in product(range(10), repeat=3):
        if (
            a_condition(candidate, (6, 1, 4))
            and b_condition(candidate)
            and c_condition(candidate)
            and d_condition(candidate)
            and a_condition(candidate, (3, 8, 0))
        ):
            return "".join(map(str, candidate))
    return "No solution found."


if __name__ == "__main__":
    print("The code from puzzle2 is: ", find_code())
