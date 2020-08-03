name = input('What is your BCO ID \n')
f= open("BCO_File.txt","w+")
f.write("BCO_ID, %s \n" % name )
description = input("Do you want to insert information into the description Domain Y or N")
if description == 'Y':
  y = range(50000)
  for i in  y:
    Keyword = input('Enter Key Word:  \n')
    f.write('Keyword %s \n'%  (i+1) + ":" + Keyword + '\n')
    more_keywords =  input('Do you have more keywords to enter Y or N? \n')
    if more_keywords == 'Y':
        i=i+1
    else:
          break 
  f.write("Keywords:  %s \n" % Keyword)
  platform = input('What platform was this performed on \n')
  f.write("Platform: %s \n" % platform)
  pipeline_steps = input('Do you have a pipeline step to enter Y or N? \n')
  if pipeline_steps == 'Y':
    x = range(50000)
    for i in x:
        Step = input('Step number: \n')
        f.write("Step number: %s \n" % Step)
        Version = input('Version: \n')
        f.write("Version: %s \n" % Version)
        Description = input('Description: \n')
        f.write("Description: %s \n" % Description)
        input_list = input('Enter input file name with extension: \n')
        f.write("input file name:  %s \n" % input_list)
        output_list = input('Enter input file name with extension: \n')
        f.write("output file name:  %s \n" % output_list)
        more_steps =  input('Do you have more pipeline step to enter Y or N? \n')
        if more_steps == 'Y':
          i=i+1
        else:
          break         
        


      

else: 
  pass
  
f.close()