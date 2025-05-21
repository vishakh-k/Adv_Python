file = open(r"C:\Users\Ethnotech\Downloads\pexels-cristian-rojas-6836442.jpg","wb");
file.write(bytes([9]));
file.close();
file = open(r"C:\Users\Ethnotech\Downloads\pexels-cristian-rojas-6836442.jpg","rb");
print(file.read());