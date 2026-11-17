class DynamicArray:
    
    def __init__(self, capacity: int):
        self.cap = capacity
        self.arr = []
        self.length = 0

    def get(self, i: int) -> int:
        if i < self.cap:
            return self.arr[i]

    def set(self, i: int, n: int) -> None:
        if i < self.cap:
            self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.cap: # occupied
            self.resize()
        self.arr.append(n)
        self.length +=1
        

    def popback(self) -> int:
        self.length-=1
        return self.arr.pop(-1)

    def resize(self) -> None:
        self.cap = 2 * self.cap

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.cap