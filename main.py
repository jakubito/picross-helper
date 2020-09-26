import sys


def filled(value):
    return f"\033[30;47m {value} \033[0m"


def dimmed(value):
    return f"\033[2m{value}\033[0m"


def blue(value):
    return f"\033[34m{value}\033[0m"


def red(value):
    return f"\033[91m{value}\033[0m"


print("Picross Helper")
print(blue("https://github.com/jakubito/picross-helper"))

while True:
    try:
        line_length = int(input("\nEnter line length: "))
    except ValueError:
        print(red("Invalid input"))
    else:
        break

while True:
    user_input = input("\n> ")

    if not user_input:
        continue

    if user_input in ("exit", "quit", "stop"):
        sys.exit(0)

    try:
        hints = list(map(int, user_input.split()))
    except ValueError:
        print(red("Invalid input"))
        continue

    hints_total = sum(hints) + len(hints) - 1
    delta = line_length - hints_total

    if delta < 0:
        print(red("Line length exceeded"))
        continue

    output = list()
    empty = 0

    for hint in hints:
        if hint > delta:
            if empty + delta > 0:
                output.append(empty + delta)
            output.append(filled(hint - delta))
            empty = 1
        else:
            empty += hint + 1

    if output:
        print(dimmed(" ⟶ ").join(map(str, output)))
    else:
        print(blue("No squares to fill"))
