###Tips When Coding
1. Step through the programs with a debugger
   1. A debugger lets you execute programs one line at a time and inspect the state of the program along the way, allowing you to pinpoint where bugs occur
2. Copy the programs manually rather than simply copying and pasting their source code
   1. This helps your "muscle memory" of the programs and forces you to consider each line as you type it


##Part I
###Chapter One
####What is Recursion? 

- A `stack` controls the programs flow of execution 
- A recursive function is a function that calls itself 
  - Functions are mini-programs inside your program  
  - All programming languages implement four features into their functions
    1. Functions have code that is run when the function is called
    2. Arguments (values) that are passed to the function when it's called
    3. Functions return a return value
    4. The program remembers which line of code called the function and returns to it when the function finishes its execution 

####What are Stacks ?
- To Understand recursion you MUST understand stacks
  - A stack is one of the simplest data structures in computer science
  - It stores multiple values like a list does-but unlike lists it limits you to adding to or removing values from the `top` of the stack only 
    - Adding values to a stack is called `pushing` and removing values is called `popping`
    - In `python`, we can `use lists as stack` if, we limit ourselves to the `append()` for `pushing` and `pop` for `removing`
- LIFO Data structure
  - Last In - First Out. Last value pushed in will be the first out to be removed
  
####What Is the Call Stack? 
* Call Stack is a stack of frame objects
  * Frame objects, frames, contain information about a single function call, including which line of code called the function, so the execution can move back there when the function returns 
  * Frame objects are created and pushed onto the stack when a function is called. When teh function returns, that frame object is popped off the stack  
    * If we call a function that calls a function that calls a function, the call stack will have three frame objections on the stack. 
    * When all these functions return, the call stack will have zero frame objects on the stack.





