#Put all your needed imports here ('os' is required)
import os


#Main function, input represents the given line where the function is called
def main(input):
    #Put all your code/actions here
    print("Hello World")
    print("This is an example module")


#Code used to communicate with the main file
output = ""
with open(os.getcwd() + '\\Modules\\input.txt', 'r') as f:
    output = f.readlines()[0]
    main(output)
