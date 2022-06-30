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
        self.__b2 = B2(n)
class D2(B2):
    def __init__(self, n):
        super().__init__(n)
        self._b2 = B2(n)
class D3(D1):
    def __init__(self, n):
        super().__init__(n)
        self._d1 = D1(n)

class D4(D2):
    def __init__(self, n):
        super().__init__(n)
        self.d2 = D2(n)
class Set_Int:
    def __init__(self, size):
        self.__index = 0
        self.__array = [None] * size
        self.__size = size
    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, value):
        self.__index = value
    @property
    def array(self):
        return self.__array

    @array.setter
    def array(self, value):
        self.__array = value
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
    def update(self, el):
        if self.__index==self.__size:
            raise Exception
        if el in self.__array:
            raise Exception
        self.__array[self.__index] = el
        self.__index+=1
    def __str__(self):
        if self.__index > 0:
            return '[' +\
                   ', '.join(map(
                       lambda s: str(s), self.__array[:self.__index])
                   )+']'
        return '[]'
    def __sub__(self, other):
        l = []
        for i in range(self.__index):
            notIn = True
            for j in range(other.__index):
                if self.__array[i] == other.__array[j]:
                    notIn = False
            if notIn:
                l.append(self.__array[i])
        index = len(l)
        diff = self.__size - index
        l += [None] * diff
        self.__index = index
        self.__array = l
        return self
    def getAverage(self):
        avg = 0
        if self.__index > 0:
            for i in range(self.__index):
                avg+=self.__array[i]
            avg/=self.__index
        return avg

d3 = D3(1)
d3.__dict__['_d1'].n = 2
d3.__dict__['_d1'].b1.n = 3
d3.__dict__['_d1'].__dict__['_D1__b2'].n = 4

d4 = D4(2)
d4.d2.n = 4
d4.d2.__dict__['_b2'].n = 8

m3 = Set_Int(10)
m3.update(d3.n)
m3.update(d3.__dict__['_d1'].n)
m3.update(d3.__dict__['_d1'].b1.n)
m3.update(d3.__dict__['_d1'].__dict__['_D1__b2'].n)

m4 = Set_Int(10)
m4.update(d4.n)
m4.update(d4.d2.n)
m4.update(d4.d2.__dict__['_b2'].n)

print('M3: ', m3)
print('M4: ', m4)
print('M3 - M4', m3 - m4)
print('AVG: ', (m3 - m4).getAverage())
