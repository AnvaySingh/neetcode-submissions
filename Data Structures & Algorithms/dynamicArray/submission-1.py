class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.size=0
        self.dynamicArray=[0]*self.capacity


    def get(self, i: int) -> int:
        return self.dynamicArray[i]


    def set(self, i: int, n: int) -> None:
        self.dynamicArray[i]=n


    def pushback(self, n: int) -> None:
        if self.size==self.capacity:
            self.resize()
        
        self.dynamicArray[self.size]=n
        self.size+=1 


    def popback(self) -> int:
        self.size-=1
        return self.dynamicArray[self.size]
        
 

    def resize(self) -> None:
        self.capacity=self.capacity*2
        newdynamicArray=[0]*self.capacity
        for j in range(self.size):
            newdynamicArray[j] = self.dynamicArray[j]

        self.dynamicArray=newdynamicArray


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
