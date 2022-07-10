import os 
g = open('In.txt','w')
f = open('IP.txt','r')
f = f.readlines()
print (f)
for x in f:
    response = os.system("ping -n 2 " + x)
    #and then check the response...
    if response == 0:
        str1 = 'is up! \n'
        g.writelines(str1)
        print (x, 'is up!', end='\n')
        
    else:
        str2 = 'is down! \n'
        g.writelines(str2)
        print (x, 'is down!')
        
        
   
