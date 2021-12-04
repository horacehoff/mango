#Put all your needed imports here ('os' is required)
import os


#Main function
def main(input):
    #Put all your code/actions here
    input = input.replace("x","")
    print("hello")
    #If input (when returning it) is null, then nothing will be printed


#Code used to communicate with the main file
output = ""
with open(os.getcwd() + '\\Modules\\input.txt', 'r') as f:
    output = f.readlines()[0]
    main(output)
