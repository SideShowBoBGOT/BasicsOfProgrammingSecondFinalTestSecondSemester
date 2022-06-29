class B1:
    def __init__(self, n):
        self.__n = n
    @property
    def n(self):
        return self.__n

    @n.setter
    def n(self, value):
        self.__n = value
    def __str__(self):
        return self.__class__.__name__+': '+str(self.n)


class B2:
    def __init__(self, n):
        self.__n = n

    @property
    def n(self):
        return self.__n

    @n.setter
    def n(self, value):
        self.__n = value

    def __str__(self):
        return self.__class__.__name__ + ': ' + str(self.n)


class D1(B1, B2):
    def __init__(self, n):
        super().__init__(n)
        self.b1 = B1(n)
        self.b2 = B2(n)
class D2:
    def __init__(self, n):
        self.__n = n

    @property
    def n(self):
        return self.__n

    @n.setter
    def n(self, value):
        self.__n = value

    def __str__(self):
        return self.__class__.__name__ + ': ' + str(self.n)
class D3(D1, D2):
    def __init__(self, n):
        super().__init__(n)
        self.d1 = D1(n)
        self.d2 = D2(n)
class D4(D3):
    def __init__(self, n):
        super().__init__(n)
        self.d4 = D4(n)
class Node:
    def __init__(self, d):
        self.__left = None
        self.__right = None
        self.__data = d
    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, value):
        self.__left = value
    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, value):
        self.__right = value
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value
class Tree:
    def __init__(self):
        self.__root = None
    def insert(self, d):
        if not self.__root:
            self.__root = Node(d)
        else:
            stop = False
            cur = self.__root
            while not stop:
                if d > cur.data:
                    if not cur.right:
                        cur.right = Node(d)
                        stop = True
                    else:
                        cur = cur.right
                elif d <= cur.left:
                    if not cur.left:
                        cur.left = Node(d)
                        stop = True
                    else:
                        cur = cur.left
    def __crawlHeight(self, node: Node, depth: int, height: []):
        height[0] = max(height[0], depth)
        if node.right:
            self.__crawlHeight(node.right, depth+1, height)
        if node.left:
            self.__crawlHeight(node.left, depth + 1, height)
    def __crawlPrint(self, node: Node, pos: []):
        if node.left:
            pos.append([len(str(node.data)), '|'])
        if node.right:
            print(' -> ', end='')
            self.__crawlPrint(node.right, pos)
        if node.left:
            pos[-1][1] = ' '
            for k in range(2):
                for el in pos[:-1]:
                    for _ in range(el[0] - 1):
                        print(' ', end='')
                    print(el[1], end='')
                    print('    ', end='')
                for _ in range(pos[-1][0] - 1):
                    print(' ', end='')
                print('|', end='')
                if k==0:
                    print('')
            print(' -> ', end='')
            self.__crawlPrint(node.left, pos)
            pos.pop()
    def print(self):
        self.__crawlPrint(self.__root, [])
    def getHeight(self):
        height = [0]
        depth = 0
        if self.__root:
            depth = 1
            self.__crawlHeight(self.__root, depth, height)
        return depth
t = Tree()
d3 = D3(123)
d3.d2.n = 2623
d3.d1.n = 98
d3.d1.b2.n = 1782
d3.d1.b1.n = 362232
t.insert(d3.n)

t.insert(d3.d2.n)
t.insert(d3.d1.n)
t.insert(d3.d1.b2.n)
t.insert(d3.d1.b1.n)
t.print()


