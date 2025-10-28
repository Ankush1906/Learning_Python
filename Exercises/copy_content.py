def  copy_content():

    file1 = open('test.txt','r')
     
    lines = file1.readlines()


    for line in lines:
        if line[0] == '#':
         f2 = open('file2.txt','a')
         f2.write(line) 
          

        
    
copy_content()




