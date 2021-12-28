"""
                        |-----------------------------------|
                        |              F O X                |        by Just_a_Mango
                        |-----------------------------------|        @Just-A-Mango on GitHub
"""


#Import the necessary modules
import sys, getopt, os


#Decides wether the program should generate a .log file when it's done processing
debug_mode = False


#Decalare the lists where the variables and their values are stored
declared_variables = []
declared_variables_values = []


#Declare the lists where the lists (inception!) and their values are stored
declared_lists = []
declared_lists_values = []


#Declare the lists where the functions and the lines they're assigned to are stored
declared_functions = []
declared_functions_lines = []
declared_functions_arguments = []
declared_functions_indents = []


#Declare the imported modules
modules = []


#Declare this language's current version
fox_version = 'InDev'


#Variable used to identify if there is an ongoing condition/exception in the current processed line
elses_lines = []
elses_indents = []

conditions = []
conditions_lines = []
conditions_level_of_indent = []


#Variales related to the 'while' function/featrue
while_values = []
while_conditions = []

is_bracket = False
all_lines = []


#Check if the modules' folder exists, and create it if it doesn't
def check_modules_folder():
    from pathlib import Path
    Path(os.getcwd() + "\\Modules\\").mkdir(parents=True, exist_ok=True)


#Check if given variables are of the same type
def check_variable_type(*objs):
    def _all_bases(o):
        for b in o.__bases__:
            if b is not object:
                yield b
            yield from _all_bases(b)
    s = [(i.__class__, *_all_bases(i.__class__)) for i in objs]
    return len(set(*s[:1]).intersection(*s[1:])) > 0


#Print the language's version and name
def print_version(version):
    print("|-----------------------------------|\r\n|          F O X  -  "+version+"          |        by Just_a_Mango\r\n|-----------------------------------|        @Just-A-Mango on GitHub\r\n")


#Installs any given module at runtime in the background
def install_module(module):
    try:
        import subprocess
        subprocess.call(["pip", "install", module], stdout = open(os.devnull, "w"), stderr = subprocess.STDOUT)
        import importlib
        i = importlib.import_module(module)
    except:
        pass


#Function used to ask, if the user asks
def askfor(arg):
    return input(arg)


#Function used to print a nice and clean error
def error(error,count):
    print("     \033[1m\033[91m😔  /!\ Fox Error /!\ 😔\033[0m     ")
    print("At \033[1m\033[92mline "+str(count)+"\033[0m ↓")
    print('\033[1m'+str(error)+'\033[0m')
    exit()


#All the properties associated with objects
def obj_property(object, property, count):
    if property == "removespace" and object.isalnum() == True:
        return object.replace("e","")
    elif property == "uppercase" and object.isalnum() == True:
        return object.upper()
    elif property == "lowercase" and object.isalnum() == True:
        return object.lower()
    elif property == "round" and object.isdecimal() == True:
        return str(int(object))
    else:
        error("Unknown property for object \x1B[3m\033[91m"+object+"\x1b[23m\033[0m -> \033[1m\033[95m"+property+"\033[0m", count)


