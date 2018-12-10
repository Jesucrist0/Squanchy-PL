# Basic Concepts

The tutorials for most programming languages start with a hello world program,so

```
print ("hello world")
```

Coming soon:

```
print "hello world"
```

That's it. Just save that as a normal text file with the extension `.sqy` and run it.


## Primitive Types

__Int__  is the same as an int in C. It can hold positive and negative whole numbers. The other two primitive data types are Double and List.

__Double__ is the same as a C Double.

__List__ is the same as a Python or Haskell list.

__Bool__ can only be `1` or `0` like C, so in fact is __Int__. We have keywords `True` and `False`.

__String__ isn't really a primitive data type, it is a __List__ of letters, numbers or other characters of any length, as in Haskell.


## Operators

In general, operators in Squanchy work the same as in any other language. It has all the ones you would expect with sensible order of operations. The following are the only major differences between operators in Squanchy and Python:
* The assignment operator is `:` instead of `=`.
* The equality operator is `=` instead of `==`.
* The are no semicolons.

Samples:

```python
not a and b
+1 -(-1-5/2)*2**2+(10%2)*3
x * 64 = x << 6
```

To sum up:
* Arithmetic Operators: `+ - * / ** %`
* Comparison Operators: `= !=  < > <= >=` 
* Assignment Operators: `:`
* Logical Operators: ` and or not << >>`

Coming soon:
* Membership Operators `in notin`
* Identity Operators: `is notis`
* Assignment Operators: `+= -=`


## Variables

A __variable__ is a place you can store a value, string, list, function (as in javascript) ...types are deduced implicitly. To create, change and use a variable, simply do the following:

```
myVarName: 78
myVarName: "hello"
myList: [1 2 3 4 5.6 "hi!" 23]
myTuple : (a,b,c)
```

Javascript

```javascript
var foo = function(a,b){ return a+b; }
```
Squanchy
```
foo : suma (a,b) -> a+b
```

`myVarName` can be any series of letters, digits and underscores, as long as it doesn't start with a number.


## Lists

Based on Haskell and Python. To construct one you don't need commas !. Elements can be accesed with the `.` operator as __Tuples__. Here is an example:

In Haskell:

```haskell
let numbers = [1,2,3,4]
let truths  = [True, False, False]
let strings = ["here", "are", "some", "strings"]
```

Squanchy:

```
list : [1 2 3 4 5 "hello"]

mylist : [12 45463 1.56 "hello"
		45 35 57]

print: mylist.0
print: mylist.3

```
The output of this will be
```
> 12
> "hello"
```

## Tuples

Based on haskell. To construct one you simple combine several expressions with commas. The names of the elements of a tuple are `1`, `2`, etc. Elements can be accesed with the `.` operator. Here is an example:

From [Haskell](https://en.wikibooks.org/wiki/Haskell/Lists_and_tuples).
> Tuples have a fixed number of elements (immutable); you can't cons to a tuple. Therefore, it makes sense to use tuples when you know in advance how many values are to be stored. For example, we might want a type for storing 2D coordinates of a point. We know exactly how many values we need for each point (two – the x and y coordinates), so tuples are applicable.

> The elements of a tuple do not need to be all of the same type. For instance, in a phonebook application we might want to handle the entries by crunching three values into one: the name, phone number, and the number of times we made calls. In such a case the three values won't have the same type, since the name and the phone number are strings, but contact counter will be a number, so lists wouldn't work.

``` haskell
(True, 1)
("Hello world", False)
(4, 5, "Six", True, 'b')
```

Squanchy 
```
my_Tuple: ("Hello world", False)
my_tuple : (1,"hello",5.6)
print: myTuple.3
print: myTuple.1
```
The output of this will be
```
> 5.6
> 1
```

Tuples within tuples (and other combinations):
```
((2,3), True)
((2,3), [2 3])
```


## !!! Constants (@deprecated)

A __constant__ is a value that is determined at compile time. Constants are created with the constants assignment operator `global`. You can declare constants as follows: `global var_name value ` . Here is an example of a simple use of constants:

```
global a 5
global b 10
global pi 3.141592653589793
global c "hello world"
print (a+b)
print (c)
```
The output of this will be
```
> 15
> "hello world"
```

a,b,c are no longer `Names`, now are `Constants`. Variable pi is now constant 3.141592653589793


## Comments

__coming soon__
Comments are parts of your program that the compiler doesn't look at, so you can write notes and whatnot. In Squanchy, single-line comments start with a `--`. Multi-line comments start with `//` and end with `\\`.


[index](index.md) | [next: Control Flow ->](2_control_flow.md)
