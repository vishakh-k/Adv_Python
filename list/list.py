'''list with numbers'''
list_one=[1,2,3,4,5,6,7,8,9,10];
#print(list_one); 

'''list with numbers and strings'''
list_two=[2,4,6,"eight",10,12,"fourteen",16,18,20];
#print(list_two); 

'''nested list'''
list_three=[[1,2,3,4],[5,6,7,8]];
#print(list_three);

'''accessing list values'''
#print(list_one[-1]);
#print(list_three[1]);

'''adding'''
list_one.append(11);
#print(list_one);

'''insert'''
list_one.insert(2,2.5);
#print(list_one);

'''extend'''
list_one.extend([12,13,14]);
#print(list_one);

'''delete'''
list_one.remove(2.5);
#print(list_one);

'''pop'''
list_one.pop();
#print(list_one);

'''clear'''
#list_one.clear();
#print(list_one);

'''slice'''
#print(list_one[:9]);

'''updating'''
list_one[4]=100;
#print(list_one);

'''concatination'''
#print(list_one+list_two); 

'''printing the elements'''
print(list_one*3); 

'''checking the elements'''
print(4 in list_one);

'''sorting'''
list_one.sort();
print(list_one);
print(sorted(list_one));

'''reverse'''
list_one.reverse()
print(list_one);

'''sum'''
print(sum(list_one));

'''using for loop'''
for i in list_one:
    print(i);