[Control structures][w-ctrl-flow], also known as [compound statements][p-st-compound], are an essential part of any programming language. They allow you to control the *flow* of execution in your program based on certain *conditions*. Python include conditional statements or *selection statements*, such as **if**; as well as looping constructs (or *iteration statements*) such as **for** and **while**.

[w-ctrl-flow]:
   https://en.wikipedia.org/wiki/Control_flow
   "Wikipedia — Control Flow"
[p-st-compound]:
   https://docs.python.org/3/reference/compound_stmts.html#compound-statements
   "Python Reference — 8. Compound Statements"

# Preliminaries

Several control structures requires a [condition][w-conditional] that controls behaviour. Control structures have a ‘body’ *block* clause, which must be indented to be considered legal syntax.

[w-conditional]:
   https://en.wikipedia.org/wiki/Conditional_(computer_programming)
   "Wikipedia — Conditional (computer programming)"

## Conditions

Statements like the [**if** statement][p-st-if], will either execute a *branch* of code, or not, depending on the value a [condition]{.stx}, which is simply an arbitrary [expr]{.stx}ression, but with a [**bool**][p-tp-bool]ean result.

We say it will conditionally execute the [branch]{.stx} or ‘body of the [**if**][p-st-if]’, when the [condition]{.stx} evaluates to [**True**][p-lit-true]. If the [condition]{.stx} expression is not a [**bool**][p-fn-bool] type, Python will convert it to boolean [automatically][idgh-py1st-wiki-types-truth-cvt] first.

[p-st-if]:
   https://docs.python.org/3/reference/compound_stmts.html#the-if-statement
   "Python Reference — Compound Statements # 8.1 If Statement"
[p-fn-bool]:
   https://docs.python.org/3/library/functions.html#bool
   "Python Built-In Functions — bool()"
[p-lit-false]:
   https://docs.python.org/3/library/constants.html#False 
   "Python Literals — False (bool)"
[p-lit-true]:
   https://docs.python.org/3/library/constants.html#True 
   "Python Literals — True (bool)"
[p-tp-bool]:
   https://docs.python.org/3/library/stdtypes.html#boolean-values
   "Python Types — Boolean Values"
[idgh-py1st-wiki-types-truth-cvt]:
   Simple-Types.md#truth-conversion
   "GitHub — Incus Data / Python First / Wiki / Simple Types # Truth Conversion"

## Blocks

The compound statements require a certain syntax. Part of that syntax, requires a [block]{.stx}. A [block]{.stx} in Python, is code that is indented. Several statements indented with the same amount of whitespace, is part of the block. There are no block delimiters.

You cannot arbitrarily indent lines of code. Blocks can only appear under certain conditions, like after the colon (**:**) part of the control structure's syntax.

Inconsistent indentation will lead to syntax errors.

Unlike some other languages, Python's blocks do not automatically introduce a nested scope. This can be confusing, but only when you forget that all names are just entries in dictionaries. Python *simulates* traditional scope with dictionaries, but basic blocks to not naturally have a nested dictionary.

The blocks of functions and classes, *do* have their own nested dictionaries, so that we can still have the concept of namespaces and *local variables*.

# If Statement

The [**if** statement][p-st-if] will execute its [block]{.stx} or ‘execution branch’, only when the required [condition]{.stx} is [**True**][p-lit-true]. If the [block]{.stx} consists of one simple statement, it can appear on the same line as the [**if**][p-st-if], but that is not considered good practice.

&nbsp;&nbsp;&nbsp;&nbsp; **if** [condition]{.stx}**:** [statement]{.stx}<br/>
&nbsp;&nbsp;&nbsp;&nbsp; **if** [condition]{.stx}**:**<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [block]{.stx} 

#### **py** — *If statement conditions*
```py
>> if True: print("TRUE")      #→ TRUE
>> if False: print("TRUE")     #→
>> if True:
··     print("TRUE")           #→ TRUE
··     print("Still TRUE")     #→ Still TRUE
>> if "ABC": print("TRUE")     #→ TRUE
>> if 12345: print("TRUE")     #→ TRUE
```

