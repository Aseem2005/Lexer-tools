def read_grammar(filename):
    grammar = {}

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            left, right = line.split("->")
            left = left.strip()
            productions = [prod.strip() for prod in right.split("|")]

            grammar[left] = productions

    return grammar