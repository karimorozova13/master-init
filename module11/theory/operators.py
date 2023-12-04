from collections import UserDict

class Dict(UserDict):
    def __add__(self,other):
        self.data.update(other)
        return self
    def __sub__(self, other):
        for key in self.data:
            if key in other:
                self.data.pop(key)
        return self
    
d1 = Dict({1:0,2:8})
d2 = Dict({3:'here', 4:'there'})
d3 = d1 + d2

print(d3)

d4 = d3 - d1
print(d4)
