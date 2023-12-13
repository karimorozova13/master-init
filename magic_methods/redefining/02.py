from collections import UserList

class MultList(UserList):
    def __mul__(self, other) :
        res=0
        l = min(len(self.data), len(other.data))
        
        for i in range(l):
            res += self.data[i] * other.data[i]
        return res
    
m = MultList([1,2,3])
s = MultList([4,5,6,7,8,9])
print(m * s)