---
title: Function Fundamentals
abstract: >
   Functions are callable objects that accept input arguments, perform specific operations or tasks, and return results. We create functions as abstractions, and to encapsulate reusable pieces of code, which improves code readability and maintainability. Functions can be recursive (call themselves).
---

# Basic Syntax

Functions are created with the [[def]{.cc} keyword][p-st-def], with a name ([ident]{.stx}ifier), followed by parentheses enclosing an optional argument list ([args]{.stx}), followed by a [block]{.stx}, which constitutes the ‘body’ of the function.

Like [assignment][p-st-assign], [[def]{.cc}][p-st-def] creates a name, and associates that name with the code ‘value’. Multiple names can reference the same function, just like multiple names can store references to the same list, tuple, dictionary, etc.

A function's [block]{.stx} must contain at least one statement, even if it is just a null statement ([[pass]{.cc}][p-st-pass]), or an expression statement, which could a *docstring*.

:::{.lines type="Syntax"}
##### Function Definition{.lines type="Syntax"}

| [[def]{.cc}][p-st-def] [ident]{.stx} [(]{.cc} [ [params]{.stx} ]{.opt} [):]{.cc}
|      ["""]{.cc} [[docstring][p-gl-docstring]]{.stx} ["""]{.cc}
|      [block]{.stx}

| [[def]{.cc}][p-st-def] [ident]{.stx} [(]{.cc} [ [params]{.stx} ]{.opt} [):]{.cc}
|      ["""]{.cc} [[docstring][p-gl-docstring]]{.stx} ["""]{.cc}
|      [block]{.stx}
|      [[return]{.cc}][p-st-return] [ [expr]{.stx} ]

| [[def]{.cc}][p-st-def] [ident]{.stx} [(]{.cc} [ [params]{.stx} ]{.opt} [):]{.cc} [statement]{.stx}

| [[def]{.cc}][p-st-def] [ident]{.stx} [(]{.cc} [ [params]{.stx} ]{.opt} [):]{.cc} [[return]{.cc}][p-st-return] [ [expr]{.stx} ]{.opt}
:::

Unfortunately, Python does not *require* a [docstring][w-docstr], but it should be considered mandatory, and represents good programming practice when present.

Also be sure to notice that the [expr]{.stx} part after [[return]{.cc}][p-st-return] is optional, in which case the function will still immediately return to the caller, but the return value will be [[None]{.cc}][p-lit-none].

[3]{.ws}[[return]{.cc}][p-st-return] [1]{.ws} []{.eqv} [1]{.ws} [[return]{.cc}][p-st-return] [[None]{.cc}][p-lit-none]

###### `py` — Simple functions{.snip}
```{.py}
def func1(): pass                  #← simplest function.

def func2(param):                  #← requires argument.
   print(f"Arg passed: {param}")

def func3():
   return "result"                 #← return ‘result’.

def func4():                       #← with docstring.
   """
   Docstring for func4
   """

func1()                            #← call `func1`.
print(func1())                     #→ None
func2("argument")                  #→ Arg passed: argument
print(f"func3() = {func3()}")      #→ func3() = result
print(func4.__doc__)               #→ Docstring for func4
```

None of these functions do anything ‘useful’, but are all syntactically complete. Note that [func4]{.cc} has one expression statement (the docstring), which means it does not syntactically ‘need’ another statement. 

[p-gl-docstring]:
   https://docs.python.org/3/glossary.html#term-docstring
   "Python Glossary — docstring"
[p-st-def]:
   https://docs.python.org/3/reference/compound_stmts.html#function-definitions
   "Python Reference — Compound Statements # 8.7 Function Definitions"
[p-st-pass]:
   https://docs.python.org/3/reference/simple_stmts.html#the-pass-statement
   "Python Reference — Simple Statements # 7.4 The pass Statement"
[p-st-return]:
   https://docs.python.org/3/reference/simple_stmts.html#the-return-statement
   "Python Reference — Simple Statements # 7.6 The return Statement"
[w-docstr]:
   https://en.wikipedia.org/wiki/Docstring
   "Wikipedia — Docstring"
[p-lit-none]:
   https://docs.python.org/3/library/constants.html#None
   "Python Constants — None"

## Function Documentation

Functions should be documented as suggested by good coding conventions. In Python, this convention involves a [docstring][w-docstr], which is a string literal immediately following the function header. Using triple quotes is another convention.

Docstrings are stored in the [\_\_doc\_\_]{.cc} attribute of modules, classes and functions. Tools like [[pydoc]{.cc}][p-lib-pydoc] and the built-in [[help]{.cc}][p-fn-help] function will read and format the string in [\_\_doc\_\_]{.cc}, which by default is [[None]{.cc}][p-lit-none].

The [[doctest]{.cc}][p-lib-doctest] allows you to write [tests][w-tests] as part of the docstring, in the form of example calls with expected results.

