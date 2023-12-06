import pickle

# serialize not-serialized attributes (file descriptors)
class Reader:
    def __init__(self,file) -> None:
        self.file = file
        self.fh = open(self.file)
        self.position= 0
    def close(self):
        self.fh.close()
    def read(self, size=1):
        data = self.fh.read(size)
        self.position = self.fh.tell()
        return data
    def __getstate__(self) -> object:
        # attributes = self.__dict__.copy()
        
        attributes = {**self.__dict__}
        attributes['fh'] = None
        return attributes
    def __setstate__(self, value):
        self.__dict__ = value
        self.fh = open(value['file'])
        self.fh.seek(value['position'])