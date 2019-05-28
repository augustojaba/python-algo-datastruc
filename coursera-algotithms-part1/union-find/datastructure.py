

class UnionFind:

    root = []
    size = []
    rank = []

    def __init__(self, n):
        for i in range(n):
            self.root.append(i)
            self.rank.append(i)
            self.size.append(1)

    def __root(self, p):
        i = p
        while i != self.root[i]:
            self.root[i] = self.root[self.root[i]]
            i = self.root[i]

        return i

    def find(self, p):
        return self.rank[self.__root(p)]

    def union(self, p, q):
        i = self.__root(p)
        j = self.__root(q)

        if i == j:
            return

        if self.size[i] > self.size[j]:
            self.root[j] = i
            self.size[i] += self.size[j]

            if self.rank[j] > self.rank[i]:
                self.rank[i] = j
        else:
            self.root[i] = j
            self.size[j] += self.size[i]

            if self.rank[i] > self.rank[j]:
                self.rank[j] = i

    def count_components(self):
        count = 0
        for i in range(len(self.root)):
            if self.root[i] == i:
                count += 1
        return count

    def print(self):
        print(list(range(10)))
        print(self.root)
        print(self.size)
        print(self.rank)
        print(str(self.count_components()) + '\n')

