It takes all sorts… of types to work with data. Languages like Python abstracts a type as an attribute of all values. It's a way to say ‘every value or *object*, has a [type]{.stx}’. Without a basic understanding of types, you will be limited with what you can do with Python.

# Type Foundations

Python has a fair number of [built-in types][p-lib-stdtypes], but you do not have to learn them all at once. The most important initial types are [**bool**][p-fn-bool] for [boolean][w-boolean] values, [**str**][p-fn-str] for [strings][w-string], [**int**][p-fn-int] for [integers][w-integer], and [**float**][p-fn-float] for [double-precision][w-dp-float] floating-point values. We might throw in a [**None**][p-lit-none] here and there, but won't make a habit of it — it has type [**NonType**](##).

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

However, you can think of a class as being analogous to a house *plan*. A physical house does not exist, but we can learn much about a future house from the plan. We can build or ‘instantiate’ several houses from the same plan. We can say that these physical house objects are *instances* of the house plan.

House plan **B** can borrow or [inherit][w-inherit] from some other house plan **A**, and *extend* the borrowed plan by, for example, adding an extension or extra room. A **B**-type house, will have characteristics common to houses build from an **A**-type plan.

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

An *instance* is just a value, having a particular type, stored somewhere in memory, often called an object. So, really, whether you say *instance*, *value*, *object*, or *expression*, it turns out to be the same thing. People create these synonyms just to discourage you from learning anything.

Any object will have a [type]{.stx}, and a [value]{.stx}. The value of an object may have a selection of [attributes][w-attrib], and [methods][w-method], which are determined by its class.

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

A [method][w-method] is a function that can be called. But unlike [built-in][p-fn] functions which can be called at any time, a method can only be called ‘on an object’. This is a way to say that an [obj]{.stx}ject must first exits, before we can call a [method]{.stx}. And not any method, only methods that are specified by the [type]{.stx} of the object.

We use the ‘dot operator (**.**)’, which some other languages call the ‘member-selection operator’, to ‘pick’ attributes or methods. To call a method (or function), we need the function call operator: **()**, which may enclosed [arg]{.stx}uments, depending on the definition of the method. Multiple arguments are separated by commas (**,**).

&nbsp;&nbsp;&nbsp;&nbsp; [obj]{.stx} **.** [method]{.stx} **()**<br/>
&nbsp;&nbsp;&nbsp;&nbsp; [obj]{.stx} **.** [method]{.stx} **(** [arg]{.stx} **)**<br/>
&nbsp;&nbsp;&nbsp;&nbsp; [obj]{.stx} **.** [method]{.stx} **(** [arg₁]{.stx}**,** [arg₂]{.stx}, … [arg<sub>n</sub>]{.stx} **)**

In the example Python code below, `123` is an object of type [**int**][p-fn-int]. The [**int**][p-fn-int] class defines methods like [**bit_length()**][p-tp-int-bitlen], which we can thus call ‘on the object `123`’. We need parentheses around the `123`, otherwise the dot operator will be confused with the decimal point. If we associated a name like `var` to `123`, the parentheses will not be needed.

```py
$> (123).bit_count()                #→ 6
$> var = 123                        #← `var` ≡ `123`
$> var.bit_count()                  #→ 6
```

We can document the fact that [**int**][p-fn-int] objects have a [**bit_length()**][p-tp-int-bitlen] method like this, where [int]{.stx} means ‘an object of type [**int**][p-fn-int]’:

&nbsp;&nbsp;&nbsp;&nbsp; [int]{.stx} **.** [**bit_length()**][p-tp-int-bitlen]

Unfortunately, the Python documentation is not so clear on this, which might be confusing until you understand the authors' conventions.

Not all methods require an [obj]{.stx}ect; some are *class methods*, which means that we can call them ‘on the class’ or on an object of the same type. An example would be [**int**][p-fn-int]**.**\[**from_bytes()**][p-tp-int-frombyte], which we can specify like this:

&nbsp;&nbsp;&nbsp;&nbsp; [**int**][p-fn-int] **.** [**from_bytes(…)**][p-tp-int-frombyte] 

```py
$> (123).from_bytes(b'\x02\x10', byteorder='big')  #→528
$> int.from_bytes(b'\x02\x10', byteorder='big')    #→528
```

The [**int**][p-fn-int]**.**\[**from_bytes(…)**][p-tp-int-frombyte] method requires arguments.

[p-fn]:
   https://docs.python.org/3/library/functions.html#
   "Python Reference — Built-in Functions"