The [condition]{.stx} is never ‘hard-coded’ as we did above. It will normally contain [comparison][idgh-py1st-wiki-expr-comp] and [logical][idgh-py1st-wiki-expr-logic] operators. The code example below checks first if **height** is not empty (empty string will be converted to [**False**][p-lit-false]). Then it shows two ways to check if the input **height** is in the range **1**…**10** inclusive.

#### **py** — *More if statement conditions*
```py
>> height = input("Height [1..10]?: ")
>> if not height:
··    print("height is empty")
>> height = input("Height [1..10]?: ")
>> if 1 <= height and height <= 10:
··    print("height is OK")
>> if 1 <= height <= 10:
··    print("height is OK")
```

The last [**if**][p-st-if] uses a Python [shorthand][idgh-py1st-wiki-expr-short] for the previous [**if**][p-st-if].

Do not confuse an [**if** statement][p-st-if] with the **if** in a [conditional expression][idgh-py1st-wiki-expr-cond].

[idgh-py1st-wiki-expr-logic]:
   Expressions.md#logic
   "GitHub — Incus Data / Python First / Wiki / Expressions # Logic"
[idgh-py1st-wiki-expr-comp]:
   Expressions.md#comparisons
   "GitHub — Incus Data / Python First / Wiki / Expressions # Comparisons"
[idgh-py1st-wiki-expr-short]:
   Expressions.md#shorthand
   "GitHub — Incus Data / Python First / Wiki / Expressions # Shorthand"
[idgh-py1st-wiki-expr-cond]:
   Expressions.md#conditional-expression
   "GitHub — Incus Data / Python First / Wiki / Expressions # Conditional Expression"

## Else Clause

