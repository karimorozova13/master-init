from collections import UserDict, UserList, UserString


class SearchValueInDictionary(UserDict):
    def search_val(self, val):
        return val in self.data.values()
    
ex = SearchValueInDictionary()
ex['b'] = 13
print(ex.search_val(13))
print(ex.search_val(5))

class Countable(UserList):
    def sum(self):
        return sum(map(lambda x:int(x), self.data))
    
new_c = Countable([1,2,3,4,5])
new_c.append(13)
print(new_c.sum())

class TruncatedStr(UserString):
    def trunc_str(self,max):
        return self.data[:max]
    
ts = TruncatedStr('Kari play with cat')
print(ts.trunc_str(13))
    