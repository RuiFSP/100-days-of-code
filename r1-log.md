# #100DaysOfCode Log - Round 1 - [Rui Pinto]

The log of my <b>#100DaysOfCode</b> challenge. Started on [January 01, Sunday, 2023].

## Log

I was looking for a structured way to learn python and also project based.
I came across Dr.Angela Yu [100 Days of Code: The Complete Python Pro Bootcamp for 2023](https://www.udemy.com/course/100-days-of-code/) which have a mini 
project at the end of each day.

All my projects and training exercises will be separated by day

   - Training folder: [All Exercises](https://github.com/RuiFSP/100-days-of-code/tree/master/Training)
   - Project folder: [All Projects](https://github.com/RuiFSP/100-days-of-code/tree/master/Projects)

My working IDE
   - Pycharm community version from JetBrains: https://www.jetbrains.com/pycharm/

### R1D28

Day28 - Tkinter, Dynamic Typing and the Pomodoro GUI Application
 - [Tkinter](https://docs.python.org/3/library/tkinter.html)
   - [Canvas Widget](https://tcl.tk/man/tcl8.6/TkCmd/canvas.htm) - Create and manipulate 'canvas' hyper graphics drawing surface widgets
   - [Tel commands](https://tcl.tk/man/tcl8.6/TclCmd/contents.htm)
     - [window.after()](https://tcl.tk/man/tcl8.6/TclCmd/after.htm) - execute a command after a time delay
 - Python Strongly Dynamic Typed
   - https://stackoverflow.com/questions/11328920/is-python-strongly-typed
 - Make and executable file for our application
   - pyinstaller: pip install pyinstaller
   - build in everything in one file: 
   ```pyinstaller --onefile -w .\<application name>.py```
     - video: [How to Convert any Python File to .EXE](https://www.youtube.com/watch?v=UZX5kH72Yx4)
 - Install sounds
   - playsound: pip install playsound
   - add you .mp3 or .wav file


The end Project is [Pomodoro Timer](https://github.com/RuiFSP/100-days-of-code/tree/master/Projects/Day28)

   
### R1D27

Day27 - Graphical User Interfaces (GUI) with Tkinter and function Arguments
 - [Tkinter](https://docs.python.org/3/library/tkinter.html)
   - The packer is one of Tk’s geometry-management mechanisms - [Packer](https://docs.python.org/3/library/tkinter.html#the-packer) 
   - Tk Commands [Tk commads](https://tcl.tk/man/tcl8.6/TkCmd/contents.htm)
   - Tk widgets: Labels, Buttons, Entry, Radiobutton, Scale, Checkbutton, Spinbox, Listbox 
   - Tk layout managers: pack(), place() and grid() 
   - Setting Options [Options control](https://docs.python.org/3/library/tkinter.html#setting-options)
     - At object creation time, using keyword arguments
       ```
            fred = Button(self, fg="red", bg="blue")
       ```
     - After object creation, treating the option name like a dictionary index
       ```
          fred["fg"] = "red"
          fred["bg"] = "blue"
       ```
     - Use the config() method to update multiple attrs subsequent to object creation
       ```
          fred.config(fg="red", bg="blue")
       ```
 - Advanced Python Arguments
   - Arguments with default values <b>def my_function(a=1, b=2, c=3)</b>
   - Unlimited Positional Arguments <b>def add(*args)</b>
     - important part is the <b>*args</b>
       - add (1,2)
       - creates a tuple ( 1, 2)
   - Many Keyword Arguments <b> def calculate(**kwargs) </b>
     - important part is the <b>**kwargs</b>
       - calculate(add=3, multiply=5)
       - creates a dict {'add': 3, 'multiply': 5}


The end Project is [Mile Converter](https://github.com/RuiFSP/100-days-of-code/tree/master/Projects/Day27)


### R1D26

Day26 - List and Dictionary Comprehensions
 - Python sequences - list, range, string, tuple
    - list comprehension: <b>[item-expression for item in iterator] or [x for x in iterator]  </b> 
    - conditional list comprehension: <b> [item-expression for item in iterator if conditional]. </b>
    - dictionary comprehension:  <b> {new_key:new_value for item in list} </b>
    - dictionary comprehension: <b> {new_key:new_value for (key,value) in dict.items()} </b>
    - conditional dictionary comprehension: <b> {new_key:new_value for (key,value) in dict.items() if test} </b>
 - Pandas
   - Usefully for dataframes: [DataFrame.iterrows()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iterrows.html)
     - <b>for (index, row) in data_frame.iterrows():</b>


The end Project is [NATO Alphabet](https://github.com/RuiFSP/100-days-of-code/tree/master/Projects/Day26)

### R1D25

Day25 - Working with csv files and analysing Data with Pandas
 - Reading csv files with Python - differences between different methods
   - default python with/open
   - with import csv
   - with pandas
 - Library: [Pandas](https://pandas.pydata.org/) 
   - commonly use to data analysis for its functionality
   - fetching data from a csv
   - grab summary statistics using panda, count, max, min, etc..
   - creating dataframes from a list or dictionary <b>pandas.DataFrame(arg)</b>
   - converting dataframes to csv

The end Project is [USA States Game](https://github.com/RuiFSP/100-days-of-code/tree/master/Projects/Day25)

### R1D24

Day24 - Mail merger example to read, write files
 - refactoring snake game
   - add scoreboard
   - keep track of high_score saved in a file
    - file system: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
      - <b>open(filename, mode)</b> 
 - Understating Relative and Absolute paths
   - Absolute File Path start in root (origin)
     - root folder: windows (c:) or mac (/)
   - Relative File Path
     - related to the working directory

The end Project is [Mail Merger](https://github.com/RuiFSP/100-days-of-code/tree/master/Projects/Day24)

### R1D23

Day23 - Capstone Project - Turtle Crossing
 - Decomposing the problem:
   - Step1: create the screen
   - Step2: create a turtle and move with only keypress "Up"
   - Step3: create n random cars and move them in the same direction
   - Step4: detect collisions between turtle and cars
   - Step5: detect turtle reach finished line 
   - Step6: create scoreboard and increase level difficulty by increasing car speed

The end Project is [Turtle Crossing](https://github.com/RuiFSP/100-days-of-code/tree/master/Projects/Day23)

### R1D22

Day22 - Building the famous game - Pong
 - Decomposing the problem:
   - Step1: create the screen
   - Step2: create and move a paddle
   - Step3: create another paddle
   - Step4: create the ball and make it move
   - Step5: Detect collision with wall and bounce
   - Step6: Detect collision with paddle
   - Step7: Detect when paddle misses
   - Step8: Keep Score

The end Project is [Pong Game](https://github.com/RuiFSP/100-days-of-code/tree/master/Projects/Day22)

### R1D21

Day21 - Finished Snake Game Part-2/2
  - Step4: detect collision with food
  - Step5: create a scoreboard
  - Step6: detect collision with walk
  - Step7: detect collision with tail
  - Inheritance - classes and inheritance from other classes
    - <b>super()</b> inheritance from parent class
  - Slicing list
    - <b>list[start slice : end slice : step]</b>
  - turtle.write() - write text on screen: https://docs.python.org/3/library/turtle.html#turtle.write

The end Project is [Snake - Part 2/2](https://github.com/RuiFSP/100-days-of-code/tree/master/Projects/Day21)

### R1D20

Day20 - Started working on Snake Game Part-1/2
  - Step1: create a snake body
  - Step2: move the snake
  - Step3: control the snake
  - Used time library to handle time related tasks: https://docs.python.org/3/library/time.html
  - Used a combination of Turtle methods tracer() and update() to work with turtle animations

The end Project is [Snake - Part 1/2](https://github.com/RuiFSP/100-days-of-code/tree/master/Projects/Day20)

### R1D19

Day19 - Instances, State and Higher Order functions
  - More on Turtle Graphics: https://docs.python.org/3/library/turtle.html
  - Event Listeners: https://docs.python.org/3/library/turtle.html#turtle.listen
  - Functions as Inputs
    - Higher Order Functions - receives a function as inputs
    - useful to use keyword arguments to be more clear
  - State
  - Multiple Instances - object is and instance of a class
    - Each instance can have different states

The end Project is [Turtle Race](https://github.com/RuiFSP/100-days-of-code/tree/master/Projects/Day19)

### R1D18 

Day 18 - Turtle library and The Graphical User Interface
  - Using Turtle Graphics: https://docs.python.org/3/library/turtle.html
  - Colors RGB values: https://trinket.io/docs/colors
  - Types of imports:
    - basic, for when we do not use it often: import turtle
    - compact, for plenty uses: from turtle import Turtle
    - give alias modules: import turtle as t
    - installing modules: some modules cannot be imported, and we need to install them first
      - library: https://pypi.org/
  - Generating Tuples and RGB Colours - immutable value


The end Project is [The Hirst Painting](https://github.com/RuiFSP/100-days-of-code/tree/master/Projects/Day18)

### R1D17 

Day 17 - OOP - Creating Classes
  - Class names convention is to use PascalCase
  - Trivia data was the data provider: https://opentdb.com/
  - Manipulation JSON files : https://docs.python.org/3/library/json.html
  - Transforming JSON file to a list of dictionaries

The end Project is [The Quiz](https://github.com/RuiFSP/100-days-of-code/tree/master/Projects/Day17)

### R1D16

Day16 - Object-Oriented-Programming
  - Procedural programming (First programming paradigm) - past examples
  - Increased complexity needs a more structured way - OOP (Second programming paradigm)
  - Using Turtle Graphics: https://docs.python.org/3/library/turtle.html
    - default library with python and great to study OOP
  - Python Packages vs Python modules
    - The Python Package Index (PyPI) is a repository of software for the Python programming language
      - python packages: https://pypi.org/

The end Project is [OOP Coffee Machine](https://github.com/RuiFSP/100-days-of-code/tree/master/Projects/Day16)

### R1D15

Day15 - Local Development environment and project coffee machine
  - Setup local environment: Python + Pycharm
  - Pycharm keyboard shortcuts: https://www.jetbrains.com/help/pycharm/mastering-keyboard-shortcuts.html
  - Using Pycharm <b>"# TODO: "</b>  to manage tasks and organize problem-solving steps
  - Setup project requirements
  - Get some emojis: 
    - news emojis: https://emojipedia.org/
    - windows: https://support.microsoft.com/en-gb/windows/windows-keyboard-tips-and-tricks-588e0b72-0fff-6d3f-aeee-6e5116097942
    - mac: https://support.apple.com/en-gb/guide/mac-help/mchlp1560/mac
  - Coffee Machine
    - Control Flow and logical operators
    - Loops
    - Functions with inputs and outputs
    - Dictionaries, Nesting
    - Score of variables

The end Project is [Coffee Machine](https://github.com/RuiFSP/100-days-of-code/tree/master/Projects/Day15)

### R1D14

Day14 - Final project for beginner section
- Steps:
  - Breakdown the problem into smaller ones
  - Make a Todo List for those problems
    - start with the easiest item
    - Turn the problem into comments
    - write code -> run code -> fix code
    - next task

The end Project is [Higher Lower](https://github.com/RuiFSP/100-days-of-code/tree/master/Projects/Day14)

### R1D13

Day13 - Debugging 😀
1) Describe problem (example)
   - what is the for-loop doing ?
   - when is the function meant to print "You got it" ?
   - What are the assumptions about i
2) Reproduce the Bug 😁
   - to fully understand the bug, we should be able to reproduce it
3) Play Computer 😂
   - imagine what the computer will do each time, when we execute the code
4) Fix Errors 😄
   - fix errors highlighted in your editor first
   - run the code, and we get for example a TypeError, because we forgot to convert a str input to int
     - we can also copy the error and search for an answer on the web : google, stackoverflow, chatgpt 🤣
   - we have a print statement and for example we forgot to correct use fstrings(annoying bugs, we do not have any help)
5) Print is your friend 😆
   - make some print statements, to help debug your code. It can be one of your best friends
6) Use a Debugger 😎
   - The BIG Gun for all Devs
     - all IDE's have a debugger
     - we also tried using python tutor for debugger: https://pythontutor.com/
7) Take a break 🌞
   - sometimes is just better to get some fresh air if we are stuck
8) Ask a Friend 🍟
   - A fresh pair of eyes to look at our code or a more experienced developer might help
9) Run your code often 💻
   - Do not wait for end to find out we have lots of bugs 
   - Importance of breaking the problem into smaller chunks and test them
10) Ask Stackoverflow 🐍
    - big community with experienced programmers that can help you tackle the biggest issues
    - https://stackoverflow.com/

Today there was no final project, but took the opportunity to do a smaller project and experiment stuff
   - Had the opportunity to us carriage return <b>"\r"</b>
   - explored a new library for time: https://docs.python.org/3/library/time.html
   - formatted strings: https://docs.python.org/3/tutorial/inputoutput.html#the-string-format-method

The end Project is [Countdown Timer](https://github.com/RuiFSP/100-days-of-code/tree/master/Projects/Day13)

### R1D12

Day12 - Scope
   - Namespaces - local vs global
   - Difference between global scope, local and block scope
   - Block scope such as (for, if , while) does not exist in python, different in language such as java, javascript
     - If you create a variable within a function, it only available inside of that function
     - If you create a variable with a block type, that does not count has local scope
   - Modify variables with global scope, inside functions, we need to explicitly mention them inside function with <b>global variable_name </b>
     - considered bad practice to update global variable inside a function
     - we should use <b>return</b> and save that value as an alternative to use global variables
   - Python Constants and Global Scope
     - This is execution for global scope variables, such as 3.14159 
     - naming convention is to use uppercase and underscore if needed: PI = 3.14159
     - This way is easier to not modify it inside local scope
   - ASCII Art: https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20

The end Project is [Guessing Game](https://github.com/RuiFSP/100-days-of-code/tree/master/Projects/Day12)

### R1D11

Day11 - The Blackjack Capstone Project
   - The project was a recap and practical approach of all the concepts learn in previous days 😀
   - For the record: Blackjack is my favorite casino game, o I had tons of fun with it 😂 

The end Project is [Blackjack](https://github.com/RuiFSP/100-days-of-code/tree/master/Projects/Day11)

### R1D10 

Day10 - Functions with outputs
   - Multiple return values
   - Docstrings '''document something'''
   - Print vs Return
   - While loops, flags and Recursion
   - call a function with a string: https://docs.python.org/3/library/functions.html#globals
     - <b>globals()"myfunction"()</b>

The end Project is [Calculator](https://github.com/RuiFSP/100-days-of-code/tree/master/Projects/Day10)

### R1D9

Day9 - Dictionaries and Nesting
   - Dictionaries -> <b>{Key: Value}</b>
   - Nesting Lists and Dictionaries

The end Project is [Secret Action](https://github.com/RuiFSP/100-days-of-code/tree/master/Projects/Day9)

### R1D8

Day8 - Functions with inputs
   - Example: <b> def my_function(something):</b>
   - Parameter vs Argument
   - Positional Arguments vs Keyword Arguments

The end project is [Caeser Cipher](https://github.com/RuiFSP/100-days-of-code/tree/master/Projects/Day8)

### R1D7

Day7 - Dedicated to revisions of past knowledge with a bigger project
   - Flow Chart Programming: https://app.diagrams.net/
   - For & While loops : https://developers.google.com/edu/python/lists#for-and-in
   - IF/ ELSE, Lists, Strings, Range
   - Modules: https://www.askpython.com/python/python-import-statement
     - from x import y,x
     - import os.system("cls" or "clear") to clear terminal

The end project is [HangMan](https://github.com/RuiFSP/100-days-of-code/tree/master/Projects/Day7)

### R1D6

Day6 - Functions, Code Blocks and While Loops
   - Built-in functions: https://docs.python.org/3/library/functions.html
   - User defined functions: <b>def my functon()</b>:
   - While loops
   - Style guide - PEP8: https://peps.python.org/pep-0008/
   - Python practice and project from: https://reeborg.ca/index_en.html

### R1D5

Day5 - Python Loops, Range and Code Blocks
   - for loop, for loop with range
   - random.shuffle, random.sample, random.choice

The end project is [Password Generator](https://github.com/RuiFSP/100-days-of-code/tree/master/Projects/Day5)

### R1D4

Day4 - Randomization and Python Lists
 - import random (.randInt,.random)
 - list - data structure
   - Python Docs: https://docs.python.org/3/tutorial/datastructures.html
   - IndexErrors - outbound
   - Nested Lists - list[[],[]]

The end project is [Rock Paper Scissors](https://github.com/RuiFSP/100-days-of-code/tree/master/Projects/Day4)

### R1D3

Day3 - Revision about Control Flow and Logical Operators
 - importance of indentation
 - if/else, nested if/else, if/elif /else, multiple if
 - and, or, not 

The end project is [Treasure Island](https://github.com/RuiFSP/100-days-of-code/tree/master/Projects/Day3)

### R1D2

Day2 - Revision about understanding types and how to manipulate strings.

The end project is [Tip Calculator](https://github.com/RuiFSP/100-days-of-code/tree/master/Projects/Day2)

### R1D1

Day1 - Revision about variables and how to manage data.
 - print, inputs

The end project is [Band Name Generator](https://github.com/RuiFSP/100-days-of-code/tree/master/Projects/Day1)





