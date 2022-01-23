import os
file = open(os.getcwd()+'/guides/rep.txt','r')
print(len(''.join(file.read().splitlines()[3:])))