[p-tp-int-bitlen]:
   https://docs.python.org/3/library/stdtypes.html#int.bit_length
   "Python Reference — Standard Types # ‹int›.bit_length()"
[p-tp-int-frombyte]:
   https://docs.python.org/3/library/stdtypes.html#int.from_bytes
   "Python Reference — Standard Types # classmethod int.from_bytes()"

### Attributes

Members that are not methods, are called [attributes][w-attrib]. Think of attributes as rooms in a house. Given two houses built from the same plan: they will have the same number of rooms (attributes), but they may not have the same *content* (e.g., furniture).

So, two objects with the same type, will have the same attributes, as defined by their class, but each instance of the common attributes, may have different values. Unless a class prevents it explicitly, we can add instance attributes to any object, at any time:

```py
$> class C: pass            #← user-defined type called `C`.
$> cobj = C()               #← create object and assign `cobj` name.
$> cobj.name = "C Object"   #← create instance attribute `name`.
$> cobj.value = 123.456     #← create instance attribute `value`.
```

Do not worry too much about the detail above… we just want you at this stage, to get ‘a feel’ for the terminology, and in this case: *attributes*.

### Member Listing

We can use the following function to display the (important) members of any object. It will indicate whether the member is an attribute, or method. It uses the [**callable**][p-fn-callable] and [**getattr**][p-fn-getattr] built-in functions.

<a id="members.py"></a>
#### **py** — *List attributes function*
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

If you were to run the above function with: `members(int)`, you would get:

