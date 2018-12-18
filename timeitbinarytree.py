import binarytree
import random
from timeit import Timer

def Randomlist(lenght,Range):
    mylist = []
    for i in range(lenght):
        mylist.append(random.randint(0, Range))
    return mylist

Length=[10, 100, 1000, 10000]
Range=[10,100,200,1000]
binarytreetime = []
for i in Length:
    for j in Range:
        mylst=Randomlist(i,j)
        s = 'TreeNode(' + str(mylst)+',0,'+'('+str(len(mylst)-1)+')'+ ')'
        t1 = Timer(s, "from binarytree import TreeNode")
        time1 = t1.timeit(3)
        binarytreetime.append(time1)
print(binarytreetime)