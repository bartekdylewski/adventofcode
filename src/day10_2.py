import re
import numpy as np

type Point = tuple[int, int]

with open("input/input10.txt", "r") as f:
    input_rows: list[str] = [x.strip() for x in f.readlines()]
    assert re.fullmatch(r"[0-9]+", "".join(input_rows))
    input = np.array([list(map(int, x)) for x in input_rows], dtype=int)

HEAD: int = 0
END: int = 9

n_rows, n_cols = input.shape

heads: list[Point] = []
for i in range(n_rows):
    for j in range(n_cols):
        if input[i, j] == HEAD:
            heads.append((i, j))


def find(i: Point) -> tuple[set[Point], int]:
    if input[i] == END:
        return set([i]), 1
    else:
        ends: set[Point] = set()
        count: int = 0
        for x, y in [(i[0] + 1, i[1]), (i[0] - 1, i[1]), (i[0], i[1] + 1), (i[0], i[1] - 1)]:
            if 0 <= x and x < n_rows and 0 <= y and y < n_cols:
                if input[x, y] == input[i] + 1:
                    new_ends, new_count = find((x, y))
                    ends = ends.union(new_ends)
                    count += new_count

        return ends, count


results = [find(x) for x in heads]
print(sum(len(x[0]) for x in results))
print(sum(x[1] for x in results))