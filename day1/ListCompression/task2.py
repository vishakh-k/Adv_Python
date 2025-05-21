def outer_funtion(x):
    def inner_funtion(y):
        return x+y;
    return inner_funtion;
add_five=outer_funtion(5);
print(add_five(10));