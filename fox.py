"""
                        |-----------------------------------|
                        |              F O X                |        by Just_a_Mango
                        |-----------------------------------|        @Just-A-Mango on GitHub
"""


#Import the necessary modules
import sys, getopt, os


#Decides wether the language should generate a .log file when it's done processing
debug_mode = False


#Lists where the variables and their values are stored
declared_variables = []
declared_variables_values = []


#Lists where the lists (inception!) and their values are stored
declared_lists = []
declared_lists_values = []


#Lists where the functions and the lines they're assigned to are stored
declared_functions = []
declared_functions_lines = []
declared_functions_arguments = []
declared_functions_indents = []


#Imported modules
modules = []


#Language's current version, and variable that tells the language if it is in console-editor mode or not
fox_version = 'InDev'
is_editor = False


#Variables used to identify if there is an ongoing condition/exception in the current processed line
elses_lines = []
elses_indents = []

conditions = []
conditions_lines = []
conditions_level_of_indent = []

to_be_replaced = []
to_be_replaced_with = []

#Variable used to identify if there is an ongoing loop
loop_lines = []
loop_level_of_indent = []


# Variable used to identify if current line contains indent-sensitive statements, and list used to contain all the lines (make all the lines accessible in any scope)
is_bracket = False
all_lines = []


#Check if the modules' folder exists, and create it if it doesn't
def check_modules_folder():
    from pathlib import Path
    Path(os.getcwd() + "\\Modules\\").mkdir(parents=True, exist_ok=True)


#Print the language's version and name
def print_version(version):
    print("|-----------------------------------|\r\n|         \U0001F98A F O X \U0001F98A -  "+version+"      |        by \033[1mJust_a_Mango\033[0m\r\n|-----------------------------------|        \033[1m@Just-A-Mango\033[0m on \033[1mGitHub\033[0m\r\n")


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
def error(error):
    print("        \033[1m\033[91m⚠️   Fox Error  ⚠️\033[0m        ")
    print("At \033[1m\033[92mline "+str(linecount)+"\033[0m ↓")
    print('\033[1m'+str(error)+'\033[0m')
    if is_editor == False:
        from sys import exit
        exit()


#All the properties associated with objects
def obj_property(object, property):
    if property == "uppercase":
        if object.isdecimal() == True:
            error("Object does not contain letters")
        return object.upper()
    elif property == "lowercase":
        if object.isdecimal() == True:
            error("Object does not contain letters")
        return object.lower()
    elif property == "onlynumbers":
        if object.isdecimal() == True:
            return "True"
        if object.isdecimal() == False:
            return "False"
    elif "remove[" in property:
        property = property.replace("remove","").replace("[","").replace("]","")
        try:
            assert property != None or property != ""
        except:
            error("⛔ Remove property cannot be empty")
        return object.replace(property, "")
    elif "replace[" in property:
        property = property.replace("replace","").replace("[","").replace("]","")
        try:
            assert property != None or property != ""
        except:
            error("⛔ Replace property cannot be empty")
        try:
            assert "," in property
        except:
            error("⛔ Replace property takes in 2 arguments: only got 1")
        to_be_replaced = property.rsplit(",", 1)
        return object.replace(to_be_replaced[0], to_be_replaced[1])
    else:
        error("❓ Unknown property for object \x1B[3m\033[91m"+object+"\x1b[23m\033[0m -> \033[1m\033[95m"+property+"\033[0m")


