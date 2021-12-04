<h1 align="center">📄 Documentation 📄</h1>

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
And the list goes on...

## Arguments
Fox supports arguments when executing it, among them are:\
 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ***This executes the given .fox file(basically the same thing in Python as doing python <myfile.py>)***
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
You can make modules for Fox using python. 
The name of the module's python file defines the name of the function you want to add (for example, if you want to add a 'create' function, then create a python file named 'create.py' in the Modules folder)
You can find a sample/example module here[https://github.com/Just-A-Mango/fox/edit/main/.github/markdown/examples.md]

