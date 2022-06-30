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
        return self.__class__.__name__ + ': ' + self.s


class D1(B):
    def __init__(self, s):
        super().__init__(s)
        self.b = B(s)


class D2(B):
    def __init__(self, s):
        super().__init__(s)
        self.__b = B(s)


class D3(B):
    def __init__(self, s):
        super().__init__(s)
        self.__b = B(s)


class D4(D1):
    def __init__(self, s):
        super().__init__(s)
        self.__d1 = D1(s)


class D5(D1, D2, D3):
    def __init__(self, s):
        super().__init__(s)
        self.d1 = D1(s)
        self.d2 = D2(s)
        self.__d3 = D3(s)


class List:
    def __init__(self, size):
        self.__size = size
        self.__array = [None] * size
        self.__index = 0

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    @property
    def array(self):
        return self.__array

    @array.setter
    def array(self, value):
        self.__array = value

    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, value):
        self.__index = value

    def insert(self, d):
        if self.index == self.size:
            raise Exception
        self.array[self.index] = d
        self.index += 1

    def sort(self):
        for i in range(self.index):
            for j in range(self.index):
                if len(self.array[i]) < len(self.array[j]):
                    self.array[i], self.array[j] = self.array[j], self.array[i]
    def __str__(self):
        return str(self.array[:self.index])

d4 = D4('djdf')
d4.__dict__['_D4__d1'].s = 'fdvbxx'
d4.__dict__['_D4__d1'].b.s = 'fcx'

d5 = D5('vcvz')
d5.d1.s = 'dcvm,xz'
d5.d2.s = 'a'
d5.__dict__['_D5__d3'].s = 'dl;xxx'
d5.d1.b.s = 'dvm./z'
d5.d2.__dict__['_D2__b'].s = 'cvbw222222'
d5.__dict__['_D5__d3'].__dict__['_D2__b'] = 'd2ro'

l = List(20)
l.insert(d4.s)
l.insert(d4.__dict__['_D4__d1'].s)
l.insert(d4.__dict__['_D4__d1'].b.s)
l.insert(d5.s)
l.insert(d5.d1.s)
l.insert(d5.d2.s)
l.insert(d5.__dict__['_D5__d3'].s)
l.insert(d5.d1.b.s)
l.insert(d5.d2.__dict__['_D2__b'].s)
l.insert(d5.__dict__['_D5__d3'].__dict__['_D2__b'])

l.sort()
print(l)
