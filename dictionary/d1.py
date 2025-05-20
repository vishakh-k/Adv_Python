dict={'name':"shravan",
      'rollno':32,
      'marks':44 };
print(dict);
print(dict['name']);
print(dict['rollno']);
print(dict['marks']);
#adding
print(dict.get('name'));
dict['grade']='A';
print(dict);
dict['name']='Vishakh';
print(dict);

#deleting
#del dict['name']
print(dict);

#dict.pop('grade');
print(dict);

#dict.clear();
print(dict);

print(dict.keys());
print(dict.values());