:::{.admon .note}
###### Long Strings as DocStrings
When you use a long string as *docstrings*, Python will remove the first newline if the long string starts with only ["""]{.cc} (or [''']{.cc}) on a line by itself. It will also remove all indentation, up to the level of the starting ["""]{.cc} (or [''']{.cc}). This is a special case, and does not apply to long strings used anywhere else.
:::

#### `py` — Print \_&hairsp;\_doc\_&hairsp;\_ attribute{.snip}
```{.py}
def foo(): "foo Documentation (docstring)"
print(foo.__doc__) ; help(foo)

print(str.__doc__, "\n", len.__doc__)   #← manual way.
help(str) ; help(len)                   #← better way.

import math                             #← for `sin` function.
print(math.sin.__doc__)                 #← manual way.
help(math.sin)                          #← better way.
```

To get documentation for a [module]{.stx} and all its classes and functions, use [[pydoc]{.cc}][p-lib-pydoc]:

[3]{.ws}[python]{.cc} [-m]{.cc} [pydoc]{.cc} [module]{.stx}

On Unix-like operating system, [[pydoc]{.cc}][p-lib-pydoc] will be an executable ‘launcher’:

[3]{.ws}[pydoc]{.cc} [module]{.stx}

It can also display documentation for your own [script]{.stx}[.py]{.cc} files:

[3]{.ws}[python]{.cc} [-m]{.cc} [pydoc]{.cc} [script]{.stx}<br/>
[3]{.ws}[pydoc]{.cc} [script]{.stx}

Note the absence of the [.py]{.cc} extension.

See [Sphinx][sphinx-home] for further conventions on documenting Python code. 

[p-lib-pydoc]:
   https://docs.python.org/3/library/pydoc.html
   "Python Library — pydoc Module"
[p-fn-help]:
   https://docs.python.org/3/library/functions.html?highlight=built%20functions#help
   "Python Reference — Built-In Functions # help()"
[p-lib-doctest]:
   https://docs.python.org/3/library/doctest.html
   "Python Library — doctest — Test Interactive Python Examples"
[w-tests]:
   https://en.wikipedia.org/wiki/Test-driven_development
   "Wikipedia — Test-Driven Development"

## Function Returns

All functions return exactly one *result*. Functions return [[None]{.cc}][p-lit-none] by default. You control return results with ‘[[return]{.cc}][p-st-return] [expr]{.stx}’, though the [expr]{.stx}ession is optional, in which case Python inserts [[None]{.cc}][p-lit-none].

Multiple [[return]{.cc}][p-st-return] statements may appear in a function, as long as you remember that no further code in the function will execute — it is an *execution transfer* statement, just like [[break]{.cc}][p-st-break] and [[continue]{.cc}][p-st-cont].

A function can return an [expr]{.stx}ession of any [type]{.stx}. It can even return different [type]{.stx}s at different times, as long as the caller can ‘handle’ it.

###### `py` — Function returning a result{.snip}
```{.py}
def foo ():
    """
    Function which takes no arguments, but does return a value.
    Not a very exciting result, just ‘that answer’.
    """
    return 42

result = foo()
print(result, end=', '); print(foo())    #→ 42, 42
```

Wherever the function [foo]{.cc} is called, the call expression will *result* in whatever the function [[return]{.cc}][p-st-return]ed. You do not necessarily have to assign its return value to a variable, unless you want to save it for later use.

A function that has multiple [[return]{.cc}][p-st-return] statements is shown below. For variety, it takes an argument, but that is not relevant to the topic. Notice the use of the [[is]{.cc} operator][p-op-is] to test the [[type]{.cc}][p-fn-type] of the argument.

[p-op-is]:
   https://docs.python.org/3/reference/expressions.html#is-not
   "Python Reference — Expressions - Identity comparisons"

###### `py` — Function with multiple return statements{.snip}
```{.py}
def foo (param):
    """
    Function having multiple `return` statements. It has little
    purpose other than to illustrate multiple return statements.
    """
    if type(param) is int  : return "It's an integer!"
    if type(param) is float: return "It's a float!"
    return "Other type"

print("1)", foo(123))   ;  print("2)", foo(param=123))  
print("3)", foo(1.23))  ;  print("4)", foo(param=1.23)) 
print("5)", foo("ABC")) ;  print("6)", foo(param="ABC"))
```
```{.output}
1) It's an integer!
2) It's an integer!
3) It's a float!
4) It's a float!
5) Other type
6) Other type
```

Note that [[else]{.cc}][p-st-if], or [[elif]{.cc}][p-st-if] was not necessary, since [[return]{.cc}][p-st-return] will return immediately. If the [[True]{.cc}][p-lit-true] block of one [[if]{.cc}][p-st-if] was not executed, the next [[if]{.cc}][p-st-if] executes.

[p-st-break]:
   https://docs.python.org/3/reference/simple_stmts.html#the-break-statement
   "Python Reference — 7 Simple Statements # 7.9 Break Statement"
[p-st-cont]:
   https://docs.python.org/3/reference/simple_stmts.html#the-continue-statement
   "Python Reference — 7 Simple Statements # 7.10 Continue Statement"
[p-fn-type]:
   https://docs.python.org/3/library/functions.html#type
   "Python Reference — Built-In Functions # type(‹object›)"
[p-st-if]:
   https://docs.python.org/3/reference/compound_stmts.html#the-if-statement
   "Python Reference — 8 Compound Statements # 8.1 The if Statement"
[p-lit-true]:
   https://docs.python.org/3/library/constants.html#True 
   "Python Literals — True (bool)"

# Parameters

Parameters are special *local* function variables, initialised by passing *arguments*.

Functions can be defined with named parameters. They are, for all intents and purposes, variables, and their scope is local to the function body. Any number of parameters can be defined, but for practical purposes, you should probably restrain yourself.

## Positional / Required Parameters

By default, and unless additional syntax is used, any parameters that have been defined *must* be passed. If a function defines 3 parameters, for example, 3 arguments must be passed — they are *required parameters*. The arguments are assigned to the parameter names in the order they were defined, i.e., *positionally*.

###### `py` — Parameters, with arguments passed positionally{.snip}
```{.py}
def three(a, b, c):
    """
    Function taking 3 mandatory parameters. Arguments can be
    passed positionally, or as keyword arguments. The argument
    values passed, are simply printed out by this function,
    so the types of arguments passed are irrelevant.
    """
    print("a = '{}'".format(a), end="; ")
    print("b = '{}'".format(b), end="; ")
    print("c = '{}'".format(c))

print("1)", end=" ")
three(123, "ABC", 4.56)
print("2)", end=" ") 
three([11, 22, 33], ("AA", 44, 55.66), "XYZ")
```
```{.output}
1) a = '123'; b = 'ABC'; c = '4.56'
2) a = '[11, 22, 33]'; b = '('AA', 44, 55.66)'; c = 'XYZ'
```

When a function is called, the arguments can be *named*. This is referred to as [**keyword arguments**][p-gl-kwargs]. For positional parameters like the [three]{.cc} function above, when *all* arguments are named, it does not matter in which order they appear in the function call.

[p-gl-kwargs]:
   https://docs.python.org/3/glossary.html#term-argument
   "Python Reference — Glossary — arguments"

###### `py` — Passing keyword arguments{.snip}
```{.py}
three(a = 123, b = "ABC", c = 5)  #← spaces around `=` are optional.
three(b="ABC", c=5, a=123)        #← order does not matter.
```
```{.output}
a = '123'; b = 'ABC'; c = 5
a = '123'; b = 'ABC'; c = 5
```

Note that while you can pass the first *n* arguments positionally and the rest by name, the reverse is not true: you cannot pass some arguments by name and then try and pass the remainder positionally.

## Optional / Default Parameters

Python provides syntax for defining parameters with default values. From the caller's perspective, this means that passing arguments for those parameters is optional. However, you can only provide default values for parameters starting from the right of the parameter list, and you cannot skip any. Unless named, arguments can also only be omitted from the right. The following is illegal, because [parm3]{.cc} must also be given a default value, if we insist on [parm2]{.cc} having a default (or we must change the order):

###### `py` — Mixing positional and keyword arguments{.snip}
```{.py}
# This would be illegal:
def foo (parm1, parm2=11, parm3):...
# This would be legal:
def foo (pos1, pos2=11, pos3=22):...
```

An valid example is presented in the next [four]{.cc} function. It can take *up to* 3 arguments. The last two arguments have default arguments and are thus optional. We have more than seven argument passing options. All the calls at the end of the example have the same effect:

###### `py` — Various examples of passing arguments{.snip}
```{.py}
def four (a, b=34, c=56):
    """
    This function requires one mandatory argument for `a`.
    Either an argument for `c` can be omitted, or both `b`
    and `c` arguments may be omitted. Just omitting `b` is
    only possible when using keyword arguments.
    """
    print("a={}, b={}, c={}".format(a, b, c))

four(12); four(12, 34); four(12, 34, 56)   #← all calls have
four(12, c=56); four(c=56, a=12)           #  the same effect.
four(b=34, a=12, c=56)
```

The output for all calls will be: ‘`a=12, b=34, c=56`’.

[sphinx-home]: 
   http://www.sphinx-doc.org/en/stable/index.html
   "Sphinx Home"

## Variable Number of Arguments

A special syntax allows a parameter of a function to be a [[tuple]{.cc}][p-fn-tuple] of values. It does not matter what you pass, it will always be a [[tuple]{.cc}][p-fn-tuple]. This allows callers to call the function with a variable number of arguments. If no arguments are passed, it is effectively an empty [[tuple]{.cc}][p-fn-tuple]. 

###### `py` — Function with variable number of arguments{.snip}
```{.py}
def five (*parms):
    """
    Function can be called with no arguments, or any number
    of arguments. All the arguments will be collected into
    the tuple called `parms` here.
    """
    if parms:
        print("No. of parms:", len(parms))
        for i, v in enumerate(parms):
            print("  parm #{} = '{}'".format(i + 1, v))
    else:
        print("No arguments passed.")

print("1)", end=" ");  five()
print("2)", end=" ");  five(11)
print("3)", end=" ");  five(11, 22)
print("4)", end=" ");  five([11, 22])
print("5)", end=" ");  five([11, 22], (33, 44), "ABC", "DEF")
```
```{.output}
1) No arguments passed.
2) No. of args: 1
   arg #1 = '11'
3) No. of args: 2
   arg #1 = '11'
   arg #2 = '22'
4) No. of args: 1
   arg #1 = '[11, 22]'
5) No. of args: 4
   arg #1 = '[11, 22]'
   arg #2 = '(33, 44)'
   arg #3 = 'ABC'
   arg #4 = 'DEF'
```

The [\*parm]{.cc} parameter will *consume* all arguments. Each argument becomes an item in the tuple. A function can only have one such parameter. If you have additional parameters,  they must either (a) be compulsory and precede the positional parameters, or (b) if optional, be defined last; and can only be passed as keyword arguments *after* the positional arguments. 

###### `py` — Function with variable, and named/optional, parameters{.snip}
```{.py}
def six (*parms, opta=12, optb=None):
   """
   Function can be called with no arguments, or any number
   of arguments. All the arguments will be collected into
   the tuple called `parms` here. Additionally, `opta` and
   /or `optb` can be passed, but only as keyword arguments,
   and only after all positional arguments.
   """
   if parms:
      print(f"No. of `parms`: {len(params)}")
   else
      print("No arguments")
   for i, v in enumerate(parms):
      print(f"   arg #{i + 1} = '{v}'")
   print("   opta =", opta)
   if optb is not None:
      print("   optb =", optb)

print("1)", end=" ");   six()
print("2)", end=" ");   six(12, 34)
print("3)", end=" ");   six(optb=False)
print("4)", end=" ");   six(12, 34, opta=45, optb=56)
```
```{.output}
1) No `args`.
   opta = 12
2) No. of `args`: 2
   arg #1 = '12'
   arg #2 = '34'
   opta = 12
3) No `args`.
   opta = 12
   optb = False
4) No. of `args`: 2
   arg #1 = '12'
   arg #2 = '34'
   opta = 45
   optb = 56
```

For interest's sake, this is how the [[print]{.cc} function][p-fn-print] has been defined (with different parameter names, of course).

[p-fn-tuple]:
   https://docs.python.org/3/library/functions.html#func-tuple
   "Python Reference — Built-In Functions # tuple"
[p-fn-print]:
   https://docs.python.org/3/library/functions.html#print
   "Python Reference — Built-In Functions # print"

## Keyword Dictionary Parameters

Just like **\*parms** provides for a [[tuple]{.cc} type][p-fn-tuple] parameter, it is possible to define a parameter with a leading **\*\***, in which case it will always be a [[dict]{.cc}][p-fn-dict]ionary. This means that the arguments to be collected in such a parameter, *must* be passed as keyword arguments. It can be combined with a **\*parms** list argument, but then it must appear after it.

###### `py` — Function with keyword dictionary parameter{.snip}
```{.py}
call_count = 0

def seven (**kwds):
    """
    Function that takes only keyword arguments. The `kwds`
    parameter is *always* a `dict`ionary. It may be empty,
    which means passing no arguments is acceptable. 
    """
    global call_count
    call_count += 1
    print("seven call #", call_count, '-' * 10, sep='', end='')
    print(f" {len(kwds)} keyword arg(s):")
    for k, v in kwds.items():
        print('   {} = {}'.format(k, v))

print("1)", end=" ");  seven()
print("2)", end=" ");  seven(key='value')

print("3)", end=" ")
seven(k1='val1', k2=222, k3=['ABC', 123], k4={'n':11, 'm':44})
```
```{.output}
1) seven call #1---------- 0 keyword arg(s):
2) seven call #2---------- 1 keyword arg(s):
   key = value
3) seven call #3---------- 4 keyword arg(s):
   k1 = val1
   k2 = 222
   k3 = ['ABC', 123]
   k4 = {'n': 11, 'm': 44}
```

As we mentioned, you can combine a variable number of arguments parameter, with keyword arguments parameter:

###### `py` — Function with variable, and keyword, parameters{.snip}
```{.py}
call_count = 0

def eight (*args, **kwds):
    """
    Function can be called with no arguments, any number of
    arguments, or just keyword arguments, or with any number
    of positional arguments & any number of keyword arguments.
    """
    global call_count
    call_count += 1
    print("eight call #", call_count, '-' * 10, sep='', end='')
    print(" {} keyword arg(s):".format(len(kwds)))
    print("   {}".format(
        "No. of `args`: {}".format(len(args))
        if len(args) else "No `args`."
        ))
    for i, v in enumerate(args):
        print("   arg #{} = '{}'".format(i+1, v))
    for k, v in kwds.items():
        print("   {} = {}".format(k, v))

print("1)", end=" ");  eight()
print("2)", end=" ");  eight(11, 22, 33)
print("3)", end=" ");  eight(44, 55, keya=66, keyb=77)
```
```{.output}
1) eight call #1---------- 0 keyword arg(s):
   No `args`.
2) eight call #2---------- 0 keyword arg(s):
   No. of `args`: 3
   arg #1 = '11'
   arg #2 = '22'
   arg #3 = '33'
3) eight call #3---------- 2 keyword arg(s):
   No. of `args`: 2
   arg #1 = '44'
   arg #2 = '55'
   keya = 66
   keyb = 77
```

[p-fn-dict]:
   https://docs.python.org/3/library/functions.html#func-dict
   "Python Reference — Built-In Functions # dict"

## Argument Operators

Python allows for a single **/** (slash) and a single [\*]{.cc} (asterisk) to be used as parameters. Technically, they are called the ‘slash’ and ‘asterisk’ *operators*. They dictate how the caller of a function is supposed to pass arguments. 

 * A parameter that consists of a single slash, must follow one or more ‘normal’ parameters. This indicates that all parameters *before* the slash, can only be passed *positionally*; never as keyword arguments.

 * A parameter consisting of only an asterisk, must be followed by one or more ‘normal’ parameters. This means that all arguments for parameters *after* the asterisk, can be passed only as *keyword arguments*.

The slash or asterisk parameters, only have an effect on how functions are called, i.e., how *arguments* are passed. Do not confuse this with parameters, or arguments, that *start* with an asterisk (or two), which represent totally different features.

Consider the example below: 

 * As a consequence of the [/]{.cc} operator, [a]{.cc} and [b]{.cc}, can only be passed *positionally*.

 * The [c]{.cc} and [d]{.cc} parameters can be passed as positional arguments, *or* as keyword arguments.

 * The [\*]{.cc} operator dictates that [e]{.cc} and [f]{.cc} can only be passed as *keyword arguments*.

###### `py` — Special parameter operators example{.snip}
```{.py}
def F(a, b, /, c, d, *, e, f):
   print(a, b, c, d, e, f)

print("1)", end=" ");   F(11, 22, 33, 44, e=55, f=66)
print("2)", end=" ");   F(11, 22, c=33, d=44, e=55, f=66)
print("3)", end=" ");   F(11, 22, 33, d=44, e=55, f=66)
print("4)", end=" ");   F(11, 22, e=55, f=66, d=44, c=33)
print("5)", end=" ");   F(11, 22, e=55, f=66, d=44, c=33)
```
```{.output}
1) 11 22 33 44 55 66
2) 11 22 33 44 55 66
3) 11 22 33 44 55 66
4) 11 22 33 44 55 66
5) 11 22 33 44 55 66
```

Trying to pass [a]{.cc} and/or [b]{.cc} as keyword arguments, will result in an error. The following calls all violate one or both of the constraints, and will not run:

###### `py` — Invalid arguments violating argument operators{.snip}
```{.py}
f(a=11, b=22, c=33, d=44, e=55, f=66)
f(a=11, b=22, c=33, d=44, 55, 66)
f(11, 22, 33, 44, 55, 66)
```

This is really rather tricky and specialised, since it ‘fine-tunes’ the *design* of a function. But *users* of a function, have to understand what these operators mean, in order to call the function correctly. The rationale for ‘positional only’ (&hairsp;[/]{.cc}&hairsp;) arguments is documented in [PEP 570][pep570].

[p-fn-list]:
   https://docs.python.org/3/library/stdtypes.html#list
   "Python Reference — Standard Types — list"
[pyd-typ-dict]:
   https://docs.python.org/3/library/functions.html#func-dict
   "Python Reference — Standard Types — dict"
[pep570]:
   https://peps.python.org/pep-0570/
   "PEP 570 — Python Positional-Only Parameters"

# Function Scope

A function ‘body’ is a [block]{.stx}, which is always a *nested scope* within an *outer* scope. Python's [scope][w-scope] implementation is called *lexical scoping*, or *static scoping*, documented under [Naming and Binding][p-exm-naming] and the [tutorial][p-tut-scopes]. Python is not a block-scoped language.

Python implements scope with dictionaries. A reference to a function's ‘local scope’ can be obtained with the built-in [[locals]{.cc}][p-fn-locals] function.

Names created in a nested scope, are only visible in that scope, and in deeper nested scopes. When an [ident]{.stx}ifier is referenced, Python looks for the name starting in the current scope, then looking upwards to the next higher scope, and so on, until it reaches the global scope. If it cannot find it there, it will look in its list of [built-in][p-lib-builtin] names.

We can create ‘local names’ using any of the normal ‘name-creation statements’: [assignment][p-st-assign], [[def]{.cc}][p-st-def], and [[class]{.cc}][p-st-class]. This means we can have local variables, local functions, and local types (classes).

[p-lib-builtin]:
   https://docs.python.org/3/library/builtins.html#module-builtins
   "Python Library — builtins — Build-In Objects"
[p-st-class]:
   https://docs.python.org/3/reference/compound_stmts.html#class-definitions
   "Python Reference — Compound Statements # 8.8 Class Definitions"
[p-st-assign]:
   https://docs.python.org/3/reference/simple_stmts.html#assignment-statements
   "Python Reference — Simple Statements # 7.2 Assignment Statements"
[p-exm-naming]:
   https://docs.python.org/3/reference/executionmodel.html#naming-and-binding
   "Python Reference — Execution Model # 4.2 Naming and Binding"
[p-tut-scopes]:
   https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces
   "Python Tutorial — Classes # Scopes and Namespaces"

## Local Names

Local variable and parameter names ([ident]{.stx}ifiers) share the same ‘namespace’, which means their names are stored in the same dictionary. This dictionary can be accessed using the built-in [[locals]{.cc}][p-fn-locals] function, which returns reference to a ‘snapshot’ of the local namespace. A new local dictionary is created each time the function is called, and it is cleared or ‘goes out of scope’ when the function returns.

###### `py` — Function local dictionary entries{.snip}
```{.py}
def foo (param):
   locvar = "local value"     #← local variable.
   def locfunc(): pass        #← local function.
   class locclass: pass       #← local class.
   for name in locals():      #← print local names.
      print(name, end=' ')
   print()

foo("argument")               #→ param locvar locfunc locclass
```
```{.output}
param locvar locfunc locclass
```

Local classes are not all that common. Local functions, on the other hand, are more numerous and useful.

Identifiers created local to a function, are only visible in that function. The [[locals]{.cc}][p-fn-locals] function is only useful when used *inside* a function. When the [[locals]{.cc}][p-fn-locals] function is used in the global environment, it will be equivalent to a call to the [[globals]{.cc}][p-fn-globals] function. Calling the built-in [[vars]{.cc}][p-fn-vars] function *without* an argument inside a function, will be equivalent to calling [[locals]{.cc}][p-fn-locals] inside the function.

[p-fn-locals]:
   https://docs.python.org/3/library/functions.html#locals
   "Python Reference — Built-In Functions # locals()"
[p-fn-vars]:
   https://docs.python.org/3/library/functions.html#vars
   "Python Reference — Built-In Functions # vars()"
[p-fn-globals]:
   https://docs.python.org/3/library/functions.html#globals
   "Python Reference — Built-In Functions # globals()"

## Local Variables

Local variables are created with the [assignment statement][p-st-assign]. Their [ident]{.stx}ifiers are created in the current [local dictionary](#local-names). They will remain visible to the rest of the statements *inside* the function.

Other than their visibility, local variables behave no different than variables defined in the global scope, or any other scope. They can be re-used to reference other objects, even with different [type]{.stx}s, at any time, within the function.

When the function returns, the local variable names cannot be obtained, and the memory of the objects they reference, will eventually be reclaimed by Python's [garbage collector][w-garbage-collector] (automatic memory manager). But for all practical purposes, the values of local variable are ‘lost’ when the function returns.

## Local Functions

Sometimes called *inner functions*, or *nested functions*, can be useful when we have an algorithm (series of steps or formulas) that is unique to a function. We use them…

 * when we want to abstract complicated behaviour; and/or
 * when we want to to avoid some repetitive code.

You can put some code inside a local function with a descriptive name. That will *abstract* the code with a name, which could make the overall behaviour of the function more readable.

###### `py` — Abstraction of algorithms as local functions{.snip}
```{.py}
def calc_stats(data):

   def mean(nums):
      return sum(nums) / len(nums)

   def variance(nums, mean_val):
      sq_sum = sum((x - mean_val) ** 2 for x in nums)
      return sq_sum / len(nums)

   def std_deviation(variance_val):
      return variance_val ** 0.5

   mean_val = mean(data)
   variance_val = variance(data, mean_val)
   stddev_val = std_deviation(variance_val)

   return {
      'mean': mean_val,
      'var' : variance_val,
      'sdev': stddev_val,
      'sum' : sum(data),
      }

data = [11, 22, 33, 44, 55, 66, 77]
statistics = calc_stats(data)
print(statistics)
```
```{.output}
{'mean': 44.0, 'var': 484.0, 'sdev': 22.0, 'sum': 308}
```

Or, sometimes you may have some code that must be repeated at several points in a function. Simply place that code in a local function, and call it where appropriate.

###### `py` — Local function for repetitive code{.snip}
```{.py}
def process_data(data):

   def do_item(item):         #← nested/inner/local function.
      return item ** 2        #← could be more complex.

   first = do_item(data[0])   #← call `do_item` several
   last = do_item(data[-1])   #  times.

   return first, last

data = [1, 2, 3, 4, 5, 6, 7]
result = process_data(data)
print(result)                 #→ (1, 49)
```

And yes, inner functions have their own local namespaces, which means they can also have local variables, and even have their own local functions. But too many levels of nesting is not encouraged.

[w-garbage-collector]:
   https://en.wikipedia.org/wiki/Garbage_collection_(computer_science)
   "Wikipedia — Garbage Collection (computer science)"

## Global & Outer Names

Functions can reference names at a higher scope. There is a problem though: When code inside a function uses [assignment][p-st-assign], which *creates names*, a new name is created *every time*, even if that name exists in a higher scope. This new name now hides, or *shadows* the higher-scoped name… until the new name goes out of scope (execution leaves the block).

### Global Names

When an ‘outer’ name is in the global scope, we can *reference* it inside any function, even a nested function.

###### `py` — Access global variable in function{.snip}
```{.py}
gvar = 123                    #← define global `gvar`.

def foo():
   print(f"1) gvar = {gvar}") #← reference global `gvar`.

def goo():
   def hoo():
      print(f"2) gvar = {gvar}")
   hoo()

foo()                         #→ 1) gvar = 123
goo()                         #→ 2) gvar = 123
```

If, for some reason, a function wants to *modify* a global variable, the [[global]{.cc}][p-st-global] statement can be used. This informs Python of the global names you want to *modify* with assignment, and to not create a new name locally.

###### `py` — Global statement prevents local name generation{.snip}
```{.py}
gvar = 123                    #← global scope variable.

def foo ():                   #← wants to modify `gvar`.
    global gvar               #← informs Python of intentions.
    gvar = 456                #← does *not* create a name.

def goo():
   def hoo():                 #← nested function that wants
      global gvar             #  to modify `gvar`.
      gvar = 789 
   hoo()

print('1) gvar =', gvar)      #→ 1) gvar = 123
foo()                         #← `foo` modifies `gvar`.
print('2) gvar =', gvar)      #→ 2) gvar = 456
goo()                         #← `hoo` modifies `gvar`.
print('3) gvar =', gvar)      #→ 3) gvar = 789
```

If [gvar]{.cc} did not exist at the time when [foo]{.cc} was called, the ‘**gvar = 456**’ statement would have created the [gvar]{.cc} globally! The first [[print]{.cc}][p-fn-print] above would have failed, but the second [[print]{.cc}][p-fn-print] would still output [456]{.cc}.

### Outer Names

There is one more statement to deal with: the [[nonlocal]{.cc}][p-st-nonlocal] statement. You might be thinking that if a name is not local, it must be global. But that is not necessarily true. Consider an [inner]{.cc} function, nested in an [outer]{.cc} function.

The [outer]{.cc} function defines some [name]{.cc} locally. The [inner]{.cc} function wants to *modify* that [name]{.cc}. But assignment *creates* names in the current scope. We need a way to specify that the [inner]{.cc} function wants to *modify* the [name]{.cc} in the [outer]{.cc} function. And thus the need for the [[nonlocal]{.cc}][p-st-nonlocal] statement.

###### `py` — Non-local referring to ‘outer’ names{.snip}
```{.py}
def outer ():
   name = "value"
   print("1) outer's `name` =", name)
   def inner():
      nonlocal name
      name = name[::-1]            #← modify ‘outer’ name.
   inner()
   print("2) outer's `name` =", name)

outer()
```
```{.output}
1) outer's `name` = value
2) outer's `name` = eulav
```

Note that [[global]{.cc}][p-st-global] would not have worked… ‘**name = name[::-1]**’ would run, but create a new [name]{.cc} in the *global scope*.

And that is how scope works in Python: nested dictionary lookups, which may require special handling using the [[global]{.cc}][p-st-global] and [[nonlocal]{.cc}][p-st-nonlocal] statements.

[p-st-global]:
   https://docs.python.org/3/reference/simple_stmts.html#the-global-statement
   "Python Reference — Simple Statements # 7.12 The global Statement"
[p-st-nonlocal]:
   https://docs.python.org/3/reference/simple_stmts.html#the-nonlocal-statement
   "Python Reference — Simple Statements # 7.13 The nonlocal Statement"

# Function Objects

Functions are ‘[first-class citizens][wp-first-class-func]’, which means that functions can be manipulated as value objects, i.e., they can be associated with a name, passed as arguments, returned from functions, stored in sequences, etc. But we can add *attributes* to function *objects*, which is the new topic.

## Callable Objects

Functions are [[callable]{.cc}][p-fn-callable] [**first-class**][wp-fcf] objects created with the [[def]{.cc}][p-st-def] keyword. Functions defined inside a class are called *methods*.

[wp-fcf]:
   https://en.wikipedia.org/wiki/First-class_function
   "Wikipedia — First-class functions"

Ultimately, a function is an *object* that is [[callable]{.cc}][p-fn-callable]. This ‘callable value’ can be associated with an [ident]{.stx}ifier, which is what [[def]{.cc}][p-st-def] does. It can be stored in sequences, passed as argument, or returned from functions… just like you can do with *any* value of *any* type; in other words: [any]{.cc} [expr]{.stx}ession.

Technically, a callable object will have a [[\_\_call\_\_]{.cc}][p-dm-call] method, which is implicitly called when you call the [object]{.stx} using ‘normal’ syntax. For methods, this means:

[3]{.ws}[object]{.stx}[(]{.cc} [args]{.stx} [)]{.cc} &nbsp;&nbsp; ≡ &nbsp;&nbsp; [object]{.stx}[.\_\_call\_\_(]{.cc} [object]{.stx}[,]{.cc} [args]{.stx} [)]{.cc}

For [built-in][p-fn] and [user-defined][p-st-def] functions, this becomes:

[3]{.ws}[ident]{.stx}[(]{.cc} [args]{.stx} [)]{.cc} &nbsp;&nbsp; ≡ &nbsp;&nbsp; [ident]{.stx}[.\_\_call\_\_(]{.cc}[args]{.stx} [)]{.cc}

[p-fn-callable]:
   https://docs.python.org/3/library/functions.html#callable
   "Python Reference — Built-In Functions # callable()"
[p-dm-call]:
   https://docs.python.org/3/reference/datamodel.html#object.__call__
   "Python Reference — Data Model # ‹obj›.__call__(self, …)"
[p-fn]:
   https://docs.python.org/3/library/functions.html
   "Python Reference — Built-In Functions"

###### `py` — Simple function features{.snip}
```{.py}
def foo (param):                     #← parameter list.
    v = "DEF"                        #← local variable.
    print(f"param={param}, v={v}")
                                     #← implicit `return None`
print(callable(foo))                 #→ True
foo("ABC")                           #← one positional argument.
foo(param="ABC")                     #← keyword argument call.
foo.__call__("ABC")                  #← long way to call `foo`.
```
```{.output}
param=ABC, v=DEF
param=ABC, v=DEF
param=ABC, v=DEF
```

Some functions prohibit passing *keyword arguments*, which is Python's terminology for ‘[named parameters][w-named-parms]’, although we prefer the term ‘named arguments’. For the above [foo]{.cc} function, the three calls are all equivalent.

[w-named-parms]:
   https://en.wikipedia.org/wiki/Named_parameter
   "Wikipedia — Named Parameters"

## Function Dictionaries

A function is ‘special kind of a class’ object; each function has its own attribute dictionary ([\_\_dict\_\_]{.cc}), which is how Python implements [scope][w-scope]. Only functions and classes have scope, unlike language like the C-family where a compound statement block also forms a scope.

Furthermore, you can add attributes to any function object, which will act much like `static` variables in the C-type languages. They are not scoped to the function, and are globally accessible. And unlike local variables, they will remain allocated, even after the function has returned.

###### `py` — Adding attributes to functions{.snip}
```{.py}
def func (param):
   """
   Function with an attribute that remains with the function.
   It will add the attribute itself, if not set by its users.
   """
   if not hasattr(func, 'counter'):
      func.counter = 0
   else:
      func.counter += 1
   print("func({p})... {c}".format(p = param, c = func.counter))
   if hasattr(func, 'other'):
      print("   other attribute =", func.other)
      del func.other

print("1)", end=" ");   func("ABC")
print("2)", end=" ");   func("DEF")
print("3)", end=" ");   func("GHI")

func.other = "Randomly added by code"
func.counter = 100
print("4)", end=" ");   func("JKL")
print("5)", end=" ");   func("MNO")
print("6)", end=" ");   func("PQR")

func.other = "Recreated"
print("7)", end=" ");   func("STU")
print("8) func.counter =", func.counter)
```
```{.output}
1) func(ABC)... 0
2) func(DEF)... 1
3) func(GHI)... 2
4) func(JKL)... 101
   other attribute = Randomly added by code
5) func(MNO)... 102
6) func(PQR)... 103
7) func(STU)... 104
   other attribute = Recreated
8) func.counter = 104
```

This can clearly be abused, so use this feature sparingly.

[w-scope]:
   https://en.wikipedia.org/wiki/Scope_(computer_science)
   "Wikipedia — Scope (computer science)"

## Function Attributes

The objects of many types, can have *attributes*. Depending on the type, these attributes (names) can be created and removed arbitrarily. This is also true for functions. Consider the following code:

###### `py` — Simple function definition with code that attaches an attribute{.snip}
```{.py}
def func(arg):
   print("arg = {}".format(arg))

func(123)                     #→ arg = 123
func.X = 234                  #← make `X` a `func` attribute.

print(getattr(func, 'X'))     #← get value of `X` attribute.
print("func.X =", func.X)

setattr(func, 'X', 345)       #← new value for `X` attribute.
func.X = 345                  #← shorthand for above.

print("func.X =", func.X)              #→ funx.X = 345
print("func.X =", getattr(func, 'X'))  #→ funx.X = 345

del func.X                    #←remove (delete) `X` attribute.
```

There are three built-in functions that can deal with attributes: [[getattr]{.cc}][p-fn-getattr] (get value of attribute, which is what ‘[.]{.cc}’ does), [**`setattr`**][p-fn-setattr] (which is what the equal sign does) and [**`hasattr`**][p-fn-hasattr] (which can check if an attribute exists on an object).

Clearly this should be used with care; we introduce it here simply as a concept that is prevalent in Python, *especially* when we get to classes. But we can start by experimenting with attributes on functions.

A function's code can use its own attributes. Below we wrote an ‘enhanced’ [func]{.cc} that checks if it has an [X]{.cc} attribute, and then also prints that out:

###### `py` — Function that uses its own attribute{.snip}
```{.py}
def func(arg):
   print(f"arg = {arg}")
   if hasattr(func, "X"):
      print("func.X =", func.X)

func(123)                     #→ arg = 123
func.X = 234                  #← create `X` as `func` attrib.

func("ABC")                   #→ arg = ABC \n func.X = 234
```

We could make the function delete the [X]{.cc} attribute after printing or using the value it references.

A good use for function attributes could be a cache for previous results, so that in expensive (slow) functions, we do not have to recalculate results if already cached. This technique is called [memoization][w-memoize].

###### `py` — Memoize results in expensive function{.snip}
```{.py}
def slow_func(x):
   if not hasattr(slow_func, "cache"):
      slow_func.cache = {}
   if x not in slow_func.cache:
     slow_func.cache[x] = x ** 2   #← ‘slow’ code.
   return slow_func.cache[x]

print(slow_func(5))                #→ 25
print(slow_func.cache)             #→ {5: 25}
```

Another use might be to keep track of number of calls to a function and the cumulative time it took to perform the actions in the function. It could be made re-usable as a decorator, as we have done with [track_stats]{.cc} below:

###### `py` — Function timer attribute{.snip}
```{.py}
import time

def track_stats(f):

   def wrapper(*args, **kwargs):
      start = time.perf_counter()
      result = f(*args, **kwargs)
      stop = time.perf_counter()
      wrapper.calls += 1
      wrapper.times += stop - start
      return result

   wrapper.calls = 0
   wrapper.times = 0
   return wrapper

@track_stats
def square(x):
    return x ** x

for i in range(500):
    print(square(i))

print(square.calls)           #→ 500
print(square.times * 1000)    #→ ‹time› in ms.
```

The [track_stats]{.cc} function can be applied as decorator to any function.

[p-fn-getattr]:
   https://docs.python.org/3/library/functions.html#getattr
   "Python Reference — Built-in Functions — getattr()"
[p-fn-setattr]:
   https://docs.python.org/3/library/functions.html#setattr
   "Python Reference — Built-in Functions — setattr()"
[p-fn-hasattr]:
   https://docs.python.org/3/library/functions.html#hasattr
   "Python Reference — Built-in Functions — setattr()"


## Function Factories

Functions that return functions, are often called function *factories* — this is not a syntax, just a common phrases meaning ‘functions that return other functions’. It is immaterial whether the function returned, is a global function, or a local function.

###### `py` — Function returning function objects{.snip}
```{.py}
import random
def FuncFactory ():
   """
   Randomly return one of three possible local functions.
   """
   def F1 ():
      print("F1() called.", end=" "); return 111
   def F2 ():
      print("F2() called.", end=" "); return 222
   def F3 ():
      print("F3() called.", end=" "); return 333

   return random.choice([F1, F2, F3])

## call `FuncFactory` 10 times, and call the function it returns
for i in range(10):
   f = FuncFactory()
   print("f() returned: {}".format(f()))
```
```{.output}
F2() called. f() returned: 222
F2() called. f() returned: 222
F3() called. f() returned: 333
F3() called. f() returned: 333
F1() called. f() returned: 111
F3() called. f() returned: 333
F3() called. f() returned: 333
F1() called. f() returned: 111
F1() called. f() returned: 111
F1() called. f() returned: 111
```

It might not seem useful, and the example above does not prove that it can be a useful technique, because we are focussed firstly on the fact that we *can* return functions.

## Passing Functions

Similarly, we could pass functions as arguments. When a function is passed as argument, it is often abstractly called a *callback* function, or a *plugin* function. The following example may not be useful in a practical sense, but does show that you *can* pass functions.

###### `py` — Function with callable parameter{.snip}
```{.py}
def TakeFunc (parm):
   """
   Function expecting to be passed a function as `parm`. It will
   simply call the function passed.
   """
   print('TakeFunc() calling `parm`... ', end='')
   parm()

def F ():
   print('F() called.');  return 11

def G ():
   print('G() called.');  return 22

def H ():
   print('H() called.');  return 33

print("1)", end=" ");  TakeFunc(G)
print("2)", end=" ");  TakeFunc(F)
print("3)", end=" ");  TakeFunc(H)
```
```{.output}
1) TakeFunc() calling `parm`... G() called.
2) TakeFunc() calling `parm`... F() called.
3) TakeFunc() calling `parm`... H() called.
```

The following example simply defines three functions, and then creates a ‘list of functions’, by arbitrarily adding them as items in a list. Then it iterates through the list, calling each function in turn.

###### `py` — Playing with functions as values{.snip}
```{.py}
def f (): print("f() called")
def g (): print("g() called")
def h (): print("h() called")

lof = [f, g, h, g, f, f]

lof[0]()
for x in lof: x()
```
```{.output}
f() called
f() called   g() called   h() called
g() called   f() called   f() called
```

Passing functions is so useful, that several functions in the Python standard library accepts functions as arguments (sometimes they are optional). Common and very useful examples are, the [[map]{.cc} function][p-fn-map], and the [[filter]{.cc} function][p-fn-filter].

###### `py` — Passing functions to `map()` and `filter()` example{.snip}
```{.py}
def twice (x): return x * 2
def odd (x):   return x % 2 != 0

data = [1, 2, 3, 4]
result = list(map(twice, data))     #←“map `twice` onto `data`” &
print("1)", result)                 # convert to a `list`.

result = list(filter(odd, data))    #←“filter on odd values” &
print("2)", result)                 # convert to a `list`.
```
```{.output}
1) [2, 4, 6, 8]
2) [1, 3]
```

Note that both [[filter]{.cc}][p-fn-filter] and [[map]{.cc}][p-fn-filter] return *iterators*, and not a complete [[list]{.cc}][p-fn-list] or [[tuple]{.cc}][p-fn-tuple]. They must be used in an *iterable* context to actually perform the iterations.

Here is an trivial example of a user-defined function similar in operation to built-in functions like [[map]{.cc}][p-fn-map] and [[filter]{.cc}][p-fn-filter], in that it also takes a function as argument:

###### `py` — Function taking ‘plugin function’ as argument{.snip}
```{.py}
ef dostuff (extra_stuff = None):
   print("dostuff() doing stuff...", end='')
   if extra_stuff:
      extra_stuff()
   else:
      print("nothing extra to do")

print("1)", end=" ");   dostuff()    #←just do ‘normal’ stuff.

def more_work():
   print("more_work() doing more work")

def other_work():
   print("orther_work() doing more work")

print("2)", end=" ");   dostuff(extra_stuff = more_work)
print("3)", end=" ");   dostuff(more_work)
print("4)", end=" ");   dostuff(extra_stuff = other_work)
```
```{.output}
1) dostuff() doing stuff...nothing extra to do
2) dostuff() doing stuff...more_work() doing more work
3) dostuff() doing stuff...more_work() doing more work
4) dostuff() doing stuff...orther_work() doing more work
```

:::{.admon .warning}
###### Global reduce()/apply() Functions in Python3
In Python3, the original built-in [reduce]{.cc} and [apply]{.cc} functions have been removed. If you require similar behaviour, use [[functools.reduce]{.cc}][p-ft-reduce]. The closes equivalent for [apply]{.cc}, can be found in the [[multiprocessing]{.cc}][p-lib-multiproc] module. Unfortunately, you will still see many references to, and examples of, the old [reduce]{.cc} and [apply]{.cc} functions. You should translate that to Python3 manually.
:::

Here is a simple example using [[functools.reduce]{.cc}][p-ft-reduce] to sum a sequence of values. For interest, we also passed a [[lambda]{.cc}][p-ex-lambda] expression to the function.

###### `py` — Example use of functools.reduce{.snip}
```{.py}
from functools import reduce

def add (a, b): return a + b

values = [11, 22, 33]
answer = reduce(add, values);                 #← custom func.
print(f"1) Sum = {answer}")
answer = reduce(lambda a, b: a + b, values);  #← pass a lambda.
print(f"2) Sum = {answer}")
```
```{.output}
1) Sum = 66
2) Sum = 66
```

[wp-first-class-func]:
   https://en.m.wikipedia.org/wiki/First-class_function
   "Wikipedia — First-class function"
[p-ft-reduce]:
   https://docs.python.org/3.0/library/functools.html#functools.reduce
   "Python Reference — functools.reduce()"
[p-lib-multiproc]:
   https://docs.python.org/3/library/multiprocessing.html?highlight=multiprocessing
   "Python Library — multiprocessing Module"

## Function Factories

Functions that return inner functions are often called *function factories*. Closures are very common in creating *specialised* functions, where the ‘outer’ function (the function factory), is passed one or more arguments, which are referenced in the ‘inner’ function's body, forming a closure.

By passing different arguments to such a factory function, it can logically generate different functions.

###### `py` — Multiplication factory function{.snip}
```{.py}
def multiply_factory (multiplier):
   def multiply_worker (multiplicant):
      return multiplicant * multiplier
   return multiply_worker

times_two = multiply_factory(2)
answer = times_two(3);     print(answer)    #→ 6
answer = times_two(9);     print(answer)    #→ 18

times_2p5 = multiply_factory(2.5)
answer = times_2p5(3);     print(answer)    #→ 7.5
answer = times_2p5(33);    print(answer)    #→ 82.5
```

The [multiply_factory]{.cc} function thus returns ‘worker’ functions that can multiply any argument by the [multiplier]{.cc} passed during the factory call. They are effectively custom functions that, once defined, will always to the same job, but not necessarily the same job as their ‘co-workers’.


# Argument Unpacking

Sometimes we have values in [[list]{.cc}][p-fn-list]s or [[dict]{.cc}][p-fn-dict]ionaries, where we want to pass their *items* as arguments to functions. Python provides a special syntax for *list argument unpacking* and *dictionary argument unpacking*.

## List Argument Unpacking

Assume you have a function called [func]{.cc} that takes three arguments, or one that takes an arbitrary number of arguments like [[five]{.cc}](#py-function-with-variable-number-of-arguments) above. And further assume you have a list of values like this:

###### `py` — Arbitrary list of three values{.snip}
```{.py}
lst = [11, 22, 33]
```

Now you want to pass those values as positional arguments. One way to do this is as follows: 

###### `py` — Passing list items individually to a function{.snip}
```{.py}
five(lst[0], lst[1], lst[2])
```
```{.output}
No. of args: 3
   arg #1 = '11'
   arg #2 = '22'
   arg #3 = '33'
```

Python offers an alternative called *list argument unpacking* in the form: **\*lst**, where [lst]{.cc} must be a [[list]{.cc}][p-fn-list] or [[tuple]{.cc}][p-fn-tuple]. This syntax can be used when passing arguments to a function that can take a variable number of arguments, or one that takes exactly that number of positional arguments produced by the unpacking.

###### `py` — Unpacking a list as individual arguments #1{.snip}
```{.py}
five(*lst)
```
```{.output}
No. of args: 3
   arg #1 = '11'
   arg #2 = '22'
   arg #3 = '33'
```

The [[four]{.cc}](#py-various-examples-of-passing-arguments) function above can take 3 arguments. Let us see how this works out:

###### `py` — Unpacking a list as individual arguments #2{.snip}
```{.py}
four(*lst)
```
```{.output}
a = '11'; b = '22'; c = '22'
```

List argument unpacking has no relationship with regard to how the parameters of a function were defined, as long as the unpacking matches the function's expectations.

### Dictionary Argument Unpacking

By the same token, assume you have a function like [[seven]{.cc}](#py-function-with-keyword-dictionary-parameter) above, which is defined to take a *dictionary parameter*. And assume you have a dictionary like [D]{.cc} below:

###### `py` — Simplistic dictionary for following examples{.snip}
```{.py}
D = {'keya':'value A', 'keyb':123}
```

We can call [[seven]{.cc}](#py-function-with-keyword-dictionary-parameter) by manually ‘unpacking’ the keyword arguments, which is again not a very robust approach. The Python alternative is *dictionary argument unpacking*, using the ‘__\*\*__[dict]{.stx}’ syntax, where [dict]{.stx} must be a [[dict]{.cc}][p-fn-dict]ionary:

###### `py` — Unpacking dictionary as individual keyword arguments{.snip}
```{.py}
print("1)", end=" ")
seven(keya=D['keya'], keyb=D['keyb']) #← manual ‘unpacking’
print("2)", end=" ")
seven(**D)                 #← dictionary argument. unpacking.
```
```{.output}
1) seven call #1---------- 2 keyword arg(s):
   keya = value A
   keyb = 123
2) seven call #2---------- 2 keyword arg(s):
   keya = value A
   keyb = 123
```

We should thus be able to call [[eight]{.cc}](#py-function-with-variable-and-keyword-parameters), which accepts both a variable number of arguments, and some keyword arguments. Yes we can, and just for fun, we also show you what it would look like if you had to manually *unpack* the `L` and `D` values:

###### `py` — Unpacking a list and a dictionary as arguments{.snip}
```{.py}
print("1)", end=" ")
eight(*lst, **dic)                   #← ‘pythonic’

print("2)", end=" ")
eight(lst[0], lst[1], lst[2], **dic) #← ‘mixed’ unpacking.

print("3)", end=" ")
eight(                               #← ‘manual’ unpacking...
   lst[0], lst[1], lst[2],
   keya=dic['keya'], keyb=dic['keyb']
   )
```
```{.output}
1) eight call #1---------- 2 keyword arg(s):
   No. of `args`: 3
   arg #1 = '11'
   arg #2 = '22'
   arg #3 = '33'
   keya = value A
   keyb = 123
2) eight call #2---------- 2 keyword arg(s):
   No. of `args`: 3
   arg #1 = '11'
   arg #2 = '22'
   arg #3 = '33'
   keya = value A
   keyb = 123
3) eight call #3---------- 2 keyword arg(s):
   No. of `args`: 3
   arg #1 = '11'
   arg #2 = '22'
   arg #3 = '33'
   keya = value A
   keyb = 123
```

If you have wondered before about the point of learning all the extra tedious syntax, you may now be convinced that you would not *want* to live without this unpacking functionality.

# Lambdas

The term [[lambda]{.cc}][p-ex-lambda] is a more formal term for ‘[anonymous function][w-anon-func] expression’.

The [[lambda]{.cc}][p-ex-lambda] keyword can be used to represent a function without a name (anonymous). Since a function is a value, the whole [[lambda]{.cc}][p-fn-lambda] expression is a value. It can therefore be [[return]{.cc}][p-st-return]ed from a function, passed to a function, or stored elsewhere. The basic syntax is as follows:

#### **Syntax** — *Lambda Expressions*
[3]{.ws}**lambda** [ [parm-list]{.stx} ] **:** [expr]{.stx}

The [parm-list]{.stx} does not have to be enclosed in parentheses. The [expr]{.stx}ession automatically results in: ‘[[return]{.cc}][p-st-return] [expr]{.stx}’. There can only be one expression, so lambdas are convenient only for simple functionality. Anywhere you can use a [[lambda]{.cc}][p-ex-lambda], you can use a function name instead. 

###### `py` — Functions and lambdas in various combinations{.snip}
```{.py}
def taker (f):
   """
   Function taking a callable as parameter. Can be a lambda
   """
   return f(4)                       #← call what was passed,
                                     #  and return its result.

def giver ():
    """
    Function returning a function... a `lambda` to be exact.
    """
    return lambda : "Yippeee!"       #← lambda with no params.

sheep = lambda x : x * x * x         #← `sheep` references code.
print("1)", sheep(2))                #← call what it references.
print("2)", taker(sheep))            #← pass value in `sheep`.
print("3)", taker(lambda x : x*x*x)) #← pass lambda directly.
sheep = giver()                      #← store `giver` result.
print("4)", sheep())                 #← call `sheep` & print.
print("5)", giver()())               #← call return value.
```
```{.output}
1) 8
2) 64
3) 64
4) Yippeee!
5) Yippeee!
```

Note that we could have passed [taker]{.cc} any name, as long as the name referenced a value, with type [function]{.cc}, or more generically: anything which is callable by the function call operator, including an [anonymous function][w-anon-func] expression ([[lambda]{.cc}][p-ex-lambda]).

[p-ex-lambda]:
   https://docs.python.org/3/reference/expressions.html?highlight=lambda#lambda
   "Python Reference — Expressions # 6.14 Lambdas"
[w-anon-func]:
   https://en.wikipedia.org/wiki/Anonymous_function
   "Wikipedia — Anonymous Functions"

# Closures

A [closure][w-closure] involves the fact that [[def]{.cc}][p-st-def] is like [assignment][p-st-assign]: it creates a name, and assigns a value. You can create a function name within a function; called a *nested function*, *inner function*, *local function*, or a ‘function within a function’. Inner functions can only be called or returned from within the *outer* function.

When the *inner* function references names of variables or parameters of the *outer* function, Python (and other languages) call this a [closure][w-closure], which means it must *capture* the referenced variables of the *outer* function somehow. The closure ‘remembers’ the context in which it was created.

[w-closure]:
   https://en.wikipedia.org/wiki/Closure_(computer_programming)
   "Wikipedia — Closure (Computer Programmin)"

###### `py` — Capturing ‘outer’ variables = closure{.snip}
```{.py}
def outer(outer_param):
    outer_var = 2
    def inner (x):
        return x * outer_var * outer_param
    return inner

f = outer(3)
print("f(4) =", f(4))
print("outer(3)(4) =", outer(3)(4))
```
```{.output}
f(4) = 24
outer(3)(4) = 24
```

If [inner]{.cc} did not reference any [outer]{.cc} names, it would not be a closure. This [inner]{.cc} function referenced two names of the [outer]{.cc} function, but that does not make it any more, or any less of a closure. There is no *degree* of closure.

# Recursion

Python supports [recursion][w-recursion], which means a function can call itself. Any recursive algorithm can be written iteratively (with loops) instead, making recursion optional. Nevertheless, some algorithms lends itself more ‘elegantly’ to a recursive solution.

Fundamentally though, recursion is just another way to *iterate* (loop).

###### `py` — Recursion as iteration{.snip}
```{.py}
def looper1 (n):
   print("looper1: Recurse #{}".format(n))
   if n > 0:
      looper1 (n - 1)

def looper2 (n):
   if n > 0:
      looper2 (n - 1)
   print("looper2: Recurse #{}".format(n))

looper1(5)
looper2(5)
```

The interesting effect of the [[print]{.cc}][p-fn-print] function call in [looper2]{.cc}, is that the ‘work’ of the function, takes place in *reverse*, which makes recursion a technique to change the order in which actions take place.

[w-recursion]:
   https://en.wikipedia.org/wiki/Recursion_(computer_science)
   "Wikipedia — Recursion (computer science)"

# Generator Functions

The [[yield]{.cc} statement][p-st-yield] turns a function into a [generator][p-gl-generator], meaning it returns an [iterator][p-tp-iterator]. Thus, *generator function* is a term to describe a function which contains one or more [[yield]{.cc}][p-st-yield] statements.

The syntax is similar to [[return]{.cc}][p-st-return], and in fact, [[yield]{.cc}][p-st-yield] *does* return an [expr]{.stx}ession to the caller. The key difference is that [[yield]{.cc}][p-st-yield] saves the state of the function, so that when it is called again, the complete state is restored, and execution continues with the *next* statement following the [[yield]{.cc}][p-st-yield] statement.

[p-st-yield]:
   https://docs.python.org/3/reference/simple_stmts.html#grammar-token-yield-stmt
   "Python Reference — Simple Statements - yield Statement"
[p-tp-iterator]:
   https://docs.python.org/3/library/stdtypes.html#iterator-types
   "Python Reference — Standard Types # Iterator Types"


##### `genfuncs.py` — Simple Generator Functions{.file}
```{.py}
def simpgen():
    """Simplest, semi-useful generator function."""
    yield 1; yield 4; yield 9; yield 16

def loopgen():
    """Generator function using a loop to `yield`."""
    for i in range(1,5):
        yield i**2

for i in simpgen(): print("i =", i, end="  ")
print()
for i in loopgen(): print("i =", i, end="  ")
print()

print(list(loopgen()))

L = list(simpgen());
T = tuple(loopgen());
D = dict(zip(range(1,5), loopgen()))

print(L, T, D, sep='\n')
```
```{.output}
i = 1  i = 4  i = 9  i = 16 
i = 1  i = 4  i = 9  i = 16 
[1, 4, 9, 16]
[1, 4, 9, 16]
(1, 4, 9, 16)
{1: 1, 2: 4, 3: 9, 4: 16}
```

Both functions above are generator functions. They both run 4 [[yield]{.cc}][p-st-yield] statements. They both return the same values. They can both be used as iterators. They can be more efficient than comprehensions, since they generate their sequences one-by-one as needed, whereas a comprehension, or a slice, will create all the numbers at once. The built-in [[range]{.cc}][p-fn-range] function is an example of a generator function.

###### `py` — Generator for reading large files{.snip}
```{.py}
def read_large_file(filepath):
   with open(filepath, 'r') as file:
      for line in file:
         yield line

file_path = 'large_file.txt'          #← replace name.

for line in read_large_file(file_path):
    print(line.strip())
```

The iterator returned by calling a generator function, or [[iter]{.cc}][p-fn-iter][(]{.cc}[sequence]{.stx}[)]{.cc}, can be passed to the built-in [[next]{.cc}][p-fn-next] function to return each item in the logical sequence. It calls the [\_\_next\_\_]{.cc} method present in all iterators.

Iteration is terminated when [[next]{.cc}][p-fn-next] raises a [StopIteration]{.cc} exception. We can simulate what a [[for]{.cc}][p-st-for] statement does:

###### `py` — Simulating a for loop{.snip}
```{.py}
SEQ = [ 11, 22, 33, 44, 55 ]

for item in SEQ:                    #←calls `iter` and `next`.
   print(f"{item } ", end="")
print()

it = iter(SEQ)                      #←manually call `iter`.
while True:
   try:
      print(f"{next(it)}", end=" ") #←manually call `next`.
   except StopIteration:
      break
print()
```
```{.output}
11 22 33 44 55
11 22 33 44 55
```

Here is another example using a generator to calculate [fibonacci numbers][w-fibonacci] given a [first]{.cc} and [last]{.cc} arguments. For example, if [first]{.cc} is [3]{.cc}, it means the 3rd number in the sequence, and a [last]{.cc} value of [10]{.cc}, would mean the 10th number in the sequence. For good measure, we use also use a nested function: [nth_fibonacci]{.cc} using [Binet's formula][w-fibo-binet].

###### `py` — Fibonacci sequence with a generator{.snip}
```{.py}
import math

SQ5 = math.sqrt(5)
PHI = (1 + SQ5) / 2.0
PSI = (1 - SQ5) / 2.0

def fibonacci(start, stop):

   def nth_fibonacci(n):
      return round((PHI ** n - PSI ** n) / SQ5)

   a, b = nth_fibonacci(start), nth_fibonacci(start + 1)

   for _ in range(stop - start):
      yield a
      a, b = b, a + b

for number in fibonacci(3, 10):
    print(number)
```

Note that the number represented by the [stop]{.cc} is not included, much like [[range]{.cc}][p-fn-range]. The algorithm is relatively efficient, but a more complex recursive solution using [memoization][w-memoize] might be more performant at the expense of using more memory.

[p-fn-map]:
   https://docs.python.org/3/library/functions.html#map
   "Python Reference — Built-in Functions - map()"
[p-fn-filter]:
   https://docs.python.org/3/library/functions.html#filter
   "Python Reference — Built-in Functions - filter()"
[p-fn-range]:
   https://docs.python.org/3/library/functions.html#func-range
   "Python Reference — Built-In Functions — range()"
[p-fn-iter]:
   https://docs.python.org/3/library/functions.html#iter
   "Python Reference — Built-In Functions — iter()"
[p-fn-next]:
   https://docs.python.org/3/library/functions.html#next
   "Python Reference — Built-In Functions — next()"
[p-st-for]:
   https://docs.python.org/3/reference/compound_stmts.html#the-for-statement
   "Python Reference — Compound Statements # 8.3 The for Statement"
[w-fibonacci]:
   https://en.wikipedia.org/wiki/Fibonacci_sequence
   "Wikipedia — Fibonacci Sequence"
[w-fibo-binet]:
   https://en.wikipedia.org/wiki/Fibonacci_sequence#Relation_to_the_golden_ratio
   "Wikipedia — Fibonacci Sequence # Relationship to Golden Ratio"
[w-memoize]:
   https://en.wikipedia.org/wiki/Memoization
   "Wikipedia — Memoization"

<!--TODO: this needs work:

###### `py` — Recursive Fibonacci with memoization{.snip}
```{.py}
import math

SQ5 = math.sqrt(5)
PHI = (1 + SQ5) / 2.0
PSI = (1 - SQ5) / 2.0

def memoize(f):
   cache = {}

   def memoized_function(*args):
      if args not in cache:
         cache[args] = f(*args)
      return cache[args]

   return memoized_function

def nth_fibonacci(n):
   return round((PHI ** n - PSI ** n) / SQ5) 

@memoize
def fibonacci_recurse(n):
   if n <= 1:
      return n
   return fibonacci_recurse(n - 1) + fibonacci_recurse(n - 2)

def fibonacci(start, stop):
   for n in range(nth_fibonacci(start), nth_fibonacci(stop) + 1):
      yield fibonacci_recurse(n)

fibonacci_seq = fibonacci(3, 5)

for number in fibonacci_seq:
   print(number)
```

The above solutions uses recursion, memoization and a decorator (**@memoize**).
-->

# Function Decorators

Functions are [first-class][w-first-class] values, which means they can be passed as arguments, returned from functions, assigned to a variable, or stored as an item in a data structure like a [[list]{.cc}][p-fn-list], [[tuple]{.cc}][p-fn-tuple], [[dict]{.cc}][p-fn-dict]ionary, or custom classes.

A particular use-case for this feature, is a pattern called [decorators][w-decorator], which has a special and convenient (but optional) syntax in Python. This pattern involves an ‘decorator’ function, that is passed a function object to ‘decorate’. This ‘decorator’ function will generally perform tasks before and/or after calling the passed function.

###### `py` — Simple decorator function{.snip}
```{.py}
def decorate(func):
   def inner():
      print("decorator work before")
      result = func()
      print("decorator work after")
      return result
   return inner

def some_func():
   print("some_func called")
   return 123

decorated = decorate(some_func)     #← returns `inner`.
r = decorated()                     #← calls `inner`.
print(f"result = {r}")              #→ result = 123
some_func = decorate(some_func)
r = some_func()                     #← calls `inner`.
print(f"result = {r}")              #→ result = 123
```

After the statement: **some\_func = decorate(some\_func)**, the *name* [some_func]{.cc} is given a new value to reference: the return from [decorate]{.cc}, which is [inner]{.cc}. Its original code is not directly referenced any more — it became ‘decorated’.

In practice, the design of decorator functions will follow a pattern that allows it to be used to decorate any function, regardless of arguments required by the function to be decorated, making it more generic.

###### `py` — More generic decorator pattern{.snip}
```{.py}
def decorator(func):
   def inner(*args, **kwds):
      print("<decoration>", end=" ")
      return func(*args, **kwds)
   return inner

def func1(): print("func1()")
def func2(a, b): print(f"func2({a}, {b})")
def func3(*args): print(f"func2{args}")

def line(n): print(f"({n}) ", end="")

line(1) ; decorator(func1)()
line(2) ; decorator(func2)(12, 34)
line(3) ; decorator(func3)("ABC", 12.34, 567)

func1 = decorator(func1)       #← decorate names.
func2 = decorator(func2)       # 
func3 = decorator(func3)       # 

line(4) ; func1()
line(5) ; func2(12, 34)
line(6) ; func3("ABC", 12.34, 567)
```
```{.output}
(1) <decoration> func1()
(2) <decoration> func2(12, 34)
(3) <decoration> func2('ABC', 12.34, 567)
(4) <decoration> func1()
(5) <decoration> func2(12, 34)
(6) <decoration> func2('ABC', 12.34, 567)
```

As you can see, the [decorator]{.cc} function can ‘decorate’ any function, regardless of the type and number of arguments passed to the function to be decorated.

Sometimes, we want to pass an additional argument to the [decorator]{.cc} function. This will require a twice-nested [inner]{.cc} function.

###### `py` — Decorator with an argument{.snip}
```{.py}
def repeater(count):
   def decorator(func):
      def inner(*args, **kwds):
         for _ in range(count):
            func(*args, **kwds)
         print()
      return inner
   return decorator

def hello(): print("Hello", end=" ")

repeater(3)(hello)()
hello = repeater(3)(hello)       #← decorate `hello`.
hello()                          #← now decorated.
```

Which brings us to Python decorator *syntax*, which simplifies the decoration, but can only be applied while *defining* the function to be decorated. Its [ident]{.stx}ifier will be given the ‘decoration’ code, just like:

[3]{.ws}[ident]{.stx} **=** [decorator]{.stx}[(]{.cc}[ident]{.stx}[)]{.cc}

The above pattern can only be applied *after* the function has been defined, while the short hand decorator syntax comes *before* the definition:

[3]{.ws}[@]{.cc}[decorator]{.stx}\
[3]{.ws}[def]{.cc} [ident]{.stx}[(]{.cc} [args]{.stx} [):]{.cc}\
[3]{.ws}[3]{.ws}···

Functions can be decorated multiple times, even with the same decorator:

[3]{.ws}[@]{.cc}[decorator₁]{.stx}\
[3]{.ws}[@]{.cc}[decorator₂]{.stx}\
[3]{.ws}[def]{.cc} [ident]{.stx}[(]{.cc} [args]{.stx} [):]{.cc}\
[3]{.ws}[3]{.ws}···

A decorator must appear on a line by itself, but may be followed by a comment. Here is a simple *decorator* function applied multiple times:

###### `py` — Multiple decorations on one function{.snip}
```{.py}
def decorate(func):
   def inner(*args, **kwds):
      print("<decoration>", end=" ")
      return func(*args, **kwds)
   return inner

@decorate
def once(): print("once()")

@decorate
@decorate
def twice(): print("twice()")

@decorate
@decorate
@decorate
def thrice(): print("thrice()")

once()  ;  twice()  ; thrice()

once = decorate(decorate(once)) ; once()
```
```{.output}
<decoration> once()
<decoration> <decoration> twice()
<decoration> <decoration> <decoration> thrice()
<decoration> <decoration> <decoration> once()
```

The last statement ‘redecorated’ the [once]{.cc} function two more times, without using the special **@**[decorator]{.stx} syntax. After this, [once]{.cc} has the same behaviour as [thrice]{.cc}.

Python provides a number functions designed as decorators, for example [[property]{.cc}][p-fn-property], [[staticmethod]{.cc}][p-fn-staticmethod], [[classmethod]{.cc}][p-fn-classmethod], and several in the [[functools]{.cc}][p-lib-functools] module.

[w-first-class]:
   https://en.wikipedia.org/wiki/First-class_citizen
   "Wikipedia — First-Class Citizen"
[w-decorator]:
   https://en.wikipedia.org/wiki/Decorator_pattern
   "Wikipedia — Decorator Pattern"
[p-fn-property]:
   https://docs.python.org/3/library/functions.html#property
   "Python Reference — Built-In Functions # property()"
[p-fn-staticmethod]:
   https://docs.python.org/3/library/functions.html#staticmethod
   "Python Reference — Built-In Functions # staticmethod()"
[p-fn-classmethod]:
   https://docs.python.org/3/library/functions.html#classmethod
   "Python Reference — Built-In Functions # classmethod()"
[p-lib-functools]:
   https://docs.python.org/3/library/functools.html
   "Python Reference — Library / functools Module"
[p-gl-generator]:
   https://docs.python.org/3/glossary.html#term-generator
   "Python Reference — Glossary - generator"
[pyd-gloss-decorator]:
   https://docs.python.org/3/glossary.html#term-decorator
   "Python Reference — Glossary - decorator"
[pyd-fn-classmeth]:
   https://docs.python.org/3/library/functions.html#classmethod
   "Python Reference — Built-in Functions - @classmethod"
[pyd-fn-object]:
   https://docs.python.org/3/library/functions.html#object
   "Python Reference — Built-in Functions - object()"
[pyd-fn-staticmeth]:
   https://docs.python.org/3/library/functions.html#staticmethod
   "Python Reference — Built-in Functions - @staticmethod"
[pyd-fn-isinstance]:
   https://docs.python.org/3/library/functions.html#isinstance
   "Python Reference — Built-in Functions - isinstance()"

