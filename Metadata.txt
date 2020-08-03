f= open("BCO_File.txt","w+")
import random
list=[]
for i in range(2):
          r=random.randint(1,100)
          if r not in list: 
            list.append(r)
            object_id ='https://portal.aws.biochemistry.gwu.edu/bco/BCO_' + str(r) 
            f.write('Object ID:  %s \n'%  object_id +'\n')
f.write('spec version: https://w3id.org/ieee/ieee-2791-schema/ \n')
for j in range(1):
          r=random.randint(1,100)
          if r not in list: 
            list.append(r)
            f.write('etag: '+ str(r)+str(r+23994) + str(r+388920))
f.close()