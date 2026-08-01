Almost every statement contains an [expression][w-expr], which we indicate in syntax as [expr]{.stx}, and sometimes refer to as [expr]{.stx}ession in paragraph text. [Expressions][p-expr] can be simple (single value), or complex (contain operators). The operands of operators are expressions, which means that an expression, can contain *sub-expressions*.

[p-expr]:
   https://docs.python.org/3/reference/expressions.html#operator-precedence
   "Python Reference — Expressions"
[w-expr]:
   https://en.wikipedia.org/wiki/Expression_(computer_science)
   "Wikipedia — Expression (computer science)"

# Expression Features

An [expression][p-expr] is a programming construct that ‘has a value’. To be more exact, an expression *results* in one, and only one, [value]{.stx}. As we have seen, any value has a [type]{.stx}, so it is reasonable to say: an [expr]{.stx}ession has a [value]{.stx} and a [type]{.stx}:

&nbsp;&nbsp;&nbsp;&nbsp; [expr]{.stx} &nbsp; ⇒ &nbsp; [value]{.stx} + [type]{.stx}

If an expression contain operators, those operators will require *operands*. Some operators require one operand (unary operators), and some require two (binary operators). Not all operators work with all [type]{.stx}s of values.

When an operator can work with multiple types of operands, we say it is *overloaded*. For example, the addition operator (**+**), is overloaded for [**str**][p-tp-str] types, which will perform *concatenation* when its operands are [**str**][p-tp-str] types, instead of addition.

The order in which expressions are evaluated, depends on the [precedence][p-op-prec] of the operators. When two operators have the same level of precedence, Python chooses one based on their [associativity][w-op-assoc] with their operands. Most operators associate from left-to-right (L→R), while the exponentiation operator associate from right-to-left (R→L).

[p-op-prec]:
   https://docs.python.org/3/reference/expressions.html#operator-precedence
   "Python Reference — Expressions # 6.17 Operator Precedence"
[p-tp-str]:
   https://docs.python.org/3/library/stdtypes.html#str
   "Python Types — str"
[w-op-assoc]:
   https://en.wikipedia.org/wiki/Operator_associativity
   "Wikipedia — Operator Associativity"

# Operator Precedence

Operators are listed below from highest to lowest precedence. Note that some operators are not symbols, but keywords. The [expr]{.stx} parts below must be an appropriate [type]{.stx} for the relevant operators. It can be a simple [obj]{.stx}ect.

