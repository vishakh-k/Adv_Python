def squres(max):
    num=1;
    while(num<max):
        yield num**2;
        num+=1;
    print(num);
rst=squres(11);
print(next(rst));
print(next(rst));
print(next(rst));
print(next(rst));
print(next(rst));
print(next(rst));
print(next(rst));
print(next(rst));
print(next(rst));
print(next(rst));
