import sys, getopt, pathlib
declared_variables = []
declared_variables_values = []
pygen_version = 'AlphaDev'

def askfor(arg):
    return input(arg)

def error(error,count):
    print(" /!\ PyGen Error /!\ ")
    print("At line "+str(count)+" ↓")
    print(str(error))
    exit()
    
def process(input,count):
    if "print" in input:
        try:
            #Remove print("") to only get what the user typed as the input
            input = input.replace("print","")
            input = input.replace("(","")
            input = input.replace(")","")
            input = input.replace("'","")
            input = input.replace('"','')
            #If what the user typed is a variable name, search it, get its value, and then print it
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
                    elif ',' in input:
                        args = input.lstrip()
                        args = args.split(',')
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
        
        
                
            

            
        
            
    

def dataread(file):
    try:
        assert file.split('.')[1] == 'pygen'
    except:
        error(file+' is not a .pygen file',0)
    file1 = open(str(file), 'r')
    linecount = 0
    lines = []
    with open(str(file1).replace("<_io.TextIOWrapper name='","").replace("' mode='r' encoding='cp1252'>","")) as file:
        for line in file:
            if not line == "":
                if not line == " ":
                    line = line.replace('\n','')
                    lines.append(line)

        for line in lines:
            process(line,linecount)
            linecount = linecount + 1
        
    














 
 

 

argumentList = sys.argv[1:]
 
options = "i:c"
 
long_options = ["CheckInstall", "InputFile ="]
 
try:

    arguments, values = getopt.getopt(argumentList, options, long_options)
     
    for currentArgument, currentValue in arguments:
        
        if currentArgument in ("-i", "--InputFile"):
            dataread(str(currentValue))
 
        if currentArgument in ("-c", "--CheckInstall"):
            print("PyGen - "+pygen_version)
            print(currentValue)
             
except getopt.error as err:
    print (str(err))
    
    




