"""
                        |-----------------------------------|
                        |              F O X                |        by Just_a_Mango
                        |-----------------------------------|        @Just-A-Mango on GitHub
"""


#Import the necessary modules
import sys, getopt, os


#Decalare the lists where the variables and their values are stored
declared_variables = []
declared_variables_values = []


#Declare the lists where the lists (inception!) and their values are stored
declared_lists = []
declared_lists_values = []


#Declare this language's current version
fox_version = 'InDev'


#Check if the modules' folder exists, and create it if it doesn't
def check_modules_folder():
    from pathlib import Path
    Path(os.getcwd() + "\\Modules\\").mkdir(parents=True, exist_ok=True)


#Print the language's version and name
def print_version(version):
    print("|-----------------------------------|\r\n|          F O X  -  "+version+"          |        by Just_a_Mango\r\n|-----------------------------------|        @Just-A-Mango on GitHub\r\n")


#Installs any given module at runtime in the background
def install_module(module):
    try:
        import subprocess
        subprocess.call(["pip", "install", module], stdout = open(os.devnull, "w"), stderr = subprocess.STDOUT)
    except:
        pass


#Prints the current Fox installation directory
def get_dir():
    print("Fox installation directory: "+os.getcwd())


#Function used to ask, if the user asks!
def askfor(arg):
    return input(arg)


#Function used to print a nice and clean error
def error(error,count):
    print("       /!\ Fox Error /!\ ")
    print("At line "+str(count)+" ↓")
    print(str(error))
    exit()
    

#Detect the installed modules/functions
def detect_modules():
    modules = []
    from fnmatch import fnmatch
    root = os.getcwd() + '\\Modules\\'
    pattern = "*.py"
    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern):
                modules.append(name.replace(".py",""))
    try:
        os.remove(os.getcwd()+'\\Modules\\input.txt')
    except:
        pass
    return modules
        


