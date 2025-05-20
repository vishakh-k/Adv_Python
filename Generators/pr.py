def count_up(max):
    count = 1
    while (count < max): 
        yield count
        count += 1;
    print(count)
num=count_up(5);
print(next(num));
print(next(num));
print(next(num));
print(next(num));