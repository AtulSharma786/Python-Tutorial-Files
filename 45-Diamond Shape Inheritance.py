class A:
    def met(self):
        print("this is a method fron class A")


class B(A):
    def met(self):
        print("this is a method fron class B")


class C(A):
    def met(self):
        print("this is a method fron class C")


class D(C, B):
    def met(self):
        print("this is a method fron class D")


a = A()
b = B()
c = C()
d = D()

d.met()