#Basically the function that IS the language
def process(input,count):
    original_input = input
    global while_values
    global conditions
    global conditions_level_of_indent
    global is_bracket
    if [s for s in declared_variables if s in input]:
        match = [s for s in declared_variables if s in input][0]
        if "declare" in input and input.split(' ')[1] != match:
            input = input.replace(match, str(declared_variables_values[declared_variables.index(match)]))
        elif "declare" not in input:
            input = input.replace(match, str(declared_variables_values[declared_variables.index(match)]))
    if "(" in input and ")" in input and input[input.find("(")+1:input.find(")")].replace(".","").isdecimal() == True:
        input = input.replace(input[input.find("(")+1:input.find(")")], str(eval(input[input.find("(")+1:input.find(")")])))
    elif "(" in input and ")" in input and "+" in input[input.find("(")+1:input.find(")")]:
        try:
            input = input.replace(input[input.find("(")+1:input.find(")")], str(eval(input[input.find("(")+1:input.find(")")])))
        except:
            in_between_token = input[input.find("(")+1:input.find(")")]
            tokens = in_between_token.split('+')
            final_token = ""
            for token in tokens:
                if "." in token:
                    if token.split(".")[0] in declared_variables:
                        token = token.replace(token.split(".")[0], declared_variables_values[declared_variables.index(token.split('.')[0])])
                    final_token = final_token+token.replace(token, obj_property(token.split('.')[0], token.split('.')[1], count))
                else:
                    final_token = final_token+token
            input = input.replace(in_between_token, final_token)
    elif "(" in input and ")" in input and "." in input[input.find("(")+1:input.find(")")]:
        try:
            input = input.replace(input[input.find("(")+1:input.find(")")], str(eval(str(input[input.find("(")+1:input.find(")")]))))
        except:
            in_between_token = input[input.find("(")+1:input.find(")")]
            final_token = in_between_token.replace(in_between_token, obj_property(in_between_token.split('.')[0], in_between_token.split('.')[1], count))
            input = input.replace(in_between_token, final_token)
    elif "." in input and [s for s in input.split(' ') if "." in s][-1]:
        matching_token = [s for s in input.split(' ') if "." in s][-1]
        input = input.replace(matching_token, obj_property(matching_token.split(".")[0], matching_token.split(".")[1], count))
    if input[0] == " " and is_bracket == False:
        if declared_functions_lines and declared_functions_lines[-1].split('-')[1] == "":
            return
        else:
            pass
        matching_conditions = [num for num in conditions_lines if num.split('-')[1] == ""]
        matching_functions = [num for num in conditions_lines if num.split('-')[1] == ""]
        matches = []
        for match in matching_conditions:
            matches.append(conditions[conditions_lines.index(match)])
        if not matches:
            result = False
        else:
            for element in matches:
                if element == True:
                    result = True
                else:
                    result = False
                    break
        if "}" not in input and "if" not in input and "define" not in input and "else" not in input:
            if result == True:
                process(input.lstrip(), count)
            else:
                pass
        else:
            if result == True:
                is_bracket = True
                process(input, count)
            else:
                pass
            
    # PRINT
    elif "print" in input:
        input = input.lstrip()
        # print(something)
        try:
            #Remove print("") to only get what the user typed as the input
            input = input.replace("print","").replace("(","").replace(")","").replace("'","").replace('"','')
            print(input)
        except:
            error("Failed to print('<whatever you typed>')",count)
    # DECLARE
    elif "declare" in input:
        # declare var_name = var_value
        # OR
        # declare list list_name = list_value
        try:
            assert input.split(' ')[0] == "declare"
        except:
            error("Wrong word order when declaring variable", count)
        if not 'list' in input:
            #Try to add declared variable and its value to declared_variables and declared_variables_values
            try:
                #Get the "raw" variable name
                input = input.lstrip()
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
                elif var_value in declared_variables:
                    declared_variables.append(var_name)
                    declared_variables_values.append(declared_variables_values[declared_variables.index(var_value)])
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
        # ask(something)
        try:
            #Get the "raw" version of what the user wants to ask
            input = input.replace("ask","")
            input = input.replace("(","")
            input = input.replace(")","")
            input = input.replace("'","")
            input = input.replace('"','')
            askfor(input)
        except:
            error("Failed to print('<whatever you asked>')",count)
    # IF
    elif "if" in input:
        is_bracket = False
        # if (something) {
        # }
        #Make sure the given syntax is correct, else, *error*
        try:
            assert "(" in input and ")" in input and "{" in input
        except:
            error("Please check the condition syntax",count)
        #Replace all the unused words to only get the condition (for example, 'if (something = 10) {' => 'something=10'))
        input = input.replace("if","")
        input = input.replace("(","")
        input = input.replace(")","")
        input = input.replace("{","")
        #Make sure the wanted condition is an '=', else, more coming soon...
        if "=" in input:
            #Replace the blank spaces and split the given expression into two to only get the variable's name and its (tested) value
            input = input.replace(" ","")
            input = input.split("=")
            #If the given condition is true, then execute the code, if the condition isn't true, then do nothing
            if input[0] in declared_variables:
                var_name = input[0]
                var_value = input[1]
                if str(var_value) == str(declared_variables_values[declared_variables.index(var_name)]):
                    conditions.append(True)
                    conditions_lines.append(str(count)+'-')
                    conditions_level_of_indent.append(len(original_input) - len(original_input.lstrip(' ')))
                else:
                    conditions.append(False)
                    conditions_lines.append(str(count)+'-')
                    conditions_level_of_indent.append(len(original_input) - len(original_input.lstrip(' ')))
                    pass
            elif input[1] in declared_variables:
                var_name = input[1]
                var_value = input[0]
                if str(var_value) == str(declared_variables_values[declared_variables.index(var_name)]):
                    conditions.append(True)
                    conditions_lines.append(str(count)+'-')
                    conditions_level_of_indent.append(len(original_input) - len(original_input.lstrip(' ')))
                else:
                    conditions.append(False)
                    conditions_lines.append(str(count)+'-')
                    conditions_level_of_indent.append(len(original_input) - len(original_input.lstrip(' ')))
                    pass
            #The following code allows the condition to be True or False even if the given condition doesn't contain a variable
            elif input[0] == input [1] and check_variable_type(input[0], input[1]) == True:
                conditions.append(True)
                conditions_lines.append(str(count)+'-')
                conditions_level_of_indent.append(len(original_input) - len(original_input.lstrip(' ')))
            elif input[0] != input [1] and check_variable_type(input[0], input[1]) == True:
                conditions.append(False)
                conditions_lines.append(str(count)+'-')
                conditions_level_of_indent.append(len(original_input) - len(original_input.lstrip(' ')))
                pass
            else:
                error("Unknown variable referenced in condition", count)
    # ELSE
    elif "else" in input:
        try:
            assert "{" in input
        except:
            error("Bad syntax when declaring condition exception -> "+input,count)
        elses_lines.append(str(count)+"-")
        elses_indents.append(len(original_input) - len(original_input.lstrip(' ')))
    #Detect the end of a condition
    elif "}" in input:
        is_bracket = False
        level_of_indent = len(input) - len(input.lstrip(' '))
        if conditions_lines and [num for num in conditions_lines if num.split('-')[1] == ""]:
            conditions_lines[conditions_level_of_indent.index(level_of_indent)] = conditions_lines[conditions_level_of_indent.index(level_of_indent)] + str(count)
        elif declared_functions_lines and declared_functions_lines[declared_functions_indents.index(level_of_indent)].split('-')[1] == "":
            declared_functions_lines[declared_functions_indents.index(level_of_indent)] = declared_functions_lines[declared_functions_indents.index(level_of_indent)] + str(count)
    # MODULES
    elif "import" in input:
        # import <module_name>
        #If a module is imported, add it to the imported modules' list
        modules.append(input.replace("import","").replace(" ",""))
        try:
            open(os.getcwd()+'\\Modules\\'+input.replace("import","").replace(" ","")+'.py', 'r')
        except:
            error("Unknown module \033[1m\033[91m"+input.replace("import","").replace(" ","")+'\033[0m', count)
    elif "define" in input:
        try:
            assert "{" in input and "(" in input and ")" in input
        except:
            error("Bad syntax when trying to define a function -> "+input, count)
        function_name = input.replace("define","").replace(" ","").replace("("+input[input.find("(")+1:input.find(")")]+")","").replace("{","")
        function_arguments = input[input.find("(")+1:input.find(")")]
        declared_functions.append(function_name)
        declared_functions_arguments.append(function_arguments)
        declared_functions_lines.append(str(count)+'-')
        declared_functions_indents.append(len(input) - len(input.lstrip(' ')))
    elif "exit" in input:
        try:
            assert "()" in input
        except:
            error("Bad syntax when calling the exit() function", count)
        exit()
    elif declared_functions:
        for function in declared_functions:
            if function in input:
                try:
                    assert "(" in input and ")" in input
                except:
                    error("You forgot the () when calling "+function+"() -> "+input, count)
                func_lines = declared_functions_lines[declared_functions.index(function)].split('-')
                rng = list(range(int(func_lines[0]), int(func_lines[-1])))
                rng.remove(rng[0])
                rng = [x - 1 for x in rng]
                for line in rng:
                    is_bracket = True
                    process(str(all_lines[line]).removeprefix('    '), count)
                break
    elif [s for s in modules if s in input] or [s for s in declared_functions if s in input]:
        if [s for s in declared_functions if s in input]:
            function =  [s for s in declared_functions if s in input][0]
    #If the given line contains any module's name, communicate with that module and process the desired function/action
    else:
        try:
            assert len(modules) > 1
        except:
            try:
                assert any(functionn in input for functionn in declared_functions) == False
            except:
                for function in declared_functions:
                    if function in input:
                        try:
                            assert "(" in input and ")" in input
                        except:
                            error("You forgot the () when calling "+function+"() -> "+input, count)
                        func_lines = declared_functions_lines[declared_functions.index(function)].split('-')
                        rng = list(range(int(func_lines[0]), int(func_lines[-1])))
                        rng.remove(rng[0])
                        rng = [x - 1 for x in rng]
                        print(rng)
                        for line in rng:
                            process(all_lines[line], count)
                        break
            try:
                assert any(module in input for module in modules) == False
                error("Unknown function referenced -> "+str(input), count)
            except:
                 for module in modules:
                    if module in input and "import" not in input:
                        with open(os.getcwd() + '\\Modules\\input.txt', 'x') as f:
                            f.write(input)
                        import subprocess
                        subprocess.call(["python", os.getcwd()+'\\Modules\\'+module+'.py'], stdout = open(os.devnull, "w"), stderr = subprocess.STDOUT)
                        os.system('python '+os.getcwd()+'\\Modules\\'+module+'.py')
                        os.remove(os.getcwd()+'\\Modules\\input.txt')
                        return
        for module in modules:
            if module in input and "import" not in input:
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
    with open(str(file1).replace("<_io.TextIOWrapper name='","").replace("' mode='r' encoding='cp1252'>","")) as file:
        for line in file:
            line = line.replace('\n','')
            lines.append(line)
        global all_lines
        all_lines = lines
        linecount = 1
        for line in lines:
            if line.isspace() == True or line == '':
                linecount = linecount + 1
            else:
                process(line, linecount)
                linecount = linecount + 1




#Detect and process the given arguments
import time
start_time = time.time()
argumentList = sys.argv[1:]
options = "i:c"
long_options = ["CheckInstall", "InputFile ="]
try:
    arguments, values = getopt.getopt(argumentList, options, long_options)
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-i", "--InputFile"):
            check_modules_folder()
            dataread(str(currentValue))
        elif currentArgument in ("-c", "--CheckInstall"):
            print_version(fox_version)
except getopt.error as err:
    print(str(err))
run_time = str((time.time() - start_time))
if debug_mode == True:
    with open('debug.log','w') as f:
        f.write('Run Time: '+run_time+" seconds\r")
else:
    try:
        import os
        os.remove("debug.log")
    except:
        pass