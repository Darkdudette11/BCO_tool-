f= open("BCO_File.txt","w+")
inside = input("Do you want to insert an input file Y or N \n")
if inside == 'Y': 
  y = range(50000)
  for i in  y:
    inside = input('Enter the name of the input file\n')
    f.write('Input file:  %s \n'%  inside +'\n')
    inside2 = input('Enter the uri of input file\n')
    f.write('Input file uri:  %s \n'%  inside2 +'\n')    
    more_explain =  input('Do you have more Input files to enter enter Y or N? \n')
    if more_explain == 'Y':
        i=i+1     
    else:
          break 
  x = range(50000)
  for j in  x:
    outside = input('Enter the name of the output file  \n')
    f.write('Output File:  %s \n'%  outside +'\n')
    outside2 = input('Enter the uri of output file\n')
    f.write('Output file uri:  %s \n'%  outside2 +'\n')      
    more_explain =  input('Do you have more Output files to enter enter Y or N? \n')
    if more_explain == 'Y':
        j=j+1
    else:
          break  
  
  
f.close()