| operators | description |
|:----------|:------------|
| **(**[expr]{.stx}…**)**, **\[**[expr]{.stx}…**\]**, **{**[key]{.stx}**:**[val]{.stx}**}**, **{**[expr]{.stx}…**}** | Force precedence; list, dictionary, set literals |
| [expr]{.stx}**\[**[index]{.stx}**\]**, [expr]{.stx}**\[**[index]{.stx}**:**[index]{.stx}**\]**, [expr]{.stx}**(**[arg]{.stx}**,**…**)**, [expr]{.stx}**.**[attr]{.stx} | Subcript, slice, function call, attribute reference |
| **await** [expr]{.stx} | Await asynchronous expression. |
| [num]{.stx}__\*\*__[exp]{.stx} | Exponentiation: raise [num]{.stx} to [exp]{.stx}. |
| **+**[expr]{.stx}, **-**[expr]{.stx}, **~**[expr]{.stx} | Unary plus, minus, bitwise NOT |
| [expr]{.stx}__\*__[expr]{.stx}, [expr]{.stx}**@**[expr]{.stx}, [expr]{.stx}**/**[expr]{.stx}, [expr]{.stx}**//**[expr]{.stx}, [expr]{.stx}**%**[expr]{.stx} | Multiplication, matrix multiplication, division, integer division, remainder (modulus) |
| [expr]{.stx}**+**[expr]{.stx}, [expr]{.stx}**-**[expr]{.stx} | Addition, subtraction (difference) |
| [int]{.stx}**<<**[int]{.stx}, [int]{.stx}**>>**[int]{.stx} | Bitwise left shift, right shift |
| [int]{.stx}**&**[int]{.stx} | Bitwise AND |
| [int]{.stx}**^**[int]{.stx} | Bitwise XOR |
| [int]{.stx}**\|**[int]{.stx} | Bitwise OR |
| **in**, **not&nbsp;in**, **is**, **is&nbsp;not**, **<**, **<=**, **>**, **>=**, **!=**, **==** | Membership (**in**), identity (**is**), comparisons, all returning **bool** |
| **not**&nbsp;[expr]{.stx} | Logical (boolean) NOT |
| **and** | Logical (boolean) AND |
| **or** | Logical (boolean) OR |
| **if**-**else** | Conditional expression |
| **lambda** | Lambda expression |
| **:=** | Assignment expression |

Note that normal assignment is a *statement*, where the right hand expression is evaluated first. This must not be confused with **:=**, a newer assignment *expression*.

As a matter of good convention, we tend to put spaces around binary operators, except the attribute reference (**.**) and exponentiation (__\*\*__) operators. No spaces after unary operators, or before the subscript operator.

## Operator Implementation

Most operators are really just ‘disguised’ function calls, with a convenient and compact syntax. Each operator correlates to a [special method][p-spec-methods], and a custom class can provide an implementation for each, to achieve *operator overloading*. Here is a table:

| Operators    | Special Methods   |
|:-------------|:------------------|
| `**`         | `__pow__`         |
| `+`          | `__add__`         |
| `-`          | `__sub__`         |
| `*`          | `__mul__`         |
| `/`          | `__truediv__`     |
| `//`         | `__floordiv__`    |
| `%`          | `__mod__`         |
| `@`          | `__matmul__`      |
| `<<`         | `__lshift__`      |
| `>>`         | `__rshift__`      |
| `&`          | `__and__`         |
| `^`          | `__xor__`         |
| `\|`         | `__or__`          |
| `==`         | `__eq__`          |
| `!=`         | `__ne__`          |
| `<`          | `__lt__`          |
| `<=`         | `__le__`          |
| `>`          | `__gt__`          |
| `>=`         | `__ge__`          |
| `+` (unary)  | `__pos__`         |
| `-` (unary)  | `__neg__`         |
| `~` (unary)  | `__invert__`      |
| `[]`         | `__getitem__`, `__setitem__` |

Please note that the logical operators (`and`, `or`, `not`) and membership testing operators (`in`, `not in`) are not associated with special methods, as they rely on the boolean values or other special methods of the objects they operate on.

The reason for this design choice, is that it allows classes to *overload* these operators.
Although not implemented as a function, we can even overload the [**\_\_call\_\_**][p-dm-call] special method to make objects [callable](##py--callable-objects).

[p-spec-methods]:
   https://docs.python.org/3/reference/datamodel.html#special-method-names
   "Python Reference — Data Model # 3.3 Special Method Names"

### Operator Module

The standard [**operator** module][p-lib-operator] provide a convenient way to ‘call’ intrinsic (built-in) operators as functions. This is mostly useful if you want to a pass an operator to a function that requires a [callable](#function-call) argument.

If this module has been [**import**][p-st-import]ed, the function call ‘**operator.add**(a, b)’ is equivalent the operator notation: ‘a **+** b’.

#### **py** — *Operator module functions*
```py
import operator, functools
result1 = operator.add(12, 34)
result2 = 12 + 34
print(result1, result2)             #→ 46 46
total = functools.reduce(
   operator.mul,                    #← pass `*`
   [11, 22, 33, 44])
print(total)                        #→ 351384
```

[p-lib-operator]:
   https://docs.python.org/3/library/operator.html
   "Python Library — operator Module"
[p-st-import]:
   https://docs.python.org/3/reference/import.html#the-import-system
   "Python Reference — 5 The Import System"

# Arithmetic

Operators that should be familiar to you, are the arithmetic operators: multiplication (__\*__), division (**/**), addition (**+**) and subtraction (**-**). They work on both [**int**][p-fn-int] and [**float**][p-fn-float] type operands, i.e., [numeric types][p-tp-num].

When mixing [**int**][p-fn-int] and [**float**][p-fn-float] operands with arithmetic operators, they will first convert the [**int**][p-fn-int] operand to [**float**][p-fn-float], before evaluating the operator. The result will thus be [**float**][p-fn-float].

