f= open("BCO_File.txt","w+")
usability = input("Do you want to insert information into the Extension Domain Y or N \n")
if usability == 'Y':
  y = range(50000)
  for i in  y:
    usability = input('Enter the uri for the extinsion domain   \n')
    f.write('Extension Domain:  %s \n'%  usability +'\n')
    more_explain =  input('Do you have more to add to the Extension domain enter Y or N? \n')
    if more_explain == 'Y':
        i=i+1
    else:
          break 
  
  
f.close()