#Basically the function that IS the language
def process(input,count):
    original_input = input
    global conditions
    global elses_lines
    global elses_indents
    global conditions_level_of_indent
    global is_bracket
    global to_be_replaced
    global to_be_replaced_with
    #Replace a variable name by its value if it isn't declaring
    if [s for s in declared_variables if s in input]:
        for match in [s for s in declared_variables if s in input]:
            if "declare" in input and input.split(' ')[1] != match:
                input = input.replace(match, str(declared_variables_values[declared_variables.index(match)]))
            elif "declare" not in input:
                input = input.replace(match, str(declared_variables_values[declared_variables.index(match)]))
    #Replace a list name by its value if it isn't declaring -> MAY NOT BE WORKING
    elif [s for s in declared_lists if s in input] and "for" not in input:
        for match in [s for s in declared_lists if s in input]:
            if "declare" in input and input.split(' ')[1] != match:
                input = input.replace(match, str(declared_lists_values[declared_lists.index(match)]))
            elif "declare" not in input:
                input = input.replace(match, str(declared_lists_values[declared_lists.index(match)]))
    #If the content of the parentheses is math, process it and replace it by the result
    if "(" in input and ")" in input and input[input.find("(")+1:input.find(")")].replace(".","").isdecimal() == True:
        input = input.replace(input[input.find("(")+1:input.find(")")], str(eval(input[input.find("(")+1:input.find(")")])))
    elif "if" in input and "(" in input and ")" in input and "." in input:
        if "=" in input:
            my_input = input.replace("if","").replace("(","").replace(")","").replace("{","").replace(" ","")
            my_input = my_input.split("=")
            if "." in my_input[0]:
                input = input.replace(my_input[0], obj_property(my_input[0].split(".")[0], my_input[0].split(".")[1]))
            if "." in my_input[1]:
                input = input.replace(my_input[1], obj_property(my_input[1].split(".")[0], my_input[1].split(".")[1]))
    #If the content of the parentheses contains +(which means "appending things to other things"), try to process it if it's math or else just "append things to other things"
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
                    final_token = final_token+token.replace(token, obj_property(token.split('.')[0], token.split('.')[1]))
                else:
                    final_token = final_token+token
            input = input.replace(in_between_token, final_token)
    #If the content of the parentheses is a single object with a property, then process that property and replace 'object.property' => 'ouput'
    elif "(" in input and ")" in input and "." in input[input.find("(")+1:input.find(")")]:
        try:
            input = input.replace(input[input.find("(")+1:input.find(")")], str(eval(str(input[input.find("(")+1:input.find(")")]))))
        except:
            in_between_token = input[input.find("(")+1:input.find(")")]
            final_token = in_between_token.replace(in_between_token, obj_property(in_between_token.split('.')[0], in_between_token.split('.')[1]))
            input = input.replace(in_between_token, final_token)
    #If, in the line, there is no parentheses but a single object with a property, do the same thing as the previous condition
    elif "." in input and [s for s in input.split(' ') if "." in s][-1]:
        matching_token = [s for s in input.split(' ') if "." in s][-1]
        input = input.replace(matching_token, obj_property(matching_token.split(".")[0], matching_token.split(".")[1]))
    #The function in charge of recognizing if the current processed line is (under ?) a condition/function/loop/etc and choosing wether to process it or not
    if input[0] == " " and is_bracket == False:
        if elses_lines and elses_lines[-1].split('-')[1] == "":
            if conditions[conditions_level_of_indent.index([num for num in conditions_level_of_indent if num == (len(original_input) - len(original_input.lstrip(' '))-4)][0])] != True:
                result = True
            else:
                result = False
        else:
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
    elif "replace" and "with" in input:
        print(input.split(" ")[3])
        to_be_replaced.append(input.split(" ")[1])
        to_be_replaced_with.append(input.split(" ")[3])
    # PRINT
    elif "print" in input:
        input = input.lstrip()
        # print(something)
        try:
            #Remove print("") to only get what the user typed as the input
            input = input.replace("print","").replace("(","").replace(")","").replace("'","").replace('"','')
            print(input)
        except:
            error("⚠️  Failed to print('whatever you typed')",count)
    # DEBUG
    elif "debug" in input:
        try:
            assert "(" in input and ")" in input
        except:
            error("⛔ Bad syntax when calling debug function")
        print("\33[31m[DEBUG]\33[0m\33[3m"+input.replace("debug","").replace("(","").replace(")","")+"\33[0m")
    # DECLARE
    elif "declare" in input:
        # declare var_name = var_value
        # OR
        # declare list list_name = list_value
        try:
            assert input.split(' ')[0] == "declare"
        except:
            error("Wrong word order when declaring variable")
        if not 'list' in input:
            #Try to add declared variable and its value to declared_variables and declared_variables_values
            try:
                #Get the "raw" variable name
                input = input.lstrip()
                input = input.split('=')
                var_name = input[0].replace("declare","").lstrip().replace(" ","")
                var_value = input[1].lstrip()
                try:
                    assert any(i.isdigit() for i in var_name) == False
                except:
                    error("⛔ Cannot declare variable with any digit in its name -> "+var_name)
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
                error("Failed to declare list <unknown name>")
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
            error("⚠️  Failed to ask('<whatever you asked>')",count)
    # IF
    elif "if" in input:
        is_bracket = False
        # if (something) {
        # }
        #Make sure the given syntax is correct, else, *error*
        try:
            assert "(" in input and ")" in input and "{" in input
        except:
            error("\U0001F64F Please check the condition syntax",count)
        #Replace all the unused syntax to only get the condition (for example, 'if (something = 10) {' => 'something=10'))
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
            elif input[0] == input [1]:
                conditions.append(True)
                conditions_lines.append(str(count)+'-')
                conditions_level_of_indent.append(len(original_input) - len(original_input.lstrip(' ')))
            elif input[0] != input [1]:
                conditions.append(False)
                conditions_lines.append(str(count)+'-')
                conditions_level_of_indent.append(len(original_input) - len(original_input.lstrip(' ')))
                pass
            else:
                error("❓ Unknown variable referenced in condition")
    #FOR # IN #
    elif "for" in input:
        try:
            assert len(input.split(" ")) == 5
            assert "{" in input
            assert "(" in input and ")" in input
        except:
            error("⛔ Bad syntax when calling loop")
        given_name = input.replace("for","").replace("(","").replace(")","").replace("{","").replace(" ","").split("in",1)[0]
        given_list = input.replace("for","").replace("(","").replace(")","").replace("{","").replace(" ","").split("in",1)[1]
        try:
            assert given_list in declared_lists
        except:
            error("⛔ Unknown list -> \x1B[3m\033[91m"+given_list+"\x1b[23m\033[0m")
        loop_lines.append(str(count)+"-")
        loop_level_of_indent.append(len(original_input) - len(original_input.lstrip(' ')))
    #Detect the end of a condition/function/loop/etc
    elif "}" in input:
        if "else" in input:
            try:
                assert "{" in input
            except:
                error("⛔ Bad syntax when declaring exception ")
            elses_lines.append(str(count)+"-")
            elses_indents.append(len(original_input) - len(original_input.lstrip(' ')))
            is_bracket = False
            level_of_indent = len(original_input) - len(original_input.lstrip(' '))
            if conditions_lines and [num for num in conditions_lines if num.split('-')[1] == ""]:
                conditions_lines[conditions_lines.index([num for num in conditions_lines if num.split('-')[1] == ""][-1])] = conditions_lines[conditions_lines.index([num for num in conditions_lines if num.split('-')[1] == ""][-1])] + str(count)
            else:
                error("⛔ Cannot find owner of bracket")
        elif "{" in input:
            error("⛔ Bad syntax when declaring exception ")
        else:
            is_bracket = False
            level_of_indent = len(original_input) - len(original_input.lstrip(' '))
            if elses_lines and [num for num in elses_lines if num.split('-')[1] == ""]:
                elses_lines[elses_indents.index(level_of_indent)] = elses_lines[elses_indents.index(level_of_indent)] + str(count)
            elif loop_lines and [num for num in loop_lines if num.split('-')[1] == ""]:
                loop_lines[loop_level_of_indent.index(level_of_indent)] = loop_lines[loop_level_of_indent.index(level_of_indent)] + str(count)
            elif conditions_lines and [num for num in conditions_lines if num.split('-')[1] == ""]:
                conditions_lines[conditions_level_of_indent.index(level_of_indent)] = conditions_lines[conditions_level_of_indent.index(level_of_indent)] + str(count)
            elif declared_functions_lines and declared_functions_lines[declared_functions_indents.index(level_of_indent)].split('-')[1] == "":
                declared_functions_lines[declared_functions_indents.index(level_of_indent)] = declared_functions_lines[declared_functions_indents.index(level_of_indent)] + str(count)
            else:
                error("⛔ Cannot find owner of bracket")
        
    # MODULES
    elif "import" in input and "un_import" not in input:
        # import <module_name>
        #If a module is imported, add it to the imported modules' list
        modules.append(input.replace("import","").replace(" ",""))
        try:
            open(os.getcwd()+'\\Modules\\'+input.replace("import","").replace(" ","")+'.py', 'r')
        except:
            error("❓ Unknown module \033[1m\033[91m"+input.replace("import","").replace(" ","")+'\033[0m')
    # UN_IMPORT MODULES
    elif "un_import" in input:
        # un_import <module_name>
        try:
            modules.remove(input.replace("un_import","").replace(" ",""))
        except:
            try:
                open(os.getcwd()+'\\Modules\\'+input.replace("un_import","").replace(" ","")+'.py', 'r')
                error("⛔ Module is not imported -> \033[1m\033[91m"+input.replace("un_import","").replace(" ","")+'\033[0m')
            except Exception as e:
                error("⛔ Module does not exist -> \033[1m\033[91m"+input.replace("un_import","").replace(" ","")+'\033[0m')
    # DEFINE -> CONDITIONS/ARGUMENTS NOT WORKING
    elif "define" in input:
        #define function_name(argument1, argument2) {
        #}
        #Let the user know if the syntax is wrong
        try:
            assert "{" in input and "(" in input and ")" in input
        except:
            error("⛔ Bad syntax when trying to define a function -> "+input)
        #Append the current line, indentation, name, and arguments to the lists
        function_name = input.replace("define","").replace(" ","").replace("("+input[input.find("(")+1:input.find(")")]+")","").replace("{","")
        function_arguments = input[input.find("(")+1:input.find(")")]
        declared_functions.append(function_name)
        declared_functions_arguments.append(function_arguments)
        declared_functions_lines.append(str(count)+'-')
        declared_functions_indents.append(len(input) - len(input.lstrip(' ')))
    # STOP
    elif "stop" in input:
        #stop()
        #Let the user know if the syntax is wrong
        try:
            assert "()" in input
            exit()
        except Exception as e:
            error("⛔ Bad syntax when calling the \033[91mstop()\033[0m function")
    # FUNCTION/MODULE CALLING
    elif [s for s in modules if s in input] or [s for s in declared_functions if s in input]:
        #FUNCTIONS
        if declared_functions and [s for s in declared_functions if s in input and declared_functions_lines[declared_functions.index(s)].split('-')[1] != ""]:
            function =  [s for s in declared_functions if s in input and declared_functions_lines[declared_functions.index(s)].split('-')[1] != ""][0]
            try:
                assert "(" in input and ")" in input
            except:
                error("You forgot the () when calling \033[91m"+function+"()\033[0m -> "+input)
            func_lines = declared_functions_lines[declared_functions.index(function)].split('-')
            rng = list(range(int(func_lines[0]), int(func_lines[-1])))
            rng.remove(rng[0])
            rng = [x - 1 for x in rng]
            for line in rng:
                process(all_lines[line].removeprefix('    '))
            return
        #MODULES
        elif modules and [s for s in modules if s in input] and "import" not in input:
            module = [s for s in modules if s in input][0]
            with open(os.getcwd() + '\\Modules\\input.txt', 'x') as f:
                f.write(input+"\n"+str(count))
            import subprocess
            subprocess.call(["python", os.getcwd()+'\\Modules\\'+module+'.py'], stdout = open(os.devnull, "w"), stderr = subprocess.STDOUT)
            os.system('python '+os.getcwd()+'\\Modules\\'+module+'.py')
            os.remove(os.getcwd()+'\\Modules\\input.txt')
            return
    else:
            error("❓ Unknown function/object -> \033[91m"+input+"\033[0m")

       


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
    global linecount
    linecount = 0
    lines = []
    with open(str(file1).replace("<_io.TextIOWrapper name='","").replace("' mode='r' encoding='cp1252'>","")) as file:
        for line in file:
            line = line.replace('\n','')
            lines.append(line)
        for line in lines:
            for replacement in to_be_replaced_with:
                if replacement in line:
                    line = line.replace(replacement, to_be_replaced[to_be_replaced_with.index(replacement)])
        global all_lines
        all_lines = lines
        linecount = 1
        for line in lines:
            if line.isspace() == True or line == '' or "#" in line or "//" in line:
                linecount = linecount + 1
            else:
                process(line, linecount)
                linecount = linecount + 1




