class B1:
    def __init__(self, s):
        self.__s = s
    @property
    def s(self):
        return self.__s

    @s.setter
    def s(self, value):
        self.__s = value
    def __str__(self):
        return "B1: "+self.__s
class B2:
    def __init__(self, s):
        self.__s = s

    @property
    def s(self):
        return self.__s

    @s.setter
    def s(self, value):
        self.__s = value

    def __str__(self):
        return "B2: " + self.__s
class D1(B1, B2):
    def __init__(self, s):
        super().__init__(s)
        self.b1 = B1(s)
        self._b2 = B2(s)

    def __str__(self):
        return "D1: " + self.s
class D2(D1):
    def __init__(self, s):
        super().__init__(s)
        self._d1 = D1(s)

    def __str__(self):
        return "D2: " + self.s
class D3(D2):
    def __init__(self, s):
        super().__init__(s)
        self.__d2 = D2(s)

    def __str__(self):
        return "D3: " + self.s
class D4(D2):
    def __init__(self, s):
        super().__init__(s)
        self.d2 = D2(s)

    def __str__(self):
        return "D4: " + self.s
class Node:
    def __init__(self, d):
        self.__data = d
        self.__next = None
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value
    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value
class List:
    def __init__(self):
        self.__head = None
    def insert(self, d):
        if not self.__head:
            self.__head = Node(d)
        else:
            cur = self.__head
            while cur.next:
                cur = cur.next
            cur.next = Node(d)
    def sort(self):
        l = []
        cur = self.__head
        while cur:
            i = 0
            for el in cur.data:
                if el.isdigit():
                    i+=1
            l.append((cur.data, i))
            cur = cur.next
        if l:
            for i, el1 in enumerate(l):
                for j, el2 in enumerate(l):
                    if el1[1] < el2[1]:
                        l[i], l[j] = l[j], l[i]
            self.__head = Node(l[0][0])
            if len(l) > 1:
                cur = self.__head
                for el in l[1:]:
                    cur.next = Node(el[0])
                    cur = cur.next
    def __str__(self):
        l = []
        cur = self.__head
        while cur:
            l.append(cur.data)
            cur = cur.next
        s = ', '.join(map(lambda s: str(s), l))
        s = '[' + s
        s = s + ']'
        return s

d3 = D3('a123')
d3.__dict__['_D3__d2'].s = 'rty89'
d3.__dict__['_D3__d2'].__dict__['_d1'].s = 'pdf234392'
d3.__dict__['_D3__d2'].__dict__['_d1'].b1.s = 'dfd12'
d3.__dict__['_D3__d2'].__dict__['_d1'].__dict__['_b2'].s = 'sdv5411'

d4 = D4('lm7665')
d4.d2.s = '01'
d4.d2.__dict__['_d1'].s = 'xxy233'
d4.d2.__dict__['_d1'].b1.s = '2'
d4.d2.__dict__['_d1'].__dict__['_b2'].s = 'opo66'

l = List()
l.insert(d3.s)
l.insert(d3.__dict__['_D3__d2'].s)
l.insert(d3.__dict__['_D3__d2'].__dict__['_d1'].s)
l.insert(d3.__dict__['_D3__d2'].__dict__['_d1'].b1.s)
l.insert(d3.__dict__['_D3__d2'].__dict__['_d1'].__dict__['_b2'].s)

l.insert(d4.s)
l.insert(d4.d2.s)
l.insert(d4.d2.__dict__['_d1'].s)
l.insert(d4.d2.__dict__['_d1'].b1.s)
l.insert(d4.d2.__dict__['_d1'].__dict__['_b2'].s)

l.sort()
print(l)