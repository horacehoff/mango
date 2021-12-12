<h1 align="center">📄 "Documentation" 📄</h1>

## Code examples

- Hello World:
```python
print(Hello World)
```
- Print what the user asked:
```python
user_asked = ask(What do you want to print ?)
print(user_asked)
```
- Do some basic math and then print it:
```python
print(5+7/5*98)
```
- If the number the user entered is 5, then print 'The number is 5!'
```cs
declare my_var = ask(Enter a number: )
if (my_var = 5) {
 print(5+7/5*98)
}
```
And the list goes on...

## Arguments
Fox supports arguments when executing it, among them are:\
 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ***This executes the given .fox file(basically the same thing in Python as doing python myfile.py)***
```sh
fox.py -i <yourfile.fox>
fox.py --InputFile <yourfile.fox>
```
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ***This retrieves the current repository and then updates the language***
```sh
fox.py -u
fox.py --Update
```
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ***This checks the current Fox installation and prints the version***
```sh
fox.py -c
fox.py --CheckInstall
```

## Making modules
What I call modules are python files that are used to add functions. You can add one function per python file, and the name of the file defines the name of the function you want to add (for example, if you want to add a 'create' function, then create a python file named 'create.py' in the Modules folder, or, to give another example, if you want to add a function say(what_i_need_to_say), then create a python file in the Modules folder called 'say.py' and Fox will automatically recognise and call the file once the function is called)
You can find a sample/example module [here](https://github.com/Just-A-Mango/fox/blob/main/Modules/example_module.py) or below:
```python
#Put all your needed imports here ('os' is required)
import os


#Main function, input represents the given line where the function is called
def main(input):
    #Put all your code/actions here
    print("Hello World")
    print("This is an example module")


#Code used to communicate with the main file
# ⚠️ YOU MUST NOT DELETE THE FOLLOWING CODE ⚠️ 
output = ""
with open(os.getcwd() + '\\Modules\\input.txt', 'r') as f:
    output = f.readlines()[0]
    main(output)
```