#Detect and process the given arguments
is_editor = False
import timeit
argumentList = sys.argv[1:]
options = "i:cd"
long_options = ["CheckInstall", "InputFile =", "Debug"]
try:
    arguments, values = getopt.getopt(argumentList, options, long_options)
    if arguments:
        for currentArgument, currentValue in arguments:
            if currentArgument in ("-i", "--InputFile"):
                check_modules_folder()
                dataread(str(currentValue))
            elif currentArgument in ("-c", "--CheckInstall"):
                print_version(fox_version)
            elif currentArgument in ("-d", "--Debug"):
                debug_mode = True
                global start
                start = timeit.default_timer()
    else:
        #If no argument is given, then start the console
        is_editor = True
        import platform
        if platform.system() == "Windows":
            os.system('cls')
        elif platform.system() == "Linux" or platform.system() == "Darwin":
            os.system('clear')
        print("----    \033[1m\033[91m\U0001F98A Fox \U0001F98A\033[0m    ----")
        index = 1
        while True:
            process(input(">>"), index)
            index = index + 1
except getopt.error as err:
    print(str(err))
end = timeit.default_timer()
if debug_mode:
    run_time = format(float(end - start), ".50f")
    with open('debug.log','w') as f:
        f.write('Run Time(it is highly probable this is false): '+run_time+" seconds")
else:
    try:
        import os
        os.remove("debug.log")
    except:
        pass