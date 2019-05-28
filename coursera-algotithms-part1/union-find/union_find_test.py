from datastructure import UnionFind


def main():
    uf = UnionFind(10)
    uf.print()
    uf.union(9, 1)
    uf.print()
    uf.union(1, 2)
    uf.print()
    uf.union(3, 4)
    uf.print()
    uf.union(1, 3)
    uf.print()
    uf.union(5, 6)
    uf.union(5, 7)
    uf.print()
    uf.union(1, 5)
    uf.print()
    uf.union(4, 1)
    uf.print()

    # uf.print()
    # uf.union(4, 3)
    # uf.print()
    # uf.union(3, 8)
    # uf.print()
    # uf.union(3, 7)
    # uf.print()
    # uf.union(9, 3)
    # uf.print()


if __name__ == '__main__':
    main()
