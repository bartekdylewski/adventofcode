from pathlib import Path


class Wire:
    def value(self, state: dict[str, "Wire"]) -> int: ...
    def show(self, state: dict[str, "Wire"]) -> str: ...


class Input(Wire):
    def __init__(self, name: str, value: int) -> None:
        self.v = value
        self.name = name

    def value(self, state: dict[str, "Wire"]) -> int:
        return self.v

    def show(self, state: dict[str, "Wire"]) -> str:
        return self.name


class Gate(Wire):
    op = "?"

    def __init__(self, name: str, left: str, right: str) -> None:
        self.left = left
        self.right = right
        self.v = None
        self.name = name

    def __repr__(self) -> str:
        return f"{self.left}{self.op}{self.right}"

    def show(self, state: dict[str, "Wire"]) -> str:
        return (
            f"({state[self.left].show(state)}{self.op}{state[self.right].show(state)})"
        )


class And(Gate):
    op = "&"

    def value(self, state: dict[str, "Wire"]) -> int:
        if self.v is None:
            self.v = state[self.left].value(state) & state[self.right].value(state)

        return self.v


class Or(Gate):
    op = "|"

    def value(self, state: dict[str, "Wire"]) -> int:
        if self.v is None:
            self.v = state[self.left].value(state) | state[self.right].value(state)

        return self.v


class Xor(Gate):
    op = "^"

    def value(self, state: dict[str, "Wire"]) -> int:
        if self.v is None:
            self.v = state[self.left].value(state) ^ state[self.right].value(state)

        return self.v


GATES = {"AND": And, "OR": Or, "XOR": Xor}


def parse(input: str) -> dict[str, "Wire"]:
    wires: dict[str, Wire] = {}

    for line in input.splitlines():
        key, _, value = line.partition(": ")
        if value:
            wires[key] = Input(key, int(value))
        operation, _, out = line.partition(" -> ")
        if out:
            l, op, r = operation.split()
            wires[out] = GATES[op](out, l, r)

    return wires


def part1(data: dict[str, "Wire"]) -> int:
    z_keys = sorted([k for k in data if k.startswith("z")], reverse=True)
    # print(z_keys)
    values = [data[k].value(data) for k in z_keys]
    return int("".join(str(v) for v in values), 2)


INPUT = parse(Path("input/input24.txt").read_text())
part1_total = part1(INPUT)
print(f"{part1_total=:}")  # 64,755,511,006,320


from pathlib import Path


def parse(input: str) -> dict[frozenset[str], str]:
    wires: dict[str, frozenset[str]] = {}

    for line in input.splitlines():
        key, _, value = line.partition(": ")
        if value:
            continue
        operation, _, out = line.partition(" -> ")
        if out:
            left, op, right = operation.split()
            wires[frozenset([left, op, right])] = out

    return wires


INPUT: dict[frozenset[str], str] = parse(Path("input/input24.txt").read_text())
INVERT: dict[set, frozenset[str]] = {v: k for k, v in INPUT.items()}
SWITCH: list[str] = []


def show(name: str) -> str:
    if name in INVERT:
        ops = "?"
        vars = []
        for s in INVERT[name]:
            if s in ("AND", "OR", "XOR"):
                ops = s
            else:
                vars.append(s)
        vars.sort()

        return f"({name}: {show(vars[0])} {ops} {show(vars[1])})"
    return name


def carry_left(z: int) -> str:
    # Returns: carry(n-1) AND (xn XOR yn)
    assert z > 0

    right = INPUT[frozenset([f"x{z:02d}", "XOR", f"y{z:02d}"])]

    left = carry(z - 1)
    return INPUT[frozenset([left, "AND", right])]


def carry(z: int) -> str:
    # carry(1) -> x00 AND y00
    # carry(n) -> (carry(n-1) AND (xn XOR yn)) OR (xn AND yn)
    if z == 0:
        res = INPUT[frozenset(["x00", "AND", "y00"])]
        return res

    # (carry(z-1) AND (xz XOR yz)) OR (xz AND yz)
    right = INPUT[frozenset([f"x{z:02d}", "AND", f"y{z:02d}"])]
    left = carry_left(z)
    expr = frozenset([left, "OR", right])
    return INPUT[expr]


def generate(z: int) -> str:
    # print(f"Generate {z}")
    right = INPUT[frozenset([f"x{z:02d}", "XOR", f"y{z:02d}"])]
    if z == 0:
        return right

    left = carry(z - 1)
    expr_key = frozenset([left, "XOR", right])
    if expr_key not in INPUT:
        expect = set(INVERT[f"z{z:02d}"])
        unique = expr_key ^ expect
        if unique & set(SWITCH):
            # Avoid infinite recursion
            raise RuntimeError("Confused!")
        print("Try switching", unique)
        switch(*list(unique))
        return generate(z)

    expr = INPUT[expr_key]

    return expr


def clean(entry: frozenset[str]) -> tuple[str, set[str]]:
    for x in entry:
        if x in ("AND", "OR", "XOR"):
            return x, set(entry) - {x}
    assert False, f"Missing op {entry}"


def switch(actual: str, expect: str) -> None:
    SWITCH.extend([expect, actual])
    INPUT[INVERT[actual]], INPUT[INVERT[expect]] = (
        INPUT[INVERT[expect]],
        INPUT[INVERT[actual]],
    )
    INVERT[expect], INVERT[actual] = INVERT[actual], INVERT[expect]


def fixup(expect: str, actual: str) -> None:
    actual_op, args = clean(INVERT[actual])
    expect_op, exp_args = clean(INVERT[expect])
    if actual_op != expect_op:
        print("Operator change", expect, actual)
        switch(actual, expect)
        return True

    # Operators match, args must differ
    for a in args:
        if a in exp_args:
            # One argument in common, fix the other.
            return fixup(list[args - {a}][0], list[exp_args - {a}][0])

    print("Couldn't find fixup", expect, actual)
    return False


zkeys = sorted([k for k in INVERT if k.startswith("z")], reverse=False)[:-1]

for expect in zkeys:
    i = int(expect[1:], 10)
    res = generate(i)
    if res != expect:
        fixup(res, expect)
        assert generate(i) == expect

SWITCH.sort()
print("Part 2:", ",".join(SWITCH))