#### **py** — *Implicit arithmetic conversion*
```py
>> print( type(12.34 * 2) )  #→ float
```

What is unusual, compared to some other languages, is that the division operator always returns a [**float**][p-fn-float]ing point result; even if both the operands are of type [**int**][p-fn-int].

#### **py** — *Floating point division*
```py
>> print( 2 / 3 )            #→ 0.6666666666666666 
>> print( type (2 / 3) )     #→ float 
```

For situations where this is undesirable behaviour, you must use the *integer division* operator: **//**. It always returns an integer value, though not necessarily of type [**int**][p-fn-int]… but even if the result is [**float**][p-fn-float], the significant digits will be **.0**.

#### **py** — *True division vs floor division*
```py
>> print ( 12   /  5 )       #→ 2.4    ← float
>> print ( 12   // 5 )       #→ 2      ← int
>> print ( 12.0 /  5 )       #→ 2.4    ← float
>> print ( 12.0 // 5 )       #→ 2.0    ← float
```

Also unusual, is the modulus or *remainder* operator (**%**). It surprisingly works with [**float**][p-fn-float] and [**int**][p-fn-int] values. In other languages, it tends to work only with integer types in those languages. It works like division, but returns the remainder, instead of the division result.

#### **py** — *Modules/remainder operator*
```py
>> print( 22 // 5 )          #→ 4      ← division.
>> print( 22 %  5 )          #→ 2      ← remainder.
>> print( 1.5 / 5 )          #→ 0.3    ← division.
>> print( 1.5 % 5 )          #→ 1.5    ← remainder
>> print( 1.5 % 1.25 )       #→ 0.25   ← remainder
```

Python also has the exponentiation or ‘to the power’ operator: __\*\*__. It can raise a numeric operand to a power. The power can be a [**float**][p-fn-float], and even negative (inverse).

#### **py** — *Exponentiation operator (to the power)*
```py
>> print( 2.5 ** 2  )        #→ 6.25   ← 2.5 × 2.5
>> print( 2.5 ** 3  )        #→ 15.625 ← 2.5 × 2.5 × 2.5
>> print( 2.5 ** -2 )        #→ 0.15   ← 1 ÷ 2.5 ÷ 2.5
>> print( 2.5 ** -3 )        #→ 0.064  ← 1 ÷ 2.5 ÷ 2.5 ÷ 2.5
>> print( 2.5 ** 0.5)        #→ 1.581… ← math.sqrt(2.5)
```

Spaces around the exponentiation operator is optional.

[p-fn-int]:
   https://docs.python.org/3/library/functions.html#int 
   "Python Built-in Functions — int()"
[p-fn-float]:
   https://docs.python.org/3/library/functions.html#float
   "Python Built-in Functions — float()"
[p-tp-num]:
   https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
   "Python Types — Numeric Types — int, float, complex"

# Comparisons

