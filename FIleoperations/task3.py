file = open(r"C:\Users\Ethnotech\Downloads\pexels-cristian-rojas-6836442.jpg","wb");
file.write(bytes([1,2,3,4,5]));
file = open(r"C:\Users\Ethnotech\Downloads\pexels-cristian-rojas-6836442.jpg","rb");
print(file.read());