"""
                        |-----------------------------------|
                        |              F O X                |        by Just_a_Mango
                        |-----------------------------------|        @Just-A-Mango on GitHub
"""
#Import the necessary modules
import sys, getopt, subprocess, os

#Decalare the lists where the variables and their values are stored
declared_variables = []
declared_variables_values = []

#Declare this language's current version and remove the update script
fox_version = 'AlphaDev'
try:
    os.remove("updatefox.py")
except:
    pass

#Print the language's version and name
def print_version(version):
    print("|-----------------------------------|\r\n|     F O X  -  version "+version+"    |        by Just_a_Mango\r\n|-----------------------------------|        @Just-A-Mango on GitHub\r\n")

def install_module(module):
    subprocess.call(["pip", "install", module], stdout = open(os.devnull, "w"), stderr = subprocess.STDOUT)
    

#Function used to update the language
def update():
    try:
        from git import Repo
    except:
        install_module('gitpython')
    try:
        if os.path.exists("updatefox.py"):
            os.remove("updatefox.py")
        else:
            pass
        with open('updatefox.py', 'x') as f:
            f.write('from git import Repo\nimport os, shutil, filecmp\npath = os.getcwd()\ntry:\n    Repo.clone_from("https://github.com/Just-A-Mango/fox", path+"//updatedfox")\n    if filecmp.cmp("fox.py", "//updatedfox//fox.py") == True:\n        print("Hooray! Your Fox installation is up-to-date!")\n    else:\n        os.remove("fox.py")\n        shutil.move(path+"//updatedfox//fox.py", path+"//fox.py")\n        shutil.rmtree(path+"//updatedfox")\nexcept:\n    print("Failed to download the new(?) Fox version")')
        os.system("python updatefox.py")
        exit()
    except:
        print("Failed to repair. Please try re-installing Fox.")

#Function used to ask, if the user asks!
def askfor(arg):
    return input(arg)

#Function used to print a nice and clean error
def error(error,count):
    print("       /!\ Fox Error /!\ ")
    print("At line "+str(count)+" ↓")
    print(str(error))
    exit()

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
                    declared_variables_values[declared_variables.index(var_name)] = var_value
            #If the value is 'ask'(at least contains it), then ask!
            elif 'ask(' in var_value:
                declared_variables.append(var_name)
                declared_variables_values.append(askfor(var_value.replace("(","").replace(")","").replace("ask","").replace("'","").replace('"','')))
            #Else, just declare and add it
            else:
                declared_variables.append(var_name)
                declared_variables_values.append(var_value)
        #If it fails, notify the user
        except:
            error("Failed to declare variable "+(input.strip.split('=')[0].replace("declare","")),count)
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
            else:
                askfor(input.strip())
        except:
            error("Failed to print('<whatever you asked>')",count)    








#This function reads the specified file and separates it into lines, which are then read and processed by the process() function
def dataread(file):
    #Check if the specified file is a .fox file, else, notify the user that it is not
    try:
        assert file.split('.')[1] == 'fox'
    except:
        error(file+' is not a .fox file',0)
    #Try to open the file and convert the entire file into individual lines
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
 
 






#Detect and process the given arguments
argumentList = sys.argv[1:]
options = "i:cu"
long_options = ["CheckInstall", "InputFile =", "Update"]
try:
    arguments, values = getopt.getopt(argumentList, options, long_options)
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-i", "--InputFile"):
            dataread(str(currentValue))
        if currentArgument in ("-c", "--CheckInstall"):
            print_version(fox_version)   
        elif currentArgument in ("-u", "--Update"):
            update()
except getopt.error as err:
    print (str(err))
    