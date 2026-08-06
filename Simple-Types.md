---
title: Simple Types
abstract: |
   It takes all sorts… of types to work with data. Languages like Python abstracts a type as an attribute of all values. It's a way to say ‘every value or *object*, has a [type]{.stx}’. Without a basic understanding of types, you will be limited with what you can do with Python.
---

# Type Foundations

Python has a fair number of [built-in types][p-lib-stdtypes], but you do not have to learn them all at once. The most important initial types are [[bool]{.cc}][p-fn-bool] for [boolean][w-boolean] values, [[str]{.cc}][p-fn-str] for [strings][w-string], [[int]{.cc}][p-fn-int] for [integers][w-integer], and [[float]{.cc}][p-fn-float] for [double-precision][w-dp-float] floating-point values. We might throw in a [[None]{.cc}][p-lit-none] here and there, but won't make a habit of it — it has type [NoneType]{.cc}.

[p-lib-stdtypes]:
   https://docs.python.org/3/library/stdtypes.html#built-in-types
   "Python Library — Built-In Types"
[p-fn-bool]:
   https://docs.python.org/3/library/functions.html#bool
   "Python Built-in Functions — bool(x=False)"
[p-fn-float]:
   https://docs.python.org/3/library/functions.html#float
   "Python Built-in Functions — float()"
[w-boolean]:
   https://en.wikipedia.org/wiki/Boolean_data_type
   "Wikipedia — Boolean Data Type"
[w-dp-float]:
   https://en.wikipedia.org/wiki/Double-precision_floating-point_format
   "Wikipedia — Double-Precision Floating-Point Format"

## Classy Types

All types in Python, are [class types][w-class], but that little detail can be ignored in the short term — it will have little bearing on what we are trying to tell you here. The word *class* has roots in [object-oriented programming][w-oop] (OOP).

This does not mean you have to become an object-oriented programmer first to learn Python. We mention it simply because you will keep coming across this term in Python and other documentation — without much explanation.

However, you can think of a class as being analogous to a house *plan*. A physical house does not exist, but we can learn much about a future house **build** from the plan. We can build or ‘instantiate’ several houses from the same plan. We can say that these physical house objects are *instances* of the house plan.

House plan [B]{.cc} can borrow or [inherit][w-inherit] from some other house plan [A]{.cc}, and *extend* the borrowed plan by, for example, adding an extension or extra room. A [B]{.cc}-type house then, will have characteristics common to houses build from an [A]{.cc}-type plan, plus additions.

[w-class]:
   https://en.wikipedia.org/wiki/Class_(computer_programming)
   "Wikipedia — Class (computer programming)"
[w-oop]:
   https://en.wikipedia.org/wiki/Object-oriented_programming
   "Wikipedia — Object-Oriented Programming"
[w-inherit]:
   https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming)
   "Wikipedia — Inheritance (object-oriented programming)"

### Objects

It also explains why the word [object][w-object] is often used instead of *value* or [expression][w-expr]: in object-oriented programming, the formal definition is: ‘an object is an instance of a class’. It's a fancy way of saying ‘a house is an instance of a plan’.

An *instance* is just a value, having a particular type, stored somewhere in memory, often called an object. So, really, whether you say *instance*, *value*, *object*, or *expression*, it ultimately turns out to be the same thing. People create these synonyms just to discourage you from learning anything.

Any object will have a [type]{.stx}, and a [value]{.stx}. The value of an object may also have a selection of [attributes][w-attrib], and [methods][w-method], which are determined by its class.

Objects can have members, classified as *attributes* and *methods*. These are defined by their [type]{.stx} (class). They can be *instance* members or *class* members. Every object gets its own instance members, but class members are shared by all objects.

[w-object]:
   https://en.wikipedia.org/wiki/Object_(computer_science)
   "Wikipedia — Object (computer science)"
[w-expr]:
   https://en.wikipedia.org/wiki/Expression_(computer_science)
   "Wikipedia — Expression (computer science)"
[w-attrib]:
   https://en.wikipedia.org/wiki/Attribute_(computing)
   "Wikipedia — Attribute (computing)"
[w-method]:
   https://en.wikipedia.org/wiki/Method_(computer_programming)
   "Wikipedia — Method (computer programming)"

### Methods

A [method][w-method] is a function that can be called. But unlike [built-in][p-fn] functions which can be called at any time, a method can only be called ‘on an object’. This is a way to say that an [obj]{.stx}ject must first exits, before we can call a [method]{.stx}. And not any method: only methods that are specified by the [type]{.stx} of the object.

We use the ‘dot operator (&hairsp;[.]{.cc}&hairsp;)’, which some other languages name the ‘member-selection operator’, to ‘pick’ an attributes or method of the object. To call a method (or function), we need the function call operator[^note1]: [(&thinsp;)]{.cc}, which may enclose [arg]{.stx}uments, depending on the definition of the method. Multiple arguments are separated by commas (**,**).