We can compare two expressions for equality using: **==** (equality operator). We can establish inequality with: **!=** (inequality operator). These operators always return a [**bool**][p-fn-bool] ([boolean][p-tp-bool]) result: [**True**](##) or [**False*](##).

#### **py** — *Equality and inequality operators*
```py
>> print( "ABC" == "abc" )           #→ False
>> print( "ABC" != "abc" )           #→ True
>> print( "ABC" == "ABC" )           #→ True
>> print( 1.0   == 1     )           #→ True
>> print( 123   != 124   )           #→ True
```

When ordering becomes important, we can use the less-than (**\<**), less-than or equal (**\<=**), greater-than (**\>**) and greater-than or equal (**\>=**) operators. Like the equality operators, they only return a [**bool**][p-tp-bool]ean result.

#### **py** — *Ordering comparison operators*
```py
>> print( "ABC" >  "abc" )           #→ False
>> print( "ABC" <  "abc" )           #→ True
>> print( "ABC" >= "ABC" )           #→ True
>> print( 123   <   123  )           #→ False
>> print( 123   <=  123  )           #→ True
```

The Unicode values for upper case letters are smaller than those of the lower case letters.

# Membership

Membership operators are used to test whether a value is a member of a sequence, such as a [**str**][p-fn-str]ing, [**list**][p-fn-list], [**tuple**][p-fn-tuple], or [**set**][p-fn-set]. The two membership operators are [**in**][p-op-in] and [**not in**][p-op-in], and both return [**bool**][p-fn-bool]ean values [**True**][p-lit-true] or [**False**][p-lit-false].

A common use case, is to check if a substring is present in a larger string, without resorting to [regular expressions][w-regex].

#### **py** — *Test for substring*
```py
text = "Python is FUN!"
print("P" in text)                   #→ True
if "FUN" in text: print("YES")       #→ YES
print("Z" in text)                   #→ False
if "Python" in text:
   print("Indeed")                   #→ Indeed
```

Since a [**str**][p-tp-str]ing is just a special sequence, the [**in**][p-op-in] operator will work with other sequences. It can test sequences within sequences as well, but the [type]{.stx}s must match.

#### **py** — *Membership test in sequences*
```py
primes = { 2, 3, 5, 7 }              #← set
print(3 in primes)                   #→ True
print(4 in primes)                   #→ False

fruits = [ "apple", "banana", "cherry", "date" ]
print("banana" in fruits)            #→ True
print("eggfruit" in fruits)          #→ False

pairs = ( ["apple", "red"],
          ["banana", "yellow"],
          ["cherry", "red"],
          ["date", "brown"], )

if ["cherry", "red"] in pairs:
   print("Cherries are red")         #→ Cherries are red
if ("cherry", "red") in pairs:
   print("Cherries are red")         #· Not matched.
```

The last examples shows that the [**tuple**][p-fn-tuple] `("cherry", "red")` will not match the [**list**][p-fn-list] `["cherry", "red"]`.

The inverse of [**in**][p-op-in] is [**not in**][p-op-in] (you cannot use ‘**in not**’).

[w-regex]:
   https://en.wikipedia.org/wiki/Regular_expression
   "Wikipedia — Regular Expressions"
[p-op-in]:
   https://docs.python.org/3/reference/expressions.html#membership-test-operations
   "Python Reference — Expressions # 6.10.2 Membership Test Operations"
[p-fn-list]:
   https://docs.python.org/3/library/functions.html?#func-list
   "Python Built-in Functions — list()"
[p-fn-set]:
   https://docs.python.org/3/library/functions.html?#func-set
   "Python Built-in Functions — set()"
[p-fn-str]:
   https://docs.python.org/3/library/functions.html#func-str
   "Python Built-in Functions — str()"
[p-fn-tuple]:
   https://docs.python.org/3/library/functions.html?#func-tuple
   "Python Built-in Functions — tuple()"

# Identity

Identity operators are used to compare the memory addresses (i.e., *references*) of two objects to determine if they refer to the same object. The two identity operators are [**is**][p-op-is] and [**is not**][p-op-is]. They employ the built-in [**id** function][p-fn-id], which returns a unique identification for an object. In the CPython implementation, this will be the address of the object.

Two objects may compare as equal *values*, but may be different objects in memory. Conversely, if objects have the same *identity*, they are obviously also equal.

Python will *sometimes* re-use existing literal objects, though this is not guaranteed, although common with the CPython implementation:

#### **py** — *Equal identities for simple literals*
```py
a = "ABC"  ;  b = "ABC"
print(a is b)                        #→ True
a = 123    ;  b = 123
print(a is b)                        #→ True
```

In the example, the [**id()**][p-fn-id]s of the objects that `a` and `b` reference may be the same in both cases, because CPython may have decided to reuse the same string object for both variables. But you should not rely on this behaviour.

The inverse of the [**is**][p-op-is], is ‘[**is not**][p-op-is]’ and not ‘**not is**’.

#### **py** — *Identity on non-trivial objects*
```py
a = ['A', 'B', 'C']
b = ['A', 'B', 'C']
print(a is b)                        #→ False
print(a is not b)                    #→ True
print(a == b)                        #→ True
```

The objects referenced by `a` and `b` are equal in *value*, but are not the same objects — they exist at different addresses in memory. Different names *can* reference the same object. This can be a problem only if you *think* they are different:

#### **py** — *Names referencing same object*
```py
a = ["A", "B", "C"]
b = a                                #← `b` is same object.
b[1] = 'X'                           #← change second item.
print(a)                             #→ ['A', 'X', 'C']
```

The same effect occurs when you pass an argument to a function… the reference is copied to the parameter. If the reference refers to a *mutable* object, the function can change the *contents* of the object (but not the reference).

#### **py** — *Passing copies of references*
```py
def fn (param): param[1] = 'X'
arg = ["A", "B", "C"]
print(arg)                           #→ ['A', 'B', 'C']
fn(arg)                              #← or: `fn(param=arg)`
print(arg)                           #→ ['A', 'X', 'C']
```

If **arg** and **param** were visible in the same scope, ‘**arg** **is** **param**’ would return [**True**][p-lit-true].

[p-op-is]:
   https://docs.python.org/3/reference/expressions.html#is-not
   "Python Reference — Expressions — 6.10.3 Identity Comparisons"
[p-fn-id]:
   https://docs.python.org/3/library/functions.html#id
   "Python Reference — Built-In Functions # id(object)"

# Logic

The prefix unary logical operator **not**; and the binary logical operators **and** and **or**; also return only [**bool**][p-tp-bool]ean results. They expect operands of type [**bool**][p-fn-bool], but will accept other [type]{.stx}s, which they will [automatically convert][idgh-py1st-wiki-stypes-truthcvt] to [**bool**][p-fn-bool].

```py
>> print( False or  False )          #→ False
>> print( False or  True  )          #→ True
>> print( True  or  False )          #→ True
>> print( True  or  True  )          #→ True
>> print( False and False )          #→ False
>> print( False and True  )          #→ False
>> print( True  and False )          #→ False
>> print( True  and True  )          #→ True
>> print( not True        )          #→ False
>> print( not False       )          #→ True
```

Python does not have an **xor** operator, but its logical result can be obtained using the other operators with the following formula (expression):

&nbsp;&nbsp;&nbsp;&nbsp; **(** [lhs]{.stx} **and** **not** [rhs]{.stx} **)** **or** **(** **not** [lhs]{.stx} **and** [rhs]{.stx} **)**

Here [lhs]{.stx} and [rhs]{.stx} means left hand side expression, and right hand side expression, respectively.

[p-fn-bool]:
   https://docs.python.org/3/library/functions.html#bool
   "Python Built-In Functions — bool()"
[p-tp-bool]:
   https://docs.python.org/3/library/stdtypes.html#boolean-values
   "Python Types — Boolean Values"
[idgh-py1st-wiki-stypes-truthcvt]:
   Simple-Types.md#truth-conversion
   "GitHub — Incus Data / Python First / Simple Types # Truth Conversion"

## Boolean Algebra

In [boolean algebra][w-bool-alg], **and** ([conjunction][w-conjunc]) is written as ∧, **or** ([disjunction][w-disjunc]) as ∨, and **not** ([negation][w-negate]) as ¬. Here are a few common boolean algebra laws:

 * De Morgan's law:
   * ¬ **(** **A** ∧ **B** **)** &nbsp; ≡ &nbsp; **(** ¬**A** **)** ∨ **(** ¬**B** **)**
   * ¬ **(** **A** ∨ **B** **)** &nbsp; ≡ &nbsp; **(** ¬**A** **)** ∧ **(** ¬**B** **)**

 * Distributive law:
   * **A** ∧ **(** **B** ∨ **C** **)** &nbsp; ≡ &nbsp; **(** **A** ∧ **B** **)** ∨ **(** **A** ∧ **C** **)**
   * **A** ∨ **(** **B** ∧ **C** **)** &nbsp; ≡ &nbsp; **(** **A** ∨ **B** **)** ∧ **(** **A** ∨ **C** **)**

 * Identity law:
   * **A** ∧ **True** &nbsp; ≡ &nbsp; **A**
   * **A** ∨ **False** &nbsp; ≡ &nbsp; **A**

 * Negation law:
   * **A** ∧ **(** ¬**A** **)** &nbsp; ≡ &nbsp; **False**
   * **A** ∨ **(** ¬**A** **)** &nbsp; ≡ &nbsp; **True**

These laws may help you simplify some complicated logical operations.

[w-bool-alg]:
   https://en.wikipedia.org/wiki/Boolean_algebra
   "Wikipedia — Boolean Algebra"
[w-conjunc]:
   https://en.wikipedia.org/wiki/Logical_conjunction
   "Wikipedia — Logical Conjunction"
[w-disjunc]:
   https://en.wikipedia.org/wiki/Logical_disjunction
   "Wikipedia — Logical Disjunction"
[w-negate]:
   https://en.wikipedia.org/wiki/Negation
   "Wikipedia — Logical Negation"

## Shorthand

Python has a special shorthand syntax for a common scenario: checking if a value is within a certain range. For example, imagine you want to check if some value **x**, is within the range [**A**…**B**] inclusive, here is one formula:

&nbsp;&nbsp;&nbsp;&nbsp; **x** **>=** **A** &nbsp; **and** &nbsp; **x** **<=** **B**

Which we can rewrite as following, with the same result and meaning:

&nbsp;&nbsp;&nbsp;&nbsp; **A** **<=** **x** &nbsp; **and** &nbsp; **x** **<=** **B**

For a non-inclusive range: (**A**…**B**), the formula would become:

&nbsp;&nbsp;&nbsp;&nbsp; **A** **<** **x** &nbsp; **and** &nbsp; **x** **<** **B**

Python allows us to shorten the last two examples as:

&nbsp;&nbsp;&nbsp;&nbsp; **A** **<=** **x** **<=** **B**<br/>
&nbsp;&nbsp;&nbsp;&nbsp; **A** **<** **x** **<** **B**<br/>

#### **py** — *Shorthand range check and equivalent*
```py
>> x = 5 ; A = 1 ; B = 10
>> print (x >= A and x <= B)         #→ True
>> print (A <= x and x <= B)         #→ True  ← better.
>> print (A <= x <= B)               #→ True  ← shorthand.
```

# Function Call

Arguably the most common and versatile operation, is the [function call][p-expr-call]. However, calls are not performed with a function call operator as in some other languages. Instead, it is a syntactic construct that *works like* an operator:

&nbsp;&nbsp;&nbsp;&nbsp; [callable]{.stx} **(** [[arg]{.stx}…]  **)**<br/>
&nbsp;&nbsp;&nbsp;&nbsp; [result]{.stx} **=** [callable]{.stx} **(** [[arg]{.stx}…]  **)**

 * it *invokes* a [**callable**][p-fn-callable] [expr]{.stx}ession as left hand operand;
 * initialises [parameters][p-glos-param] from [arguments][p-glos-arg] between the parentheses; and
 * finally produces a return result, which may optionally be assigned a name.

This is very similar to the operation of operators; we just use different terminology (arguments instead of operands, for example). In fact, we can even [map operators][p-op-map] to functions.

The ‘[callable]{.stx} **`(`**…**`)`**’ syntax is really shorthand for Python mechanics calling a special [**\_\_call\_\_**][p-dm-call] method.

[p-glos-arg]:
   https://docs.python.org/3/glossary.html#term-argument
   "Python Glossary — Argument"
[p-glos-param]:
   https://docs.python.org/3/glossary.html#term-parameter
   "Python Glossary — Parameter"

## Callables

Any [exp]{.stx}ression that is [**callable**][p-fn-callable] can be *invoked* with parentheses following the [exp]{.stx}ression. We can test if an [expr]{.stx}ession can be invoked, with the [**callable(**[expr]{.stx}**)**][p-fn-callable] built-in function.

Technically, Python looks for a special [**\_\_call\_\_**][p-dm-call] method in the [type]{.stx} of the [expr]{.stx}ession, and simply invokes *that*, passing it the arguments, and collecting its return value.

#### **py** — *Built-in function call detail*
```py
import builtins
print(builtins.str.__call__(123))    #→ 123
print(str(123))                      #→ 123
```

For calling methods in custom classes the same syntax is used, but is again a convenient shorthand for a more complex operation, where Python must pass the [object]{.stx} on which the method is called, as the first argument.

&nbsp;&nbsp;&nbsp;&nbsp; [obj]{.stx}**.**[method]{.stx}**(**[args]{.stx}**)** &nbsp;&nbsp; ≡ &nbsp;&nbsp; [class]{.stx}**.**[method]{.stx}**(**[obj]{.stx}**,** [args]{.stx}**)**

That leads to a number of ways a [method]{.stx} can be called, though in practice one should simply used the most succinct version:

#### **py** — *Calling object method equivalences*
```py
class Demo:
   def method(self, param): print(f"method({param})")
obj = Demo()
obj.method("arg")                    #→ method(arg)
Demo.method(obj, "arg")              #→ method(arg)
type(obj).method(obj, "arg")         #→ method(arg)
obj.__class__.method(obj, "arg")     #→ method(arg)
```

An [object]{.stx} can be made callable, if its class implements the [**\_\_call\_\_**][p-dm-call] method.

#### **py** — *Callable objects*
```py
class CallMe:
   def __call__(self, param): print(f"CallMe {param}")
obj1 = CallMe()  ;  obj2 = CallMe()
obj1("ABC")                          #→ CallMe ABC
obj2(12345)                          #→ CallMe 12345
CallMe.__call__(obj1, "ABC")         #→ CallMe ABC
CallMe.__call__(obj2, 12345)         #→ CallMe 12345
```

This makes Python very flexible, yet the shorthand syntax forms it provides are concise and obviously preferred. We show the alternatives only as a way to *understand* the Python function call mechanism.

[p-dm-call]:
   https://docs.python.org/3/reference/datamodel.html#object.__call__
   "Python Reference — Data Model # ‹obj›.__call__(self, …)"
[p-fn-callable]:
   https://docs.python.org/3/library/functions.html#callable
   "Python Built-In Functions — callable()"
[p-op-map]:
   https://docs.python.org/3/library/operator.html#mapping-operators-to-functions
   "Python Operator Module — Mapping Operators to Functions"
[p-expr-call]:
   https://docs.python.org/3/reference/expressions.html#calls
   "Python Expressions — 6.3.4 Calls"

# Conditional Expression

This looks a lot like the [**if** statement][p-st-if], but is an [expr]{.stx}ession, which means it returns a result. Statements do not return results in Python. The [**if** conditional expression][p-expr-cond] also use the [**if**](##) and [**else**](##) keywords, and will result in one of two values: [true-expr]{.stx} or [false-expr]{.stx}, if the [[condition]{.stx}][idgh-py1st-wiki-ctrl-cond] is [**True**][p-lit-true] or [**False**][p-lit-false], respectively.

&nbsp;&nbsp;&nbsp;&nbsp; [true-expr]{.stx} **if** [condition]{.stx} **else** [false-expr]{.stx}

It is similar in operation to the [conditional operator] as found in C-like languages.

#### **py** — *Conditional expression*
```py
>> height = 5
>> cat = "small" if height < 10 else "large"
>> print(cat)
#→ small
```

It is a more compact alternative to the same logic using an [**if** statement][idgh-py1st-wiki-ctrl-ifst]:

#### **py** — *Alternative without conditional expression*
```py
>> height = 5
>> if height < 10:
··    cat = "small"
·· else:
··    cat = "large"
>> print(cat)                        #→ small
```

It is similar in operation to the C/C++ conditional operator **?:**, though arguably more readable.

[p-st-if]:
   https://docs.python.org/3/reference/compound_stmts.html#the-if-statement
   "Python Reference — Compound Statements # 8.1 If Statement"
[p-expr-cond]:
   https://docs.python.org/3/reference/expressions.html#conditional-expressions
   "Python Reference — Expressions # 6.13 Conditional Expressions"
[idgh-py1st-wiki-ctrl-ifst]:
   Control-Structures.md#if-statement
   "GitHub — Incus Data / Python First / Wiki / Control Structures # If Statement"
[idgh-py1st-wiki-ctrl-cond]:
   Control-Structures.md#conditions
[p-lit-false]:
   https://docs.python.org/3/library/constants.html#False 
   "Python Literals — False (bool)"
[p-lit-true]:
   https://docs.python.org/3/library/constants.html#True 
   "Python Literals — True (bool)"
[w-cond-op]:
   https://en.wikipedia.org/wiki/Conditional_operator
   "Wikipedia — Conditional Operator"

