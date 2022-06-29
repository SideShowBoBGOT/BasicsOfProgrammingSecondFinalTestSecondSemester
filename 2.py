class B1:
    def __init__(self, i):
        self.__i = abs(i)

    @property
    def i(self):
        return self.__i

    @i.setter
    def i(self, value):
        self.__i = abs(value)

    def __str__(self):
        return 'B1 ' + str(self.__i)


class B2:
    def __init__(self, i):
        self.__i = abs(i)

    @property
    def i(self):
        return self.__i

    @i.setter
    def i(self, value):
        self.__i = abs(value)

    def __str__(self):
        return 'B2 ' + str(self.__i)


class D1(B2):
    def __init__(self, i):
        super().__init__(i)
        self.b2 = B2(i)
        self.__b1 = B1(i)

    def __str__(self):
        return 'D1 ' + str(self.i)


class D2(D1):
    def __init__(self, i):
        super().__init__(i)
        self.d1 = D1(i)

    def __str__(self):
        return 'D2 ' + str(self.i)


class D3(D1):
    def __init__(self, i):
        super().__init__(i)
        self.__d1 = D1(i)

    def __str__(self):
        return 'D3 ' + str(self.i)


class Set:
    def __init__(self):
        self.__s = []

    def update(self, el):
        if el in self.__s:
            raise Exception
        self.__s.append(el)
        for i, el1 in enumerate(self.__s):
            for j, el2 in enumerate(self.__s):
                if el1 > el2:
                    self.__s[i], self.__s[j] = self.__s[j], self.__s[i]

    def diff(self, other):
        s = []
        for el in self.__s:
            if not el in other.__s:
                s.append(el)
        self.__s = s

    def sum(self):
        sum = 0
        for el in self.__s:
            sum += el
        return sum

d2 = D2(5)
d2.d1.i = 4
d2.d1.b2.i = 6
d2.d1.__dict__['_D1__b1'].i = 7

s2 = Set()
s2.update(d2.i)
s2.update(d2.d1.i)
s2.update(d2.d1.b2.i)
s2.update(d2.d1.__dict__['_D1__b1'].i)

d3 = D3(1)
d3.__dict__['_D3__d1'].i = 2
d3.b2.i = 3
d3.__dict__['_D3__d1'].__dict__['_D1__b1'].i = 4

s3 = Set()

s3.update(d3.i)
s3.update(d3.__dict__['_D3__d1'].i)
s3.update(d3.b2.i)
s3.update(d3.__dict__['_D3__d1'].__dict__['_D1__b1'].i)

s3.diff(s2)
print(s3.sum())


