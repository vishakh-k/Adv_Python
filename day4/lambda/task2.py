#filter method
even_numbers = list(filter(lambda x: x % 2 == 0, range(1, 11)))
print(even_numbers)

#map method
nums = [1,2,3,4,5,6,7,8,9,10]
squares = list(map(lambda x: x**2, nums))
print(squares)

#
list1=['c',"java","c#","c++","js"];
uppercase=list(map(lambda str:str.upper(),list1));
print(uppercase);