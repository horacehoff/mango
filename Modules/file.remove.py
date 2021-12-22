#Put all your needed imports here
# ⚠️ YOU MUST NOT REMOVE 'OS' ⚠️ 
import os


#Main function, input represents the given line where the function is called
# ⚠️ YOU MUST NOT ALTER THE NAME OR THE ARGUMENTS OF THE FOLLOWING FUNCTION ⚠️ 
def main(input):
    #Put all your code/actions here
    file_path = input[input.find('(')+1:input.find(')')]
    os.remove(file_path)
    

#Code used to communicate with the main file
# ⚠️ YOU MUST NOT DELETE THE FOLLOWING CODE ⚠️ 
output = ""
with open(os.getcwd() + '\\Modules\\input.txt', 'r') as f:
    output = f.readlines()[0]
    main(output)