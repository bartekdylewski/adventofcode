import functools


def part1(inp: str):
    patterns_part, designs_part = inp.split("\n\n")
    patterns = {pattern.strip() for pattern in patterns_part.split(",")}
    designs = designs_part.splitlines()

    @functools.cache
    def is_possble(design: str):
        if len(design) == 0:
            return True
        if design in patterns:
            return True
        for i in range(1, min(4, len(design))):
            if is_possble(design[:i]) and is_possble(design[i:]):
                return True
        return False

    possible = [design for design in designs if is_possble(design)]
    return len(possible)

def part2(inp: str):
    patterns_part, designs_part = inp.split("\n\n")
    patterns = {pattern.strip() for pattern in patterns_part.split(",")}
    max_pattern_len = max(map(len, patterns))
    designs = designs_part.splitlines()

    @functools.cache
    def arrangements(design: str) -> int:
        if len(design) == 0:
            return 1
        variants = int(design in patterns)
        for i in range(1, min(max_pattern_len + 1, len(design))):
            if design[:i] not in patterns:
                continue
            variants += arrangements(design[i:])
        return variants

    return sum(map(arrangements, designs))

input = open("input/input19.txt", "r").read()
print(part1(input))
print(part2(input))