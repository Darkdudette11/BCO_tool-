f= open("BCO_File.txt","w+")
usability = input("Do you want to insert information into the Usability Domain Y or N \n")
if usability == 'Y':
  y = range(50000)
  for i in  y:
    usability = input('Enter any phrases that would help understand the purpose and use of the   \n')
    f.write('Usability Domain:  %s \n'%  usability +'\n')
    more_explain =  input('Do you have more to add to the usability domain enter Y or N? \n')
    if more_explain == 'Y':
        i=i+1
    else:
          break 
  
  
f.close()