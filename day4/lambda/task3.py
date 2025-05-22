"""from functools import reduce

list1 = [1, 2, 3, 4, 5]
num = reduce(lambda x,y : x + y, list1)
print(num)"""

"""from functools import reduce

list1=[1,2,3,4,5,6,7];
max1=reduce(lambda x,y:x if x>y else y,list1);
print(max1);"""

from functools import reduce

list1 = [1, 2, 3, 4, 5]
num1 = reduce(lambda x,y : x + y, list1)
num2 = reduce(lambda x,y : x * y, list1)
print(num1,num2);

