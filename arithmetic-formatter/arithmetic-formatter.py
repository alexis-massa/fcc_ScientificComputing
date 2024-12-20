def arithmetic_arranger(problems: list[str], show_answers: bool = False) -> str:
    """
    Arrange arithmetic problems vertically for display.

    Args:
    -----
        problems (list[str]): List of arithmetic problems in the form "num1 operator num2".
        show_answers (bool): Whether to include the solutions.

    Returns:
    --------
        str: Formatted string of arranged problems or an error message.
    """
    if len(problems) > 5:
        return "Error: Too many problems."

    top, bottom, lines, results = [], [], [], []

    for problem in problems:
        num1, operator, num2 = problem.split()
        if operator not in ("+", "-"):
            return "Error: Operator must be '+' or '-'."
        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(num1), len(num2)) + 2  # Dynamic width for alignment
        top.append(num1.rjust(width))
        bottom.append(operator + num2.rjust(width - 1))
        lines.append("-" * width)
        if show_answers:
            results.append(str(eval(f"{num1} {operator} {num2}")).rjust(width))

    arranged = "    ".join(top) + "\n" + "    ".join(bottom) + "\n" + "    ".join(lines)
    if show_answers:
        arranged += "\n" + "    ".join(results)
    return arranged


# Test cases
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
