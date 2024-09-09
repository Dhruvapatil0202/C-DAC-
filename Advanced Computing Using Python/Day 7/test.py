class A:
    var1 = 10

    def increament(self):
        self.var1 += 1
        print(f"In class method: {self.var1}")

    @classmethod
    def increament2(cls):
        cls.var1 +=1
        print(f"In class method: {cls.var1}")

if __name__ == "__main__":
    a = A()
    b = A()

    b.increament2()
    a.increament()
