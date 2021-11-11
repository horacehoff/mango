import sys, getopt
declared_variables = []
declared_variables_values = []

def main(argv):
   inputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile="])
   except getopt.GetoptError:
      print('pygen.py -i <inputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('pygen.py -i <inputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
         
   return inputfile

def askfor(arg):
    return input(arg)

def error(error,count):
    print(" /!\ PyGen Error /!\ \rAt line "+str(count)+" ↓\r"+str(error))
    

def process(input,count):
    if "print" in input:
        try:
            input = input.replace("print","")
            input = input.replace("(","")
            input = input.replace(")","")
            input = input.replace("'","")
            input = input.replace('"','')
            if input in declared_variables:
                print(declared_variables_values[declared_variables.index(input)])
            else:
                try:
                    print(eval(input))
                except:
                    if "+" in input:
                        args = input.lstrip().replace(" ","")
                        args = args.split('+')
                        final_print = ""
                        for arg in args:
                            if arg in declared_variables:
                                final_print = final_print+declared_variables_values[declared_variables.index(arg)]
                            else:
                                try:
                                    final_print = final_print+eval(arg)
                                except: 
                                    final_print = final_print+arg
                        print(final_print)
                    else:
                        print(input.strip())
                
        except:
            error("Failed to print('<whatever you typed>')",count)
    elif "declare" in input:
        try:
            input = input.strip()
            input = input.split('=')
            var_name = input[0].replace("declare","").lstrip().replace(" ","")
            var_value = input[1].lstrip()
            if var_name in declared_variables:
                if 'ask(' in var_value:
                    declared_variables_values[declared_variables.index(var_name)] = askfor(var_value.replace("(","").replace(")","").replace("ask","").replace("'","").replace('"',''))
                else:
                    declared_variables_values[declared_variables.index(var_name)] = var_value
                    
            elif 'ask(' in var_value:
                print("Duh")
                declared_variables.append(var_name)
                declared_variables_values.append(askfor(var_value.replace("(","").replace(")","").replace("ask","").replace("'","").replace('"','')))
            
            else:
                declared_variables.append(var_name)
                declared_variables_values.append(var_value)
        except:
            error("Failed to declare variable "+(input.strip.split('=')[0].replace("declare","")),count)
    elif "ask" in input:
        try:
            input = input.replace("ask","")
            input = input.replace("(","")
            input = input.replace(")","")
            input = input.replace("'","")
            input = input.replace('"','')
            if input in declared_variables:
                askfor(declared_variables_values[declared_variables.index(input)])
            else:
                askfor(input.strip())
        except:
            error("Failed to print('<whatever you asked>')",count)
        
        
                
            

            
        
            
    
        
    
























file1 = open(main(sys.argv[1:]), 'r')
linecount = 0
lines = []
with open('mycooltext.txt') as file:
    for line in file:
        if not line == "":
            if not line == " ":
                line = line.replace('\n','')
                lines.append(line)
            
    print(lines)
    for line in lines:
        process(line,linecount)
        linecount = linecount + 1
        
