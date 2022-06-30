class B1:
    def __init__(self, s):
        self.__s = s
    @property
    def s(self):
        return self.__s

    @s.setter
    def s(self, value):
        self.__s = value
    def __str__(self):
        return self.__class__.__name__+': '+self.s


class B2:
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


class B3:
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
class D1(B1, B2, B3):
    def __init__(self, s):
        super().__init__(s)
        self.b1 = B1(s)
        self.b2 = B2(s)
        self._b3 = B3(s)
class D3(B3):
    def __init__(self, s):
        super().__init__(s)
        self.b3 = B3(s)
class D2(D1, D3):
    def __init__(self, s):
        super().__init__(s)
        self.d1 = D1(s)
        self.__d3 = D3(s)
class D4(D2):
    def __init__(self, s):
        super().__init__(s)
        self._d2 = D2(s)
class Stack:
    def __init__(self, size):
        self.__size = size
        self.__array = [None]*size
        self.__index = 0
    def push(self, d):
        if self.__index==self.__size:
            raise Exception
        self.__array[self.__index] = d
        self.__index+=1
    def top(self):
        if self.__index == 0:
            raise Exception
        return self.__array[self.__index - 1]
    def pop(self):
        if self.__index == 0:
            raise Exception
        self.__array[self.__index - 1] = None
        self.__index-=1
    def isEmpty(self):
        if self.__index >0:
            return False
        return True
def shantingYard(exp: str):
    st = Stack(len(exp))
    s = ''
    for el in exp:
        if el.isdigit():
            s+=el
        else:
            s += ','
            if st.isEmpty():
                st.push(el)
            elif (st.top()=='*' or st.top()=='/') and (el=='+' or el=='-'):
                while (not st.isEmpty()) and st.top()!='(':
                    s += ','
                    s+=st.top()
                    st.pop()
                st.push(el)
            elif el==')':
                while (not st.isEmpty()) and st.top() != '(':
                    s += ','
                    s += st.top()
                    st.pop()
                st.pop()
            else:
                st.push(el)
    while not st.isEmpty():
        s += ','
        s += st.top()
        st.pop()
    s = s.replace(',,',',')
    return s
print(shantingYard('1+3+4-(8*9-12)*11'))
d4 = D4('1+3+4-(8*9-12)*11')
d4.__dict__['_d2'].s = '7+2+3/12'
d4.__dict__['_d2'].d1.s = '(15+2)*75-100'
d4.__dict__['_d2'].__dict__['_D2__d3'].s = '100+9'
d4.__dict__['_d2'].__dict__['_D2__d3'].b3.s = '11+9'
d4.__dict__['_d2'].d1.b1.s = '40*9-13'
d4.__dict__['_d2'].d1.b2.s = '177-13'
d4.__dict__['_d2'].d1.__dict__['_b3'].s = '1+1'

print(shantingYard(d4.s))
print(shantingYard(d4.__dict__['_d2'].s))
print(shantingYard(d4.__dict__['_d2'].d1.s))
print(shantingYard(d4.__dict__['_d2'].__dict__['_D2__d3'].s))
print(shantingYard(d4.__dict__['_d2'].__dict__['_D2__d3'].b3.s))
print(shantingYard(d4.__dict__['_d2'].d1.b1.s))
print(shantingYard(d4.__dict__['_d2'].d1.b2.s))
print(shantingYard(d4.__dict__['_d2'].d1.__dict__['_b3'].s))




