class A:
    def __init__(self):
        print("Class A")

    def present(self):
        print("Class A is there.")


class B(A):
    def __init__(self):
        super().__init__()
        print("Class B")

    def present(self):
        print("Class B is there.")


class C(A):
    def __init__(self):
        super().__init__()
        print("Class C")

    def present(self):
        print("Class C is there.")


class D(B, C):
    def __init__(self):
        super().__init__()
        print("Class D")
        super().present()  # will call "present()" def in class B

    def present(self):
        print("Class D is there.")


print(D.__mro__)
obj_d = D()
obj_d.present()
