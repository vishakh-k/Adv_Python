def evenOdd():
    list=[1,2,3,4,5,6,7,8,9,10];
    even_numbers=[];
    odd_numbers=[];
    for i in list:
        if i%2==0:
            even_numbers.append(i);
        else:
            odd_numbers.append(i);
    print("Even numbers",even_numbers);
    print("Odd numbers",odd_numbers);
    print(len(list));
    print(sum(list));
evenOdd();