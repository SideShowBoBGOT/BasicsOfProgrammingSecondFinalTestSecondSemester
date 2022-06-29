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
class D1(B1):
    def __init__(self, n):
        super().__init__(n)
        self._b1 = B1(n)
class D2(B1):
    def __init__(self, n):
        super().__init__(n)
        self.b1 = B1(n)

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

class D3(D2, B2):
    def __init__(self, n):
        super().__init__(n)
        self._d2 = D2(n)
        self._b2 = B2(n)
class D4(D1, D3):
    def __init__(self, n):
        super().__init__(n)
        self.d1 = D1(n)
        self.d3 = D3(n)
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
class Stack:
    def __init__(self):
        self.__top = None
    def push(self, d):
        if not self.__top:
            self.__top = Node(d)
        else:
            node = Node(d)
            node.next = self.__top
            self.__top = node
    def pop(self):
        node = self.__top
        self.__top = self.__top.next
        return node.data
    def isEmpty(self):
        if self.__top:
            return False
        return True
def reverseInt(number):
    st = Stack()
    while number > 0:
        st.push(number%10)
        number//=10
    i = 1
    rev = 0
    while not st.isEmpty():
        n = st.pop()
        rev += n*i
        i*=10
    return rev

def reverseFloat(number):
    s = str(number)
    s1, s2 = s.split('.')
    n1 = int(s1)
    n2 = int(s2)
    n1 = reverseInt(n1)
    n2 = reverseInt(n2)
    s1 = str(n2)
    s2 = str(n1)
    s1+='.'+s2
    return float(s1)

d4 = D4(123.456)
d4.n = reverseFloat(d4.n)
d4.d1.n = reverseFloat(987.22221)
d4.d1.__dict__['_b1'].n = reverseFloat(256.112)
d4.d3.__dict__['_b2'].n = reverseFloat(890.1)
d4.d3.__dict__['_d2'].n = reverseFloat(3542.01)
d4.d3.__dict__['_d2'].b1 = reverseFloat(285.88732)
print(d4)
print(d4.d1)
print(d4.d1.__dict__['_b1'])
print(d4.d3.__dict__['_b2'])
print(d4.d3.__dict__['_d2'])
print(d4.d3.__dict__['_d2'].b1)



