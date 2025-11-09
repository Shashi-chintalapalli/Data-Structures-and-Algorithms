class BubbleSort:
    def __init__(self,number):
        self.number=number
    def bubble_sort(self):
        n=len(self.number)
        for i in range(n):
            for j in range(n-1-i):
                if self.number[j]>self.number[j+1]:
                    self.number[j],self.number[j+1]=self.number[j+1],self.number[j]
        return self.number
search=BubbleSort([5, 1, 4, 2, 8])
print(search.bubble_sort())
                    
                
        