def swapFileData():
    fileName1 = input("Enter File 1 Name Here")

    file1 = open(fileName1,'r')
    for line1 in file1:
        data_a = line1
        print(line1)
    
    fileName2 = input("Enter File 2 Name Here")
    file2 = open(fileName2,'r')
    for line2 in file2:
        data_a = line2
        print(line2)
  
    f = open(fileName1,'w')
    f.write("data_b")
    i = open(fileName2,'w')
    i.write("data_a")




swapFileData()