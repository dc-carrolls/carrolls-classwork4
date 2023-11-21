class NotPermittedShape(Exception):
    pass


class Pentamino:
    def __init__(self, *scheme):
        self.scheme = scheme

        self.squares = [
            (i, j)
            for i, row in enumerate(self.scheme)
            for j, col in enumerate(row)
            if col
        ]


def combine(p1, p1_squ, p2, p2_squ, dir_):
    field = [
        [0 for _ in range(SPACING)]
        for _ in range(SPACING)
    ]

    p1_x = p1_y = SPACING // 2

    p2_x = p1_x + p1_squ[0] - p2_squ[0] + dir_[0]
    p2_y = p1_y + p1_squ[1] - p2_squ[1] + dir_[1]

    fit(field, p1, (p1_x, p1_y))
    fit(field, p2, (p2_x, p2_y))

    return prettify(field)


def fit(field, pentamino, coords):
    for squ in pentamino.squares:
        x = coords[0] + squ[0]
        y = coords[1] + squ[1]

        if field[x][y]:
            raise NotPermittedShape

        field[x][y] = 1


def prettify(field):
    f = field.copy()

    cols = set(range(SPACING))
    ignored_cols = set()
    for col in cols:
        for row in f:
            if row[col]:
                break
        else:
            ignored_cols.add(col)
    preserved_cols = cols.difference(ignored_cols)
    
    res = []

    for row in f:
        if set(row) != {0}:
            res.append([row[c] for c in preserved_cols])
    
    return tuple(
        tuple(i) for i in res
    )


PENTAMINOES = {
    "F": Pentamino([0, 1, 1], [1, 1, 0], [0, 1, 0]),
    "G": Pentamino([1, 1, 0], [0, 1, 1], [0, 1, 0]),
    "I": Pentamino([1], [1], [1], [1], [1]),
    "L": Pentamino([1, 0], [1, 0], [1, 0], [1, 1]),
    "J": Pentamino([0, 1], [0, 1], [0, 1], [1, 1]),
    "N": Pentamino([0, 1], [1, 1], [1, 0], [1, 0]),
    "M": Pentamino([1, 0], [1, 1], [0, 1], [0, 1]),
    "P": Pentamino([1, 1], [1, 1], [1, 0]),
    "Q": Pentamino([1, 1], [1, 1], [0, 1]),
    "T": Pentamino([1, 1, 1], [0, 1, 0], [0, 1, 0]),
    "U": Pentamino([1, 0, 1], [1, 1, 1]),
    "V": Pentamino([1, 0, 0], [1, 0, 0], [1, 1, 1]),
    "W": Pentamino([1, 0, 0], [1, 1, 0], [0, 1, 1]),
    "X": Pentamino([0, 1, 0], [1, 1, 1], [0, 1, 0]),
    "Z": Pentamino([1, 1, 0], [0, 1, 0], [0, 1, 1]),
    "S": Pentamino([0, 1, 1], [0, 1, 0], [1, 1, 0]),
    "Y": Pentamino([0, 1], [1, 1], [0, 1], [0, 1]),
    "A": Pentamino([1, 0], [1, 1], [1, 0], [1, 0]),
}

SPACING = 20

L = (-1, 0)
R = (1, 0)
U = (0, 1)
D = (0, -1)


def main():
    print("Demian Volkov")
    print("Year 12 (17 years old)")
    print("Dulwich College")
    print()

    p1, p2 = (PENTAMINOES[i] for i in input())

    shapes = set()

    for p1_squ in p1.squares:
        for p2_squ in p2.squares:
            for dir_ in (L, R, U, D):
                try:
                    shape = combine(
                        p1, p1_squ,
                        p2, p2_squ,
                        dir_,
                    )
                except NotPermittedShape:
                    pass
                else:
                    shapes.add(shape)        
    
    print(len(shapes))


if __name__ == "__main__":
    main()
