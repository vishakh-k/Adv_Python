try:
    d={
        'name':"abc"
    }
    print(d['name']);
except KeyError:
    print("Key error");
else:
    print("No error");
finally:
    print("Program executed")