[^note1]:
   Technically, its not a ‘real’ operator — it just *acts* like one.

[3]{.ws}[obj]{.stx} [.]{.cc} [method]{.stx} [( )]{.cc}\
[3]{.ws}[obj]{.stx} [.]{.cc} [method]{.stx} [(]{.cc} [arg]{.stx} [)]{.cc}\
[3]{.ws}[obj]{.stx} [.]{.cc} [method]{.stx} [(]{.cc} [arg₁]{.stx} [,]{.cc} [arg₂]{.stx}, … [arg<sub>n</sub>]{.stx} [)]{.cc}

In the example Python code below, [123]{.cc} is an object of type [[int]{.cc}][p-fn-int]. The [[int]{.cc}][p-fn-int] class defines methods like [[bit_length()]{.cc}][p-tp-int-bitlen], which we can thus call ‘on the object [123]{.cc}’. We need parentheses around the [123]{.cc}, otherwise the dot operator will be confused with the decimal point. If we associated a name like [var]{.cc} to [123]{.cc}, the parentheses will not be needed.


:::{.cli prompt='>>'}
###### `repl` — Calling a method on an int value
 * ``(123).bit_count()                #▷ 6``{.py .ws}
 * ``var = 123``{.py .ws}
 * ``var.bit_count()                  #▷ 6``{.py .ws}
:::

We can document the fact that [[int]{.cc}][p-fn-int] objects have a [[bit_length()]{.cc}][p-tp-int-bitlen] method like this, where [int]{.stx} means ‘an object of type [[int]{.cc}][p-fn-int]’:

[3]{.ws}[int]{.stx} [.]{.cc} [[bit_length(&thinsp;)]{.cc}][p-tp-int-bitlen]

Unfortunately, the Python documentation is not so clear on this, which might be confusing until you understand the various authors' conventions.

Not all methods require an [obj]{.stx}ect; some are *class methods*, which means that we can call them ‘on the class’, *or* on an object of the same type. An example would be ‘&thinsp;[[int]{.cc}][p-fn-int][&hairsp;.&hairsp;]{.cc}[[from_bytes(&hairsp;)]{.cc}][p-tp-int-frombyte]&thinsp;’, which we can specify like this:

[3]{.ws}[[int]{.cc}][p-fn-int] [.]{.cc} [[from_bytes(…)]{.cc}][p-tp-int-frombyte] 

:::{.cli prompt='>>'}
 * ``(123).from_bytes(b'\x02\x10', byteorder='big')  #▷528``{.py .ws}
 * ``int.from_bytes(b'\x02\x10', byteorder='big')    #▷528``{.py .ws}
:::

The [[int]{.cc}][p-fn-int][.]{.cc}[[from_bytes(…)]{.cc}][p-tp-int-frombyte] method requires arguments. You'll probably never need [from_bytes]{.cc}; this is not about [from_bytes]{.cc}, but the principles and concepts of *methods*.

[p-fn]:
   https://docs.python.org/3/library/functions.html#
   "Python Reference — Built-in Functions"
[p-tp-int-bitlen]:
   https://docs.python.org/3/library/stdtypes.html#int.bit_length
   "Python Reference — Standard Types # ‹int›.bit_length()"
[p-tp-int-frombyte]:
   https://docs.python.org/3/library/stdtypes.html#int.from_bytes
   "Python Reference — Standard Types # classmethod int.from_bytes()"
[p-tp-object]:
   https://docs.python.org/3/library/functions.html#object
   "Python Built-In Functions ― class object"
[p-tp-str]:
   https://docs.python.org/3/library/functions.html#str
   "Python Built-In Functions ― class str"
[p-t-obj-str]:
   https://docs.python.org/3/reference/datamodel.html#object.__str__
   "Python Reference — Data Model # [object]{.stx}.\_\_str\_\_(*self*)"

### Attributes

Members that are not methods, are called [attributes][w-attrib]. Think of attributes as rooms in a house. Given two houses built from the same plan: they will have the same number of rooms (attributes), but they may not have the same *content* (e.g., furniture).

So, two objects with the same type, will have the same attributes, as defined by their class, but each instance of the common attributes, may have different values. Unless a class prevents it explicitly, we can add instance attributes to any object, at any time:

:::{.cli prompt='>>'}
###### `repl` — Creating instance attributes
 * ``class C: pass            #← user-defined type called `C`.``{.py .ws}
 * ``cobj = C()               #← create object and assign `cobj` name.``{.py .ws}
 * ``cobj.name = "C Object"   #← create instance attribute `name`.``{.py .ws}
 * ``cobj.value = 123.456     #← create instance attribute `value`.``{.py .ws}
:::

