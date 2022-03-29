class Kasr:

    def __init__(self, s, n):
        self.soorat = s
        self.makhraj = n 

    def sum(self, mehman):
        result = Kasr(None, None) 
        result.soorat = (self.soorat * mehman.makhraj) + (self.makhraj * mehman.soorat)
        result.makhraj = self.makhraj * mehman.makhraj
        return result 

    def mul(self, mehman):
        result = Kasr(None, None) 
        result.soorat = self.soorat * mehman.soorat
        result.makhraj = self.makhraj * mehman.makhraj
        return result 

    def sub(self, mehman):
        result = Kasr(None, None)
        result.soorat = (self.soorat * mehman.makhraj) - (self.makhraj * mehman.soorat)
        result.makhraj = self.makhraj * mehman.makhraj
        return result

    def div(self, mehman):
        result = Kasr(None, None)
        result.soorat = self.soorat * mehman.makhraj
        result.makhraj = self.makhraj * mehman.soorat
        return result

    def show(self):
        print(self.soorat, '/', self.makhraj)  

a = Kasr(3, 5)
b= Kasr(4, 3)

c = a.sum(b)
c.show()

d = a.mul(b)
d.show()


e = a.sub(b) 
e.show()


f = a.div(b)
f.show()  