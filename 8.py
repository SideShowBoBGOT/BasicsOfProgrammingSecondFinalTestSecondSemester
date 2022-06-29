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
        self.b = B(c)
class D2(B):
    def __init__(self, c):
        super().__init__(c)
        self.__b = B(c)
class D3(D1):
    def __init__(self, c):
        super().__init__(c)
        self.__d1 = D1(c)
class D4(D2):
    def __init__(self, c):
        super().__init__(c)
        self.d2 = D2(c)
class Set:
    def __init__(self):
        self.__s = []
    def update(self, d):
        if d in self.__s:
            raise Exception
        self.__s.append(d)
    def __sub__(self, other):
        l = []
        for el in self.__s:
            if not el in other.__s:
                l.append(el)
        self.__s = l
        return self
    def max(self):
        for i, el1 in enumerate(self.__s):
            for j, el2 in enumerate(self.__s):
                if el1 < el2:
                    self.__s[i], self.__s[j] = self.__s[j], self.__s[i]

        return self.__s[-1]
    def __str__(self):
        return '[' + ', '.join(self.__s) + ']'
c3 = Set()
c4 = Set()

d3 = D3('f')
d3.__dict__['_D3__d1'].c = 'l'
d3.__dict__['_D3__d1'].b.c = 'x'

c3.update(d3.c)
c3.update(d3.__dict__['_D3__d1'].c)
c3.update(d3.__dict__['_D3__d1'].b.c )

d4 = D4('n')
d4.d2.c = 'x'
d4.d2.__dict__['_D2__b'].c = 'u'

c4.update(d4.c)
c4.update(d4.d2.c)
c4.update(d4.d2.__dict__['_D2__b'].c)

print('C3: ', c3)
print('C4: ', c4)
print('C3 - C4: ', c3 - c4)
print('max: ', (c3 - c4).max())




