from pampy import _,match

class Test():
    def __init__(self, arr, patt):
        self.arr = arr
        self.patt = patt
        
    def run(self):
        return match(self.arr, self.patt, lambda x: f'b is: {x}')
    
arr = ['a', 1, 'b', 2, 'c', 3, 'd', 4, 'e', 5]

patt = ['a', 1, 'b', 2, 'c',_, 'd', 4, 'e', 5]

the_test = Test(arr, patt)

print(the_test.run())