#Basically the function that IS the language
def process(input,count):
    # PRINT
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
            elif input in declared_lists:
                list_toprint = declared_lists_values[declared_lists.index(input)]
                list_toprint = list_toprint.replace("+",",")
                list_toprint = "["+list_toprint+"]"
                print(list_toprint)
            #Else, if it's an equation(or simple math), just calculate and print it
            else:
                try:
                    print(eval(input))
                except:
                    #If The user tries to calculate/join strings/numbers
                    if "+" in input:
                        args = input.lstrip().replace(" ","")
                        args = args.split('+')
                        final_print = ""
                        for arg in args:
                            #If detected arguments are known variables, join and print them
                            if arg in declared_variables:
                                final_print = final_print+declared_variables_values[declared_variables.index(arg)]
                            else:
                                #If it can calculate, then do so, else, join
                                try:
                                    final_print = final_print+eval(arg)
                                except: 
                                    final_print = final_print+arg
                        print(final_print)
                    #The user tries to join strings/numbers
                    elif ',' in input:
                        args = input.lstrip()
                        args = args.split(',')
                        final_print = ""
                        for arg in args:
                            if arg in declared_variables:
                                final_print = final_print+declared_variables_values[declared_variables.index(arg)]
                            else:
                                #If it can't calculate, then join (joins 99.9% of the time (not a bug!))
                                try:
                                    final_print = final_print+eval(arg)
                                except: 
                                    final_print = final_print+arg
                        print(final_print)
                    #If all else fails, just print what's in-between the brackets
                    else:
                        print(input.strip())
                
        except:
            error("Failed to print('<whatever you typed>')",count)
    # DECLARE
    elif "declare" in input:
        if not 'list' in input:
            #Try to add declared variable and its value to declared_variables and declared_variables_values
            try:
                #Get the "raw" variable name
                input = input.strip()
                input = input.split('=')
                var_name = input[0].replace("declare","").lstrip().replace(" ","")
                var_value = input[1].lstrip()
                #If the declared variable already exists, then overwrite its value
                if var_name in declared_variables:
                    if 'ask(' in var_value:
                        declared_variables_values[declared_variables.index(var_name)] = askfor(var_value.replace("(","").replace(")","").replace("ask","").replace("'","").replace('"',''))
                    else:
                        try:
                            eval_ed = eval(var_value)
                            declared_variables_values[declared_variables.index(var_name)] = eval_ed
                        except:
                            declared_variables_values[declared_variables.index(var_name)] = var_value
                #If the value is 'ask'(at least contains it), then ask!
                elif 'ask(' in var_value:
                    declared_variables.append(var_name)
                    declared_variables_values.append(askfor(var_value.replace("(","").replace(")","").replace("ask","").replace("'","").replace('"','')))
                #Else, just declare and add it
                else:
                    try:
                        to_add = eval(var_value)
                        declared_variables.append(var_name)
                        declared_variables_values.append(to_add)
                    except:
                        declared_variables.append(var_name)
                        declared_variables_values.append(var_value)
            #If it fails, notify the user
            except:
                error("Failed to declare variable "+(input.strip.split('=')[0].replace("declare","")),count)
        else:
            try:
                #Split the given line into two distinct strings : the first one is the list's name, and the second one is the list's value
                input = input.split('=')
                list_name = input[0]
                list_name = list_name.replace("declare","")
                list_name = list_name.replace("list","")
                list_name = list_name.replace(" ","")
                input = input[1]
                input = input.replace(" ","")
                input = input.split(',')
                list_toadd = ""
                #Store the content of the list into a single string and separate them using +
                for word in input:
                    word = word.replace("[","")
                    word = word.replace("]","")
                    list_toadd = list_toadd+word+"+"
                if list_toadd[-1] == "+":
                    list_toadd = list_toadd.removesuffix("+")
                #If the list's name already exists, overwrite its value, otherwise simply add it to the declared lists and declared lists' values
                if not list_name in declared_lists:
                    declared_lists.append(list_name)
                    declared_lists_values.append(list_toadd) 
                else:
                    declared_lists_values[declared_lists.index[list_name]] = list_toadd
            #The 
            except:
                error("Failed to declare list <unknown name>", count)
    # ASK
    elif "ask" in input:
        try:
            #Get the "raw" version of what the user wants to ask
            input = input.replace("ask","")
            input = input.replace("(","")
            input = input.replace(")","")
            input = input.replace("'","")
            input = input.replace('"','')
            #If what the user wants to ask is a known variable, ask the content/value of the variable
            if input in declared_variables:
                askfor(declared_variables_values[declared_variables.index(input)])
            elif input in declared_lists:
                askfor(declared_lists_values[declared_lists.index(input)])
            else:
                askfor(input.strip())
        except:
            error("Failed to print('<whatever you asked>')",count)
    # MODULES
    for module in detect_modules():
        #If the given line contains any module's name, communicate with that module and process the desired function/action
        if module in input:
            with open(os.getcwd() + '\\Modules\\input.txt', 'x') as f:
                f.write(input)
            import subprocess
            subprocess.call(["python", os.getcwd()+'\\Modules\\'+module+'.py'], stdout = open(os.devnull, "w"), stderr = subprocess.STDOUT)
            os.system('python '+os.getcwd()+'\\Modules\\'+module+'.py')
            os.remove(os.getcwd()+'\\Modules\\input.txt')
            break
                    
            
            
        
        




#This function reads the specified file and separates it into lines, which are then read and processed by the process() function
def dataread(file):
    #Check if the specified file is a .fox file, else, notify the user that it is not
    try:
        file = file.removeprefix(".\\")
        assert file.split('.')[1] == 'fox'
    except:
        error(file+' is not a .fox file',0)
    #Try to open the file and convert the entire file into individual lines
    file1 = open(str(file), 'r')
    linecount = 0
    lines = []
    with open(str(file1).replace("<_io.TextIOWrapper name='","").replace("' mode='r' encoding='cp1252'>","").removeprefix(".\\")) as file:
        for line in file:
            if not line == "":
                if not line == " ":
                    line = line.replace('\n','')
                    lines.append(line)

        for line in lines:
            process(line,linecount)
            linecount = linecount + 1


#Detect and process the given arguments
argumentList = sys.argv[1:]
options = "i:c"
long_options = ["CheckInstall", "InputFile ="]
try:
    arguments, values = getopt.getopt(argumentList, options, long_options)
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-i", "--InputFile"):
            check_modules_folder()
            dataread(str(currentValue))
        if currentArgument in ("-c", "--CheckInstall"):
            print_version(fox_version)
except getopt.error as err:
    print (str(err))