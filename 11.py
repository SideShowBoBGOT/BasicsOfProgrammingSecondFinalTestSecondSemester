class B:
    def __init__(self, c):
        self.__c = c
    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        self.__c = value
    def __str__(self):
        return self.__class__.__name__+': '+self.c
class D1(B):
    def __init__(self, c):
        super().__init__(c)
        self.__b = B(c)
class D2(B):
    def __init__(self, c):
        super().__init__(c)
        self.b = B(c)
class D4(D1,D2):
    def __init__(self, c):
        super().__init__(c)
        self.d1 = D1(c)
        self._b = B(c)
        self._d2 = D2(c)
class D3(D1):
    def __init__(self, c):
        super().__init__(c)
        self._d1 = D1(c)
class Node:
    def __init__(self, d):
        self.__next = None
        self.__data = d
    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value
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
    def __str__(self):
        l = []
        cur = self.__head
        while cur:
            l.append(cur.data)
            cur = cur.next
        return str(l)
    def sort(self):
        l1 = []
        cur = self.__head
        while cur:
            l1.append(cur.data)
            cur = cur.next
        l = []
        for el1 in l1:
            count = 0
            for el2 in l1:
                if el1 == el2:
                    count+=1
            l.append((el1, count))

        for i, el1 in enumerate(l):
            for j, el2 in enumerate(l):
                if el1[0] < el2[0]:
                    l[i], l[j] = l[j], l[i]
        if l:
            self.__head = Node(l[0])
            cur = self.__head
            if len(l) > 1:
                for el in l[1:]:
                    cur.next = Node(el)
                    cur = cur.next
d3 = D3('x')
d3.__dict__['_d1'].c = 'k'
d3.__dict__['_d1'].__dict__['_D1__b'].c = 'u'

d4 = D4('a')
d4.d1.c = 'h'
d4.d1.__dict__['_D1__b'].c = 'e'
d4.__dict__['_b'].c = 'y'
d4.__dict__['_d2'].c = 'q'
d4.__dict__['_d2'].b.c = 'm'

c = List()
c.insert(d3.c)
c.insert(d3.__dict__['_d1'].c)
c.insert(d3.__dict__['_d1'].__dict__['_D1__b'].c)
c.insert(d4.c)
c.insert(d4.d1.c)
c.insert(d4.d1.__dict__['_D1__b'].c)
c.insert(d4.__dict__['_b'].c)
c.insert(d4.__dict__['_d2'].c)
c.insert(d4.__dict__['_d2'].b.c)

c.sort()
print(c)