Do not worry too much about the detail above… we just want you at this stage, to get ‘a feel’ for the terminology, and in this case: *attributes*.

### Member Listing

We can use the following function to display the (important) members of any object. It will indicate whether the member is an attribute, or method. It uses the [[callable]{.cc}][p-fn-callable] and [[getattr]{.cc}][p-fn-getattr] built-in functions.

###### `py` — List attributes function {#members.py .snip}
```py
def members (obj):
   for m in dir(obj):
      if m.startswith('__'): continue
      attr = getattr(obj, m)
      if callable(attr):
         print(f"method   : {m}")
      else:
         print(f"attribute: {m}")
```

If you were to run the [above function]{#members.py} with: [members(int)]{.cc}, you would get:

```{.output}
method   : as_integer_ratio
method   : bit_count
method   : bit_length
method   : conjugate
attribute: denominator
method   : from_bytes
attribute: imag
attribute: numerator
attribute: real
method   : to_bytes
```

And, you can of course simply run [[help(&hairsp;int&hairsp;)]{.cc}][p-fn-help] or [[dir(&hairsp;int&hairsp;)]{.cc}][p-fn-dir] in a REPL for all the necessary information about all the members. The [[members()]{.cc}](#members.py) function can be enhanced to also determine whether a member is an *instance* member, or a *class* member, but we shall leave that for later.

[p-fn-callable]:
   https://docs.python.org/3/library/functions.html#callable
   "Python Built-In Functions — callable()"
[p-fn-classmeth]:
   https://docs.python.org/3/library/functions.html#classmethod
   "Python Built-In Functions — classmethod()"
[p-fn-getattr]:
   https://docs.python.org/3/library/functions.html#getattr
   "Python Built-In Functions — getattr()"
[p-fn-help]:
   https://docs.python.org/3/library/functions.html#help
   "Python Built-In Functions — help()"
[p-fn-dir]:
   https://docs.python.org/3/library/functions.html#help
   "Python Built-In Functions — dir()"

## Object Type

The most basic, yet important type in Python, is [**object**][p-fn-obj]. It is significant, because it is the ‘master plan’ from which all other ‘plans’ are derived. Practically, this means that all the characteristics of the [**object**][p-fn-obj] class, will be available in *all other types*.

All the methods and attributes defined in the [**object**][p-fn-obj] class, will be present in all other objects, regardless of their [type]{.stx}. We say [**object**][p-fn-obj] is the ‘base class’ for all other classes.

### String Conversion

As all Python types inherit from [[object]{.cc}][p-tp-object], all objects will inherit a [[\_\_str\_\_]{.cc}][p-t-obj-str] method, which is what is called automatically when you use the built-in [[str(]{.cc} [object]{.stx} [)]{.cc}][p-tp-str] type function. This makes *all* Python objects convertible to strings — it even happens automatically in cases where a [[str]{.cc}][p-tp-str] is required, and the [object]{.stx} is not a [[str]{.cc}][p-tp-str]. The [[repr]{.cc}][p-fn-repr] function also can convert any object to a string.

:::{.cli prompt='>>'}
###### `repl` — Converting objects to strings
 * ``str(123)        #▷ '123'``{.py .ws}
 * ``str(1.23)       #▷ '1.23'``{.py .ws}
 * ``str(str)        #▷ "<class 'str'>"``{.py .ws}
 * ``str(type)       #▷ "<class 'type'>"``{.py .ws}
:::

The [[repr]{.cc}][p-fn-repr] will show the output the way you would normally *represent* the value in Python syntax. For strings, it will enclose the result in single quotes. This is the function the REPL uses to automatically show the results of expressions; you'll probably never use it yourself.

[p-fn-obj]:
   https://docs.python.org/3/library/functions.html#object
   "Python Built-In Functions — object()"
[p-fn-str]:
   https://docs.python.org/3/library/functions.html#str
   "Python Built-In Functions — str()"
[p-fn-repr]:
   https://docs.python.org/3/library/functions.html#repr
   "Python Built-In Functions — repr()"

## Type Type

To confuse the issue of types a little more, Python has a [type]{.stx} called [[type]{.cc}][p-fn-type], which can be used to determine the type of any object passed as argument. When the result is converted to a string (automatically or explicitly), you will get the name of the type.

:::{.cli prompt='>>'}
###### `repl` — Determining types of objects
 * ``type(type)         #▷ <class 'type'>``{.py .ws}
 * ``type(int)          #▷ <class 'type'>``{.py .ws}
 * ``type(str)          #▷ <class 'type'>``{.py .ws}
 * ``type(0)            #▷ <class 'int'>``{.py .ws}
 * ``type(0.0)          #▷ <class 'float'>``{.py .ws}
 * ``type(True)         #▷ <class 'bool'>``{.py .ws}
 * ``type("")           #▷ <class 'str'>``{.py .ws}
 * ``type('')           #▷ <class 'str'>``{.py .ws}
:::

Note that the CPython REPL will output [\<class '[type]{.stx}'\>]{.cc}, while IPython will output just [type]{.stx}. And, if you want to output the result in a script, you have to use [[print(&hairsp;)]{.cc}][p-fn-print].

Whenever you are in doubt regarding the [type]{.stx} of an [expr]{.stx}ession, do:

[3]{.ws}[print( type( [expr]{.stx} ) )]{.cc}

The extra spaces have no effect… we just added them for readability.

[p-fn-type]:
   https://docs.python.org/3/library/functions.html#type
   "Python Built-in Functions ­— type()"
[p-fn-print]:
   https://docs.python.org/3/library/functions.html#print
   "Python Built-in Functions — print()"

## Truth

Unlike human societies (and AI to some extend), computer languages have no ‘grey areas’ or ‘false news’ — it's all zeros and ones. Which we abstract ‘truth’ with Python as [[False]{.cc}][p-lit-false] or [[True]{.cc}][p-lit-true] keywords respectively. Values that represent ‘truth’ have type [[bool]{.cc}][p-fn-bool] (boolean), and can only be only one of these two values.

### Truth Conversion

The [[bool]{.cc}][p-fn-bool] (boolean) type in Python, like all types, is also a *type function*. It can be used to create *boolean* values. If called without an argument, it will create the boolean value [[False]{.cc}][p-lit-false].

Absolutely *any* value of *any* type, can be converted to boolean. This conversion is based on [truth value testing][p-truth] rules. Almost any value converted to [[bool]{.cc}][p-fn-bool], will result in [[True]{.cc}][p-lit-true] except for the following:

 * [[None]{.cc}][p-lit-none] and [[False]{.cc}][p-lit-false];
 * [Numerical][p-tp-nums] values that are zero:
   * [[0]{.cc}][p-fn-int] — integer or [[int]{.cc}][p-fn-int]
   * [[0.0]{.cc}][p-fn-float] — floating-point or [[float]{.cc}][p-fn-float]
   * [[0j]{.cc}][p-fn-complex] — complex or [[complex]{.cc}][p-fn-complex]
   * [[Decimal(0)]{.cc}][p-lib-decimal] — fixed/floating point, useful for currency
   * [[Fraction(0,1)]{.cc}][p-lib-fraction] — fractions
 * Empty collections or *sequences*:
   * [['']{.cc}][p-fn-str] or [[""]{.cc}][p-fn-str] — empty strings or [[str(&hairsp;)]{.cc}][p-fn-str]
   * [[(&hairsp;)]{.cc}][p-fn-tuple] — empty tuples or [[tuple()]{.cc}][p-fn-tuple]
   * [[[&hairsp;]]{.cc}][p-fn-list] — empty lists or [[list()]{.cc}][p-fn-list]
   * [[{&hairsp;}]{.cc}][p-fn-dict] — empty dictionaries or [[dict()]{.cc}][p-fn-dict]
   * [[set(&hairsp;)]{.cc}][p-fn-set] — empty sets
   * [[range(0)]{.cc}][p-fn-range] — empty ranges

:::{.cli prompt='>>'}
###### `repl` — Values that converts to False
 * ``bool()                                    #▷ False``{.py .ws}
 * ``bool(0)     ; bool(0.0)    ; bool(0j)     #▷all `False`.``{.py .ws}
 * ``bool('')    ; bool("")     ; bool(())     #▷all `False`.``{.py .ws}
 * ``bool([])    ; bool({})     ; bool(set())  #▷all `False`.``{.py .ws}
 * ``bool(str()) ; bool(list())                #▷all `False`.``{.py .ws}
:::

[p-tp-nums]:
   https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
   "Python Standard Types — Numeric Types — int, float, complex"
[p-lex-kwds]:
   https://docs.python.org/3/reference/lexical_analysis.html?highlight=keywords#keywords
   "Python Reference — Lexical Analysis # 2.3.1 Keywords"
[p-truth]:
   https://docs.python.org/3/library/stdtypes.html#truth
   "Python Reference — Truth Value Testing"
[p-lib-decimal]:
   https://docs.python.org/3/library/decimal.html#module-decimal
   "Python Library — decimal"
[p-lib-fraction]:
   https://docs.python.org/3/library/fractions.html
[p-fn-tuple]:
   https://docs.python.org/3/library/functions.html?#func-tuple
   "Python Built-in Functions — tuple()"
[p-fn-dict]:
   https://docs.python.org/3/library/functions.html?#func-dict
   "Python Built-in Functions — dict()"
[p-fn-list]:
   https://docs.python.org/3/library/functions.html?#func-list
   "Python Built-in Functions — list()"
[p-fn-set]:
   https://docs.python.org/3/library/functions.html?#func-set
   "Python Built-in Functions — set()"
[p-fn-range]:
   https://docs.python.org/3/library/functions.html?#func-range
   "Python Built-in Functions — range()"
[p-lit-none]:
   https://docs.python.org/3/library/constants.html#None
   "Python Literals — None (NonType)"
[p-lit-false]:
   https://docs.python.org/3/library/constants.html#False 
   "Python Literals — False (bool)"
[p-lit-true]:
   https://docs.python.org/3/library/constants.html#True 
   "Python Literals — True (bool)"

### Implicit Truths

There are parts of Python syntax that require [[bool]{.cc}][p-fn-bool]ean values ([expr]{.stx}essions) as part of the syntax. Some operators, like the [logical operators][p-expr-boolops], also require operands of [type]{.stx} [[bool]{.cc}][p-fn-bool].

If the [type]{.stx} of an [expr]{.stx}ession is not [[bool]{.cc}][p-fn-bool] wherever Python expects it, the interpreter will *automatically* or *implicitly*, call the [[bool]{.cc}][p-fn-bool] function to convert the [expr]{.stx}ession to boolean.

This is one very fundamental truth in Python: **everything is implicitly convertible to boolean**.

Initially, it seems to make no sense that [[bool][p-fn-bool]("ABC")]{.cc} or [[bool][p-fn-bool](123)]{.cc} to have the value [[True]{.cc}][p-lit-true], and [[bool][p-fn-bool](0)]{.cc} to result in [[False]{.cc}][p-lit-false]. Practical uses of this inescapable truth, will become more apparent later as we explore more Python syntax.

[p-expr-boolops]:
   https://docs.python.org/3/reference/expressions.html#boolean-operations
   "Python Expressions — 6.11 Boolean Operations"

# Arithmetic Types

It should be no surprise that Python provides good support for arithmetic of several kinds. It even implements [arbitrary-precision][w-arb-prec] arithmetic on integers.

## Integer Type

Python provides the [[int]{.cc}][p-fn-int] type to represents integer values. [Integers][w-integer] are whole numbers without a fractional part, that are useful in situations where floating point would be overkill. Operations on integers are generally faster than floating point operations.

Since all types in Python are classes, this means that an [[int]{.cc}][p-fn-int] value is an *object*. In turn, an [[int]{.cc}][p-fn-int] object will have [methods][w-method], and [attributes][w-attrib]. Some [method]{.stx}s take [arg]{.stx}uments, which are sometimes optional:

[3]{.ws}[obj]{.stx}[.]{.cc}[method]{.stx}[(]{.cc} [ [arg]{.stx}…  ] [)]{.cc}

An example would be the [[bit_count]{.cc}][p-tp-int-bit_count] method, which is an *instance* method, which means we first need an [[int]{.cc}][p-fn-int] object. We can document the syntax as:

[3]{.ws}[int]{.stx}[.]{.cc}[[bit_count(&hairsp;)]{.cc}][p-tp-int-bit_count]

On the other hand, the [[from_bytes]{.cc}][p-tp-int-from_bytes] method is a *class method*, which means we do not (necessarily) need an [[int]{.cc}][p-fn-int] object in order to call it. Syntax-wise, we show it as:

[3]{.ws}[[int]{.cc}][p-fn-int][.]{.cc}[[from_bytes(…)]{.cc}][p-tp-int-from_bytes]

The [[int]{.cc}][p-fn-int] function accepts an optional argument, or one argument, or two arguments. It can be used to truncate [[float]{.cc}][p-fn-float] values and return only the integer part. But, it can be passed a [[str]{.cc}][p-fn-str]ing type argument, which will be ‘converted’ to an [[int]{.cc}][p-fn-int]… as long as the characters in the string ‘looks like an integer’.

[3]{.ws}[[int(&hairsp;)]{.cc}][p-fn-int]\
[3]{.ws}[[int(]{.cc} [arg]{.stx} [)]{.cc}][p-fn-int]\
[3]{.ws}[[int(]{.cc} [arg]{.stx}**, base=[[base]{.stx}]{.cc})**][p-fn-int]

Note that ["123"]{.cc} has type [[str]{.cc}][p-fn-str]ing, and [123]{.cc} has type [[int]{.cc}][p-fn-int], which has an effect on an operator like [\*]{.cc} (asterisk), which can have different behaviour depending on the types of the operands:

```py
>> 123 * 2              #▷ 246      — int * int ≡ multiplication
>> int("123") * 2       #▷ 246      — int * int ≡ multiplication
>> "123" * 2            #▷ 123123   — str * int ≡ string repetition
>> 2 * "123"            #▷ 123123   — int * str ≡ string repetition
```

If the string representation of the argument is in base 2 (binary), you must pass a [base]{.cc} argument ([2]{.cc}). Similar for base [8]{.cc} (octal), and base [16]{.cc} (hexadecimal). The literal prefixes are not necessary, but allowed:

```py
>> int("1111011", 2)       #▷ 123
>> int("0b1111011", 2)     #▷ 123
>> int("1111011", base=2)  #▷ 123
>> int("0x7b", 16)         #▷ 123
>> int("7B", base=16)      #▷ 123
```

You can pass arguments as a single [expr]{.stx}ession, or by naming the argument, using the name of the parameter as documented — Python call this ‘keyword argument’ syntax. There is a reason for this naming, but is unfortunately not readily apparent from above. Just try to remember that inside a function call operator, something like ‘**base=16**’, is called a *keyword argument*.

[3]{.ws}[func]{.stx} [(]{.cc} [parm-name]{.stx}[=]{.cc}[expr]{.stx} [)]{.cc} `  `{.ws} []{.lar} *keyword argument*

[p-fn-int]:
   https://docs.python.org/3/library/functions.html#int 
   "Python Built-in Functions — int()"
[w-arb-prec]:
   https://en.wikipedia.org/wiki/Arbitrary-precision_arithmetic
   "Wikipedia — Arbitrary-Precision Arithmetic"
[w-integer]:
   https://en.wikipedia.org/wiki/Integer_(computer_science)
   "Wikipedia — Integer (computer science)"
[p-tp-int-bit_count]:
   https://docs.python.org/3/library/stdtypes.html#int.bit_count
   "Python Standard Types — int # ‹int›.bit_count()"
[p-tp-int-from_bytes]:
   https://docs.python.org/3/library/stdtypes.html#int.from_bytes
   "Python Standard Types — int # int.from_bytes()"

## Floating-Point Type

For situations where integers are not sufficient, as with physical data like distance, mass, velocity, etc., we have the [[float]{.cc}][p-fn-float] type. [Floating-point][w-float] types support typical arithmetic operators like multiplication (&hairsp;[*]{.cc}&hairsp;), addition ([+]{.cc}), subtraction (&hairsp;[-]{.cc}&hairsp;), and division (&hairsp;[/]{.cc}&hairsp;), and floor division ([&hairsp;//&hairsp;]{.cc}).

Like [integers](#integer-type), a [[float]{.cc}][p-fn-float] object have methods and attributes, for example:

[3]{.ws}[float]{.stx}[.]{.cc}[[hex(&hairsp;)]{.cc}][p-tp-float-hex] \ \  []{.lar} to hexadecimal representation.\
[3]{.ws}[[float]{.cc}][p-fn-float][.]{.cc}[[fromhex('…')]{.cc}][p-tp-float-fromhex] \ \  []{.lar} from hexadecimal represention.

Try [[help]{.cc}][p-fn-help][(float.hex)]{.cc} for example, to see the documentation.

Most of the functions in the standard [[math]{.cc} module][p-lib-math] has many function that require [[float]{.cc}][p-fn-float]s as arguments, and return results of type [[float]{.cc}][p-fn-float]. It also has some mathematical constants like [pi]{.cc} (π).

```py
>> import math
>> r = 1.23
>> a = math.pi * r**2        #← A = ¶r²
>> print(f"Area: {a:.4f}")   #▷ Area: 4.7529
```

We shall see a lot more of [[float]{.cc}][p-fn-float] later.

[w-float]:
   https://en.wikipedia.org/wiki/Floating-point_arithmetic
   "Wikipedia — Floating-Point Arithmetic"
[p-tp-float-hex]:
   https://docs.python.org/3/library/stdtypes.html#float.hex
   "Python Standard Types — float # hex()"
[p-tp-float-fromhex]:
   https://docs.python.org/3/library/stdtypes.html#float.fromhex
   "Python Standard Types — float # fromhex()"
[p-lib-math]:
   https://docs.python.org/3/library/math.html
   "Python Library — math Module"

## Complex Types

If your application requires [complex][w-complex] mathematics, Python has got you covered with the built-in [[complex]{.cc}][p-fn-complex] type. A complex number has [real]{.cc} and [imag]{.cc}inary parts. The normal arithmetic operators will perform complex arithmetic as expected.

A [[complex]{.cc}][p-fn-complex] object will have [real]{.cc} and [imag]{.cc}(inary) attributes.

:::{.cli prompt='>>'}
###### `repl` — Complex numbers examples
 * ``c = complex(3, 4)       #← 3+4i or ‘3+4j’ in Python.``{.py .ws}
 * ``c = 3+4j                #← same value, but as literal.``{.py .ws}
 * ``print(c)                #▷ (3+4j)``{.py .ws}
 * ``import math as m``{.py .ws}
 * ``m.hypot(c.real, c.imag) #▷ 5.0``{.py .ws}
:::

[w-complex]:
   https://en.wikipedia.org/wiki/Complex_number
   "Wikipedia — Complex Number"
[p-fn-complex]:
   https://docs.python.org/3/library/functions.html#complex
   "Python Built-In Functions — complex()"

# String Type

Programmer spend a *lot* of time manipulating [strings][w-string]. It should be no surprise that Python provides the [[str]{.cc}][p-fn-str] type to represent string objects. Strings are [immutable][w-immutable] — once created, the content cannot be modified. This is a safety measure, and also aid efficiency under certain circumstances.

## Immutability

A consequence of immutability, is that none of the instance methods of type [[str]{.cc}][p-fn-str] will be able to modify the original string — but will return a *new* copy of the string with possible modifications applied.

:::{.cli prompt='>>'}
###### `repl` — String immutability demo
 * ``s = "abcdef"``{.py .ws}
 * ``s.upper()                  #← does not change `s`.``{.py .ws}
 * ``s = s.upper()              #← that's how to do it.``{.py .ws}
:::

The reason for immutability is for efficiency, and fewer chances of being surprised by results. Strings are use a lot in programs, so although not apparent, their immutability makes for better programs.

## Encodings

Python can support several string [encodings][w-chr-enc], but the internal and default representation make it easy to convert to/from [UTF-8][w-utf8]. Your Python source files should also be in UTF-8 encoding, as a matter of good convention.

Python also supports *byte strings* of type [[bytes]{.cc}][p-fn-bytes], which are not treated as UTF-8, but is useful when converting to/from UTF-8 and some other encoding. Python makes it simple to work with strings — most of the time, it ‘just works’.

:::{.cli prompt='>>'}
###### `repl` — String encoding and UTF-8
 * ``string = 'Hello, World!'          #← internal representation.``{.py .ws}
 * ``encoded = string.encode('utf-8')``{.py .ws}
 * ``print(encoded)                    #▷ b'Hello, World!'``{.py .ws}
 * ``decoded = encoded.decode('utf-8')``{.py .ws}
 * ``print(decoded)                    #▷ Hello, World!``{.py .ws}
 * ``type(encoded)                     #▷ <class 'bytes'>``{.py .ws}
:::

As we mentioned above, any object can be ‘converted’ to a string representation by passing it to the [[str]{.cc}][p-fn-str] function.

## Regular Expressions 

The [[str]{.cc}][p-fn-str] class defines *many* string-manipulation functions. Strings are also often used with the methods and classes of the Standard Library's [[re]{.cc} module][p-lib-re], which implement [regular expression][w-regex] pattern matching. There is also the third party [[regex]{.cc} module][pypi-regex] with even more regular expression support.

Two major [[re]{.cc}][p-lib-re] methods are [[match()]{.cc}][p-lib-re-match] which matches a pattern at the *beginning* of a string, and [[search()]{.cc}][p-lib-re-search] tries to match *anywhere* in the string.

:::{.cli prompt='>>'}
###### `repl` — Regular expressions and re module
 * ``import re``{.py .ws}
 * ``print(re.match("ABC", "ABCDEFG"))``{.py .ws}
 [\<re.Match object; span=(0, 3), match='ABC'\>]{.output}
 * ``print(re.match("DEF", "ABCDEFG"))``{.py .ws}
[None]{.output}
 * ``print(re.search("ABC", "ABCDEFG"))``{.py .ws}
[\<re.Match object; span=(0, 3), match='ABC'\>]{.output}
 * ``print(re.search("DEF", "ABCDEFG"))``{.py .ws}
[\<re.Match object; span=(3, 6), match='DEF'\>]{.output}
:::

The [[str]{.cc}][p-fn-str] methods [[split()]{.cc}][p-tp-str-split] and [[replace()]{.cc}][p-tp-str-replace] can also use regular expression for very flexible string splitting base on complex delimiters, and sophisticated search-and-replace operations.

[p-lib-re-match]:
   https://docs.python.org/3/library/re.html#re.match
   "Python Library — re.match()"
[p-lib-re-search]:
   https://docs.python.org/3/library/re.html#re.search
   "Python Library — re.search()"
[p-tp-str-split]:
   https://docs.python.org/3/library/stdtypes.html#str.split
   "Python Library — str.split()"
[p-tp-str-replace]:
   https://docs.python.org/3/library/stdtypes.html#str.replace
   "Python Library — str.replace()"

## String Formatting

The [[str]{.stx}[.format]{.cc}][p-tp-str-fmt] allows us to [format][p-strfmt-stx] strings in a multitude of ways. It is newer and more flexible than the older ‘printf-style’ formatting familiar to C programmers which *overloads* the [%]{.cc} (modulus) operator to perform the formatting. From Python 3.6, a much better option is available in the form of *formatted string literals*, or just [f-strings][p-lex-fstr] for short.

### Printf-Style

The **`%`** overloaded operator is inspired by the C [[printf]{.cc}][w-c-printf] function. A ‘format string’ contains ‘placeholders’ starting with the percentage sign. Following the [%]{.cc}, are *format specifiers*. The placeholder is replaced with the formatted string representation of an [expr]{.stx}ession.

[3]{.ws}["]{.cc}…[%]{.cc}[specifier]{.stx}…["]{.cc} &nbsp; [%]{.cc} &nbsp; [expr]{.stx}

:::{.cli prompt='>>'}
 * ``name = "ABC"``{.py .ws}
 * ``age = 123``{.py .ws}
 * ``result = "Name: %s (%dy)" % (name, age)``{.py .ws}
 * ``print(result)``{.py .ws}
[Name: ABC (123y)]{.output}
 * ``print("Name: %s (%dy)" % (name, age))``{.py .ws}
[Name: ABC (123y)]{.output}
:::

### Format Method

The [[str]{.cc}][p-fn-str][.]{.cc}[[format]{.cc}][p-tp-str-fmt] method also has placeholders which are replaced with a formatted string representation of some [expr]{.stx}ession. The placeholders are in the form of matching curly braces: [{]{.cc} … [}]{.cc}. To actually produce curly braces, they must be doubled up: [{{]{.cc} and/or [}}]{.cc}.

[3]{.ws}["]{.cc}…[{&hairsp;}]{.cc}…[".format(]{.cc} [expr]{.stx} [)]{.cc}

:::{.cli prompt='>>'}
###### `repl` — String formatting method
 * ``name = "ABC"``{.py .ws}
 * ``age = 123``{.py .ws}
 * ``result = "Name: {} ({}y)".format(name, age)``{.py .ws}
 * ``print(result)``{.py .ws}
[Name: ABC (123y)]{.output}
 * ``print("Name: {} ({}y)".format(name, age))``{.py .ws}
[Name: ABC (123y)]{.output}
:::


### Format Literals

The Python 3.6 formatted string literals allows for a more compact syntax compared to the [format method above](#format-method). It is less error-prone and highly recommended. The big difference is that strings must start with an [f]{.cc} prefix, and that inside the curly braces, any [expr]{.stx}ession can appear — this is called [string interpolation][w-str-inter] in many languages.

:::{.cli prompt='>>'}
###### `repl` — Formatted string literals{#repl-f-strings}
 * ``name = "ABC"``{.py .ws}
 * ``age = 123``{.py .ws}
 * ``result = f"Name: {name} ({age}y)"``{.py .ws}
 * ``print(result)``{.py .ws}
 [Name: ABC (123y)]{.output}
 * ``print(f"Name: {name} ({age}y)")``{.py .ws}
 [Name: ABC (123y)]{.output}
:::

We call such strings *f-strings* for short. They use the same ‘formatting language’ as [[str]{.cc}][p-fn-str][.]{.cc}[[format]{.cc}][p-tp-str-fmt] for the [expr]{.stx}essions between the curly braces.

[w-string]:
   https://en.wikipedia.org/wiki/String_(computer_science)
   "Wikipedia — String (computer science)"
[w-immutable]:
   https://en.wikipedia.org/wiki/Immutable_object
   "Wikipedia — Immutable Object"
[w-chr-enc]:
   https://en.wikipedia.org/wiki/Character_encoding
   "Wikipedia — Character Encoding"
[w-utf8]:
   https://en.wikipedia.org/wiki/UTF-8
   "Wikipedia — UTF-8"
[p-fn-bytes]:
   https://docs.python.org/3/library/functions.html#func-bytes
   "Python Built-In Functions — bytes()"
[p-lib-re]:
   https://docs.python.org/3/library/re.html#module-re
   "Python Library — re Module"
[w-regex]:
   https://en.wikipedia.org/wiki/Regular_expression
   "Wikipedia — Regular Expression"
[pypi-regex]:
   https://pypi.org/project/regex/
   "PyPI — regex"
[p-tp-str-fmt]:
   https://docs.python.org/3/library/stdtypes.html#str.format
   "Python Types — ‹str›.format()"
[p-strfmt-stx]:
   https://docs.python.org/3/library/string.html#formatstrings
   "Python Library — Format String Syntax"
[p-lex-fstr]:
   https://docs.python.org/3/reference/lexical_analysis.html#f-strings
   "Python Lexical Analysis — Formatted String Literals"
[w-c-printf]:
   https://en.wikipedia.org/wiki/Printf_format_string
   "Wikipedia — printf Format String"
[w-str-inter]:
   https://en.wikipedia.org/wiki/String_interpolation
   "Wikipedia — String Interpolation"
[py-lib-re-match]:
   https://docs.python.org/3/library/re.html#re.match
   "Python Library — re # re.match()"
[py-lib-re-search]:
   https://docs.python.org/3/library/re.html#re.search
   "Python Library — re # re.search()"

