<h1 align="center">📄 "Documentation" 📄</h1>

## Code examples
Here are a few examples of what Mango's syntax looks like/will look like (**VERY WIP**!)
- Hello World:
```python
print(Hello World)
```
- Print what the user asked:
```python
declare user_asked = ask(What do you want to print ?)
print(user_asked)
```
- Do some basic math and then print it:
```python
print(5+7/5*98)
```
- If the number the user entered is 5, then print 'The number is 5!', else, print 'The number is not 5!'
```cs
declare my_var = ask(Enter a number: )
if (my_var = 5) {
 print(The number is 5!)
}
else {
 print(The number is not 5!)
}
```
- Declare a function and call it
```cs
define my_function() {
 print(You just called my_function!)
}
my_function()
```
And the list goes on...
## Arguments
Mango supports arguments when executing it, among them are:\
 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ***This executes the given .mango file(basically the same thing in Python as doing python myfile.py)***
```sh
mango -i <yourfile.mango>
mango --InputFile <yourfile.mango>
```
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ***This checks the current Mango installation and prints the version***
```sh
mango -c
mango --CheckInstall
```
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ***The -d argument means debug mode***
```sh
mango -i <yourfile.mango> -d
```

## Making modules
What I call modules are python files that are used to add functions. You can add one function per python file, and the name of the file defines the name of the function you want to add (for example, if you want to add a 'create' function, then create a python file named 'create.py' in the Modules folder, or, to give another example, if you want to add a function say(what_i_need_to_say), then create a python file in the Modules folder called 'say.py' and Mango will automatically recognize and call the file once the function is called)
You can find a sample/example module [here](https://github.com/Just-A-Mango/mango/blob/main/Modules/example_module.py) or below:
```python
#Put all your needed imports here
# ⚠️ YOU MUST NOT REMOVE 'OS' ⚠️ 
import os


#The name of your module, should be indicative of what module has been called in case of an error
module_name = "Example Module"


#Function used to report error, can be modified, although the name mustn't change
def error(error):
    print("        \033[1m\033[91m⚠️   Mango Module Error  ⚠️\033[0m        ")
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
```
