import math
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
        return self.__class__.__name__ + ': ' + str(self.i)


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
        return self.__class__.__name__ + ': ' + str(self.i)


class D1(B1):
    def __init__(self, i):
        super().__init__(i)
        self.b1 = B1(i)


class D2(B1, B2):
    def __init__(self, i):
        super().__init__(i)
        self._b1 = B1(i)
        self.b2 = B2(i)


class D3(D1, D2):
    def __init__(self, i):
        super().__init__(i)
        self.d1 = D1(i)
        self._d2 = D2(i)


class Stack:
    def __init__(self):
        self.__l = []

    def push(self, i):
        self.__l.append(i)

    def pop(self):
        self.__l.pop()

    def revert_number(self, n):
        while n > 0:
            self.push(n % 10)
            n //= 10
        rev = 0
        i = 1
        while self.__l:
            topp = self.__l[-1]
            self.pop()
            temp = topp * i
            rev += temp
            i *= 10
        return rev


st = Stack()
d3 = D3(356782)
d3.i = st.revert_number(d3.i)
d3.d1.i = st.revert_number(19902)
d3.__dict__['_d2'].i = st.revert_number(1982)
d3.d1.b1.i = st.revert_number(152423)
d3.__dict__['_d2'].__dict__['_b1'].i = st.revert_number(244221)
d3.__dict__['_d2'].b2.i = st.revert_number(1010333)
print(d3)
print(d3.d1)
print(d3.__dict__['_d2'])
print(d3.d1.b1)
print(d3.__dict__['_d2'].__dict__['_b1'])
print(d3.__dict__['_d2'].b2)
