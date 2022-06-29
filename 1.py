class B:
    def __init__(self, s):
        self.__s = s
    @property
    def s(self):
        return self.__s

    @s.setter
    def s(self, value):
        self.__s = value
    def __str__(self):
        return self.__s
class D1(B):
    def __init__(self, s):
        super().__init__(s)
class D4:
    def __init__(self, s):
        self.__d1 = D1(s)
        self.__s = s
    @property
    def d1(self):
        return self.__d1
    
    @d1.setter
    def d1(self, value):
        self.__d1 = value
    @property
    def s(self):
        return self.__s

    @s.setter
    def s(self, value):
        self.__s = value

    def __str__(self):
        return self.__s
class D2:
    def __init__(self, s):
        self.__b = B(s)
        self.__s = s
    @property
    def b(self):
        return self.__b
    
    @b.setter
    def b(self, value):
        self.__b = value    
    @property
    def s(self):
        return self.__s

    @s.setter
    def s(self, value):
        self.__s = value

    def __str__(self):
        return self.__s
class D3:
    def __init__(self, s):
        self.__b = B(s)
        self.__s = s
    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        self.__b = value
    @property
    def s(self):
        return self.__s

    @s.setter
    def s(self, value):
        self.__s = value

    def __str__(self):
        return self.__s
class D5(D2):
    def __init__(self, s):
        super().__init__(s)
        self.__d3 = D3(s)
    @property
    def d3(self):
        return self.__d3
    
    @d3.setter
    def d3(self, value):
        self.__d3 = value
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
    def sort(self):
        l = []
        cur = self.__head
        while cur:
            l.append(cur.data)
            cur = cur.next
        if l:
            for i, el1 in enumerate(l):
                for j, el2 in enumerate(l):
                    if el1.s > el2.s:
                        l[i], l[j] = l[j], l[i]
            self.__head = Node(l[0])
            cur = self.__head
            if len(l) > 1:
                for el in l[1:]:
                    cur.next = Node(el)
                    cur = cur.next
    def __str__(self):
        l = []
        cur = self.__head
        s =''
        while cur:
            s+=str(cur.data) + ', '
            cur = cur.next
        return s

d41 = D4('x')
d42 = D4('i')
d43 = D4('a')
d51 = D5('j')
d52 = D5('f')
d53 = D5('b')
l = List()
l.insert(d41)
l.insert(d42)
l.insert(d43)
l.insert(d51)
l.insert(d52)
l.insert(d53)
l.sort()
print(l)
