from datastructure import UnionFind


def main():
    with open('social_network_input.log') as f:
        line = f.readline()
        uf = UnionFind(int(line))
        uf.print()

        lines = f.read().splitlines()

        for line in lines:
            line = line.split(' ', 2)
            uf.union(int(line[0]), int(line[1]))
            if uf.count_components() <= 1:
                print(line[2])
                return

        print(float('inf'))

        # while line:
        #     line = f.readline()
        #     print(line)
        #     print(line.split(' '))



if __name__ == '__main__':
    main()


