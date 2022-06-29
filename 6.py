class B:
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
class D1(B):
    def __init__(self, n):
        super().__init__(n)
        self.b = B(n)
class D2(B):
    def __init__(self, n):
        super().__init__(n)
        self.__b = B(n)
class D3(D1, D2):
    def __init__(self, n):
        super().__init__(n)
        self.__d1 = D1(n)
        self.d2 = D2(n)
class D4(D1, D2):
    def __init__(self, n):
        super().__init__(n)
        self.__d1 = D1(n)
        self.d2 = D2(n)
class Set:
    def __init__(self):
        self.s = []
    def update(self, d):
        if d in self.s:
            raise Exception
        self.s.append(d)
        for i, el1 in enumerate(self.s):
            for j, el2 in enumerate(self.s):
                if el1 < el2:
                    self.s[i], self.s[j] = self.s[j], self.s[i]
    def __str__(self):
        s = ', '.join(map(lambda s: str(s), self.s))
        s = '[' + s + ']'
        return s
    def symmetric_diff(self, other):
        l = []
        for el in self.s:
            if not el in other.s:
                l.append(el)
        for el in other.s:
            if not el in self.s:
                l.append(el)
        self.s = l
    def max(self):
        return self.s[-1]
d3 = D3(1)
d3.__dict__['_D3__d1'].n = 2
d3.d2.n = 3
d3.__dict__['_D3__d1'].b.n = 4
d3.d2.__dict__['_D2__b'].n = 5

d4 = D4(3)
d4.__dict__['_D4__d1'].n = 5
d4.d2.n = 4
d4.__dict__['_D4__d1'].b.n = 9
d4.d2.__dict__['_D2__b'].n = 8

m3 = Set()
m3.update(d3.n)
m3.update(d3.__dict__['_D3__d1'].n)
m3.update(d3.d2.n)
m3.update(d3.__dict__['_D3__d1'].b.n)
m3.update(d3.d2.__dict__['_D2__b'].n)

m4 = Set()
m4.update(d4.n)
m4.update(d4.__dict__['_D4__d1'].n)
m4.update(d4.d2.n)
m4.update(d4.__dict__['_D4__d1'].b.n)
m4.update(d4.d2.__dict__['_D2__b'].n)

m3.symmetric_diff(m4)
print(m3)
print("Max: ", m3.max())