The [**if**][p-st-if] statement [above](#if-statement) will either take a branch, or not. Execution continues in either situation after the statement. We can provide an *alternate* or ‘false’ branch, if the ‘true’ branch was not taken. This requires the optional [**else** clause][p-st-else].

&nbsp;&nbsp;&nbsp;&nbsp; **if** [condition]{.stx}**:**<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [true-block]{.stx}<br/>
&nbsp;&nbsp;&nbsp;&nbsp; **else:**<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [false-block]{.stx} 

#### **py** — *Else clause example*
```py
>> if True:
··    print("TRUE")
·· else:
··    print("FALSE")            #→ TRUE
>> print("AFTER")               #→ AFTER
>> if False:
··    print("TRUE")
·· else:
··    print("FALSE")            #→ FALSE
>> print("AFTER")               #→ AFTER
```

The [**else**][p-st-else] cannot appear by itself. This is not the only place where it can be used. We shall see it again later.

[p-st-else]:
   https://docs.python.org/3/reference/compound_stmts.html#else-clause
   "Python Reference — Compound Statements # 8.4.3 Else Clause"

## Elif Clause

We can create a control structure that selects one of *multiple* branches, not just two — often called a *multi-way select statement*. This requires a variation of the [**if**][p-st-if] statement called [**elif**][p-st-if] (short for ‘else if’). An [**if**][p-st-if] statement may have multiple such [**elif**][p-st-if] clauses. Each [**elif**][p-st-if] must have its own [condition]{.stx}.

&nbsp;&nbsp;&nbsp;&nbsp; **if** [condition₁]{.stx}**:**<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [block₁]{.stx}<br/>
&nbsp;&nbsp;&nbsp;&nbsp; **elif** [condition₂]{.stx}**:**<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [block₂]{.stx}<br/>
&nbsp;&nbsp;&nbsp;&nbsp; ··· <br/>
&nbsp;&nbsp;&nbsp;&nbsp; **else:**<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [false-block]{.stx} 

The [**else** clause](#else-clause) is still optional, and if present, must appear last. Its [false-block]{.stx} will only be executed if all the [conditions]{.stx} above it, resulted in [**False**][p-lit-false].

# While Loop

The [**while** statement][p-st-while] is an *iteration statement* or ‘loop’. It executes its body [block]{.stx} while a [[condition]{.stx}](#conditions) remains [**True**][p-lit-true] (or: until the [condition]{.stx} becomes [**False**][p-lit-false]).

&nbsp;&nbsp;&nbsp;&nbsp; **while** [condition₁]{.stx}**:**<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [block₁]{.stx}<br/>

Apart from the keyword, it has the same structure as the [**if** statement](#if-statement) above. You should make sure that the [condition]{.stx} becomes [**False**][p-lit-false] at some point, otherwise the iteration will continue indefinitely. Such a loop is called an *infinite loop*, which is seldom desirable.

#### **py** — *While loop with descending numbers*
```py
>> i = 5
>> while i > 0:
··     print(i, end=' ')         #→ 5 4 3 2 1
··     i = i - 1                 #← (1)
>> print(i)                      #→ 0
```

 * `(1)` — Here we ensure that the [condition]{.stx} `i > 0` will eventually become [**False**][p-lit-false].

If you wanted to output to be with ascending numbers, you can write the iteration as follows:

#### **py** — *While loop with ascending numbers*
```py
>> i = 0
>> while i < 5:
··     print(i + 1, end=' ')     #→ 1 2 3 4 5 
··     i = i + 1                 #← (1)
>> print(i)                      #→ 0
```

[p-st-while]:
   https://docs.python.org/3/reference/compound_stmts.html#the-while-statement
   "Python Reference — Compound Statements # 8.2 While Statement"

# For Loop

This statement should have been called the ‘foreach statement’, and that is how you should think about it. Although spelled wrong, the [**for** statement][p-st-for] iterates through a *sequence* (a fancy name for a collection of items).

&nbsp;&nbsp;&nbsp;&nbsp; **for** [item]{.stx} **in** [sequence]{.stx}**:**<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [block]{.stx}<br/>

Abstractly, this construct implements “for each [item]{.stx} in a collection [sequence]{.stx}…”. It iterates through a collection of items, one item per iteration.

Since strings (type [**str**][p-fn-str] expressions) are sequences, we can use this to iterate through the characters in a string.

#### **py** — *Iterate through characters in string*
```py
>> for c in "ABCDE":
··    print(f"({c})", end='')  #→(A)(B)(C)(D)(E)
```

It becomes even more useful, if we consider the [**range** function][p-fn-range]; it produces a [**range** object][p-tp-range], which is documented as being a *sequence*. We can reproduce the logic in a prior [**while** statement](#while-statement) example, using [**for**][p-st-for] this time:

#### **py** — *For loop with range generator*
```py
>> for i in range(5):
··    print(i + 1, end=' ')    #→ 1 2 3 4 5 
>> print(i)                    #→ 5
```

First recognise that the name **`i`** is available (in scope) after the loop has terminated. Secondly: when we know the number of iterations required, the [**for**][p-st-for] is more compact than an equivalent [**while**][p-st-while], and should be preferred. 

[p-st-for]:
   https://docs.python.org/3/reference/compound_stmts.html#the-for-statement
   "Python Reference — Compound Statements # 8.3 For Statement"
[p-fn-str]:
   https://docs.python.org/3/library/stdtypes.html#str
   "Python Built-In Functions — str()"
[p-fn-range]:
   https://docs.python.org/3/library/stdtypes.html#range
   "Python Built-In Functions — range()"
[p-tp-range]:
   https://docs.python.org/3/library/stdtypes.html#range
   "Python Reference — Standard Types # range()"

# Break & Continue

The [**break**][p-st-break] and [**continue**][p-st-cont] statements are *execution transfer* statements. They summarily transfer execution away from the normal flow of control. This means that no statement after an execution transfer statement, will execute.

As a consequence, these statements are only really useful after a conditional statement such as [**if**](#if-statement). Furthermore, they are constrained to the blocks of iteration statements like [**for**](#for-statement) and [**while**](#while-statement).

## Break Statement

The [**break**][p-st-break] statement will ‘jump out’ of an iteration statement; immediately, regardless of the state of the iteration and a possible [condition]{.stx}.

The following example will repeatedly request a **height** from the user, while it is not valid. When the user entered something, the [**break**][p-st-break] statement will terminate the loop:

#### **py** — *Deliberate infinite loop for repeated input*
```py
>> while True:
··    height = input("Height?: ")
··    if height:
··       break
··    print("Try again.")
·· # use `height` here...
```

This is an example of a deliberate infinite loop that is actually useful. It is better than the alternative, which must duplicate the [**input**][p-fn-input] part:

#### **py** — *Inefficient repeated input loop*
```py
>> height = input("Height?: ")
>> while not height:
··    height = input("Height?: ")
··    if height:
··       break
··    print("Try again.")
·· # use `height` here...
```

Do not use [**break**][p-st-break] indiscriminately. For patterns like the prior example above, it is easy to recognise and understand, and will not earn you the ire of your colleagues.

[p-st-break]:
   https://docs.python.org/3/reference/simple_stmts.html#the-break-statement
   "Python Reference — Simple Statements # 7.9 Break Statement"
[p-st-cont]:
   https://docs.python.org/3/reference/simple_stmts.html#the-continue-statement
   "Python Reference — Simple Statements # 7.10 Continue Statement"
[p-fn-input]:
   https://docs.python.org/3/library/functions.html#input
   "Python Built-In Functions — input()"

### Loop Else

An interesting Python feature, is that the [**else**][p-st-else] can also appear at then end of any of the iteration statements, [**for**][p-st-for] and [**while**][p-st-while]:

&nbsp;&nbsp;&nbsp;&nbsp; **for** ‖ **while** … **:**<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [block₁]{.stx}<br/>
&nbsp;&nbsp;&nbsp;&nbsp; **else:**<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [block₂]{.stx}<br/>

The code in [block₂]{.stx} will only run if the loop in [block₁]{.stx} finished without being interrupted by a [**break**][p-st-break]. This is similar to using a flag variable called **broke** to check if the loop ended normally or was broken out of, as we do in the following example:

#### **py** — *Check if loop terminated with break*
```py
>> broke = False
>> for i in range(5):
··    if i == 3: 
··       broke = True
··       break
··    print(i, end=' ')       #→ 0 1 2
>> if not broke: 
··    print("Normal stop")    #← will not run.
```

Using the [**else**][p-st-else] clause would eliminate the need for the **broke** flag, without affecting the behaviour:

#### **py** — *Else clause on for loop*
```py
>> for i in range(5):
··    if i == 3: 
··       break
··    print(i, end=' ')       #→ 0 1 2
>> else: 
··    print("Normal stop")    #← will not run.
```

And that is the only reason [**else**][p-st-else] is allowed after iteration statements — a nice convenience when you need it, otherwise you just ignore it.

## Continue Statement

The [**continue**][p-st-cont] statement ‘performs the next iteration’ immediately, instead of when the flow reach the normal end of the block. Like [**break**](#break-statement), it is really only useful after an [**if**](#if-statement) statement. It can simplify some code, mostly in the reduction of indentation levels.

Here is an example script snippet that calculates the sum of squares of a list of positive numbers. It ignores negative numbers, and does *not* use [**continue**][p-st-cont].

#### **py** — *Sum of squares of positive numbers*
```py
nums = [1, -2, 3, -4, 5, -6, 7]
sosq = 0
for num in nums:
   if num >= 0:
      sosq += num ** 2

print(f"Sum of squares: {sosq}")
```

Notice that the ‘work’ `sosq += num ** 2` is three levels deep. Now we rewrite the above code extract, using [**continue**][p-st-cont]:

#### **py** — *Next iteration with continue*
```py
nums = [1, -2, 3, -4, 5, -6, 7]
sosq = 0
for num in nums:
   if num < 0: continue
   sosq += num ** 2

print(f"Sum of squares: {sosq}")
```

Using [**continue**][p-st-cont] can save indentation levels and make code neater. However, like [**break**][p-st-cont], [**continue**][p-st-cont] changes the normal flow of control and can make complex code harder to follow. Use it carefully — always consider readability first.

# Pattern Matching

[**PEP-634**][pep-634] contains the formal specification for *structural pattern matching*, while [**PEP-636**][pep-636] is a tutorial. This Python 3.10 *syntax* provides a new [**match**][p-st-match] statement, which is vaguely similar to ‘[switch][w-switch]’ statements as found in some C-like languages.

#### **`py`** — *some structural pattern matching examples*
```py
value = "something"                #←or use `input(…)`

### Match constants, including strings, using `|` for alternation.

match value.lower():
   case "one thing":
      print("One Thing")
   case "some thing" | "something":
      print("Some Thing")
   case "other" | "other thing":
      print("Other Thing")
   case _:                        #←‘wildcard’; matches anything.
      print("Or Another Thing")

errors = [200, 202, 300, 400, 405, 500, 600]

### Match constants, or bind to variable (`e`) and include `if`

for error in errors:
   match error:
      case e if 100 <= e < 200:
         print(f"{error}: Informational status")
      case 200:
         print(f"{error}: Absolute success")
      case e if 200 < e < 300:
         print(f"{error}: Generally successful")
      case 300:
         print(f"{error}: Specific redirection")
      case e if 300 < e < 400:
         print(f"{error}: Other redirection")
      case e if 400 <= e < 500:
         print(f"{error}: Some request error")
      case e if 500 <= e < 600:
         print(f"{error}: Some server error")
      case _:
          print(f"{error}: Unrecognised error")
```

[w-switch]:
   https://en.wikipedia.org/wiki/Switch_statement
   "Wikipedia — Switch Statement"
[py-st-match]:
   https://docs.python.org/3/reference/compound_stmts.html#the-match-statement
   "Python Reference — Compound Statements # 8.6 The Match Statement"
[pep-634]:
   https://peps.python.org/pep-0634/
   "PEP-634 — Structural Pattern Matching — Specification"
[pep-636]:
   https://peps.python.org/pep-0636/
   "PEP-636 — Structural Pattern Matching — Tutorial"

The last example would arguably more readable with a series of [**if**][p-st-if]-[**elif**][p-st-if] statements, but structural pattern matching can get much fancier than these simple examples.

You can bind a value to a name and use it in the corresponding code block:

#### **py** — *Binding names in match statements*
```py
def greet(who):
   match who:
      case {"name": str(name), "age": int(age)}:
         print(f"Hi, {name}! ({age} years old)")
      case _:
         print("Invalid `who` data")

greet({"name": "Shane", "age": 24})  #→ Hi, Shane! (24 years old)
```

The first [**case**][p-st-match] bounds `name` (of type [**str**][p-fn-str]ing) and `age` (of type [**int**][p-fn-int]) to the values passed in the dictionary, so that is can be used with the [**print**][p-fn-print] that follows. It could have been any names.

You can match sequences, such as lists or tuples, with a specified structure:

#### **py** — *Matching sequences*
```py
def describe(colors):
   match colors:
      case []:
         print("No colors")
      case [single]:
         print(f"One color: {single}")
      case [first, second]:
         print(f"Two colors: {first}, {second}")
      case [_, *others]:
         print(f"Multiple: {', '.join(others)}")

describe(["red", "green", "blue"])  #→ Multiple: green, blue
```

[Guards][p-st-guard] are additional conditions that must be satisfied for a case to be considered a match. You can add a guard to a case statement by using the [**if**][p-st-guard] keyword:

#### **py** — *If guards in cases*
```py
def process_number(number):
   match number:
      case x if x < 0:
         print("Negative number")
      case x if x == 0:
         print("Zero")
      case x if x > 0:
         print("Positive number")

process_number(42)                 #→ Positive number
```

This also creates the value `x` as a binding for `number`, in case you wanted to use it in the [**case**][p-st-match] blocks.

To simulate the ‘default’ or ‘catch-all’ situation as found in other languages, we use ‘[**case**][p-st-match] **_:**’. It must appear last for it to be useful. If no such catch-all case is present, and none of the other [**case**][p-st-match]s matched, nothing will be executed in the [**match**][p-st-match] statement.

[p-st-match]:
   https://docs.python.org/3/reference/compound_stmts.html#the-match-statement
   "Python Reference — Compound Statements # 8.6 The Match Statement"
[p-st-guard]:
   https://docs.python.org/3/reference/compound_stmts.html#guards
   "Python Reference — Compound Statements # 8.6.2 Guards"
[p-fn-int]:
   https://docs.python.org/3/library/functions.html#int 
   "Python Built-in Functions — int()"
[p-fn-print]:
   https://docs.python.org/3/library/functions.html#print
   "Python Built-in Functions — print()"

