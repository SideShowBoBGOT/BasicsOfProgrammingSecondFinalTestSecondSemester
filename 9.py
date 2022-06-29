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


class B3:
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

class D1(B1, B2, B3):
    def __init__(self, n):
        super().__init__(n)
        self.b1 = B1(n)
        self.b2 = B2(n)
        self.__b3 = B3(n)
class D2(D1):
    def __init__(self, n):
        super().__init__(n)
        self.d1 = D1(n)
class Stack:
    def __init__(self):
        self.__s = []
    def push(self, n):
        self.__s.append(n)
    def pop(self):
        n = self.__s[-1]
        self.__s.pop()
        return n
    def isEmpty(self):
        if self.__s:
            return False
        return True

d2 = D2(4)
d2.d1.n = 5
d2.d1.b1.n = 6
d2.d1.b2.n = 7
d2.d1.__dict__['_D1__b3'].n = 8
st1 = Stack()
st2 = Stack()
st1.push(d2.n)
st1.push(d2.d1.n)
st1.push(d2.d1.b1.n)
st1.push(d2.d1.b2.n)
st1.push(d2.d1.__dict__['_D1__b3'].n)
st2.push(d2.d1.__dict__['_D1__b3'].n)
st2.push(d2.d1.b2.n)
st2.push(d2.d1.b1.n)
st2.push(d2.d1.n)
st2.push(d2.n)
sum = 0
while not st1.isEmpty():
    sum += st1.pop()*st2.pop()
print(sum)