```
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

And, you can of course simply run [**help(int)**][p-fn-help] or [**dir(int)**][p-fn-dir] in a REPL for all the necessary information about all the members. The [**members()**](#members.py) function can be enhanced to also determine whether a member is an *instance* member, or a *class* member, but we shall leave that for later.

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

The most important ability all objects of all types inherits from [**object**][p-fn-obj], is the conversion to [string](#strings) ([**str**][p-fn-str]). This means you can pass any object to [**str**][p-fn-str], or for that matter: [**repr**][p-fn-repr], and you will obtain a string representation of the object.

```py
>> str(123)        #→ 123
>> str(1.23)       #→ 1.23
>> str(str)        #→ <class 'str'>
>> str(type)       #→ <class 'type'>
```

The [**repr**][p-fn-repr] will show the output the way you would normally *represent* the value in Python syntax.

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

To confuse the issue of types a little more, Python has a [type]{.stx} called [**type**][p-fn-type], which can be used to determine the type of any object passed as argument. When the result is converted to a string (automatically or explicitly), you will get the name of the type.

```py
>> type(type)                    #→ type
>> type(int)                     #→ type
>> type(str)                     #→ type
>> type(0)                       #→ int
>> type(0.0)                     #→ float
>> type(True)                    #→ bool
>> type("")                      #→ str
>> type('')                      #→ str
```

Note that the CPython REPL will output `class ‹type›`, while IPython will output just `‹type›`. And, if you want to output the result in a script, you have to use **print**.

Whenever you are in doubt regarding the [type]{.stx} of an [expr]{.stx}ession, do:

&nbsp;&nbsp;&nbsp;&nbsp; **print( type(** [expr]{.stx} **) )**

The extra spaces have no effect… we just added them for readability.

[p-fn-type]:
   https://docs.python.org/3/library/functions.html#type
   "Python Built-in Functions ­— type()"
[p-fn-print]:
   https://docs.python.org/3/library/functions.html#print
   "Python Built-in Functions — print()"

## Truth

Unlike human societies (and AI to some extend), computer languages have no ‘grey areas’ or ‘false news’ — it's all zeros and ones, which we abstract with Python as [**False**][p-lit-false] or [**True**][p-lit-true] keywords respectively. Values that represent ‘truth’ have type [**bool**][p-fn-bool] (boolean), and can only be only one of these two values.

### Truth Conversion

The [**bool**][p-fn-bool] (boolean) type in Python, like all types, is a *function*. It can be used to create *boolean* values. If called without an argument, it will create the boolean value [**False**][p-lit-false].

Absolutely *any* value of *any* type, can be converted to boolean. This conversion is based on [rules][p-truth]. Almost any value converted to [**bool**][p-fn-bool], will result in [**True**][p-lit-true] except for the following:

 * [**None**][p-lit-none] and [**False**][p-lit-false];
 * [Numerical][p-tp-nums] values that are zero:
   * [**0**][p-fn-int] — integer or [**int**][p-fn-int]
   * [**0.0**][p-fn-float] — floating-point or [**float**][p-fn-float]
   * [**0j**][p-fn-complex] — complex or [**complex**][p-fn-complex]
   * [**Decimal(0)**][p-lib-decimal] — fixed/floating point, useful for currency
   * [**Fraction(0,1)**][p-lib-fraction] — fractions
 * Empty collections or *sequences*:
   * [**''**][p-fn-str] or [**""**][p-fn-str] — empty strings or [**str()**][p-fn-str]
   * [**()**][p-fn-tuple] — empty tuples or [**tuple**][p-fn-tuple]
   * [**[]**][p-fn-list] — empty lists or [**list**][p-fn-list]
   * [**{}**][p-fn-dict] — empty dictionaries or [**dict**][p-fn-dict]
   * [**set()**][p-fn-set] — empty sets
   * [**range(0)**][p-fn-range] — empty ranges

```py
>> bool()                                  #→ False
>> bool(0)   ; bool(0.0) ; bool(0j)        #→all `False`.
>> bool('')  ; bool("")  ; bool(())        #→all `False`.
>> bool([])  ; bool({})  ; bool(set())     #→all `False`.
```

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

There are parts of Python syntax that require [**bool**][p-fn-bool]ean values ([expr]{.stx}essions) as part of the syntax. Some operators, like the [logical operators][p-expr-boolops], also require operands of [type]{.stx} [**bool**][p-fn-bool].

If the [type]{.stx} of an [expr]{.stx}ession is not [**bool**][p-fn-bool] wherever Python expects it, the interpreter will *automatically* or *implicitly*, call the [**bool**][p-fn-bool] function to convert the [expr]{.stx}ession to boolean.

This is one very fundamental truth in Python: **everything is implicitly convertible to boolean**.

Initially, it seems to make no sense that **[bool][p-fn-bool]("ABC")** or **[bool][p-fn-bool](123)** to have the value [**True**][p-lit-true], and **[bool][p-fn-bool](0)** to result in [**False**][p-lit-false]. Practical uses of this inescapable truth, will become more apparent later as we explore more Python syntax.

[p-expr-boolops]:
   https://docs.python.org/3/reference/expressions.html#boolean-operations
   "Python Expressions — 6.11 Boolean Operations"

# Arithmetic Types

It should be no surprise that Python provides good support for arithmetic of several kinds. It even implements [arbitrary-precisions][w-arb-prec] arithmetic on integers.

## Integer Type

Python provides the [**int**][p-fn-int] type to represents integer values. [Integers][w-integer] are whole numbers without a fractional part, that are useful in situations where floating point would be overkill. Operations on integers are generally faster than floating point operations.

Since all types in Python are classes, this means that an [**int**][p-fn-int] value is an *object*. In turn, an [**int**][p-fn-int] object will have [methods][w-method], and [attributes][w-attrib]. Some [method]{.stx}s take [arg]{.stx}uments, which are sometimes optional:

&nbsp;&nbsp;&nbsp;&nbsp; [obj]{.stx}**.**[method]{.stx}**(** [ [arg]{.stx}…  ] **)**

An example would be the [**bit_count**][p-tp-int-bit_count] method, which is an *instance* method, which means we first need an [**int**][p-fn-int] object. We can document the syntax as:

&nbsp;&nbsp;&nbsp;&nbsp; [int]{.stx}**.**\[**bit_count()**][p-tp-int-bit_count]

On the other hand, the [**from_bytes**][p-tp-int-from_bytes] method is a *class method*, which means we do not (necessarily) need an [**int**][p-fn-int] object in order to call it. Syntax-wise, we show it as:

&nbsp;&nbsp;&nbsp;&nbsp; [**int**][p-fn-int]**.**\[**from_bytes(…)**][p-tp-int-from_bytes]

The [**int**][p-fn-int] function accepts an optional argument, or one argument, or two arguments. It can be used to truncate [**float**][p-fn-float] values and return only the integer part. But, it can be passed a [**str**][p-fn-str]ing type argument, which will be ‘converted’ to an [**int**][p-fn-int]… as long as the characters in the string ‘looks like an integer’.

&nbsp;&nbsp;&nbsp;&nbsp; [**int()**][p-fn-int]<br/> 
&nbsp;&nbsp;&nbsp;&nbsp; [**int(** [arg]{.stx} **)**][p-fn-int]<br/> 
&nbsp;&nbsp;&nbsp;&nbsp; [**int(** [arg]{.stx}**, base=**[base]{.stx}**)**][p-fn-int]

Note that **"123"** has type [**str**][p-fn-str]ing, and **123** has type [**int**][p-fn-int], which has an effect on an operator like __*__ (asterisk), which can have different behaviour depending on the types of the operands:

```py
>> 123 * 2              #→ 246      — int * int ≡ multiplication
>> int("123") * 2       #→ 246      — int * int ≡ multiplication
>> "123" * 2            #→ 123123   — str * int ≡ string repetition
>> 2 * "123"            #→ 123123   — int * str ≡ string repetition
```

If the string representation of the argument is in base 2 (binary), you must pass a [**base**](##) argument ([**2**](##)). Similar for base 8 (octal), and base 16 (hexadecimal). The literal prefixes are not necessary, but allowed:

```py
>> int("1111011", 2)       #→ 123
>> int("0b1111011", 2)     #→ 123
>> int("1111011", base=2)  #→ 123
>> int("0x7b", 16)         #→ 123
>> int("7B", base=16)      #→ 123
```

You can pass arguments as a single [expr]{.stx}ession, or by naming the argument, using the name of the parameter as documented — Python call this ‘keyword argument’ syntax. There is a reason for this naming, but is unfortunately not readily apparent from above. Just try to remember that inside a function call operator, something like ‘**base=16**’, is called a *keyword argument*.

&nbsp;&nbsp;&nbsp;&nbsp; [func]{.stx} **(** [parm-name]{.stx}**=**[expr]{.stx} **)** &nbsp;&nbsp; ← keyword argument

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

For situations where integers are not sufficient, as with physical data like distance, mass, velocity, etc., we have the [**float**][p-fn-float] type. [Floating-point][w-float] types support typical arithmetic operators like multiplication (__*__), addition (**+**), subtraction (**-**), and division (**/**).

Like [integers](#integer-type), a [**float**][p-fn-float] object have methods and attributes, for example:

&nbsp;&nbsp;&nbsp;&nbsp; [float]{.stx}**.**\[**hex()**][p-tp-float-hex] &nbsp;&nbsp; ← to hexadecimal representation.<br/>
&nbsp;&nbsp;&nbsp;&nbsp; [**float**][p-fn-float]**.**\[**fromhex()**][p-tp-float-fromhex] &nbsp;&nbsp; ← from hexadecimal represention.

Try [**help**][p-fn-help]**(float.hex)** for example, to see the documentation.

Most of the functions in the standard [**math** module][p-lib-math] has many function that require [**float**][p-fn-float]s as arguments, and return results of type [**float**][p-fn-float]. It also has some mathematical constants like **pi** (π).

```py
>> import math
>> r = 1.23
>> a = math.pi * r**2        #← A = ¶r²
>> print(f"Area: {a:.4f}")   #→ Area: 4.7529
```

We shall see a lot more of [**float**][p-fn-float] later.

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

If your application requires [complex][w-complex] mathematics, Python has got you covered with the built-in [**complex**][p-fn-complex] type. A complex number has **real** and **imag**inary parts. The normal arithmetic operators will perform complex arithmetic as expected.

A [**complex**][p-fn-complex] object will have **real** and **imag**(inary) attributes.

```py
>> c = complex(3, 4)       #← 3+4i or ‘3+4j’ in Python.
>> c = 3+4j                #← same value, but as literal.
>> print(c)                #→ (3+4j)
>> import math as m
>. m.hypot(c.real, c.imag) #→ 5.0
```

[w-complex]:
   https://en.wikipedia.org/wiki/Complex_number
   "Wikipedia — Complex Number"
[p-fn-complex]:
   https://docs.python.org/3/library/functions.html#complex
   "Python Built-In Functions — complex()"

# String Type

Programmer spend a *lot* of time manipulating [strings][w-string]. It should be no surprise that Python provides the [**str**][p-fn-str] type to represent string objects. Strings are [immutable][w-immutable] — once created, the content cannot be modified. This is a safety measure, and also aid efficiency under certain circumstances.

## Immutability

A consequence of immutability, is that none of the instance methods of type [**str**][p-fn-str] will be able to modify the original string — but will return a *new* copy of the string with possible modifications applied.

```py
>> s = "abcdef"
>> s.upper()                  #← does not change `s`.
>> s = s.upper()              #← that's how to do it.
```

## Encodings

Although Python can support several string [encoding][w-chr-enc], but the internal and default representation make it easy to convert to/from [UTF-8][w-utf8]. Your Python source files should also be in UTF-8 encoding, as a matter of good convention.

Python also supports *byte strings* of type [**bytes**][p-fn-bytes], which are not treated as UTF-8, but is useful when converting to/from UTF-8 and some other encoding. Python makes it simple to work with strings — most of the time, it ‘just works’.

```py
>> string = 'Hello, World!'          #← internal representation.
>> encoded = string.encode('utf-8')
>> print(encoded)                    #→ b'Hello, World!'
>> decoded = encoded.decode('utf-8')
>> print(decoded)                    #→ Hello, World!
>> type(encoded)                     #→ <class 'bytes'>
```

As we mentioned above, any object can be ‘converted’ to a string representation by passing it to the [**str**][p-fn-str] function.

## Regular Expressions 

The [**str**][p-fn-str] class defines *many* string-manipulation functions. Strings are also often used with the methods and classes of the Standard Library's [**re** module][p-lib-re], which implement [regular expression][w-regex] pattern matching. There is also the third party [**regex** module][pypi-regex] with even more regular expression support.

Two major [**re**][p-lib-re] methods are [**match()**][p-lib-re-match] which matches a pattern at the *beginning* of a string, and [**search()**][p-lib-re-search] tries to match *anywhere* in the string.

```py
>> import re
>> print(re.match("ABC", "ABCDEFG"))
#→ <re.Match object; span=(0, 3), match='ABC'>
>> print(re.match("DEF", "ABCDEFG"))
#→ None 
>> print(re.search("ABC", "ABCDEFG"))
#→ <re.Match object; span=(0, 3), match='ABC'>
>> print(re.search("DEF", "ABCDEFG"))
#→ <re.Match object; span=(3, 6), match='DEF'> 
```

The [**str**][p-fn-str] methods [**split()**][p-tp-str-split] and [**replace()**][p-tp-str-replace] can also use regular expression for very flexible string splitting base on complex delimiters, and sophisticated search-and-replace operations.

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

The [[str]{.stx}**.format**][p-tp-str-fmt] allows us to [format][p-strfmt-stx] strings in a multitude of ways. It is newer and more flexible than the older ‘printf-style’ formatting familiar to C programmers which *overloads* the **%** (modulus) operator to perform the formatting. From Python 3.6, a much better option is available in the form of *formatted string literals*, or just [f-strings][p-lex-fstr] for short.

### Printf-Style

The **`%`** overloaded operator is inspired by the C [**printf**][w-c-printf] function. A ‘format string’ contains ‘placeholders’ starting with the percentage sign. Following the **%**, are *format specifiers*. The placeholder is replaced with the formatted string representation of an [expr]{.stx}ession.

&nbsp;&nbsp;&nbsp;&nbsp;**"**…**%**[specifier]{.stx}…**"** &nbsp; **%** &nbsp; [expr]{.stx}

```py
>> name = "ABC"
>> age = 123
>> result = "Name: %s (%dy)" % (name, age)
>> print(result)
#→ Name: ABC (123y)
>> print("Name: %s (%dy)" % (name, age))
#→ Name: ABC (123y)
```

### Format Method

The [**str**][p-fn-str]**.**\[**format**][p-tp-str-fmt] method also has placeholders which are replaced with a formatted string representation of some [expr]{.stx}ession. The placeholders are in the form of matching curly braces: **{** … **}**. To actually produce curly braces, they must be doubled up: **{{** and/or **}}**.

&nbsp;&nbsp;&nbsp;&nbsp;**"**…{}…**".format(** [expr]{.stx} **)**

```py
>> name = "ABC"
>> age = 123
>> result = "Name: {} ({}y)".format(name, age)
>> print(result)
#→ Name: ABC (123y)
>> print("Name: {} ({}y)".format(name, age))
#→ Name: ABC (123y)
```

### Format Literals

The Python 3.6 formatted string literals allows for a more compact syntax compared to the [format method above](#format-method). It is less error-prone and highly recommended. The big difference is that strings must start with an **f** prefix, and that inside the curly braces, any [expr]{.stx}ession can appear — this is called [string interpolation][w-str-inter] in many languages.

```py
>> name = "ABC"
>> age = 123
>> result = f"Name: {name} ({age}y)"
>> print(result)
#→ Name: ABC (123y)
>> print(f"Name: {name} ({age}y)")
#→ Name: ABC (123y)
```

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
