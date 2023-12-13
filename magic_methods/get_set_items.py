class PositiveNumbers:
    def __init__(self, data=[]) -> None:
        super().__init__()
        self.data = [el for el in list(filter(lambda x: x > 0, data))]
        
    def __getitem__(self, idx):
        if idx is None:
            return self.data
        return self.data[idx]
    def __setitem__(self, idx,val):
        if idx >=0 and idx < len(self.data) and val >=0:
            self.data[idx] = val
        return self.data[idx]
    def append(self,item)-> None:
        if item >=0:
            self.data.append(item)
    
list = PositiveNumbers([3,-5,-8,9,2])
list[0] = 13
print(list.data)
list.append(99)
print(list.data)

