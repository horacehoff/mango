#Put all your needed imports here
# ⚠️ YOU MUST NOT REMOVE 'OS' ⚠️ 
import os


#The name of your module, should be indicative of what module has been called in case of an error
module_name = "Example Module"


#Function used to report error, can be modified, although the name mustn't change
def error(error):
    print("        \033[1m\033[91m⚠️   Fox Module Error  ⚠️\033[0m        ")
    print("At \033[1m\033[92mline "+str(line)+"\033[0m with module \33[93m"+module_name+"\033[0m ↓")
    print('\033[1m'+str(error)+'\033[0m')
    exit()


#Main function, input represents the given line where the function is called, current_line represents the line number where this module is called
# ⚠️ YOU MUST NOT ALTER THE NAME OR THE ARGUMENTS OF THE FOLLOWING FUNCTION ⚠️ 
def main(input, current_line):
    #Put all your code/actions here
    print(input)
    error("An example error")


#Code used to communicate with the main file
# ⚠️ YOU MUST NOT DELETE/ALTER THE FOLLOWING CODE ⚠️
output = ""
line = ""
with open(os.getcwd() + '\\Modules\\input.txt', 'r') as f:
    output = f.readlines()
    line = output[1]
    main(output[0], line)